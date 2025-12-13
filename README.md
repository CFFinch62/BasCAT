# BasCAT - BASIC Computer Architecture Trainer

An educational 8-bit computer simulator with visual circuit representation, assembly programming, and a BASIC-like high-level language that compiles to assembly.

## Project Vision

BasCAT is designed to teach computer architecture by providing:
- **Visual Learning**: See how data flows through CPU, ALU, registers, and memory
- **Dual-Level Programming**: Write in BASIC, see the assembly code it generates
- **Interactive Debugging**: Step through code and watch the circuit animate in real-time
- **Educational Accuracy**: Proper architectural hierarchy (ALU inside CPU, etc.)

## Current Status: Phase 1 Complete ✅

### What's Working
- **Circuit Visualization**: Interactive view showing CPU (with embedded ALU), registers, RAM, and buses
- **Assembly Programming**: Simple instruction set (LOAD, ADD, SUB, JMP, HALT)
- **Execution Control**: Run, step, and reset with adjustable clock speed
- **Real-time Animation**: Bus transfers and register updates visualized
- **ALU Flags Display**: Shows Zero, Negative, Carry, and Overflow flags

### Architecture
- **CPU**: 8-bit with embedded ALU
  - General Purpose Registers: A, B, C, D (8-bit)
  - Special Registers: PC (16-bit), IR (8-bit), MAR (16-bit)
  - ALU with flags: Z, N, C, O
- **RAM**: 256 bytes
- **Buses**: Data bus and Address bus with visual animations

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

Example program:
```assembly
; Simple addition
LOAD A, 10    ; Load 10 into register A
ADD A, 5      ; Add 5 to A
HALT          ; Stop execution
```

### Controls
- **Run**: Execute the program continuously at the selected speed
- **Step**: Execute one instruction
- **Reset**: Clear all registers and stop execution
- **Speed Slider**: Adjust execution speed (0.1 Hz to 10 Hz)

## Development Roadmap

See [IMPLEMENTATION_PLAN.md](dev-docs/IMPLEMENTATION_PLAN.md) for the complete 6-phase plan.

### Upcoming Phases
- **Phase 2**: I/O System (memory-mapped I/O, input/output panel)
- **Phase 3**: Enhanced Instruction Set (logic, branching, stack operations)
- **Phase 4**: BASIC-like Language (compiler, dual-editor view)
- **Phase 5**: Advanced Debugging (dual-level execution tracking)
- **Phase 6**: Polish (examples, tutorials, documentation)

## Documentation

- [ARCHITECTURE.md](dev-docs/ARCHITECTURE.md) - System architecture and design
- [IMPLEMENTATION_PLAN.md](dev-docs/IMPLEMENTATION_PLAN.md) - Detailed development plan
- [CHANGELOG-Phase1.md](dev-docs/CHANGELOG-Phase1.md) - Phase 1 changes and decisions

## Testing

```bash
source venv/bin/activate
python -m pytest tests/ -v
```

Current test coverage:
- Core memory operations
- ALU arithmetic
- CPU instruction fetch/execute
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
