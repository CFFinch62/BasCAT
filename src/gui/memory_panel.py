"""
Memory Panel Widget for BasCAT

Shows detailed memory contents including:
- Full memory dump (address, hex, decimal, ASCII)
- Stack region highlighting
- Variable region highlighting  
- I/O port indicators
"""

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                              QTableWidgetItem, QLabel, QGroupBox, QHeaderView,
                              QScrollArea, QPushButton, QComboBox)
from PyQt6.QtGui import QFont, QColor, QBrush
from PyQt6.QtCore import Qt, pyqtSignal


class MemoryPanel(QWidget):
    """
    Memory viewer panel showing memory contents in a table format.
    Highlights stack region and variable locations.
    """
    
    def __init__(self, memory=None):
        super().__init__()
        self.memory = memory
        self.sp_value = 0xFD  # Default stack pointer
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(2)
        
        # Header with controls (compact)
        header = QHBoxLayout()
        header.setSpacing(5)
        
        # View mode selector
        header.addWidget(QLabel("View:"))
        self.view_mode = QComboBox()
        self.view_mode.addItems(["Stack Region", "Variables", "Full Memory", "I/O Ports"])
        self.view_mode.currentTextChanged.connect(self.on_view_changed)
        header.addWidget(self.view_mode)
        
        header.addStretch()
        
        # Stack info (inline with header)
        self.stack_info = QLabel("SP: 0xFD | Entries: 0")
        self.stack_info.setStyleSheet("color: #888; font-size: 9px;")
        header.addWidget(self.stack_info)
        
        # Refresh button
        refresh_btn = QPushButton("↻")
        refresh_btn.setMaximumWidth(30)
        refresh_btn.setToolTip("Refresh display")
        refresh_btn.clicked.connect(self.refresh_display)
        header.addWidget(refresh_btn)
        
        layout.addLayout(header)
        
        # Memory table (compact)
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Addr", "Hex", "Dec", "Chr", "Region"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setFont(QFont("Courier New", 9))  # Smaller font
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setDefaultSectionSize(18)  # Compact rows
        self.table.verticalHeader().setVisible(False)  # Hide row numbers
        self.table.setStyleSheet("""
            QTableWidget {
                background-color: #1e1e1e;
                alternate-background-color: #252525;
                color: #e0e0e0;
            }
            QTableWidget::item:selected {
                background-color: #3a3a00;
            }
            QHeaderView::section {
                background-color: #2a2a2a;
                color: #00ffcc;
                padding: 2px;
                border: 1px solid #333;
                font-size: 9px;
            }
        """)
        
        layout.addWidget(self.table)
        
        # Set minimum height so dock can be resized smaller
        self.setMinimumHeight(100)
        
        # Initial display
        self.on_view_changed("Stack Region")
        
    def set_memory(self, memory):
        """Set the memory object to read from"""
        self.memory = memory
        self.refresh_display()
        
    def set_sp(self, sp_value):
        """Update stack pointer value"""
        self.sp_value = sp_value
        self.update_stack_info()
        if self.view_mode.currentText() == "Stack Region":
            self.refresh_display()
            
    def update_stack_info(self):
        """Update the stack info bar"""
        stack_entries = 0xFD - self.sp_value
        self.stack_info.setText(f"SP: 0x{self.sp_value:02X} | Stack entries: {stack_entries}")
        
    def on_view_changed(self, mode):
        """Handle view mode change"""
        self.refresh_display()
        
    def refresh_display(self):
        """Refresh the memory display based on current view mode"""
        mode = self.view_mode.currentText()
        
        if mode == "Stack Region":
            self.show_stack_region()
        elif mode == "Variables":
            self.show_variables()
        elif mode == "Full Memory":
            self.show_full_memory()
        elif mode == "I/O Ports":
            self.show_io_ports()
            
    def show_stack_region(self):
        """Show stack memory region (0xF0-0xFD)"""
        self.table.setRowCount(0)
        
        # Stack grows downward from 0xFD
        for addr in range(0xFD, 0xEF, -1):  # Show 0xFD down to 0xF0
            self.add_memory_row(addr, "Stack")
            
        self.update_stack_info()
        
    def show_variables(self):
        """Show variable memory region (0x80-0x99 for A-Z)"""
        self.table.setRowCount(0)
        
        var_names = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, var_name in enumerate(var_names):
            addr = 0x80 + i  # A=0x80, B=0x81, etc.
            self.add_memory_row(addr, f"Var {var_name}")
            
    def show_full_memory(self):
        """Show all 256 bytes of memory (0x00-0xFF)"""
        self.table.setRowCount(0)
        
        for addr in range(0, 256):
            region = self.get_region_name(addr)
            self.add_memory_row(addr, region)
            
    def show_io_ports(self):
        """Show I/O port addresses"""
        self.table.setRowCount(0)
        
        self.add_memory_row(0xFE, "OUT Port")
        self.add_memory_row(0xFF, "IN Port")
        
    def add_memory_row(self, addr, region):
        """Add a row to the memory table"""
        row = self.table.rowCount()
        self.table.insertRow(row)
        
        # Get value from memory
        if self.memory:
            try:
                value = self.memory._data[addr]  # Direct access to avoid I/O side effects
            except (IndexError, AttributeError):
                value = 0
        else:
            value = 0
            
        # Address
        addr_item = QTableWidgetItem(f"0x{addr:02X}")
        addr_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Hex value
        hex_item = QTableWidgetItem(f"0x{value:02X}")
        hex_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Decimal value
        dec_item = QTableWidgetItem(str(value))
        dec_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # ASCII (if printable)
        if 32 <= value <= 126:
            ascii_char = chr(value)
        else:
            ascii_char = "·"
        ascii_item = QTableWidgetItem(ascii_char)
        ascii_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Region
        region_item = QTableWidgetItem(region)
        
        # Highlight based on region
        if "Stack" in region and addr > self.sp_value:
            # Active stack entry (above SP)
            for item in [addr_item, hex_item, dec_item, ascii_item, region_item]:
                item.setBackground(QBrush(QColor("#2a3a2a")))
                item.setForeground(QBrush(QColor("#55ff55")))
        elif addr == self.sp_value and "Stack" in region:
            # Stack pointer location
            for item in [addr_item, hex_item, dec_item, ascii_item, region_item]:
                item.setBackground(QBrush(QColor("#3a3a1a")))
                item.setForeground(QBrush(QColor("#ffff55")))
            region_item.setText(region + " ◄SP")
        elif "Port" in region:
            # I/O ports
            for item in [addr_item, hex_item, dec_item, ascii_item, region_item]:
                item.setForeground(QBrush(QColor("#ff55ff")))
        elif "Var" in region:
            # Variables
            for item in [addr_item, hex_item, dec_item, ascii_item, region_item]:
                item.setForeground(QBrush(QColor("#55ffff")))
                
        self.table.setItem(row, 0, addr_item)
        self.table.setItem(row, 1, hex_item)
        self.table.setItem(row, 2, dec_item)
        self.table.setItem(row, 3, ascii_item)
        self.table.setItem(row, 4, region_item)
        
    def get_region_name(self, addr):
        """Get region name for an address"""
        if addr >= 0xFE:
            return "I/O Port"
        elif addr > 0xED:
            return "Stack"
        elif 0x80 <= addr <= 0x99:
            var_name = chr(ord('A') + addr - 0x80)
            return f"Var {var_name}"
        elif addr < 0x80:
            return "Program"
        else:
            return "Free RAM"
