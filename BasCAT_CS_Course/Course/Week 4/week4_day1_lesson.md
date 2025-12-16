# Week 4, Day 1: Comparison and Flags

**Topic**: The CMP Instruction and Understanding Status Flags
**Duration**: 50 minutes
**Learning Objectives**:
- Use CMP instruction to compare values
- Understand how CMP sets flags
- Read and interpret status flags
- Prepare for conditional jumps

---

## Materials Needed

- Computers with BasCAT
- Week 3 quiz (graded, ready to return)
- Handout: "Flags Reference Card"
- Flag visualization poster

---

## Lesson Outline

### Warm-Up / Week 3 Recap & Bridge (7 minutes)

**Return Week 3 Quiz**:
- Quick review of logic operations
- Common errors discussed

**The Next Level**:
"So far, our programs run straight through - line by line. But real programs make DECISIONS!"

**Demo Two Programs**:

**Program 1** (boring):
```assembly
IN A
ADD A, 10
OUT A
HALT
```
"Always adds 10. Every time. No choices."

**Program 2** (exciting - preview):
```assembly
IN A
CMP A, 18
; If A >= 18, add 10
; If A < 18, add 5
; (We'll learn how to do this!)
```

**Today's Foundation**: "Before we can make decisions, we need to COMPARE values!"

### Direct Instruction: The CMP Instruction (13 minutes)

**What is CMP?**

"CMP = COMPARE. It compares two values and sets FLAGS to tell you the result."

**Syntax**:
```assembly
CMP register, value
```

**What CMP Does**:
1. Subtracts value from register (internally)
2. Sets flags based on result
3. **Does NOT change the register!** (unlike SUB)
4. Just tells you: equal? greater? less?

**Example**:
```assembly
LOAD A, 10
CMP A, 10      ; Compare A with 10
; Flags are set, but A still = 10!
OUT A          ; Still outputs 10
HALT
```

**CMP vs SUB**:
```
SUB A, 5  →  A = A - 5  (changes A)
CMP A, 5  →  Sets flags (A unchanged)
```

**The Flags Review**:
```
Flags: ZNCO [0000]
       ││││
       │││└─ O: Overflow
       ││└── C: Carry/Borrow
       │└─── N: Negative
       └──── Z: Zero
```

**How CMP Sets Flags**:

**Example 1: Equal Values**
```assembly
LOAD A, 50
CMP A, 50      ; 50 - 50 = 0
; Z flag = 1 (Zero flag set!)
; Result is zero, so values are EQUAL
```

**Example 2: Greater Than**
```assembly
LOAD A, 100
CMP A, 50      ; 100 - 50 = 50 (positive)
; Z flag = 0 (not zero)
; C flag = 0 (no borrow)
; Result positive, so A > value
```

**Example 3: Less Than**
```assembly
LOAD A, 30
CMP A, 50      ; 30 - 50 = -20 (underflow)
; Z flag = 0 (not zero)
; C flag = 1 (borrow occurred!)
; Underflow means A < value
```

**Reading Comparison Results**:

| To Check | Look At | Condition |
|----------|---------|-----------|
| A == B | Z flag | Z = 1 |
| A != B | Z flag | Z = 0 |
| A > B | C and Z flags | C = 0, Z = 0 |
| A < B | C flag | C = 1 |
| A >= B | C flag | C = 0 |
| A <= B | C or Z | C = 1 or Z = 1 |

**Live Demo in BasCAT**:
```assembly
LOAD A, 75
CMP A, 50
; Watch flags in circuit view
; Z = 0 (not equal)
; C = 0 (no borrow, A >= B)
HALT
```

Point to flags display, show they're set without changing A.

**Why This Matters**:
"Tomorrow we'll use these flags to make decisions - IF flags say equal, DO this!"

### Guided Practice: Flag Reading (15 minutes)

**Challenge 1: Equality Test** (5 min)

"Compare two values, determine if equal"
```assembly
IN A           ; First number
IN B           ; Second number
CMP A, B       ; Compare
; Check flags - if Z=1, they're equal!
HALT
```

Students run with different inputs:
- Input 10, 10 → Z flag set
- Input 10, 20 → Z flag clear

**Challenge 2: Greater Than Test** (5 min)

"Test if user input > 50"
```assembly
IN A
CMP A, 50
; Check flags
; If C=0 and Z=0, then A > 50
HALT
```

Test cases:
- Input 75 → C=0, Z=0 (greater)
- Input 50 → C=0, Z=1 (equal)
- Input 25 → C=1, Z=0 (less)

**Challenge 3: Multiple Comparisons** (5 min)

"Compare same value against multiple thresholds"
```assembly
IN A
MOV B, A       ; Save input

CMP A, 0       ; Compare with 0
; Observe flags

MOV A, B       ; Restore
CMP A, 50      ; Compare with 50
; Observe flags

MOV A, B       ; Restore
CMP A, 100     ; Compare with 100
; Observe flags

HALT
```

Input 60:
- vs 0: C=0 (greater)
- vs 50: C=0 (greater)
- vs 100: C=1 (less)

**Key Teaching Point**: "CMP doesn't change the value, so we can compare same number multiple times!"

### Independent Practice: Comparison Challenges (10 minutes)

**Level 1 - Basic: Range Testing**
```assembly
; Test if input is between 10 and 20
IN A
MOV B, A

CMP A, 10      ; A >= 10?
; Check C flag

MOV A, B
CMP A, 20      ; A <= 20?
; Check C and Z flags

HALT
```

**Level 2 - Intermediate: Threshold Classification**
```assembly
; Classify input: low (<50), medium (50-100), high (>100)
IN A
MOV B, A

CMP A, 50
; Save flag status in mind

MOV A, B
CMP A, 100
; Compare flags to classify

HALT
```

**Level 3 - Advanced: Multiple Value Comparison**
```assembly
; Read 3 values, find relationships
; Which is largest? Which is smallest?
IN A
IN B
IN C

; Compare A with B
MOV D, A
CMP D, B
; Note flags

; Compare B with C
MOV D, B
CMP D, C
; Note flags

; Compare A with C
MOV D, A
CMP D, C
; Note flags

HALT
```

### Class Discussion: Flags as Decision Foundation (5 minutes)

**The Big Picture**:

"Today you learned to SET flags with CMP.
Tomorrow: Use flags to JUMP to different code!
This week: Build programs that make DECISIONS!"

**Preview - Conditional Jump**:
```assembly
LOAD A, 18
CMP A, 21      ; Compare with drinking age
JC label       ; Jump if Carry (if A < 21)
; Code for "you're old enough"
HALT
label:
; Code for "too young"
HALT
```

"We'll learn JC, JZ, JNC, JNZ tomorrow!"

**Real-World Analogies**:
- "If temperature > 80, turn on AC"
- "If password correct, unlock phone"
- "If age >= 18, allow entry"
- "If health = 0, game over"

**Interactive**: "Name a program that makes decisions"
Students suggest: Games, calculators, login systems, etc.

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

1. What does CMP do to the compared values? (Answer: Nothing! Sets flags only)
2. If CMP sets Z flag, what does that mean? (Equal)
3. Code: Compare register A with 100
```assembly
CMP A, 100
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"JUMPS! Make your programs go to different places based on comparisons!"

---

## Homework

**Assignment**: "Flag Observation Practice"

**Program 1**: Equality Checker
```assembly
; Check if two inputs are equal
IN A
IN B
CMP A, B
; Observe Z flag
; If Z=1, they're equal!
HALT
```

**Program 2**: Threshold Detector
```assembly
; Check if input >= 100
IN A
CMP A, 100
; If C=0, input >= 100
; If C=1, input < 100
HALT
```

**Program 3**: Triple Compare
```assembly
; Compare input against 25, 50, 75
; Observe flags for each
IN A
MOV B, A

CMP A, 25
; Note flags

MOV A, B
CMP A, 50
; Note flags

MOV A, B
CMP A, 75
; Note flags

HALT
```

**Challenge**: Create comparison table showing what flags are set for different input values (0, 50, 100, 200) compared against 100.

**Due**: Next class
**Submit**: `week4_day1_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (CMP understanding)
- ✓ Flag reading observation
- ✓ Comparison execution
- ✓ Class discussion participation

### Success Criteria:
- Student understands CMP doesn't change values
- Student can read Z flag for equality
- Student can read C flag for comparison
- Student knows flags enable decisions

---

## Differentiation

### For Struggling Students:
- **Focus on Z flag only**: Just equality testing
- **Visual**: Flag chart always visible
- **Simple Comparisons**: Use nice round numbers
- **Pair Work**: Watch flags together

### For Advanced Students:
- **All Flag Combinations**: Explore N and O flags
- **Signed Comparisons**: Negative number comparisons
- **Optimization**: Minimize comparisons needed
- **Preview**: Look ahead at conditional jumps

### For ELL Students:
- **Vocabulary**: Compare, equal, greater, less, flag, status
- **Visual Flags**: Color-coded flag states
- **Sentence Frames**:
  - "CMP sets flags but ___ the value"
  - "Z flag set means values are ___"
- **Flag Chart**: Always accessible

---

## Teacher Notes

### Common Errors:

1. **"CMP changed my register!"**
   - Emphasize: CMP does NOT modify registers
   - Show with OUT before and after CMP

2. **"I don't understand the flags"**
   - Start with Z flag only (easiest)
   - Use simple, equal values first
   - Build to greater/less than

3. **"C flag confuses me"**
   - Remember: C=1 means borrow (A < B)
   - C=0 means no borrow (A >= B)
   - Use consistent examples

4. **"Why not just use SUB?"**
   - SUB destroys original value
   - CMP preserves for later use
   - CMP is specifically for testing

### Time Management:
- If running short: Skip Level 3 practice
- If running long: Add more flag examples
- Keep focus on Z and C flags

### Setup:
- [ ] Flag chart on wall
- [ ] Test all CMP examples
- [ ] Prepare flag observation sheet
- [ ] Have comparison table ready

### Follow-Up:
- Review exit tickets - CMP vs SUB clear?
- Prepare jump instructions for tomorrow
- Create decision flowcharts

---

## Handout: Flags Reference Card

```
╔════════════════════════════════════════════╗
║         FLAGS REFERENCE CARD               ║
╠════════════════════════════════════════════╣
║                                            ║
║  Flags: ZNCO [????]                        ║
║         ││││                               ║
║         │││└─ O: Overflow (signed)         ║
║         ││└── C: Carry/Borrow              ║
║         │└─── N: Negative (bit 7)          ║
║         └──── Z: Zero                      ║
║                                            ║
║  CMP INSTRUCTION:                          ║
║  ┌──────────────────────────────────────┐ ║
║  │ CMP register, value                  │ ║
║  │ • Compares by subtracting (internal) │ ║
║  │ • Sets flags based on result         │ ║
║  │ • Does NOT change register!          │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  READING COMPARISONS:                      ║
║                                            ║
║  Equal (A == B):                           ║
║  └─> Z flag = 1                           ║
║                                            ║
║  Not Equal (A != B):                       ║
║  └─> Z flag = 0                           ║
║                                            ║
║  Greater Than (A > B):                     ║
║  └─> C = 0 and Z = 0                      ║
║                                            ║
║  Less Than (A < B):                        ║
║  └─> C = 1                                ║
║                                            ║
║  Greater or Equal (A >= B):                ║
║  └─> C = 0                                ║
║                                            ║
║  Less or Equal (A <= B):                   ║
║  └─> C = 1 or Z = 1                       ║
║                                            ║
║  EXAMPLES:                                 ║
║                                            ║
║  LOAD A, 50                                ║
║  CMP A, 50     ; Z=1 (equal)               ║
║                                            ║
║  LOAD A, 100                               ║
║  CMP A, 50     ; C=0, Z=0 (greater)        ║
║                                            ║
║  LOAD A, 25                                ║
║  CMP A, 50     ; C=1 (less)                ║
║                                            ║
║  KEY POINT:                                ║
║  CMP sets flags, register unchanged!       ║
║  Can compare same value multiple times!    ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-15: Justify the selection of algorithms
- 3A-AP-13: Create prototypes

**Learning Objectives**:
- LO2.1: Write functional assembly programs
- LO1.1: Explain CPU components (flags)
- LO4.1: Decompose problems

---

*End of Week 4, Day 1 Lesson Plan*
