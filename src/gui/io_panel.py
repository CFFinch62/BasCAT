"""
I/O Panel Widget for BasCAT

Provides input and output interface for programs.
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTextEdit,
                             QLineEdit, QPushButton, QLabel, QGroupBox)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, pyqtSignal


class IOPanel(QWidget):
    """
    I/O Panel widget showing input field and output display.
    """

    # Signal emitted when user wants to send input
    input_submitted = pyqtSignal(str)  # Input string

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Setup the UI layout"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(5)

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

        # Input instructions
        input_label = QLabel("Enter input (press Enter or click Send):")
        input_label.setWordWrap(True)

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

        # Mode selection (future feature - character vs line mode)
        mode_label = QLabel("Input mode: Character-by-character (each char is one byte)")
        mode_label.setStyleSheet("color: #888; font-size: 9px;")

        input_layout.addWidget(input_label)
        input_layout.addLayout(input_row)
        input_layout.addWidget(mode_label)
        input_group.setLayout(input_layout)

        # Add both groups to main layout
        main_layout.addWidget(output_group)
        main_layout.addWidget(input_group)

    def on_send_input(self):
        """Handle sending input to the program"""
        text = self.input_field.text()
        if text:
            # Emit signal with the input text
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

        Args:
            value: Byte value (0-255)
        """
        # Display as character if printable ASCII
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
