# Week 1, Day 2: Multiple Registers

**Topic**: Using All Four General-Purpose Registers
**Duration**: 50 minutes
**Learning Objectives**:
- Use registers A, B, C, and D effectively
- Understand that all general-purpose registers work identically
- Load different values into different registers
- Plan register usage before coding

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 1 (for review)
- Handout: "Register Planning Worksheet" (see end of lesson)
- Graph paper (for register diagrams)

---

## Lesson Outline

### Warm-Up / Homework Review (8 minutes)

**Homework Showcase**:
- "Who can share one number from their 'Five Facts' program?"
- Project 2-3 student solutions on screen
- Discuss: "Did everyone use register A? Could you have used other registers?"

**Quick Check**:
Display this code, ask "What will it output?"
```assembly
LOAD A, 10
OUT A
LOAD A, 20
OUT A
HALT
```
**Answer**: 10, then 20

**Discussion**: 
- "The second LOAD replaced the first value in A"
- "What if we want to keep BOTH 10 and 20 at the same time?"
- **Today's Answer**: "Use different registers!"

### Direct Instruction: The Four Registers (10 minutes)

**Concept Introduction**:

"Yesterday we used register A. But BasCAT has 4 registers: A, B, C, and D. They're all identical! Think of them like 4 boxes on your desk - each can hold a different item."

**Whiteboard Diagram**:
```
┌─────────────────────────────┐
│         CPU                 │
│  ┌───┐ ┌───┐ ┌───┐ ┌───┐  │
│  │ A │ │ B │ │ C │ │ D │  │
│  │ ? │ │ ? │ │ ? │ │ ? │  │
│  └───┘ └───┘ └───┘ └───┘  │
└─────────────────────────────┘
```

**Key Points**:
- Each register can hold ONE number (0-255)
- They all work exactly the same way
- You can load different values into each one
- They all exist at the same time

**Live Demonstration**:
```assembly
; Using all four registers
LOAD A, 10
LOAD B, 20
LOAD C, 30
LOAD D, 40
OUT A
OUT B
OUT C
OUT D
HALT
```

**Execute Step-by-Step** (use Step button):
- After `LOAD A, 10`: Point to register A showing "10"
- After `LOAD B, 20`: Now A=10, B=20
- After `LOAD C, 30`: Now A=10, B=20, C=30
- After `LOAD D, 40`: All four registers have different values!
- Watch each OUT read from different register

**Circuit Focus**: 
- "See all 4 registers lit up with different values?"
- "Each LOAD instruction targets a specific register"
- "Each OUT instruction reads from a specific register"

**Why This Matters**:
"If you're doing a calculation like (A + B) × C, you need multiple registers to hold all those values!"

### Guided Practice: Register Planning (15 minutes)

**Activity**: "Data Storage Challenge"

**Problem**: Store and Display Ages
- Store YOUR age in one register
- Store your BEST FRIEND's age in another
- Store your TEACHER's age in a third (make a guess!)
- Display all three values

**Step 1: Planning (5 min)**
Hand out "Register Planning Worksheet"

"Before you write ANY code, plan which register holds what."

Students fill out:
```
Register A will hold: My age (16)
Register B will hold: Friend's age (15)
Register C will hold: Teacher's age (35)
Register D will hold: (not needed)
```

**Walk around**: Check that students are planning, not jumping to code

**Step 2: Coding (8 min)**
Now implement the plan:
```assembly
; Age Storage Program by [Student Name]

LOAD A, 16      ; My age
LOAD B, 15      ; Friend's age (Sam)
LOAD C, 35      ; Teacher's age (Mr. Smith)

; Display all values
OUT A
OUT B
OUT C

HALT
```

**Key Teaching Points While Circulating**:
- Comments explain what each register holds
- Register choice doesn't matter (could use D instead of C)
- HALT at the end prevents infinite execution

**Step 3: Share (2 min)**
- Pick 2 students to show solutions
- Ask: "Did you plan first? Did it help?"
- Emphasize: Planning prevents mistakes

### Independent Practice: Challenge Levels (12 minutes)

**Students Choose Difficulty**:

**Level 1 - Basic: Birthday Data**
Write a program that stores and outputs:
- Day you were born (1-31)
- Month you were born (1-12)
- Year (last 2 digits, like 07 for 2007)
- Your current age

Use four different registers, output all four values.

**Level 2 - Intermediate: ASCII Initials**
Store ASCII codes for your initials:
- Look up ASCII codes (A=65, B=66, etc.)
- Store first initial in register A
- Store last initial in register B
- Output both
- Example: For "Alice Brown" → A(65), B(66)

**Level 3 - Advanced: Reverse Order**
Create a data card with 4 facts (your choice):
- Use all 4 registers (A, B, C, D)
- Output them in REVERSE order: D, C, B, A
- In comments, explain WHY reverse order works

**Timer**: "You have 10 minutes - GO!"

**Support**: 
- Circulate and help
- Point struggling students to Level 1
- Challenge fast finishers with Level 3

### Class Discussion: Register Strategy (5 minutes)

**Whole Class Debrief**:

"Let's talk about what you learned."

**Question 1**: "Why did we plan which register to use before coding?"
- Expected answers:
  - Prevents confusion
  - Helps organize code
  - Makes debugging easier
  - You know what goes where

**Question 2**: "Does it REALLY matter which register you use?"
- Answer: "No! They're all identical."
- "BUT: Using them consistently makes YOUR code easier to read"
- "Convention: Most programmers use A for main work, B/C/D for temporary storage"

**Question 3**: "What if you need to store 10 numbers, but only have 4 registers?"
- Take guesses
- **Preview**: "Tomorrow we'll learn about MEMORY - much bigger storage!"

**Misconception Check**:
Show this code:
```assembly
LOAD A, 10
LOAD A, 20
OUT A
HALT
```

Ask: "What will this output?"
- **Answer**: 20 (not 10!)
- **Key Point**: "Each register holds only ONE value. The second LOAD overwrites the first."
- **Solution**: "Use different registers to keep both values!"

---

## Closure / Exit Ticket (5 minutes)

**Quick Write**:

Solve this problem ON PAPER (no computer):

"Write assembly code to:
1. Store 5 in register A
2. Store 10 in register B
3. Output both numbers
4. Stop the program"

**Expected Answer**:
```assembly
LOAD A, 5
LOAD B, 10
OUT A
OUT B
HALT
```

**Collect**: Students turn in paper as exit ticket

**Assessment**: Can student write multi-register code independently?

**Preview Tomorrow**:
"Tomorrow: What if you want to COPY data from register A to register B? We'll learn the MOV instruction!"

---

## Homework

**Assignment**: "Reverse Order Challenge"

Write a program that:
1. Loads these 5 values: 100, 200, 300, 400, 500
2. Outputs them in REVERSE order: 500, 400, 300, 200, 100

**The Catch**: You only have 4 registers (A, B, C, D)!

**Strategy Hint**: 
- Load first 4 values into the 4 registers
- Output in reverse (D, C, B, A)
- Then REUSE a register for the 5th value

**Example Start**:
```assembly
; Reverse Order by [Your Name]

LOAD A, 100
LOAD B, 200
LOAD C, 300
LOAD D, 400

; Output D first (400)
OUT D

; Now load 500 into D (reusing the register!)
LOAD D, 500
OUT D        ; Output 500

; Continue with C, B, A...
```

**Challenge**: Finish the program to output all 5 values in reverse order

**Bonus**: Can you do it with even FEWER instructions?

**Due**: Beginning of next class
**Submit**: Save as `week1_day2_homework.asm`

---

## Assessment

### Formative Assessment:
- ✓ Exit ticket (multi-register code writing)
- ✓ Observation during independent practice
- ✓ Register Planning Worksheet completion
- ✓ Class discussion participation

### Success Criteria:
- Student can load different values into different registers
- Student can output from any register
- Student plans register usage before coding
- Student understands register values can be overwritten

---

## Differentiation

### For Struggling Students:
- **Scaffold**: Provide partially completed code to finish
- **Visual Aid**: Use physical cups labeled A, B, C, D with number cards
- **Pair Programming**: Partner with successful peer
- **Simplified Task**: Only use 2 registers instead of 4
- **Extra Time**: Allow to finish during next class warm-up

### For Advanced Students:
- **ASCII Challenge**: Spell entire name using ASCII codes
- **Efficiency Challenge**: What's the minimum number of instructions to solve the homework?
- **Preview Concept**: Try to figure out how to copy from one register to another (they might discover they need MOV)
- **Extension**: Create a pattern using numbers across registers

### For ELL Students:
- **Vocabulary Cards**: Register A/B/C/D with visual labels
- **Sentence Frames**: 
  - "Register A holds ___"
  - "I will store ___ in register ___"
- **Bilingual Partner**: Pair with speaker of same language if possible
- **Visual Register Chart**: Keep diagram visible at all times

---

## Teacher Notes

### Common Student Errors:

1. **"I loaded A twice and only the first one worked!"**
   - Explain: Second LOAD overwrites first
   - Show in circuit view: Watch value change

2. **"Why can't I just use A for everything?"**
   - Explain: You can, but you'll lose previous values
   - Show: Need multiple registers to keep multiple values

3. **"Do I have to use A first, then B, then C?"**
   - Clarify: No! Use any order, any combination
   - Show: LOAD C, then A, then D - all works fine

4. **Syntax errors: "LOAD 10, A" instead of "LOAD A, 10"**
   - Reinforce: Destination first, then source
   - Mnemonic: "LOAD (where), (what)"

### Time Management:
- If running short: Reduce independent practice to 8 minutes
- If running long: Skip some class discussion, move to homework debrief
- Have Level 1 solution ready for students who finish early

### Setup Checklist:
- [ ] Print Register Planning Worksheets (1 per student)
- [ ] Test demo program before class
- [ ] Prepare exit ticket slips (or digital form)
- [ ] ASCII table printed/posted for Level 2 students

### Follow-Up for Next Class:
- Grade exit tickets tonight (quick scan: can they write multi-register code?)
- Prepare homework solutions to show
- Identify students struggling with syntax for extra help

---

## Handout: Register Planning Worksheet

```
╔══════════════════════════════════════════════════╗
║      REGISTER PLANNING WORKSHEET                 ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  Name: ______________________  Date: __________  ║
║                                                  ║
║  PROBLEM: What am I trying to solve?             ║
║  ____________________________________________    ║
║  ____________________________________________    ║
║                                                  ║
║  DATA: What information do I need to store?      ║
║  1. ________________________________________     ║
║  2. ________________________________________     ║
║  3. ________________________________________     ║
║  4. ________________________________________     ║
║                                                  ║
║  REGISTER ASSIGNMENTS:                           ║
║                                                  ║
║  Register A will hold: ______________________   ║
║                                                  ║
║  Register B will hold: ______________________   ║
║                                                  ║
║  Register C will hold: ______________________   ║
║                                                  ║
║  Register D will hold: ______________________   ║
║                                                  ║
║  ┌────────────────────────────────────────┐     ║
║  │ PLANNING CHECKLIST:                    │     ║
║  │ □ I identified what data I need        │     ║
║  │ □ I assigned each data to a register   │     ║
║  │ □ I avoided using same register twice  │     ║
║  │ □ I added comments to explain my plan  │     ║
║  └────────────────────────────────────────┘     ║
║                                                  ║
║  Now write your code! Refer back to this plan.   ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-17: Decompose problems into sub-problems
- 3A-AP-13: Create prototypes using algorithms

**Learning Objectives Addressed**:
- LO2.2: Use registers effectively
- LO4.1: Decompose problems into computational steps
- LO2.1: Write functional assembly programs

---

*End of Week 1, Day 2 Lesson Plan*
