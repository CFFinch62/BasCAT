# BasCAT - BASIC Computer Architecture Trainer

An educational 8-bit computer simulator with visual circuit representation, assembly programming, and a BASIC-like high-level language that compiles to assembly.

## Project Vision

BasCAT is designed to teach computer architecture by providing:
- **Visual Learning**: See how data flows through CPU, ALU, registers, and memory
- **Dual-Level Programming**: Write in BASIC, see the assembly code it generates
- **Interactive Debugging**: Step through code and watch the circuit animate in real-time
- **Educational Accuracy**: Proper architectural hierarchy (ALU inside CPU, etc.)

## Current Status: Phase 3 Complete ✅

### What's Working
- **Circuit Visualization**: Interactive view showing CPU (with embedded ALU), registers, RAM, I/O ports, and buses
- **Enhanced Instruction Set**: 23 instructions including logic operations, conditional branching, stack operations, and memory access
- **Interactive I/O System**: Memory-mapped I/O allowing programs to accept input and display output
- **I/O Panel**: Dedicated GUI panel for user input/output interaction
- **Execution Control**: Run, step, and reset with adjustable clock speed
- **Real-time Animation**: Bus transfers, register updates, I/O operations, and stack operations visualized
- **ALU Flags Display**: Shows Zero, Negative, Carry, and Overflow flags
- **Example Programs**: 9 example programs demonstrating all features

### Architecture
- **CPU**: 8-bit with embedded ALU
  - General Purpose Registers: A, B, C, D (8-bit)
  - Special Registers: PC (16-bit), IR (8-bit), MAR (16-bit), SP (8-bit)
  - ALU with flags: Z, N, C, O
- **RAM**: 256 bytes
  - 0x00-0xFD: General RAM + Stack (253 bytes)
  - 0xFE: OUTPUT port (memory-mapped I/O)
  - 0xFF: INPUT port (memory-mapped I/O)
- **Stack**: Grows downward from 0xFD, managed by SP register
- **I/O System**: Memory-mapped I/O controller with input queue and output buffer
- **Buses**: Data bus and Address bus with visual animations

### Instruction Set (23 total)
- **Arithmetic & Logic**: NOP, ADD, SUB, AND, OR, XOR, NOT
- **Data Movement**: LOAD, MOV, LDM, STM
- **Control Flow**: CMP, JMP, JZ, JNZ, JC, JNC
- **Stack**: PUSH, POP
- **I/O**: IN, OUT
- **System**: HALT

## Installation

### Prerequisites
- Python 3.12+
- PyQt6

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd BasCAT

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Application
```bash
source venv/bin/activate
python3 -m src.bascat
```

Or use the convenience script:
```bash
./run.sh
```

### Writing Assembly Code

Example program with loops:
```assembly
; Count from 0 to 9
LOAD A, 0
loop:
    OUT A         ; Output current number
    ADD A, 1      ; Increment
    CMP A, 10     ; Compare with limit
    JNZ loop      ; Jump if not zero
HALT
```

More examples in the [examples/](examples/) directory:
- `01_echo.asm` - Simple echo program
- `02_add_numbers.asm` - Sequential input demonstration
- `03_hello_world.asm` - Outputs "HI"
- `04_logic_operations.asm` - Logic operations (AND, OR, XOR, NOT)
- `05_conditional_loop.asm` - Conditional loop using CMP and JNZ
- `06_stack_demo.asm` - Stack operations (PUSH/POP)
- `07_memory_operations.asm` - Memory access (LDM/STM)
- `08_mov_register.asm` - MOV instruction variants
- `09_complex_program.asm` - Complex accumulator with input loop

### Controls
- **Run**: Execute the program continuously at the selected speed
- **Step**: Execute one instruction
- **Reset**: Clear all registers and stop execution
- **Speed Slider**: Adjust execution speed (0.1 Hz to 10 Hz)

### Using I/O
1. Type input in the I/O Panel input field (right side)
2. Click "Send" or press Enter to queue the input
3. Run your program - `IN` instructions will read the queued input
4. Output from `OUT` instructions appears in the output display

## Development Roadmap

See [IMPLEMENTATION_PLAN.md](dev-docs/IMPLEMENTATION_PLAN.md) for the complete 6-phase plan.

### Completed Phases
- **Phase 1**: Architecture Fix - ALU Integration ✅
- **Phase 2**: I/O System ✅
- **Phase 3**: Enhanced Instruction Set ✅

### Upcoming Phases
- **Phase 4**: BASIC-like Language (compiler, dual-editor view)
- **Phase 5**: Advanced Debugging (dual-level execution tracking)
- **Phase 6**: Polish (examples, tutorials, documentation)

## Documentation

- [ARCHITECTURE.md](dev-docs/ARCHITECTURE.md) - System architecture and design
- [IMPLEMENTATION_PLAN.md](dev-docs/IMPLEMENTATION_PLAN.md) - Detailed development plan
- [CHANGELOG-Phase1.md](dev-docs/CHANGELOG-Phase1.md) - Phase 1: Architecture Fix
- [CHANGELOG-Phase2.md](dev-docs/CHANGELOG-Phase2.md) - Phase 2: I/O System
- [CHANGELOG-Phase3.md](dev-docs/CHANGELOG-Phase3.md) - Phase 3: Enhanced Instruction Set

## Testing

```bash
source venv/bin/activate
python -m pytest tests/ -v
```

Current test coverage (15 tests, all passing):
- Core memory operations
- ALU arithmetic and logic operations
- CPU instruction fetch/execute
- All Phase 3 instructions (logic, branching, stack, memory)
- Simulation manager

## Project Structure

```
BasCAT/
├── src/
│   ├── bascat.py          # Entry point
│   ├── core/              # Simulation engine
│   │   ├── cpu.py         # CPU with embedded ALU
│   │   ├── alu.py         # Arithmetic Logic Unit
│   │   ├── memory.py      # RAM
│   │   ├── assembler.py   # Assembly → bytecode
│   │   ├── clock.py       # Timing/clock
│   │   ├── signals.py     # Qt signals
│   │   └── sim_manager.py # Orchestration
│   └── gui/               # User interface
│       ├── main_window.py # Main application window
│       ├── circuit_view.py# Circuit visualization
│       ├── editor.py      # Code editor
│       ├── controls.py    # Control panel
│       └── components/
│           └── graphics.py# Visual components
├── tests/                 # Test suite
├── dev-docs/              # Development documentation
├── assets/                # Stylesheets, resources
└── requirements.txt       # Python dependencies
```

## Contributing

This is an educational project. Contributions are welcome, especially:
- Additional example programs
- Bug fixes
- Documentation improvements
- Educational content

## License

[To be determined]

## Credits

**BasCAT** - BASIC Computer Architecture Trainer
Educational 8-bit computer simulator

---

*"Understanding computers from the ground up"*
