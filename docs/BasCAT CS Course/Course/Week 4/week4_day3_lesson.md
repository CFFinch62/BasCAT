# Week 4, Day 3: Loops with Jumps

**Topic**: Creating Loops - Repeating Code
**Duration**: 50 minutes
**Learning Objectives**:
- Create loops using JMP and conditional jumps
- Implement counters and loop control
- Understand infinite vs controlled loops
- Build iterative algorithms

---

## Materials

- Computers with BasCAT
- Handout: "Loop Patterns Guide"
- Flowchart templates

---

## Lesson Outline

### Warm-Up (7 min)

**The Repetition Problem**:
"What if we want to do something 10 times? Write code 10 times?"
```assembly
OUT A
OUT A
OUT A
... (8 more times)
```
"There's a better way: LOOPS!"

### Direct Instruction: Loop Basics (12 min)

**Infinite Loop** (simplest):
```assembly
loop:
  OUT A
  JMP loop     ; Jump back to loop
; Never reaches here!
```

**Controlled Loop** (with counter):
```assembly
LOAD A, 0      ; Counter
loop:
  OUT A
  ADD A, 1     ; Increment
  CMP A, 10
  JC loop      ; If < 10, loop again
HALT
```

**Loop Structure**:
1. Initialize counter
2. Loop body (work)
3. Update counter
4. Test condition
5. Jump back or exit

**Example: Countdown**:
```assembly
LOAD A, 10
countdown:
  OUT A
  SUB A, 1
  JNZ countdown    ; If not zero, continue
HALT
```

**Loop Variables**:
- Counter: Tracks iterations
- Limit: When to stop
- Step: How much to change per loop

### Guided Practice (15 min)

**Challenge 1: Count to N**
```assembly
; Count from 0 to user input
IN B           ; Limit
LOAD A, 0      ; Counter
loop:
  OUT A
  ADD A, 1
  CMP A, B
  JNZ loop
HALT
```

**Challenge 2: Multiplication by Addition**
```assembly
; Multiply A * B using loop
IN A           ; Multiplicand
IN B           ; Multiplier
LOAD C, 0      ; Result
LOAD D, 0      ; Counter
mult_loop:
  ADD C, A
  ADD D, 1
  CMP D, B
  JC mult_loop
OUT C
HALT
```

**Challenge 3: Sum of Numbers**
```assembly
; Sum 1 + 2 + 3 + ... + N
IN B           ; N
LOAD A, 0      ; Sum
LOAD C, 1      ; Counter
sum_loop:
  ADD A, C
  ADD C, 1
  CMP C, B
  JC sum_loop
  JZ sum_loop  ; Include N itself
OUT A
HALT
```

### Independent Practice (10 min)

**Level 1**: Powers of 2
Output 1, 2, 4, 8, 16, 32, 64, 128

**Level 2**: Factorial (simplified)
Calculate N! = 1×2×3×...×N

**Level 3**: Pattern Generator
Create repeating bit pattern with loop

### Class Discussion (6 min)

**Loop vs Linear**:
- Linear: Fixed actions
- Loop: Variable repetitions
- Loops enable: Counting, accumulation, patterns

**Common Loop Bugs**:
1. Off-by-one errors
2. Infinite loops
3. Wrong comparison
4. Forgetting to update counter

---

## Closure / Exit Ticket (5 min)

Write loop that outputs 5 four times.

**Preview**: "Tomorrow: Combining loops and conditionals!"

---

## Homework

**Program 1**: Even Numbers
Loop outputting 0, 2, 4, 6, 8, 10

**Program 2**: User-Controlled Repeat
Read value, output it N times (read N from user)

**Challenge**: Fibonacci sequence (5 numbers)

**Due**: Next class

---

## Standards Alignment
**CSTA**: 3A-AP-15
**LO**: LO2.1, LO4.2

---

*End of Week 4, Day 3 Lesson Plan*
