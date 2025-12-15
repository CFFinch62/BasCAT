from PyQt6.QtWidgets import QPlainTextEdit, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QFont, QTextCursor, QColor, QTextFormat
from PyQt6.QtCore import Qt

class CodeEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.editor = QPlainTextEdit()
        font = QFont("Monospace")
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.editor.setFont(font)

        self.layout.addWidget(self.editor)

        # Default placeholder code - demonstrates I/O
        self.editor.setPlainText(
            "; CAL-EB Assembly - I/O Demo\n"
            "; Type input in the I/O panel, then run\n"
            "IN A          ; Read input to register A\n"
            "OUT A         ; Echo it back to output\n"
            "HALT\n"
        )

        # Track current highlighted line
        self.current_highlight_line = -1

    def get_code(self):
        return self.editor.toPlainText()

    def highlight_line(self, line_number):
        """Highlight the specified line number (0-based)"""
        self.current_highlight_line = line_number

        # Create a selection for the line
        block = self.editor.document().findBlockByLineNumber(line_number)

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
