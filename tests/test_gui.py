import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication

def run_tests():
    # Setup app
    app = QApplication.instance()
    if app is None:
        app = QApplication([])

    print("Testing MainWindow...")
    from src.gui.main_window import MainWindow
    window = MainWindow()
    if window.windowTitle() != "CAL-EB: 8-Bit Computer Trainer":
        raise AssertionError("Window title incorrect")

    print("Testing CodeEditor...")
    from src.gui.editor import CodeEditor
    editor = CodeEditor()
    if editor.editor.toPlainText() is None:
         raise AssertionError("Editor content is None")

    print("Testing ControlPanel...")
    from src.gui.controls import ControlPanel
    panel = ControlPanel()
    if panel.btn_run.text() != "Run":
         raise AssertionError("Run button text incorrect")

    print("Testing CircuitView...")
    from src.gui.circuit_view import CircuitView
    cv = CircuitView()
    items = cv.scene.items()
    if len(items) == 0:
        raise AssertionError("CircuitView scene is empty")
    print(f"  - Found {len(items)} items in scene")

    print("GUI Tests Passed!")

if __name__ == "__main__":
    try:
        run_tests()
    except Exception as e:
        print(f"GUI Test Failed: {e}")
        sys.exit(1)
