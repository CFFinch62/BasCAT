# Week 1, Day 3: Moving Data with MOV

**Topic**: The MOV Instruction - Copying Between Registers
**Duration**: 50 minutes
**Learning Objectives**:
- Use MOV to copy data between registers
- Understand the difference between copying and moving
- Recognize when to use LOAD vs MOV
- Implement register-to-register operations

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 2 (reverse order program)
- Handout: "LOAD vs MOV Comparison Chart"
- Index cards for register swapping activity

---

## Lesson Outline

### Warm-Up / Homework Review (7 minutes)

**Homework Debrief**: Reverse Order Challenge

Project student solution on screen:
```assembly
; Student solution example
LOAD A, 100
LOAD B, 200
LOAD C, 300
LOAD D, 400
OUT D        ; 400
LOAD D, 500  ; Reuse D!
OUT D        ; 500
OUT C        ; 300
OUT B        ; 200
OUT A        ; 100
HALT
```

**Discussion**:
- "Did you realize you could REUSE a register?"
- "What happens to the old value when you LOAD a new one?" (It's replaced)
- "This works, but is there a better way?"

**Today's Problem**:
Show this code:
```assembly
LOAD A, 42
; I want B to also have 42
; How do I do it?
```

**Student Guesses**:
- `LOAD B, 42` ← Yes, but what if we don't know the value?
- What if A was calculated, not a constant?

**Today's Answer**: **MOV instruction!**

### Direct Instruction: The MOV Instruction (12 minutes)

**Concept Introduction**:

"MOV stands for MOVE, but it doesn't actually *move* data - it *copies* it!"

**Analogy**:
"Think of LOAD like writing a number on a blank register. MOV is like photocopying what's already in one register to another register."

**Syntax**:
```assembly
MOV destination, source
```

**Examples**:
```assembly
LOAD A, 100    ; A = 100
MOV B, A       ; Copy A to B, now B = 100 too
               ; A still has 100!
```

**Live Demonstration**:
```assembly
; MOV Demonstration
LOAD A, 42

MOV B, A       ; B gets copy of A
MOV C, B       ; C gets copy of B
MOV D, C       ; D gets copy of C

; Now all registers have 42!
OUT A
OUT B
OUT C
OUT D
HALT
```

**Execute Step-by-Step**:
- After `LOAD A, 42`: A=42
- After `MOV B, A`: A=42, B=42 (A unchanged!)
- After `MOV C, B`: A=42, B=42, C=42
- After `MOV D, C`: All four = 42

**Circuit Focus**:
- "Watch the data travel from register to register"
- "See how the source register keeps its value"
- "Data bus carries the copy"

**Key Point - Copy, Not Move**:
```assembly
LOAD A, 10
MOV B, A
; Question: What's in A now?
; Answer: Still 10! (it was copied, not moved)
```

**When to Use Each**:

| Situation | Use | Example |
|-----------|-----|---------|
| I know the exact value | LOAD | `LOAD A, 42` |
| I want to copy another register | MOV | `MOV B, A` |
| I want to preserve a value | MOV | `MOV D, A` before changing A |

### Guided Practice: Copy Challenge (15 minutes)

**Challenge 1: The Copy Chain** (5 min)

"Write a program that:
1. Loads 99 into register A
2. Copies it to B
3. Copies B to C
4. Copies C to D
5. Outputs all four registers"

**Expected Solution**:
```assembly
LOAD A, 99
MOV B, A
MOV C, B
MOV D, C
OUT A
OUT B
OUT C
OUT D
HALT
```

**Check Understanding**:
- "After all the MOVs, what value is in each register?" (All 99)
- "Did any register lose its value?" (No, MOV copies)

**Challenge 2: Value Preservation** (5 min)

"Problem: You need to do something that changes register A, but you want to remember A's original value."

Code:
```assembly
LOAD A, 50
; Save A before changing it
MOV B, A       ; Save copy in B

; Now change A
LOAD A, 100

; Output both
OUT B          ; Original value (50)
OUT A          ; New value (100)
HALT
```

**Real-World Use**: "Programmers do this ALL THE TIME when they need to keep a backup of data!"

**Challenge 3: Independent Work** (5 min)

"Write a program that:
1. Loads YOUR age into A
2. Copies it to registers B, C, and D
3. Outputs them in this order: B, D, A, C"

Students work independently.

**Extension**: "Can you output each register twice without loading/moving again?"

### Independent Practice: Swap Challenge (10 minutes)

**The Big Challenge**: Register Swapping

"This is a classic programming problem!"

**Problem**:
```assembly
LOAD A, 10
LOAD B, 20
; How do you swap them so A=20 and B=10?
```

**Think-Pair-Share** (3 min):
- Think individually: 1 minute
- Discuss with partner: 2 minutes
- Share ideas with class

**Common (Wrong) Answer**:
```assembly
MOV A, B       ; A = 20 (good!)
MOV B, A       ; B = 20 (PROBLEM! We lost the 10!)
```

**Why This Doesn't Work**:
- After first MOV, both A and B are 20
- The original value of A (10) is lost!

**Solution - Use a Temporary Register**:
```assembly
LOAD A, 10
LOAD B, 20

; Swap using C as temporary storage
MOV C, A       ; C = 10 (save A)
MOV A, B       ; A = 20 (copy B to A)
MOV B, C       ; B = 10 (restore from C)

OUT A          ; Should output 20
OUT B          ; Should output 10
HALT
```

**Step Through Together**:
1. Before: A=10, B=20, C=?
2. `MOV C, A`: A=10, B=20, C=10
3. `MOV A, B`: A=20, B=20, C=10
4. `MOV B, C`: A=20, B=10, C=10
5. Success!

**Physical Demonstration** (if time):
- Three students hold cards: A(10), B(20), C(blank)
- Act out the three MOV instructions
- Class sees the swap happen physically

**Student Task**: "Now YOU write a swap program. Use any numbers you want."

### Class Discussion: LOAD vs MOV (6 minutes)

**Comparison Activity**:

Show side-by-side code:

**Option 1**:
```assembly
LOAD A, 50
LOAD B, 50
LOAD C, 50
```

**Option 2**:
```assembly
LOAD A, 50
MOV B, A
MOV C, A
```

**Questions**:
1. "Do both programs end with the same result?" (Yes, all registers = 50)
2. "Which is better? Why?"
   - Option 2: If you change the value, you only change it once
   - Option 2: Makes it clear all registers get THE SAME value
   - Option 1: More explicit, easier for beginners to read

3. "When would you HAVE to use MOV?"
   - When you don't know the value (it was calculated)
   - When preserving a register value
   - When swapping

**Key Takeaway**:
"Both work! Use LOAD when you know the value, use MOV when copying from another register."

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper, write code to solve this:
```
Start: A=10, B=20, C=0, D=0
Goal:  A=20, B=10, C=10, D=20
(Swap A and B, then copy them to C and D)
```

**Expected Answer**:
```assembly
; Assume A and B already loaded with 10 and 20
MOV C, A       ; Save A (C=10)
MOV A, B       ; A = 20
MOV B, C       ; B = 10
MOV D, A       ; D = 20
HALT
```

**Collect and Review**: Check understanding of MOV

**Preview Tomorrow**:
"Tomorrow we learn about MEMORY - storage that holds WAY more than 4 values!"

---

## Homework

**Assignment**: "The Cascade"

Write a program that demonstrates the "cascading" effect of MOV:

```assembly
; The Cascade by [Your Name]

LOAD A, 1
OUT A          ; Output 1

MOV B, A
ADD A, B       ; We'll use ADD next week, but A becomes 2
OUT A          ; Output 2

MOV C, A
ADD A, C       ; A becomes 4
OUT A          ; Output 4

MOV D, A
ADD A, D       ; A becomes 8
OUT A          ; Output 8

HALT

; This should output: 1, 2, 4, 8 (powers of 2!)
```

**Wait - we haven't learned ADD yet!**
- "Don't worry - ADD is simple: `ADD A, B` adds B to A"
- "Tomorrow we'll learn it properly, but you can use it tonight"
- "If you get stuck, just do the cascade without the ADD - just use MOV"

**Alternative (if not comfortable with ADD)**:
```assembly
LOAD A, 10
OUT A

MOV B, A
OUT B

MOV C, B
OUT C

MOV D, C
OUT D

HALT
; Outputs: 10, 10, 10, 10
```

**Challenge**: Create your own cascade pattern with different values

**Due**: Next class
**Submit**: `week1_day3_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (swap + copy problem)
- ✓ Guided practice observation
- ✓ Swap challenge completion
- ✓ Class discussion participation

### Success Criteria:
- Student can use MOV to copy between registers
- Student understands MOV doesn't delete source
- Student can solve swap problem with temporary register
- Student knows when to use LOAD vs MOV

---

## Differentiation

### For Struggling Students:
- **Visual Aid**: Use colored blocks to represent register contents
- **Step-by-Step Guide**: Provide template for swap with blanks to fill
- **Pair Programming**: Work with stronger peer
- **Simplified Swap**: Just do A↔B, not involving C and D

### For Advanced Students:
- **Three-Way Swap**: Swap A→B, B→C, C→A (cyclic swap)
- **Minimize Instructions**: What's fewest MOVs to copy A to all 4 registers?
- **Challenge**: Swap WITHOUT using a third register (they'll discover they can't!)
- **Research**: Look up "XOR swap trick" (works in real assembly!)

### For ELL Students:
- **Vocabulary**: Copy, move, source, destination, temporary
- **Sentence Frames**: 
  - "MOV copies from ___ to ___"
  - "The source is ___, the destination is ___"
- **Visual Flowchart**: Draw arrows showing data flow
- **Bilingual Glossary**: MOV terms in home language

---

## Teacher Notes

### Common Misconceptions:

1. **"MOV moves data (deletes from source)"**
   - Clarify: It COPIES (source unchanged)
   - Show: After MOV B, A - A still has its value

2. **"I can swap with just two MOVs"**
   - Show why it doesn't work (loses data)
   - Demonstrate need for temporary storage

3. **"MOV and LOAD are the same"**
   - Clarify differences with comparison chart
   - LOAD: immediate value → register
   - MOV: register → register (or immediate → register)

### Time Savers:
- Have swap solution ready to show if students struggle
- Pre-create "register cards" for physical demonstration
- Skip physical demonstration if running short on time

### Setup Checklist:
- [ ] Test all example programs before class
- [ ] Print LOAD vs MOV comparison handout
- [ ] Prepare index cards for swap demonstration (optional)
- [ ] Have exit ticket ready (paper or digital)

### Follow-Up:
- Review exit tickets - can students solve swap problem?
- Identify students confused about copy vs move
- Preview ADD instruction for those using it in homework

---

## Handout: LOAD vs MOV Comparison

```
╔════════════════════════════════════════════════╗
║      LOAD vs MOV: WHAT'S THE DIFFERENCE?       ║
╠════════════════════════════════════════════════╣
║                                                ║
║  LOAD reg, value                               ║
║  └─> Puts a CONSTANT into a register          ║
║                                                ║
║  Example: LOAD A, 42                           ║
║  Result: A = 42                                ║
║                                                ║
║  ┌──────────────────────────────────────┐     ║
║  │  Use LOAD when:                      │     ║
║  │  • You know the exact number         │     ║
║  │  • You're initializing a register    │     ║
║  │  • You're starting fresh             │     ║
║  └──────────────────────────────────────┘     ║
║                                                ║
║ ─────────────────────────────────────────────  ║
║                                                ║
║  MOV dest, source                              ║
║  └─> COPIES one register to another           ║
║                                                ║
║  Example: MOV B, A                             ║
║  Result: B = (whatever A was)                  ║
║          A is UNCHANGED                        ║
║                                                ║
║  ┌──────────────────────────────────────┐     ║
║  │  Use MOV when:                       │     ║
║  │  • Copying between registers         │     ║
║  │  • Preserving a value                │     ║
║  │  • You don't know the exact value    │     ║
║  └──────────────────────────────────────┘     ║
║                                                ║
║  COMMON PATTERN:                               ║
║                                                ║
║  LOAD A, 10    ; Put 10 in A                   ║
║  MOV B, A      ; Copy A to B                   ║
║  MOV C, A      ; Copy A to C                   ║
║  ; Now A, B, C all = 10                        ║
║                                                ║
║  KEY POINT: MOV does NOT delete the source!    ║
║                                                ║
╚════════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms
- 3A-CS-02: Compare levels of abstraction in computing

**Learning Objectives**:
- LO2.2: Use registers effectively
- LO2.1: Write functional assembly programs
- LO4.2: Implement algorithms efficiently

---

*End of Week 1, Day 3 Lesson Plan*
