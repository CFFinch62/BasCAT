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

        # Logic operations
        "AND": 0x05,   # AND Reg, Reg/Value
        "OR": 0x06,    # OR Reg, Reg/Value
        "XOR": 0x07,   # XOR Reg, Reg/Value
        "NOT": 0x08,   # NOT Reg

        # Comparison and branching
        "CMP": 0x09,   # CMP Reg, Reg/Value - Compare and set flags
        "JMP": 0x10,   # JMP Address
        "JZ": 0x11,    # JZ Address - Jump if Zero
        "JNZ": 0x12,   # JNZ Address - Jump if Not Zero
        "JC": 0x13,    # JC Address - Jump if Carry
        "JNC": 0x14,   # JNC Address - Jump if Not Carry

        # Stack operations
        "PUSH": 0x20,  # PUSH Reg
        "POP": 0x21,   # POP Reg

        # Memory operations
        "LDM": 0x30,   # LDM Reg, [addr] - Load from memory
        "STM": 0x31,   # STM [addr], Reg - Store to memory

        # I/O operations
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
        Two-pass assembler: Pass 1 finds labels, Pass 2 generates code.
        Returns (byte_list, error_message, line_map)
        line_map is a dict mapping memory_address -> source_line_number
        """
        lines = source_code.splitlines()
        machine_code = []
        labels = {}  # Maps label names to addresses
        line_map = {}  # Maps memory address to source line number

        # PASS 1: Find all labels and their addresses
        current_address = 0
        for line_num, line in enumerate(lines):
            line = line.split(';')[0].strip()  # Remove comments
            if not line:
                continue

            # Check if this line is a label (ends with :)
            if line.endswith(':'):
                label_name = line[:-1].strip().upper()
                labels[label_name] = current_address
                continue

            # Count instruction size to track addresses
            parts = line.upper().replace(',', ' ').split()
            if not parts:
                continue

            op = parts[0]
            if op in Assembler.OPCODES:
                # Calculate how many bytes this instruction will take
                current_address += 1  # Opcode byte

                # Add operand bytes
                if op in ("LOAD", "CMP", "LDM", "STM", "MOV"):
                    current_address += 2  # register + value/address
                elif op in ("ADD", "SUB", "AND", "OR", "XOR", "JMP", "JZ", "JNZ", "JC", "JNC"):
                    current_address += 1  # single operand
                elif op in ("NOT", "PUSH", "POP", "OUT", "IN"):
                    current_address += 1  # single register
                # HALT and NOP have no operands

        # PASS 2: Generate machine code
        for line_num, line in enumerate(lines):
            line = line.split(';')[0].strip()  # Remove comments
            if not line:
                continue

            # Skip label definitions
            if line.endswith(':'):
                continue

            parts = line.upper().replace(',', ' ').split()
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

                elif op == "ADD" or op == "SUB":
                    # ADD/SUB Reg, Value (Immediate)
                    if len(parts) < 3:
                        return None, f"{op} requires Register and Value", {}
                    reg = parts[1]
                    val = parts[2]
                    try:
                        machine_code.append(int(val, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid value {val}", {}

                elif op == "AND" or op == "OR" or op == "XOR":
                    # Logic operations: AND/OR/XOR Reg, Value
                    if len(parts) < 3:
                        return None, f"{op} requires Register and Value", {}
                    reg = parts[1]
                    val = parts[2]
                    try:
                        machine_code.append(int(val, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid value {val}", {}

                elif op == "NOT":
                    # NOT Reg
                    if len(parts) < 2:
                        return None, "NOT requires a Register", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                elif op == "CMP":
                    # CMP Reg, Value - Compare register with value
                    if len(parts) < 3:
                        return None, "CMP requires Register and Value", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}
                    val = parts[2]
                    try:
                        machine_code.append(int(val, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid value {val}", {}

                elif op == "JMP" or op == "JZ" or op == "JNZ" or op == "JC" or op == "JNC":
                    # Jump instructions: JMP/JZ/JNZ/JC/JNC Address or Label
                    if len(parts) < 2:
                        return None, f"{op} requires an Address or Label", {}
                    addr_or_label = parts[1]

                    # Check if it's a label
                    if addr_or_label in labels:
                        machine_code.append(labels[addr_or_label] & 0xFF)
                    else:
                        # Try to parse as numeric address
                        try:
                            machine_code.append(int(addr_or_label, 0) & 0xFF)
                        except ValueError:
                            return None, f"Undefined label or invalid address: {addr_or_label}", {}

                elif op == "PUSH" or op == "POP":
                    # Stack operations: PUSH/POP Reg
                    if len(parts) < 2:
                        return None, f"{op} requires a Register", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                elif op == "LDM":
                    # LDM Reg, [addr] - Load from memory address
                    if len(parts) < 3:
                        return None, "LDM requires Register and [Address]", {}
                    reg = parts[1]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}
                    # Parse address (might be [addr] or just addr)
                    addr_str = parts[2].strip('[]')
                    try:
                        machine_code.append(int(addr_str, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid address {addr_str}", {}

                elif op == "STM":
                    # STM [addr], Reg - Store to memory address
                    if len(parts) < 3:
                        return None, "STM requires [Address] and Register", {}
                    # Parse address (might be [addr] or just addr)
                    addr_str = parts[1].strip('[]')
                    try:
                        machine_code.append(int(addr_str, 0) & 0xFF)
                    except ValueError:
                        return None, f"Invalid address {addr_str}", {}
                    reg = parts[2]
                    if reg in Assembler.REGISTERS:
                        machine_code.append(Assembler.REGISTERS[reg])
                    else:
                        return None, f"Unknown register {reg}", {}

                elif op == "MOV":
                    # MOV Dest, Source (both registers or immediate)
                    if len(parts) < 3:
                        return None, "MOV requires Destination and Source", {}
                    dest = parts[1]
                    src = parts[2]

                    if dest not in Assembler.REGISTERS:
                        return None, f"Unknown register {dest}", {}
                    machine_code.append(Assembler.REGISTERS[dest])

                    # Source can be register or immediate value
                    if src in Assembler.REGISTERS:
                        machine_code.append(0x80 | Assembler.REGISTERS[src])  # High bit = register
                    else:
                        try:
                            machine_code.append(int(src, 0) & 0x7F)  # Low 7 bits = immediate value
                        except ValueError:
                            return None, f"Invalid source {src}", {}

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
