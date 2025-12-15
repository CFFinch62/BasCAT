# Week 3, Day 4: Logic Operations Applications

**Topic**: Real-World Bit Manipulation and Pattern Creation
**Duration**: 50 minutes
**Learning Objectives**:
- Apply logic operations to solve real problems
- Create visual bit patterns
- Implement practical bit manipulation algorithms
- Optimize bit operations

---

## Materials

- Computers with BasCAT
- Homework from Day 3
- Handout: "Bit Manipulation Cookbook"
- Example: Color manipulation demo

---

## Lesson Outline

### Warm-Up: Real-World Problem (7 min)

**The Permission System Challenge**:
"You're building a file system. Each file has 3 permissions stored in one byte:
- Bit 0: Read (1)
- Bit 1: Write (2)
- Bit 2: Execute (4)"

**Tasks**:
1. Grant all permissions
2. Check if user has write permission
3. Revoke execute permission

**Solution Discussion**: Use OR to grant, AND to check, AND+NOT to revoke

### Direct Instruction: Practical Patterns (12 min)

**Pattern 1: Testing Specific Bits**
```assembly
; Check if bit 3 is set in value
LOAD A, 45         ; Test value
AND A, 8           ; Mask for bit 3
; If A != 0, bit 3 was set
OUT A
HALT
```

**Pattern 2: Setting Multiple Bits**
```assembly
; Set bits 1, 3, 5 in value 0
LOAD A, 0
OR A, 2            ; Bit 1
OR A, 8            ; Bit 3
OR A, 32           ; Bit 5
OUT A              ; Result: 42
HALT
```

**Pattern 3: Clearing Specific Bits**
```assembly
; Clear bit 7 from value 255
LOAD A, 255
LOAD B, 128        ; Bit to clear
NOT B              ; Create clearing mask
AND A, B           ; Clear the bit
OUT A              ; Result: 127
HALT
```

**Pattern 4: Toggling Bits**
```assembly
; Toggle bit 4 repeatedly
LOAD A, 0
XOR A, 16          ; Toggle on
OUT A              ; 16
XOR A, 16          ; Toggle off
OUT A              ; 0
HALT
```

**Pattern 5: Extracting Nibbles**
```assembly
; Extract and swap nibbles
LOAD A, 0xAB       ; 10101011
MOV B, A
AND A, 0x0F        ; Lower nibble = 11 (0xB)
AND B, 0xF0        ; Upper nibble = 160 (0xA0)
OUT A
OUT B
HALT
```

### Guided Practice: Build a Bit Toolkit (15 min)

**Challenge 1: Permission Manager**
```assembly
; Start with no permissions
LOAD A, 0

; Grant read (bit 0)
OR A, 1
OUT A              ; 1

; Grant write (bit 1)
OR A, 2
OUT A              ; 3

; Check if has execute (bit 2)
MOV B, A
AND B, 4
OUT B              ; 0 (no execute)

; Grant execute
OR A, 4
OUT A              ; 7 (all permissions)

HALT
```

**Challenge 2: Color Channel Extraction**
Simulate extracting RGB from a byte (simplified):
```assembly
; Color byte: RRGGBBXX (2 bits each)
LOAD A, 0b11100100  ; Sample color

; Extract red (bits 6-7)
MOV B, A
AND B, 0b11000000
OUT B              ; Red channel

; Extract green (bits 4-5)
MOV B, A
AND B, 0b00110000
OUT B              ; Green channel

; Extract blue (bits 2-3)
AND A, 0b00001100
OUT A              ; Blue channel

HALT
```

**Challenge 3: Bit Counter**
Count how many bits are set (simplified version):
```assembly
; Count bits in value 7 (0b00000111)
; Expected: 3 bits set

LOAD A, 7
LOAD B, 0          ; Counter

; Check bit 0
MOV C, A
AND C, 1
ADD B, C           ; Add 1 if set

; Check bit 1
MOV C, A
AND C, 2
; (Bit 1 is worth 2, but we want count 1)
; Simplified: just checking

; Repeat for other bits...
; (Full version would be complex)

OUT B              ; Partial count
HALT
```

### Independent Practice: Create Your Application (12 min)

**Choose a Project**:

**Level 1**: Bit Flag System
Create system with 4 flags (bits 0-3):
- Set flags on/off
- Check if any flag is set
- Count set flags

**Level 2**: Simple Encryption
```assembly
; XOR cipher
IN A               ; Message
IN B               ; Key
XOR A, B           ; Encrypt
OUT A

XOR A, B           ; Decrypt
OUT A              ; Original
HALT
```

**Level 3**: Bit Pattern Generator
Create these patterns in sequence:
- 0b00000001
- 0b00000011
- 0b00000111
- 0b00001111
(Each adds one more bit)

### Class Discussion: Optimization and Efficiency (6 min)

**Question**: "Which is better?"

**Method 1**: Multiple ORs
```assembly
LOAD A, 0
OR A, 1
OR A, 2
OR A, 4
```

**Method 2**: Single OR
```assembly
LOAD A, 0
OR A, 7      ; Sets bits 0, 1, 2 at once
```

**Answer**: Method 2 is more efficient!

**Optimization Tips**:
1. Combine operations when possible
2. Use appropriate operation for task
3. Minimize register usage
4. Pre-calculate masks when possible

**Real Impact**: "In graphics engines, these optimizations happen billions of times per second!"

---

## Closure / Exit Ticket (5 min)

Write code to:
"Set bits 0 and 7 in value 0, output result"

**Expected**:
```assembly
LOAD A, 0
OR A, 129      ; 128 + 1
OUT A
HALT
```

**Preview Tomorrow**: "Lab Day! Create a complete bit manipulation tool!"

---

## Homework

**Program 1**: Permission Checker
```assembly
; Check if value has read AND write permissions
; Read = bit 0, Write = bit 1
IN A               ; Get permissions byte
MOV B, A
AND B, 3           ; Check bits 0 and 1
OUT B              ; If 3, has both
HALT
```

**Program 2**: Bit Flipper
```assembly
; Flip specific bits based on input
IN A               ; Value
IN B               ; Bits to flip (mask)
XOR A, B
OUT A
HALT
```

**Challenge**: Create a program that uses all 4 logic operations to transform input value through multiple stages, outputting after each stage.

**Due**: Tomorrow (for lab reference)

---

## Assessment

**Formative**:
- Application creation
- Optimization understanding
- Real-world problem solving

**Success Criteria**:
- Can apply logic operations to practical problems
- Can choose appropriate operation for task
- Can optimize bit manipulation code

---

## Differentiation

**Struggling**: Provide templates, simpler patterns
**Advanced**: Complex applications, efficiency challenges
**ELL**: Visual diagrams, real-world examples

---

## Teacher Notes

**Common Issues**:
- Choosing wrong operation for task
- Not understanding when to optimize
- Difficulty with multi-step patterns

**Time Savers**:
- Have pattern solutions ready
- Pre-test all examples
- Calculator for verification

**Key Concepts**:
- Right tool for the job
- Optimization matters
- Real applications exist

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-AP-17
**LO**: LO4.2, LO4.3

---

*End of Week 3, Day 4 Lesson Plan*
