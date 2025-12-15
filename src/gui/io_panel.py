"""
I/O Panel Widget for BasCAT

Provides input and output interface for programs.
Supports two modes:
- ASCII mode: Each character is sent as its ASCII value (original behavior)
- Numeric mode: Input is parsed as a decimal number (0-255), output shows decimal values
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
                             QLineEdit, QPushButton, QLabel, QGroupBox,
                             QRadioButton, QButtonGroup, QMessageBox)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, pyqtSignal


class IOPanel(QWidget):
    """
    I/O Panel widget showing input field and output display.
    Supports ASCII and Numeric modes for input/output.
    """

    # Signal emitted when user wants to send input
    # In ASCII mode: emits the raw string
    # In Numeric mode: emits a string containing the numeric value
    input_submitted = pyqtSignal(str)
    
    # Signal for numeric input (value as int)
    numeric_input_submitted = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.numeric_mode = False  # Default to ASCII mode
        self.setup_ui()

    def setup_ui(self):
        """Setup the UI layout"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

        # Mode selection at the top
        mode_group = QGroupBox("I/O Mode")
        mode_layout = QHBoxLayout()
        
        self.ascii_radio = QRadioButton("ASCII (character-by-character)")
        self.numeric_radio = QRadioButton("Numeric (decimal values)")
        self.ascii_radio.setChecked(True)
        
        self.mode_button_group = QButtonGroup()
        self.mode_button_group.addButton(self.ascii_radio, 0)
        self.mode_button_group.addButton(self.numeric_radio, 1)
        self.mode_button_group.idClicked.connect(self.on_mode_changed)
        
        mode_layout.addWidget(self.ascii_radio)
        mode_layout.addWidget(self.numeric_radio)
        mode_group.setLayout(mode_layout)

        # Output section
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout()

        self.output_display = QTextEdit()
        self.output_display.setReadOnly(True)
        self.output_display.setFont(QFont("Courier New", 10))
        self.output_display.setMinimumHeight(150)
        self.output_display.setPlaceholderText("Program output will appear here...")

        # Clear output button
        clear_btn = QPushButton("Clear Output")
        clear_btn.clicked.connect(self.clear_output)

        output_layout.addWidget(self.output_display)
        output_layout.addWidget(clear_btn)
        output_group.setLayout(output_layout)

        # Input section
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout()

        # Input instructions (will update based on mode)
        self.input_label = QLabel("Enter input (press Enter or click Send):")
        self.input_label.setWordWrap(True)

        # Input field and send button in horizontal layout
        input_row = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Courier New", 10))
        self.input_field.setPlaceholderText("Type input here...")
        self.input_field.returnPressed.connect(self.on_send_input)

        self.send_btn = QPushButton("Send")
        self.send_btn.clicked.connect(self.on_send_input)
        self.send_btn.setMaximumWidth(80)

        input_row.addWidget(self.input_field)
        input_row.addWidget(self.send_btn)

        # Mode hint label
        self.mode_hint = QLabel("Each character is sent as one ASCII byte (e.g., '5' → 0x35)")
        self.mode_hint.setStyleSheet("color: #888; font-size: 9px;")

        input_layout.addWidget(self.input_label)
        input_layout.addLayout(input_row)
        input_layout.addWidget(self.mode_hint)
        input_group.setLayout(input_layout)

        # Add all groups to main layout
        main_layout.addWidget(mode_group)
        main_layout.addWidget(output_group)
        main_layout.addWidget(input_group)

    def on_mode_changed(self, button_id):
        """Handle mode change"""
        self.numeric_mode = (button_id == 1)
        
        if self.numeric_mode:
            self.input_field.setPlaceholderText("Enter number 0-255...")
            self.mode_hint.setText("Number is sent as a single byte value (e.g., '25' → 0x19)")
        else:
            self.input_field.setPlaceholderText("Type input here...")
            self.mode_hint.setText("Each character is sent as one ASCII byte (e.g., '5' → 0x35)")

    def is_numeric_mode(self):
        """Check if numeric mode is active"""
        return self.numeric_mode

    def on_send_input(self):
        """Handle sending input to the program"""
        text = self.input_field.text()
        if not text:
            return
            
        if self.numeric_mode:
            # Parse as numeric value
            try:
                value = int(text)
                if not (0 <= value <= 255):
                    QMessageBox.warning(self, "Invalid Input", 
                                       "Value must be between 0 and 255.")
                    return
                # Emit numeric input signal
                self.numeric_input_submitted.emit(value)
                # Show feedback
                self.append_output(f"> {value} (0x{value:02X})\n", color="#00aa00")
            except ValueError:
                QMessageBox.warning(self, "Invalid Input",
                                   "Please enter a valid decimal number (0-255).")
                return
        else:
            # ASCII mode - emit string as before
            self.input_submitted.emit(text)
            # Show what was sent in output (for feedback)
            self.append_output(f"> {text}\n", color="#00aa00")

        # Clear input field
        self.input_field.clear()

    def append_output(self, text, color=None):
        """
        Append text to the output display.

        Args:
            text: Text to append
            color: Optional color in hex format (e.g., "#ff0000")
        """
        cursor = self.output_display.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)

        if color:
            # Insert with color
            format = cursor.charFormat()
            original_color = format.foreground()
            format.setForeground(QColor(color))
            cursor.setCharFormat(format)
            cursor.insertText(text)
            # Restore original color
            format.setForeground(original_color)
            cursor.setCharFormat(format)
        else:
            cursor.insertText(text)

        self.output_display.setTextCursor(cursor)
        self.output_display.ensureCursorVisible()

    def clear_output(self):
        """Clear the output display"""
        self.output_display.clear()

    def display_byte(self, value):
        """
        Display a single byte value as output.
        Behavior depends on current mode:
        - ASCII mode: Display as character if printable, hex otherwise
        - Numeric mode: Display as decimal number

        Args:
            value: Byte value (0-255)
        """
        if self.numeric_mode:
            # Numeric mode - display as decimal value with newline
            self.append_output(f"{value}\n")
        else:
            # ASCII mode - display as character if printable
            if 32 <= value <= 126:
                self.append_output(chr(value))
            elif value == 10:  # Newline
                self.append_output('\n')
            elif value == 13:  # Carriage return
                self.append_output('\r')
            elif value == 9:  # Tab
                self.append_output('\t')
            else:
                # Non-printable - show hex code
                self.append_output(f"[0x{value:02X}]", color="#888888")

    def display_char(self, char):
        """
        Display a character.

        Args:
            char: Character to display
        """
        self.append_output(char)

    def set_input_enabled(self, enabled):
        """
        Enable or disable input field.

        Args:
            enabled: True to enable, False to disable
        """
        self.input_field.setEnabled(enabled)
        self.send_btn.setEnabled(enabled)

