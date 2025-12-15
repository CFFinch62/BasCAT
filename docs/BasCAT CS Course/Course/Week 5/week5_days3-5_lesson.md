# Week 5, Day 3: Subroutines Introduction

**Topic**: Creating and Calling Subroutines
**Duration**: 50 minutes
**Learning Objectives**:
- Understand subroutine concept
- Use labels for code organization
- Pass data via registers
- Return from subroutines with JMP

---

## Overview

**Subroutines** = reusable code blocks
Students learn to organize code into functions (simplified - no CALL/RET yet in BasCAT)

**Pattern**:
```assembly
; Main program
LOAD A, 10
JMP subroutine
return_point:
; Continue...

subroutine:
  ; Do work
  JMP return_point
```

---

# Week 5, Day 4: Advanced Stack Patterns

**Topic**: Complex Stack Applications
**Duration**: 50 minutes
**Learning Objectives**:
- Implement expression evaluation
- Create nested data structures
- Use stack for temporary storage
- Optimize stack usage

---

## Overview

**Applications**:
1. Expression evaluation (postfix)
2. Backtracking algorithms
3. State preservation
4. Nested function calls

**Example - RPN Calculator**:
```assembly
; Read: 5 3 + (means 5+3)
IN A           ; 5
PUSH A
IN A           ; 3
PUSH A
; Operator: +
POP B          ; 3
POP A          ; 5
ADD A, B
OUT A          ; 8
HALT
```

---

# Week 5, Day 5: Lab Day - Stack Application

**Topic**: Week 5 Capstone Project
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all stack concepts
- Create complete stack-based program
- Demonstrate data structure mastery

---

## Lab Project Options

**Option 1: Reverse Polish Notation Calculator**
- Read operands and operators
- Use stack for evaluation
- Support +, -, operations
- Output results

**Option 2: Data Reverser/Processor**
- Read variable number of inputs
- Store on stack
- Process in reverse order
- Apply transformations

**Option 3: Multi-Level Undo System**
- Simulate state changes
- Push states on stack
- Pop to undo
- Demonstrate LIFO

**Option 4: Stack-Based Sorting** (simplified)
- Read numbers
- Use stack to organize
- Output in different order
- Demonstrate algorithm

---

## Requirements (All Projects)

- Uses PUSH and POP correctly
- Implements loop with stack
- Handles variable-size data
- Well-documented code
- Working demonstration

---

## Rubric (50 points)

**Stack Usage (20 pts)**:
- Correct PUSH/POP
- Proper LIFO order
- Balanced operations

**Functionality (15 pts)**:
- Program works
- Handles edge cases
- Multiple iterations

**Code Quality (10 pts)**:
- Organization
- Comments
- Efficiency

**Documentation (5 pts)**:
- Algorithm explained
- Stack states documented

**Bonus (+10 pts)**:
- Complex features
- Multiple data types
- Error handling
- Optimization

---

## Week 5 Quiz (if time)

**Sample Questions** (25 pts):
1. What does PUSH do? (3)
2. What does LIFO mean? (2)
3. Write code to save A, B, restore in reverse (6)
4. When to use stack vs memory? (4)
5. Debug stack code (5)
6. Trace stack state through operations (5)

---

## Closure

**Next Week Preview**: "Final assembly week - putting EVERYTHING together!"

---

## Standards Alignment
**CSTA**: 3A-AP-13, 3A-AP-16, 3A-DA-10
**LO**: LO2.1, LO4.1, LO4.4

---

*End of Week 5 Complete Lesson Series*
