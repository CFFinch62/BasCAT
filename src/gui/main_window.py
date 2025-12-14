from PyQt6.QtWidgets import QMainWindow, QDockWidget, QLabel, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from src.gui.circuit_view import CircuitView
from src.gui.editor import CodeEditor
from src.gui.dual_editor import DualEditor
from src.gui.controls import ControlPanel
from src.gui.io_panel import IOPanel
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

        # Execution mode: "basic" or "assembly" (for step-over vs step-into)
        self.execution_mode = "basic"

    def connect_signals(self):
        # Run Button Logic: Assemble -> Load -> Run
        self.control_panel.run_clicked.connect(self.on_run)
        self.control_panel.step_clicked.connect(self.on_step)
        self.control_panel.step_over_clicked.connect(self.on_step_over)
        self.control_panel.reset_clicked.connect(self.on_reset)
        self.control_panel.speed_changed.connect(self.sim.set_speed)

        # Connect mode toggle
        self.control_panel.mode_changed.connect(self.on_mode_changed)

        # Connect code execution tracking
        from src.core.signals import signals
        signals.current_line_changed.connect(self.on_line_changed)

        # Connect dual editor signals
        self.dual_editor.compilation_successful.connect(self.on_compilation_success)
        self.dual_editor.compilation_failed.connect(self.on_compilation_failed)

        # Connect I/O signals
        self.io_panel.input_submitted.connect(self.on_input_submitted)
        signals.output_written.connect(self.io_panel.display_byte)
        signals.output_char_written.connect(self.io_panel.display_char)
        signals.output_cleared.connect(self.io_panel.clear_output)

    def on_run(self):
        """Run the program (uses compiled assembly)"""
        # Get assembly code (either compiled or from dual editor)
        code = self.dual_editor.get_assembly_code()

        if not code.strip():
            # No compiled code, try to compile first
            self.dual_editor.on_compile()
            code = self.dual_editor.get_assembly_code()

        if code.strip() and self.sim.load_code(code):
            # Pass line mapping to sim manager
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)
            self.sim.run()

    def on_step(self):
        """Step into: Execute single assembly instruction"""
        # Load code if not already loaded (first step)
        if not self.sim.line_map:
            code = self.dual_editor.get_assembly_code()
            if not code.strip():
                # Try to compile
                self.dual_editor.on_compile()
                code = self.dual_editor.get_assembly_code()

            if not self.sim.load_code(code):
                return  # Assembly error
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)

        self.sim.step()

    def on_step_over(self):
        """Step over: Execute entire BASIC statement (multiple assembly instructions)"""
        # Load code if not already loaded (first step)
        if not self.sim.line_map:
            code = self.dual_editor.get_assembly_code()
            if not code.strip():
                # Try to compile
                self.dual_editor.on_compile()
                code = self.dual_editor.get_assembly_code()

            if not self.sim.load_code(code):
                return  # Assembly error
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)

        self.sim.step_over()

    def on_reset(self):
        """Reset the simulation"""
        self.dual_editor.clear_highlights()
        self.sim.reset()

    def on_mode_changed(self, mode):
        """Handle execution mode change (basic vs assembly)"""
        self.execution_mode = mode
        self.sim.set_execution_mode(mode)
        self.dual_editor.set_mode(mode)

    def on_line_changed(self, line_number):
        """Handle execution line change - highlight in appropriate editor(s)"""
        # This is the assembly line number from the CPU
        if self.execution_mode == "basic":
            # Highlight both BASIC and Assembly
            self.dual_editor.highlight_assembly_line(line_number)
        else:
            # Only highlight assembly
            self.dual_editor.highlight_assembly_line(line_number)

    def on_compilation_success(self, assembly_code, line_map):
        """Handle successful BASIC compilation"""
        print(f"Compilation successful: {len(assembly_code)} chars, {len(line_map)} mapped lines")

    def on_compilation_failed(self, error_message):
        """Handle failed BASIC compilation"""
        print(f"Compilation failed: {error_message}")

    def on_input_submitted(self, text):
        """Handle input submitted from I/O panel"""
        # Queue the input string to the I/O controller
        self.sim.memory.io_controller.queue_string(text)

    def setup_docks(self):
        # Dual Editor Dock (Left) - BASIC + Assembly side-by-side
        self.editor_dock = QDockWidget("Code Editor (BASIC + Assembly)", self)
        self.editor_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.dual_editor = DualEditor()
        self.editor_dock.setWidget(self.dual_editor)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.editor_dock)

        # Control Panel Dock (Top)
        self.control_dock = QDockWidget("Controls", self)
        self.control_dock.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.control_panel = ControlPanel()
        self.control_dock.setWidget(self.control_panel)
        self.addDockWidget(Qt.DockWidgetArea.TopDockWidgetArea, self.control_dock)

        # I/O Panel Dock (Right)
        self.io_dock = QDockWidget("Input/Output", self)
        self.io_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.io_panel = IOPanel()
        self.io_dock.setWidget(self.io_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.io_dock)
