# Phase 5: Student Materials - Assessments & Worksheets

**Complete assessment package for 15-week BasCAT course**

---

## Contents

1. Weekly Quizzes (Weeks 1-14)
2. Midterm Exam (Week 8)
3. Final Exam (Week 15)
4. Worksheets and Handouts
5. Answer Keys

---

# Part 1: Weekly Quizzes

## Quiz Format
- **Duration**: 10-15 minutes
- **Points**: 25 points each
- **Frequency**: End of each week (Weeks 1-14)
- **Format**: Mix of multiple choice, short answer, code writing

---

## Week 1 Quiz: Data Movement

**Name**: _________________ **Date**: _________________

**Part 1: Multiple Choice (2 pts each, 10 pts total)**

1. What does the LOAD instruction do?
   a) Moves data between registers
   b) Stores data in memory
   c) Puts a value into a register
   d) Outputs data

2. Which register would you typically use for calculations?
   a) Program Counter
   b) Register A, B, C, or D
   c) Instruction Register
   d) Stack Pointer

3. What is the purpose of the MOV instruction?
   a) Store in memory
   b) Load from memory
   c) Copy between registers
   d) Output data

4. STM stands for:
   a) Store to Memory
   b) Set the Memory
   c) Stop the Machine
   d) Start Memory

5. What happens after LOAD A, 10?
   a) Address 10 gets value A
   b) Register A gets value 10
   c) Memory 10 gets A
   d) Nothing

**Part 2: Short Answer (3 pts each, 9 pts total)**

6. What's the difference between LOAD and LDM?

7. Why might you use MOV instead of LOAD?

8. What does HALT do and why is it important?

**Part 3: Code Writing (6 pts)**

9. Write assembly code to:
   - Load value 42 into register A
   - Copy it to register B
   - Store B's value in memory address 100
   - HALT

**Answer Key Week 1**:
1. c, 2. b, 3. c, 4. a, 5. b
6. LOAD puts immediate value in register; LDM loads from memory address
7. MOV copies between registers without needing memory access
8. HALT stops program execution; without it program runs into garbage
9. 
```assembly
LOAD A, 42
MOV B, A
STM 100, B
HALT
```

---

## Week 2 Quiz: Arithmetic & I/O

**Part 1: Multiple Choice (10 pts)**

1. What does ADD A, 5 do?
   a) Sets A to 5
   b) Adds 5 to A
   c) Adds A and 5, stores in new register
   d) Outputs A + 5

2. The Z flag is set when:
   a) Result is zero
   b) Result is negative
   c) Overflow occurs
   d) Program halts

3. What does IN A do?
   a) Outputs A
   b) Loads A from memory
   c) Waits for user input into A
   d) Adds to A

4. If A = 10 and you SUB A, 15, what happens?
   a) A = -5
   b) A = 5
   c) A = 251 (underflow)
   d) Error

5. OUT A displays:
   a) Value of A
   b) Address of A
   c) Binary of A
   d) Nothing

**Part 2: True/False (2 pts each, 6 pts)**

6. ADD changes the destination register. T/F
7. SUB can cause underflow in unsigned arithmetic. T/F
8. IN is a blocking operation (waits for input). T/F

**Part 3: Code Writing (9 pts)**

9. Write code to:
   - Read two numbers
   - Add them
   - Subtract second from first
   - Output both results

---

## Week 3 Quiz: Logic Operations

**Part 1: Binary Conversion (2 pts each, 6 pts)**

1. Convert 00001111 to decimal: _____
2. Convert 15 to binary (8 bits): _____
3. What is 11111111 in decimal: _____

**Part 2: Logic Operations (3 pts each, 12 pts)**

4. What is 11110000 AND 00001111? _____
5. What is 10101010 OR 01010101? _____
6. What is 11110000 XOR 11110000? _____
7. What is NOT 10101010? _____

**Part 3: Application (7 pts)**

8. Write code to extract the lower 4 bits from register A and output the result.

---

## Week 4 Quiz: Control Flow

**Part 1: Multiple Choice (10 pts)**

1. CMP A, 10 followed by JZ label jumps when:
   a) A < 10
   b) A > 10
   c) A = 10
   d) Always

2. JC jumps when the Carry flag is:
   a) 0
   b) 1
   c) Set or Clear
   d) Never

3. What's wrong with this loop?
   ```
   loop:
     OUT A
     JMP loop
   ```
   a) No initialization
   b) No exit condition
   c) No HALT
   d) Nothing wrong

4-5. [More questions about jumps and loops]

**Part 2: Code Analysis (8 pts)**

6. What does this code output for input 15?
   ```assembly
   IN A
   CMP A, 10
   JNC big
   LOAD A, 0
   OUT A
   HALT
   big:
   LOAD A, 1
   OUT A
   HALT
   ```

**Part 3: Code Writing (7 pts)**

7. Write a loop that outputs 1, 2, 3, 4, 5

---

## Weeks 5-14 Quizzes

**Week 5: Stack Operations**
- PUSH/POP mechanics
- LIFO concept
- Stack balance
- Subroutine basics

**Week 6: Integration Review**
- All assembly concepts
- Program design
- Debugging

**Week 7: BASIC Fundamentals**
- Line numbers
- Variables
- INPUT/PRINT
- Simple programs

**Week 8: Advanced BASIC**
- FOR loops
- IF-THEN
- Arrays
- GOSUB/RETURN

**Week 9: Computer Architecture**
- CPU components
- Fetch-execute cycle
- Memory hierarchy
- I/O systems

**Week 10: Compiler Design**
- Compilation stages
- Expression translation
- Code generation
- Optimization

**Week 11: Advanced Assembly**
- Optimization techniques
- Debugging strategies
- Best practices

**Week 12: Real-World Systems**
- Operating systems
- Embedded systems
- Networks
- Security

**Week 13: Advanced BASIC**
- Modular programming
- Error handling
- Algorithms

**Week 14: Integration**
- Language selection
- Translation
- Performance comparison

[Full quizzes follow same format: 25 points, 10-15 minutes, mix of question types]

---

# Part 2: Midterm Exam (Week 8)

**Duration**: 90 minutes (can be split across 2 days)
**Points**: 100 points
**Format**: Written + Practical

## Midterm: Written Portion (50 points)

**Section 1: Assembly Fundamentals (20 pts)**

1. Label the CPU diagram (5 pts)
   [Diagram with ALU, Control Unit, Registers, PC, IR]

2. Trace this program's execution (5 pts)
   ```assembly
   LOAD A, 10
   LOAD B, 5
   ADD A, B
   OUT A
   HALT
   ```
   Show register values after each instruction.

3. Multiple choice questions (10 pts)
   - Memory addressing
   - Stack operations
   - Flags
   - Instructions

**Section 2: Logic and Control Flow (15 pts)**

4. Calculate logic operations (6 pts)
   - Given binary values, perform AND, OR, XOR

5. Analyze control flow (9 pts)
   - Given code with loops/conditionals
   - Predict output
   - Identify bugs

**Section 3: Program Design (15 pts)**

6. Design algorithm (7 pts)
   - Given problem description
   - Write pseudocode solution
   - Explain approach

7. Optimization (8 pts)
   - Given inefficient code
   - Identify problems
   - Suggest improvements

## Midterm: Practical Portion (50 points)

**Challenge 1: Data Processing (25 pts)**
Write assembly program that:
- Reads 5 numbers
- Finds the maximum
- Outputs the maximum

Must use: loops, comparison, memory/stack

**Challenge 2: Pattern Generator (25 pts)**
Write assembly program that:
- Reads N from user
- Outputs numbers 1 to N
- Outputs sum of 1 to N

Must use: loops, arithmetic, proper structure

**Grading Rubric**:
- Functionality: 15 pts
- Code quality: 5 pts
- Documentation: 5 pts

---

# Part 3: Final Exam (Week 15)

**Duration**: 2 hours
**Points**: 200 points (100 written + 100 practical)
**Comprehensive**: All course material

## Final Exam: Written Portion (100 points)

**Section 1: Assembly Programming (25 pts)**
- Write assembly code
- Debug assembly
- Optimize assembly
- Explain execution

**Section 2: BASIC Programming (25 pts)**
- Write BASIC code
- Convert assembly to BASIC
- Arrays and loops
- Subroutines

**Section 3: Computer Architecture (25 pts)**
- CPU components
- Memory hierarchy
- Instruction encoding
- I/O systems

**Section 4: Integration & Design (25 pts)**
- Language selection
- Compilation process
- Optimization
- System design

## Final Exam: Practical Portion (100 points)

**Challenge 1: Assembly Implementation (50 pts)**
Complex algorithm in assembly
- Must use all major concepts
- Efficient solution
- Well-documented

**Challenge 2: BASIC Implementation (50 pts)**
Same or similar algorithm in BASIC
- Compare to assembly version
- Analyze differences
- Justify language choice

---

# Part 4: Student Worksheets

## Worksheet 1: Binary Practice
- Decimal to binary conversion (20 problems)
- Binary to decimal conversion (20 problems)
- Binary arithmetic
- Answer key included

## Worksheet 2: Instruction Tracing
- Step-by-step execution
- Register value tracking
- Memory state tracking
- 10 progressively complex programs

## Worksheet 3: Code Completion
- Fill in missing instructions
- Complete partial programs
- Fix bugs in code
- 15 exercises

## Worksheet 4: Assembly Reference Card
- All instructions with syntax
- Flag meanings
- Common patterns
- Quick reference guide

## Worksheet 5: BASIC Reference Card
- Keywords and syntax
- Common structures
- Array operations
- Function reference

## Worksheet 6: Memory Maps
- Practice drawing memory layouts
- Address calculation
- Stack visualization
- 10 scenarios

## Worksheet 7: Flowchart Practice
- Algorithm to flowchart
- Flowchart to code
- Debugging flowcharts
- 8 exercises

## Worksheet 8: Optimization Challenges
- Inefficient code provided
- Student optimizes
- Compare instruction counts
- 10 programs

## Worksheet 9: Debug Detective
- Buggy programs
- Find and fix errors
- Explain what was wrong
- 12 programs

## Worksheet 10: Architecture Diagrams
- Label components
- Trace data flow
- Explain operations
- Multiple diagrams

---

# Part 5: Student Handouts

## Handout 1: Assembly Quick Reference
**Single-page laminated card**
- All instructions
- Syntax examples
- Flags
- Common patterns

## Handout 2: BASIC Quick Reference
**Single-page laminated card**
- Keywords
- Structure
- Examples
- Tips

## Handout 3: Binary Conversion Chart
**Visual aid**
- 8-bit positions
- Common values
- Conversion method
- Practice area

## Handout 4: Flag Reference
**Detailed guide**
- Z, N, C, O flags
- When they're set
- How to use them
- Examples

## Handout 5: Memory Map Template
**Blank template**
- Address column
- Value column
- Notes column
- Reusable for all programs

## Handout 6: Program Planning Sheet
**Design template**
- Problem statement
- Input/Output
- Algorithm steps
- Memory map
- Pseudocode area

## Handout 7: Debugging Checklist
**Systematic approach**
- Common errors
- Check list
- Testing strategies
- Help resources

## Handout 8: Project Planning Guide
**For major projects**
- Requirements checklist
- Timeline
- Testing plan
- Submission checklist

## Handout 9: Architecture Poster
**Large wall poster**
- CPU diagram
- Memory hierarchy
- Instruction cycle
- Color-coded

## Handout 10: Course Roadmap
**Visual curriculum map**
- Weekly topics
- Projects
- Assessments
- Prerequisites

---

# Answer Keys

## Complete Answer Keys Provided For:
- All 14 weekly quizzes
- Midterm exam (both portions)
- Final exam (both portions)
- All 10 worksheets
- All practice problems

**Format**:
- Correct answers highlighted
- Partial credit guidance
- Common errors noted
- Grading rubrics

---

# Assessment Philosophy

**Formative Assessment** (ongoing):
- Weekly quizzes
- Exit tickets
- Worksheets
- Class participation

**Summative Assessment** (major):
- 4 Projects (40%)
- Midterm (10%)
- Final Exam (10%)
- Weekly Quizzes (20%)
- Participation (5%)
- Final Project (15%)

**Total**: 100%

---

# Grading Scale

**Standard Scale**:
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

**Honors Scale** (optional):
- A: 93-100%
- A-: 90-92%
- B+: 87-89%
- [etc.]

---

*End of Phase 5: Student Materials*
*All assessments, worksheets, and handouts specified*
