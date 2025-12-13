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
        
        # Internal State
        self.halted = False

    def reset(self):
        self.PC = 0
        self.IR = 0
        self.MAR = 0
        for r in self.registers:
            self.registers[r] = 0
        self.halted = False
        
        # Emit updates
        signals.pc_updated.emit(self.PC)
        signals.mar_updated.emit(self.MAR)
        signals.ir_updated.emit(self.IR)
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

        elif opcode == 0x04:  # MOV Dest, Source (placeholder)
            dest = self.fetch_byte()
            src = self.fetch_byte()
            # Not fully implemented

        elif opcode == 0x10:  # JMP Address
            addr = self.fetch_byte()
            self.PC = addr
            signals.pc_updated.emit(self.PC)

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
