# Week 3, Day 3: NOT and Combining Logic Operations

**Topic**: Bit Inversion with NOT and Complex Bit Patterns
**Duration**: 50 minutes
**Learning Objectives**:
- Use NOT instruction to invert all bits
- Combine AND, OR, XOR, and NOT in programs
- Create complex bit patterns
- Understand practical applications of bit manipulation

---

## Materials

- Computers with BasCAT
- Homework from Day 2
- Handout: "Complete Logic Operations Reference"

---

## Lesson Outline

### Warm-Up (7 min)

**Homework Review**: OR and XOR patterns
**Bridge**: "We can set bits (OR), toggle bits (XOR), mask bits (AND)... what about INVERTING ALL bits at once?"

### Direct Instruction: NOT Operation (10 min)

**NOT - Bit Inversion**:
```
NOT: Flips every bit
0 → 1
1 → 0
```

**Truth Table**:
```
A | NOT A
--|------
0 |  1
1 |  0
```

**Example**:
```
  10101010  (170)
NOT
  --------
  01010101  (85)
```

**BasCAT Syntax**:
```assembly
NOT register
```

**Example Program**:
```assembly
LOAD A, 0b11110000    ; 240
NOT A                  ; Inverts to 0b00001111
OUT A                  ; Outputs 15
HALT
```

**Key Insight**: "NOT has NO second operand - it operates on entire register!"

**NOT vs XOR All Bits**:
```assembly
; These are equivalent:
LOAD A, 170
NOT A              ; Method 1
; vs
LOAD A, 170
XOR A, 255         ; Method 2 (XOR with all 1s)
```

### Guided Practice: Combining Operations (15 min)

**Challenge 1: Complementary Patterns**
Create two complementary patterns (opposites):
```assembly
LOAD A, 0b10101010
OUT A              ; 170
MOV B, A
NOT B
OUT B              ; 85 (complement)
HALT
```

**Challenge 2: Clear Specific Bits**
"Clear bits 0-3 (set them to 0) using AND and NOT"
```assembly
LOAD A, 255        ; All 1s
LOAD B, 15         ; Bits to clear (0b00001111)
NOT B              ; B = 0b11110000 (mask)
AND A, B           ; Clear lower 4 bits
OUT A              ; 240
HALT
```

**Challenge 3: Complex Pattern**
Step-by-step pattern creation:
```assembly
LOAD A, 0          ; Start with 0
OR A, 0b00001111   ; Set lower nibble (15)
XOR A, 0b10101010  ; Toggle specific bits (175)
AND A, 0b11110000  ; Keep upper nibble (160)
NOT A              ; Invert all (95)
OUT A
HALT
```

### Independent Practice: Bit Pattern Challenges (12 min)

**Level 1 - Basic**:
Create alternating patterns:
- Start: 0
- Set every other bit (0,2,4,6)
- Output result

**Level 2 - Intermediate**:
```assembly
; Create "checkerboard" then invert
LOAD A, 0
OR A, 0b01010101   ; Checkerboard
OUT A
NOT A              ; Inverted checkerboard
OUT A
HALT
```

**Level 3 - Advanced**:
Create a "bit carousel":
- Start with 0b00000001
- Shift pattern using logic operations
- Create sequence: 1, 3, 7, 15, 31, 63, 127, 255

### Class Discussion: Practical Applications (6 min)

**Real-World Uses**:
1. **Graphics**: Color inversion (NOT)
2. **Encryption**: XOR cipher
3. **Permissions**: Set/check/clear access rights
4. **Network**: Subnet masks (AND)
5. **Compression**: Pattern detection

**Interactive**: "Design a simple permission system using bits"
- Bit 0: Read
- Bit 1: Write
- Bit 2: Execute

Show how to grant, revoke, check permissions using logic operations.

---

## Closure / Exit Ticket (5 min)

Write code to:
1. Start with 0b11110000
2. Invert all bits
3. Output result

**Expected**: 15

**Preview Tomorrow**: "Putting it all together - create visual patterns and solve real problems!"

---

## Homework

**Program 1**: Complete Inversion
```assembly
LOAD A, 100
OUT A
NOT A
OUT A          ; Output complement
HALT
```

**Program 2**: Bit Mask Creator
Create a mask for bits 2, 4, 6:
```assembly
LOAD A, 0
OR A, 4        ; Bit 2
OR A, 16       ; Bit 4
OR A, 64       ; Bit 6
OUT A          ; Mask (84)
NOT A          ; Inverted mask
OUT A          ; Output both
HALT
```

**Challenge**: Use all 4 operations (AND, OR, XOR, NOT) in one program to create pattern 0b10110110.

**Due**: Next class

---

## Assessment

**Formative**:
- Exit ticket (NOT operation)
- Pattern creation observation
- Combined operations understanding

**Success Criteria**:
- Can use NOT correctly
- Can combine multiple logic operations
- Understands bit manipulation applications

---

## Differentiation

**Struggling**: Focus on NOT only, skip combinations
**Advanced**: Multi-step patterns, encryption, optimization
**ELL**: Visual patterns, binary chart reference

---

## Teacher Notes

**Common Errors**:
- Forgetting NOT has no second operand
- Confusing NOT with XOR 255 (they're equivalent!)
- Wrong order of operations

**Time Savers**:
- Pre-calculate expected outputs
- Have visual patterns ready
- Binary calculator for verification

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-DA-09
**LO**: LO2.1, LO4.2

---

*End of Week 3, Day 3 Lesson Plan*
