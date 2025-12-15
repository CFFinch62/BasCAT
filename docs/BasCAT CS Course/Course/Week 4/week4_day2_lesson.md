# Week 4, Day 2: Conditional Jumps

**Topic**: JZ, JNZ, JC, JNC - Making Decisions
**Duration**: 50 minutes
**Learning Objectives**:
- Use conditional jump instructions
- Create branching program logic
- Implement IF-THEN logic in assembly
- Understand labels and program flow

---

## Materials

- Computers with BasCAT
- Homework from Day 1
- Handout: "Conditional Jump Reference"
- Flowchart examples

---

## Lesson Outline

### Warm-Up / CMP Review (7 min)

**Quick Review**:
"Yesterday: CMP sets flags. Today: Use flags to JUMP!"

**Demo the Power**:
```assembly
IN A
CMP A, 18
JC too_young      ; Jump if A < 18
; Code for adults
OUT A
HALT

too_young:
; Code for minors
LOAD A, 0
OUT A
HALT
```

"The program chooses DIFFERENT paths based on input!"

### Direct Instruction: Conditional Jumps (13 min)

**What is a Jump?**

"Normally programs run line-by-line. JUMP says: Go to a different line!"

**Label Syntax**:
```assembly
label_name:
; Code here
```

**Unconditional Jump** (always jumps):
```assembly
JMP label      ; Always go to label
```

**Conditional Jumps** (jump based on flags):

**JZ - Jump if Zero**
```assembly
CMP A, 10
JZ equal       ; Jump if Z flag = 1 (values equal)
; Code if not equal
HALT
equal:
; Code if equal
HALT
```

**JNZ - Jump if Not Zero**
```assembly
CMP A, 10
JNZ not_equal  ; Jump if Z flag = 0 (values different)
; Code if equal
HALT
not_equal:
; Code if not equal
HALT
```

**JC - Jump if Carry**
```assembly
CMP A, 18
JC less_than   ; Jump if C flag = 1 (A < B)
; Code if A >= 18
HALT
less_than:
; Code if A < 18
HALT
```

**JNC - Jump if No Carry**
```assembly
CMP A, 18
JNC greater_equal  ; Jump if C flag = 0 (A >= B)
; Code if A < 18
HALT
greater_equal:
; Code if A >= 18
HALT
```

**Summary Table**:
| Instruction | Jumps When | Use Case |
|-------------|------------|----------|
| JZ | Z = 1 | Values equal |
| JNZ | Z = 0 | Values different |
| JC | C = 1 | Less than |
| JNC | C = 0 | Greater or equal |
| JMP | Always | Unconditional |

**Example: Age Checker**
```assembly
IN A           ; Get age
CMP A, 21
JC under_21    ; If age < 21, jump

; Age >= 21
LOAD A, 1      ; Can drink
OUT A
HALT

under_21:
LOAD A, 0      ; Cannot drink
OUT A
HALT
```

**Flowchart**:
```
[Input age]
    ↓
[age < 21?]
  ↙     ↘
YES      NO
 ↓        ↓
[0]      [1]
 ↓        ↓
[Output] [Output]
```

### Guided Practice: Simple Conditionals (15 min)

**Challenge 1: Even/Odd Detector** (5 min)

"Check if number is even (bit 0 = 0)"
```assembly
IN A
AND A, 1       ; Check bit 0
JZ even        ; If 0, it's even

; Odd number
LOAD A, 1
OUT A
HALT

even:
LOAD A, 0
OUT A
HALT
```

**Challenge 2: Range Validator** (5 min)

"Check if input is in valid range (0-100)"
```assembly
IN A
CMP A, 0
JC invalid     ; If < 0, invalid

CMP A, 100
JNC valid      ; If >= 100, valid (wait, we want <=!)
JMP valid      ; This needs fixing...

invalid:
LOAD A, 0
OUT A
HALT

valid:
LOAD A, 1
OUT A
HALT
```

*Note: This is intentionally buggy to teach debugging!*

**Challenge 3: Max Finder** (5 min)

"Find larger of two inputs"
```assembly
IN A
IN B
CMP A, B
JNC a_larger   ; If A >= B, A is larger

; B is larger
OUT B
HALT

a_larger:
OUT A
HALT
```

### Independent Practice: Decision Programs (10 min)

**Level 1**: Simple Threshold
```assembly
; Output 1 if input > 50, else 0
IN A
CMP A, 50
JNC above      ; If >= 50 (wait, we want >, need to think...)

; Below or equal
LOAD A, 0
OUT A
HALT

above:
LOAD A, 1
OUT A
HALT
```

**Level 2**: Grade Classifier
```assembly
; A grade: >= 90
; B grade: >= 80
; C grade: < 80
IN A

CMP A, 90
JNC grade_a

CMP A, 80
JNC grade_b

; Grade C
LOAD A, 67     ; ASCII 'C'
OUT A
HALT

grade_a:
LOAD A, 65     ; ASCII 'A'
OUT A
HALT

grade_b:
LOAD A, 66     ; ASCII 'B'
OUT A
HALT
```

**Level 3**: Absolute Difference
```assembly
; Output |A - B|
IN A
IN B
CMP A, B
JNC a_bigger

; B >= A
SUB B, A
OUT B
HALT

a_bigger:
SUB A, B
OUT A
HALT
```

### Class Discussion: Program Flow (5 min)

**Linear vs Branching**:

**Before**:
```
Line 1 → Line 2 → Line 3 → HALT
```

**Now**:
```
Line 1 → Line 2 → Decision
                    ↙     ↘
             Path A      Path B
                ↓          ↓
              HALT       HALT
```

**Key Insights**:
- Programs can take different paths
- Flags determine which path
- Labels mark destinations
- Every path should reach HALT

**Common Patterns**:
1. IF-THEN: Jump to special code, or skip it
2. IF-ELSE: Jump to one of two code blocks
3. Cascade: Multiple comparisons in sequence

---

## Closure / Exit Ticket (5 min)

Write code:
"If input >= 100, output 1. Otherwise output 0."

**Expected**:
```assembly
IN A
CMP A, 100
JNC big
LOAD A, 0
OUT A
HALT
big:
LOAD A, 1
OUT A
HALT
```

**Preview Tomorrow**: "LOOPS! Repeat code multiple times with jumps!"

---

## Homework

**Program 1**: Password Checker (simplified)
```assembly
; If input == 42, output 1 (correct)
; Else output 0 (wrong)
IN A
CMP A, 42
JZ correct
LOAD A, 0
OUT A
HALT
correct:
LOAD A, 1
OUT A
HALT
```

**Program 2**: Sign Detector
```assembly
; If bit 7 = 1, number is "negative" (>=128)
; Output 1 for negative, 0 for positive
IN A
AND A, 128
JZ positive
LOAD A, 1
OUT A
HALT
positive:
LOAD A, 0
OUT A
HALT
```

**Challenge**: Three-way decision - classify input as low (<33), medium (33-66), or high (>66). Output 1, 2, or 3.

**Due**: Next class

---

## Assessment

**Formative**:
- Conditional logic understanding
- Label usage
- Program flow design
- Debugging branching code

**Success Criteria**:
- Can use JZ/JNZ correctly
- Can use JC/JNC correctly
- Can create branching logic
- Understands program flow changes

---

## Differentiation

**Struggling**: IF-THEN only (no ELSE), simple conditions
**Advanced**: Multiple conditions, nested decisions, optimization
**ELL**: Flowcharts, visual program flow, code templates

---

## Teacher Notes

**Common Errors**:
- Forgetting HALT in both paths
- Wrong jump instruction (JC vs JNC)
- Label typos
- Infinite loops (preview tomorrow)

**Time Savers**:
- Have flowchart templates
- Pre-drawn decision trees
- Working examples ready

---

## Standards Alignment

**CSTA**: 3A-AP-15, 3A-AP-16
**LO**: LO2.1, LO4.1

---

*End of Week 4, Day 2 Lesson Plan*
