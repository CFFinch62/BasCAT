# Week 2, Day 4: Combining All Concepts

**Topic**: Integrating I/O, Arithmetic, Registers, and Memory
**Duration**: 50 minutes
**Learning Objectives**:
- Combine input, arithmetic, and output in complex programs
- Use memory to store multiple calculated values
- Design multi-step interactive programs
- Apply all Week 1 and Week 2 concepts together

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 3
- Handout: "Program Design Template"
- Examples of real calculators/apps

---

## Lesson Outline

### Warm-Up / Homework Showcase (7 minutes)

**Student Solutions**:
- Project 2-3 homework programs
- "Age Calculator" (most common)
- Discuss different approaches

**Quick Poll**:
"Who found interactive programs more fun than static ones?"
(Most hands should raise)

**Today's Challenge**:
"Everything you've learned comes together today. We're building REAL applications!"

**Show Real-World Example**:
"A smartphone calculator app does exactly what we're learning:
- Takes INPUT (you tap numbers)
- Does ARITHMETIC (adds, subtracts)
- Shows OUTPUT (displays result)
- Stores values in MEMORY (memory button)"

### Direct Instruction: Program Design Strategy (12 minutes)

**The Problem-Solving Process**:

"Before writing code, PLAN your program!"

**5-Step Design Process**:

1. **Understand**: What does the program need to do?
2. **Input**: What data do I need from the user?
3. **Process**: What calculations/operations?
4. **Output**: What should be displayed?
5. **Storage**: What needs to be saved in memory?

**Example Problem**: "Grade Average Calculator"
- Read 3 test scores
- Calculate sum
- Output each score and the sum

**Step 1 - Understand**:
"Calculate average of 3 test scores"

**Step 2 - Input**:
- First test score
- Second test score
- Third test score

**Step 3 - Process**:
- Add all three scores

**Step 4 - Output**:
- Each original score
- The sum

**Step 5 - Storage**:
- Need to save scores to output them later
- Use memory addresses 10, 11, 12

**Planning Document**:
```
INPUTS:
- Score 1 (via IN A, store to address 10)
- Score 2 (via IN A, store to address 11)
- Score 3 (via IN A, store to address 12)

PROCESSING:
- Load all three scores
- Add them together
- Result in register A

OUTPUTS:
- Score 1 from memory
- Score 2 from memory
- Score 3 from memory
- Sum from register A

MEMORY MAP:
Address 10: Score 1
Address 11: Score 2
Address 12: Score 3
```

**Live Coding** (students follow along):
```assembly
; Grade Average Calculator
; Reads 3 scores, outputs each and their sum

; === INPUT SECTION ===
IN A
STM 10, A      ; Store score 1

IN A
STM 11, A      ; Store score 2

IN A
STM 12, A      ; Store score 3

; === PROCESSING SECTION ===
LDM A, 10      ; Load score 1
LDM B, 11      ; Load score 2
LDM C, 12      ; Load score 3

ADD A, B       ; A = score1 + score2
ADD A, C       ; A = sum of all three

; === OUTPUT SECTION ===
LDM B, 10      ; Reload score 1
OUT B

LDM B, 11      ; Reload score 2
OUT B

LDM B, 12      ; Reload score 3
OUT B

OUT A          ; Output sum

HALT

; === MEMORY MAP ===
; Address 10: First test score
; Address 11: Second test score
; Address 12: Third test score
```

**Test Together**:
Input: 85, 90, 95
Output: 85, 90, 95, 270

**Key Points**:
- Organized into sections (Input, Process, Output)
- Comments explain each part
- Memory map documented
- Tested with real values

### Guided Practice: Design Before Code (15 minutes)

**Challenge**: "Shopping Cart Calculator"

"Create a program that:
1. Reads prices of 3 items
2. Calculates total
3. Calculates change from $100
4. Outputs each price, total, and change"

**Step 1: Plan Together** (5 min)

Fill out design template together:

```
PROBLEM: Shopping cart with change calculation

INPUTS:
- Item 1 price
- Item 2 price
- Item 3 price

PROCESSING:
- Sum of all prices
- 100 - sum = change

OUTPUTS:
- Each item price
- Total
- Change

MEMORY MAP:
Address 20: Item 1
Address 21: Item 2
Address 22: Item 3
```

**Step 2: Code Together** (10 min)

Students code while teacher circulates:

```assembly
; Shopping Cart Calculator

; Input prices
IN A
STM 20, A

IN A
STM 21, A

IN A
STM 22, A

; Calculate total
LDM A, 20
LDM B, 21
LDM C, 22
ADD A, B
ADD A, C       ; A = total

; Save total for later
MOV D, A

; Calculate change from 100
LOAD B, 100
SUB B, A       ; B = change

; Output results
LDM A, 20
OUT A          ; Item 1

LDM A, 21
OUT A          ; Item 2

LDM A, 22
OUT A          ; Item 3

OUT D          ; Total

OUT B          ; Change

HALT
```

**Test**: Input 25, 30, 20
Expected Output: 25, 30, 20, 75, 25

### Independent Practice: Build Your Own (10 minutes)

**Choose a Project**:

**Level 1 - Basic: Two-Number Stats**
Read two numbers, output:
- First number
- Second number
- Sum
- Difference (first - second)

**Level 2 - Intermediate: Temperature Converter**
Read Fahrenheit temperature
Calculate pseudo-Celsius: (F - 32)
Output both temperatures

**Level 3 - Advanced: Savings Calculator**
Read:
- Starting amount
- Deposit 1
- Deposit 2
- Withdrawal
Calculate and output:
- Starting amount
- After deposit 1
- After deposit 2
- After withdrawal (final balance)

**Example Level 3 Solution**:
```assembly
; Savings Calculator
IN A
STM 50, A      ; Starting

IN A           ; Deposit 1
MOV B, A
LDM A, 50
ADD A, B
STM 51, A      ; Balance after dep 1

IN A           ; Deposit 2
MOV B, A
LDM A, 51
ADD A, B
STM 52, A      ; Balance after dep 2

IN A           ; Withdrawal
MOV B, A
LDM A, 52
SUB A, B
STM 53, A      ; Final balance

; Output all states
LDM A, 50
OUT A
LDM A, 51
OUT A
LDM A, 52
OUT A
LDM A, 53
OUT A

HALT
```

### Class Discussion: Program Quality (6 minutes)

**What Makes a Good Program?**

Show two versions of same program:

**Version A** (Poor):
```assembly
IN A
IN B
ADD A, B
OUT A
HALT
```

**Version B** (Good):
```assembly
; Two-Number Adder
; Reads two numbers and outputs their sum

; === INPUT ===
IN A           ; First number
IN B           ; Second number

; === PROCESS ===
ADD A, B       ; Calculate sum

; === OUTPUT ===
OUT A          ; Display result

HALT

; Memory: None used
; Registers: A (sum), B (second number)
```

**Discussion**:
"Both programs work! But Version B is better because:
- Comments explain what's happening
- Sections are clear (Input/Process/Output)
- Future-you can understand it
- Others can understand it
- Easier to modify/debug"

**Code Quality Checklist**:
- [ ] Comments explain sections
- [ ] Memory map documented
- [ ] Tested with multiple inputs
- [ ] Organized structure
- [ ] Meaningful variable usage

**Real-World Connection**:
"Professional programmers spend MORE time reading code than writing it! Clear code is essential."

---

## Closure / Exit Ticket (5 minutes)

**Design Challenge**:

On paper, PLAN (don't code) a program that:
1. Reads your age
2. Reads your friend's age
3. Calculates and outputs the sum
4. Calculates and outputs the difference

**Required**: List inputs, processing, outputs

**Example Answer**:
```
Inputs: My age, friend's age
Processing: Sum (age1 + age2), Diff (age1 - age2)
Outputs: Sum, Difference
Memory: Address 10 (my age), Address 11 (friend's age)
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"Lab Day! You'll create a complete calculator application!"

---

## Homework

**Assignment**: "Personal Finance Tracker"

Create a program that:
1. Reads weekly allowance
2. Reads amount spent on Monday
3. Reads amount spent on Tuesday
4. Reads amount spent on Wednesday
5. Calculates remaining balance
6. Outputs:
   - Starting allowance
   - After Monday
   - After Tuesday
   - After Wednesday (final balance)

**Requirements**:
- Use memory to store each day's balance
- Include comments for each section
- Create memory map
- Test with realistic values

**Example**:
Input: 50, 10, 15, 8
Output: 50, 40, 25, 17

**Challenge**: Add a fourth day and calculate how much MORE you can spend before running out.

**Due**: Tomorrow (for lab day reference)
**Submit**: `week2_day4_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (program design)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Code organization

### Success Criteria:
- Student can design multi-step programs
- Student can combine I/O, arithmetic, memory
- Student organizes code with comments
- Student documents memory usage

---

## Differentiation

### For Struggling Students:
- **Template**: Provide section structure
- **Simpler Problem**: Just input + output, skip storage
- **Pair Programming**: Work with partner
- **Visual Flowchart**: Draw before coding

### For Advanced Students:
- **Complex Calculations**: More operations
- **Optimization**: Minimize memory usage
- **Creative**: Design own problem/solution
- **Research**: Look up real calculator algorithms

### For ELL Students:
- **Vocabulary**: Section, organize, document, plan
- **Template**: Provide planning document
- **Visual**: Flowchart with pictures
- **Bilingual Pair**: If available

---

## Teacher Notes

### Common Errors:

1. **"I lost the input values!"**
   - Solution: Store in memory before processing
   - Use MOV to preserve in registers temporarily

2. **"My outputs are in wrong order"**
   - Check: Loading from correct memory addresses?
   - Review memory map

3. **"Program is too complicated"**
   - Break into sections
   - Test each section separately

4. **"Memory addresses are confusing"**
   - Use consistent addressing (10-19 for one type, 20-29 for another)
   - Always document memory map

### Time Management:
- If running short: Skip Level 3 independent practice
- If running long: Extend design discussion
- Have multiple examples ready

### Setup:
- [ ] Print Program Design Templates
- [ ] Test all example programs
- [ ] Prepare flowchart examples
- [ ] Have solution variations ready

### Follow-Up:
- Review exit tickets - can students plan programs?
- Prepare for Lab Day (Day 5)
- Have calculator project specs ready

---

## Handout: Program Design Template

```
╔════════════════════════════════════════════╗
║       PROGRAM DESIGN TEMPLATE              ║
╠════════════════════════════════════════════╣
║                                            ║
║  Program Name: _______________________     ║
║  Your Name: __________________________     ║
║  Date: _______________________________     ║
║                                            ║
║  STEP 1: UNDERSTAND THE PROBLEM            ║
║  What does this program need to do?        ║
║  ______________________________________    ║
║  ______________________________________    ║
║                                            ║
║  STEP 2: IDENTIFY INPUTS                   ║
║  What data comes from the user?            ║
║  1. ___________________________________    ║
║  2. ___________________________________    ║
║  3. ___________________________________    ║
║  4. ___________________________________    ║
║                                            ║
║  STEP 3: DEFINE PROCESSING                 ║
║  What calculations/operations needed?      ║
║  1. ___________________________________    ║
║  2. ___________________________________    ║
║  3. ___________________________________    ║
║  4. ___________________________________    ║
║                                            ║
║  STEP 4: PLAN OUTPUTS                      ║
║  What should be displayed?                 ║
║  1. ___________________________________    ║
║  2. ___________________________________    ║
║  3. ___________________________________    ║
║  4. ___________________________________    ║
║                                            ║
║  STEP 5: MEMORY MAP                        ║
║  What needs to be stored?                  ║
║  ┌────────┬──────────────────────────┐    ║
║  │Address │ Purpose                  │    ║
║  ├────────┼──────────────────────────┤    ║
║  │        │                          │    ║
║  ├────────┼──────────────────────────┤    ║
║  │        │                          │    ║
║  ├────────┼──────────────────────────┤    ║
║  │        │                          │    ║
║  └────────┴──────────────────────────┘    ║
║                                            ║
║  STEP 6: CODE STRUCTURE                    ║
║  Organize into sections:                   ║
║  □ INPUT section                           ║
║  □ PROCESSING section                      ║
║  □ OUTPUT section                          ║
║  □ Comments explaining each part           ║
║  □ Memory map in comments                  ║
║                                            ║
║  NOW START CODING!                         ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms to solve problems
- 3A-AP-17: Decompose problems into sub-problems
- 3A-AP-16: Design and iteratively develop programs

**Learning Objectives**:
- LO4.1: Decompose problems into computational steps
- LO2.1: Write functional assembly programs
- LO4.4: Design data structures using available memory

---

*End of Week 2, Day 4 Lesson Plan*
