from PyQt6.QtCore import QObject, pyqtSignal

class ArchitectureSignals(QObject):
    """
    Central signal hub for the CAL-EB architecture.
    Simulates the control and data buses by emitting signals when state changes.
    """
    # Memory signals
    memory_read = pyqtSignal(int)  # address
    memory_write = pyqtSignal(int, int)  # address, value
    memory_changed = pyqtSignal(int, int)  # address, new_value

    # CPU Register updates (for visualization)
    register_updated = pyqtSignal(str, int)  # register_name, value
    pc_updated = pyqtSignal(int)
    mar_updated = pyqtSignal(int)
    ir_updated = pyqtSignal(int)

    # ALU flags update (for visualization)
    flags_updated = pyqtSignal(dict)  # flags dictionary {'Z': 0/1, 'N': 0/1, 'C': 0/1, 'O': 0/1}

    # Bus activity (for animation)
    # source, destination, value, bus_type ('data', 'address', 'control')
    bus_transfer = pyqtSignal(str, str, int, str)

    # Code execution tracking
    # Emits the source line number being executed
    current_line_changed = pyqtSignal(int)  # line_number

    def __init__(self):
        super().__init__()

# Global singleton for easy access across components
signals = ArchitectureSignals()
