# Week 1, Day 1: Introduction & First Program

**Topic**: What is a Register? Your First Assembly Program
**Duration**: 50 minutes
**Learning Objectives**:
- Understand what a register is and why computers need them
- Write and execute a simple assembly program
- Observe data flow through BasCAT's circuit visualization

---

## Materials Needed

- Computers with BasCAT installed
- Projector for demonstration
- Student notebooks for circuit diagrams
- Handout: "Register Quick Reference Card" (see end of lesson)

---

## Lesson Outline

### Warm-Up / Hook (5 minutes)

**Activity**: "Human Computer" game
- Ask 3 student volunteers to come forward
- Give each a small whiteboard (or paper)
- Tell them: "You are registers A, B, and C"
- Teacher says: "Load 42 into register A"
  - Student A writes "42" on their board
- Teacher: "Load 100 into register B"
  - Student B writes "100"
- **Debrief**: "What you just did is exactly what a computer does! Registers are like these whiteboards - tiny, fast places to hold numbers."

### Introduction to Registers (10 minutes)

**Direct Instruction**:

"Computers need places to store data temporarily while they work. Think about doing math in your head:
- You remember the numbers you're working with
- You do calculations
- You remember the result

Computers do the same thing, but they use **registers** instead of memory.

**Key Points**:
- **Registers** are tiny, super-fast storage locations inside the CPU
- BasCAT has 4 general-purpose registers: A, B, C, D
- Each holds one 8-bit number (0-255)
- Registers are like the CPU's scratch pad

**Why not just use memory for everything?**
- Memory is slower (like walking to a filing cabinet)
- Registers are faster (like keeping paper on your desk)
- The ALU can only work with data in registers"

**Visual**: Point to BasCAT circuit view
- Show the 4 register boxes on the left
- Show they're connected to the CPU
- Explain data bus carries values to/from registers

### First Program Demonstration (15 minutes)

**Teacher Live Coding**: Project BasCAT on screen

"Let's write our very first assembly program. It will:
1. Put a number in register A
2. Send it to the output
3. Stop"

**Type together**:
```assembly
LOAD A, 72
OUT A
HALT
```

**Explain each line**:
- `LOAD A, 72` - "Load the value 72 into register A"
  - LOAD is the instruction
  - A is the destination register
  - 72 is the value (happens to be ASCII for 'H')
- `OUT A` - "Output whatever is in register A"
  - Sends value to the I/O panel
- `HALT` - "Stop the program"
  - Tells the CPU to stop executing

**Execute**:
- Click "Step" button slowly
- Watch each instruction execute
- Point out circuit animations:
  - Value 72 appears in instruction
  - Travels over bus to register A
  - Register A lights up with 72
  - OUT instruction sends 72 to output port
  - Output displays "72"

**Discussion**: "Notice we got '72' as output. That's actually the ASCII code for the letter 'H'. Computers store everything as numbers!"

### Guided Practice (15 minutes)

**Activity**: Modify the Program

"Now you try! Modify this program to output your age instead of 72."

**Student Task**:
```assembly
LOAD A, ??    ; Replace ?? with your age
OUT A
HALT
```

**Circulate and Help**:
- Check students are saving files
- Help with syntax if needed
- Encourage students to use Step mode to watch execution

**Extension for Fast Finishers**:
- "Can you output two numbers? Try adding another LOAD and OUT"
- Example solution:
```assembly
LOAD A, 25    ; My age
OUT A
LOAD A, 12    ; My favorite number
OUT A
HALT
```

**Common Issues to Address**:
- Forgetting HALT (program keeps running)
- Typos in instruction names
- Not saving file before running

### Circuit Analysis (5 minutes)

**Whole Class Discussion**:

"Let's watch one student's program execute in slow motion."

**Pick a volunteer**, project their screen:
- Click "Step" through each instruction
- Class observes circuit view
- Ask questions:
  - "Where did the number come from?" (From the instruction in memory)
  - "Which bus carried it?" (Data bus)
  - "Where did it go?" (Register A)
  - "What happened when we executed OUT?" (Register A → Output port)

**Draw on Board**:
```
[Memory] --data bus--> [Register A] --data bus--> [Output Port]
```

"This is the **data path** for our program. Every instruction follows paths like this through the computer."

---

## Closure / Exit Ticket (5 minutes)

**Quick Write** (in notebooks):

Answer these 3 questions:
1. What is a register? (in your own words)
2. What does the LOAD instruction do?
3. Draw the path data takes from the LOAD instruction to register A

**Share Out**:
- Call on 2-3 students to share their answers
- Clarify any misconceptions

**Preview Tomorrow**:
"Tomorrow we'll use all 4 registers (A, B, C, D) and learn how to move data between them!"

---

## Homework

**Assignment**: "Five Facts About Me"

Write an assembly program that outputs 5 numbers representing facts about you:
- Your age
- Your birth month (1-12)
- Your favorite number
- Number of siblings
- Your house/apartment number (or last 2 digits)

**Requirements**:
- Use LOAD to put each number in register A
- Use OUT after each LOAD to display it
- Include comments explaining each number
- End with HALT

**Example**:
```assembly
; Five Facts About Me by [Your Name]

LOAD A, 16      ; My age
OUT A

LOAD A, 7       ; Born in July (month 7)
OUT A

LOAD A, 42      ; Favorite number
OUT A

LOAD A, 2       ; I have 2 siblings
OUT A

LOAD A, 58      ; House number 58
OUT A

HALT
```

**Due**: Beginning of next class
**Format**: Save as `week1_day1_homework.asm` and submit

---

## Assessment

### Formative Assessment (During Class):
- ✓ Observation during guided practice
- ✓ Circuit analysis participation
- ✓ Exit ticket responses

### Criteria for Success:
- Student can explain what a register is
- Student can write a simple LOAD/OUT/HALT program
- Student can identify data flow in circuit view

---

## Differentiation

### For Struggling Students:
- Pair with a peer for guided practice
- Provide completed example to modify
- Use physical manipulatives (cards for registers)
- One-on-one help during guided practice

### For Advanced Students:
- Challenge: Output ASCII art (use ASCII codes to make letters)
- Extension: Try loading into registers B, C, D (they'll discover they can!)
- Research: Look up ASCII table, plan a secret message

### For ELL Students:
- Pre-teach vocabulary: register, load, output, halt
- Visual vocabulary cards with pictures
- Sentence frames: "A register is ___"
- Partner with strong English speaker

---

## Teacher Notes

### Common Misconceptions:
1. **"Register A is special"** - Clarify all 4 general registers work the same way
2. **"LOAD moves data"** - Clarify LOAD copies data, it doesn't move it
3. **"The number disappears after OUT"** - Show register A still contains the value

### Time Management:
- If running short, skip circuit analysis discussion (can do tomorrow)
- If running long, reduce guided practice time (homework covers same skill)

### Setup Before Class:
- [ ] BasCAT installed and tested on all computers
- [ ] Example program loaded and ready to demo
- [ ] Projector working
- [ ] Handouts printed

### Follow-Up for Next Lesson:
- Review homework submissions
- Identify students who struggled with syntax
- Prepare examples using multiple registers

---

## Handout: Register Quick Reference Card

```
╔════════════════════════════════════════╗
║   BasCAT REGISTER QUICK REFERENCE      ║
╠════════════════════════════════════════╣
║                                        ║
║  GENERAL PURPOSE REGISTERS:            ║
║  ┌───┐ ┌───┐ ┌───┐ ┌───┐               ║
║  │ A │ │ B │ │ C │ │ D │               ║
║  └───┘ └───┘ └───┘ └───┘               ║
║                                        ║
║  Each register holds:                  ║
║  • One 8-bit number (0-255)            ║
║  • Temporary storage for calculations  ║
║  • Very fast access                    ║
║                                        ║
║  BASIC INSTRUCTIONS (Day 1):           ║
║                                        ║
║  LOAD reg, value                       ║
║  └─> Put a number into a register      ║
║      Example: LOAD A, 42               ║
║                                        ║
║  OUT reg                               ║
║  └─> Display register's value          ║
║      Example: OUT A                    ║
║                                        ║
║  HALT                                  ║
║  └─> Stop the program                  ║
║                                        ║
║  SYNTAX RULES:                         ║
║  • One instruction per line            ║
║  • Comments start with ;               ║
║  • Case doesn't matter (LOAD = load)   ║
║  • Numbers can be 0-255                ║
║                                        ║
╚════════════════════════════════════════╝
```

**Tip**: Tape this to your monitor or keep in your notebook!

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms to solve computational problems

**Learning Objectives Addressed**:
- LO2.1: Write functional assembly programs
- LO2.2: Use registers effectively
- LO1.2: Trace data flow through computer system

---

*End of Week 1, Day 1 Lesson Plan*
