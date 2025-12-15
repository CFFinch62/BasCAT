# BasCAT Course Assessment Framework

**Course**: Understanding Computers from the Ground Up
**Assessment Philosophy**: Multiple measures, growth-focused, authentic demonstrations of learning

---

## Assessment Overview

### Core Principles

1. **Multiple Measures**: No single test determines success
2. **Authentic Assessment**: Real programming, not just memorization
3. **Growth Mindset**: Revision and improvement encouraged
4. **Transparent Criteria**: Students know expectations upfront
5. **Formative Focus**: Regular feedback guides learning

### Assessment Categories

| Category | Weight | Purpose | Frequency |
|----------|--------|---------|-----------|
| Programming Projects | 50% | Apply skills to solve problems | 4 major projects |
| Weekly Quizzes | 15% | Check conceptual understanding | 14 quizzes |
| Midterm Exam | 15% | Assess assembly mastery | Week 8 |
| Final Exam | 15% | Comprehensive understanding | Week 15 |
| Participation/Labs | 5% | Engagement and effort | Ongoing |

---

## Programming Projects (50% total)

### Project 1: Simple Calculator (Week 3, 10%)

**Description**: Create a calculator in assembly that performs basic arithmetic operations.

**Requirements**:
- Accept user input for two numbers
- Allow user to choose operation (+, -, AND, OR)
- Perform calculation correctly
- Display result
- Include comments explaining each section

**Learning Objectives Assessed**:
- LO2.1: Write functional assembly programs
- LO2.2: Use registers effectively
- LO4.1: Decompose problems into steps

**Rubric**:

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| **Functionality** | All operations work correctly, handles edge cases | All operations work, minor issues | Most operations work | Program crashes or doesn't work |
| **Code Quality** | Well-organized, efficient, excellent comments | Organized, comments present | Somewhat organized, few comments | Disorganized, no comments |
| **Input/Output** | Clear prompts, formatted output | Functional I/O | Basic I/O working | I/O issues |
| **Use of Instructions** | Optimal instruction selection | Appropriate instructions | Some inefficiency | Poor instruction choices |

**Total**: 40 points (×2.5 = 10% of course grade)

**Submission**: Upload .asm file + memory map diagram + written explanation

**Late Policy**: -10% per day, max 3 days late

---

### Project 2: Assembly Application (Week 6, 15%)

**Description**: Create a complete application in assembly demonstrating all concepts learned.

**Options** (choose one):
1. **Number Guessing Game**: Computer picks number, user guesses, program gives hints
2. **Grade Analyzer**: Input grades, calculate average, find min/max
3. **Simple Text Adventure**: Room navigation with choices
4. **Custom Idea**: Propose your own (must be approved)

**Requirements**:
- Uses I/O (IN, OUT)
- Uses loops (CMP + conditional jumps)
- Uses conditionals (IF-THEN logic)
- Uses stack (PUSH/POP) for data management
- Uses memory (LDM/STM) for variable storage
- At least 40 lines of code (excluding comments)
- Well-commented (explain every section)
- Memory map documentation
- Demonstration video or live demo

**Learning Objectives Assessed**:
- LO2.1: Write functional assembly programs
- LO2.2: Use registers effectively
- LO2.3: Implement control structures
- LO2.4: Manage stack operations
- LO4.1: Decompose problems
- LO4.2: Implement algorithms efficiently

**Rubric**:

| Criterion | Excellent (5) | Proficient (4) | Developing (3) | Beginning (2) | Incomplete (1) |
|-----------|---------------|----------------|----------------|---------------|---------------|
| **Functionality** (15 pts) | Works perfectly, handles all inputs | Works correctly, minor edge case issues | Works mostly, some bugs | Limited functionality | Doesn't work |
| **Complexity** (10 pts) | Sophisticated algorithm, all features | Good complexity, most features | Adequate complexity | Too simple | Trivial |
| **Code Quality** (10 pts) | Excellent organization, optimal code | Well organized, good code | Acceptable organization | Poor organization | Very poor |
| **Documentation** (10 pts) | Excellent comments, complete memory map | Good comments, memory map | Basic comments | Few comments | No documentation |
| **Creativity** (5 pts) | Highly original | Original touches | Standard implementation | Basic | No creativity |

**Total**: 50 points (×3 = 15% of course grade)

**Submission**: .asm file + memory map + README explaining program + demo

**Presentation**: 3-minute demo in class

---

### Project 3: BASIC Application (Week 10, 15%)

**Description**: Recreate your Week 6 assembly project in BASIC (or create new application).

**Requirements**:
- Same functionality as assembly version OR new equivalent-complexity program
- Uses variables (LET)
- Uses control structures (IF...THEN, FOR...NEXT)
- Uses I/O (INPUT, PRINT)
- Well-commented
- Comparison document: BASIC vs Assembly (what's easier? harder? different?)

**Learning Objectives Assessed**:
- LO3.1: Write programs in SimpleBASCAT
- LO3.2: Understand compilation process
- LO3.3: Predict assembly output
- LO4.1: Problem decomposition

**Rubric**:

| Criterion | Excellent (5) | Proficient (4) | Developing (3) | Beginning (2) | Incomplete (1) |
|-----------|---------------|----------------|----------------|---------------|---------------|
| **Functionality** (15 pts) | Perfect, enhanced features | Works correctly | Works mostly | Limited function | Doesn't work |
| **BASIC Usage** (10 pts) | Excellent use of language features | Good use | Adequate | Poor | Very poor |
| **Code Quality** (10 pts) | Clean, readable, well-structured | Good structure | Acceptable | Poor | Very poor |
| **Comparison Analysis** (10 pts) | Deep insights, specific examples | Good analysis | Basic comparison | Minimal | Missing |
| **Presentation** (5 pts) | Engaging, clear | Clear | Acceptable | Poor | Missing |

**Total**: 50 points (×3 = 15% of course grade)

**Submission**: .bas file + compiled assembly + comparison document + demo

**Presentation**: 3-minute demo comparing BASIC and assembly versions

---

### Project 4: Final Project (Week 15, 10%)

**Description**: Original program demonstrating comprehensive understanding.

**Requirements**:
- Assembly OR BASIC (or both!)
- Original idea (not replicating previous projects)
- Demonstrates at least 4 major concepts:
  - [ ] Complex control flow (nested loops, multiple conditions)
  - [ ] Data structures (arrays, lists using memory)
  - [ ] User interaction (meaningful I/O)
  - [ ] Algorithm implementation (search, sort, calculate)
- Documentation package:
  - Design document (what, why, how)
  - User guide (how to use program)
  - Technical documentation (how it works)
  - Reflection (what you learned)

**Learning Objectives Assessed**: ALL

**Rubric**:

| Criterion | Excellent (5) | Proficient (4) | Developing (3) | Beginning (2) | Incomplete (1) |
|-----------|---------------|----------------|----------------|---------------|---------------|
| **Originality** (10 pts) | Highly creative, novel | Original touches | Standard idea | Derivative | Copied |
| **Technical Complexity** (10 pts) | Sophisticated, >4 concepts | 4 concepts well-used | 3 concepts | 2 concepts | Trivial |
| **Functionality** (10 pts) | Perfect, polished | Works well | Works mostly | Limited | Broken |
| **Documentation** (10 pts) | Comprehensive, professional | Complete | Adequate | Minimal | Missing |
| **Presentation** (10 pts) | Engaging, insightful | Clear, complete | Acceptable | Poor | Missing |

**Total**: 50 points (×2 = 10% of course grade)

**Presentation**: 5-minute demo + 3-minute Q&A

**Final Submission**: Complete package uploaded + in-class presentation

---

## Weekly Quizzes (15% total)

### Format
- **Frequency**: Fridays (Weeks 1-7, 9-15) = 14 quizzes
- **Duration**: 10-15 minutes
- **Format**: Mix of multiple choice, short answer, code snippets
- **Topics**: That week's material

### Grading
- Each quiz worth equal points
- Lowest 2 quiz scores dropped
- Remaining 12 quizzes averaged for grade

### Sample Quiz Questions

**Week 1 Quiz (Data Movement)**:
1. What is the primary difference between a register and memory? (2 pts)
2. Write an instruction to load the value 42 into register A. (2 pts)
3. What addressing mode does `STM 10, A` use? (2 pts)
4. Draw the data flow when executing `MOV B, A`. (4 pts)

**Week 4 Quiz (Control Flow)**:
1. What does the CMP instruction do? (2 pts)
2. Write a loop that counts from 5 down to 0. (5 pts)
3. When does the JZ instruction jump? (2 pts)
4. Explain how JNZ can create a loop. (3 pts)

**Week 7 Quiz (BASIC)**:
1. Write a BASIC program to add two numbers. (4 pts)
2. How does `LET A = 10` translate to assembly? (3 pts)
3. What's the difference between PRINT and OUT? (2 pts)
4. What do line numbers provide in BASIC? (1 pt)

### Retake Policy
- Can retake ONE quiz per semester
- Retake score replaces original
- Must be retaken within 1 week

---

## Midterm Exam (Week 8, 15%)

### Format
- **Duration**: Full class period (50 minutes)
- **Total Points**: 100 points

### Structure

**Part 1: Programming (40 points)**
- Write assembly program to solve given problem
- Example: "Write a program that reads numbers until 0 is entered, then outputs their sum"
- Graded on correctness, efficiency, comments

**Part 2: Code Reading (25 points)**
- Given assembly program, answer questions:
  - What does it do?
  - Trace execution for given input
  - Identify the value in register A after line X
  - Draw memory state at specific point

**Part 3: Short Answer (20 points)**
- Define key terms (ALU, stack, flags, etc.)
- Explain concepts (why registers? how does CMP work?)
- Compare/contrast (immediate vs direct addressing)

**Part 4: Circuit Analysis (15 points)**
- Given program, draw data flow through circuit
- Identify which components are used
- Explain bus traffic for specific instruction

### Sample Midterm Questions

**Programming**:
```
Write an assembly program that:
1. Reads a number from the user
2. Outputs all numbers from 1 to that number
3. For each number divisible by 3, output 99 instead

Example: Input 10, Output: 1 2 99 4 5 99 7 8 99 10
```

**Code Reading**:
```assembly
LOAD A, 0
LOAD B, 1
loop:
  OUT A
  MOV C, A
  ADD A, B
  MOV B, C
  CMP A, 20
  JC loop
HALT
```
Questions:
- What does this program output?
- What mathematical sequence is this?
- What's the value of B after the 3rd iteration?

**Short Answer**:
- Explain why the stack grows downward from 0xFD instead of upward from 0x00.
- What are the four ALU flags? Give an example of when each is set.

**Circuit Analysis**:
- For the instruction `ADD A, B`, trace the data flow from memory through all components to the final result.

### Grading Rubric
- Programming: Full credit for working code, partial for attempt
- Code Reading: All-or-nothing per question
- Short Answer: Points for completeness and accuracy
- Circuit Analysis: Points for each correct component/connection

---

## Final Exam (Week 15, 15%)

### Format
- **Duration**: Full class period (50 minutes)
- **Total Points**: 100 points
- **Comprehensive**: Covers all course material

### Structure

**Part 1: Programming Choice (30 points)**
- Choose to write in Assembly OR BASIC
- Solve moderately complex problem
- Graded on correctness and code quality

**Part 2: Compilation Analysis (20 points)**
- Given BASIC program, write the assembly it would compile to
- Or: Given assembly, write equivalent BASIC
- Tests understanding of compilation process

**Part 3: Architecture Concepts (30 points)**
- Multiple choice and short answer
- Covers CPU, memory, I/O, real architectures
- Application of concepts to scenarios

**Part 4: Essay (20 points)**
- Choose one of three prompts:
  1. "Explain how abstraction layers in computers make programming easier. Use specific BasCAT examples."
  2. "Compare BasCAT to a real computer (6502, ARM, x86). What's simplified in BasCAT and why?"
  3. "Design an extension to BasCAT (new instruction, feature, or capability). Explain what it does and why it's useful."

### Sample Final Questions

**Programming**:
```
Write a program (assembly OR BASIC) that:
- Reads 5 numbers from the user
- Stores them in memory
- Outputs them in reverse order
- Then outputs the largest number
```

**Compilation**:
```basic
10 LET A = 0
20 FOR I = 1 TO 5
30   LET A = A + I
40 NEXT I
50 PRINT A
60 END
```
Write the assembly code this BASIC program would compile to.

**Architecture**:
1. Explain the fetch-decode-execute cycle using a specific BasCAT instruction as an example.
2. Why does BasCAT use memory-mapped I/O instead of separate I/O instructions?
3. Compare BasCAT's stack to a modern computer's stack. What's similar? Different?

**Essay** (graded on depth, examples, clarity):
- Thesis statement
- Specific examples from course
- Clear explanation
- Connection to broader CS concepts

---

## Participation & Lab Work (5%)

### Components

**Daily Engagement** (2%)
- Attentiveness during demonstrations
- Asking/answering questions
- Helping peers
- Active participation in discussions

**Lab Work** (2%)
- On-task during lab time
- Making progress on projects
- Using class time effectively
- Seeking help appropriately

**Reflection Journals** (1%)
- Weekly reflection on learning
- Honest assessment of understanding
- Questions for clarification
- Connection to prior knowledge

### Grading
- Not about perfection, about effort
- Based on teacher observation
- Self-assessment component
- Peer feedback component

---

## Grading Scale

### Standard Scale
- A: 90-100%
- B: 80-89%
- C: 70-79%
- D: 60-69%
- F: Below 60%

### Alternative: Standards-Based Grading

**Mastery Levels**:
- 4 = Exceeds Standard (demonstrates advanced understanding)
- 3 = Meets Standard (demonstrates proficient understanding)
- 2 = Approaching Standard (demonstrates partial understanding)
- 1 = Below Standard (demonstrates minimal understanding)

**Learning Objectives Graded**:
- Each LO assessed multiple times
- Final grade = average of LO scores
- Students can revise work to improve scores

**Conversion to Letter Grade**:
- Average 3.5-4.0 = A
- Average 2.5-3.4 = B
- Average 1.5-2.4 = C
- Average 1.0-1.4 = D
- Average below 1.0 = F

---

## Revision Policy

### Projects
- Can revise and resubmit for improved grade
- Must resubmit within 1 week of receiving feedback
- New grade = average of original and revision (or higher of the two - teacher choice)
- Encourages growth mindset

### Quizzes
- One retake allowed per semester
- Must prepare and demonstrate readiness

### Exams
- No revisions (cumulative nature)
- Can improve through final project/exam

---

## Academic Integrity

### Expectations
- Individual work unless specified otherwise
- Collaboration on concepts encouraged
- Direct code copying prohibited
- Cite any code adapted from examples

### Violations
- First offense: Zero on assignment, parent contact, reflection assignment
- Second offense: Zero on assignment, meeting with administration
- Third offense: Course failure, administrative action

### Collaboration vs Cheating

**Allowed**:
- Discussing approaches and strategies
- Helping debug (pointing out errors)
- Sharing ideas and pseudocode
- Pair programming (when assigned)

**Not Allowed**:
- Copying code line-for-line
- Sharing actual code files
- Submitting someone else's work
- Using solutions found online

---

## Feedback Mechanisms

### For Students

**Immediate Feedback**:
- BasCAT circuit view (does your program work?)
- Compiler errors (syntax issues)
- Peer code review (fresh perspective)

**Regular Feedback**:
- Quiz results (conceptual understanding)
- Project rubrics (detailed assessment)
- Weekly check-ins (individual progress)

**Summative Feedback**:
- Exam results (comprehensive understanding)
- Final project evaluation (holistic view)
- Course reflection (growth narrative)

### For Teacher

**Student Feedback**:
- Weekly anonymous surveys (what's working?)
- Mid-semester evaluation (adjust course)
- End-of-course evaluation (improve next time)

**Self-Assessment**:
- Are learning objectives being met?
- What activities are most effective?
- Where are students struggling?

---

## Special Accommodations

### For Students with IEPs/504s
- Extended time on assessments
- Alternate assessment formats
- Reduced project scope (same concepts, smaller scale)
- Note-taking support
- Preferential seating for screen visibility

### For English Language Learners
- Vocabulary support (CS term glossary)
- Extra time for reading/writing
- Visual instruction emphasis (BasCAT helps!)
- Peer support/pairing

### For Advanced Students
- Extension activities
- Independent study options
- Mentor opportunities (help peers)
- Advanced topics (explore beyond curriculum)

---

## Assessment Calendar

### Semester Overview

| Week | Assessment | Weight |
|------|------------|--------|
| 1 | Quiz 1 | Quiz grade |
| 2 | Quiz 2 | Quiz grade |
| 3 | Quiz 3 + **Project 1** | Quiz + 10% |
| 4 | Quiz 4 | Quiz grade |
| 5 | Quiz 5 | Quiz grade |
| 6 | Quiz 6 + **Project 2** | Quiz + 15% |
| 7 | Quiz 7 | Quiz grade |
| 8 | **Midterm Exam** | 15% |
| 9 | Quiz 8 | Quiz grade |
| 10 | Quiz 9 + **Project 3** | Quiz + 15% |
| 11 | Quiz 10 | Quiz grade |
| 12 | Quiz 11 | Quiz grade |
| 13 | Quiz 12 | Quiz grade |
| 14 | Quiz 13 | Quiz grade |
| 15 | Quiz 14 + **Project 4** + **Final Exam** | Quiz + 10% + 15% |

**Total Quizzes**: 14 (drop 2 lowest = 12 count)
**Total Projects**: 4 (50% total)
**Total Exams**: 2 (30% total)
**Participation**: Ongoing (5%)

---

*This assessment framework ensures multiple opportunities for students to demonstrate learning through varied authentic tasks.*
