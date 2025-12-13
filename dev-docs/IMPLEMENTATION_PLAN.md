# BasCAT Evolution Implementation Plan

## Project Vision
Transform BasCAT into a comprehensive educational 8-bit computer simulator with:
1. Proper architectural hierarchy (ALU inside CPU)
2. Input/Output capabilities for interactive programs
3. BASIC-like high-level language that compiles to assembly
4. Visual debugging showing both high-level and assembly code execution

---

## Current State Analysis

### What's Working
- PyQt6-based GUI with circuit visualization
- Basic CPU simulation with registers (A, B, C, D, PC, IR, MAR)
- Simple assembler for basic instructions (LOAD, ADD, SUB, JMP, HALT)
- Memory system (256 bytes)
- Visual bus animations showing data flow
- Code editor with line highlighting during execution
- Clock-based execution (run/step/reset controls)

### Architectural Issues
1. **ALU Separation**: ALU is displayed as a separate component outside the CPU (lines 118-130 in circuit_view.py), but architecturally it should be inside the CPU
2. **No I/O System**: No way for programs to accept input or display output
3. **Limited Instruction Set**: Only 7 basic instructions
4. **No High-Level Language**: Only assembly programming available
5. **No Dual-View Debugging**: Can't see high-level code mapped to assembly

---

## Implementation Phases

## Phase 1: Fix Architecture - ALU Integration

**Goal**: Make ALU a proper component inside CPU, both logically and visually

### Tasks
1. **Refactor CPU Visualization**
   - Modify [circuit_view.py](src/gui/circuit_view.py) to remove standalone ALU block
   - Add ALU as a sub-component inside the CPU block visual
   - Update [components/graphics.py](src/gui/components/graphics.py) to support nested components

2. **Update CPU Logic**
   - Ensure [cpu.py](src/core/cpu.py) already contains ALU (it does at line 10)
   - No logic changes needed, just visual reorganization

3. **Adjust Bus Connections**
   - Remove direct ALU-to-bus connections (lines 127-130 in circuit_view.py)
   - ALU operations flow through CPU to buses
   - Keep internal signal emissions for ALU operations

**Files to Modify**:
- [src/gui/circuit_view.py](src/gui/circuit_view.py) - lines 118-130
- [src/gui/components/graphics.py](src/gui/components/graphics.py) - add CPUVisual enhancements

---

## Phase 2: Add I/O System

**Goal**: Enable programs to read input and write output

### 2.1: Memory-Mapped I/O Architecture

**Design**:
- Reserve memory addresses for I/O:
  - `0xFE` (254): OUTPUT port - write to display
  - `0xFF` (255): INPUT port - read from keyboard/input buffer
- Add I/O controller to manage input queue and output buffer

### Tasks
1. **Create I/O Controller**
   - New file: [src/core/io_controller.py](src/core/io_controller.py)
   - Manage input queue (FIFO buffer)
   - Manage output buffer for display
   - Emit signals when output changes

2. **Update Memory System**
   - Modify [memory.py](src/core/memory.py) to intercept reads/writes to I/O addresses
   - Route I/O operations to I/O controller

3. **Add I/O Instructions**
   - Extend instruction set in [assembler.py](src/core/assembler.py):
     - `IN reg` - Read from INPUT port to register
     - `OUT reg` - Write from register to OUTPUT port
   - Update [cpu.py](src/core/cpu.py) to execute I/O instructions

### 2.2: GUI I/O Interface

**Design**:
- Add I/O panel as a dock widget
- Input section: Text field for typing input, button to submit
- Output section: Scrollable display area (like a terminal)

### Tasks
1. **Create I/O Panel Widget**
   - New file: [src/gui/io_panel.py](src/gui/io_panel.py)
   - Input text field with "Send" button
   - Output display (QTextEdit, read-only, monospace font)
   - Connect to I/O controller signals

2. **Integrate into Main Window**
   - Update [main_window.py](src/gui/main_window.py)
   - Add I/O panel as bottom or right dock widget
   - Wire up signal/slot connections

3. **Visual I/O Port Representation**
   - Add I/O port visual component to circuit view
   - Show I/O operations with bus animations
   - Position near memory (since it's memory-mapped)

**Files to Create**:
- [src/core/io_controller.py](src/core/io_controller.py)
- [src/gui/io_panel.py](src/gui/io_panel.py)

**Files to Modify**:
- [src/core/memory.py](src/core/memory.py)
- [src/core/cpu.py](src/core/cpu.py)
- [src/core/assembler.py](src/core/assembler.py)
- [src/gui/main_window.py](src/gui/main_window.py)
- [src/gui/circuit_view.py](src/gui/circuit_view.py)
- [src/core/sim_manager.py](src/core/sim_manager.py)

---

## Phase 3: Enhanced Instruction Set

**Goal**: Provide a richer assembly language for more complex programs

### New Instructions to Add
```
Logic:
  AND reg, reg/value
  OR reg, reg/value
  XOR reg, reg/value
  NOT reg

Comparison:
  CMP reg, reg/value    ; Compare, set flags

Branching:
  JZ addr              ; Jump if Zero flag set
  JNZ addr             ; Jump if Zero flag clear
  JC addr              ; Jump if Carry flag set
  JNC addr             ; Jump if Carry flag clear

Stack:
  PUSH reg
  POP reg

Memory:
  LDM reg, [addr]      ; Load from memory address
  STM [addr], reg      ; Store to memory address

Enhanced MOV:
  MOV reg, reg         ; Move between registers
  MOV reg, value       ; Move immediate value
```

### Tasks
1. **Update Assembler**
   - Add new opcodes to [assembler.py](src/core/assembler.py)
   - Implement operand parsing for new instruction formats

2. **Update CPU**
   - Add flag support (already in ALU, need to expose in CPU)
   - Implement new instruction execution in [cpu.py](src/core/cpu.py)
   - Add stack pointer (SP) register

3. **Update Circuit Visualization**
   - Add SP register visual
   - Add flags display (Z, N, C, O)

**Files to Modify**:
- [src/core/assembler.py](src/core/assembler.py)
- [src/core/cpu.py](src/core/cpu.py)
- [src/gui/circuit_view.py](src/gui/circuit_view.py)
- [src/gui/components/graphics.py](src/gui/components/graphics.py)

---

## Phase 4: BASIC-like High-Level Language

**Goal**: Create a simple high-level language that compiles to assembly

### 4.1: Language Design - "SimpleBasCAT"

**Features**:
```basic
10 REM Simple BASIC program
20 LET A = 0
30 INPUT B
40 LET A = A + B
50 PRINT A
60 IF A < 100 THEN GOTO 30
70 END
```

**Supported Constructs**:
- Variables (single letter A-Z, maps to memory locations)
- Arithmetic: `+`, `-`, `*`, `/`, `MOD`
- Comparison: `=`, `<>`, `<`, `>`, `<=`, `>=`
- Control: `GOTO`, `IF...THEN`, `FOR...NEXT`
- I/O: `INPUT`, `PRINT`
- Line numbers (for GOTO targets)
- Comments: `REM`

### 4.2: Compiler Architecture

**Components**:
1. **Lexer**: Tokenize BASIC source
2. **Parser**: Build AST (Abstract Syntax Tree)
3. **Code Generator**: Emit assembly from AST
4. **Symbol Table**: Track variables, line numbers, labels

### Tasks
1. **Create Compiler Package**
   - New directory: [src/compiler/](src/compiler/)
   - [src/compiler/lexer.py](src/compiler/lexer.py) - Tokenization
   - [src/compiler/parser.py](src/compiler/parser.py) - Parsing to AST
   - [src/compiler/codegen.py](src/compiler/codegen.py) - Assembly generation
   - [src/compiler/compiler.py](src/compiler/compiler.py) - Main compiler interface

2. **Create Dual-Editor Interface**
   - Split editor into two tabs or side-by-side panes:
     - BASIC editor (high-level)
     - Assembly editor (generated, read-only by default)
   - Add "Compile" button to generate assembly from BASIC

3. **Source Line Mapping**
   - Compiler generates mapping: BASIC line → Assembly lines
   - Both editors highlight during execution
   - User sees which BASIC statement is executing and what assembly it generated

4. **Update Sim Manager**
   - [sim_manager.py](src/core/sim_manager.py) handles two-level line mapping
   - Track both BASIC and assembly execution positions

**Files to Create**:
- [src/compiler/__init__.py](src/compiler/__init__.py)
- [src/compiler/lexer.py](src/compiler/lexer.py)
- [src/compiler/parser.py](src/compiler/parser.py)
- [src/compiler/codegen.py](src/compiler/codegen.py)
- [src/compiler/compiler.py](src/compiler/compiler.py)

**Files to Modify**:
- [src/gui/editor.py](src/gui/editor.py) - Create dual-pane editor
- [src/gui/main_window.py](src/gui/main_window.py) - Add compile button
- [src/core/sim_manager.py](src/core/sim_manager.py) - Handle dual-level mapping

---

## Phase 5: Debugging & Visualization Enhancements

**Goal**: Make the relationship between high-level and assembly code crystal clear

### Features
1. **Dual-Level Execution View**
   - Both BASIC and Assembly editors visible simultaneously
   - Synchronized highlighting during execution
   - Visual arrows/lines connecting BASIC statement to assembly instructions

2. **Step Through Options**
   - Step Over: Execute entire BASIC statement (multiple assembly instructions)
   - Step Into: Execute single assembly instruction
   - Run to Line: In either BASIC or Assembly view

3. **Enhanced Circuit Animation**
   - Show which BASIC construct is executing in the circuit view
   - Annotate bus transfers with operation context (e.g., "PRINT A")

4. **Execution History**
   - Timeline showing execution flow
   - Ability to step backwards (replay from start with saved states)

### Tasks
1. **Multi-Level Stepper**
   - Modify control panel for step-over vs step-into
   - Update [sim_manager.py](src/core/sim_manager.py) for smart stepping

2. **Visual Mapping Display**
   - Highlight connected code regions in both views
   - Add side panel showing current operation in plain English

3. **State History**
   - Record CPU/memory snapshots at BASIC statement boundaries
   - Allow replay/rewind

**Files to Modify**:
- [src/gui/controls.py](src/gui/controls.py) - Enhanced control buttons
- [src/core/sim_manager.py](src/core/sim_manager.py) - State management
- [src/gui/circuit_view.py](src/gui/circuit_view.py) - Contextual annotations

---

## Phase 6: Polish & Educational Features

**Goal**: Make BasCAT a premier educational tool

### Features
1. **Example Programs Library**
   - Menu with sample programs (BASIC and Assembly)
   - Categories: Hello World, Math, Loops, Functions, Games

2. **Tutorial Mode**
   - Step-by-step guided tutorials
   - Explanatory tooltips for each component
   - Quiz questions after each lesson

3. **Performance Metrics**
   - Instruction count
   - Clock cycles used
   - Memory utilization
   - I/O operations

4. **Export/Share**
   - Save/load programs
   - Export execution trace
   - Share via URL (encode program in URL params)

5. **Help System**
   - Complete instruction reference
   - BASIC language guide
   - Interactive component help (click CPU for CPU docs)

### Tasks
1. **Create Examples**
   - Directory: [examples/](examples/)
   - JSON catalog of examples with metadata

2. **Add Menu System**
   - File → New, Open, Save, Save As
   - Examples → (categorized submenu)
   - Help → Instruction Reference, BASIC Guide, About

3. **Metrics Panel**
   - New dock widget showing statistics
   - Update in real-time during execution

4. **Documentation**
   - [docs/](docs/) directory
   - Markdown files for reference materials
   - Embed in app with QTextBrowser

**Files to Create**:
- [examples/](examples/) - Directory with example programs
- [src/gui/metrics_panel.py](src/gui/metrics_panel.py)
- [docs/instruction_reference.md](docs/instruction_reference.md)
- [docs/basic_guide.md](docs/basic_guide.md)

**Files to Modify**:
- [src/gui/main_window.py](src/gui/main_window.py) - Add menus and help

---

## Testing Strategy

### Unit Tests
- Test each instruction independently
- Test assembler with valid/invalid input
- Test BASIC compiler with sample programs
- Test I/O controller

### Integration Tests
- Full program execution (assembly)
- Full program execution (BASIC → assembly → execution)
- GUI interaction tests

### Test Files to Create/Update
- [tests/test_io.py](tests/test_io.py)
- [tests/test_compiler.py](tests/test_compiler.py)
- [tests/test_instructions.py](tests/test_instructions.py)
- Update existing: [tests/test_core.py](tests/test_core.py)

---

## Implementation Timeline

### Priority Order
1. **Phase 1** (Architecture Fix) - Quick win, 1-2 days
2. **Phase 2** (I/O System) - Critical for useful programs, 3-5 days
3. **Phase 3** (Enhanced Instructions) - Foundation for complex programs, 2-3 days
4. **Phase 4** (BASIC Compiler) - Main feature, 5-7 days
5. **Phase 5** (Debugging Tools) - Quality of life, 3-4 days
6. **Phase 6** (Polish) - Ongoing, 3-5 days

**Estimated Total**: 3-4 weeks of focused development

---

## Success Metrics

The project will be considered successful when:
1. ALU is visually shown inside the CPU block
2. Users can write programs that accept keyboard input and display output
3. Users can write BASIC programs that compile to assembly
4. Users can step through BASIC code and see the corresponding assembly execute
5. Circuit visualization clearly shows what's happening at both levels
6. At least 10 example programs demonstrating capabilities
7. Complete documentation for instruction set and BASIC language

---

## Future Enhancements (Beyond Scope)

- Interrupt system
- Multiple I/O devices (keyboard, display, timer, etc.)
- Debugger with breakpoints
- Memory visualization (hex dump view)
- Assembler macros and procedures
- BASIC functions and subroutines
- Sound output
- Graphics mode (pixel display)
- Save/restore machine state
- Step backwards (full replay)
- Assembly optimization hints from BASIC compiler
