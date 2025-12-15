"""
Code Generator for SimpleBASCAT

Converts AST to BasCAT assembly language.
"""

from typing import Dict, List, Tuple
from src.compiler.ast_nodes import *


class CodeGenerator:
    """
    Generates BasCAT assembly code from AST.
    Manages variable allocation and label generation.
    """

    # Variable memory mapping: A→0x80, B→0x81, ..., Z→0x99
    # This gives 128 bytes (0x00-0x7F) for program code
    VAR_BASE_ADDR = 0x80

    def __init__(self):
        self.assembly_lines: List[str] = []
        self.line_map: Dict[int, List[int]] = {}  # BASIC line → assembly line numbers
        self.for_stack: List[Tuple[str, int, int]] = []  # (var, start_asm_line, end_value)
        self.temp_counter = 0
        self.label_counter = 0

    def var_address(self, var_name: str) -> str:
        """Get memory address for variable as hex string (A→0x0A, B→0x0B, etc.)"""
        addr = self.VAR_BASE_ADDR + (ord(var_name) - ord('A'))
        return f"0x{addr:02X}"


    def emit(self, code: str, comment: str = ""):
        """Emit a line of assembly code"""
        if comment:
            self.assembly_lines.append(f"{code:<20} ; {comment}")
        else:
            self.assembly_lines.append(code)

    def emit_label(self, label: str):
        """Emit a label"""
        self.assembly_lines.append(f"{label}:")

    def new_label(self, prefix="L") -> str:
        """Generate unique label"""
        self.label_counter += 1
        return f"{prefix}{self.label_counter}"

    def generate(self, program: Program) -> Tuple[str, Dict[int, List[int]]]:
        """
        Generate assembly code from AST.
        Returns (assembly_code, line_map)
        """
        self.assembly_lines = []
        self.line_map = {}

        # Add header comment
        self.emit("; SimpleBASCAT Compiled Program")
        self.emit("")

        # Generate code for each statement
        for stmt in program.statements:
            # Track start of this BASIC line's assembly
            basic_line = stmt.line_number
            asm_start = len(self.assembly_lines)

            # Emit label for this line number (for GOTO targets)
            self.emit_label(f"L{basic_line}")

            self.emit("", f"BASIC line {basic_line}")
            self.generate_statement(stmt)

            # Track end of this BASIC line's assembly
            asm_end = len(self.assembly_lines)
            self.line_map[basic_line] = list(range(asm_start, asm_end))

        # Ensure program ends with HALT if not already there
        if not self.assembly_lines or not self.assembly_lines[-1].strip().startswith("HALT"):
            self.emit("HALT")

        return "\n".join(self.assembly_lines), self.line_map

    def generate_statement(self, stmt: ASTNode):
        """Generate code for a statement"""
        if isinstance(stmt, LetStatement):
            self.generate_let(stmt)
        elif isinstance(stmt, PrintStatement):
            self.generate_print(stmt)
        elif isinstance(stmt, InputStatement):
            self.generate_input(stmt)
        elif isinstance(stmt, IfStatement):
            self.generate_if(stmt)
        elif isinstance(stmt, GotoStatement):
            self.generate_goto(stmt)
        elif isinstance(stmt, ForStatement):
            self.generate_for(stmt)
        elif isinstance(stmt, NextStatement):
            self.generate_next(stmt)
        elif isinstance(stmt, RemStatement):
            self.generate_rem(stmt)
        elif isinstance(stmt, EndStatement):
            self.generate_end(stmt)
        elif isinstance(stmt, PokeStatement):
            self.generate_poke(stmt)

    def generate_let(self, stmt: LetStatement):
        """Generate LET statement: LET A = expression"""
        # Evaluate expression into register A
        self.generate_expression(stmt.expression)

        # Store result in variable's memory location
        addr = self.var_address(stmt.variable)
        self.emit(f"STM {addr}, A", f"{stmt.variable} = result")

    def generate_print(self, stmt: PrintStatement):
        """Generate PRINT statement"""
        # Evaluate expression into register A
        self.generate_expression(stmt.expression)

        # Output register A
        self.emit("OUT A", "Print value")
        
        # Output newline (ASCII 10) for traditional BASIC behavior
        self.emit("LOAD A, 0x0A", "Newline character")
        self.emit("OUT A", "Print newline")

    def generate_input(self, stmt: InputStatement):
        """Generate INPUT statement"""
        # Read input into register A
        self.emit("IN A", f"Input {stmt.variable}")

        # Store in variable's memory location
        addr = self.var_address(stmt.variable)
        self.emit(f"STM {addr}, A", f"Store in {stmt.variable}")

    def generate_if(self, stmt: IfStatement):
        """Generate IF...THEN GOTO statement"""
        condition = stmt.condition

        # Evaluate left side into A
        self.generate_expression(condition.left)

        # For comparison, we need right side as immediate value
        # If it's a simple number, use it directly
        if isinstance(condition.right, NumberLiteral):
            cmp_value = condition.right.value
        elif isinstance(condition.right, Variable):
            # Load variable first, store temporarily
            self.emit("PUSH A", "Save left side")
            addr = self.var_address(condition.right.name)
            self.emit(f"LDM A, {addr}", f"Load {condition.right.name}")
            self.emit("STM 0x64, A", "Store right side temporarily")
            self.emit("POP A", "Restore left side")
            self.emit("LDM B, 0x64", "Right side to temp")
            # For now, use immediate comparison
            # This is simplified - ideally we'd support register comparisons
            cmp_value = 0x64
        else:
            # Complex expression - evaluate and store
            self.emit("PUSH A", "Save left side")
            self.generate_expression(condition.right)
            self.emit("STM 0x65, A", "Store right value")
            self.emit("POP A", "Restore left side")
            self.emit("LDM B, 0x65", "Load right for comparison")
            cmp_value = 0x65

        # Compare A with value/memory location (format as hex)
        self.emit(f"CMP A, 0x{cmp_value:02X}", f"Compare: {condition.op}")

        # Generate appropriate conditional jump
        target_label = f"L{stmt.target_line}"

        if condition.op == '=':
            self.emit(f"JZ {target_label}", "Jump if equal")
        elif condition.op == '<>':
            self.emit(f"JNZ {target_label}", "Jump if not equal")
        elif condition.op == '<':
            self.emit(f"JC {target_label}", "Jump if less than")
        elif condition.op == '>':
            self.emit(f"JNC {target_label}", "Jump if greater than")
        elif condition.op == '<=':
            # Jump if carry OR zero
            skip_label = self.new_label("skip")
            self.emit(f"JC {target_label}", "Jump if less than")
            self.emit(f"JZ {target_label}", "or if equal")
        elif condition.op == '>=':
            # Jump if not carry OR zero
            self.emit(f"JNC {target_label}", "Jump if greater/equal")

    def generate_goto(self, stmt: GotoStatement):
        """Generate GOTO statement"""
        target_label = f"L{stmt.target_line}"
        self.emit(f"JMP {target_label}", f"GOTO {stmt.target_line}")

    def generate_for(self, stmt: ForStatement):
        """Generate FOR statement"""
        var = stmt.variable
        addr = self.var_address(var)

        # Evaluate start expression
        self.generate_expression(stmt.start_expr)
        self.emit(f"STM {addr}, A", f"{var} = start value")

        # For simplicity in v1.0, only support literal end values
        if not isinstance(stmt.end_expr, NumberLiteral):
            raise SyntaxError(f"FOR loops currently only support literal end values at line {stmt.line_number}")

        end_value = stmt.end_expr.value
        end_plus_one = end_value + 1

        # Generate loop start label
        loop_label = self.new_label("loop")
        self.emit_label(loop_label)

        # Remember this FOR loop for matching NEXT (store end+1 value directly)
        self.for_stack.append((var, loop_label, end_plus_one))

    def generate_next(self, stmt: NextStatement):
        """Generate NEXT statement"""
        if not self.for_stack:
            raise SyntaxError(f"NEXT without FOR at line {stmt.line_number}")

        var, loop_label, end_plus_one = self.for_stack.pop()

        if var != stmt.variable:
            raise SyntaxError(
                f"NEXT {stmt.variable} doesn't match FOR {var} at line {stmt.line_number}"
            )

        addr = self.var_address(var)

        # Increment loop variable
        self.emit(f"LDM A, {addr}", f"Load {var}")
        self.emit("ADD A, 1", "Increment")
        self.emit(f"STM {addr}, A", f"Store {var}")

        # Compare with end+1 value (which is now a literal, formatted as hex)
        self.emit(f"CMP A, 0x{end_plus_one:02X}", f"Compare with {end_plus_one}")

        # Jump back if not equal (continue loop)
        self.emit(f"JNZ {loop_label}", "Continue loop")

    def generate_rem(self, stmt: RemStatement):
        """Generate REM (comment) - just emit as comment"""
        self.emit("", f"REM: {stmt.comment}")

    def generate_end(self, stmt: EndStatement):
        """Generate END statement"""
        self.emit("HALT", "END")

    def generate_poke(self, stmt: PokeStatement):
        """Generate POKE statement: POKE address, value"""
        # For simple case: POKE literal_address, expression
        if isinstance(stmt.address, NumberLiteral):
            # Evaluate value into A
            self.generate_expression(stmt.value)
            # Store at literal address
            addr = stmt.address.value
            self.emit(f"STM 0x{addr:02X}, A", f"POKE {addr}")
        else:
            # Complex address expression - evaluate address, save, then value
            # Note: This is simplified; full indirect addressing would need CPU support
            self.generate_expression(stmt.address)
            self.emit("PUSH A", "Save address")
            self.generate_expression(stmt.value)
            self.emit("MOV B, A", "Value to B")
            self.emit("POP A", "Restore address")
            # For now, use a fixed temp location approach
            # This is a limitation - recommend using literal addresses
            self.emit("; POKE with variable address - limited support", "")

    def generate_expression(self, expr: ASTNode):
        """Generate code for expression, result in register A"""
        if isinstance(expr, NumberLiteral):
            self.emit(f"LOAD A, 0x{expr.value:02X}", f"Literal {expr.value}")

        elif isinstance(expr, Variable):
            addr = self.var_address(expr.name)
            self.emit(f"LDM A, {addr}", f"Load {expr.name}")

        elif isinstance(expr, PeekExpression):
            # PEEK(address) - load from memory address
            if isinstance(expr.address, NumberLiteral):
                addr = expr.address.value
                self.emit(f"LDM A, 0x{addr:02X}", f"PEEK({addr})")
            else:
                # Variable address - evaluate and use
                self.generate_expression(expr.address)
                # Note: True indirect addressing needs CPU support
                self.emit("; PEEK with variable address - limited support", "")
        elif isinstance(expr, BinaryOp):
            # Optimize for Variable op Variable case
            if isinstance(expr.left, Variable) and isinstance(expr.right, Variable):
                # Both are variables - load directly into A and B
                left_addr = self.var_address(expr.left.name)
                right_addr = self.var_address(expr.right.name)
                self.emit(f"LDM A, {left_addr}", f"Load {expr.left.name}")
                self.emit(f"LDM B, {right_addr}", f"Load {expr.right.name}")
                
                # Emit the operation: A = A op B
                if expr.op == '+':
                    self.emit("ADD A, B", "Add registers")
                elif expr.op == '-':
                    self.emit("SUB A, B", "Subtract registers")
                elif expr.op == 'AND':
                    self.emit("AND A, B", "AND registers")
                elif expr.op == 'OR':
                    self.emit("OR A, B", "OR registers")
                elif expr.op == 'XOR':
                    self.emit("XOR A, B", "XOR registers")
            else:
                # General case: evaluate left side first
                self.generate_expression(expr.left)

                # If right side is a literal, use immediate mode (format as hex)
                if isinstance(expr.right, NumberLiteral):
                    value = expr.right.value
                    hex_value = f"0x{value:02X}"
                    if expr.op == '+':
                        self.emit(f"ADD A, {hex_value}", "Add immediate")
                    elif expr.op == '-':
                        self.emit(f"SUB A, {hex_value}", "Subtract immediate")
                    elif expr.op == 'AND':
                        self.emit(f"AND A, {hex_value}", "AND immediate")
                    elif expr.op == 'OR':
                        self.emit(f"OR A, {hex_value}", "OR immediate")
                    elif expr.op == 'XOR':
                        self.emit(f"XOR A, {hex_value}", "XOR immediate")
                elif isinstance(expr.right, Variable):
                    # Variable on right, complex left - save left, load right, restore
                    self.emit("PUSH A", "Save left operand")
                    addr = self.var_address(expr.right.name)
                    self.emit(f"LDM B, {addr}", f"Load {expr.right.name}")
                    self.emit("POP A", "Restore left operand")

                    # Now emit the operation: A = A op B
                    if expr.op == '+':
                        self.emit("ADD A, B", "Add registers")
                    elif expr.op == '-':
                        self.emit("SUB A, B", "Subtract registers")
                    elif expr.op == 'AND':
                        self.emit("AND A, B", "AND registers")
                    elif expr.op == 'OR':
                        self.emit("OR A, B", "OR registers")
                    elif expr.op == 'XOR':
                        self.emit("XOR A, B", "XOR registers")
                else:
                    # Complex expression on right - not yet fully supported
                    self.emit("; Complex expression - not yet fully supported", "")

        elif isinstance(expr, UnaryOp):
            # Evaluate operand
            self.generate_expression(expr.operand)

            # Apply operator
            if expr.op == 'NOT':
                self.emit("NOT A", "Bitwise NOT")
            elif expr.op == '-':
                # Negate: 0 - A
                self.emit("PUSH A", "Save A")
                self.emit("LOAD A, 0")
                self.emit("POP B")
                self.emit("SUB A, B", "Negate")


# Example usage
if __name__ == "__main__":
    from src.compiler.lexer import Lexer
    from src.compiler.parser import Parser

    source = """10 REM Simple program
20 LET A = 5
30 LET B = 10
40 LET C = A + B
50 PRINT C
60 END
"""

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    codegen = CodeGenerator()
    assembly, line_map = codegen.generate(ast)

    print("Generated Assembly:")
    print(assembly)
    print("\nLine Mapping:")
    for basic_line, asm_lines in sorted(line_map.items()):
        print(f"BASIC {basic_line} → Assembly lines {asm_lines}")
