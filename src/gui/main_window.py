from PyQt6.QtWidgets import (QMainWindow, QDockWidget, QLabel, QWidget, QVBoxLayout,
                              QFileDialog, QMessageBox, QTextBrowser, QDialog,
                              QDialogButtonBox, QSplitter)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
import json
import os

from src.gui.circuit_view import CircuitView
from src.gui.dual_editor import DualEditor
from src.gui.controls import ControlPanel
from src.gui.io_panel import IOPanel
from src.gui.metrics_panel import MetricsPanel
from src.gui.memory_panel import MemoryPanel
from src.core.sim_manager import SimManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BasCAT: BASIC Computer Architecture Trainer")
        self.resize(1400, 900)
        
        # Set application icon
        from PyQt6.QtGui import QIcon
        import os
        icon_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "bascat_icon_512_v2.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # Simulation Backbone
        self.sim = SimManager()

        # Central Widget: Splitter with CPU Circuit and Memory Panel
        self.central_splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left: Circuit View (CPU visualization)
        self.central_widget = CircuitView()
        self.central_splitter.addWidget(self.central_widget)
        
        # Right: Memory Panel (stack/memory viewer)
        self.memory_panel = MemoryPanel()
        self.central_splitter.addWidget(self.memory_panel)
        
        # Set initial sizes (circuit wider, memory narrower)
        self.central_splitter.setSizes([550, 250])
        self._memory_panel_last_size = 250  # Track last size for toggle
        
        self.setCentralWidget(self.central_splitter)

        # Setup Docks
        self.setup_docks()

        # Setup Menus
        self.setup_menus()

        # Connect Controls
        self.connect_signals()

        # Execution mode: "basic" or "assembly" (for step-over vs step-into)
        self.execution_mode = "basic"

        # Current file path
        self.current_file = None


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
        signals.current_line_changed.connect(self.on_instruction_executed)

        # Connect dual editor signals
        self.dual_editor.compilation_successful.connect(self.on_compilation_success)
        self.dual_editor.compilation_failed.connect(self.on_compilation_failed)

        # Connect I/O signals
        self.io_panel.input_submitted.connect(self.on_input_submitted)
        self.io_panel.numeric_input_submitted.connect(self.on_numeric_input_submitted)
        signals.output_written.connect(self.io_panel.display_byte)
        signals.output_char_written.connect(self.io_panel.display_char)
        signals.output_char_written.connect(lambda: self.metrics_panel.increment_output())
        signals.output_cleared.connect(self.io_panel.clear_output)

    def on_run(self):
        """Run the program (uses compiled or hand-written assembly)"""
        code = self.dual_editor.get_assembly_code()

        if not code.strip():
            # No assembly code available
            if self.execution_mode == "basic":
                # Try to compile BASIC first
                self.dual_editor.on_compile()
                code = self.dual_editor.get_assembly_code()
            else:
                # In assembly mode, user needs to write code
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "No Code", "Please enter assembly code to run.")
                return

        if code.strip() and self.sim.load_code(code):
            # Pass line mapping to sim manager (empty in assembly mode)
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)
            # Refresh memory panel to show loaded program
            self.memory_panel.refresh_display()
            self.central_widget.stack_visual.set_sp(0xFD)
            self.sim.run()

    def on_step(self):
        """Step into: Execute single assembly instruction"""
        # Load code if not already loaded (first step)
        if not self.sim.line_map:
            code = self.dual_editor.get_assembly_code()
            if not code.strip():
                if self.execution_mode == "basic":
                    # Try to compile
                    self.dual_editor.on_compile()
                    code = self.dual_editor.get_assembly_code()
                else:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(self, "No Code", "Please enter assembly code to run.")
                    return

            if not self.sim.load_code(code):
                return  # Assembly error
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)
            # Refresh memory panel to show loaded program
            self.memory_panel.refresh_display()
            self.central_widget.stack_visual.set_sp(0xFD)

        self.sim.step()
        # Refresh memory panel after step execution
        self.memory_panel.refresh_display()

    def on_step_over(self):
        """Step over: Execute entire BASIC statement (multiple assembly instructions)"""
        # Load code if not already loaded (first step)
        if not self.sim.line_map:
            code = self.dual_editor.get_assembly_code()
            if not code.strip():
                if self.execution_mode == "basic":
                    # Try to compile
                    self.dual_editor.on_compile()
                    code = self.dual_editor.get_assembly_code()
                else:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(self, "No Code", "Please enter assembly code to run.")
                    return

            if not self.sim.load_code(code):
                return  # Assembly error
            self.sim.set_basic_line_map(self.dual_editor.basic_to_asm_map)
            # Refresh memory panel to show loaded program
            self.memory_panel.refresh_display()
            self.central_widget.stack_visual.set_sp(0xFD)

        self.sim.step_over()
        # Refresh memory panel after step execution
        self.memory_panel.refresh_display()

    def on_reset(self):
        """Reset the simulation"""
        self.dual_editor.clear_highlights()
        self.sim.reset()
        self.metrics_panel.reset_metrics()
        # Refresh memory panel to show cleared memory
        self.memory_panel.refresh_display()
        # Update stack visual with reset SP
        self.central_widget.stack_visual.set_sp(0xFD)

    def on_instruction_executed(self):
        """Update metrics when an instruction is executed"""
        self.metrics_panel.increment_instruction()
        self.metrics_panel.set_pc(self.sim.cpu.PC)
        self.metrics_panel.set_halted(self.sim.cpu.halted)

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
        # Get bytecode size
        from src.core.assembler import Assembler
        bytecode, error, _ = Assembler.assemble(assembly_code)
        if bytecode:
            self.metrics_panel.set_program_size(len(bytecode))

    def on_compilation_failed(self, error_message):
        """Handle failed BASIC compilation"""
        pass

    def on_input_submitted(self, text):
        """Handle input submitted from I/O panel (ASCII mode)"""
        # Queue the input string to the I/O controller
        self.sim.memory.io_controller.queue_string(text)

    def on_numeric_input_submitted(self, value):
        """Handle numeric input submitted from I/O panel (Numeric mode)"""
        # Queue the single byte value directly
        self.sim.memory.io_controller.queue_input(value)

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

        # I/O Panel Dock (Right top)
        self.io_dock = QDockWidget("Input/Output", self)
        self.io_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.io_panel = IOPanel()
        self.io_dock.setWidget(self.io_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.io_dock)

        # Metrics Panel Dock (Right bottom)
        self.metrics_dock = QDockWidget("Performance Metrics", self)
        self.metrics_dock.setAllowedAreas(Qt.DockWidgetArea.RightDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        self.metrics_panel = MetricsPanel()
        self.metrics_dock.setWidget(self.metrics_panel)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.metrics_dock)

        # Connect memory reference to circuit view and memory panel
        # (memory_panel is created in __init__ as part of central splitter)
        self.central_widget.set_memory(self.sim.memory)
        self.memory_panel.set_memory(self.sim.memory)
        
        # Connect SP updates to memory panel and toggle signal
        from src.core.signals import signals
        signals.sp_updated.connect(self.memory_panel.set_sp)
        signals.memory_panel_toggle.connect(self.toggle_memory_panel)

    def toggle_memory_panel(self):
        """Toggle memory panel visibility by collapsing/expanding the splitter"""
        sizes = self.central_splitter.sizes()
        if sizes[1] > 0:
            # Memory panel is visible, collapse it
            self._memory_panel_last_size = sizes[1]
            self.central_splitter.setSizes([sizes[0] + sizes[1], 0])
        else:
            # Memory panel is collapsed, restore it
            total = sizes[0] + sizes[1]
            self.central_splitter.setSizes([total - self._memory_panel_last_size, self._memory_panel_last_size])


    def setup_menus(self):
        """Setup application menus"""
        menubar = self.menuBar()

        # File Menu
        file_menu = menubar.addMenu("&File")

        new_action = QAction("&New", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self.file_new)
        file_menu.addAction(new_action)

        open_action = QAction("&Open...", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.file_open)
        file_menu.addAction(open_action)

        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self.file_save)
        file_menu.addAction(save_action)

        save_as_action = QAction("Save &As...", self)
        save_as_action.setShortcut("Ctrl+Shift+S")
        save_as_action.triggered.connect(self.file_save_as)
        file_menu.addAction(save_as_action)

        file_menu.addSeparator()

        quit_action = QAction("&Quit", self)
        quit_action.setShortcut("Ctrl+Q")
        quit_action.triggered.connect(self.close)
        file_menu.addAction(quit_action)

        # Examples Menu
        examples_menu = menubar.addMenu("&Examples")
        self.load_examples_menu(examples_menu)

        # Help Menu
        help_menu = menubar.addMenu("&Help")

        inst_ref_action = QAction("&Instruction Reference", self)
        inst_ref_action.setShortcut("F1")
        inst_ref_action.triggered.connect(self.show_instruction_reference)
        help_menu.addAction(inst_ref_action)

        basic_guide_action = QAction("&BASIC Language Guide", self)
        basic_guide_action.setShortcut("F2")
        basic_guide_action.triggered.connect(self.show_basic_guide)
        help_menu.addAction(basic_guide_action)

        help_menu.addSeparator()

        about_action = QAction("&About BasCAT", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    # File Menu Handlers
    def file_new(self):
        """Create new program"""
        reply = QMessageBox.question(
            self, "New Program",
            "Clear current code and start new program?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.dual_editor.basic_editor.set_code("")
            self.dual_editor.assembly_editor.set_code("")
            self.dual_editor.compiled_assembly = ""
            self.current_file = None
            self.on_reset()

    def file_open(self):
        """Open existing file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Program",
            "", "BASIC Files (*.bas);;All Files (*)"
        )
        if filename:
            try:
                with open(filename, 'r') as f:
                    code = f.read()
                self.dual_editor.basic_editor.set_code(code)
                self.current_file = filename
                self.setWindowTitle(f"BasCAT - {os.path.basename(filename)}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file:\n{e}")

    def file_save(self):
        """Save current file"""
        if self.current_file:
            self._save_to_file(self.current_file)
        else:
            self.file_save_as()

    def file_save_as(self):
        """Save as new file"""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Program As",
            "", "BASIC Files (*.bas);;All Files (*)"
        )
        if filename:
            if not filename.endswith('.bas'):
                filename += '.bas'
            self._save_to_file(filename)
            self.current_file = filename
            self.setWindowTitle(f"BasCAT - {os.path.basename(filename)}")

    def _save_to_file(self, filename):
        """Save BASIC code to file"""
        try:
            code = self.dual_editor.get_basic_code()
            with open(filename, 'w') as f:
                f.write(code)
            QMessageBox.information(self, "Saved", f"Program saved to:\n{filename}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save file:\n{e}")

    # Examples Menu
    def load_examples_menu(self, menu):
        """Load examples from catalog and populate menu"""
        try:
            catalog_path = os.path.join(os.path.dirname(__file__), "..", "..", "examples", "catalog.json")
            with open(catalog_path, 'r') as f:
                catalog = json.load(f)

            # Group by category
            categories = {}
            for example in catalog['examples']:
                cat = example['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(example)

            # Create submenu for each category
            for category_name in sorted(categories.keys()):
                submenu = menu.addMenu(category_name)
                for example in categories[category_name]:
                    action = QAction(f"{example['title']} ({example['difficulty']})", self)
                    action.setToolTip(example['description'])
                    action.triggered.connect(lambda checked, ex=example: self.load_example(ex))
                    submenu.addAction(action)

        except Exception as e:
            action = QAction("(No examples available)", self)
            action.setEnabled(False)
            menu.addAction(action)

    def load_example(self, example):
        """Load an example program"""
        try:
            example_path = os.path.join(os.path.dirname(__file__), "..", "..", "examples", example['file'])
            with open(example_path, 'r') as f:
                code = f.read()

            # Show info about the example
            info = f"**{example['title']}**\n\n"
            info += f"Category: {example['category']}\n"
            info += f"Difficulty: {example['difficulty']}\n\n"
            info += f"{example['description']}\n\n"
            info += f"Concepts: {', '.join(example['concepts'])}"

            msg = QMessageBox(self)
            msg.setWindowTitle("Load Example")
            msg.setText(f"Load example program '{example['title']}'?")
            msg.setInformativeText(info)
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msg.setDefaultButton(QMessageBox.StandardButton.Yes)

            if msg.exec() == QMessageBox.StandardButton.Yes:
                # Check if this is an assembly or BASIC example
                is_assembly = example['file'].endswith('.asm')

                if is_assembly:
                    # Load directly into assembly editor, clear BASIC editor
                    self.dual_editor.basic_editor.set_code("")
                    self.dual_editor.assembly_editor.set_code(code)
                    self.dual_editor.compiled_assembly = code
                else:
                    # Load into BASIC editor (normal flow)
                    self.dual_editor.basic_editor.set_code(code)
                    self.dual_editor.assembly_editor.set_code("")
                    self.dual_editor.compiled_assembly = ""

                self.current_file = None
                self.setWindowTitle(f"BasCAT - {example['title']} (Example)")
                self.on_reset()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load example:\n{e}")

    # Help Menu
    def show_instruction_reference(self):
        """Show assembly instruction reference"""
        self._show_help_document(
            "Assembly Instruction Reference",
            os.path.join(os.path.dirname(__file__), "..", "..", "docs", "assembly_guide.md")
        )

    def show_basic_guide(self):
        """Show BASIC language guide"""
        self._show_help_document(
            "SimpleBASCAT Language Guide",
            os.path.join(os.path.dirname(__file__), "..", "..", "docs", "basic_guide.md")
        )

    def _show_help_document(self, title, filepath):
        """Show a markdown document in a dialog"""
        try:
            with open(filepath, 'r') as f:
                content = f.read()

            dialog = QDialog(self)
            dialog.setWindowTitle(title)
            dialog.resize(800, 600)

            layout = QVBoxLayout(dialog)

            browser = QTextBrowser()
            browser.setMarkdown(content)
            browser.setOpenExternalLinks(True)
            layout.addWidget(browser)

            buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
            buttons.rejected.connect(dialog.close)
            layout.addWidget(buttons)

            dialog.exec()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load help document:\n{e}")

    def show_about(self):
        """Show about dialog"""
        about_text = """
        <h2>BasCAT</h2>
        <h3>BASIC Computer Architecture Trainer</h3>
        <p><b>Version 1.0</b></p>

        <p>An educational 8-bit computer simulator for learning:</p>
        <ul>
            <li>Assembly language programming</li>
            <li>Computer architecture fundamentals</li>
            <li>How high-level languages compile to machine code</li>
            <li>CPU, memory, and I/O operations</li>
        </ul>

        <p><b>Features:</b></p>
        <ul>
            <li>23 assembly instructions</li>
            <li>SimpleBASCAT high-level language</li>
            <li>Dual-level debugging (BASIC + Assembly)</li>
            <li>Visual circuit simulation</li>
            <li>Memory-mapped I/O</li>
            <li>Performance metrics</li>
        </ul>

        <p><b>Quick Start:</b></p>
        <ol>
            <li>Load an example from the Examples menu</li>
            <li>Click "Compile" to generate assembly</li>
            <li>Use "Step Over" to execute BASIC statements</li>
            <li>Watch the circuit visualization</li>
        </ol>

        <p><b>Help:</b></p>
        <ul>
            <li>F1 - Assembly Instruction Reference</li>
            <li>F2 - BASIC Language Guide</li>
        </ul>

        <p><i>Built with PyQt6 and Python</i></p>
        """

        QMessageBox.about(self, "About BasCAT", about_text)
