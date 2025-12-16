# Week 3, Day 2: OR and XOR Operations

**Topic**: Setting and Toggling Bits with OR and XOR
**Duration**: 50 minutes
**Learning Objectives**:
- Use OR instruction to set bits
- Use XOR instruction to toggle bits
- Understand truth tables for OR and XOR
- Create bit patterns using logic operations

---

## Materials Needed

- Computers with BasCAT
- Homework from Day 1
- Handout: "Logic Operations Comparison Chart"
- Light switch demo (optional - for XOR concept)

---

## Lesson Outline

### Warm-Up / AND Review (7 minutes)

**Homework Quick Check**:
- "Who successfully extracted the lower nibble from 173?"
- Expected output: 13
- Review the concept: "AND masks/keeps specific bits"

**Quick AND Quiz**:
Show on board:
```
  10101010
& 11110000
  --------
  ????????
```

Students calculate: Answer = 10100000

**Bridge to Today**:
"Yesterday: AND erases bits (sets them to 0)
Today: OR sets bits (makes them 1), XOR flips bits!"

### Direct Instruction: OR Operation (12 minutes)

**The OR Operation**:

"OR compares bits and asks: Is AT LEAST ONE a 1?"

**Truth Table for OR**:
```
A | B | A OR B
--|---|-------
0 | 0 |   0    ← Only 0 when BOTH are 0
0 | 1 |   1
1 | 0 |   1
1 | 1 |   1
```

"If EITHER bit is 1 (or both), result is 1!"

**Example**:
```
  00001111  (15)
| 11110000  (240)
  --------
  11111111  (255)
```

"Combined all the 1s from both numbers!"

**Another Example**:
```
  10101010  (170)
| 01010101  (85)
  --------
  11111111  (255)
```

**The OR Instruction in BasCAT**:

**Syntax**:
```assembly
OR register, value
```

**Example**:
```assembly
LOAD A, 0b00001111    ; A = 15
OR A, 0b11110000      ; A = 255
OUT A
HALT
```

**Setting Specific Bits**:

"OR is perfect for SETTING bits (making them 1)!"

**Example**: "Turn on bit 5 in value 0b00000011"
```assembly
LOAD A, 0b00000011    ; Original: 3
OR A, 0b00100000      ; Set bit 5 (value 32)
OUT A                 ; Result: 35
HALT
```

**Visual**:
```
  00000011  (Original)
| 00100000  (Bit 5)
  --------
  00100011  (Result = 35)
```

**Key Insight**:
"OR with 0 keeps original bit
OR with 1 sets bit to 1 (regardless of original)"

### Direct Instruction: XOR Operation (12 minutes)

**The XOR (Exclusive OR) Operation**:

"XOR asks: Are the bits DIFFERENT?"

**Truth Table for XOR**:
```
A | B | A XOR B
--|---|--------
0 | 0 |   0
0 | 1 |   1    ← Different? Yes!
1 | 0 |   1    ← Different? Yes!
1 | 1 |   0    ← Same? Result is 0
```

"Result is 1 only when bits are DIFFERENT!"

**Example**:
```
  11110000  (240)
^ 00001111  (15)
  --------
  11111111  (255)
```

**Same Value XOR**:
```
  10101010  (170)
^ 10101010  (170)
  --------
  00000000  (0)
```

"XORing a value with itself gives 0!"

**The XOR Instruction in BasCAT**:

**Syntax**:
```assembly
XOR register, value
```

**Toggling Bits**:

"XOR is perfect for FLIPPING/TOGGLING bits!"

**Example**: "Flip all bits (invert)"
```assembly
LOAD A, 0b10101010    ; A = 170
XOR A, 0b11111111     ; Flip all bits
OUT A                 ; Result: 85
HALT
```

**Visual**:
```
  10101010  (Original)
^ 11111111  (Flip all)
  --------
  01010101  (Result = 85)
```

**Selective Toggle**:
```assembly
LOAD A, 0b00000000    ; Start with 0
XOR A, 0b00000011     ; Flip bits 0-1
OUT A                 ; Result: 3

XOR A, 0b00000011     ; Flip again
OUT A                 ; Result: 0 (back to original!)
HALT
```

**Light Switch Analogy**:
"XOR is like a light switch:
- First XOR: Turns on
- Second XOR: Turns off
- Toggles back and forth!"

**Key Insight**:
"XOR with 0 keeps original bit
XOR with 1 flips bit"

### Guided Practice: OR and XOR (15 minutes)

**Challenge 1: OR Practice** (5 min)

"Set bits 0, 1, and 2 in value 0b00000000"

**Solution**:
```assembly
LOAD A, 0b00000000    ; Start with 0
OR A, 0b00000111      ; Set bits 0-2
OUT A                 ; Should output 7
HALT
```

**Challenge 2: XOR Toggle** (5 min)

"Create a blinking pattern - toggle bits back and forth"

**Solution**:
```assembly
LOAD A, 0b00000000
XOR A, 0b11111111     ; All on
OUT A                 ; 255

XOR A, 0b11111111     ; All off
OUT A                 ; 0

XOR A, 0b11111111     ; All on again
OUT A                 ; 255
HALT
```

**Challenge 3: Combining Operations** (5 min)

"Start with 0b10101010:
1. OR with 0b00001111 (set lower 4 bits)
2. XOR with 0b11111111 (flip all bits)
Output after each step"

**Solution**:
```assembly
LOAD A, 0b10101010    ; 170
OUT A

OR A, 0b00001111      ; Set lower 4
OUT A                 ; 175

XOR A, 0b11111111     ; Flip all
OUT A                 ; 80
HALT
```

**Verify**:
```
Step 1: 10101010 (170)
Step 2: 10101111 (175) after OR
Step 3: 01010000 (80) after XOR
```

### Independent Practice: Pattern Creation (10 minutes)

**Choose Your Level**:

**Level 1 - Basic: Simple Patterns**
Create programs that output these sequences:
1. 0 → 255 (using OR to set all bits)
2. 255 → 0 (using XOR to flip all bits)

**Level 2 - Intermediate: Bit Manipulation**
Start with 0b00000000:
- Set bit 7 (OR with 128)
- Set bit 0 (OR with 1)
- Toggle bit 7 (XOR with 128)
Output after each operation

**Expected outputs**: 128, 129, 1

**Level 3 - Advanced: Encryption**
Simple XOR encryption:
```assembly
; "Encrypt" value 65 (ASCII 'A')
; Using key 42
LOAD A, 65
XOR A, 42             ; Encrypted
OUT A

XOR A, 42             ; Decrypt (XOR again with same key!)
OUT A                 ; Should output 65 again
HALT
```

"This is how simple XOR encryption works - XOR twice returns original!"

### Class Discussion: Logic Operations Summary (6 minutes)

**Comparison Table**:

| Operation | Purpose | When Result = 1 |
|-----------|---------|-----------------|
| AND | Mask/Keep bits | Both bits are 1 |
| OR | Set bits | At least one bit is 1 |
| XOR | Toggle bits | Bits are different |

**Use Cases**:

**AND**:
- Extract specific bits
- Check if bits are set
- Subnet masks

**OR**:
- Set specific bits
- Combine flags
- Build up values

**XOR**:
- Toggle bits on/off
- Simple encryption
- Swap values (advanced)
- Check if values are different

**Interactive Question**:
"You want to turn ON bit 3 in value 0b00000000. Which operation?"

**Answer**: OR with 0b00001000 (value 8)

**Why?**
```
  00000000  (Original)
| 00001000  (Set bit 3)
  --------
  00001000  (Result)
```

**Real-World Connection**:
"Graphics programs use these constantly:
- AND: Extract color channels (red, green, blue)
- OR: Combine colors
- XOR: Create special effects
- Game pixels use bit operations millions of times per second!"

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper:
1. What's 0b11110000 OR 0b00001111? (Answer: 11111111)
2. What's 0b10101010 XOR 0b11111111? (Answer: 01010101)
3. Write code to set bit 7 in value 0

**Expected Answer #3**:
```assembly
LOAD A, 0
OR A, 128      ; Set bit 7
OUT A
HALT
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"Tomorrow: NOT operation (invert all bits) and combining ALL four logic operations!"

---

## Homework

**Assignment**: "Logic Operations Practice"

**Program 1**: Bit Builder
```assembly
; Build up value from 0 using OR
LOAD A, 0
OR A, 1        ; Set bit 0
OR A, 2        ; Set bit 1
OR A, 4        ; Set bit 2
OR A, 8        ; Set bit 3
OUT A          ; Should output 15
HALT
```

**Program 2**: Bit Blinker
```assembly
; Create alternating pattern
LOAD A, 0
XOR A, 255     ; All on
OUT A

XOR A, 255     ; All off
OUT A

XOR A, 170     ; Specific pattern
OUT A

XOR A, 170     ; Back to off
OUT A
HALT
```

**Program 3**: Practical Application
```assembly
; File permissions (simplified)
; Start with no permissions (0)
; Grant read (bit 0)
; Grant write (bit 1)
; Grant execute (bit 2)
; Output final permissions

LOAD A, 0
OR A, 1        ; Read
OR A, 2        ; Write
OR A, 4        ; Execute
OUT A          ; Should be 7 (all permissions)
HALT
```

**Challenge**: Create a program that:
- Starts with 0b00000000
- Uses OR to set bits 0, 2, 4, 6 (checkerboard pattern)
- Uses XOR to flip all bits
- Uses AND to keep only lower 4 bits
- Output after each step

**Due**: Next class
**Submit**: `week3_day2_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (OR, XOR operations)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Truth table understanding

### Success Criteria:
- Student understands OR truth table
- Student understands XOR truth table
- Student can use OR to set bits
- Student can use XOR to toggle bits

---

## Differentiation

### For Struggling Students:
- **Truth Tables**: Always visible reference
- **Simple Values**: Use 0-15 only (4 bits)
- **Visual**: Draw bit-by-bit comparisons
- **Skip XOR**: Focus on OR first

### For Advanced Students:
- **XOR Swap**: Research swapping values using XOR
- **Encryption**: Multi-step XOR encryption
- **Optimization**: Achieve patterns with fewer operations
- **Research**: Gray code, parity bits

### For ELL Students:
- **Vocabulary**: Exclusive, toggle, flip, set, invert
- **Visual Truth Tables**: Color-coded
- **Sentence Frames**:
  - "OR sets bits to ___"
  - "XOR flips bits when ___"
- **Physical Demo**: Light switch for XOR

---

## Teacher Notes

### Common Errors:

1. **"OR and XOR confuse me"**
   - Emphasize difference: OR = "at least one", XOR = "different"
   - Use real examples: OR = "coffee OR tea" (can have both), XOR = "heads XOR tails" (exclusive)

2. **"Why XOR twice returns original?"**
   - Demo with light switch
   - Show mathematically: A XOR B XOR B = A

3. **"When do I use which?"**
   - AND: Keep/check bits
   - OR: Set/turn on bits
   - XOR: Toggle/flip bits

### Time Management:
- If running short: Combine XOR and OR instruction time
- If running long: Add more examples
- Have truth tables always visible

### Setup:
- [ ] Truth table posters
- [ ] Test all examples
- [ ] Print comparison chart
- [ ] Light switch for XOR demo (optional)

### Follow-Up:
- Review exit tickets - OR/XOR understanding?
- Prepare NOT operation for tomorrow
- Plan combined logic operations examples

---

## Handout: Logic Operations Comparison

```
╔════════════════════════════════════════════╗
║      LOGIC OPERATIONS COMPARISON           ║
╠════════════════════════════════════════════╣
║                                            ║
║  AND - Keep/Mask Bits                      ║
║  ┌───┬───┬───────┐                         ║
║  │ A │ B │ A & B │                         ║
║  ├───┼───┼───────┤                         ║
║  │ 0 │ 0 │   0   │                         ║
║  │ 0 │ 1 │   0   │                         ║
║  │ 1 │ 0 │   0   │                         ║
║  │ 1 │ 1 │   1   │ ← Both must be 1        ║
║  └───┴───┴───────┘                         ║
║                                            ║
║  Use: Extract/check specific bits          ║
║  Mask with 0: Erases bit                   ║
║  Mask with 1: Keeps bit unchanged          ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  OR - Set Bits                             ║
║  ┌───┬───┬───────┐                         ║
║  │ A │ B │ A | B │                         ║
║  ├───┼───┼───────┤                         ║
║  │ 0 │ 0 │   0   │                         ║
║  │ 0 │ 1 │   1   │ ← At least one = 1      ║
║  │ 1 │ 0 │   1   │                         ║
║  │ 1 │ 1 │   1   │                         ║
║  └───┴───┴───────┘                         ║
║                                            ║
║  Use: Turn bits ON                         ║
║  OR with 0: Keeps bit unchanged            ║
║  OR with 1: Sets bit to 1                  ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  XOR - Toggle Bits                         ║
║  ┌───┬───┬───────┐                         ║
║  │ A │ B │ A ^ B │                         ║
║  ├───┼───┼───────┤                         ║
║  │ 0 │ 0 │   0   │                         ║
║  │ 0 │ 1 │   1   │ ← Bits different        ║
║  │ 1 │ 0 │   1   │                         ║
║  │ 1 │ 1 │   0   │                         ║
║  └───┴───┴───────┘                         ║
║                                            ║
║  Use: Flip bits on/off                     ║
║  XOR with 0: Keeps bit unchanged           ║
║  XOR with 1: Flips bit                     ║
║                                            ║
║  Special: A XOR B XOR B = A                ║
║  (XOR twice returns original!)             ║
║                                            ║
║ ═══════════════════════════════════════    ║
║                                            ║
║  QUICK EXAMPLES:                           ║
║                                            ║
║  Set bit 5:    OR A, 32                    ║
║  Clear bit 5:  AND A, 223 (NOT 32)         ║
║  Toggle bit 5: XOR A, 32                   ║
║  Check bit 5:  AND A, 32  (if != 0, set)   ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-DA-09: Translate between representations
- 3A-AP-13: Create prototypes using algorithms

**Learning Objectives**:
- LO2.1: Write functional assembly programs
- LO4.2: Implement algorithms efficiently
- LO5.1: Explain abstraction layers

---

*End of Week 3, Day 2 Lesson Plan*
