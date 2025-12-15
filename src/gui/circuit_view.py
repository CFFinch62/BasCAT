from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QPainter, QBrush, QColor, QPen
from PyQt6.QtCore import Qt

class CircuitView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 700, 550)
        self.setScene(self.scene)

        # Render settings for high quality
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setBackgroundBrush(QBrush(QColor("#1e1e1e")))
        
        # Allow this view to shrink so bottom dock can expand
        self.setMinimumHeight(200)

        # Grid lines (optional visual aid)
        self.draw_grid()
        self.setup_scene()


    def draw_grid(self):
        pen = QPen(QColor("#2a2a2a"))
        pen.setWidth(1)
        grid_size = 50
        
        for x in range(0, int(self.scene.width()), grid_size):
            self.scene.addLine(x, 0, x, self.scene.height(), pen)
        for y in range(0, int(self.scene.height()), grid_size):
            self.scene.addLine(0, y, self.scene.width(), y, pen)

    def setup_scene(self):
        from src.gui.components.graphics import CPUVisual, RegisterVisual, MemoryVisual, IOPortVisual, BusVisual

        # Layout constants - everything is positioned relative to buses
        LEFT_BUS_X = 130        # Data bus X position
        RIGHT_BUS_X = 520       # Address bus X position
        CENTER_X = (LEFT_BUS_X + RIGHT_BUS_X) / 2  # Center between buses = 325

        REG_WIDTH = 80
        REG_HEIGHT = 55
        REG_SPACING = 70        # Vertical spacing between registers

        # ===== BUSES (draw first as background) =====
        # Data Bus - vertical line on the left
        self.data_bus_main = BusVisual([(LEFT_BUS_X, 30), (LEFT_BUS_X, 480)], "Data Bus")
        self.scene.addItem(self.data_bus_main)

        # Address Bus - vertical line on the right
        self.addr_bus_main = BusVisual([(RIGHT_BUS_X, 30), (RIGHT_BUS_X, 480)], "Addr Bus")
        self.scene.addItem(self.addr_bus_main)

        # ===== LEFT SIDE: General Purpose Registers (A, B, C, D) =====
        # Add label for general purpose registers
        from PyQt6.QtWidgets import QGraphicsTextItem
        from PyQt6.QtGui import QFont, QColor

        LEFT_REG_X = 20
        gp_label = QGraphicsTextItem("General Purpose")
        gp_label.setDefaultTextColor(QColor("#888888"))
        gp_label.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        gp_label.setPos(LEFT_REG_X - 5, 28)
        self.scene.addItem(gp_label)

        self.reg_a = RegisterVisual(LEFT_REG_X, 50, "A")
        self.reg_b = RegisterVisual(LEFT_REG_X, 50 + REG_SPACING, "B")
        self.reg_c = RegisterVisual(LEFT_REG_X, 50 + REG_SPACING * 2, "C")
        self.reg_d = RegisterVisual(LEFT_REG_X, 50 + REG_SPACING * 3, "D")

        self.reg_a.set_value(0)
        self.reg_b.set_value(0)
        self.reg_c.set_value(0)
        self.reg_d.set_value(0)

        self.scene.addItem(self.reg_a)
        self.scene.addItem(self.reg_b)
        self.scene.addItem(self.reg_c)
        self.scene.addItem(self.reg_d)

        # Connections from left registers to data bus
        reg_center_y = lambda row: 50 + row * REG_SPACING + REG_HEIGHT / 2
        self.bus_a = BusVisual([(LEFT_REG_X + REG_WIDTH, reg_center_y(0)), (LEFT_BUS_X, reg_center_y(0))])
        self.bus_b = BusVisual([(LEFT_REG_X + REG_WIDTH, reg_center_y(1)), (LEFT_BUS_X, reg_center_y(1))])
        self.bus_c = BusVisual([(LEFT_REG_X + REG_WIDTH, reg_center_y(2)), (LEFT_BUS_X, reg_center_y(2))])
        self.bus_d = BusVisual([(LEFT_REG_X + REG_WIDTH, reg_center_y(3)), (LEFT_BUS_X, reg_center_y(3))])

        self.scene.addItem(self.bus_a)
        self.scene.addItem(self.bus_b)
        self.scene.addItem(self.bus_c)
        self.scene.addItem(self.bus_d)

        # ===== RIGHT SIDE: Special Registers (PC, IR, MAR) =====
        # Add label for special registers
        RIGHT_REG_X = RIGHT_BUS_X + 30
        sp_label = QGraphicsTextItem("Special Registers")
        sp_label.setDefaultTextColor(QColor("#888888"))
        sp_label.setFont(QFont("Arial", 9, QFont.Weight.Bold))
        sp_label.setPos(RIGHT_REG_X - 5, 28)
        self.scene.addItem(sp_label)

        self.pc = RegisterVisual(RIGHT_REG_X, 50, "PC")
        self.ir = RegisterVisual(RIGHT_REG_X, 50 + REG_SPACING, "IR")
        self.mar = RegisterVisual(RIGHT_REG_X, 50 + REG_SPACING * 2, "MAR")
        self.sp = RegisterVisual(RIGHT_REG_X, 50 + REG_SPACING * 3, "SP")

        self.pc.set_value(0)
        self.ir.set_value(0)
        self.mar.set_value(0)
        self.sp.set_value(0xFD)

        self.scene.addItem(self.pc)
        self.scene.addItem(self.ir)
        self.scene.addItem(self.mar)
        self.scene.addItem(self.sp)

        # Connections from address bus to right registers
        self.bus_pc = BusVisual([(RIGHT_BUS_X, reg_center_y(0)), (RIGHT_REG_X, reg_center_y(0))])
        self.bus_ir = BusVisual([(RIGHT_BUS_X, reg_center_y(1)), (RIGHT_REG_X, reg_center_y(1))])
        self.bus_mar = BusVisual([(RIGHT_BUS_X, reg_center_y(2)), (RIGHT_REG_X, reg_center_y(2))])
        self.bus_sp = BusVisual([(RIGHT_BUS_X, reg_center_y(3)), (RIGHT_REG_X, reg_center_y(3))])

        self.scene.addItem(self.bus_pc)
        self.scene.addItem(self.bus_ir)
        self.scene.addItem(self.bus_mar)
        self.scene.addItem(self.bus_sp)

        # ===== CENTER: CPU Block (centered between buses) =====
        CPU_WIDTH = 200
        CPU_HEIGHT = 250
        cpu_x = CENTER_X - CPU_WIDTH / 2
        self.cpu_rect = CPUVisual(cpu_x, 60)
        self.scene.addItem(self.cpu_rect)

        # Connections from CPU to both buses
        cpu_center_y = 60 + CPU_HEIGHT / 2
        self.bus_cpu_data = BusVisual([(cpu_x, cpu_center_y), (LEFT_BUS_X, cpu_center_y)])
        self.bus_cpu_addr = BusVisual([(cpu_x + CPU_WIDTH, cpu_center_y), (RIGHT_BUS_X, cpu_center_y)])
        self.scene.addItem(self.bus_cpu_data)
        self.scene.addItem(self.bus_cpu_addr)

        # ===== MEMORY (centered, below CPU) =====
        MEM_WIDTH = 120
        MEM_HEIGHT = 60
        mem_x = CENTER_X - MEM_WIDTH / 2
        self.memory = MemoryVisual(mem_x, 340)  # Moved up from 410 since ALU is now inside CPU
        self.scene.addItem(self.memory)

        # Memory connections to buses
        mem_center_y = 340 + MEM_HEIGHT / 2
        self.bus_mem_data = BusVisual([(mem_x, mem_center_y), (LEFT_BUS_X, mem_center_y)])
        self.bus_mem_addr = BusVisual([(mem_x + MEM_WIDTH, mem_center_y), (RIGHT_BUS_X, mem_center_y)])
        self.scene.addItem(self.bus_mem_data)
        self.scene.addItem(self.bus_mem_addr)

        # ===== I/O PORTS (below memory) =====
        IO_WIDTH = 100
        IO_HEIGHT = 70
        io_x = CENTER_X - IO_WIDTH / 2
        self.io_port = IOPortVisual(io_x, 430)
        self.scene.addItem(self.io_port)

        # I/O port connections to buses
        io_center_y = 430 + IO_HEIGHT / 2
        self.bus_io_data = BusVisual([(io_x, io_center_y), (LEFT_BUS_X, io_center_y)])
        self.scene.addItem(self.bus_io_data)

        # ===== STACK VISUAL (next to I/O) =====
        from src.gui.components.graphics import StackVisual
        STACK_WIDTH = 85
        stack_x = io_x + IO_WIDTH + 20  # Right of I/O
        self.stack_visual = StackVisual(stack_x, 390)
        self.stack_visual.clicked = self.on_stack_clicked
        self.scene.addItem(self.stack_visual)

        # Connect signals
        from src.core.signals import signals
        signals.bus_transfer.connect(self.on_bus_transfer)
        signals.register_updated.connect(self.on_register_updated)
        signals.pc_updated.connect(self.on_pc_updated)
        signals.ir_updated.connect(self.on_ir_updated)
        signals.mar_updated.connect(self.on_mar_updated)
        signals.sp_updated.connect(self.on_sp_updated)
        signals.flags_updated.connect(self.on_flags_updated)

    def on_bus_transfer(self, source, dest, value, bus_type):
        from src.gui.components.graphics import DataPacket
        from PyQt6.QtCore import QVariantAnimation, QEasingCurve

        # Determine path based on source/dest (Simplified mapping)
        # Ideally we have a routing map. For now, assume everything goes via Main Data Bus?
        # Or just animate on the specific bus segment if known.

        # Demo Animation: Animate along the data bus (LEFT_BUS_X = 130)
        path = [(130, 50), (130, 480)]  # Default - along data bus
        if source == "Memory":
            path = [(130, 480), (130, 50)]  # Memory (bottom) to CPU (top)

        packet = DataPacket(path)
        self.scene.addItem(packet)

        anim = QVariantAnimation(self)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setDuration(500) # 500ms
        anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        anim.valueChanged.connect(packet.set_progress)
        anim.finished.connect(lambda: self.scene.removeItem(packet))
        anim.start()

    def on_register_updated(self, register_name, value):
        """Update register visual when register value changes"""
        register_map = {
            "A": self.reg_a,
            "B": self.reg_b,
            "C": self.reg_c,
            "D": self.reg_d
        }
        if register_name in register_map:
            register_map[register_name].set_value(value)

    def on_pc_updated(self, value):
        """Update PC visual when program counter changes"""
        self.pc.set_value(value)

    def on_ir_updated(self, value):
        """Update IR visual when instruction register changes"""
        self.ir.set_value(value)

    def on_mar_updated(self, value):
        """Update MAR visual when memory address register changes"""
        self.mar.set_value(value)

    def on_sp_updated(self, value):
        """Update SP visual when stack pointer changes"""
        self.sp.set_value(value)
        # Also update stack visual
        self.stack_visual.set_sp(value)

    def on_flags_updated(self, flags_dict):
        """Update CPU flags display when ALU flags change"""
        self.cpu_rect.update_flags(flags_dict)

    def on_stack_clicked(self):
        """Handle stack visual click - emit signal to toggle memory panel"""
        from src.core.signals import signals
        signals.memory_panel_toggle.emit()

    def set_memory(self, memory):
        """Set memory reference for stack visual"""
        self.stack_visual.set_memory(memory)
