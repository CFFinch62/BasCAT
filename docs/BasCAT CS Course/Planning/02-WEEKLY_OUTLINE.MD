# BasCAT Course: 15-Week Detailed Outline

**Course**: Understanding Computers from the Ground Up **Platform**: BasCAT

------

## PART 1: ASSEMBLY PROGRAMMING (Weeks 1-6)

------

### Week 1: Data Movement - "The CPU's Scratch Pad"

**Learning Objectives**:

- Understand registers as fast temporary storage
- Load immediate values into registers
- Move data between registers
- Store and load data from memory
- Distinguish addressing modes (immediate, direct)

**BasCAT Instructions**: LOAD, MOV, LDM, STM, OUT, HALT

#### Day 1: Introduction & First Program

- **Concept**: What is a register? Why do we need them?

- **Activity**: Write "Hello World" (output a number)

  ```assembly
  LOAD A, 72    ; ASCII 'H'OUT AHALT
  ```

- **Circuit Focus**: Watch value travel from instruction → CPU → register A → output

- **Homework**: Modify program to output your age

#### Day 2: Multiple Registers

- **Concept**: General-purpose vs special registers

- **Activity**: Load different values into A, B, C, D

  ```assembly
  LOAD A, 10LOAD B, 20LOAD C, 30LOAD D, 40OUT AOUT BOUT COUT DHALT
  ```

- **Circuit Focus**: All four general-purpose registers visible

- **Homework**: Store 5 facts about yourself in registers, output in reverse order

#### Day 3: Moving Data with MOV

- **Concept**: Copying vs moving data

- **Activity**: MOV instruction practice

  ```assembly
  LOAD A, 100MOV B, A      ; Copy A to BMOV C, B      ; Copy B to CMOV D, C      ; Copy C to DOUT D         ; All have 100HALT
  ```

- **Circuit Focus**: Register-to-register data transfer

- **Challenge**: Swap two registers (introduces stack concept)

- **Homework**: Create a "data chain" through all registers

#### Day 4: Memory Storage

- **Concept**: RAM as permanent storage (vs registers)

- **Activity**: Store and retrieve from memory

  ```assembly
  LOAD A, 42STM 10, A     ; Store to memory[10]LOAD A, 0     ; Clear registerLDM A, 10     ; Load from memory[10]OUT A         ; Should output 42HALT
  ```

- **Circuit Focus**: Address bus, data bus, RAM component

- **Homework**: Create a "variable database" with 5 stored values

#### Day 5: Lab Day - Personal Data Card

- **Project**: Store personal data (age, birth month, favorite number, etc.)
- **Requirements**:
  - Use at least 5 memory locations
  - Retrieve and display in different order than stored
  - Include comments explaining each value
- **Assessment**: Code review, circuit tracing diagram
- **Reflection**: What's the difference between registers and memory?

**Week 1 Quiz**: Friday, covers registers, memory, addressing modes

------

### Week 2: Arithmetic & I/O - "Making the Computer Calculate"

**Learning Objectives**:

- Perform addition and subtraction
- Understand ALU operations and flags
- Use IN instruction for user input
- Combine arithmetic with I/O

**BasCAT Instructions**: ADD, SUB, IN (plus Week 1 instructions)

#### Day 1: Addition Basics

- **Concept**: How the ALU performs addition

- **Activity**: Simple calculator

  ```assembly
  LOAD A, 10ADD A, 5      ; A = 15OUT AHALT
  ```

- **Circuit Focus**: ALU component inside CPU, flags display

- **Challenge**: Add three numbers together

- **Homework**: Create addition table (1+1, 1+2, 1+3, etc.)

#### Day 2: Subtraction & Flags

- **Concept**: Flags (Z, N, C, O) and what they mean

- **Activity**: Subtraction practice

  ```assembly
  LOAD A, 20SUB A, 5      ; A = 15OUT AHALT
  ```

- **Circuit Focus**: Watch flags change based on result

- **Homework**: Experiment with subtraction causing underflow

#### Day 3: User Input with IN

- **Concept**: Memory-mapped I/O, getting data from outside

- **Activity**: Echo program

  ```assembly
  IN A          ; Read user inputOUT A         ; Echo it backHALT
  ```

- **Circuit Focus**: I/O ports (0xFF input, 0xFE output)

- **Discussion**: Why memory-mapped I/O? Alternatives?

- **Homework**: Read two numbers, output both

#### Day 4: Interactive Calculator

- **Concept**: Combining input, arithmetic, output

- **Activity**: Two-number addition

  ```assembly
  IN A          ; First numberIN B          ; Second numberADD A, B      ; Sum in AOUT A         ; Display resultHALT
  ```

- **Circuit Focus**: Complete data flow: input → registers → ALU → output

- **Homework**: Create subtraction calculator

#### Day 5: Lab Day - Four-Function Calculator

- **Project**: Calculator with +, -, (and later *, /)
- **Requirements**:
  - Read operation choice (1=add, 2=subtract)
  - Read two operands
  - Perform calculation
  - Output result
- **Extension**: Add multiplication by repeated addition
- **Reflection**: Why is the ALU inside the CPU?

**Week 2 Quiz**: Friday, covers arithmetic, flags, I/O

------

### Week 3: Logic Operations - "Thinking in Bits"

**Learning Objectives**:

- Understand binary representation
- Perform AND, OR, XOR, NOT operations
- Use logic for bit masking
- Apply logic operations to solve problems

**BasCAT Instructions**: AND, OR, XOR, NOT

#### Day 1: Binary Basics & AND

- **Concept**: Binary numbers, truth tables

- **Activity**: AND operation

  ```assembly
  LOAD A, 0b11110000AND A, 0b00001111  ; Result: 0OUT AHALT
  ```

- **Circuit Focus**: ALU performing logic operation

- **Homework**: Create AND truth table with code

#### Day 2: OR and XOR

- **Concept**: Set bits (OR), toggle bits (XOR)

- **Activity**: Bit manipulation

  ```assembly
  LOAD A, 0b00001111OR A, 0b11110000   ; Result: 0xFFOUT ALOAD A, 0b10101010XOR A, 0b11111111  ; Toggle all bitsOUT AHALT
  ```

- **Homework**: Experiment with different bit patterns

#### Day 3: NOT and Bit Masking

- **Concept**: Inverting bits, extracting specific bits

- **Activity**: Mask operations

  ```assembly
  LOAD A, 0b11010110AND A, 0b00001111  ; Keep only lower nibbleOUT AHALT
  ```

- **Real-world**: Network subnetting, permissions, color values

- **Homework**: Extract individual bits (bit 0, bit 7, etc.)

#### Day 4: Logic Applications

- **Concept**: Practical uses of bit operations

- **Activity**: Simple encryption (XOR cipher)

  ```assembly
  IN A           ; Read characterXOR A, 0x5A    ; Encrypt with keyOUT A          ; Output encryptedHALT
  ```

- **Challenge**: Decrypt the same way (XOR again)

- **Homework**: Create permission checker (read=bit 0, write=bit 1, execute=bit 2)

#### Day 5: Lab Day - Simple Calculator Enhancement

- **Project**: Add AND/OR/XOR operations to calculator
- **Requirements**:
  - Read operation choice (1-6)
  - Read two operands
  - Perform arithmetic OR logic operation
  - Output result
- **Assessment**: Working calculator + code explanation

**Week 3 Project Due**: Simple Calculator (10% of grade) **Week 3 Quiz**: Friday, covers logic operations, binary

------

### Week 4: Control Flow - "Making Decisions"

**Learning Objectives**:

- Understand program counter and jumps
- Use CMP to set flags
- Implement conditional branches
- Create loops

**BasCAT Instructions**: CMP, JMP, JZ, JNZ, JC, JNC

#### Day 1: Unconditional Jumps

- **Concept**: Program counter, sequential vs non-sequential execution

- **Activity**: Infinite loop

  ```assembly
  loop:  LOAD A, 1  OUT A  JMP loop    ; Jump back to loop
  ```

- **Circuit Focus**: PC register changes on jump

- **Warning**: Infinite loops! Use HALT to stop.

- **Homework**: Create countdown (manual jumps)

#### Day 2: Comparison & Flags

- **Concept**: CMP instruction, reading flags

- **Activity**: Conditional jump introduction

  ```assembly
  LOAD A, 10CMP A, 10    ; Compare A with 10JZ equal     ; Jump if zero flag setLOAD A, 0OUT AHALTequal:  LOAD A, 1  OUT A  HALT
  ```

- **Circuit Focus**: Flags register after CMP

- **Homework**: Experiment with JC, JNC

#### Day 3: Loops with Conditionals

- **Concept**: Counter loops, termination conditions

- **Activity**: Count from 0 to 9

  ```assembly
  LOAD A, 0loop:  OUT A  ADD A, 1  CMP A, 10  JNZ loop    ; Continue if not 10HALT
  ```

- **Circuit Focus**: Loop iteration visualization

- **Homework**: Count backwards from 10 to 0

#### Day 4: IF-ELSE Logic

- **Concept**: Conditional branching, code paths

- **Activity**: Number comparison

  ```assembly
  IN A          ; Read numberCMP A, 50JC less       ; Jump if less than 50LOAD A, 1     ; >= 50OUT AHALTless:  LOAD A, 0  OUT A  HALT
  ```

- **Homework**: Three-way comparison (<50, =50, >50)

#### Day 5: Lab Day - Interactive Programs

- **Project**: Number guessing game or input validator
- **Requirements**:
  - Use loops
  - Use conditionals
  - Accept user input
  - Provide meaningful output
- **Extension**: Count how many attempts user makes
- **Reflection**: How do high-level IF and FOR map to assembly?

**Week 4 Quiz**: Friday, covers control flow, loops

------

### Week 5: Stack & Memory - "Organizing Data"

**Learning Objectives**:

- Understand stack (LIFO) architecture
- Use PUSH and POP instructions
- Manage stack pointer
- Organize data in memory

**BasCAT Instructions**: PUSH, POP

#### Day 1: Introduction to the Stack

- **Concept**: LIFO (Last In, First Out), stack pointer

- **Activity**: Basic push/pop

  ```assembly
  LOAD A, 10PUSH A        ; Save ALOAD A, 0     ; Modify APOP A         ; Restore AOUT A         ; Should output 10HALT
  ```

- **Circuit Focus**: SP register, stack memory area

- **Homework**: Push multiple values, pop in reverse

#### Day 2: Register Preservation

- **Concept**: Saving/restoring state

- **Activity**: "Subroutine" pattern

  ```assembly
  ; Save all registersPUSH APUSH BPUSH CPUSH D; Do work that modifies registersLOAD A, 99; Restore all registersPOP DPOP CPOP BPOP AHALT
  ```

- **Homework**: Nested pushes (stack depth experiment)

#### Day 3: Stack Applications

- **Concept**: Using stack for temporary storage

- **Activity**: Swap registers without temp

  ```assembly
  LOAD A, 10LOAD B, 20PUSH APUSH BPOP A         ; A = 20POP B         ; B = 10OUT AOUT BHALT
  ```

- **Challenge**: Reverse order of 4 values

- **Homework**: Expression evaluation using stack

#### Day 4: Memory Organization

- **Concept**: Memory map, data structures

- **Activity**: Array-like storage

  ```assembly
  ; Store array of 5 valuesLOAD A, 10STM 50, ALOAD A, 20STM 51, A; ... etc; Access by indexLDM A, 50     ; array[0]LDM B, 51     ; array[1]HALT
  ```

- **Homework**: Create grade book (10 grades)

#### Day 5: Lab Day - Data Structure

- **Project**: Implement simple data structure
- **Options**:
  - Array sum/average
  - Find maximum in list
  - Reverse list using stack
  - Simple buffer
- **Assessment**: Correct implementation + memory map diagram
- **Reflection**: Why is the stack useful?

**Week 5 Quiz**: Friday, covers stack, memory organization

------

### Week 6: Complex Programs - "Putting It All Together"

**Learning Objectives**:

- Combine all assembly concepts
- Design non-trivial programs
- Debug complex code
- Optimize for size/speed

**BasCAT Instructions**: All 23 instructions

#### Day 1: Program Design

- **Concept**: Algorithm design before coding
- **Activity**: Plan a complex program (flowchart, pseudocode)
- **Example**: Text-based game (guess the number, adventure)
- **Discussion**: Breaking problems into steps
- **Homework**: Design your own program idea

#### Day 2: Implementation Workshop

- **Concept**: Incremental development
- **Activity**: Build program in stages
  - Stage 1: Basic structure
  - Stage 2: Add input
  - Stage 3: Add logic
  - Stage 4: Polish
- **Homework**: Continue implementation

#### Day 3: Debugging Strategies

- **Concept**: Common errors, using circuit view for debugging
- **Activity**: Debug broken programs
- **Techniques**:
  - Tracing execution
  - Checking flags
  - Memory inspection
  - Step-by-step execution
- **Homework**: Debug 3 provided broken programs

#### Day 4: Optimization

- **Concept**: Size vs speed tradeoffs
- **Activity**: Optimize example program
  - Reduce instruction count
  - Reduce memory usage
  - Improve algorithm efficiency
- **Homework**: Optimize your Week 6 project

#### Day 5: Lab Day - Project Work

- **Project**: Assembly Application (15% of grade)
- **Options**:
  - Text-based game (number guessing, simple adventure)
  - Data processing tool (statistics, sorting)
  - Interactive calculator (extended)
  - Simulation (simple state machine)
- **Requirements**:
  - Uses all major concepts (I/O, loops, conditionals, stack)
  - Well-commented code
  - Memory map documentation
  - Demonstration of working program

**Week 6 Project Due**: Assembly Application (15% of grade) **Week 6 Quiz**: Comprehensive assembly review

------

## PART 2: BASIC PROGRAMMING (Weeks 7-10)

------

### Week 7: BASIC Basics - "Abstraction Begins"

**Learning Objectives**:

- Write SimpleBASCAT programs
- Understand compilation process
- Map BASIC to assembly mentally
- Use variables instead of memory addresses

**SimpleBASCAT Features**: LET, PRINT, INPUT, REM, END

#### Day 1: Hello World in BASIC

- **Concept**: High-level vs low-level languages

- **Activity**: First BASIC program

  ```basic
  10 REM Hello World20 PRINT 7230 END
  ```

- **View Compilation**: See assembly output

- **Compare**: Same program in assembly (Week 1)

- **Homework**: Modify to print your name (ASCII values)

#### Day 2: Variables

- **Concept**: Named memory locations

- **Activity**: Variable assignment

  ```basic
  10 LET A = 1020 LET B = 2030 LET C = A + B40 PRINT C50 END
  ```

- **View Compilation**: How LET becomes LOAD/STM

- **Homework**: Create multi-step calculation

#### Day 3: Input and Output

- **Concept**: Interactive programs in BASIC

- **Activity**: Echo program

  ```basic
  10 INPUT A20 PRINT A30 END
  ```

- **Compare**: Assembly version (Week 2)

- **Discussion**: How much simpler is BASIC?

- **Homework**: Interactive calculator (BASIC)

#### Day 4: Arithmetic in BASIC

- **Concept**: Expression evaluation

- **Activity**: Complex expressions

  ```basic
  10 LET A = 520 LET B = 330 LET C = A + B40 LET D = C - A50 PRINT D60 END
  ```

- **View Compilation**: See multiple assembly instructions

- **Homework**: Implement formula (temperature conversion, etc.)

#### Day 5: Lab Day - BASIC Practice

- **Project**: Rewrite Week 2 calculator in BASIC
- **Requirements**:
  - User-friendly prompts
  - Multiple operations
  - Clear output
- **Compare**: Lines of BASIC vs lines of assembly
- **Reflection**: What's easier in BASIC? What's hidden?

**Week 7 Quiz**: Friday, covers BASIC syntax, variables

------

### Week 8: Control Structures - "BASIC Logic"

**Learning Objectives**:

- Use IF...THEN statements
- Implement FOR...NEXT loops
- Use GOTO (sparingly)
- Understand structured programming

**SimpleBASCAT Features**: IF...THEN, FOR...NEXT, GOTO

#### Day 1: Conditional Statements

- **Concept**: IF...THEN in BASIC

- **Activity**: Comparison program

  ```basic
  10 INPUT A20 IF A > 50 THEN GOTO 5030 PRINT 040 END50 PRINT 160 END
  ```

- **View Compilation**: See CMP and conditional jump

- **Homework**: Three-way comparison

#### Day 2: FOR Loops

- **Concept**: Counted loops

- **Activity**: Count from 0 to 9

  ```basic
  10 FOR I = 0 TO 920   PRINT I30 NEXT I40 END
  ```

- **View Compilation**: See loop assembly code

- **Compare**: Assembly version (Week 4)

- **Homework**: Multiplication table using loop

#### Day 3: Nested Loops

- **Concept**: Loops within loops

- **Activity**: Pattern generation

  ```basic
  10 FOR I = 1 TO 520   FOR J = 1 TO 530     PRINT I40   NEXT J50 NEXT I60 END
  ```

- **Challenge**: Triangle pattern (increasing output)

- **Homework**: Create interesting pattern

#### Day 4: Combining IF and FOR

- **Concept**: Complex control flow

- **Activity**: Filtering with conditions

  ```basic
  10 FOR I = 0 TO 1020   IF I > 5 THEN GOTO 5030   PRINT I40 NEXT I50 END
  ```

- **Homework**: Even number printer, prime checker

#### Day 5: Lab Day + MIDTERM REVIEW

- **Lab**: Practice problems combining all BASIC features
- **Review**: Assembly concepts for midterm
- **Practice**: Sample midterm problems

**Week 8 MIDTERM EXAM**: Friday (15% of grade)

- Part 1: Assembly programming
- Part 2: Short answer (architecture concepts)
- Part 3: Code reading/tracing

------

### Week 9: Compilation Viewing - "Lifting the Hood"

**Learning Objectives**:

- Understand compilation process deeply
- Predict assembly from BASIC
- Optimize BASIC for efficiency
- Debug using both views

**Focus**: Dual-editor view, source mapping

#### Day 1: Compilation Deep Dive

- **Concept**: Lexer, parser, code generator
- **Activity**: Watch compilation step-by-step
- **Exercise**: Predict assembly before compiling
- **Discussion**: Why multiple steps?
- **Homework**: Predict assembly for 5 BASIC programs

#### Day 2: Source Line Mapping

- **Concept**: BASIC line → Assembly lines
- **Activity**: Dual-view execution
  - Step through BASIC
  - Watch assembly execute
  - See mapping in action
- **Homework**: Trace complex program both ways

#### Day 3: Efficiency Analysis

- **Concept**: Good vs bad BASIC code
- **Activity**: Compare two solutions
  - Inefficient version (many instructions)
  - Efficient version (fewer instructions)
- **Learn**: Compiler limitations
- **Homework**: Optimize provided BASIC code

#### Day 4: Debugging with Both Views

- **Concept**: Use assembly view to understand bugs
- **Activity**: Debug BASIC program using assembly
- **Techniques**:
  - Check flags in assembly view
  - Verify memory in circuit view
  - Track registers during loops
- **Homework**: Fix 3 buggy BASIC programs

#### Day 5: Lab Day - Translation Challenge

- **Project**: Translate assembly to BASIC
- **Given**: Complex assembly program
- **Task**: Write equivalent BASIC program
- **Compare**: Are they identical? Why or why not?
- **Reflection**: When would you use assembly vs BASIC?

**Week 9 Quiz**: Friday, covers compilation, optimization

------

### Week 10: Complex BASIC Programs - "Real Applications"

**Learning Objectives**:

- Design complete programs
- Apply all BASIC features
- Create user-friendly applications
- Document code effectively

**Focus**: Final BASIC project

#### Day 1: Project Planning

- **Concept**: Requirements, design, implementation
- **Activity**: Choose project idea
- **Options**:
  - Game (Week 6 project in BASIC)
  - Data analyzer (statistics on input)
  - Interactive quiz
  - Text adventure
- **Deliverable**: Design document (flowchart, pseudocode)

#### Day 2-3: Implementation

- **Activity**: Code project
- **Support**: Teacher circulates, helps debug
- **Peer Review**: Share progress, get feedback
- **Homework**: Continue development

#### Day 4: Testing & Polish

- **Concept**: User testing, edge cases
- **Activity**: Test each other's programs
- **Improvements**: Fix bugs, add features
- **Homework**: Final polish

#### Day 5: Presentations

- **Project**: BASIC Application (15% of grade)
- **Present**: 3-minute demo + 2-minute Q&A
- **Discuss**: Design decisions, challenges, learning
- **Reflection**: BASIC vs Assembly - when to use each?

**Week 10 Project Due**: BASIC Application (15% of grade)

------

## PART 3: COMPUTER ARCHITECTURE CONCEPTS (Weeks 11-15)

------

### Week 11: CPU Architecture Deep Dive

**Learning Objectives**:

- Understand fetch-decode-execute cycle in depth
- Learn about pipelining
- Explore cache memory
- Compare simple vs modern CPUs

**Topics**: Instruction cycle, pipeline, cache, modern features

#### Day 1: Fetch-Decode-Execute

- **Concept**: The instruction cycle
- **Activity**: Trace execution step-by-step
- **BasCAT**: Watch PC, IR, MAR during execution
- **Discussion**: Why is this cycle fundamental?
- **Homework**: Draw cycle diagram for sample program

#### Day 2: Pipelining

- **Concept**: Overlapping instruction execution
- **Activity**: Compare sequential vs pipelined
- **Simulation**: Model pipeline with students (physical activity)
- **Tradeoffs**: Speed vs complexity
- **Homework**: Research pipeline hazards

#### Day 3: Cache Memory

- **Concept**: Memory hierarchy, locality
- **Activity**: Simulate cache hit/miss
- **BasCAT Connection**: Why aren't BasCAT's registers a cache?
- **Real-world**: Modern CPU cache levels (L1, L2, L3)
- **Homework**: Calculate cache performance for scenarios

#### Day 4: Modern CPU Features

- **Concept**: Superscalar, out-of-order execution, branch prediction
- **Activity**: Compare BasCAT to modern CPU (Intel, ARM)
- **Discussion**: Evolution of architecture
- **Homework**: Research specific modern CPU

#### Day 5: Lab Day - CPU Comparison

- **Project**: Compare architectures
- **Task**: Create presentation comparing BasCAT, 6502, and modern CPU
- **Focus**: Instruction set, features, performance

**Week 11 Quiz**: Friday, covers CPU architecture

------

### Week 12: Memory Hierarchy

**Learning Objectives**:

- Understand memory types and characteristics
- Learn about virtual memory
- Explore memory management
- Connect to BasCAT's simple memory

**Topics**: RAM, ROM, virtual memory, memory management

#### Day 1: Memory Types

- **Concept**: RAM, ROM, volatile vs non-volatile
- **Activity**: Compare characteristics (speed, cost, persistence)
- **BasCAT**: All RAM (no ROM)
- **Real-world**: Flash, SSD, HDD
- **Homework**: Memory hierarchy diagram

#### Day 2: Virtual Memory

- **Concept**: Address spaces, paging, TLB
- **Activity**: Simulate page table lookup
- **Discussion**: Why virtual memory?
- **Homework**: Calculate page table for scenario

#### Day 3: Memory Management

- **Concept**: Allocation, fragmentation, garbage collection
- **Activity**: Simulate memory allocator
- **Connection**: BasCAT's fixed addresses vs dynamic
- **Homework**: Research garbage collection algorithms

#### Day 4: Memory Performance

- **Concept**: Latency, bandwidth, bottlenecks
- **Activity**: Analyze memory access patterns
- **BasCAT**: Every memory access is same speed
- **Real-world**: DRAM timing, memory controllers
- **Homework**: Optimize program for memory access

#### Day 5: Lab Day - Memory Deep Dive

- **Project**: Memory map analysis
- **Task**: Diagram memory usage of complex program
- **Deliverable**: Memory map + access pattern analysis

**Week 12 Quiz**: Friday, covers memory hierarchy

------

### Week 13: I/O Systems

**Learning Objectives**:

- Understand I/O architectures
- Learn about interrupts
- Explore DMA (Direct Memory Access)
- Compare I/O methods

**Topics**: Memory-mapped I/O, interrupts, DMA, peripherals

#### Day 1: I/O Methods

- **Concept**: Memory-mapped vs port-mapped, polling vs interrupts
- **Activity**: Compare approaches
- **BasCAT**: Memory-mapped polling (simplest)
- **Real-world**: Modern interrupt-driven I/O
- **Homework**: Research specific I/O device

#### Day 2: Interrupts

- **Concept**: Hardware interrupts, interrupt vectors, handlers
- **Activity**: Simulate interrupt handling
- **Discussion**: Why interrupts? Limitations?
- **Homework**: Design interrupt system for BasCAT (theoretical)

#### Day 3: DMA

- **Concept**: Direct Memory Access, bus mastering
- **Activity**: Compare CPU-driven vs DMA
- **Performance**: Calculate DMA advantage
- **Homework**: Analyze when DMA is beneficial

#### Day 4: Peripheral Devices

- **Concept**: Keyboards, displays, storage, network
- **Activity**: Research modern peripheral interfaces
- **Standards**: USB, PCIe, SATA, etc.
- **Homework**: Trace data path for specific device

#### Day 5: Lab Day - I/O Design

- **Project**: Design I/O system
- **Task**: Extend BasCAT with new I/O device (theoretical)
- **Options**: Timer, display, storage
- **Deliverable**: Architecture diagram + interface spec

**Week 13 Quiz**: Friday, covers I/O systems

------

### Week 14: Real-World Architectures

**Learning Objectives**:

- Compare historical and modern architectures
- Understand RISC vs CISC
- Learn about ARM, x86, and other architectures
- Connect BasCAT concepts to real processors

**Topics**: 6502, Z80, 8086, ARM, x86-64, RISC-V

#### Day 1: Historical Context

- **Concept**: Evolution of CPUs (1970s-today)
- **Activity**: Timeline of important processors
- **Comparison**: BasCAT vs 6502 vs Z80
- **Discussion**: Design decisions then and now
- **Homework**: Research specific vintage CPU

#### Day 2: RISC vs CISC

- **Concept**: Reduced vs Complex Instruction Set
- **Activity**: Compare ARM (RISC) to x86 (CISC)
- **BasCAT**: Which category?
- **Tradeoffs**: Simplicity vs power
- **Homework**: Find RISC and CISC examples in real code

#### Day 3: Modern x86

- **Concept**: x86-64 architecture, backward compatibility
- **Activity**: Examine x86 assembly
- **Comparison**: x86 vs BasCAT assembly
- **Discussion**: Why is x86 so complex?
- **Homework**: Write simple x86 program (optional)

#### Day 4: ARM & Mobile

- **Concept**: ARM architecture, mobile/embedded
- **Activity**: Compare ARM to x86
- **Real-world**: Phones, tablets, embedded systems
- **Discussion**: Why ARM for mobile?
- **Homework**: Research ARM vs x86 in specific devices

#### Day 5: Lab Day - Architecture Comparison

- **Project**: Presentation on real architecture
- **Task**: Deep dive into one real processor
- **Deliverable**: 5-minute presentation + comparison to BasCAT
- **Topics**: Instruction set, features, history, applications

**Week 14 Quiz**: Friday, covers architectures

------

### Week 15: Final Projects & Assessment

**Learning Objectives**:

- Demonstrate comprehensive understanding
- Apply concepts creatively
- Communicate technical knowledge
- Reflect on learning journey

**Topics**: Final project, presentations, comprehensive exam

#### Day 1: Final Project Work

- **Project**: Original Program (10% of grade)
- **Options**:
  - Assembly or BASIC (or both!)
  - Game, tool, simulation, art
  - Must demonstrate multiple concepts
- **Time**: Open lab for development

#### Day 2: Final Project Work (continued)

- **Activity**: Peer testing
- **Feedback**: Give and receive suggestions
- **Polish**: Final improvements

#### Day 3: Project Presentations

- **Format**: 5-minute demo + 3-minute Q&A
- **Content**:
  - What does your program do?
  - What concepts does it use?
  - What challenges did you face?
  - What are you proud of?
- **Assessment**: Functionality + explanation + code quality

#### Day 4: Comprehensive Review

- **Activity**: Review all topics
- **Format**: Student-led review stations
- **Topics**: Assembly, BASIC, Architecture, I/O, Memory
- **Practice**: Sample exam questions

#### Day 5: FINAL EXAM

- **Format**: (20% of grade)
  - Part 1: Programming (assembly or BASIC)
  - Part 2: Code reading and tracing
  - Part 3: Short answer (concepts)
  - Part 4: Essay (architecture analysis)
- **Time**: Full class period

**Week 15 Final Project Due**: Original Program (10% of grade) **Week 15 Final Exam**: Comprehensive assessment (20% of grade)

------

## Course Completion

**Post-Course**:

- Grade final projects and exams
- Provide individual feedback
- Distribute certificates/completion letters
- Survey students on experience
- Recommend next steps for continued learning

**Student Outcomes**:

- Portfolio of programs (assembly and BASIC)
- Deep understanding of computer architecture
- Foundation for advanced CS study
- Confidence in problem-solving and debugging

------

*This detailed outline provides the roadmap for creating individual lesson plans in Phase 2.*
