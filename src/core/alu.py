from src.core.signals import signals

class ALU:
    """
    Arithmetic Logic Unit.
    Performs operations on 8-bit data.
    """
    def __init__(self):
        self.flags = {"Z": 0, "N": 0, "C": 0, "O": 0}  # Zero, Negative, Carry, Overflow

    def operate(self, op_code, operand_a, operand_b=0):
        """
        Executes an operation based on op_code.
        Returns the result (8-bit).
        """
        result = 0
        
        # Simple string-based opcodes for internal logic, actual CPU will use bytecodes
        if op_code == "ADD":
            res = operand_a + operand_b
            result = res & 0xFF
            self.update_flags(result, is_addition=True, op_a=operand_a, op_b=operand_b, res_raw=res)
            
        elif op_code == "SUB":
            res = operand_a - operand_b
            result = res & 0xFF
            self.update_flags(result, is_addition=False, op_a=operand_a, op_b=operand_b, res_raw=res)
            
        elif op_code == "AND":
            result = (operand_a & operand_b) & 0xFF
            self.update_flags(result)
            
        elif op_code == "OR":
            result = (operand_a | operand_b) & 0xFF
            self.update_flags(result)
            
        elif op_code == "XOR":
            result = (operand_a ^ operand_b) & 0xFF
            self.update_flags(result)
            
        elif op_code == "NOT":
            result = (~operand_a) & 0xFF
            self.update_flags(result)
            
        elif op_code == "MOV":
             # Pass through
             result = operand_b & 0xFF
        
        signals.bus_transfer.emit("ALU", "Internal Bus", result, "data")
        return result

    def update_flags(self, result, is_addition=None, op_a=0, op_b=0, res_raw=0):
        # Zero Flag
        self.flags["Z"] = 1 if result == 0 else 0

        # Negative Flag (MSB is set)
        self.flags["N"] = 1 if (result & 0x80) else 0

        # Carry Flag (Simplification)
        if is_addition is not None:
             if is_addition:
                 # Carry out of bit 7
                 self.flags["C"] = 1 if res_raw > 255 else 0
             else:
                 # Borrow (Carry is usually inverse borrow in some archs, but we'll stick to simple borrow=0/1 or carry logic)
                 # For SUB: A - B. If B > A, we wrapped.
                 self.flags["C"] = 1 if op_b > op_a else 0
        else:
            self.flags["C"] = 0

        # Overflow Flag (Signed arithmetic overflow)
        # implementation details can vary, keeping it simple for now or adding later
        self.flags["O"] = 0 # Placeholder

        # Emit signal for GUI update
        signals.flags_updated.emit(self.flags.copy())

    def add(self, a, b):
        """Convenience method for addition"""
        return self.operate("ADD", a, b)

    def subtract(self, a, b):
        """Convenience method for subtraction"""
        return self.operate("SUB", a, b)
