# Project 1: Assembly Calculator

**Week**: 3 (Logic Operations)
**Duration**: 2 class periods
**Points**: 50
**Type**: Individual project

---

## Project Overview

Students will create a calculator program in assembly that performs multiple operations on user-provided numbers using arithmetic and logic operations learned in Weeks 1-3.

---

## Learning Objectives

- LO2.1: Write functional assembly programs
- LO2.2: Use registers effectively
- LO4.1: Decompose problems into steps
- LO4.2: Implement algorithms efficiently

---

## Requirements

### Core Features (Required)

**Must Include**:
1. **User Input**: Read two numbers from user
2. **Multiple Operations**: 
   - Addition
   - Subtraction
   - Bitwise AND
   - Bitwise OR
3. **Output**: Display result of each operation
4. **Code Quality**:
   - Comments explaining each section
   - Organized structure
   - Proper use of registers
   - HALT statement

### Bonus Features (Optional)

- XOR operation (+3 points)
- NOT operation on each input (+3 points)
- Display results in specific format (+2 points)
- Input validation (check for zero) (+2 points)

---

## Specifications

### Input Format
- Program reads exactly 2 numbers via IN instruction
- Numbers can be 0-255 (8-bit values)
- No input validation required (bonus if implemented)

### Output Format
- Output each operation result on separate line
- Use OUT instruction for each result
- Output order: Addition, Subtraction, AND, OR (then bonuses if implemented)

### Program Structure
```assembly
; ==========================================
; PROGRAM: Basic Calculator
; AUTHOR: [Student Name]
; DATE: [Date]
; ==========================================

; === INPUT SECTION ===
; Read two numbers

; === OPERATIONS SECTION ===
; Perform calculations

; === OUTPUT SECTION ===
; Display results

HALT
```

---

## Starter Code Template

```assembly
; ==========================================
; PROGRAM: Basic Calculator
; AUTHOR: _____________________
; DATE: _____________________
; ==========================================

; === INPUT SECTION ===
; TODO: Read first number into register A
; TODO: Read second number into register B

; === OPERATIONS SECTION ===

; Addition
; TODO: Calculate A + B, store in C

; Subtraction
; TODO: Calculate A - B, store in C

; AND Operation
; TODO: Calculate A AND B, store in C

; OR Operation
; TODO: Calculate A OR B, store in C

; === OUTPUT SECTION ===
; TODO: Output each result

HALT

; === MEMORY MAP ===
; A: First input number
; B: Second input number
; C: Result register
; D: Temporary storage (if needed)
```

---

## Example Solution

```assembly
; ==========================================
; PROGRAM: Basic Calculator
; AUTHOR: Solution Key
; DATE: 2025-12-15
; ==========================================

; === INPUT SECTION ===
IN A           ; Read first number
IN B           ; Read second number

; Save inputs for later operations
PUSH A
PUSH B

; === OPERATIONS SECTION ===

; Addition
POP B          ; Restore B
POP A          ; Restore A
PUSH A         ; Save again
PUSH B         ; Save again
MOV C, A       ; Copy A to C
ADD C, B       ; C = A + B
OUT C          ; Output sum

; Subtraction
POP B          ; Restore B
POP A          ; Restore A
PUSH A         ; Save again
PUSH B         ; Save again
MOV C, A       ; Copy A to C
SUB C, B       ; C = A - B
OUT C          ; Output difference

; AND Operation
POP B          ; Restore B
POP A          ; Restore A
PUSH A         ; Save again
PUSH B         ; Save again
MOV C, A       ; Copy A to C
AND C, B       ; C = A AND B
OUT C          ; Output AND result

; OR Operation
POP B          ; Restore B
POP A          ; Restore A
MOV C, A       ; Copy A to C
OR C, B        ; C = A OR B
OUT C          ; Output OR result

HALT

; === MEMORY MAP ===
; A: First input number
; B: Second input number
; C: Result register
; Stack: Used to preserve A and B between operations
```

### Solution with Bonuses

```assembly
; ==========================================
; PROGRAM: Advanced Calculator
; AUTHOR: Solution Key (with bonuses)
; DATE: 2025-12-15
; ==========================================

; === INPUT SECTION ===
IN A           ; Read first number
IN B           ; Read second number

; Save inputs
PUSH A
PUSH B

; === OPERATIONS SECTION ===

; Addition
POP B
POP A
PUSH A
PUSH B
MOV C, A
ADD C, B
OUT C

; Subtraction
POP B
POP A
PUSH A
PUSH B
MOV C, A
SUB C, B
OUT C

; AND Operation
POP B
POP A
PUSH A
PUSH B
MOV C, A
AND C, B
OUT C

; OR Operation
POP B
POP A
PUSH A
PUSH B
MOV C, A
OR C, B
OUT C

; XOR Operation (BONUS)
POP B
POP A
PUSH A
PUSH B
MOV C, A
XOR C, B
OUT C

; NOT Operations (BONUS)
POP B
POP A
MOV C, A
NOT C
OUT C          ; NOT of first input

MOV C, B
NOT C
OUT C          ; NOT of second input

HALT
```

---

## Test Cases

### Test Case 1: Basic Values
**Input**: 15, 10
**Expected Output**:
- Addition: 25
- Subtraction: 5
- AND: 10 (00001111 AND 00001010 = 00001010)
- OR: 15 (00001111 OR 00001010 = 00001111)

### Test Case 2: Zero
**Input**: 0, 5
**Expected Output**:
- Addition: 5
- Subtraction: 251 (underflow: 0 - 5 wraps to 251)
- AND: 0
- OR: 5

### Test Case 3: Same Values
**Input**: 7, 7
**Expected Output**:
- Addition: 14
- Subtraction: 0
- AND: 7
- OR: 7

### Test Case 4: Maximum Values
**Input**: 255, 255
**Expected Output**:
- Addition: 254 (overflow: 255 + 255 = 510, wraps to 254)
- Subtraction: 0
- AND: 255
- OR: 255

### Test Case 5: Powers of 2
**Input**: 128, 64
**Expected Output**:
- Addition: 192
- Subtraction: 64
- AND: 0 (10000000 AND 01000000 = 00000000)
- OR: 192 (10000000 OR 01000000 = 11000000)

---

## Rubric (50 points total)

### Functionality (25 points)
- **25**: All operations work correctly, handles all test cases
- **20**: All operations implemented, minor errors in 1-2 test cases
- **15**: 3 operations work correctly
- **10**: 2 operations work correctly
- **5**: 1 operation works correctly
- **0**: Program doesn't compile or run

### Input/Output (10 points)
- **10**: Correctly reads 2 inputs, outputs all 4 results in order
- **8**: Correct I/O but minor formatting issues
- **6**: Missing one output or input issue
- **4**: Multiple I/O problems
- **0**: I/O doesn't work

### Code Organization (8 points)
- **8**: Clear sections, logical flow, easy to follow
- **6**: Organized but could be clearer
- **4**: Somewhat disorganized
- **2**: Very disorganized
- **0**: No organization

### Comments & Documentation (7 points)
- **7**: Comprehensive comments, header complete, explains logic
- **5**: Good comments but missing some explanations
- **3**: Minimal comments
- **1**: Almost no comments
- **0**: No comments

### Bonus Points (up to +10)
- XOR operation: +3
- NOT operations: +3
- Formatted output: +2
- Input validation: +2

### Deductions
- Missing HALT: -5
- Syntax errors (if runs): -2 each
- Incorrect register usage: -3
- Memory leaks (stack imbalance): -5

---

## Common Mistakes & Troubleshooting

### Mistake 1: Overwriting Input Values
**Problem**:
```assembly
IN A
IN B
ADD A, B       ; A now contains sum, lost original value!
SUB A, B       ; Wrong! A no longer has original value
```

**Solution**: Use stack or additional registers
```assembly
IN A
IN B
PUSH A         ; Save A
PUSH B         ; Save B
; Restore before each operation
```

### Mistake 2: Wrong Output Order
**Problem**: Outputs OR before AND

**Solution**: Follow specification order exactly

### Mistake 3: Forgetting HALT
**Problem**: Program continues into garbage memory

**Solution**: Always end with HALT

### Mistake 4: Stack Imbalance
**Problem**:
```assembly
PUSH A
PUSH B
POP A          ; Only one POP!
```

**Solution**: Match every PUSH with POP

### Mistake 5: Underflow Confusion
**Problem**: Student doesn't understand why 5 - 10 = 251

**Explanation**: Unsigned 8-bit arithmetic wraps around

---

## Grading Checklist

**For Teachers**:

□ Program compiles without errors
□ Addition works correctly
□ Subtraction works correctly (including underflow)
□ AND operation works correctly
□ OR operation works correctly
□ Reads 2 inputs properly
□ Outputs 4 results
□ Has HALT statement
□ Code is organized
□ Has meaningful comments
□ Header filled out
□ Bonus features (if present)

**Quick Grade Estimate**:
- All working + good code = 45-50
- All working + poor code = 35-40
- Most working = 30-35
- Some working = 20-30
- Barely working = 10-20

---

## Extensions for Advanced Students

1. **Menu System**: Let user choose which operation to perform
2. **Multiple Numbers**: Calculate on 3 or more inputs
3. **Chained Operations**: (A + B) AND (A - B)
4. **Result Storage**: Save results in memory, display all at end
5. **Binary Display**: Show inputs and outputs in binary format

---

## Student Submission Checklist

**Before Submitting**:
□ I tested with at least 3 different inputs
□ All required operations work
□ Program has HALT
□ Code has comments
□ Header is filled out
□ I saved as `project1_calculator_[LastName].asm`
□ Program outputs results in correct order
□ I included bonus features (if attempted)

---

## Time Estimates

**Planning**: 10 minutes
**Coding**: 30-40 minutes
**Testing**: 10-15 minutes
**Documentation**: 5-10 minutes
**Total**: ~1 class period (plus homework time)

---

## Learning Outcomes

After completing this project, students can:
- ✓ Combine multiple assembly operations
- ✓ Use registers effectively
- ✓ Preserve values during calculations
- ✓ Structure programs logically
- ✓ Test and debug assembly code
- ✓ Document code professionally

---

## Standards Alignment

**CSTA**: 3A-AP-13 (Create prototypes)
**Course LOs**: LO2.1, LO2.2, LO4.1, LO4.2

---

*End of Project 1 Specification*
