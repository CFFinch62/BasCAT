# Week 2, Day 2: Subtraction & Flags

**Topic**: The SUB Instruction and Understanding ALU Flags
**Duration**: 50 minutes
**Learning Objectives**:
- Use SUB instruction to perform subtraction
- Understand and observe ALU flags (Z, N, C, O)
- Handle underflow situations
- Combine ADD and SUB in programs

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 1
- Handout: "Flags Cheat Sheet"
- Number line visual (for negative numbers)

---

## Lesson Outline

### Warm-Up / Homework Review (7 minutes)

**Quick Homework Check**:
- "Who successfully added three numbers?"
- Project one student solution for Program 3 (progressive sum)
- Verify output: 5, 15, 30

**Mental Math Warm-Up**:
"Quick! What's 100 - 25?" (75)
"What's 10 - 15?" (Negative 5!)
"What happens if a computer tries 10 - 15?"

**Today's Question**: "Subtraction seems simple, but computers handle it differently than humans!"

### Direct Instruction: The SUB Instruction (12 minutes)

**Syntax**:
```assembly
SUB register, value
```

**What it does**:
- Subtracts the value FROM the register
- Stores result back in the register
- Updates ALU flags
- Like ADD, it's DESTRUCTIVE

**Simple Example**:
```assembly
LOAD A, 20
SUB A, 5       ; A = A - 5
OUT A          ; Output: 15
HALT
```

**Execute Step-by-Step**:
1. A = 20 (after LOAD)
2. A = 15 (after SUB)
3. Output: 15

**Circuit Animation**:
- Watch ALU perform subtraction
- See result return to register A
- Note flags display

**Multiple Subtractions**:
```assembly
LOAD A, 100
SUB A, 25      ; A = 75
SUB A, 25      ; A = 50
SUB A, 25      ; A = 25
OUT A          ; Output: 25
HALT
```

"Each SUB reduces the value further."

**The Underflow Problem**:

"What happens with 10 - 15?"

```assembly
LOAD A, 10
SUB A, 15
OUT A          ; What will this output?
```

**Run it**: Output is 251!

**Why?**
- Can't have negative numbers in 8-bit unsigned
- 10 - 15 = -5
- Wraps around: 256 - 5 = 251
- This is called UNDERFLOW

**Visual on Number Line**:
```
... 253 254 255 | 0 1 2 ... 10 ... 15 ...
                 ↑
            Wraps here!
```

**Understanding Flags**:

Point to Flags display: `Flags: ZNCO [0000]`

**Z (Zero) Flag**:
```assembly
LOAD A, 10
SUB A, 10      ; A = 0
; Flags: Z=1 (zero flag set!)
```
"Set when result = 0. Useful for checking if values are equal!"

**C (Carry/Borrow) Flag**:
```assembly
LOAD A, 10
SUB A, 15      ; Underflow!
; Flags: C=1 (carry/borrow happened)
```
"Set when we needed to 'borrow' (underflow occurred)"

**N (Negative) Flag**:
- Set when bit 7 of result = 1
- In unsigned math, this means value ≥ 128

**O (Overflow) Flag**:
- Set for signed overflow
- We'll explore this more later

**When Flags Are Useful**:
"Flags tell us what happened during the operation:
- Z flag: Did we reach zero?
- C flag: Did we go negative (underflow)?
- We'll use these for IF statements next week!"

### Guided Practice: Subtraction Basics (15 minutes)

**Challenge 1: Simple Subtraction** (5 min)

"Subtract 18 from 50"

**Expected Solution**:
```assembly
LOAD A, 50
SUB A, 18
OUT A          ; 32
HALT
```

**Challenge 2: Sequential Subtraction** (5 min)

"Start with 100, subtract 10 three times, output result"

**Expected Solution**:
```assembly
LOAD A, 100
SUB A, 10      ; A = 90
SUB A, 10      ; A = 80
SUB A, 10      ; A = 70
OUT A
HALT
```

**Challenge 3: ADD and SUB Together** (5 min)

"Start with 50, add 20, subtract 15, output result"

**Expected Solution**:
```assembly
LOAD A, 50
ADD A, 20      ; A = 70
SUB A, 15      ; A = 55
OUT A
HALT
```

**Observation Time**:
- "Watch the flags change as you execute"
- "Use Step mode to see each operation"
- "What do the flags show after each instruction?"

### Independent Practice: Calculation Challenges (10 minutes)

**Choose Your Level**:

**Level 1 - Basic: Countdown**
Start with 20, subtract 5 repeatedly, output each time:
```assembly
LOAD A, 20
OUT A          ; 20
SUB A, 5
OUT A          ; 15
SUB A, 5
OUT A          ; 10
SUB A, 5
OUT A          ; 5
HALT
```

**Level 2 - Intermediate: Preserve Original**
```assembly
; Calculate 100 - 37, but keep both values
LOAD A, 100
MOV B, A       ; Save original
SUB A, 37      ; A = 63
OUT B          ; Original: 100
OUT A          ; Result: 63
HALT
```

**Level 3 - Advanced: Multi-Step Calculation**
Calculate: (50 + 20) - 15
Then: Take that result and subtract 10
Output both intermediate results

**Expected Solution (Level 3)**:
```assembly
LOAD A, 50
ADD A, 20      ; A = 70
MOV B, A       ; Save first result
SUB A, 15      ; A = 55
OUT B          ; First: 55
MOV C, A       ; Save second result
SUB A, 10      ; A = 45
OUT C          ; Second: 55 (oops, wrong! Need to fix logic)
OUT A          ; Final: 45
HALT
```

Better solution:
```assembly
LOAD A, 50
ADD A, 20      ; A = 70
SUB A, 15      ; A = 55
OUT A          ; First result
SUB A, 10      ; A = 45
OUT A          ; Final result
HALT
```

### Class Discussion: Flags in Action (6 minutes)

**Experiment Together**:

```assembly
LOAD A, 25
SUB A, 25
OUT A
```

**Questions**:
1. "What's the output?" (0)
2. "Which flag is set?" (Z - Zero flag)
3. "When might this be useful?" (Checking if values are equal!)

**Underflow Experiment**:
```assembly
LOAD A, 5
SUB A, 10
OUT A
```

**Questions**:
1. "What's the output?" (251)
2. "Which flag is set?" (C - Carry/Borrow flag)
3. "How can you tell underflow happened?" (Output > original value, C flag set)

**Practical Use**:
"Next week you'll learn IF statements. We'll use these flags to make decisions:
- IF result is zero, do something
- IF underflow happened, handle it
- This is how computers make choices!"

**Real-World Connection**:
"Video games use flags constantly:
- Health reaches 0? (Z flag) → Game over!
- Score goes negative? (C flag) → Reset to 0"

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper, solve this:
"Write code to subtract 12 from 50, then subtract 8 more, then output the result."

**Expected Answer**:
```assembly
LOAD A, 50
SUB A, 12      ; A = 38
SUB A, 8       ; A = 30
OUT A
HALT
```

**Bonus Question**: "What would the Z flag be after this program?" (0 - not zero)

**Collect**: Exit tickets

**Preview Tomorrow**:
"Tomorrow: USER INPUT! Your programs will finally interact with you using the IN instruction!"

---

## Homework

**Assignment**: "Subtraction Practice"

**Program 1**: Age Difference
Calculate the difference between your age and your parent's age (or teacher's age)
```assembly
; Example: Parent is 45, I'm 16
LOAD A, 45
SUB A, 16
OUT A          ; Difference: 29
HALT
```

**Program 2**: Countdown Sequence
Start at 30, subtract 6 five times, output after each subtraction
```
Expected output: 24, 18, 12, 6, 0
```

**Program 3**: Underflow Exploration
```assembly
; Try subtracting a LARGER number from a smaller one
LOAD A, 10
SUB A, 25
OUT A          ; What's the output?
; Write in comments what happened and why
HALT
```

**Challenge**: Create a program that:
- Starts with 100
- Adds 50 (= 150)
- Subtracts 75 (= 75)
- Adds 25 (= 100)
- Subtracts 100 (= 0)
- Outputs each intermediate result

**Due**: Next class
**Submit**: `week2_day2_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (subtraction syntax)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Flags understanding (class discussion)

### Success Criteria:
- Student can write SUB instruction correctly
- Student understands underflow
- Student can observe flags
- Student can combine ADD and SUB

---

## Differentiation

### For Struggling Students:
- **Calculator**: Verify answers
- **Skip Underflow**: Focus on normal subtraction only
- **Template**: Provide partially completed code
- **Pair Work**: Work with partner

### For Advanced Students:
- **Underflow Deep Dive**: Explore wraparound thoroughly
- **Flags Challenge**: Predict which flags will be set
- **Efficiency**: Minimize instructions for complex calculations
- **Research**: Look up "two's complement" (how computers do negative numbers)

### For ELL Students:
- **Vocabulary**: Subtract, difference, underflow, borrow, flags
- **Visual**: Number line showing wraparound
- **Sentence Frames**:
  - "SUB subtracts ___ from ___"
  - "Underflow happens when ___"
- **Calculator**: Verify math in any language

---

## Teacher Notes

### Common Errors:

1. **"SUB 5, A" instead of "SUB A, 5"**
   - Reinforce: Destination first!
   - "SUB (from what), (subtract what)"

2. **"My answer is negative but showing big number"**
   - Explain underflow/wraparound
   - Show on number line
   - Explain unsigned vs signed integers (briefly)

3. **"The flags confuse me"**
   - Focus on Z and C for now
   - "We'll use them more next week"
   - N and O can wait

4. **"I want negative numbers!"**
   - Explain BasCAT uses unsigned integers
   - "Real computers have signed types"
   - "This is a simplified educational model"

### Time Management:
- If running short: Skip underflow deep dive
- If running long: Reduce independent practice
- Have flag examples ready to show

### Setup:
- [ ] Test underflow examples before class
- [ ] Print Flags Cheat Sheet
- [ ] Number line visual prepared
- [ ] Calculator available for verification

### Follow-Up:
- Review exit tickets - subtraction syntax correct?
- Prepare for IN instruction (Day 3)
- Have I/O examples ready

---

## Handout: Flags Cheat Sheet

```
╔════════════════════════════════════════════╗
║         ALU FLAGS CHEAT SHEET              ║
╠════════════════════════════════════════════╣
║                                            ║
║  Flags: ZNCO [0000]                        ║
║          ││││                              ║
║          │││└─ O: Overflow                 ║
║          ││└── C: Carry/Borrow             ║
║          │└─── N: Negative                 ║
║          └──── Z: Zero                     ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  Z - ZERO FLAG                             ║
║  ┌──────────────────────────────────────┐ ║
║  │ Set when result = 0                  │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  Example:                                  ║
║  LOAD A, 10                                ║
║  SUB A, 10     ; A = 0, Z flag = 1         ║
║                                            ║
║  Use: Check if two values are equal        ║
║       Check if countdown reached 0         ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  C - CARRY/BORROW FLAG                     ║
║  ┌──────────────────────────────────────┐ ║
║  │ Set on overflow (ADD > 255)          │ ║
║  │ Set on underflow (SUB goes negative) │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  Example (Overflow):                       ║
║  LOAD A, 200                               ║
║  ADD A, 100    ; Result: 44, C flag = 1    ║
║                                            ║
║  Example (Underflow):                      ║
║  LOAD A, 10                                ║
║  SUB A, 20     ; Result: 246, C flag = 1   ║
║                                            ║
║  Use: Detect if math went out of range     ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  N - NEGATIVE FLAG                         ║
║  ┌──────────────────────────────────────┐ ║
║  │ Set when bit 7 of result = 1         │ ║
║  │ (values 128-255)                     │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  Use: Advanced signed arithmetic           ║
║       (we'll learn more later)             ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  O - OVERFLOW FLAG                         ║
║  ┌──────────────────────────────────────┐ ║
║  │ Set on signed integer overflow       │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  Use: Advanced signed arithmetic           ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  WATCHING FLAGS:                           ║
║  • Look at circuit view during execution   ║
║  • Use Step mode to see changes            ║
║  • Next week: Use flags for IF statements! ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms
- 3A-CS-01: Explain abstractions

**Learning Objectives**:
- LO2.1: Write functional assembly programs
- LO1.1: Explain CPU components (ALU flags)
- LO4.2: Implement algorithms efficiently

---

*End of Week 2, Day 2 Lesson Plan*
