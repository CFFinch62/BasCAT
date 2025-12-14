from src.core.signals import signals
from src.core.alu import ALU

class CPU:
    """
    Central Processing Unit for CAL-EB.
    """
    def __init__(self, memory):
        self.memory = memory
        self.alu = ALU()
        
        # Registers
        self.registers = {
            "A": 0, "B": 0, "C": 0, "D": 0
        }
        self.PC = 0      # Program Counter (16-bit)
        self.IR = 0      # Instruction Register (8-bit opcode)
        self.MAR = 0     # Memory Address Register (16-bit)
        self.SP = 0xFD   # Stack Pointer (starts at 253, before I/O ports at 254-255)
        
        # Internal State
        self.halted = False

    def reset(self):
        self.PC = 0
        self.IR = 0
        self.MAR = 0
        self.SP = 0xFD
        for r in self.registers:
            self.registers[r] = 0
        self.halted = False

        # Emit updates
        signals.pc_updated.emit(self.PC)
        signals.mar_updated.emit(self.MAR)
        signals.ir_updated.emit(self.IR)
        signals.sp_updated.emit(self.SP)
        for r, v in self.registers.items():
            signals.register_updated.emit(r, v)

    def fetch_byte(self):
        """Fetch a single byte from memory at PC, increment PC"""
        self.MAR = self.PC
        signals.mar_updated.emit(self.MAR)

        byte_val = self.memory.read(self.MAR)

        self.PC += 1
        signals.pc_updated.emit(self.PC)

        return byte_val

    def execute_instruction(self):
        """Fetch and execute one complete instruction"""
        if self.halted:
            return

        # Fetch opcode
        opcode = self.fetch_byte()
        self.IR = opcode
        signals.ir_updated.emit(self.IR)
        signals.bus_transfer.emit("Memory", "IR", self.IR, "data")

        # Decode and execute
        if opcode == 0x00:  # NOP
            pass

        elif opcode == 0x01:  # LOAD Reg, Value
            reg_idx = self.fetch_byte()
            value = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                self.registers[reg_name] = value
                signals.register_updated.emit(reg_name, value)
                signals.bus_transfer.emit("Memory", reg_name, value, "data")

        elif opcode == 0x02:  # ADD Reg, Value (simplified: add immediate to A)
            value = self.fetch_byte()
            result = self.alu.add(self.registers["A"], value)
            self.registers["A"] = result & 0xFF
            signals.register_updated.emit("A", self.registers["A"])

        elif opcode == 0x03:  # SUB (placeholder)
            value = self.fetch_byte()
            result = self.alu.subtract(self.registers["A"], value)
            self.registers["A"] = result & 0xFF
            signals.register_updated.emit("A", self.registers["A"])

        elif opcode == 0x04:  # MOV Dest, Source
            dest_idx = self.fetch_byte()
            src_byte = self.fetch_byte()
            dest_name = self._reg_name(dest_idx)
            if dest_name:
                # Check if source is a register (high bit set) or immediate value
                if src_byte & 0x80:
                    # Source is a register
                    src_idx = src_byte & 0x7F
                    src_name = self._reg_name(src_idx)
                    if src_name:
                        self.registers[dest_name] = self.registers[src_name]
                        signals.bus_transfer.emit(src_name, dest_name, self.registers[dest_name], "data")
                else:
                    # Source is immediate value
                    self.registers[dest_name] = src_byte
                    signals.bus_transfer.emit("Memory", dest_name, src_byte, "data")
                signals.register_updated.emit(dest_name, self.registers[dest_name])

        # Logic operations
        elif opcode == 0x05:  # AND Reg, Value
            value = self.fetch_byte()
            result = self.alu.operate("AND", self.registers["A"], value)
            self.registers["A"] = result & 0xFF
            signals.register_updated.emit("A", self.registers["A"])

        elif opcode == 0x06:  # OR Reg, Value
            value = self.fetch_byte()
            result = self.alu.operate("OR", self.registers["A"], value)
            self.registers["A"] = result & 0xFF
            signals.register_updated.emit("A", self.registers["A"])

        elif opcode == 0x07:  # XOR Reg, Value
            value = self.fetch_byte()
            result = self.alu.operate("XOR", self.registers["A"], value)
            self.registers["A"] = result & 0xFF
            signals.register_updated.emit("A", self.registers["A"])

        elif opcode == 0x08:  # NOT Reg
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                result = self.alu.operate("NOT", self.registers[reg_name])
                self.registers[reg_name] = result & 0xFF
                signals.register_updated.emit(reg_name, self.registers[reg_name])

        # Comparison
        elif opcode == 0x09:  # CMP Reg, Value
            reg_idx = self.fetch_byte()
            value = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                # Perform subtraction to set flags, but don't store result
                self.alu.subtract(self.registers[reg_name], value)

        # Branching
        elif opcode == 0x10:  # JMP Address
            addr = self.fetch_byte()
            self.PC = addr
            signals.pc_updated.emit(self.PC)

        elif opcode == 0x11:  # JZ Address - Jump if Zero
            addr = self.fetch_byte()
            if self.alu.flags["Z"] == 1:
                self.PC = addr
                signals.pc_updated.emit(self.PC)

        elif opcode == 0x12:  # JNZ Address - Jump if Not Zero
            addr = self.fetch_byte()
            if self.alu.flags["Z"] == 0:
                self.PC = addr
                signals.pc_updated.emit(self.PC)

        elif opcode == 0x13:  # JC Address - Jump if Carry
            addr = self.fetch_byte()
            if self.alu.flags["C"] == 1:
                self.PC = addr
                signals.pc_updated.emit(self.PC)

        elif opcode == 0x14:  # JNC Address - Jump if Not Carry
            addr = self.fetch_byte()
            if self.alu.flags["C"] == 0:
                self.PC = addr
                signals.pc_updated.emit(self.PC)

        # Stack operations
        elif opcode == 0x20:  # PUSH Reg
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                # Push register value onto stack
                self.memory.write(self.SP, self.registers[reg_name])
                signals.bus_transfer.emit(reg_name, "Memory", self.registers[reg_name], "data")
                self.SP = (self.SP - 1) & 0xFF  # Decrement SP (stack grows down)
                signals.sp_updated.emit(self.SP)

        elif opcode == 0x21:  # POP Reg
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                # Pop value from stack into register
                self.SP = (self.SP + 1) & 0xFF  # Increment SP
                signals.sp_updated.emit(self.SP)
                value = self.memory.read(self.SP)
                self.registers[reg_name] = value
                signals.register_updated.emit(reg_name, value)
                signals.bus_transfer.emit("Memory", reg_name, value, "data")

        # Memory operations
        elif opcode == 0x30:  # LDM Reg, [addr] - Load from memory
            reg_idx = self.fetch_byte()
            addr = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                value = self.memory.read(addr)
                self.registers[reg_name] = value
                signals.register_updated.emit(reg_name, value)
                signals.bus_transfer.emit("Memory", reg_name, value, "data")

        elif opcode == 0x31:  # STM [addr], Reg - Store to memory
            addr = self.fetch_byte()
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                self.memory.write(addr, self.registers[reg_name])
                signals.bus_transfer.emit(reg_name, "Memory", self.registers[reg_name], "data")

        # I/O operations
        elif opcode == 0x40:  # OUT Reg - Write register to OUTPUT port (0xFE)
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                value = self.registers[reg_name]
                # Write to OUTPUT port address
                self.memory.write(0xFE, value)
                signals.bus_transfer.emit(reg_name, "I/O", value, "data")

        elif opcode == 0x41:  # IN Reg - Read from INPUT port (0xFF) to register
            reg_idx = self.fetch_byte()
            reg_name = self._reg_name(reg_idx)
            if reg_name:
                # Read from INPUT port address
                value = self.memory.read(0xFF)
                self.registers[reg_name] = value
                signals.register_updated.emit(reg_name, value)
                signals.bus_transfer.emit("I/O", reg_name, value, "data")

        elif opcode == 0xFF:  # HALT
            self.halted = True

    def _reg_name(self, idx):
        """Convert register index to name"""
        names = {0: "A", 1: "B", 2: "C", 3: "D"}
        return names.get(idx)

    # Legacy method for compatibility
    def fetch(self):
        """Legacy fetch - now executes full instruction"""
        self.execute_instruction()
        return self.IR
