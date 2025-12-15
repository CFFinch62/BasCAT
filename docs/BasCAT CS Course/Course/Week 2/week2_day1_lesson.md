# Week 2, Day 1: Addition Basics

**Topic**: The ADD Instruction and ALU Operations
**Duration**: 50 minutes
**Learning Objectives**:
- Understand the ALU (Arithmetic Logic Unit) role
- Use ADD instruction to perform addition
- Observe ALU flags in circuit view
- Combine addition with data storage

---

## Materials Needed

- Computers with BasCAT
- Week 1 quiz (graded, ready to return)
- Handout: "ALU Quick Reference"
- Calculators for verification (optional)

---

## Lesson Outline

### Warm-Up / Week 1 Recap (7 minutes)

**Return Week 1 Quiz**:
- Hand back graded quizzes
- Quick review of common errors
- "Any questions about Week 1 concepts?"

**Week 1 Quick Review Game**:
"I'll show you code, you tell me what it does!"

```assembly
LOAD A, 10
MOV B, A
STM 20, B
```
**Answer**: Loads 10 into A, copies to B, stores B in memory address 20

**Bridge to Today**:
"Last week you learned to STORE data. This week: CALCULATE with data!"

**Demo Problem**:
"You have 5 apples. Your friend gives you 3 more. How many now?"
- Humans: Do mental math
- Computers: Use the ALU!

### Direct Instruction: The ALU (12 minutes)

**Concept**: The Arithmetic Logic Unit

"Remember from Week 1 that the ALU is INSIDE the CPU. It's the calculator part of the computer!"

**Visual on BasCAT**:
- Point to circuit view
- Show CPU box
- Point to ALU inside CPU
- "This tiny component does ALL the math!"

**The ADD Instruction**:

**Syntax**:
```assembly
ADD register, value
```

**What it does**:
- Adds the value to whatever is already in the register
- Stores result back in the same register
- Updates ALU flags

**Important**: ADD is DESTRUCTIVE
- The original value is replaced by the sum
- If you need the original, save it first!

**First Example**:
```assembly
LOAD A, 10
ADD A, 5       ; A = A + 5
OUT A          ; Output: 15
HALT
```

**Execute Step-by-Step**:
1. A = 10 (after LOAD)
2. A = 15 (after ADD)
3. Output: 15

**Circuit Animation**:
- Watch value 10 load into A
- Watch ADD instruction
- See ALU light up
- See result (15) go back to A
- "The ALU did the math!"

**Adding Two Registers**:
"You can also add one register to another!"

```assembly
LOAD A, 10
LOAD B, 5
ADD A, B       ; A = A + B
OUT A          ; Output: 15
HALT
```

**Key Point**:
- A gets the result (15)
- B keeps its value (5)
- Only the DESTINATION changes

**Adding Multiple Values**:
```assembly
LOAD A, 5
ADD A, 3       ; A = 8
ADD A, 2       ; A = 10
ADD A, 1       ; A = 11
OUT A          ; Output: 11
HALT
```

"Each ADD builds on the previous result!"

**The Flags Display**:

Point to flags in circuit view:
```
Flags: ZNCO [0000]
```

**After addition**:
- Z (Zero): Set if result = 0
- N (Negative): Set if bit 7 = 1
- C (Carry): Set if result > 255 (overflow)
- O (Overflow): Set if signed overflow

**Simple Example**:
```assembly
LOAD A, 100
ADD A, 50      ; Result: 150
; Flags: [0000] - no flags set

LOAD A, 200
ADD A, 100     ; Result: 44 (wraps around!)
; Flags: [0011] - Carry and Overflow set
```

"We'll use flags more next week. For now, just know they exist!"

### Guided Practice: Simple Addition (15 minutes)

**Challenge 1: Two Numbers** (5 min)

"Write a program that:
1. Adds 25 + 17
2. Outputs the result"

**Expected Solution**:
```assembly
LOAD A, 25
ADD A, 17
OUT A          ; 42
HALT
```

**Challenge 2: Three Numbers** (5 min)

"Add three numbers together: 10 + 20 + 30"

**Expected Solution**:
```assembly
LOAD A, 10
ADD A, 20      ; A = 30
ADD A, 30      ; A = 60
OUT A
HALT
```

**Challenge 3: Using Two Registers** (5 min)

"Add the contents of register A and register B, output the sum."

**Expected Solution**:
```assembly
LOAD A, 15
LOAD B, 25
ADD A, B       ; A = 40
OUT A
HALT
```

**Common Issues to Address**:
1. **"My answer is wrong!"**
   - Check: Did you add in the right order?
   - Verify with calculator

2. **"ADD A, A doesn't work!"**
   - Actually it does! It doubles A
   - Example: A=10, ADD A, A → A=20

3. **"The original value disappeared!"**
   - Yes! ADD is destructive
   - Solution: Save original with MOV first

### Independent Practice: Addition Challenges (10 minutes)

**Choose Your Challenge**:

**Level 1 - Basic: Sum Calculator**
Write a program that:
- Adds 5 + 10 + 15 + 20
- Outputs the sum (50)

**Level 2 - Intermediate: Save and Add**
```assembly
; Store original value, then add to it
LOAD A, 30
MOV B, A       ; Save original in B
ADD A, 20      ; A = 50
OUT B          ; Output original (30)
OUT A          ; Output sum (50)
HALT
```

**Level 3 - Advanced: Running Total**
Create a program that:
- Starts with 0
- Adds 1, outputs result
- Adds 2, outputs result  
- Adds 3, outputs result
- Should output: 1, 3, 6

**Example Solution (Level 3)**:
```assembly
LOAD A, 0
ADD A, 1
OUT A          ; 1
ADD A, 2
OUT A          ; 3
ADD A, 3
OUT A          ; 6
HALT
```

**Extension**: "Can you output ALL intermediate sums for a problem?"

### Class Discussion: When ADD Changes Things (6 minutes)

**Show This Code**:
```assembly
LOAD A, 50
LOAD B, 30
ADD A, B
OUT A
OUT B
```

**Questions**:
1. "What does A hold after ADD?" (80)
2. "What does B hold after ADD?" (30 - unchanged!)
3. "How would you preserve A's original value?"

**Solution**:
```assembly
LOAD A, 50
MOV C, A       ; Save A
LOAD B, 30
ADD A, B       ; A = 80
OUT C          ; Original A (50)
OUT A          ; Sum (80)
OUT B          ; B unchanged (30)
HALT
```

**Real-World Connection**:
"This is why calculators have a memory button - sometimes you need to save values before calculating!"

**Preview Overflow**:
```assembly
LOAD A, 200
ADD A, 100
OUT A          ; What will this output?
```

Run it: Output is 44!
"Why? 200 + 100 = 300, but max is 255. It wraps around!"
"We'll explore this more as we go."

---

## Closure / Exit Ticket (5 minutes)

**Quick Write**:

On paper, write code to solve:
"Add 12 + 8 + 5 and output the result."

**Expected Answer**:
```assembly
LOAD A, 12
ADD A, 8
ADD A, 5
OUT A
HALT
```

OR:
```assembly
LOAD A, 12
LOAD B, 8
LOAD C, 5
ADD A, B
ADD A, C
OUT A
HALT
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"Tomorrow: SUBTRACTION! Plus we'll start using INPUT to make our programs interactive!"

---

## Homework

**Assignment**: "Math Practice"

Write three separate programs:

**Program 1**: Add your age + your best friend's age
```assembly
; Example for age 16 + age 15
LOAD A, 16
ADD A, 15
OUT A          ; 31
HALT
```

**Program 2**: Add three favorite numbers together
```assembly
; Example: 7 + 13 + 42
LOAD A, 7
ADD A, 13
ADD A, 42
OUT A          ; 62
HALT
```

**Program 3**: Progressive sum (show each step)
Add 5 + 10 + 15, outputting after EACH addition
```assembly
LOAD A, 5
OUT A          ; 5
ADD A, 10
OUT A          ; 15
ADD A, 15
OUT A          ; 30
HALT
```

**Challenge**: Create a program that adds 5 numbers and outputs both:
- The sum
- The original first number (using MOV to save it)

**Due**: Next class
**Submit**: Three files or one file with three programs separated by comments

---

## Assessment

### Formative:
- ✓ Exit ticket (basic addition)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Class discussion participation

### Success Criteria:
- Student can write ADD instruction correctly
- Student understands ADD is destructive
- Student can add multiple values sequentially
- Student can use ADD with both immediate values and registers

---

## Differentiation

### For Struggling Students:
- **Calculator**: Allow calculator to verify answers
- **Template**: Provide partially completed code
- **Pair Work**: Partner with successful peer
- **Simplified**: Focus on 2-number addition only

### For Advanced Students:
- **Overflow Challenge**: Explore what happens with 200 + 100
- **Efficiency**: What's the minimum instructions to add 5 numbers?
- **Pattern**: Create Fibonacci-like sequence using ADD
- **Research**: Look up "integer overflow" in real programming

### For ELL Students:
- **Vocabulary**: Sum, add, result, destination, destructive
- **Visual**: Show addition with physical blocks/counters
- **Sentence Frames**:
  - "ADD adds ___ to ___"
  - "The result goes in ___"
- **Native Language**: Allow math verification in home language

---

## Teacher Notes

### Common Errors:

1. **"ADD 10, A" instead of "ADD A, 10"**
   - Reinforce: Destination first!
   - Mnemonic: "ADD (where), (what)"

2. **"My sum is wrong"**
   - Check mental math vs computer output
   - Use calculator to verify
   - Check for typos in values

3. **"I get weird numbers with big sums"**
   - Explain overflow (briefly)
   - Show: 255 + 1 = 0
   - "We'll explore this more later"

4. **"Why does B not change when I ADD A, B?"**
   - Clarify: Only destination (first operand) changes
   - Show in circuit view

### Time Management:
- If running short: Skip Level 3 independent practice
- If running long: Reduce class discussion time
- Have solutions ready to show

### Setup:
- [ ] Week 1 quizzes graded and ready
- [ ] Test all example programs
- [ ] Print ALU Quick Reference
- [ ] Calculators available (optional)

### Follow-Up:
- Review exit tickets - addition syntax correct?
- Prepare for subtraction (Day 2)
- Have overflow examples ready for later

---

## Handout: ALU Quick Reference

```
╔════════════════════════════════════════════╗
║         ALU QUICK REFERENCE                ║
╠════════════════════════════════════════════╣
║                                            ║
║  The ALU (Arithmetic Logic Unit) is the    ║
║  calculator inside the CPU!                ║
║                                            ║
║  ADDITION:                                 ║
║  ┌──────────────────────────────────────┐ ║
║  │ ADD register, value                  │ ║
║  │ ADD register, register               │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  EXAMPLES:                                 ║
║                                            ║
║  ADD A, 10                                 ║
║  └─> Adds 10 to A                         ║
║      A = A + 10                           ║
║                                            ║
║  ADD A, B                                  ║
║  └─> Adds B to A                          ║
║      A = A + B                            ║
║      B is unchanged                       ║
║                                            ║
║  IMPORTANT:                                ║
║  • ADD is DESTRUCTIVE                     ║
║  • Original value in destination is lost  ║
║  • Save original with MOV if needed       ║
║                                            ║
║  COMMON PATTERN:                           ║
║                                            ║
║  LOAD A, 10                                ║
║  ADD A, 5      ; A = 15                    ║
║  ADD A, 3      ; A = 18                    ║
║  OUT A         ; Output: 18                ║
║                                            ║
║  SAVING ORIGINAL VALUE:                    ║
║                                            ║
║  LOAD A, 20                                ║
║  MOV B, A      ; Save original             ║
║  ADD A, 10     ; A = 30                    ║
║  OUT B         ; Original: 20              ║
║  OUT A         ; Sum: 30                   ║
║                                            ║
║  FLAGS (we'll learn more next week):       ║
║  Z - Zero (result is 0)                    ║
║  N - Negative (bit 7 = 1)                  ║
║  C - Carry (overflow > 255)                ║
║  O - Overflow (signed overflow)            ║
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
- LO1.1: Explain CPU components (ALU)
- LO4.2: Implement algorithms efficiently

---

*End of Week 2, Day 1 Lesson Plan*
