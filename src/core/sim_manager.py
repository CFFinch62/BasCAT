from src.core.cpu import CPU
from src.core.memory import Memory
from src.core.clock import Clock
from src.core.assembler import Assembler
from src.core.signals import signals

class SimManager:
    def __init__(self):
        self.memory = Memory()
        self.cpu = CPU(self.memory)
        self.clock = Clock()
        self.line_map = {}  # Maps memory address to source line number

        self.clock.tick.connect(self.handle_tick)
    
    def load_code(self, source_code):
        machine_code, error, line_map = Assembler.assemble(source_code)
        if error:
            print(f"Assembly Error: {error}")
            return False

        # Reset CPU and memory first
        self.clock.stop()
        self.cpu.reset()
        self.memory.reset()

        # Then set line_map and load program
        self.line_map = line_map
        self.memory.load_program(0, machine_code)
        print(f"Program loaded. line_map={self.line_map}")
        return True

    def reset(self):
        self.clock.stop()
        self.cpu.reset()
        self.memory.reset()
        self.line_map = {}  # Clear line map so step will reload code

    def run(self):
        self.clock.start(1) # Default 1Hz

    def step(self):
        # Allow single step
        self.handle_tick()
        
    def stop(self):
        self.clock.stop()

    def set_speed(self, hz):
        self.clock.set_speed(hz)

    def handle_tick(self):
        if self.cpu.halted:
            self.clock.stop()
            return

        # Emit the current source line being executed
        current_address = self.cpu.PC
        print(f"DEBUG: PC={current_address}, line_map={self.line_map}")
        if current_address in self.line_map:
            line_num = self.line_map[current_address]
            print(f"DEBUG: Emitting line {line_num}")
            signals.current_line_changed.emit(line_num)

        # Execute one full instruction
        self.cpu.fetch()
