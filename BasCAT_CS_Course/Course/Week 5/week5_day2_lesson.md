# Week 5, Day 2: Stack with Loops

**Topic**: Using Stack in Iterative Algorithms
**Duration**: 50 minutes
**Learning Objectives**:
- Combine stack operations with loops
- Implement variable-size data storage
- Create stack-based algorithms
- Manage dynamic data structures

---

## Materials

- Computers with BasCAT
- Homework from Day 1
- Handout: "Stack Loop Patterns"

---

## Lesson Outline

### Warm-Up (7 min)

**Review**: PUSH/POP basics
**Today**: "Use stack to handle unknown amounts of data!"

**Demo**:
```assembly
; Reverse N numbers (N from user)
IN B           ; How many numbers?
LOAD C, 0      ; Counter

push_loop:
  IN A
  PUSH A
  ADD C, 1
  CMP C, B
  JC push_loop

; Now pop all
pop_loop:
  POP A
  OUT A
  SUB C, 1
  JNZ pop_loop
HALT
```

### Direct Instruction (12 min)

**Pattern 1: Accumulate with Stack**
```assembly
; Sum unknown count of numbers (end with 0)
LOAD B, 0      ; Sum
LOAD C, 0      ; Count

input_loop:
  IN A
  CMP A, 0
  JZ done_input
  PUSH A
  ADD C, 1
  JMP input_loop

done_input:
  CMP C, 0
  JZ finished

sum_loop:
  POP A
  ADD B, A
  SUB C, 1
  JNZ sum_loop

finished:
  OUT B
  HALT
```

**Pattern 2: Stack as Buffer**
```assembly
; Store values, process later
LOAD C, 0

; Collect
collect:
  IN A
  CMP A, 255     ; Sentinel
  JZ process
  PUSH A
  ADD C, 1
  JMP collect

; Process
process:
  CMP C, 0
  JZ done
  POP A
  ; Do something with A
  OUT A
  SUB C, 1
  JMP process

done:
  HALT
```

**Pattern 3: Nested Loops with Stack**
Preserve outer loop counter while running inner loop

### Guided Practice (15 min)

**Challenge 1**: Read numbers until 0, output in reverse

**Challenge 2**: Find maximum from N numbers using stack

**Challenge 3**: Stack-based palindrome checker (simplified)

### Independent Practice (10 min)

**Level 1**: Reverse array of user-specified size
**Level 2**: Stack calculator (RPN basics)
**Level 3**: Nested data processing

### Class Discussion (6 min)

**Stack Benefits**:
- Don't need to know size in advance
- Automatic memory management
- Natural for reversing
- Enables recursion (preview)

**Stack vs Array**:
- Stack: LIFO, automatic
- Array: Random access, manual

---

## Closure (5 min)

**Exit Ticket**: Write loop that pushes 1-10, then pops all

**Preview**: "Tomorrow: Subroutines and procedures using stack!"

---

## Homework

**Program 1**: Variable-size reversal (user chooses how many numbers)
**Program 2**: Stack-based filtering (push only even numbers)
**Challenge**: Min/max finder using stack

**Due**: Next class

---

## Standards Alignment
**CSTA**: 3A-AP-17, 3A-DA-10
**LO**: LO2.1, LO4.1, LO4.4

---

*End of Week 5, Day 2 Lesson Plan*
