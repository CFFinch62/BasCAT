from src.core.signals import signals

class Memory:
    """
    Represents the 64KB memory space of the CAL-EB computer.
    Address range: 0x0000 to 0xFFFF (0 - 65535)
    """
    SIZE = 65536

    def __init__(self):
        self._data = bytearray(self.SIZE)
        self.reset()
        
        # Connect signals acting as inputs to the memory unit
        # In a real circuit, these would be control lines
        # Here we just listen to requested writes
        # signals.memory_write.connect(self.write)  # Be careful of loops if CPU emits this

    def reset(self):
        """Clears all memory to 0."""
        for i in range(self.SIZE):
            self._data[i] = 0
        # Determine if we want to emit mass change signals (probably not for reset)
    
    def read(self, address):
        """
        Reads a byte from the specified address.
        """
        if 0 <= address < self.SIZE:
            val = self._data[address]
            # Visualize the read operation
            signals.bus_transfer.emit("Memory", "Data Bus", val, "data")
            return val
        else:
            raise ValueError(f"Memory access out of bounds: {address:#06x}")

    def write(self, address, value):
        """
        Writes a byte to the specified address.
        """
        if 0 <= address < self.SIZE:
            val = value & 0xFF  # Ensure 8-bit
            self._data[address] = val
            signals.memory_changed.emit(address, val)
            signals.bus_transfer.emit("Data Bus", "Memory", val, "data")
        else:
            raise ValueError(f"Memory write out of bounds: {address:#06x}")

    def load_program(self, start_address, data):
        """Helper to load a program (list of bytes) into memory."""
        for i, byte in enumerate(data):
            self.write(start_address + i, byte)
