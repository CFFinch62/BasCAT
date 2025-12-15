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
        self.line_map = {}  # Maps memory address to assembly line number
        self.basic_line_map = {}  # Maps BASIC line number → list of assembly line numbers
        self.asm_to_basic_map = {}  # Maps assembly line number → BASIC line number
        self.execution_mode = "basic"  # "basic" or "assembly"
        self.current_basic_line = None  # Track current BASIC line for step-over

        self.clock.tick.connect(self.handle_tick)
    
    def load_code(self, source_code):
        machine_code, error, line_map = Assembler.assemble(source_code)
        if error:
            return False

        # Reset CPU and memory first
        self.clock.stop()
        self.cpu.reset()
        self.memory.reset()

        # Then set line_map and load program
        self.line_map = line_map
        self.memory.load_program(0, machine_code)
        return True

    def set_basic_line_map(self, basic_line_map):
        """
        Set the BASIC-to-assembly line mapping.
        basic_line_map: dict mapping BASIC line number → list of assembly line numbers
        """
        self.basic_line_map = basic_line_map
        # Build reverse map
        self.asm_to_basic_map = {}
        for basic_line, asm_lines in basic_line_map.items():
            for asm_line in asm_lines:
                self.asm_to_basic_map[asm_line] = basic_line

    def set_execution_mode(self, mode):
        """Set execution mode: 'basic' or 'assembly'"""
        self.execution_mode = mode

    def reset(self):
        self.clock.stop()
        self.cpu.reset()
        self.memory.reset()
        self.line_map = {}  # Clear line map so step will reload code
        self.current_basic_line = None

    def run(self):
        self.clock.start(1) # Default 1Hz

    def step(self):
        """Step into: Execute single assembly instruction"""
        self.handle_tick()

    def step_over(self):
        """
        Step over: Execute entire BASIC statement (all its assembly instructions).
        Keeps stepping until we move to a different BASIC line.
        """
        if self.cpu.halted:
            return

        # Get current BASIC line
        current_address = self.cpu.PC
        if current_address in self.line_map:
            asm_line = self.line_map[current_address]
            if asm_line in self.asm_to_basic_map:
                start_basic_line = self.asm_to_basic_map[asm_line]
            else:
                # No BASIC mapping, just do single step
                self.step()
                return
        else:
            # No line mapping, just do single step
            self.step()
            return

        # Execute instructions until we reach a different BASIC line
        while not self.cpu.halted:
            self.handle_tick()

            # Check if we've moved to a different BASIC line
            current_address = self.cpu.PC
            if current_address in self.line_map:
                asm_line = self.line_map[current_address]
                if asm_line in self.asm_to_basic_map:
                    current_basic_line = self.asm_to_basic_map[asm_line]
                    if current_basic_line != start_basic_line:
                        # Moved to different BASIC line, stop
                        break
                else:
                    # No BASIC mapping, stop
                    break
            else:
                # No line mapping, stop
                break

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
        if current_address in self.line_map:
            line_num = self.line_map[current_address]
            signals.current_line_changed.emit(line_num)

        # Execute one full instruction
        self.cpu.fetch()
