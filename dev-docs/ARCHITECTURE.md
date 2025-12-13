# BasCAT Architecture Documentation

## System Overview

BasCAT is an educational 8-bit computer simulator with dual-level programming (BASIC and Assembly) and real-time circuit visualization.

---

## Component Architecture

### Current Architecture (Before Refactor)

```
┌─────────────────────────────────────────────────────────┐
│                    Main Window (GUI)                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐  ┌─────────────────┐  ┌────────────┐ │
│  │              │  │                 │  │            │ │
│  │  Code Editor │  │  Circuit View   │  │  Control   │ │
│  │  (Assembly)  │  │                 │  │  Panel     │ │
│  │              │  │                 │  │            │ │
│  └──────────────┘  └─────────────────┘  └────────────┘ │
│                                                          │
└─────────────────────────────────────────────────────────┘

Circuit View Components (ISSUE: ALU is separate):
┌─────────────────────────────────────────────┐
│                                             │
│  Registers    Data Bus    Addr Bus   CPU   │
│  (A,B,C,D) ──────┼──────────┼────── ┌───┐  │
│             ─────┼──────────┼────── │   │  │
│  (PC,IR,     ────┼──────────┼────── │CPU│  │
│   MAR)      ─────┼──────────┼────── │   │  │
│                  │          │       └───┘  │
│                  │          │              │
│               ┌──┴──┐       │              │
│               │ ALU │ ←─────┘ WRONG!       │
│               └──┬──┘                      │
│                  │                         │
│               ┌──┴──────┐                  │
│               │ Memory  │                  │
│               └─────────┘                  │
└─────────────────────────────────────────────┘
```

### Target Architecture (After Phase 1)

```
Circuit View Components (CORRECT):
┌──────────────────────────────────────────────┐
│                                              │
│  Registers    Data Bus    Addr Bus          │
│  (A,B,C,D) ──────┼──────────┼──────         │
│             ─────┼──────────┼──────         │
│  (PC,IR,     ────┼──────────┼──────         │
│   MAR)      ─────┼──────────┼──────         │
│                  │          │               │
│             ┌────┴──────────┴────┐          │
│             │       CPU           │          │
│             │  ┌─────────────┐   │          │
│             │  │  ALU (inside)│  │          │
│             │  │  Flags: ZNCO │  │          │
│             │  └─────────────┘   │          │
│             │  Control Unit       │          │
│             └────┬──────────┬────┘          │
│                  │          │               │
│               ┌──┴──────────┴──┐            │
│               │  Memory + I/O  │            │
│               └────────────────┘            │
└──────────────────────────────────────────────┘
```

---

## Target Software Architecture (After All Phases)

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE (PyQt6)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌────────────────┐  ┌───────────────┐  ┌──────────────────┐   │
│  │ BASIC Editor   │  │ Assembly      │  │ Circuit View     │   │
│  │ - Syntax HL    │  │ Editor        │  │ - CPU (with ALU) │   │
│  │ - Line mapping │  │ - Generated   │  │ - Registers      │   │
│  │ - Step through │  │ - Editable    │  │ - Memory         │   │
│  └────────┬───────┘  └───────┬───────┘  │ - Buses          │   │
│           │                  │          │ - I/O Ports      │   │
│           │                  │          └──────────────────┘   │
│  ┌────────┴──────────────────┴───────┐  ┌──────────────────┐   │
│  │     Control Panel                 │  │   I/O Panel      │   │
│  │  Run | Step | Step Over | Reset   │  │  Input: [____]   │   │
│  │  Speed: [slider] Metrics          │  │  Output: [disp]  │   │
│  └───────────────────────────────────┘  └──────────────────┘   │
│                                                                  │
└──────────────────────┬───────────────────────────────────────────┘
                       │
┌──────────────────────┴───────────────────────────────────────────┐
│                      COMPILER LAYER                              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  BASIC Source  →  Lexer  →  Parser  →  CodeGen  →  Assembly    │
│                                  ↓                               │
│                          Line Mapping Table                      │
│                     (BASIC line ↔ Assembly lines)               │
│                                                                  │
└──────────────────────┬───────────────────────────────────────────┘
                       │
┌──────────────────────┴───────────────────────────────────────────┐
│                     SIMULATION LAYER                             │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐     ┌────────────────┐    ┌────────────────┐ │
│  │  Assembler   │────→│  Sim Manager   │───→│  Clock/Timer   │ │
│  │  - Tokenize  │     │  - Load code   │    │  - Hz control  │ │
│  │  - Emit      │     │  - Run/Step    │    │  - Tick events │ │
│  │  - Line map  │     │  - State mgmt  │    └────────────────┘ │
│  └──────────────┘     └────────┬───────┘                        │
│                                │                                │
│  ┌─────────────────────────────┴────────────────────────────┐  │
│  │                     HARDWARE SIMULATION                   │  │
│  │                                                            │  │
│  │  ┌────────────────────────────────────────┐               │  │
│  │  │            CPU                         │               │  │
│  │  │  ┌──────────────────────────────┐     │               │  │
│  │  │  │  Registers: A,B,C,D          │     │               │  │
│  │  │  │  Special: PC, IR, MAR, SP    │     │               │  │
│  │  │  └──────────────────────────────┘     │               │  │
│  │  │  ┌──────────────────────────────┐     │               │  │
│  │  │  │  ALU (Inside CPU)            │     │               │  │
│  │  │  │  - Operations: +,-,&,|,^,~   │     │               │  │
│  │  │  │  - Flags: Z,N,C,O            │     │               │  │
│  │  │  └──────────────────────────────┘     │               │  │
│  │  │  ┌──────────────────────────────┐     │               │  │
│  │  │  │  Control Unit                │     │               │  │
│  │  │  │  - Decode instructions       │     │               │  │
│  │  │  │  - Execute micro-ops         │     │               │  │
│  │  │  └──────────────────────────────┘     │               │  │
│  │  └────────────┬────────────────┬──────────┘               │  │
│  │               │                │                          │  │
│  │         Data Bus         Address Bus                      │  │
│  │               │                │                          │  │
│  │  ┌────────────┴────────────────┴──────────┐              │  │
│  │  │         Memory (256 bytes)             │              │  │
│  │  │  0x00-0xFD: General RAM                │              │  │
│  │  │  0xFE: OUTPUT port (memory-mapped)     │              │  │
│  │  │  0xFF: INPUT port (memory-mapped)      │              │  │
│  │  └────────────┬───────────────────────────┘              │  │
│  │               │                                          │  │
│  │  ┌────────────┴───────────────┐                          │  │
│  │  │    I/O Controller          │                          │  │
│  │  │  - Input queue (FIFO)      │                          │  │
│  │  │  - Output buffer           │                          │  │
│  │  │  - Signals to GUI          │                          │  │
│  │  └────────────────────────────┘                          │  │
│  │                                                            │  │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│                    SIGNAL SYSTEM (Qt Signals)                    │
├──────────────────────────────────────────────────────────────────┤
│  - register_updated(name, value)                                │
│  - pc_updated(value)                                             │
│  - ir_updated(value)                                             │
│  - mar_updated(value)                                            │
│  - bus_transfer(source, dest, value, bus_type)                  │
│  - current_line_changed(line_number)                            │
│  - output_written(value)                                         │
│  - input_requested()                                             │
│  - clock_tick()                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## Data Flow

### Assembly Program Execution

```
1. User writes Assembly in Editor
         ↓
2. Click "Run" or "Step"
         ↓
3. Assembler.assemble(source_code)
         → Returns: [bytecode], line_map
         ↓
4. SimManager.load_code()
         → CPU.reset()
         → Memory.load_program(bytecode)
         ↓
5. Clock.start() or SimManager.step()
         ↓
6. For each tick:
         → SimManager.handle_tick()
         → emit current_line_changed (highlights editor)
         → CPU.execute_instruction()
              → Fetch opcode
              → Decode
              → Execute (may use ALU, Memory, I/O)
              → Emit signals (register_updated, bus_transfer, etc.)
         ↓
7. GUI updates:
         → Editor highlights current line
         → Circuit view animates bus transfers
         → Registers update their displays
         → I/O panel shows input/output
```

### BASIC Program Execution (Phase 4)

```
1. User writes BASIC in Editor
         ↓
2. Click "Compile"
         ↓
3. Compiler.compile(basic_source)
         → Lexer: tokenize
         → Parser: build AST
         → CodeGen: emit assembly
         → Returns: assembly_code, basic_to_asm_map
         ↓
4. Display generated assembly in Assembly Editor pane
         ↓
5. Click "Run" or "Step"
         ↓
6. Same as Assembly execution (steps 3-7 above)
         BUT: Highlight both BASIC and Assembly lines
         using the two-level line mapping
```

---

## Instruction Set Architecture

### Opcodes (Current + Planned)

| Opcode | Mnemonic | Operands | Description | Status |
|--------|----------|----------|-------------|--------|
| 0x00 | NOP | - | No operation | ✓ Implemented |
| 0x01 | LOAD | reg, imm8 | Load immediate to register | ✓ Implemented |
| 0x02 | ADD | reg, imm8 | Add immediate to register A | ✓ Implemented |
| 0x03 | SUB | reg, imm8 | Subtract immediate from A | ✓ Implemented |
| 0x04 | MOV | reg, reg | Move between registers | Partial |
| 0x05 | AND | reg, imm8 | Bitwise AND | Planned |
| 0x06 | OR | reg, imm8 | Bitwise OR | Planned |
| 0x07 | XOR | reg, imm8 | Bitwise XOR | Planned |
| 0x08 | NOT | reg | Bitwise NOT | Planned |
| 0x09 | CMP | reg, imm8 | Compare, set flags | Planned |
| 0x10 | JMP | addr | Unconditional jump | ✓ Implemented |
| 0x11 | JZ | addr | Jump if zero flag set | Planned |
| 0x12 | JNZ | addr | Jump if zero flag clear | Planned |
| 0x13 | JC | addr | Jump if carry flag set | Planned |
| 0x14 | JNC | addr | Jump if carry flag clear | Planned |
| 0x20 | PUSH | reg | Push register to stack | Planned |
| 0x21 | POP | reg | Pop from stack to register | Planned |
| 0x30 | LDM | reg, [addr] | Load from memory | Planned |
| 0x31 | STM | [addr], reg | Store to memory | Planned |
| 0x40 | IN | reg | Read from INPUT port (0xFF) | Planned |
| 0x41 | OUT | reg | Write to OUTPUT port (0xFE) | Planned |
| 0xFF | HALT | - | Stop execution | ✓ Implemented |

### Registers

| Register | Size | Purpose |
|----------|------|---------|
| A, B, C, D | 8-bit | General purpose |
| PC | 16-bit | Program Counter |
| IR | 8-bit | Instruction Register |
| MAR | 16-bit | Memory Address Register |
| SP | 16-bit | Stack Pointer (to add) |

### Flags (in ALU)

| Flag | Meaning |
|------|---------|
| Z | Zero (result was 0) |
| N | Negative (MSB set) |
| C | Carry (overflow/borrow) |
| O | Overflow (signed) |

---

## BASIC Language Specification (Phase 4)

### Grammar (Simplified)

```
program     := line*
line        := NUMBER statement NEWLINE
statement   := REM comment
             | LET variable = expression
             | INPUT variable
             | PRINT expression
             | GOTO NUMBER
             | IF condition THEN statement
             | FOR variable = expr TO expr
             | NEXT variable
             | END

expression  := term ((+|-) term)*
term        := factor ((*|/|MOD) factor)*
factor      := NUMBER | variable | (expression)

condition   := expression relop expression
relop       := = | <> | < | > | <= | >=

variable    := A | B | C | D | ... | Z
```

### Example Program

```basic
10 REM Simple addition program
20 PRINT "Enter first number:"
30 INPUT A
40 PRINT "Enter second number:"
50 INPUT B
60 LET C = A + B
70 PRINT "Sum is:"
80 PRINT C
90 END
```

### Compilation Strategy

Each BASIC statement maps to one or more assembly instructions:

```
LET A = 5
    ↓
    LOAD A, 5

LET C = A + B
    ↓
    MOV C, A      ; Copy A to C
    ADD C, B      ; Add B to C

IF A < 10 THEN GOTO 50
    ↓
    CMP A, 10     ; Compare A with 10
    JC LINE50     ; Jump if A < 10

PRINT A
    ↓
    OUT A         ; Write A to OUTPUT port
```

---

## Memory Map

```
0x0000 - 0x00EF (0-239):   Program/Data area (240 bytes)
0x00F0 - 0x00FD (240-253): Stack area (14 bytes)
0x00FE (254):              OUTPUT port (memory-mapped I/O)
0x00FF (255):              INPUT port (memory-mapped I/O)
```

---

## File Structure

```
BasCAT/
├── src/
│   ├── bascat.py              # Entry point
│   ├── core/                  # Simulation engine
│   │   ├── __init__.py
│   │   ├── cpu.py             # CPU with embedded ALU
│   │   ├── alu.py             # ALU (used by CPU)
│   │   ├── memory.py          # Memory + I/O intercept
│   │   ├── io_controller.py   # NEW: I/O management
│   │   ├── clock.py           # Clock/timing
│   │   ├── assembler.py       # Assembly → bytecode
│   │   ├── sim_manager.py     # Orchestrates simulation
│   │   └── signals.py         # Qt signal definitions
│   ├── compiler/              # NEW: BASIC compiler
│   │   ├── __init__.py
│   │   ├── lexer.py           # Tokenization
│   │   ├── parser.py          # AST generation
│   │   ├── codegen.py         # Assembly generation
│   │   └── compiler.py        # Main interface
│   └── gui/                   # User interface
│       ├── __init__.py
│       ├── main_window.py     # Main application window
│       ├── editor.py          # Code editor (dual-pane)
│       ├── circuit_view.py    # Circuit visualization
│       ├── controls.py        # Run/Step/Reset controls
│       ├── io_panel.py        # NEW: I/O interface
│       ├── metrics_panel.py   # NEW: Statistics display
│       └── components/
│           ├── __init__.py
│           └── graphics.py    # Visual components
├── tests/
│   ├── test_core.py
│   ├── test_gui.py
│   ├── test_sim.py
│   ├── test_io.py             # NEW
│   ├── test_compiler.py       # NEW
│   └── test_instructions.py   # NEW
├── examples/                  # NEW: Sample programs
│   ├── hello_world.bas
│   ├── hello_world.asm
│   ├── fibonacci.bas
│   └── ...
├── docs/                      # NEW: Documentation
│   ├── instruction_reference.md
│   └── basic_guide.md
├── assets/
│   └── styles.qss
├── dev-docs/
│   ├── CHANGELOG-Master.md
│   ├── IMPLEMENTATION_PLAN.md # THIS FILE'S COMPANION
│   └── ARCHITECTURE.md        # THIS FILE
├── requirements.txt
└── README.md
```

---

## Key Design Principles

1. **Educational First**: Every feature should help users understand how computers work
2. **Visual Clarity**: The circuit view should accurately represent the architecture
3. **Dual-Level Learning**: BASIC shows high-level concepts, Assembly shows how they're implemented
4. **Real-Time Feedback**: Immediate visual response to all operations
5. **Simplicity**: 8-bit design keeps complexity manageable for learners
6. **Extensibility**: Architecture allows adding new features without major rewrites

---

## Critical Relationships

### ALU ↔ CPU
- ALU is a **component inside** CPU, not a peer
- CPU calls ALU methods for arithmetic/logic operations
- ALU flags are read by CPU for conditional branching

### Memory-Mapped I/O
- I/O ports appear as memory addresses (0xFE, 0xFF)
- Memory class intercepts reads/writes to these addresses
- I/O Controller handles actual input/output operations

### Compiler ↔ Assembler
- Compiler generates assembly source code as text
- Assembler converts that text to bytecode
- Both maintain line mapping for debugging

### Signals ↔ GUI
- Core simulation emits Qt signals for all state changes
- GUI components listen and update displays
- Decoupled architecture: core doesn't know about GUI

---

## Performance Considerations

- **Clock Speed**: User-adjustable from 0.1 Hz to 100 Hz
- **Animation**: Skip animations at high speeds (>10 Hz)
- **Memory**: 256 bytes is tiny, no optimization needed
- **GUI Updates**: Batch updates during fast execution

---

## Next Steps

See [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for detailed implementation phases.
