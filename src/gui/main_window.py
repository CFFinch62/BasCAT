from PyQt6.QtWidgets import QMainWindow, QDockWidget, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from src.gui.circuit_view import CircuitView
from src.gui.editor import CodeEditor
from src.gui.controls import ControlPanel
from src.core.sim_manager import SimManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAL-EB: 8-Bit Computer Trainer")
        self.resize(1200, 800)
        
        # Simulation Backbone
        self.sim = SimManager()
        
        # Central Widget (Circuit Board)
        self.central_widget = CircuitView()
        self.setCentralWidget(self.central_widget)
        
        # Setup Docks
        self.setup_docks()
        
        # Connect Controls
        self.connect_signals()

    def connect_signals(self):
        # Run Button Logic: Assemble -> Load -> Run
        self.control_panel.run_clicked.connect(self.on_run)
        self.control_panel.step_clicked.connect(self.on_step)
        self.control_panel.reset_clicked.connect(self.on_reset)
        self.control_panel.speed_changed.connect(self.sim.set_speed)

        # Connect code execution tracking
        from src.core.signals import signals
        signals.current_line_changed.connect(self.editor.highlight_line)

    def on_run(self):
        code = self.editor.get_code()
        if self.sim.load_code(code):
            self.sim.run()

    def on_step(self):
        # Load code if not already loaded (first step)
        if not self.sim.line_map:
            code = self.editor.get_code()
            if not self.sim.load_code(code):
                return  # Assembly error
        self.sim.step()

    def on_reset(self):
        self.editor.clear_highlight()
        self.sim.reset()

    def setup_docks(self):
        # Code Editor Dock (Left)
        self.editor_dock = QDockWidget("Assembly Editor", self)
        self.editor_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)
        self.editor = CodeEditor()
        self.editor_dock.setWidget(self.editor)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.editor_dock)
        
        # Control Panel Dock (Top)
        self.control_dock = QDockWidget("Controls", self)
        self.control_dock.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.control_panel = ControlPanel()
        self.control_dock.setWidget(self.control_panel)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.control_dock)

        # TODO: Memory Viewer Dock (Future Phase)
        # This will show a hex dump view of RAM contents for debugging
        # Plan: Bottom dock with scrollable hex/ASCII display
        # self.memory_viewer_dock = QDockWidget("Memory Viewer", self)
        # self.memory_viewer = MemoryViewerWidget()
        # self.memory_viewer_dock.setWidget(self.memory_viewer)
        # self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.memory_viewer_dock)
