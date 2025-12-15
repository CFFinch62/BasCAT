from PyQt6.QtWidgets import QGraphicsRectItem, QGraphicsTextItem, QGraphicsItem
from PyQt6.QtGui import QBrush, QColor, QPen, QFont, QPainterPath, QPainterPathStroker
from PyQt6.QtCore import Qt

class VisualComponent(QGraphicsRectItem):
    def __init__(self, x, y, width, height, label, show_value=True):
        # Create rectangle at LOCAL origin (0,0), then position the item in scene
        super().__init__(0, 0, width, height)
        self.setPos(x, y)  # Position the item in scene coordinates

        self.setBrush(QBrush(QColor("#2a2a2a")))
        self.setPen(QPen(QColor("#00ffcc"), 2))

        # Store dimensions
        self.comp_width = width
        self.comp_height = height
        self.show_value = show_value

        # Label text
        self.text = QGraphicsTextItem(label, self)
        self.text.setDefaultTextColor(QColor("#00ffcc"))
        label_font = QFont("Arial", 11, QFont.Weight.Bold)
        self.text.setFont(label_font)

        if show_value:
            # Label at top, value below
            text_width = self.text.boundingRect().width()
            self.text.setPos((width - text_width) / 2, 3)

            # Value display
            self.value_text = QGraphicsTextItem("0x00", self)
            self.value_text.setDefaultTextColor(QColor("#ffffff"))
            value_font = QFont("Courier New", 12, QFont.Weight.Bold)
            self.value_text.setFont(value_font)

            value_width = self.value_text.boundingRect().width()
            value_height = self.value_text.boundingRect().height()
            self.value_text.setPos((width - value_width) / 2, (height - value_height) / 2 + 5)
        else:
            # No value - center the label
            self.value_text = None
            text_width = self.text.boundingRect().width()
            text_height = self.text.boundingRect().height()
            self.text.setPos((width - text_width) / 2, (height - text_height) / 2)

    def set_value(self, value):
        if not self.show_value or self.value_text is None:
            return

        if isinstance(value, int):
            self.value_text.setPlainText(f"0x{value:02X}")
        else:
            self.value_text.setPlainText(str(value))

        # Re-center value text
        value_width = self.value_text.boundingRect().width()
        value_height = self.value_text.boundingRect().height()
        self.value_text.setPos((self.comp_width - value_width) / 2, (self.comp_height - value_height) / 2 + 5)

class CPUVisual(VisualComponent):
    def __init__(self, x, y):
        # CPU doesn't show a value, just the label centered
        super().__init__(x, y, 200, 250, "CPU", show_value=False)
        self.setBrush(QBrush(QColor("#1a1a3a")))
        self.setPen(QPen(QColor("#5555ff"), 3))

        # Add ALU as a sub-component inside CPU
        # Position it in the lower portion of the CPU block
        self.alu = ALUSubVisual(40, 160)  # Position relative to CPU's local coordinates
        self.alu.setParentItem(self)  # Make ALU a child of CPU

        # Add flags display below ALU
        self.flags_text = QGraphicsTextItem("Flags: ZNCO [0000]", self)
        self.flags_text.setDefaultTextColor(QColor("#aaaaaa"))
        flags_font = QFont("Courier New", 9, QFont.Weight.Normal)
        self.flags_text.setFont(flags_font)
        flags_width = self.flags_text.boundingRect().width()
        self.flags_text.setPos((200 - flags_width) / 2, 220)

    def update_flags(self, flags_dict):
        """Update the flags display: flags_dict = {'Z': 0/1, 'N': 0/1, 'C': 0/1, 'O': 0/1}"""
        z = flags_dict.get('Z', 0)
        n = flags_dict.get('N', 0)
        c = flags_dict.get('C', 0)
        o = flags_dict.get('O', 0)
        flags_str = f"Flags: ZNCO [{z}{n}{c}{o}]"
        self.flags_text.setPlainText(flags_str)
        # Re-center
        flags_width = self.flags_text.boundingRect().width()
        self.flags_text.setPos((200 - flags_width) / 2, 220)

class ALUSubVisual(VisualComponent):
    """ALU as a sub-component inside CPU - smaller, nested version"""
    def __init__(self, x, y):
        # Smaller ALU for inside the CPU
        super().__init__(x, y, 120, 50, "ALU", show_value=False)
        self.setBrush(QBrush(QColor("#3a1a1a")))
        self.setPen(QPen(QColor("#ff5555"), 2))
        # Adjust label font to be smaller
        label_font = QFont("Arial", 10, QFont.Weight.Bold)
        self.text.setFont(label_font)
        # Re-center text
        text_width = self.text.boundingRect().width()
        text_height = self.text.boundingRect().height()
        self.text.setPos((120 - text_width) / 2, (50 - text_height) / 2)

class ALUVisual(VisualComponent):
    """Standalone ALU visual - kept for backward compatibility but won't be used"""
    def __init__(self, x, y):
        # ALU doesn't show a value, just the label centered
        super().__init__(x, y, 100, 60, "ALU", show_value=False)
        self.setBrush(QBrush(QColor("#3a1a1a")))
        self.setPen(QPen(QColor("#ff5555"), 3))

class RegisterVisual(VisualComponent):
    def __init__(self, x, y, name):
        # Registers show their name and value
        super().__init__(x, y, 80, 55, name, show_value=True)
        self.setBrush(QBrush(QColor("#1a3a1a")))
        self.setPen(QPen(QColor("#55ff55"), 2))

class MemoryVisual(VisualComponent):
    def __init__(self, x, y):
        # Memory is RAM - shows label and size info
        super().__init__(x, y, 120, 60, "RAM", show_value=False)
        self.setBrush(QBrush(QColor("#3a3a1a")))
        self.setPen(QPen(QColor("#ffff55"), 3))

        # Add size indicator below the RAM label
        self.size_text = QGraphicsTextItem("256 bytes", self)
        self.size_text.setDefaultTextColor(QColor("#999999"))
        size_font = QFont("Arial", 8, QFont.Weight.Normal)
        self.size_text.setFont(size_font)
        size_width = self.size_text.boundingRect().width()
        self.size_text.setPos((120 - size_width) / 2, 35)

class IOPortVisual(VisualComponent):
    """Visual representation of I/O ports"""
    def __init__(self, x, y):
        super().__init__(x, y, 100, 70, "I/O", show_value=False)
        self.setBrush(QBrush(QColor("#3a1a3a")))
        self.setPen(QPen(QColor("#ff55ff"), 3))

        # Reposition the main "I/O" label to the top instead of centered
        text_width = self.text.boundingRect().width()
        self.text.setPos((100 - text_width) / 2, 3)

        # Add port labels below the main label
        self.input_label = QGraphicsTextItem("IN: 0xFF", self)
        self.input_label.setDefaultTextColor(QColor("#aaaaaa"))
        input_font = QFont("Courier New", 8, QFont.Weight.Normal)
        self.input_label.setFont(input_font)
        self.input_label.setPos(10, 28)

        self.output_label = QGraphicsTextItem("OUT: 0xFE", self)
        self.output_label.setDefaultTextColor(QColor("#aaaaaa"))
        output_font = QFont("Courier New", 8, QFont.Weight.Normal)
        self.output_label.setFont(output_font)
        self.output_label.setPos(10, 46)


class StackVisual(VisualComponent):
    """Visual representation of the stack showing top entries"""
    
    # Signal emitted when stack is clicked
    clicked = None  # Will be set by CircuitView
    
    def __init__(self, x, y, memory=None):
        super().__init__(x, y, 85, 120, "Stack", show_value=False)
        self.setBrush(QBrush(QColor("#2a1a2a")))
        self.setPen(QPen(QColor("#aa55aa"), 2))
        self.memory = memory
        self.sp_value = 0xFD
        
        # Reposition the main "Stack" label to the top
        text_width = self.text.boundingRect().width()
        self.text.setPos((85 - text_width) / 2, 2)
        
        # Stack entry labels (show top 4 entries)
        self.entry_labels = []
        entry_font = QFont("Courier New", 8, QFont.Weight.Normal)
        
        for i in range(4):
            label = QGraphicsTextItem("--: --", self)
            label.setDefaultTextColor(QColor("#aaaaaa"))
            label.setFont(entry_font)
            label.setPos(5, 22 + i * 18)
            self.entry_labels.append(label)
            
        # Click hint
        self.hint_text = QGraphicsTextItem("▼ Click", self)
        self.hint_text.setDefaultTextColor(QColor("#666666"))
        hint_font = QFont("Arial", 7)
        self.hint_text.setFont(hint_font)
        hint_width = self.hint_text.boundingRect().width()
        self.hint_text.setPos((85 - hint_width) / 2, 100)
        
        # Make clickable
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
    def set_memory(self, memory):
        """Set memory reference for reading stack contents"""
        self.memory = memory
        self.update_display()
        
    def set_sp(self, sp_value):
        """Update stack pointer and refresh display"""
        self.sp_value = sp_value
        self.update_display()
        
    def update_display(self):
        """Update the stack entry display"""
        for i, label in enumerate(self.entry_labels):
            addr = 0xFD - i  # Stack addresses from top
            
            if addr <= self.sp_value:
                # Below or at SP - empty
                label.setPlainText(f"{addr:02X}: --")
                label.setDefaultTextColor(QColor("#555555"))
            else:
                # Above SP - has data
                if self.memory:
                    try:
                        value = self.memory._data[addr]
                        label.setPlainText(f"{addr:02X}: {value:02X}")
                        label.setDefaultTextColor(QColor("#55ff55"))
                    except (IndexError, AttributeError):
                        label.setPlainText(f"{addr:02X}: ??")
                        label.setDefaultTextColor(QColor("#ff5555"))
                else:
                    label.setPlainText(f"{addr:02X}: ??")
                    label.setDefaultTextColor(QColor("#888888"))
                    
    def mousePressEvent(self, event):
        """Handle click to toggle memory panel"""
        if self.clicked:
            self.clicked()
        super().mousePressEvent(event)
        
    def hoverEnterEvent(self, event):
        """Highlight on hover"""
        self.setPen(QPen(QColor("#ff88ff"), 3))
        super().hoverEnterEvent(event)
        
    def hoverLeaveEvent(self, event):
        """Remove highlight"""
        self.setPen(QPen(QColor("#aa55aa"), 2))
        super().hoverLeaveEvent(event)


class BusVisual(QGraphicsItem):
    def __init__(self, path_points, label="Bus"):
        super().__init__()
        self.points = path_points # List of (x, y) tuples
        self.label = label
        self.active = False
        self.color = QColor("#444444")
        self.active_color = QColor("#00ff00")
        
    def boundingRect(self):
        return self.shape().boundingRect()

    def shape(self):
        path = QPainterPath()
        if not self.points:
            return path
        path.moveTo(self.points[0][0], self.points[0][1])
        for x, y in self.points[1:]:
            path.lineTo(x, y)
        
        # Stroke width buffering for hit testing/bounds
        stroker = QPainterPathStroker()
        stroker.setWidth(10) # Hit area width
        return stroker.createStroke(path)

    def paint(self, painter, option, widget):
        pen = QPen(self.active_color if self.active else self.color)
        pen.setWidth(4)
        painter.setPen(pen)

        if len(self.points) < 2:
            return

        # Draw lines connecting all points
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            painter.drawLine(int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]))

class DataPacket(QGraphicsItem):
    def __init__(self, path_points, color=QColor("#00ff9d")):
        super().__init__()
        self.points = path_points
        self.color = color
        self.progress = 0.0 # 0.0 to 1.0 along the path
        self.radius = 5
        
        # Calculate total length for accurate speed
        self.total_length = 0
        self.segments = []
        if len(self.points) >= 2:
            for i in range(len(self.points) - 1):
                p1 = self.points[i]
                p2 = self.points[i+1]
                # Dist
                d = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
                self.segments.append(d)
                self.total_length += d
                
    def boundingRect(self):
        return QGraphicsRectItem(0,0,1,1).boundingRect() # simplified

    def shape(self):
        path = QPainterPath()
        path.addEllipse(self.pos(), self.radius, self.radius)
        return path

    def paint(self, painter, option, widget):
        painter.setBrush(QBrush(self.color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(int(-self.radius), int(-self.radius), int(self.radius*2), int(self.radius*2))
        
    def set_progress(self, val):
        self.progress = val
        # Calculate position based on progress
        distance = val * self.total_length
        current_dist = 0
        
        for i, seg_len in enumerate(self.segments):
            if current_dist + seg_len >= distance:
                # We are in this segment
                ratio = (distance - current_dist) / seg_len if seg_len > 0 else 0
                p1 = self.points[i]
                p2 = self.points[i+1]
                
                new_x = p1[0] + (p2[0] - p1[0]) * ratio
                new_y = p1[1] + (p2[1] - p1[1]) * ratio
                self.setPos(new_x, new_y)
                break
            current_dist += seg_len
        self.update()
