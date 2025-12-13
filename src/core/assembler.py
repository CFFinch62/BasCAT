class Assembler:
    """
    Simple assembler for CAL-EB.
    Supports a minimal instruction set.
    """
    OPCODES = {
        "NOP": 0x00,
        "LOAD": 0x01,  # LOAD Reg, Value
        "ADD": 0x02,   # ADD Reg, Reg/Value
        "SUB": 0x03,   # SUB Reg, Value
        "MOV": 0x04,   # MOV Dest, Source
        "JMP": 0x10,   # JMP Address
        "OUT": 0x40,   # OUT Reg - Write register to OUTPUT port (0xFE)
        "IN": 0x41,    # IN Reg - Read from INPUT port (0xFF) to register
        "HALT": 0xFF
    }
    
    # Register map
    REGISTERS = {"A": 0, "B": 1, "C": 2, "D": 3}

    @staticmethod
    def assemble(source_code):
        """
        Converts assembly source string to a list of bytes (machine code).
        Returns (byte_list, error_message, line_map)
        line_map is a dict mapping memory_address -> source_line_number
        """
        lines = source_code.splitlines()
        machine_code = []
        labels = {}
        line_map = {}  # Maps memory address to source line number

        # Pass 1: Find labels (simplified - assumption: label is "Name:")
        # Ideally we'd do strict parsing, but for now we skip label storage logic
        # and just focus on straightforward instruction parsing.

        for line_num, line in enumerate(lines):
            line = line.split(';')[0].strip().upper() # Remove comments
            if not line:
                continue
            
            parts = line.replace(',', ' ').split()
            if not parts:
                continue
                
            op = parts[0]
            if op in Assembler.OPCODES:
                # Map this memory address to the source line number
                line_map[len(machine_code)] = line_num

                opcode = Assembler.OPCODES[op]
                machine_code.append(opcode)
                
                # Handle operands (Very simplified)
                # Ideally check op type for number of args
                if op == "LOAD":
                    # LOAD A, 10 -> [0x01, 0x00 (RegA), 0x0A]
                    if len(parts) < 3:
                        return None, "LOAD requires Register and Value", {}
                    reg = parts[1]
                    val = parts[2]

                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                    try:
                        machine_code.append(int(val, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid value {val}", {}

                elif op == "ADD":
                    # ADD A, 5 (Immediate) - currently only supports adding to A
                    if len(parts) < 3:
                        return None, "ADD requires Register and Value", {}
                    reg = parts[1]
                    val = parts[2]
                    # Note: Currently ADD only works with register A in CPU
                    try:
                        machine_code.append(int(val, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid value {val}", {}

                elif op == "OUT":
                    # OUT A - Write register A to OUTPUT port
                    if len(parts) < 2:
                        return None, "OUT requires a Register", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                elif op == "IN":
                    # IN A - Read from INPUT port to register A
                    if len(parts) < 2:
                        return None, "IN requires a Register", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                elif op == "HALT":
                    pass
                    
            else:
                return None, f"Unknown Opcode: {op}", {}

        return machine_code, None, line_map
