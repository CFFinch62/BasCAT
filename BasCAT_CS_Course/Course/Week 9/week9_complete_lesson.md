# Week 9: Computer Architecture Deep Dive

**Theme**: Understanding How Computers Actually Work
**Duration**: 5 days (50 minutes each)

---

## Week 9, Day 1: CPU Architecture

**Topic**: Inside the Processor
**Duration**: 50 minutes
**Learning Objectives**:
- Understand CPU components
- Explain fetch-execute cycle
- Trace instruction execution
- Connect to BasCAT visualization

### Lesson Overview

**CPU Components**:
1. **ALU** (Arithmetic Logic Unit)
   - Does all math and logic
   - Students have used this for 8 weeks!
   
2. **Control Unit**
   - Manages instruction execution
   - Coordinates all components

3. **Registers**
   - Fast storage (A, B, C, D in BasCAT)
   - Students used these since Week 1

4. **Program Counter (PC)**
   - Tracks current instruction
   - Automatically increments

5. **Instruction Register (IR)**
   - Holds current instruction
   - Decoded by control unit

**Fetch-Execute Cycle**:
```
1. FETCH: Read instruction from memory (PC → IR)
2. DECODE: Figure out what to do
3. EXECUTE: Do it (ALU, memory, etc.)
4. INCREMENT: PC++, repeat
```

**Hands-On**: Watch in BasCAT circuit view
- Step through program
- Watch PC increment
- See instruction in IR
- Observe ALU activate

**Activity**: Students trace simple program showing fetch-execute for each instruction

---

## Week 9, Day 2: Memory Hierarchy

**Topic**: RAM, Cache, and Storage
**Duration**: 50 minutes
**Learning Objectives**:
- Understand memory hierarchy
- Compare speed vs capacity
- Explain cache concept
- Relate to BasCAT memory

### Key Concepts

**Memory Hierarchy** (fastest to slowest):
```
Registers     (4 in BasCAT)      Fastest, Smallest
↓
Cache         (not in BasCAT)     Very fast, Small
↓
RAM           (256 bytes BasCAT)  Fast, Medium
↓
Hard Drive    (not in BasCAT)     Slow, Huge
```

**Why Hierarchy?**:
- Fast memory is expensive
- Slow memory is cheap
- Trade-off: Speed vs Size

**Memory Access Times** (relative):
- Register: 1 cycle
- RAM: 10 cycles
- Disk: 1,000,000 cycles!

**BasCAT Example**:
```assembly
LOAD A, 10      ; Fast (immediate)
LDM A, 100      ; Slower (memory access)
```

"Both seem instant in BasCAT, but real CPUs have delays!"

**Activity**: Calculate impact of memory access patterns on performance

---

## Week 9, Day 3: Instruction Set Architecture

**Topic**: How Instructions Are Encoded
**Duration**: 50 minutes
**Learning Objectives**:
- Understand instruction encoding
- Decode binary instructions
- Compare RISC vs CISC
- Relate to BasCAT instruction set

### Key Concepts

**Instruction Format** (simplified):
```
[OPCODE][OPERAND1][OPERAND2]
  8 bits   8 bits    8 bits
```

**Example Encoding**:
```
LOAD A, 42
↓
[00000001][00000000][00101010]
 LOAD op    Reg A      Value 42
```

**BasCAT Instruction Set**:
- ~20 instructions
- Simple encoding
- Easy to understand

**RISC vs CISC**:
- **RISC**: Few simple instructions (like BasCAT)
- **CISC**: Many complex instructions
- Modern CPUs: Mix of both

**Activity**: Students encode/decode BasCAT instructions by hand

---

## Week 9, Day 4: Input/Output Systems

**Topic**: How Computers Communicate
**Duration**: 50 minutes
**Learning Objectives**:
- Understand I/O mechanisms
- Explain memory-mapped I/O
- Describe polling vs interrupts
- Connect to BasCAT I/O

### Key Concepts

**Memory-Mapped I/O** (BasCAT uses this):
```
Address 254 (0xFE): OUTPUT device
Address 255 (0xFF): INPUT device
```

Students have been using this!
```assembly
IN A           ; Read from 0xFF
OUT A          ; Write to 0xFE
```

**I/O Methods**:

1. **Polling** (what BasCAT does):
```assembly
wait:
  IN A         ; Check for input
  CMP A, 0
  JZ wait      ; Wait until something there
```

2. **Interrupts** (real systems):
   - Hardware signals CPU
   - CPU saves state
   - Handles interrupt
   - Resumes program

**I/O Devices**:
- Keyboard (input)
- Display (output)
- Disk drives (both)
- Network cards (both)

**Activity**: Design simple I/O system for custom device

---

## Week 9, Day 5: Lab Day - Architecture Exploration

**Topic**: Computer Architecture Analysis
**Duration**: 50 minutes
**Learning Objectives**:
- Apply architecture knowledge
- Analyze BasCAT design
- Design improvements
- Present findings

### Lab Project Options

**Option 1: BasCAT Architecture Report**
- Analyze BasCAT CPU
- Document components
- Compare to real CPUs
- Suggest improvements

**Option 2: Performance Analysis**
- Compare assembly programs
- Count instructions
- Estimate cycles
- Optimize for speed

**Option 3: Custom Instruction Design**
- Design new instruction
- Explain encoding
- Show use cases
- Justify addition

**Option 4: Architecture Comparison**
- Research real CPU (ARM, x86, RISC-V)
- Compare to BasCAT
- Present similarities/differences
- Explain trade-offs

### Requirements

**All Projects Include**:
- Written report (2-3 pages)
- Diagrams/illustrations
- Code examples (if applicable)
- Presentation (5 min)

**Topics to Cover**:
- CPU components
- Instruction execution
- Memory system
- I/O handling

### Rubric (50 points)

**Technical Accuracy (20)**:
- Correct architecture concepts
- Accurate analysis
- Proper terminology

**Depth of Analysis (15)**:
- Thorough investigation
- Clear explanations
- Good examples

**Presentation (10)**:
- Clear diagrams
- Well-organized
- Professional quality

**Code/Examples (5)**:
- Working demonstrations
- Clear illustrations
- Proper documentation

**Bonus (+10)**:
- Research beyond requirements
- Creative insights
- Exceptional presentation

---

## Week 9 Assessment

**Written Exam** (25 pts):
1. Label CPU diagram (5)
2. Explain fetch-execute (5)
3. Memory hierarchy (5)
4. Instruction encoding (5)
5. I/O methods (5)

**Practical Analysis** (25 pts):
- Analyze given program
- Count cycles/memory access
- Suggest optimizations
- Justify recommendations

---

## Week Reflection

**Key Takeaways**:
1. Computers are layered systems
2. Trade-offs everywhere (speed/size/cost)
3. Simple principles, complex implementation
4. BasCAT teaches real concepts

**Connection to Earlier Weeks**:
- Week 1-6: Used these concepts
- Week 7-8: Abstracted away from them
- Week 9: Understood how it all works

**Next Week**: "Compiler Design - BASIC to Assembly!"

---

## Standards Alignment

**CSTA**: 
- 3A-CS-01: Explain how abstractions hide implementation details
- 3A-CS-02: Compare levels of abstraction

**Learning Objectives**:
- LO1.1: Explain CPU components and their functions
- LO1.2: Trace data flow through computer system
- LO1.3: Trace control flow during execution
- LO5.1: Explain abstraction layers in computing systems

---

*End of Week 9 Complete Lesson Series*
