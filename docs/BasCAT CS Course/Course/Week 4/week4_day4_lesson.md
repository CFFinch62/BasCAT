# Week 4, Day 4: Complex Control Flow

**Topic**: Nested Loops and Combined Conditionals
**Duration**: 50 minutes
**Learning Objectives**:
- Combine loops with conditional logic
- Create nested control structures
- Design complex algorithms
- Optimize control flow

---

## Materials

- Computers with BasCAT
- Handout: "Control Flow Patterns"

---

## Lesson Outline

### Warm-Up (7 min)

**Review**: Conditionals + Loops separately
**Today**: Combine them for powerful programs!

### Direct Instruction: Combined Structures (12 min)

**Pattern 1: Loop with Conditional Inside**
```assembly
; Output only even numbers 0-10
LOAD A, 0
loop:
  MOV B, A
  AND B, 1       ; Check if even
  JNZ skip       ; If odd, skip output
  OUT A          ; Output even
skip:
  ADD A, 1
  CMP A, 11
  JC loop
HALT
```

**Pattern 2: Conditional with Loop Inside**
```assembly
; If input > 5, count to 10; else count to 5
IN A
CMP A, 5
JNC big_count

; Small count
LOAD B, 5
JMP do_count

big_count:
LOAD B, 10

do_count:
LOAD A, 0
count_loop:
  OUT A
  ADD A, 1
  CMP A, B
  JC count_loop
HALT
```

**Pattern 3: Loop with Exit Condition**
```assembly
; Loop until user inputs 0
loop:
  IN A
  CMP A, 0
  JZ done
  OUT A
  JMP loop
done:
HALT
```

**Pattern 4: Accumulator with Threshold**
```assembly
; Sum inputs until total > 100
LOAD A, 0      ; Sum
sum_loop:
  IN B
  ADD A, B
  CMP A, 100
  JC sum_loop
OUT A
HALT
```

### Guided Practice (15 min)

**Challenge 1**: Prime Checker (simplified)
Check if input is 2, 3, 5, or 7

**Challenge 2**: Range Summer
Sum all numbers between user input A and B

**Challenge 3**: Conditional Counter
Count inputs until seeing specific value

### Independent Practice (10 min)

**Level 1**: Filtered Output
Loop 1-20, output only multiples of 3

**Level 2**: Search
Read numbers until finding target value

**Level 3**: Mini-Game
Guess the number (compare, give hints, loop)

### Class Discussion (6 min)

**Algorithm Design**:
- Break problem into steps
- Identify loops needed
- Identify decisions needed
- Combine structures

**Debugging Strategies**:
- Test one structure at a time
- Use Step mode extensively
- Check counter updates
- Verify all paths reach HALT

---

## Closure (5 min)

**Exit Ticket**: Describe algorithm for "find largest of N numbers"

**Preview**: "Lab Day tomorrow - build complete program!"

---

## Homework

**Program 1**: Factorial with loop
**Program 2**: Average calculator (sum N inputs, divide)
**Challenge**: Number guessing game with limited tries

**Due**: Tomorrow

---

## Standards Alignment
**CSTA**: 3A-AP-16, 3A-AP-17
**LO**: LO4.1, LO4.2

---

*End of Week 4, Day 4 Lesson Plan*
