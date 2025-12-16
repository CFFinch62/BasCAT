# Week 11: Advanced Assembly & Optimization

**Theme**: Performance, Optimization, and Advanced Techniques
**Duration**: 5 days (50 minutes each)

---

## Week 11, Day 1: Code Optimization Techniques

**Topic**: Writing Efficient Assembly Code
**Duration**: 50 minutes
**Learning Objectives**:
- Identify optimization opportunities
- Reduce instruction count
- Minimize memory access
- Improve algorithm efficiency

### Key Concepts

**Why Optimize?**
- Faster execution
- Less memory usage
- Better resource utilization
- Real-world performance matters

**Optimization Strategies**:

**1. Register Reuse**
```assembly
; Inefficient
LOAD A, 10
STM 100, A
LDM A, 100     ; Unnecessary memory access!

; Optimized
LOAD A, 10     ; A already has value
```

**2. Instruction Reduction**
```assembly
; Inefficient (5 instructions)
LOAD A, 5
ADD A, 5
ADD A, 5
ADD A, 5
ADD A, 5       ; A = 25

; Optimized (3 instructions)
LOAD A, 5
MOV B, A       ; B = 5
ADD A, A       ; A = 10
ADD A, A       ; A = 20
ADD A, B       ; A = 25
```

**3. Loop Optimization**
```assembly
; Inefficient - recalculates constant
loop:
  LOAD B, 10
  LOAD C, 5
  ADD B, C     ; Constant calculation inside loop!
  ; ... use B ...
  SUB D, 1
  JNZ loop

; Optimized - calculate once
LOAD B, 10
LOAD C, 5
ADD B, C       ; Calculate before loop
loop:
  ; ... use B (already 15) ...
  SUB D, 1
  JNZ loop
```

**4. Memory Access Reduction**
```assembly
; Inefficient
LOAD A, 5
STM 100, A
; ... other code ...
LDM B, 100     ; Could have kept in register

; Optimized
LOAD A, 5
; ... other code ...
MOV B, A       ; No memory access needed
```

### Lab Exercise

**Challenge**: Optimize given program
- Count original instructions
- Identify inefficiencies
- Rewrite optimized version
- Measure improvement

---

## Week 11, Day 2: Debugging Assembly Programs

**Topic**: Systematic Debugging Strategies
**Duration**: 50 minutes
**Learning Objectives**:
- Use BasCAT debugging features
- Trace program execution
- Identify common bugs
- Fix logical errors

### Key Concepts

**Debugging Tools in BasCAT**:
1. **Step Mode**: Execute one instruction at a time
2. **Breakpoints**: Pause at specific lines
3. **Register Watch**: Monitor register values
4. **Memory View**: Check memory contents
5. **Stack View**: Verify stack operations

**Common Bug Categories**:

**1. Register Mix-ups**
```assembly
LOAD A, 10
LOAD B, 20
ADD B, A       ; Oops! Wanted result in A
OUT A          ; Outputs wrong value
```

**2. Off-by-One Errors**
```assembly
; Want loop 10 times
LOAD A, 0
loop:
  OUT A
  ADD A, 1
  CMP A, 10
  JC loop        ; Runs 10 times (0-9) - correct!
  
; But if you want 1-10:
LOAD A, 1
loop:
  OUT A
  ADD A, 1
  CMP A, 11      ; Need 11 here!
  JC loop
```

**3. Stack Imbalance**
```assembly
PUSH A
PUSH B
POP A          ; Only one POP!
; Stack corrupted!
```

**4. Missing HALT**
```assembly
LOAD A, 10
OUT A
; Missing HALT - program runs into garbage!
```

**5. Wrong Jump Condition**
```assembly
CMP A, 10
JC label       ; Jumps if A < 10
; Did you mean JNC (A >= 10)?
```

### Debugging Methodology

**Step-by-Step Process**:
1. **Reproduce**: Make bug happen consistently
2. **Isolate**: Find which section has bug
3. **Trace**: Step through suspicious code
4. **Check**: Verify register/memory values
5. **Hypothesize**: What's wrong?
6. **Fix**: Make minimal change
7. **Test**: Verify fix works

### Lab Exercise

Students debug intentionally buggy programs:
- Logic errors
- Stack problems
- Jump mistakes
- Memory issues

---

## Week 11, Day 3: Advanced Data Structures

**Topic**: Implementing Complex Structures in Assembly
**Duration**: 50 minutes
**Learning Objectives**:
- Create linked structures
- Implement queues
- Build hash tables (simplified)
- Manage dynamic data

### Key Concepts

**1. Array Manipulation**
```assembly
; Store array at addresses 10-19
LOAD A, 0      ; Counter
LOAD B, 10     ; Base address
store_loop:
  STM B, A     ; Store value at address
  ADD B, 1     ; Next address
  ADD A, 1     ; Next value
  CMP A, 10
  JC store_loop
```

**2. Stack as Queue (FIFO simulation)**
```assembly
; Circular buffer in memory
; Addresses 50-59 (10 elements)
; Head pointer at 60
; Tail pointer at 61

; Enqueue
LDM A, 61      ; Get tail
STM A, B       ; Store value at tail
ADD A, 1
CMP A, 60      ; Wrap at 60?
JNZ no_wrap
LOAD A, 50     ; Reset to start
no_wrap:
STM 61, A      ; Update tail
```

**3. Simple Lookup Table**
```assembly
; Powers of 2 lookup
; Address 100: 1
; Address 101: 2
; Address 102: 4
; Address 103: 8
; etc.

; Get 2^N
LOAD A, N
ADD A, 100     ; Calculate address
LDM B, A       ; Load power of 2
```

---

## Week 11, Day 4: Assembly Best Practices

**Topic**: Professional Assembly Programming
**Duration**: 50 minutes
**Learning Objectives**:
- Write maintainable code
- Document effectively
- Follow conventions
- Structure programs well

### Key Concepts

**Code Organization**:
```assembly
; ==========================================
; PROGRAM: Grade Calculator
; AUTHOR: Student Name
; DATE: 2024-12-15
; PURPOSE: Calculate average of N grades
; ==========================================

; === CONSTANTS ===
; None

; === VARIABLES ===
; A: Running sum
; B: Count
; C: Current grade

; === MEMORY MAP ===
; 10-19: Grade storage
; 20: Final average

; === MAIN PROGRAM ===
LOAD A, 0      ; Initialize sum
LOAD B, 0      ; Initialize count

; === INPUT SECTION ===
input_loop:
  IN C
  CMP C, 0     ; 0 = done
  JZ calculate
  ADD A, C     ; Add to sum
  ADD B, 1     ; Increment count
  JMP input_loop

; === CALCULATION SECTION ===
calculate:
  ; Divide A by B (simplified)
  ; ... division code ...

; === OUTPUT SECTION ===
output:
  OUT A
  HALT
```

**Commenting Standards**:
```assembly
; Good comments explain WHY, not WHAT
LOAD A, 10     ; Bad: Load 10 into A
LOAD A, 10     ; Good: Set loop counter to 10
```

**Naming Conventions**:
```assembly
; Use descriptive labels
loop:          ; Bad - generic
count_loop:    ; Good - specific
calc_average:  ; Good - describes purpose
```

---

## Week 11, Day 5: Lab Day - Optimization Challenge

**Topic**: Performance Competition
**Duration**: 50 minutes
**Learning Objectives**:
- Apply optimization techniques
- Measure performance
- Compare approaches
- Present solutions

### Lab Project

**The Challenge**: "Fastest Factorial"

Write assembly program to calculate factorial:
- Input: N (1-10)
- Output: N!
- Constraint: Minimize instruction count

**Scoring**:
- Correctness: 30 points
- Instruction count: 20 points (fewer = better)
- Code quality: 20 points
- Documentation: 10 points
- Creativity: 10 points
- Bonus: +10 for sub-50 instructions

**Example Approaches**:

**Approach 1: Repeated Addition** (slow)
```assembly
; Multiply by repeated addition
; Result in A, multiply by B
; Using C as counter
multiply:
  LOAD C, 0    ; Result
  LOAD D, 0    ; Counter
mult_loop:
  ADD C, A
  ADD D, 1
  CMP D, B
  JC mult_loop
  MOV A, C     ; Move result
  RETURN
```

**Approach 2: Lookup Table** (fast but limited)
```assembly
; Pre-calculated factorials in memory
; 1! at address 100 = 1
; 2! at address 101 = 2
; 3! at address 102 = 6
; etc.
IN A           ; Get N
ADD A, 99      ; Calculate address
LDM B, A       ; Load factorial
OUT B
HALT
```

**Approach 3: Optimized Loop** (balanced)

### Competition Rules
- 45 minutes to code
- Test with values 1-10
- Must output correct results
- Instruction count measured in compiled code
- Winner gets bonus points

---

## Week 11 Assessment

**Quiz** (25 pts):
1. Identify 3 optimization opportunities (9)
2. Debug given code (8)
3. Design data structure (8)

**Performance Analysis** (25 pts):
- Analyze two programs
- Count instructions
- Suggest optimizations
- Estimate improvement

---

## Week Reflection

**Key Skills Developed**:
- Optimization thinking
- Systematic debugging
- Advanced data structures
- Professional coding practices

**Next Week**: "Real-World Computing Systems"

---

## Standards Alignment

**CSTA**: 3A-AP-17 (Decompose), 3A-AP-21 (Evaluate)
**LO**: LO2.5, LO4.2, LO4.3

---

*End of Week 11 Complete Lesson Series*
