"""
Dual Editor Widget for Phase 5

Displays BASIC code (editable) and generated Assembly code side-by-side.
Provides synchronized highlighting during execution.

Mode behavior:
- BASIC Mode: Shows BASIC editor, assembly hidden until compiled (with toggle)
- Assembly Mode: Shows only assembly editor (editable), BASIC hidden
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
                              QPlainTextEdit, QLabel, QPushButton, QMessageBox)
from PyQt6.QtGui import QFont, QTextCursor, QColor, QTextFormat
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QTextEdit


class SingleEditor(QWidget):
    """Single code editor with line highlighting support"""

    def __init__(self, title, read_only=False, placeholder_text=""):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

        # Title label
        self.title_label = QLabel(title)
        self.title_label.setStyleSheet("font-weight: bold; padding: 4px;")
        self.layout.addWidget(self.title_label)

        # Code editor
        self.editor = QPlainTextEdit()
        font = QFont("Monospace", 10)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.editor.setFont(font)
        self.editor.setReadOnly(read_only)
        self.editor.setPlaceholderText(placeholder_text)

        if read_only:
            self.editor.setStyleSheet("background-color: #2a2a2a;")

        self.layout.addWidget(self.editor)

        # Track current highlighted line
        self.current_highlight_line = -1

    def get_code(self):
        """Get editor contents"""
        return self.editor.toPlainText()

    def set_code(self, code):
        """Set editor contents"""
        self.editor.setPlainText(code)

    def set_read_only(self, read_only):
        """Set read-only state"""
        self.editor.setReadOnly(read_only)
        if read_only:
            self.editor.setStyleSheet("background-color: #2a2a2a;")
        else:
            self.editor.setStyleSheet("")

    def set_title(self, title):
        """Update the title label"""
        self.title_label.setText(title)

    def highlight_line(self, line_number):
        """Highlight the specified line number (0-based)"""
        self.current_highlight_line = line_number

        # Create a selection for the line
        block = self.editor.document().findBlockByLineNumber(line_number)
        if not block.isValid():
            return

        cursor = QTextCursor(block)
        cursor.select(QTextCursor.SelectionType.LineUnderCursor)

        # Create extra selection with highlight color
        selection = QTextEdit.ExtraSelection()
        selection.format.setBackground(QColor("#3a3a00"))  # Dark yellow background
        selection.format.setProperty(QTextFormat.Property.FullWidthSelection, True)
        selection.cursor = cursor

        # Apply the selection
        self.editor.setExtraSelections([selection])

        # Scroll to the highlighted line
        self.editor.setTextCursor(cursor)
        self.editor.ensureCursorVisible()

    def clear_highlight(self):
        """Clear any line highlighting"""
        self.current_highlight_line = -1
        self.editor.setExtraSelections([])
        # Force visual update
        self.editor.viewport().update()


class DualEditor(QWidget):
    """
    Dual-pane editor showing BASIC and Assembly code side-by-side.

    Mode behavior:
    - BASIC Mode: BASIC editor visible; assembly toggleable (hidden by default until compiled)
    - Assembly Mode: Only assembly editor visible (editable)
    """

    # Signal emitted when compilation succeeds
    compilation_successful = pyqtSignal(str, dict)  # assembly_code, line_map

    # Signal emitted when compilation fails
    compilation_failed = pyqtSignal(str)  # error_message

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Button bar
        self.button_bar = QHBoxLayout()
        
        self.compile_button = QPushButton("🔨 Compile BASIC → Assembly")
        self.compile_button.clicked.connect(self.on_compile)
        self.compile_button.setToolTip("Compile BASIC code to Assembly (Ctrl+B)")
        self.button_bar.addWidget(self.compile_button)
        
        self.toggle_asm_button = QPushButton("📄 Show Assembly")
        self.toggle_asm_button.clicked.connect(self.toggle_assembly_visibility)
        self.toggle_asm_button.setToolTip("Toggle assembly code visibility")
        self.button_bar.addWidget(self.toggle_asm_button)
        
        self.button_bar.addStretch()

        self.layout.addLayout(self.button_bar)

        # Splitter for two editors
        self.splitter = QSplitter(Qt.Orientation.Horizontal)

        # BASIC editor (left)
        self.basic_editor = SingleEditor(
            "BASIC Code (SimpleBASCAT)",
            read_only=False,
            placeholder_text="Enter BASIC code here...\nExample:\n10 LET A = 0\n20 PRINT A\n30 END"
        )

        # Default BASIC code
        self.basic_editor.set_code(
            "10 REM SimpleBASCAT Demo\n"
            "20 LET A = 0\n"
            "30 INPUT B\n"
            "40 LET A = A + B\n"
            "50 PRINT A\n"
            "60 IF A < 100 THEN GOTO 30\n"
            "70 END\n"
        )

        # Assembly editor (right)
        self.assembly_editor = SingleEditor(
            "Generated Assembly (Read-Only)",
            read_only=True,
            placeholder_text="Assembly code will appear here after compilation..."
        )

        self.splitter.addWidget(self.basic_editor)
        self.splitter.addWidget(self.assembly_editor)
        self.splitter.setSizes([500, 500])  # Equal split
        
        # Prevent editors from collapsing and set minimum sizes
        self.splitter.setChildrenCollapsible(False)
        self.basic_editor.setMinimumWidth(200)
        self.assembly_editor.setMinimumWidth(200)

        self.layout.addWidget(self.splitter)

        # Store compilation results
        self.compiled_assembly = ""
        self.basic_to_asm_map = {}  # Maps BASIC line number → list of assembly line numbers
        self.asm_to_basic_map = {}  # Maps assembly line number → BASIC line number

        # Execution mode: "basic" or "assembly"
        self.mode = "basic"
        
        # Assembly visibility state (for BASIC mode)
        self.assembly_visible = False
        
        # Initialize visibility for BASIC mode
        self._apply_mode()

    def _apply_mode(self):
        """Apply visibility settings based on current mode"""
        if self.mode == "assembly":
            # Assembly mode: only show assembly editor (editable)
            self.basic_editor.hide()
            self.assembly_editor.show()
            self.assembly_editor.set_read_only(False)
            self.assembly_editor.set_title("Assembly Code")
            
            # Hide BASIC-specific buttons
            self.compile_button.hide()
            self.toggle_asm_button.hide()
        else:
            # BASIC mode: show BASIC editor, assembly based on toggle
            self.basic_editor.show()
            self.assembly_editor.set_read_only(True)
            self.assembly_editor.set_title("Generated Assembly (Read-Only)")
            
            # Show BASIC-specific buttons
            self.compile_button.show()
            self.toggle_asm_button.show()
            
            # Apply assembly visibility toggle
            if self.assembly_visible:
                self.assembly_editor.show()
                self.toggle_asm_button.setText("📄 Hide Assembly")
            else:
                self.assembly_editor.hide()
                self.toggle_asm_button.setText("📄 Show Assembly")

    def toggle_assembly_visibility(self):
        """Toggle assembly editor visibility (BASIC mode only)"""
        if self.mode == "basic":
            self.assembly_visible = not self.assembly_visible
            self._apply_mode()

    def get_basic_code(self):
        """Get BASIC code"""
        return self.basic_editor.get_code()

    def get_assembly_code(self):
        """Get assembly code (compiled or hand-written depending on mode)"""
        if self.mode == "assembly":
            return self.assembly_editor.get_code()
        return self.compiled_assembly

    def on_compile(self):
        """Compile BASIC code to Assembly"""
        from src.compiler.compiler import SimpleBASCATCompiler

        basic_code = self.basic_editor.get_code()

        if not basic_code.strip():
            QMessageBox.warning(self, "Compilation Error", "BASIC code is empty!")
            self.compilation_failed.emit("BASIC code is empty")
            return

        # Compile
        compiler = SimpleBASCATCompiler()
        result = compiler.compile(basic_code)

        if result.success:
            # Update assembly editor
            self.compiled_assembly = result.assembly
            self.assembly_editor.set_code(result.assembly)

            # Store line mappings
            self.basic_to_asm_map = result.line_map
            self.build_reverse_map()

            # Auto-show assembly after successful compilation
            self.assembly_visible = True
            self._apply_mode()

            # Emit success signal
            self.compilation_successful.emit(result.assembly, result.line_map)

            QMessageBox.information(
                self,
                "Compilation Successful",
                f"BASIC code compiled successfully!\n\n"
                f"Generated {len(result.assembly.splitlines())} lines of assembly.\n"
                f"Bytecode size: {len(result.bytecode)} bytes"
            )
        else:
            # Show error
            self.compilation_failed.emit(result.error)
            QMessageBox.critical(
                self,
                "Compilation Failed",
                f"Failed to compile BASIC code:\n\n{result.error}"
            )

    def build_reverse_map(self):
        """Build reverse mapping from assembly line → BASIC line"""
        self.asm_to_basic_map = {}
        for basic_line, asm_lines in self.basic_to_asm_map.items():
            for asm_line in asm_lines:
                self.asm_to_basic_map[asm_line] = basic_line

    def highlight_assembly_line(self, asm_line_number):
        """Highlight an assembly line (0-based)"""
        self.assembly_editor.highlight_line(asm_line_number)

        # Also highlight corresponding BASIC line if mapping exists
        if asm_line_number in self.asm_to_basic_map:
            basic_line = self.asm_to_basic_map[asm_line_number]
            self.highlight_basic_line_number(basic_line)

    def highlight_basic_line_number(self, basic_line_number):
        """
        Highlight a BASIC line by its line number (e.g., 10, 20, 30).
        Finds the actual editor line (0-based) that starts with this number.
        """
        code = self.basic_editor.get_code()
        lines = code.splitlines()

        for i, line in enumerate(lines):
            # Check if this line starts with the line number
            parts = line.strip().split()
            if parts and parts[0].isdigit() and int(parts[0]) == basic_line_number:
                self.basic_editor.highlight_line(i)
                return

    def highlight_basic_statement(self, basic_line_number):
        """
        Highlight a BASIC statement and all its corresponding assembly lines.
        basic_line_number is the BASIC line number (e.g., 10, 20, 30).
        """
        # Highlight BASIC line
        self.highlight_basic_line_number(basic_line_number)

        # Highlight first assembly line for this BASIC statement
        if basic_line_number in self.basic_to_asm_map:
            asm_lines = self.basic_to_asm_map[basic_line_number]
            if asm_lines:
                # Highlight the first assembly line for this statement
                self.assembly_editor.highlight_line(asm_lines[0])

    def clear_highlights(self):
        """Clear all highlighting in both editors"""
        self.basic_editor.clear_highlight()
        self.assembly_editor.clear_highlight()

    def set_mode(self, mode):
        """Set execution mode: 'basic' or 'assembly'"""
        self.mode = mode
        self._apply_mode()
