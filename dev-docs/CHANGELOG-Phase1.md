# CHANGELOG - Phase 1: Architecture Fix - ALU Integration

**Date**: December 13, 2025
**Status**: ✅ COMPLETED

---

## Overview

Phase 1 focused on fixing the architectural representation of the ALU component. Previously, the ALU was incorrectly displayed as a standalone component outside the CPU in the circuit visualization, which was architecturally misleading. The ALU is a functional unit inside the CPU, and this phase corrected that representation both visually and logically.

---

## Goals

- [x] Make ALU a visual sub-component inside the CPU block
- [x] Remove standalone ALU visualization from circuit view
- [x] Remove direct ALU-to-bus connections
- [x] Add flags display to show ALU state
- [x] Maintain all existing functionality
- [x] Ensure all tests pass

---

## Changes Made

### 1. Enhanced CPU Visual Component

**File**: [src/gui/components/graphics.py](../src/gui/components/graphics.py)

#### Created `ALUSubVisual` Class
- New component class for the ALU to be displayed inside the CPU
- Smaller dimensions (120x50) to fit within CPU block
- Styled with red theme (#ff5555 border, #3a1a1a background)
- Uses smaller font (10pt) for compact display

#### Enhanced `CPUVisual` Class
- Added ALU as a child component using Qt's parent-child relationship
- Positioned ALU at coordinates (40, 160) relative to CPU's local coordinate system
- Added flags display showing ALU status: "Flags: ZNCO [0000]"
- Implemented `update_flags()` method to update flag display dynamically
- Flags positioned at bottom of CPU block (y=220)

**Code Changes**:
```python
class CPUVisual(VisualComponent):
    def __init__(self, x, y):
        super().__init__(x, y, 200, 250, "CPU", show_value=False)
        # ... existing code ...

        # Add ALU as a sub-component inside CPU
        self.alu = ALUSubVisual(40, 160)
        self.alu.setParentItem(self)  # Parent-child relationship

        # Add flags display
        self.flags_text = QGraphicsTextItem("Flags: ZNCO [0000]", self)
        # ... styling ...

    def update_flags(self, flags_dict):
        """Update the flags display"""
        z = flags_dict.get('Z', 0)
        n = flags_dict.get('N', 0)
        c = flags_dict.get('C', 0)
        o = flags_dict.get('O', 0)
        flags_str = f"Flags: ZNCO [{z}{n}{c}{o}]"
        self.flags_text.setPlainText(flags_str)
```

---

### 2. Updated Circuit View Layout

**File**: [src/gui/circuit_view.py](../src/gui/circuit_view.py)

#### Removed Standalone ALU Components
- Removed standalone `ALUVisual` instantiation (previously at line 122)
- Removed ALU-to-bus connection visuals (lines 127-130)
- Updated imports to remove `ALUVisual` reference

#### Adjusted Component Positions
- Memory component moved from y=410 to y=340 (70 pixels up)
- This utilizes the space previously occupied by standalone ALU
- Updated memory bus connection y-coordinate calculations

#### Added Flags Signal Connection
- Connected `signals.flags_updated` to `on_flags_updated()` handler
- New handler method forwards flag updates to CPU visual component

**Code Changes**:
```python
def setup_scene(self):
    from src.gui.components.graphics import CPUVisual, RegisterVisual, MemoryVisual, BusVisual
    # Removed ALUVisual from imports

    # ... CPU setup (unchanged) ...

    # Memory moved up since ALU is now inside CPU
    self.memory = MemoryVisual(mem_x, 340)  # Was 410

    # Connect flags signal
    signals.flags_updated.connect(self.on_flags_updated)

def on_flags_updated(self, flags_dict):
    """Update CPU flags display when ALU flags change"""
    self.cpu_rect.update_flags(flags_dict)
```

---

### 3. Added Flags Signal

**File**: [src/core/signals.py](../src/core/signals.py)

#### New Signal Definition
- Added `flags_updated = pyqtSignal(dict)` for ALU flag changes
- Signal carries dictionary with flag states: `{'Z': 0/1, 'N': 0/1, 'C': 0/1, 'O': 0/1}`
- Positioned logically with other register update signals

**Code Changes**:
```python
class ArchitectureSignals(QObject):
    # ... existing signals ...

    # ALU flags update (for visualization)
    flags_updated = pyqtSignal(dict)  # flags dictionary
```

---

### 4. Updated ALU to Emit Flags

**File**: [src/core/alu.py](../src/core/alu.py)

#### Enhanced `update_flags()` Method
- Added signal emission after flag calculation
- Emits copy of flags dictionary to prevent external modification
- Ensures GUI stays synchronized with ALU state

**Code Changes**:
```python
def update_flags(self, result, is_addition=None, op_a=0, op_b=0, res_raw=0):
    # ... existing flag calculations ...

    # Emit signal for GUI update
    signals.flags_updated.emit(self.flags.copy())
```

---

## Visual Changes

### Before Phase 1:
```
┌─────────────────────────────────────┐
│  Registers    CPU    Registers      │
│     │          │          │          │
│     └──────────┴──────────┘          │
│                                      │
│            ┌─────┐                   │
│            │ ALU │  ← Standalone!    │
│            └─────┘                   │
│                                      │
│            ┌────────┐                │
│            │ MEMORY │                │
│            └────────┘                │
└─────────────────────────────────────┘
```

### After Phase 1:
```
┌─────────────────────────────────────┐
│  Registers  ┌──────┐  Registers     │
│     │       │ CPU  │      │         │
│     │       │┌────┐│      │         │
│     │       ││ALU ││      │         │
│     │       │└────┘│      │         │
│     │       │Flags │      │         │
│     └───────└──────┴──────┘         │
│                                      │
│           ┌────────┐                 │
│           │ MEMORY │  ← Moved up    │
│           └────────┘                 │
└─────────────────────────────────────┘
```

---

## Testing

### Test Results
All existing tests pass without modification:
- `test_memory_read_write` ✅ PASSED
- `test_alu_add` ✅ PASSED
- `test_cpu_fetch` ✅ PASSED
- `test_simulation_run` ✅ PASSED

**Test Command**:
```bash
source venv/bin/activate
python -m pytest tests/ -v
```

**Result**: 4 passed in 0.11s

### Manual Testing
- Application launches successfully
- CPU block now contains ALU sub-component
- Flags display shows "Flags: ZNCO [0000]" initially
- No visual rendering errors
- All imports resolve correctly

---

## Architecture Improvements

### Correct Hierarchical Representation
The new structure properly reflects computer architecture:
- **CPU** is the top-level processing unit
  - **ALU** is a functional unit inside the CPU
  - **Control Unit** logic resides in CPU
  - **Registers** interface with CPU

This matches how real CPUs are organized and provides better educational value.

### Benefits
1. **Educational Accuracy**: Students see correct architectural relationships
2. **Visual Clarity**: ALU inside CPU makes the hierarchy obvious
3. **Extensibility**: Easier to add more CPU internals (e.g., instruction decoder)
4. **Maintainability**: Component relationships match logical relationships

---

## Files Modified

| File | Lines Changed | Type |
|------|---------------|------|
| [src/gui/components/graphics.py](../src/gui/components/graphics.py) | +31 | Addition/Enhancement |
| [src/gui/circuit_view.py](../src/gui/circuit_view.py) | -15, +5 | Removal/Simplification |
| [src/core/signals.py](../src/core/signals.py) | +3 | Addition |
| [src/core/alu.py](../src/core/alu.py) | +3 | Addition |

**Total**: 4 files modified, ~22 net lines added

---

## Backward Compatibility

### Maintained
- All existing tests pass
- All CPU/ALU logic unchanged
- Signal system extended, not modified
- Memory operations unchanged
- Register operations unchanged

### Removed
- Standalone `ALUVisual` component (kept as deprecated class for compatibility)
- Direct ALU bus connections in circuit view
- No breaking changes to APIs

---

## Known Issues

None identified in Phase 1.

---

## Next Steps (Phase 2)

The next phase will add I/O capabilities:
- Memory-mapped I/O ports at addresses 0xFE and 0xFF
- I/O controller for input/output management
- GUI I/O panel with input field and output display
- New instructions: IN and OUT
- Visual representation of I/O ports in circuit view

See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for full Phase 2 details.

---

## Conclusion

Phase 1 successfully corrected the architectural representation of the ALU, moving it from a standalone component to its proper place inside the CPU. The change improves educational accuracy, maintains all existing functionality, and sets a solid foundation for future phases.

**Time Invested**: ~1 hour
**Complexity**: Low
**Risk**: Low
**Status**: ✅ Production Ready
