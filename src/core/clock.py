from PyQt6.QtCore import QTimer, QObject, pyqtSignal

class Clock(QObject):
    tick = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.tick.emit)
        
    def start(self, frequency_hz):
        interval_ms = int(1000 / frequency_hz)
        self.timer.start(interval_ms)
        
    def stop(self):
        self.timer.stop()
        
    def set_speed(self, frequency_hz):
        if self.timer.isActive():
            self.start(frequency_hz)
