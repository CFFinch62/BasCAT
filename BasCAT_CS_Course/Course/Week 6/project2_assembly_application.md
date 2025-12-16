# Project 2: Assembly Game or Application

**Week**: 6 (Integration Project)
**Duration**: 5 class periods (full week)
**Points**: 100
**Type**: Individual project

---

## Project Overview

Students will create a comprehensive assembly program demonstrating mastery of all concepts from Weeks 1-6. This is a capstone project for the assembly programming unit.

---

## Learning Objectives

- LO2.1: Write functional assembly programs
- LO2.2: Use registers effectively
- LO2.3: Manage memory addressing
- LO2.4: Implement control structures
- LO2.5: Debug assembly programs
- LO4.1: Decompose problems
- LO4.2: Implement algorithms efficiently

---

## Project Options

Students choose ONE of the following:

### Option 1: Number Guessing Game
- Computer "thinks" of number (1-100)
- User guesses
- Program gives "higher" or "lower" hints
- Counts number of attempts
- Asks to play again

### Option 2: Quiz Program
- Stores 5 questions (expected answers in memory)
- Asks each question
- Checks user's answer
- Tracks score
- Displays final score

### Option 3: Data Analysis Tool
- Reads N numbers from user
- Calculates: min, max, sum, average
- Stores numbers in memory
- Displays all statistics

### Option 4: Simple Calculator with Memory
- Menu-driven calculator
- Operations: +, -, AND, OR, XOR
- Memory functions (store, recall, clear)
- Runs until user quits

### Option 5: Pattern Generator
- Creates visual patterns using numbers
- User chooses pattern type
- Generates pattern (counting, fibonacci, powers)
- Option to generate multiple patterns

### Option 6: Student's Choice
- Must get teacher approval
- Must use all required components
- Submit design document first

---

## Core Requirements

**ALL projects must include**:

### 1. Memory Usage (STM/LDM)
- Store at least 5 values in memory
- Load values from memory
- Document memory map

### 2. Stack Operations (PUSH/POP)
- Use stack to preserve values
- Balanced PUSH/POP
- Document stack usage

### 3. Arithmetic Operations
- At least 2 different operations (ADD, SUB)
- Use in meaningful way

### 4. Logic Operations
- At least 1 logic operation (AND, OR, XOR, NOT)
- Use for actual purpose (not just demo)

### 5. Comparisons (CMP)
- Use CMP for decisions
- Multiple comparisons

### 6. Conditional Jumps
- At least 3 different conditional jumps
- JZ, JNZ, JC, or JNC
- Use appropriately

### 7. Loops
- At least 2 loops
- Different loop types (count, condition)

### 8. User Interaction
- Read user input (IN)
- Display output (OUT)
- Interactive experience

### 9. Code Organization
- Clear sections
- Meaningful labels
- Logical flow

### 10. Documentation
- Header with program info
- Comments explaining logic
- Memory map documented

---

## Detailed Specifications

### Option 1: Number Guessing Game

**Starter Code**:
```assembly
; ==========================================
; PROGRAM: Number Guessing Game
; AUTHOR: _____________________
; ==========================================

; === CONSTANTS ===
; Secret number: 42 (can be changed)

; === MAIN GAME ===
LOAD A, 42     ; Secret number
LOAD B, 0      ; Attempt counter

game_loop:
  IN C         ; Get guess
  ADD B, 1     ; Increment attempts
  
  CMP C, A
  JZ correct   ; If equal, won!
  
  JC too_low   ; If C < A
  
  ; Too high
  LOAD D, 1
  OUT D        ; Output 1 for "too high"
  JMP game_loop
  
too_low:
  LOAD D, 0
  OUT D        ; Output 0 for "too low"
  JMP game_loop
  
correct:
  OUT B        ; Output number of attempts
  HALT

; === MEMORY MAP ===
; A: Secret number
; B: Attempt counter
; C: User's guess
; D: Hint output
```

**Expected Behavior**:
- User inputs guesses
- Program outputs:
  - 0 if guess too low
  - 1 if guess too high
  - Number of attempts when correct

**Bonus Ideas**:
- Ask to play again (+5)
- Random-ish secret number (+10)
- Track best score (+5)

---

### Option 2: Quiz Program

**Structure**:
```assembly
; Store correct answers at addresses 10-14
; Address 10: Answer to Q1
; Address 11: Answer to Q2
; etc.

; Load answers into memory
LOAD A, 5
STM 10, A     ; Q1: What is 2+3?
LOAD A, 10
STM 11, A     ; Q2: What is 5*2?
; ... etc

; Quiz loop
LOAD C, 0     ; Score
LOAD D, 0     ; Question number

quiz_loop:
  ; Display question number
  OUT D
  
  ; Get user answer
  IN B
  
  ; Calculate memory address
  LOAD A, 10
  ADD A, D
  
  ; Load correct answer
  LDM A, A
  
  ; Compare
  CMP B, A
  JNZ wrong
  
  ; Correct!
  ADD C, 1
  
wrong:
  ADD D, 1
  CMP D, 5
  JC quiz_loop
  
; Display final score
OUT C
HALT
```

---

### Option 3: Data Analysis Tool

**Requirements**:
- Read N numbers (user specifies N)
- Store all numbers in memory
- Find minimum value
- Find maximum value
- Calculate sum
- Calculate average
- Output all statistics

**Algorithm Hints**:
```assembly
; Read N
IN A
STM 100, A    ; Store count

; Initialize min/max
LOAD B, 255   ; Min (start at max)
LOAD C, 0     ; Max (start at min)
LOAD D, 0     ; Sum

; Read numbers
; For each number:
;   Store in memory
;   Compare with min/max
;   Add to sum
```

---

## Example Full Solution: Number Guessing Game (Extended)

```assembly
; ==========================================
; PROGRAM: Number Guessing Game (Extended)
; AUTHOR: Solution Key
; DATE: 2025-12-15
; ==========================================

; === SETUP ===
LOAD A, 42     ; Secret number (can be changed)
LOAD B, 0      ; Attempt counter

; === GAME LOOP ===
game_loop:
  IN C         ; Get user's guess
  ADD B, 1     ; Count this attempt
  
  ; Save registers
  PUSH A
  PUSH B
  PUSH C
  
  ; Check if correct
  CMP C, A
  JZ correct
  
  ; Check if too low
  JC too_low
  
  ; Too high
  LOAD D, 72     ; ASCII 'H'
  OUT D
  POP C
  POP B
  POP A
  JMP game_loop
  
too_low:
  LOAD D, 76     ; ASCII 'L'
  OUT D
  POP C
  POP B
  POP A
  JMP game_loop
  
correct:
  ; Clean stack
  POP C
  POP B
  POP A
  
  ; Output attempts
  OUT B
  
  ; Ask to play again
  IN D
  CMP D, 1
  JZ restart
  HALT
  
restart:
  LOAD B, 0     ; Reset attempts
  JMP game_loop

; === MEMORY MAP ===
; A: Secret number (42)
; B: Attempt counter
; C: Current guess
; D: Output message
; Stack: Temporary storage during comparisons
```

---

## Rubric (100 points)

### Functionality (40 points)
- **40**: All features work perfectly, handles edge cases
- **35**: All features work, minor issues
- **30**: Most features work correctly
- **25**: Core functionality works
- **20**: Partial functionality
- **10**: Minimal functionality
- **0**: Doesn't work

### Required Components (30 points)
Each component worth 3 points:
- Memory operations (STM/LDM)
- Stack operations (PUSH/POP)
- Arithmetic operations
- Logic operations
- Comparisons (CMP)
- Conditional jumps
- Loops
- User input (IN)
- User output (OUT)
- Proper HALT

### Code Quality (15 points)
- **15**: Excellent organization, efficient, clear logic
- **12**: Well-organized, good structure
- **9**: Adequate organization
- **6**: Poor organization
- **3**: Very poor organization
- **0**: No organization

### Documentation (10 points)
- **10**: Complete header, comprehensive comments, memory map
- **8**: Good documentation, minor gaps
- **6**: Adequate comments
- **4**: Minimal comments
- **2**: Almost no documentation
- **0**: No documentation

### Testing & Debug (5 points)
- **5**: Thoroughly tested, no bugs
- **4**: Well-tested, minor bugs
- **3**: Some testing, some bugs
- **2**: Minimal testing
- **0**: Not tested

### Bonus Points (up to +20)
- Exceptional creativity: +10
- Additional features: +5
- Outstanding optimization: +5
- Helping classmates: +3
- Early completion: +2

---

## Test Requirements

Students must test with:
1. **Normal cases**: Typical inputs
2. **Edge cases**: 0, 255, boundary values
3. **Error cases**: Invalid inputs (if handling)
4. **Multiple runs**: Verify consistency

**Testing Log Template**:
```
Test 1: [Description]
Input: [Values]
Expected: [Results]
Actual: [Results]
Pass/Fail: [Status]
```

---

## Common Mistakes

### 1. Stack Imbalance
```assembly
PUSH A
PUSH B
POP A          ; Missing one POP!
; Stack corrupted
```

### 2. Infinite Loops
```assembly
loop:
  ; ... code ...
  JMP loop     ; No exit condition!
```

### 3. Memory Overwrites
```assembly
LOAD A, 10
STM 50, A
; ... other code ...
LOAD B, 20
STM 50, B      ; Oops! Overwrote A's value
```

### 4. Wrong Jump Conditions
```assembly
CMP A, 10
JC wrong_label  ; Meant JNC?
```

### 5. Forgetting to Save Registers
```assembly
LOAD A, 42     ; Important value!
; ... lots of code using A ...
; A lost!
```

---

## Grading Efficiency Tips

**For Teachers**:

1. **Quick Functionality Check** (2 min):
   - Run program
   - Test basic features
   - Verify outputs

2. **Component Checklist** (1 min):
   - Scan for memory operations
   - Find stack usage
   - Check loops/conditionals

3. **Code Review** (2 min):
   - Check organization
   - Verify comments
   - Note quality

**Total grading time: ~5 minutes per project**

---

## Student Presentation Guidelines

**Day 5 presentations (3 minutes each)**:
1. Demo program (1.5 min)
2. Explain one interesting part (1 min)
3. Q&A (0.5 min)

**Presentation Rubric** (included in Code Quality):
- Clear demonstration
- Explains design choices
- Answers questions

---

## Extensions

**For students who finish early**:
1. Add difficulty levels
2. Implement high score system
3. Create more sophisticated algorithms
4. Optimize for instruction count
5. Add visual feedback (number patterns)

---

## Learning Outcomes

After this project, students can:
- ✓ Design complete assembly programs
- ✓ Integrate multiple concepts
- ✓ Debug complex issues
- ✓ Document professionally
- ✓ Test thoroughly
- ✓ Present technical work

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-AP-16, 3A-AP-17
**Course LOs**: LO2.1-2.5, LO4.1-4.2

---

*End of Project 2 Specification*
