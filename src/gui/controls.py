from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSlider, QLabel, QComboBox
from PyQt6.QtCore import Qt, pyqtSignal

class ControlPanel(QWidget):
    # Signals to Main Window -> CPU
    run_clicked = pyqtSignal()
    step_clicked = pyqtSignal()
    step_over_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    speed_changed = pyqtSignal(int)
    mode_changed = pyqtSignal(str)  # "basic" or "assembly"

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        self.btn_reset = QPushButton("Reset")
        self.btn_step = QPushButton("Step Into")
        self.btn_step_over = QPushButton("Step Over")
        self.btn_run = QPushButton("Run")

        # Mode selector
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["BASIC Mode", "Assembly Mode"])
        self.mode_selector.setToolTip(
            "BASIC Mode: Step through BASIC statements\n"
            "Assembly Mode: Step through individual assembly instructions"
        )

        self.slider_speed = QSlider(Qt.Orientation.Horizontal)
        self.slider_speed.setRange(1, 20) # 1Hz to 20Hz
        self.slider_speed.setValue(1)

        # Tooltips
        self.btn_reset.setToolTip("Reset CPU and memory")
        self.btn_step.setToolTip("Step Into: Execute one assembly instruction")
        self.btn_step_over.setToolTip("Step Over: Execute one BASIC statement")
        self.btn_run.setToolTip("Run program continuously")

        layout.addWidget(self.btn_reset)
        layout.addWidget(self.btn_step)
        layout.addWidget(self.btn_step_over)
        layout.addWidget(self.btn_run)
        layout.addWidget(QLabel("Mode:"))
        layout.addWidget(self.mode_selector)
        layout.addWidget(QLabel("Speed:"))
        layout.addWidget(self.slider_speed)

        # Connect internal signals
        self.btn_reset.clicked.connect(self.reset_clicked.emit)
        self.btn_step.clicked.connect(self.step_clicked.emit)
        self.btn_step_over.clicked.connect(self.step_over_clicked.emit)
        self.btn_run.clicked.connect(self.run_clicked.emit)
        self.slider_speed.valueChanged.connect(self.speed_changed.emit)
        self.mode_selector.currentIndexChanged.connect(self.on_mode_changed)

    def on_mode_changed(self, index):
        """Handle mode combo box change"""
        mode = "basic" if index == 0 else "assembly"
        self.mode_changed.emit(mode)
