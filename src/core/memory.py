from src.core.signals import signals
from src.core.io_controller import IOController

class Memory:
    """
    Represents the 256-byte RAM of the CAL-EB computer.
    Address range: 0x00 to 0xFF (0 - 255)

    Memory Map:
    - 0x00-0xFD (0-253): General RAM
    - 0xFE (254): OUTPUT port (memory-mapped I/O)
    - 0xFF (255): INPUT port (memory-mapped I/O)
    """
    SIZE = 256  # 8-bit address space

    def __init__(self, io_controller=None):
        self._data = bytearray(self.SIZE)
        self.io_controller = io_controller or IOController()
        self.reset()

        # Connect signals acting as inputs to the memory unit
        # In a real circuit, these would be control lines
        # Here we just listen to requested writes
        # signals.memory_write.connect(self.write)  # Be careful of loops if CPU emits this

    def reset(self):
        """Clears all memory to 0."""
        for i in range(self.SIZE):
            self._data[i] = 0
        self.io_controller.reset()
        # Determine if we want to emit mass change signals (probably not for reset)

    def read(self, address):
        """
        Reads a byte from the specified address.
        Intercepts I/O port reads.
        """
        if not (0 <= address < self.SIZE):
            raise ValueError(f"Memory access out of bounds: {address:#04x}")

        # Check for I/O port reads
        if address == IOController.INPUT_PORT:
            # Read from INPUT port (0xFF)
            val = self.io_controller.read_input()
            signals.bus_transfer.emit("I/O", "Data Bus", val, "data")
            return val
        elif address == IOController.OUTPUT_PORT:
            # Reading from OUTPUT port returns last written value (from RAM)
            val = self._data[address]
            signals.bus_transfer.emit("Memory", "Data Bus", val, "data")
            return val
        else:
            # Normal RAM read
            val = self._data[address]
            signals.bus_transfer.emit("Memory", "Data Bus", val, "data")
            return val

    def write(self, address, value):
        """
        Writes a byte to the specified address.
        Intercepts I/O port writes.
        """
        if not (0 <= address < self.SIZE):
            raise ValueError(f"Memory write out of bounds: {address:#04x}")

        val = value & 0xFF  # Ensure 8-bit

        # Check for I/O port writes
        if address == IOController.OUTPUT_PORT:
            # Write to OUTPUT port (0xFE)
            self.io_controller.write_output(val)
            signals.bus_transfer.emit("Data Bus", "I/O", val, "data")
            # Also store in RAM for potential readback
            self._data[address] = val
        elif address == IOController.INPUT_PORT:
            # Writing to INPUT port is generally not allowed, but we'll allow it
            # (some systems use this for status/control)
            self._data[address] = val
            signals.memory_changed.emit(address, val)
            signals.bus_transfer.emit("Data Bus", "Memory", val, "data")
        else:
            # Normal RAM write
            self._data[address] = val
            signals.memory_changed.emit(address, val)
            signals.bus_transfer.emit("Data Bus", "Memory", val, "data")

    def load_program(self, start_address, data):
        """Helper to load a program (list of bytes) into memory."""
        for i, byte in enumerate(data):
            self.write(start_address + i, byte)
