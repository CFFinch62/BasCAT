# Week 3, Day 1: Binary Basics & AND Operation

**Topic**: Understanding Binary and the AND Instruction
**Duration**: 50 minutes
**Learning Objectives**:
- Understand binary number representation
- Convert between decimal and binary (simple cases)
- Use AND instruction for bit masking
- Understand truth tables for AND

---

## Materials Needed

- Computers with BasCAT
- Week 2 quiz (graded, ready to return)
- Handout: "Binary Basics Chart"
- Binary counting manipulatives (optional - cards with 0/1)
- Truth table posters

---

## Lesson Outline

### Warm-Up / Week 2 Recap & Binary Introduction (8 minutes)

**Return Week 2 Quiz**:
- Hand back graded quizzes
- Quick review of common errors
- "Any questions about arithmetic or I/O?"

**The Computer's Secret**:

"Pop quiz: What language do computers REALLY speak?"
- Students might say: "Assembly!" "Code!" "Python!"
- **Answer**: "Binary! Just 0s and 1s."

**Demo on Paper**:
"How do YOU count? 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, then what?"
- Start over with 10 (two digits)
- **We use 10 symbols** (0-9)

"Computers only have TWO symbols: 0 and 1"
- 0, 1, then what? 10! (one-zero, not ten)
- This is BINARY (base 2)

**Quick Binary Count**:
```
Decimal: 0  1  2  3  4   5   6   7   8
Binary:  0  1  10 11 100 101 110 111 1000
```

"Each position is a power of 2!"

### Direct Instruction: Binary Numbers (12 minutes)

**Understanding Binary**:

"In decimal, each position is worth 10× more:
- Ones place (10⁰ = 1)
- Tens place (10¹ = 10)  
- Hundreds place (10² = 100)"

"In binary, each position is worth 2× more:"

**8-Bit Binary Chart** (write on board):
```
Position: 7    6    5    4    3    2    1    0
Value:    128  64   32   16   8    4    2    1
Binary:   ?    ?    ?    ?    ?    ?    ?    ?
```

**Example: Decimal 25 → Binary**
```
25 = 16 + 8 + 1
Position: 7  6  5  4  3  2  1  0
Value:    128 64 32 16 8  4  2  1
Binary:   0  0  0  1  1  0  0  1
                   ↑  ↑     ↑
                   16 8     1  = 25
```

**Binary: 00011001 = 25 in decimal**

**Practice Together**:
"What's binary 00001111 in decimal?"
```
Position: 7  6  5  4  3  2  1  0
Value:    128 64 32 16 8  4  2  1
Binary:   0  0  0  0  1  1  1  1
                      ↑  ↑  ↑  ↑
                      8  4  2  1  = 15
```

**Why This Matters for Programming**:
"When we write `LOAD A, 15` in BasCAT, the computer stores it as `00001111`!"

**Binary in BasCAT**:
"You can write binary directly in BasCAT using 0b prefix:"
```assembly
LOAD A, 0b00001111    ; Same as LOAD A, 15
LOAD B, 0b11110000    ; Same as LOAD B, 240
```

### The AND Operation (Introduction)

**What is AND?**

"AND compares two binary values bit-by-bit:
- If BOTH bits are 1 → Result is 1
- Otherwise → Result is 0"

**Truth Table for AND**:
```
A | B | A AND B
--|---|--------
0 | 0 |   0
0 | 1 |   0
1 | 0 |   0
1 | 1 |   1    ← Only when BOTH are 1!
```

**Example**:
```
  11110000  (240)
& 00001111  (15)
  --------
  00000000  (0)
```

"No positions have 1 in BOTH, so result is all 0s!"

**Another Example**:
```
  11111111  (255)
& 00001111  (15)
  --------
  00001111  (15)
```

"Bottom 4 bits match, so they stay 1!"

**The AND Instruction in BasCAT**:

**Syntax**:
```assembly
AND register, value
```

**Example**:
```assembly
LOAD A, 0b11110000    ; A = 240
AND A, 0b00001111     ; A = 0 (no matching 1s)
OUT A
HALT
```

**Circuit Focus**:
- Run in BasCAT
- Watch ALU perform AND operation
- See result return to register

### Guided Practice: AND Operations (15 minutes)

**Challenge 1: Simple AND** (5 min)

"What's the result?"
```assembly
LOAD A, 0b11111111
AND A, 0b11110000
OUT A
HALT
```

Work it out on paper first, then test!

**Answer**: 
```
  11111111  (255)
& 11110000  (240)
  --------
  11110000  (240)
```

**Challenge 2: Masking** (5 min)

"The most common use of AND: MASKING (keeping only certain bits)"

**Problem**: "You have the value 0b11010110. Keep only the lower 4 bits (right side), zero out the upper 4 bits."

**Solution**:
```assembly
LOAD A, 0b11010110    ; Original value
AND A, 0b00001111     ; Mask (keep lower 4)
OUT A                 ; Should output 6 (0b00000110)
HALT
```

**Visual**:
```
  11010110  (Original)
& 00001111  (Mask)
  --------
  00000110  (Result = 6)
```

**Challenge 3: Practical Application** (5 min)

"Network subnet masks use AND! Simplified example:"

```assembly
; IP address (simplified): 192
; Subnet mask: 240 (keep network part)
LOAD A, 192           ; 11000000
AND A, 240            ; 11110000
OUT A                 ; Network address
HALT
```

**Test and Verify**:
```
  11000000  (192)
& 11110000  (240)
  --------
  11000000  (192)
```

"This is how routers determine if two devices are on same network!"

### Independent Practice: AND Challenges (10 minutes)

**Choose Your Level**:

**Level 1 - Basic: Extract Bits**
Write programs for these:
1. Value 255, keep lower 4 bits (mask with 15)
2. Value 170 (0b10101010), keep upper 4 bits (mask with 240)

**Level 2 - Intermediate: Multiple Masks**
```assembly
; Start with value 0b11111111
; Apply three different masks
; Output after each mask
LOAD A, 0b11111111
OUT A                 ; 255

AND A, 0b11110000
OUT A                 ; ?

AND A, 0b11000000
OUT A                 ; ?

HALT
```

**Level 3 - Advanced: Permission System**
```assembly
; Simulate file permissions (simplified)
; Bit 0 = Read, Bit 1 = Write, Bit 2 = Execute
; User has: 0b00000111 (all permissions)
; Check if user can Write (bit 1)

LOAD A, 0b00000111    ; User permissions
AND A, 0b00000010     ; Check write bit
OUT A                 ; If result != 0, has write permission
HALT
```

**Expected Output (Level 3)**: 2 (0b00000010 - yes, has write!)

### Class Discussion: Why AND Matters (5 minutes)

**Real-World Uses of AND**:

1. **Bit Masking** (extracting specific bits)
   - Graphics: Extract color channels
   - Networking: Subnet calculations
   - Permissions: Check access rights

2. **Testing Bits** (checking if specific bits are set)
   - Keyboard input: Which keys pressed?
   - Device status: Is device ready?
   - Flags: Is error flag set?

3. **Security** (combining permissions)
   - User has permission X AND permission Y?
   - Both conditions must be true

**Interactive Question**:
"If you have value 0b10101010 and mask with 0b11110000, what do you get?"

**Work it out together**:
```
  10101010  (170)
& 11110000  (240)
  --------
  10100000  (160)
```

**Key Insight**:
"AND with 0 always gives 0 (erases bits)
AND with 1 keeps the original bit (preserves bits)"

---

## Closure / Exit Ticket (5 minutes)

**Quick Assessment**:

On paper:
1. What's binary 00001010 in decimal? (Answer: 10)
2. Calculate: 0b11110000 AND 0b00001111 (Answer: 0)
3. Write code to load 200, AND with 15, output result

**Expected Answer #3**:
```assembly
LOAD A, 200
AND A, 15
OUT A
HALT
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"Tomorrow: OR and XOR! OR sets bits, XOR flips bits. You'll create PATTERNS!"

---

## Homework

**Assignment**: "Bit Masking Practice"

**Program 1**: Lower Nibble Extractor
```assembly
; Extract lower 4 bits from 173
; 173 = 0b10101101
; Lower 4 bits = 0b00001101 = 13
LOAD A, 173
AND A, 15         ; Mask: 0b00001111
OUT A             ; Should output 13
HALT
```

**Program 2**: Upper Nibble Extractor
```assembly
; Extract upper 4 bits from 173
; Need to mask with 240 (0b11110000)
LOAD A, 173
AND A, 240
OUT A             ; Should output 160
HALT
```

**Program 3**: Bit Testing
```assembly
; Test if bit 5 is set in value 100
; Mask: 0b00100000 (32)
LOAD A, 100
AND A, 32
OUT A             ; If != 0, bit 5 is set
HALT
```

**Challenge**: Create a program that takes binary 11111111 and progressively masks it:
- Mask with 254 (all but bit 0)
- Mask with 252 (all but bits 0-1)
- Mask with 248 (all but bits 0-2)
Output after each mask

**Due**: Next class
**Submit**: `week3_day1_homework.asm`

---

## Assessment

### Formative:
- ✓ Exit ticket (binary conversion, AND operation)
- ✓ Guided practice observation
- ✓ Independent practice completion
- ✓ Class discussion participation

### Success Criteria:
- Student can convert simple binary to decimal
- Student understands AND truth table
- Student can use AND for bit masking
- Student can write AND instruction correctly

---

## Differentiation

### For Struggling Students:
- **Binary Chart**: Provide filled-out chart
- **Calculator**: Allow binary/decimal converter
- **Skip Conversion**: Focus on AND operation only
- **Simpler Values**: Use only 0-15 (4 bits)

### For Advanced Students:
- **16-bit Challenge**: Work with larger values
- **Complex Masks**: Multiple sequential masks
- **Real Applications**: Research subnet masking
- **Optimization**: Achieve result with fewer operations

### For ELL Students:
- **Vocabulary**: Binary, bit, mask, nibble, truth table
- **Visual**: Binary chart always visible
- **Sentence Frames**:
  - "AND keeps bits where both are ___"
  - "Masking means ___"
- **Bilingual**: Binary is universal!

---

## Teacher Notes

### Common Errors:

1. **"Binary is too hard!"**
   - Start with small numbers (0-15)
   - Use visual charts
   - Don't require memorization, allow reference

2. **"I don't understand AND"**
   - Use truth table
   - Physical demo: Two switches both on
   - "Both must be 1"

3. **"Why 0b prefix?"**
   - Explain: Tells computer "this is binary"
   - Can also use decimal if easier

4. **"Masking confuses me"**
   - Analogy: Stencil covers parts, reveals others
   - Draw visual diagram

### Time Management:
- If running short: Skip Level 3 practice
- If running long: Reduce binary basics time
- Don't get bogged down in binary conversion

### Setup:
- [ ] Binary chart posters on wall
- [ ] Truth table visible
- [ ] Test AND examples before class
- [ ] Calculator for verification

### Follow-Up:
- Review exit tickets - binary understanding?
- Prepare OR/XOR for tomorrow
- Have pattern examples ready

---

## Handout: Binary Basics Chart

```
╔════════════════════════════════════════════╗
║         BINARY BASICS REFERENCE            ║
╠════════════════════════════════════════════╣
║                                            ║
║  8-BIT BINARY POSITIONS:                   ║
║  ┌───┬───┬───┬───┬───┬───┬───┬───┐        ║
║  │128│ 64│ 32│ 16│ 8 │ 4 │ 2 │ 1 │        ║
║  ├───┼───┼───┼───┼───┼───┼───┼───┤        ║
║  │ ? │ ? │ ? │ ? │ ? │ ? │ ? │ ? │        ║
║  └───┴───┴───┴───┴───┴───┴───┴───┘        ║
║   Bit 7 6  5  4  3  2  1  0                ║
║                                            ║
║  COMMON CONVERSIONS:                       ║
║  Decimal │ Binary                          ║
║  ────────┼──────────                       ║
║     0    │ 00000000                        ║
║     1    │ 00000001                        ║
║     15   │ 00001111                        ║
║     16   │ 00010000                        ║
║     255  │ 11111111                        ║
║                                            ║
║  QUICK REFERENCE:                          ║
║  • Lower 4 bits: AND with 15 (00001111)    ║
║  • Upper 4 bits: AND with 240 (11110000)   ║
║  • Bit 0: AND with 1                       ║
║  • Bit 7: AND with 128                     ║
║                                            ║
║  AND TRUTH TABLE:                          ║
║  ┌───┬───┬───────┐                         ║
║  │ A │ B │ A & B │                         ║
║  ├───┼───┼───────┤                         ║
║  │ 0 │ 0 │   0   │                         ║
║  │ 0 │ 1 │   0   │                         ║
║  │ 1 │ 0 │   0   │                         ║
║  │ 1 │ 1 │   1   │ ← Both must be 1        ║
║  └───┴───┴───────┘                         ║
║                                            ║
║  IN BASCAT:                                ║
║  LOAD A, 0b11110000  ; Binary literal      ║
║  AND A, 0b00001111   ; Mask operation      ║
║  OUT A               ; Result              ║
║                                            ║
║  MASKING CONCEPT:                          ║
║  • 0 in mask → bit becomes 0 (erase)       ║
║  • 1 in mask → bit unchanged (keep)        ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-DA-09: Translate between representations
- 3A-AP-13: Create prototypes using algorithms

**Learning Objectives**:
- LO4.2: Implement algorithms efficiently
- LO2.1: Write functional assembly programs
- LO5.1: Explain abstraction layers

---

*End of Week 3, Day 1 Lesson Plan*
