from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSlider, QLabel
from PyQt6.QtCore import Qt, pyqtSignal

class ControlPanel(QWidget):
    # Signals to Main Window -> CPU
    run_clicked = pyqtSignal()
    step_clicked = pyqtSignal()
    reset_clicked = pyqtSignal()
    speed_changed = pyqtSignal(int)
    
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)
        
        self.btn_reset = QPushButton("Reset")
        self.btn_step = QPushButton("Step")
        self.btn_run = QPushButton("Run")
        
        self.slider_speed = QSlider(Qt.Orientation.Horizontal)
        self.slider_speed.setRange(1, 20) # 1Hz to 20Hz
        self.slider_speed.setValue(1)
        
        layout.addWidget(self.btn_reset)
        layout.addWidget(self.btn_step)
        layout.addWidget(self.btn_run)
        layout.addWidget(QLabel("Speed:"))
        layout.addWidget(self.slider_speed)
        
        # Connect internal signals
        self.btn_reset.clicked.connect(self.reset_clicked.emit)
        self.btn_step.clicked.connect(self.step_clicked.emit)
        self.btn_run.clicked.connect(self.run_clicked.emit)
        self.slider_speed.valueChanged.connect(self.speed_changed.emit)
