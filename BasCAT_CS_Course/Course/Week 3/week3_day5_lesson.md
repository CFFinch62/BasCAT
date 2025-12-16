# Week 3, Day 5: Lab Day - Bit Manipulation Tool

**Topic**: Week 3 Capstone Project - Create a Bit Tool
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all logic operations in complete program
- Create useful bit manipulation utility
- Document bitwise algorithms
- Demonstrate mastery of Week 3 concepts

---

## Materials

- Computers with BasCAT
- Project rubric (printed)
- Handout: "Bit Tool Project Spec"

---

## Lab Project: Bit Manipulation Tool

### Project Description

Create a comprehensive bit manipulation utility demonstrating all four logic operations.

**Core Requirements**:
1. Uses all 4 operations: AND, OR, XOR, NOT
2. Interactive (uses IN for user input)
3. Produces meaningful output
4. Well-documented with binary explanations
5. Includes bit pattern demonstrations

---

## Lesson Outline

### Project Launch (10 min)

**Project Options** (students choose one):

**Option 1: Bit Pattern Generator**
- Takes input value
- Demonstrates all 4 operations on it
- Shows binary patterns
- Outputs results of each operation

**Option 2: Permission Manager**
- Grant permissions (OR)
- Check permissions (AND)
- Revoke permissions (AND + NOT)
- Toggle permissions (XOR)
- Full CRUD for bit flags

**Option 3: Simple Encryption Tool**
- Input message byte
- Input key byte
- Encrypt with XOR
- Decrypt with XOR
- Demonstrate reversibility

**Option 4: Bit Mask Creator**
- Create custom masks
- Apply masks to values
- Show masking effects
- Multiple mask operations

**Example - Pattern Generator**:
```assembly
; Bit Pattern Tool
; Shows all operations on input value

IN A               ; Get value from user
MOV B, A           ; Save original

; Demonstrate AND
AND A, 0b11110000  ; Mask upper nibble
OUT A              ; Show result

; Demonstrate OR
MOV A, B           ; Restore
OR A, 0b00001111   ; Set lower nibble
OUT A

; Demonstrate XOR
MOV A, B
XOR A, 0b11111111  ; Flip all
OUT A

; Demonstrate NOT
MOV A, B
NOT A
OUT A

; Show original
OUT B

HALT
```

**Requirements** (write on board):
```
□ All 4 logic operations used
□ Interactive (IN instruction)
□ At least 4 different outputs
□ Comments explaining operations
□ Binary values documented
□ Working demonstration
```

### Independent Work Time (35 min)

**Students Work** on chosen project

**Teacher Circulates**:

**First 10 minutes**:
- Verify students chose appropriate project
- Check planning/design
- Ensure all 4 operations will be used

**Middle 15 minutes**:
- Debug logic errors
- Help with binary calculations
- Verify operations are correct
- Encourage testing

**Final 10 minutes**:
- Ensure programs run
- Check documentation
- Verify all requirements met
- Push for polish/extras

**Common Support Needs**:

1. **"How do I use all 4?"**
   - AND: Mask/extract
   - OR: Set bits
   - XOR: Toggle bits
   - NOT: Invert all

2. **"What should I output?"**
   - Result of each operation
   - Original value for comparison
   - Intermediate steps
   - Binary representation (as decimal)

3. **"My binary math is wrong!"**
   - Use binary calculator
   - Work through step-by-step
   - Verify with simple values (like 15, 255)

**Differentiation**:

**Struggling**:
- Provide template
- Reduce to 3 operations
- Simpler values (0-15)
- Allow partner work

**On-Level**:
- Complete all requirements
- Good documentation
- Working demonstration

**Advanced**:
- Complex application
- Multiple inputs
- Optimization
- Creative functionality
- Help others

---

## Week 3 Quiz (if time, or next class) (10 min)

**Sample Questions** (25 points):

1. Convert 0b00001111 to decimal (2 pts)
2. What's 0b11110000 AND 0b00001111? (3 pts)
3. What's 0b10101010 OR 0b01010101? (3 pts)
4. What's 0b11110000 XOR 0b11110000? (3 pts)
5. What does NOT do? (2 pts)
6. Write code to set bit 7 in value 0 (4 pts)
7. Which operation tests if bit is set? (2 pts)
8. Which operation toggles bits? (2 pts)
9. Code: Use AND to extract lower 4 bits from 173 (4 pts)
10. Real-world use of XOR? (2 pts - encryption, swap, etc.)

---

## Closure / Project Submission (5 min)

**Submission**:
Save as: `week3_bittool_[YourName].asm`

**Self-Check**:
```
□ All 4 operations used
□ Program runs without errors
□ Uses IN for input
□ Multiple outputs shown
□ Comments explain each operation
□ Binary values documented
□ Tested with different inputs
```

**Turn In**: Upload or demonstrate live

**Next Week Preview**: 
"Week 4: CONTROL FLOW! Loops and IF statements - make programs that make decisions and repeat!"

---

## Assessment

### Project Rubric (50 points)

**Functionality (20 pts)**:
- All 4 operations work correctly
- Interactive input
- Produces expected outputs
- No errors

**Logic Operations (15 pts)**:
- AND used appropriately (4 pts)
- OR used appropriately (4 pts)
- XOR used appropriately (4 pts)
- NOT used appropriately (3 pts)

**Documentation (10 pts)**:
- Comments explain operations
- Binary values documented
- Clear structure
- Purpose explained

**Code Quality (5 pts)**:
- Well-organized
- Efficient
- Clean implementation

**Bonus (+10 pts)**:
- Creative application (+3)
- Multiple inputs (+3)
- Extra functionality (+2)
- Exceptional documentation (+2)

---

## Differentiation

**Struggling**:
- Template provided
- 3 operations acceptable
- Simplified requirements
- Extended time

**Advanced**:
- Complex multi-step operations
- Multiple modes/functions
- Optimization challenge
- Creative applications

**ELL**:
- Comments can include native language
- Visual documentation acceptable
- Oral explanation option
- Partner demonstration

---

## Teacher Notes

**Grading Efficiency**:
- Test each program quickly
- Check for all 4 operations
- Verify documentation
- 5 minutes per student max

**Common Project Issues**:

1. **"Only using 3 operations"**
   - Guide to add missing one
   - Show example application

2. **"Program doesn't work"**
   - Debug in Step mode
   - Check binary math
   - Verify logic

3. **"Finished early"**
   - Add more operations
   - Test edge cases
   - Help neighbor
   - Improve documentation

**Success Indicators**:
- Understanding of each operation's purpose
- Appropriate operation selection
- Working implementation
- Clear documentation

**Week 3 Achievements**:
- Binary understanding
- All 4 logic operations mastered
- Bit manipulation skills
- Real-world applications

---

## Handout: Bit Tool Project Spec

```
╔════════════════════════════════════════════╗
║       BIT MANIPULATION TOOL PROJECT        ║
╠════════════════════════════════════════════╣
║                                            ║
║  GOAL: Create a useful bit tool            ║
║                                            ║
║  CHOOSE ONE:                               ║
║  • Pattern Generator                       ║
║  • Permission Manager                      ║
║  • Encryption Tool                         ║
║  • Mask Creator                            ║
║  • Your Creative Idea (get approval)       ║
║                                            ║
║  REQUIREMENTS:                             ║
║  □ Use AND operation                       ║
║  □ Use OR operation                        ║
║  □ Use XOR operation                       ║
║  □ Use NOT operation                       ║
║  □ Interactive (IN instruction)            ║
║  □ Multiple outputs                        ║
║  □ Comments explaining operations          ║
║  □ Binary values documented                ║
║                                            ║
║  EXAMPLE STRUCTURE:                        ║
║  ; === INPUT ===                           ║
║  IN A              ; Get user value        ║
║                                            ║
║  ; === AND DEMO ===                        ║
║  ; Extract lower nibble                    ║
║  MOV B, A                                  ║
║  AND B, 0b00001111                         ║
║  OUT B                                     ║
║                                            ║
║  ; === OR DEMO ===                         ║
║  ; Set bit 7                               ║
║  MOV B, A                                  ║
║  OR B, 0b10000000                          ║
║  OUT B                                     ║
║                                            ║
║  ; === XOR DEMO ===                        ║
║  ; Toggle all bits                         ║
║  MOV B, A                                  ║
║  XOR B, 0b11111111                         ║
║  OUT B                                     ║
║                                            ║
║  ; === NOT DEMO ===                        ║
║  ; Invert                                  ║
║  MOV B, A                                  ║
║  NOT B                                     ║
║  OUT B                                     ║
║                                            ║
║  HALT                                      ║
║                                            ║
║  GRADING (50 points):                      ║
║  • Functionality: 20 pts                   ║
║  • Logic Operations: 15 pts                ║
║  • Documentation: 10 pts                   ║
║  • Code Quality: 5 pts                     ║
║  • Bonus: up to +10 pts                    ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-AP-16, 3A-AP-17
**LO**: LO2.1, LO2.5, LO4.2, LO4.3

---

*End of Week 3, Day 5 Lesson Plan*
*End of Week 3 Complete Lesson Series*
