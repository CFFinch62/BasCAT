# Week 5, Day 1: The Stack - Introduction

**Topic**: Understanding the Stack and PUSH/POP
**Duration**: 50 minutes
**Learning Objectives**:
- Understand stack data structure (LIFO)
- Use PUSH to save data on stack
- Use POP to retrieve data from stack
- Understand stack pointer concept

---

## Materials Needed

- Computers with BasCAT
- Week 4 quiz (graded, ready to return)
- Handout: "Stack Basics Guide"
- Physical stack demo (plates or books)

---

## Lesson Outline

### Warm-Up / Week 4 Recap & Stack Introduction (8 minutes)

**Return Week 4 Quiz**:
- Review control flow concepts
- Address common loop/conditional errors

**The Problem**: "Limited Registers"

"We have only 4 registers (A, B, C, D). What if we need to save 10 values temporarily?"

**Demo the Problem**:
```assembly
LOAD A, 10
LOAD B, 20
LOAD C, 30
LOAD D, 40
; All registers full!
; Need to do calculation that uses A
; But we need A's value later!
```

**Solutions So Far**:
- Memory: `STM address, A` (but need to track addresses)
- What if we don't know how many values in advance?

**Today's Solution**: "The STACK - automatic memory management!"

**Physical Demo**:
- Stack of plates/books
- Add to top (PUSH)
- Remove from top (POP)
- Last In, First Out (LIFO)

### Direct Instruction: Stack Basics (13 minutes)

**What is a Stack?**

"A stack is a LIFO (Last In, First Out) data structure:
- Like a stack of plates
- Add to top (PUSH)
- Remove from top (POP)
- Can't access middle without removing top items"

**Stack in BasCAT**:

**Whiteboard Diagram**:
```
Memory (High addresses at top):
┌─────────────┐
│   Stack     │ ← Stack grows DOWN
│   Pointer   │ ← Points to top of stack
│   (SP)      │
├─────────────┤
│    ???      │
├─────────────┤
│    ???      │
├─────────────┤
│    ...      │
└─────────────┘
```

**Stack Pointer (SP)**:
- Special register tracking top of stack
- Automatically updated by PUSH/POP
- You don't usually access SP directly

**The PUSH Instruction**:

**Syntax**:
```assembly
PUSH register
```

**What PUSH does**:
1. Decrements stack pointer
2. Stores register value at SP location
3. Register value unchanged

**Example**:
```assembly
LOAD A, 42
PUSH A         ; Save A on stack
; A still = 42
; Stack now has 42 on top
```

**The POP Instruction**:

**Syntax**:
```assembly
POP register
```

**What POP does**:
1. Loads value from SP location into register
2. Increments stack pointer
3. Stack value "removed" (SP moved)

**Example**:
```assembly
POP B          ; Get value from stack into B
; B now = 42
; Stack pointer moved up
```

**LIFO in Action**:
```assembly
LOAD A, 10
LOAD B, 20
LOAD C, 30

PUSH A         ; Stack: [10]
PUSH B         ; Stack: [10, 20]
PUSH C         ; Stack: [10, 20, 30]

POP D          ; D = 30, Stack: [10, 20]
POP D          ; D = 20, Stack: [10]
POP D          ; D = 10, Stack: []
```

"Notice: POP gives values in REVERSE order from PUSH!"

**Circuit View**:
- Show stack area in memory
- Point to stack pointer register
- Watch SP change during PUSH/POP

**Why Use Stack?**:
1. **Temporary Storage**: Save values during calculations
2. **Preserve Registers**: Save before using, restore after
3. **Function Calls**: Save state before calling subroutine (next week)
4. **Unknown Quantity**: Don't need to know how many values in advance

### Guided Practice: Basic Stack Operations (15 minutes)

**Challenge 1: Simple Save/Restore** (5 min)

"Save register A, do calculation, restore A"
```assembly
LOAD A, 100
PUSH A         ; Save A

; Use A for something else
LOAD A, 5
ADD A, 10
OUT A          ; Output 15

; Restore original A
POP A
OUT A          ; Output 100
HALT
```

**Challenge 2: Swap Using Stack** (5 min)

"Swap values in A and B using stack"
```assembly
LOAD A, 10
LOAD B, 20

PUSH A         ; Stack: [10]
PUSH B         ; Stack: [10, 20]
POP A          ; A = 20, Stack: [10]
POP B          ; B = 10, Stack: []

OUT A          ; 20
OUT B          ; 10
HALT
```

**Challenge 3: Preserve Multiple Registers** (5 min)

"Save A, B, C, use them for calculation, restore all"
```assembly
LOAD A, 1
LOAD B, 2
LOAD C, 3

; Save all
PUSH A
PUSH B
PUSH C

; Do calculations
LOAD A, 100
LOAD B, 200
ADD A, B
OUT A          ; 300

; Restore in reverse order!
POP C          ; C = 3
POP B          ; B = 2
POP A          ; A = 1

OUT A          ; 1
OUT B          ; 2
OUT C          ; 3
HALT
```

**Key Point**: "PUSH order and POP order must be OPPOSITE!"

### Independent Practice: Stack Challenges (10 minutes)

**Level 1 - Basic: Register Backup**
```assembly
; Save A and B, overwrite them, restore them
LOAD A, 50
LOAD B, 75

PUSH A
PUSH B

LOAD A, 0
LOAD B, 0
OUT A          ; 0
OUT B          ; 0

POP B
POP A
OUT A          ; 50
OUT B          ; 75
HALT
```

**Level 2 - Intermediate: Calculation with Preservation**
```assembly
; Calculate (A + B) × C
; But preserve original A, B, C values
IN A
IN B
IN C

; Save originals
PUSH A
PUSH B
PUSH C

; Calculate
ADD A, B       ; A = sum
MOV D, A
POP C          ; Get C back (stack has A, B left)
MOV A, D       ; Move sum to A

; Multiply by repeated addition (simplified)
; (Full multiplication would need loop)

; Restore originals
POP B
POP A

OUT A
OUT B
OUT C
HALT
```

**Level 3 - Advanced: Reverse Array**
```assembly
; Read 5 numbers, output in reverse order
IN A
PUSH A
IN A
PUSH A
IN A
PUSH A
IN A
PUSH A
IN A
PUSH A

; Now pop all (automatic reverse!)
POP A
OUT A
POP A
OUT A
POP A
OUT A
POP A
OUT A
POP A
OUT A
HALT
```

### Class Discussion: Stack Applications (4 minutes)

**When to Use Stack**:

1. **Temporary Register Storage**
   - Need register for calculation
   - Original value needed later
   - PUSH before, POP after

2. **Reversing Order**
   - PUSH items in order
   - POP gives reverse
   - Useful for algorithms

3. **Nested Operations**
   - Save state at each level
   - Unwind in reverse

4. **Unknown Quantity**
   - Don't know how many items
   - Stack grows as needed
   - Pop until empty

**Real-World Examples**:
- Function calls (next week!)
- Undo/Redo in applications
- Browser back button (stack of pages)
- Expression evaluation
- Recursion

**Interactive**: "Name a feature that uses a stack"
- Text editor undo
- Calculator parentheses
- File path navigation

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper:
1. What does PUSH do? (Saves value on stack)
2. What does POP do? (Retrieves value from stack)
3. What does LIFO mean? (Last In, First Out)
4. Code: Save register A on stack, then restore it

**Expected #4**:
```assembly
PUSH A
; ... other code ...
POP A
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"Stack with loops and procedures - saving state in complex programs!"

---

## Homework

**Assignment**: "Stack Practice"

**Program 1**: Three-Value Reverse
```assembly
; Read 3 values, output in reverse order
IN A
PUSH A
IN A
PUSH A
IN A
PUSH A

POP A
OUT A
POP A
OUT A
POP A
OUT A
HALT
```

**Program 2**: Preserve and Calculate
```assembly
; Read two numbers
; Save them
; Output their sum
; Restore and output originals
IN A
IN B
PUSH A
PUSH B

ADD A, B
OUT A          ; Sum

POP B
POP A
OUT A          ; Original A
OUT B          ; Original B
HALT
```

**Program 3**: Nested Preservation
```assembly
; Save A
; Save B
; Do calculation
; Restore B
; Restore A
; Output both originals
LOAD A, 10
LOAD B, 20

PUSH A
PUSH B

LOAD A, 100
LOAD B, 200
ADD A, B
OUT A          ; 300

POP B          ; B = 20
POP A          ; A = 10
OUT A
OUT B
HALT
```

**Challenge**: Use stack to reverse 10 numbers (read with loop, push all, pop all with loop).

**Due**: Next class
**Submit**: `week5_day1_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (stack concepts)
- ✓ PUSH/POP execution
- ✓ LIFO understanding
- ✓ Stack usage patterns

### Success Criteria:
- Student can use PUSH correctly
- Student can use POP correctly
- Student understands LIFO order
- Student can preserve register values

---

## Differentiation

### For Struggling Students:
- **Physical Model**: Use actual stack of objects
- **Simplified**: Just save/restore one register
- **Visual**: Draw stack state after each operation
- **Pair Work**: Trace together

### For Advanced Students:
- **Complex Patterns**: Multiple saves/restores
- **Stack Algorithms**: Implement stack-based solutions
- **Optimization**: Minimize stack usage
- **Research**: Call stack in real systems

### For ELL Students:
- **Vocabulary**: Stack, push, pop, LIFO, top, pointer
- **Visual Diagrams**: Stack state always shown
- **Sentence Frames**:
  - "PUSH saves ___ on ___"
  - "POP retrieves ___ from ___"
- **Physical Demo**: Hands-on stacking

---

## Teacher Notes

### Common Errors:

1. **"I pushed A, B, C but popped in same order"**
   - Emphasize LIFO - reverse order
   - Draw stack diagram showing layers

2. **"Stack pointer confuses me"**
   - Explain: Automatic management
   - Students don't manually control SP
   - Just use PUSH/POP

3. **"When do I use stack vs memory?"**
   - Stack: Temporary, automatic, LIFO
   - Memory: Permanent, manual addressing

4. **"My values disappeared"**
   - Check PUSH/POP balance
   - Too many POPs = undefined behavior

### Time Management:
- If running short: Skip Level 3 practice
- If running long: Add more stack examples
- Physical demo is important - don't skip

### Setup:
- [ ] Physical stack materials (plates/books)
- [ ] Stack diagram on board
- [ ] Test PUSH/POP examples
- [ ] Prepare visual aids

### Follow-Up:
- Review exit tickets - LIFO clear?
- Prepare procedures for later this week
- Create stack state diagrams

---

## Handout: Stack Basics Guide

```
╔════════════════════════════════════════════╗
║           STACK BASICS GUIDE               ║
╠════════════════════════════════════════════╣
║                                            ║
║  WHAT IS A STACK?                          ║
║  • LIFO: Last In, First Out                ║
║  • Like a stack of plates                  ║
║  • Add to top (PUSH)                       ║
║  • Remove from top (POP)                   ║
║                                            ║
║  STACK OPERATIONS:                         ║
║                                            ║
║  PUSH register                             ║
║  └─> Saves register value on stack        ║
║      Register value unchanged              ║
║      Stack pointer decremented             ║
║                                            ║
║  POP register                              ║
║  └─> Loads top stack value into register  ║
║      Stack pointer incremented             ║
║                                            ║
║  VISUAL EXAMPLE:                           ║
║                                            ║
║  LOAD A, 10                                ║
║  PUSH A        Stack: [10]                 ║
║                                            ║
║  LOAD B, 20                                ║
║  PUSH B        Stack: [10, 20]             ║
║                                            ║
║  POP C         C=20, Stack: [10]           ║
║  POP D         D=10, Stack: []             ║
║                                            ║
║  KEY RULES:                                ║
║  1. LIFO order (reverse of PUSH)           ║
║  2. Balance PUSH and POP                   ║
║  3. Don't POP empty stack                  ║
║  4. Stack grows downward in memory         ║
║                                            ║
║  COMMON PATTERNS:                          ║
║                                            ║
║  Save/Restore:                             ║
║  PUSH A        ; Save                      ║
║  ; ... use A for other things              ║
║  POP A         ; Restore                   ║
║                                            ║
║  Reverse Order:                            ║
║  PUSH A                                    ║
║  PUSH B                                    ║
║  PUSH C                                    ║
║  POP D         ; D=C                       ║
║  POP E         ; E=B                       ║
║  POP F         ; F=A                       ║
║                                            ║
║  WHEN TO USE STACK:                        ║
║  ✓ Temporary value storage                 ║
║  ✓ Preserve registers during calculations  ║
║  ✓ Reverse order of items                  ║
║  ✓ Function calls (next week!)             ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-DA-10: Evaluate the tradeoffs in how data elements are organized
- 3A-AP-13: Create prototypes using algorithms

**Learning Objectives**:
- LO2.1: Write functional assembly programs
- LO1.3: Trace data flow through stack
- LO4.4: Design data structures using stack

---

*End of Week 5, Day 1 Lesson Plan*
