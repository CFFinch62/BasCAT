# Week 1, Day 4: Memory Storage

**Topic**: RAM - Storage Beyond Registers
**Duration**: 50 minutes
**Learning Objectives**:
- Understand memory as permanent data storage
- Use STM (Store to Memory) and LDM (Load from Memory)
- Differentiate between registers and memory
- Create a memory map for programs

---

## Materials Needed

- Computers with BasCAT
- Handout: "Memory Map Template"
- Graph paper for memory diagrams
- Post-it notes for memory address activity

---

## Lesson Outline

### Warm-Up / Problem Introduction (8 minutes)

**The Register Limitation Problem**:

"You have a homework assignment with 10 math problems. Each answer is a number. How do you store all 10 answers?"

Students: "Use 10 registers!"
Teacher: "But we only have 4 registers (A, B, C, D)..."

**Demo the Problem**:
```assembly
; Trying to store 10 values in 4 registers
LOAD A, 1      ; Answer to problem 1
LOAD B, 2      ; Answer to problem 2
LOAD C, 3      ; Answer to problem 3
LOAD D, 4      ; Answer to problem 4
; Now what? We're out of registers!
```

**The Solution**: "We need MORE storage. That's what MEMORY (RAM) is for!"

**Quick Poll**:
- "How many of you have heard of RAM?"
- "What do you think RAM does?"

### Direct Instruction: Understanding Memory (12 minutes)

**Concept**: Memory as a Filing Cabinet

"Think of memory like a giant filing cabinet:
- Registers = papers on your desk (4 sheets)
- Memory = filing cabinet (256 drawers!)
- Each drawer has an ADDRESS (like drawer #1, drawer #2, etc.)"

**Whiteboard Diagram**:
```
REGISTERS (Fast)          MEMORY (Bigger)
┌───┐ ┌───┐              ┌─────────────┐
│ A │ │ B │              │ 0: [   ]   │
├───┤ ├───┤              ├─────────────┤
│ C │ │ D │              │ 1: [   ]   │
└───┘ └───┘              ├─────────────┤
  4 spaces                │ 2: [   ]   │
                          ├─────────────┤
                          │ ...         │
                          ├─────────────┤
                          │ 255: [  ]   │
                          └─────────────┘
                           256 spaces!
```

**Memory Addresses**:
- Memory has 256 locations (addresses 0-255)
- Each location stores ONE byte (0-255)
- Each location has a unique ADDRESS

**BasCAT Circuit View**:
- Point to RAM component
- "This big box is memory - 256 bytes!"
- Point to address bus: "This tells memory WHICH address to read/write"
- Point to data bus: "This carries the actual data"

**Two New Instructions**:

**STM (Store to Memory)**:
```assembly
STM address, register
```
Example: `STM 10, A` means "Store register A's value at memory address 10"

**LDM (Load from Memory)**:
```assembly
LDM register, address
```
Example: `LDM A, 10` means "Load memory address 10's value into register A"

**Live Demonstration**:
```assembly
; Memory Storage Demo

LOAD A, 42
STM 10, A      ; Store 42 at address 10

LOAD A, 0      ; Clear register A
OUT A          ; Output 0 (to show A is really cleared)

LDM A, 10      ; Load from address 10
OUT A          ; Output 42 (it was saved in memory!)

HALT
```

**Execute Step-by-Step**:
1. A=42 (after LOAD)
2. Memory[10]=42 (after STM), A still = 42
3. A=0 (after clearing LOAD)
4. A=42 (after LDM from memory)

**Circuit Focus**:
- Watch STM: Register A → Address bus shows "10" → Data flows to memory
- Watch LDM: Address bus shows "10" → Data flows from memory → Register A

**Key Differences**:

| Registers | Memory |
|-----------|--------|
| 4 total | 256 total |
| Very fast | Slightly slower |
| Temporary | More permanent |
| CPU can work with directly | Must load into register first |

### Guided Practice: Variable Storage (15 minutes)

**Concept**: Memory as Variables

"In real programming, we use memory like variables. Each address can hold a different piece of data."

**Example - Student Data**:
```assembly
; Store student information
; Let's say:
;   Address 20 = age
;   Address 21 = grade level
;   Address 22 = favorite number

LOAD A, 16
STM 20, A      ; Store age at address 20

LOAD A, 11
STM 21, A      ; Store grade (11th grade)

LOAD A, 7
STM 22, A      ; Store favorite number

; Now retrieve and display
LDM A, 20
OUT A          ; Show age

LDM A, 21
OUT A          ; Show grade

LDM A, 22
OUT A          ; Show favorite number

HALT
```

**Memory Map**:
```
Address | Contents | Meaning
--------|----------|----------
   20   |    16    | My age
   21   |    11    | Grade level
   22   |     7    | Favorite number
```

**Class Activity**: Create Your Own Data Storage

Students write program to store 5 facts:
- Address 50: Your age
- Address 51: Birth month
- Address 52: Number of siblings
- Address 53: Favorite number
- Address 54: Lucky number

**Template**:
```assembly
; My Data Storage by [Name]

; Store data
LOAD A, ??
STM 50, A      ; Age

; ... continue for all 5 facts ...

; Retrieve and display
LDM A, 50
OUT A

; ... continue for all 5 facts ...

HALT
```

**Circulate**: Help students create memory maps

### Independent Practice: Data Organization (10 minutes)

**Challenge**: Grade Book System

"Create a program that stores 5 test scores in memory (addresses 10-14), then outputs them all."

**Requirements**:
1. Use addresses 10, 11, 12, 13, 14
2. Store any 5 test scores (0-100)
3. Retrieve and output all 5 scores
4. Include comments showing which address stores which test

**Extension for Fast Finishers**:
- Output scores in reverse order
- Store scores, clear registers, then retrieve
- Use different addresses (try 100, 101, 102, etc.)

**Example Memory Map**:
```
Address | Score | Test
--------|-------|------
   10   |  95   | Test 1
   11   |  87   | Test 2
   12   |  92   | Test 3
   13   |  78   | Test 4
   14   |  100  | Test 5
```

### Class Discussion: Registers vs Memory (5 minutes)

**Comparison Activity**:

"When should you use registers vs memory?"

**Scenario 1**: "You're adding two numbers"
- Answer: Use registers (faster, ALU works with registers)

**Scenario 2**: "You need to store 20 student grades"
- Answer: Use memory (not enough registers)

**Scenario 3**: "You're doing a calculation and need the result later"
- Answer: Store in memory to free up registers

**Scenario 4**: "Quick temporary calculation"
- Answer: Use registers (faster)

**Rule of Thumb**:
- Registers: Active work, calculations
- Memory: Long-term storage, lots of data

**Memory Addresses to Avoid**:
- Address 254 (0xFE): OUTPUT port
- Address 255 (0xFF): INPUT port
- Use addresses 0-253 for your data

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper, write code to:
1. Store the value 99 at memory address 25
2. Clear register A (set it to 0)
3. Load the value from address 25 into register A
4. Output register A

**Expected Answer**:
```assembly
LOAD A, 99
STM 25, A
LOAD A, 0
LDM A, 25
OUT A
HALT
```

**Key Question**: "What will the output be?" (Answer: 99)

**Collect**: Turn in exit ticket

**Preview Tomorrow**:
"Tomorrow is LAB DAY! You'll create a complete 'Personal Data Card' program using everything we've learned this week!"

---

## Homework

**Assignment**: "Memory Array"

Create a program that:
1. Stores your name spelled out in ASCII codes in memory
   - Use addresses 100, 101, 102, etc.
   - One letter per address
2. Retrieves and outputs each letter

**Example for "SAM"**:
- S = 83, A = 65, M = 77

```assembly
; My Name in Memory by Sam

; Store name
LOAD A, 83
STM 100, A     ; S

LOAD A, 65
STM 101, A     ; A

LOAD A, 77
STM 102, A     ; M

; Output name
LDM A, 100
OUT A

LDM A, 101
OUT A

LDM A, 102
OUT A

HALT
```

**Requirements**:
- At least 3 letters
- Use consecutive memory addresses starting at 100
- Include memory map in comments
- Output should spell your name (or initials)

**ASCII Reference**: https://www.asciitable.com

**Due**: Next class (bring for Lab Day)
**Submit**: `week1_day4_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (STM/LDM usage)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Memory map creation

### Success Criteria:
- Student can use STM to store values in memory
- Student can use LDM to retrieve values from memory
- Student understands memory addresses
- Student can create a memory map

---

## Differentiation

### For Struggling Students:
- **Template**: Provide partially completed program with blanks
- **Visual**: Use physical mailboxes with addresses
- **Simplified**: Store only 3 values instead of 5
- **Pair Work**: Partner with successful student

### For Advanced Students:
- **Challenge**: Create "database" with 10 items
- **Efficiency**: Minimize number of LOAD instructions
- **Pattern**: Store values in pattern (2, 4, 6, 8...)
- **Research**: Find out how much RAM modern computers have

### For ELL Students:
- **Vocabulary**: Address, store, load, memory, retrieve
- **Visual Memory Map**: Always show diagram
- **Sentence Frames**:
  - "Address ___ holds ___"
  - "STM stores ___ at address ___"
- **Bilingual Pair**: If possible

---

## Teacher Notes

### Common Errors:

1. **"STM 10, A" vs "STM A, 10" (backwards)**
   - Mnemonic: "STM address, register" (where, what)
   - Compare to "LOAD register, value" (what, where) - note difference!

2. **"I stored it but can't get it back"**
   - Check: Are they loading from the same address they stored to?
   - Use memory map to track

3. **"Using addresses 254 or 255"**
   - Explain: These are I/O ports, not storage
   - Show error that occurs

4. **"Thinking memory clears when loaded"**
   - Clarify: LDM COPIES from memory, doesn't delete it
   - Memory keeps value until overwritten

### Time Management:
- If running short: Reduce independent practice to 5 minutes
- If running long: Add bonus challenge during independent practice

### Setup:
- [ ] Print memory map templates (one per student)
- [ ] ASCII table posted or printed
- [ ] Graph paper available
- [ ] Test example programs

### Follow-Up:
- Review exit tickets - can students use STM/LDM correctly?
- Prepare for tomorrow's lab day (Week 1 Day 5)
- Have rubric ready for lab project

---

## Handout: Memory Map Template

```
╔══════════════════════════════════════════════╗
║         MEMORY MAP TEMPLATE                  ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Program: ___________________________        ║
║  Your Name: _____________________            ║
║                                              ║
║  ┌──────────┬──────────┬───────────────┐    ║
║  │ Address  │ Contents │ Description   │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  ├──────────┼──────────┼───────────────┤    ║
║  │          │          │               │    ║
║  └──────────┴──────────┴───────────────┘    ║
║                                              ║
║  NOTES:                                      ║
║  • Use addresses 0-253 for data              ║
║  • Avoid 254 (OUTPUT) and 255 (INPUT)        ║
║  • Each address holds 0-255                  ║
║  • Document what each address represents     ║
║                                              ║
╚══════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-17: Decompose problems
- 3A-CS-01: Explain how abstractions hide implementation details

**Learning Objectives**:
- LO1.4: Explain how memory addresses map to data storage
- LO2.1: Write functional assembly programs
- LO4.4: Design data structures using available memory

---

*End of Week 1, Day 4 Lesson Plan*
