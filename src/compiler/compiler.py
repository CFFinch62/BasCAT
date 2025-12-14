"""
SimpleBASCAT Compiler

Main compiler interface that coordinates lexer, parser, and code generator.
"""

from typing import Tuple, Dict, List, Optional
from src.compiler.lexer import Lexer
from src.compiler.parser import Parser
from src.compiler.codegen import CodeGenerator
from src.core.assembler import Assembler


class CompilationResult:
    """Result of compilation"""
    def __init__(self, success: bool, assembly: str = "", bytecode: List[int] = None,
                 line_map: Dict[int, List[int]] = None, error: str = None):
        self.success = success
        self.assembly = assembly
        self.bytecode = bytecode or []
        self.line_map = line_map or {}
        self.error = error


class SimpleBASCATCompiler:
    """
    Complete compiler for SimpleBASCAT language.

    Workflow:
    1. Lexer: Source code → Tokens
    2. Parser: Tokens → AST
    3. Code Generator: AST → Assembly
    4. Assembler: Assembly → Bytecode
    """

    def __init__(self):
        self.last_assembly = ""
        self.last_line_map = {}

    def compile(self, source_code: str) -> CompilationResult:
        """
        Compile BASIC source code to bytecode.

        Args:
            source_code: SimpleBASCAT source code

        Returns:
            CompilationResult with success status, assembly, bytecode, and line mapping
        """
        try:
            # Stage 1: Lexical Analysis
            lexer = Lexer(source_code)
            tokens = lexer.tokenize()

            # Stage 2: Parsing
            parser = Parser(tokens)
            ast = parser.parse()

            # Stage 3: Code Generation
            codegen = CodeGenerator()
            assembly_code, line_map = codegen.generate(ast)

            # Store for later retrieval
            self.last_assembly = assembly_code
            self.last_line_map = line_map

            # Stage 4: Assembly to Bytecode
            bytecode, asm_error, asm_line_map = Assembler.assemble(assembly_code)

            if asm_error:
                return CompilationResult(
                    success=False,
                    assembly=assembly_code,
                    error=f"Assembly error: {asm_error}"
                )

            return CompilationResult(
                success=True,
                assembly=assembly_code,
                bytecode=bytecode,
                line_map=line_map
            )

        except SyntaxError as e:
            return CompilationResult(
                success=False,
                error=f"Syntax error: {str(e)}"
            )

        except Exception as e:
            return CompilationResult(
                success=False,
                error=f"Compilation error: {str(e)}"
            )

    def get_assembly(self) -> str:
        """Get the last generated assembly code"""
        return self.last_assembly

    def get_line_map(self) -> Dict[int, List[int]]:
        """Get the BASIC line → assembly line mapping"""
        return self.last_line_map


# Example usage and testing
if __name__ == "__main__":
    # Test program 1: Simple arithmetic
    program1 = """10 REM Calculate sum
20 LET A = 5
30 LET B = 10
40 LET C = A + B
50 PRINT C
60 END
"""

    # Test program 2: Input and conditional
    program2 = """10 REM Input test
20 INPUT A
30 IF A > 50 THEN GOTO 60
40 PRINT 0
50 GOTO 70
60 PRINT 1
70 END
"""

    # Test program 3: Loop
    program3 = """10 REM Count to 5
20 FOR I = 0 TO 5
30   PRINT I
40 NEXT I
50 END
"""

    compiler = SimpleBASCATCompiler()

    for i, program in enumerate([program1, program2, program3], 1):
        print(f"\n{'='*60}")
        print(f"Test Program {i}:")
        print('='*60)
        print(program)

        result = compiler.compile(program)

        if result.success:
            print("\n✓ Compilation successful!")
            print(f"\nGenerated Assembly ({len(result.assembly.splitlines())} lines):")
            print("-" * 60)
            print(result.assembly)
            print(f"\nBytecode ({len(result.bytecode)} bytes):")
            print(" ".join(f"{b:02X}" for b in result.bytecode[:20]))
            if len(result.bytecode) > 20:
                print(f" ... ({len(result.bytecode) - 20} more bytes)")
            print(f"\nLine Mapping:")
            for basic_line in sorted(result.line_map.keys())[:5]:
                asm_lines = result.line_map[basic_line]
                print(f"  BASIC line {basic_line} → Assembly lines {asm_lines}")
        else:
            print(f"\n✗ Compilation failed:")
            print(f"  {result.error}")
