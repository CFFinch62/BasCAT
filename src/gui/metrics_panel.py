"""
Metrics Panel for Phase 6

Displays real-time execution statistics:
- Instructions executed
- Clock cycles
- Memory utilization
- I/O operations
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox, QGridLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class MetricsPanel(QWidget):
    """
    Panel displaying execution metrics and statistics.

    Shows:
    - Instruction count
    - Clock cycles
    - Memory usage
    - I/O operations count
    """

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.reset_metrics()

    def init_ui(self):
        """Initialize the UI components"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)

        # Title
        title = QLabel("Performance Metrics")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(12)
        title.setFont(title_font)
        layout.addWidget(title)

        # Execution metrics group
        exec_group = QGroupBox("Execution")
        exec_layout = QGridLayout()

        self.lbl_instructions = self._create_metric_label("0")
        self.lbl_cycles = self._create_metric_label("0")

        exec_layout.addWidget(QLabel("Instructions:"), 0, 0)
        exec_layout.addWidget(self.lbl_instructions, 0, 1)
        exec_layout.addWidget(QLabel("Clock Cycles:"), 1, 0)
        exec_layout.addWidget(self.lbl_cycles, 1, 1)

        exec_group.setLayout(exec_layout)
        layout.addWidget(exec_group)

        # Memory metrics group
        mem_group = QGroupBox("Memory")
        mem_layout = QGridLayout()

        self.lbl_mem_used = self._create_metric_label("0 bytes")
        self.lbl_mem_percent = self._create_metric_label("0%")

        mem_layout.addWidget(QLabel("Used:"), 0, 0)
        mem_layout.addWidget(self.lbl_mem_used, 0, 1)
        mem_layout.addWidget(QLabel("Utilization:"), 1, 0)
        mem_layout.addWidget(self.lbl_mem_percent, 1, 1)

        mem_group.setLayout(mem_layout)
        layout.addWidget(mem_group)

        # I/O metrics group
        io_group = QGroupBox("I/O Operations")
        io_layout = QGridLayout()

        self.lbl_input_ops = self._create_metric_label("0")
        self.lbl_output_ops = self._create_metric_label("0")

        io_layout.addWidget(QLabel("Input:"), 0, 0)
        io_layout.addWidget(self.lbl_input_ops, 0, 1)
        io_layout.addWidget(QLabel("Output:"), 1, 0)
        io_layout.addWidget(self.lbl_output_ops, 1, 1)

        io_group.setLayout(io_layout)
        layout.addWidget(io_group)

        # CPU state group
        cpu_group = QGroupBox("CPU State")
        cpu_layout = QGridLayout()

        self.lbl_pc = self._create_metric_label("0")
        self.lbl_halted = self._create_metric_label("No")

        cpu_layout.addWidget(QLabel("PC:"), 0, 0)
        cpu_layout.addWidget(self.lbl_pc, 0, 1)
        cpu_layout.addWidget(QLabel("Halted:"), 1, 0)
        cpu_layout.addWidget(self.lbl_halted, 1, 1)

        cpu_group.setLayout(cpu_layout)
        layout.addWidget(cpu_group)

        # Add stretch to push everything to top
        layout.addStretch()

    def _create_metric_label(self, text):
        """Create a styled label for metric values"""
        label = QLabel(text)
        font = QFont("Monospace")
        font.setStyleHint(QFont.StyleHint.Monospace)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        return label

    def reset_metrics(self):
        """Reset all metrics to zero"""
        self.instruction_count = 0
        self.clock_cycles = 0
        self.input_operations = 0
        self.output_operations = 0
        self.program_bytes = 0
        self.update_display()

    def increment_instruction(self):
        """Increment instruction counter"""
        self.instruction_count += 1
        self.clock_cycles += 1  # For now, 1 instruction = 1 cycle
        self.update_display()

    def increment_input(self):
        """Increment input operation counter"""
        self.input_operations += 1
        self.update_display()

    def increment_output(self):
        """Increment output operation counter"""
        self.output_operations += 1
        self.update_display()

    def set_program_size(self, bytes_used):
        """Set the program size in bytes"""
        self.program_bytes = bytes_used
        self.update_display()

    def set_pc(self, pc_value):
        """Update PC display"""
        self.lbl_pc.setText(f"{pc_value}")

    def set_halted(self, halted):
        """Update halted status"""
        self.lbl_halted.setText("Yes" if halted else "No")
        if halted:
            self.lbl_halted.setStyleSheet("color: red; font-weight: bold;")
        else:
            self.lbl_halted.setStyleSheet("")

    def update_display(self):
        """Update all metric displays"""
        self.lbl_instructions.setText(f"{self.instruction_count}")
        self.lbl_cycles.setText(f"{self.clock_cycles}")
        self.lbl_input_ops.setText(f"{self.input_operations}")
        self.lbl_output_ops.setText(f"{self.output_operations}")

        # Memory metrics
        total_memory = 256  # 256 bytes total
        self.lbl_mem_used.setText(f"{self.program_bytes} bytes")

        percent = (self.program_bytes / total_memory) * 100 if total_memory > 0 else 0
        self.lbl_mem_percent.setText(f"{percent:.1f}%")
