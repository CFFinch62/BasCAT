# Week 2, Day 3: User Input with IN

**Topic**: Interactive Programs with the IN Instruction
**Duration**: 50 minutes
**Learning Objectives**:
- Use IN instruction to read user input
- Understand memory-mapped I/O
- Create interactive programs
- Combine input, arithmetic, and output

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 2
- Handout: "I/O Reference Card"
- Example of INPUT port diagram

---

## Lesson Outline

### Warm-Up / The Limitation of Static Programs (7 minutes)

**Demo a Boring Program**:
```assembly
LOAD A, 10
ADD A, 5
OUT A
HALT
```

"This program ALWAYS outputs 15. Every single time. Boring!"

**The Problem**:
- All our programs have been STATIC
- They do the same thing every time
- No interaction with the user

**Student Poll**:
"Raise your hand if you've used a program that asks for input?"
- Calculator apps
- Games (enter your name)
- Search engines
- Login screens

**Today's Solution**: "Make OUR programs interactive with the IN instruction!"

**Demo Sneak Peak**:
Run this program:
```assembly
IN A
OUT A
HALT
```
Type: 42
Output: 42

"The program echoed back what YOU typed! That's interaction!"

### Direct Instruction: The IN Instruction (12 minutes)

**Memory-Mapped I/O Review**:

"Remember from Week 1: Special memory addresses are connected to I/O devices!"

**Whiteboard Diagram**:
```
Memory Map:
┌───────────────────┐
│ 0-253: Regular    │
│        RAM        │
├───────────────────┤
│ 254 (0xFE):      │
│   OUTPUT Port     │ ← OUT instruction
├───────────────────┤
│ 255 (0xFF):      │
│   INPUT Port      │ ← IN instruction
└───────────────────┘
```

**The IN Instruction**:

**Syntax**:
```assembly
IN register
```

**What it does**:
1. Waits for user to type something and press Enter
2. Reads one value from the input queue
3. Stores it in the specified register

**Simple Example**:
```assembly
IN A           ; Wait for input
OUT A          ; Echo it back
HALT
```

**Execution Flow**:
1. Program hits IN instruction
2. **PAUSES** waiting for input
3. User types "25" and presses Enter
4. Value 25 goes into register A
5. Program continues

**Circuit View**:
- Point to I/O Port component
- Show INPUT port at address 0xFF
- "When you type in the I/O Panel, data goes here"
- "IN instruction reads from this port"

**Important Points**:

1. **Blocking**: IN waits for input (program pauses)
2. **One Value**: IN reads ONE number at a time
3. **Destructive**: Overwrites register contents
4. **Interactive**: Makes programs dynamic!

**Simple Interactive Calculator**:
```assembly
; Add two user inputs
IN A           ; Get first number
IN B           ; Get second number
ADD A, B       ; Add them
OUT A          ; Show result
HALT
```

**Demo**:
- Run in BasCAT
- Type: 10 [Enter]
- Type: 15 [Enter]  
- Output: 25

"You just made a calculator that works with ANY numbers!"

**Multiple Inputs**:
```assembly
; Calculate (A + B) - C
IN A
IN B
IN C
ADD A, B       ; A = A + B
SUB A, C       ; A = A - C
OUT A
HALT
```

"The program asks for three inputs, then does math!"

### Guided Practice: Interactive Programs (15 minutes)

**Challenge 1: Echo** (3 min)

"Write a program that reads one number and outputs it."

**Expected Solution**:
```assembly
IN A
OUT A
HALT
```

Test with different inputs!

**Challenge 2: Add to Constant** (5 min)

"Read a number from user, add 10 to it, output result."

**Expected Solution**:
```assembly
IN A
ADD A, 10
OUT A
HALT
```

Test: Input 5 → Output 15

**Challenge 3: Two-Number Calculator** (7 min)

"Read two numbers, subtract the second from the first, output result."

**Expected Solution**:
```assembly
IN A           ; First number
IN B           ; Second number
SUB A, B       ; A - B
OUT A
HALT
```

Test: Input 50, 20 → Output 30

**Common Issues to Address**:

1. **"Nothing happens!"**
   - Check: Did you press Enter after typing?
   - Check: Is program waiting at IN instruction?

2. **"I only see one number in output"**
   - Remember: One OUT per value
   - Want both inputs shown? Use two OUTs

3. **"My calculation is wrong"**
   - Verify input order matters (especially for SUB)
   - Test with simple numbers (like 10 and 5)

### Independent Practice: Interactive Challenge (10 minutes)

**Choose Your Level**:

**Level 1 - Basic: Double It**
Read a number, double it (add it to itself), output
```assembly
IN A
ADD A, A       ; Double (A + A)
OUT A
HALT
```

Test: Input 7 → Output 14

**Level 2 - Intermediate: Three Numbers**
Read three numbers, add all three, output sum
```assembly
IN A
IN B
IN C
ADD A, B
ADD A, C
OUT A
HALT
```

Test: Input 5, 10, 15 → Output 30

**Level 3 - Advanced: Complex Calculation**
Read two numbers (A and B)
Calculate: (A + B) - 10
Output both the sum AND the final result

**Expected Solution (Level 3)**:
```assembly
IN A
IN B
ADD A, B       ; A = sum
OUT A          ; Show sum
SUB A, 10      ; A = sum - 10
OUT A          ; Show final result
HALT
```

Test: Input 25, 15 → Output 40, 30

**Extension**: 
"Can you create a program where the user determines how many times to do an operation?" (Preview loops!)

### Class Discussion: Why Interactive Matters (6 minutes)

**Comparison Activity**:

**Static Program**:
```assembly
LOAD A, 10
LOAD B, 20
ADD A, B
OUT A
HALT
```
"This ONLY adds 10 + 20. Forever."

**Interactive Program**:
```assembly
IN A
IN B
ADD A, B
OUT A
HALT
```
"This adds ANY two numbers the user wants!"

**Questions**:
1. "Which program is more useful?" (Interactive!)
2. "What real programs use input?"
   - Calculators
   - Games
   - Search engines
   - EVERY app you use!

3. "What's the tradeoff?"
   - Interactive: More useful but slower (waits for user)
   - Static: Fast but limited

**Real-World Connection**:
"Every app on your phone uses input:
- Games: Touch screen, buttons
- Calculator: Number pad
- Messages: Keyboard
- Camera: Tap to take photo

Input makes computers INTERACTIVE instead of just automatic!"

**Preview Next Week**:
"Next week you'll learn LOOPS. Imagine:
- Keep asking for numbers until user says stop
- Repeat calculations multiple times
- THIS is real programming!"

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper, write code to:
"Read a number from the user, add 5 to it, output the result."

**Expected Answer**:
```assembly
IN A
ADD A, 5
OUT A
HALT
```

**Bonus**: "How would you read TWO numbers and output both?"

**Collect**: Exit tickets

**Preview Tomorrow**:
"Tomorrow we'll combine EVERYTHING: input, output, arithmetic, and memory storage!"

---

## Homework

**Assignment**: "Interactive Programs"

**Program 1**: Age Calculator
Read the current year, read birth year, calculate age, output
```assembly
; Example: 2024 - 2008 = 16
IN A           ; Current year
IN B           ; Birth year
SUB A, B       ; Calculate age
OUT A
HALT
```

**Program 2**: Temperature Converter (simplified)
Read Fahrenheit temperature, subtract 32, output (simplified conversion)
```assembly
IN A           ; Temp in F
SUB A, 32      ; Simplified conversion
OUT A
HALT
```

**Program 3**: Three-Number Average (simplified)
Read three numbers, add them together, output the sum
(We'll do real division later!)
```assembly
IN A
IN B
IN C
ADD A, B
ADD A, C
OUT A          ; This is the SUM (not average yet)
HALT
```

**Challenge**: Create a program that:
- Reads two numbers
- Calculates and outputs their sum
- Calculates and outputs their difference  
- Calculates and outputs their sum minus 100

Example: Input 60, 40
Output: 100 (sum), 20 (difference), 0 (sum-100)

**Due**: Next class
**Submit**: `week2_day3_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (IN syntax)
- ✓ Guided practice observation
- ✓ Interactive program creation
- ✓ Class discussion participation

### Success Criteria:
- Student can write IN instruction correctly
- Student understands program waits for input
- Student can combine IN with arithmetic
- Student can test programs with different inputs

---

## Differentiation

### For Struggling Students:
- **Template**: Provide program structure with blanks
- **Echo First**: Master simple echo before arithmetic
- **Pair Work**: Test each other's programs
- **Visual**: Flowchart showing input → process → output

### For Advanced Students:
- **Multiple Operations**: Chain many calculations
- **Input Validation**: What happens with bad input?
- **Creative**: Make a quiz program (ask questions)
- **Research**: How do real programs validate input?

### For ELL Students:
- **Vocabulary**: Input, output, interactive, wait, pause
- **Sentence Frames**:
  - "IN reads ___ from ___"
  - "The program waits for ___"
- **Visual I/O Diagram**: Always visible
- **Bilingual Pair**: If possible

---

## Teacher Notes

### Common Errors:

1. **"My program doesn't stop at IN"**
   - Check: Is there input queued already?
   - Solution: Clear input queue, run fresh

2. **"I typed 10 but got different output"**
   - Check: Did you add/subtract to it?
   - Verify: What should the answer be?

3. **"Can I read text/letters?"**
   - Yes! ASCII codes
   - A = 65, B = 66, etc.
   - We'll explore this more later

4. **"What if user presses Enter with no number?"**
   - BasCAT may default to 0
   - In real programming, this needs error handling

### Time Management:
- If running short: Skip Level 3 independent practice
- If running long: Add more class discussion
- Have working examples ready to demo

### Setup:
- [ ] Test I/O panel before class
- [ ] Print I/O Reference Card
- [ ] Ensure all computers can access I/O
- [ ] Have backup examples ready

### Follow-Up:
- Review exit tickets - IN syntax correct?
- Prepare for combining concepts (Day 4)
- Plan comprehensive review for Day 5

---

## Handout: I/O Reference Card

```
╔════════════════════════════════════════════╗
║         INPUT/OUTPUT REFERENCE             ║
╠════════════════════════════════════════════╣
║                                            ║
║  MEMORY-MAPPED I/O:                        ║
║  ┌──────────────────────────────────────┐ ║
║  │ Address 0xFF (255): INPUT Port       │ ║
║  │ Address 0xFE (254): OUTPUT Port      │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  INPUT - Read from User:                   ║
║  ═══════════════════════════              ║
║                                            ║
║  IN register                               ║
║                                            ║
║  Example:                                  ║
║  IN A           ; Read into A              ║
║  IN B           ; Read into B              ║
║                                            ║
║  What happens:                             ║
║  1. Program PAUSES                         ║
║  2. Waits for user input                   ║
║  3. User types number and presses Enter    ║
║  4. Value goes into register               ║
║  5. Program continues                      ║
║                                            ║
║  ═══════════════════════════              ║
║                                            ║
║  OUTPUT - Display to User:                 ║
║  ═══════════════════════════              ║
║                                            ║
║  OUT register                              ║
║                                            ║
║  Example:                                  ║
║  OUT A          ; Display A                ║
║  OUT B          ; Display B                ║
║                                            ║
║  ═══════════════════════════              ║
║                                            ║
║  COMMON PATTERNS:                          ║
║                                            ║
║  Echo:                                     ║
║  IN A                                      ║
║  OUT A                                     ║
║                                            ║
║  Calculate:                                ║
║  IN A                                      ║
║  IN B                                      ║
║  ADD A, B                                  ║
║  OUT A                                     ║
║                                            ║
║  Multiple Outputs:                         ║
║  IN A                                      ║
║  MOV B, A        ; Save original           ║
║  ADD A, 10       ; Calculate               ║
║  OUT B           ; Show original           ║
║  OUT A           ; Show result             ║
║                                            ║
║  TIPS:                                     ║
║  • IN blocks until input received          ║
║  • Press Enter to send input               ║
║  • One number per IN instruction           ║
║  • Test with simple numbers first!         ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms
- 3A-AP-16: Design and iteratively develop programs

**Learning Objectives**:
- LO2.1: Write functional assembly programs
- LO1.2: Trace data flow through computer system
- LO4.1: Decompose problems into computational steps

---

*End of Week 2, Day 3 Lesson Plan*
