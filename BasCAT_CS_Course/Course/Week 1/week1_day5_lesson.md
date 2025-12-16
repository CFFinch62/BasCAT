# Week 1, Day 5: Lab Day - Personal Data Card

**Topic**: Week 1 Capstone Project
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all Week 1 concepts in a complete program
- Create organized, well-documented code
- Demonstrate understanding of registers and memory
- Debug and refine programs independently

---

## Materials Needed

- Computers with BasCAT
- Project rubric (printed, one per student)
- Homework from all week (for reference)
- Handout: "Program Checklist"

---

## Lab Project: Personal Data Card

### Project Description

Students create a comprehensive program that stores and displays personal data using both registers and memory, demonstrating mastery of Week 1 concepts.

**Requirements**:
1. Store at least 5 different personal data points
2. Use both registers AND memory
3. Retrieve and display all data
4. Include a complete memory map
5. Well-commented code explaining each section
6. Working demonstration

---

## Lesson Outline

### Introduction & Project Launch (10 minutes)

**Project Overview**:

"Today you're creating a 'Personal Data Card' - think of it like a digital business card that stores information about you."

**Show Example Output**:
```
[Running example program]
Output: 16, 8, 7, 42, 100
(Age, birth month, siblings, favorite number, lucky number)
```

**Project Requirements**:

"Your program must:
1. Store 5+ pieces of data about yourself
2. Use at least 2 memory addresses (not just registers)
3. Output all the data
4. Include comments explaining what each number means
5. Create a memory map showing your data organization"

**Data Ideas** (write on board):
- Age
- Birth month/day/year
- Number of siblings
- Favorite number
- Lucky number
- Height (in inches)
- Grade level
- Jersey number (sports)
- House/apartment number
- Initials (ASCII codes)

**Show Example Program**:
```assembly
; Personal Data Card by Mr. Smith
; This program stores and displays my information

; === STORE DATA IN MEMORY ===
LOAD A, 35
STM 10, A      ; My age at address 10

LOAD A, 3
STM 11, A      ; Birth month (March) at address 11

LOAD A, 2
STM 12, A      ; Number of children at address 12

; === STORE DATA IN REGISTERS ===
LOAD B, 7      ; Lucky number in register B
LOAD C, 42     ; Favorite number in register C

; === DISPLAY ALL DATA ===
LDM A, 10      ; Get age from memory
OUT A

LDM A, 11      ; Get birth month
OUT A

LDM A, 12      ; Get number of children
OUT A

OUT B          ; Lucky number
OUT C          ; Favorite number

HALT

; === MEMORY MAP ===
; Address 10: Age (35)
; Address 11: Birth month (3)
; Address 12: Number of children (2)
; Register B: Lucky number (7)
; Register C: Favorite number (42)
```

**Circuit Demonstration**:
- Run the example in BasCAT
- Step through showing:
  - Data being stored in memory
  - Data being stored in registers
  - Data being retrieved and output

**Assessment Rubric** (distribute handout):

| Criteria | Points | Description |
|----------|--------|-------------|
| Functionality | 15 | Program runs without errors, outputs all data |
| Data Storage | 10 | Uses both registers AND memory correctly |
| Code Quality | 10 | Well-organized, clear structure |
| Comments | 10 | Explains each section and data point |
| Memory Map | 5 | Complete map included in comments |
| **Total** | **50** | |

**Questions**: Answer any clarifying questions

**Time Management**: "You have 35 minutes to work. Use them wisely!"

### Independent Work Time (35 minutes)

**Students Work Independently**:
- Create their personal data card program
- Test and debug their code
- Create memory map
- Add comments

**Teacher Role - Circulate and Help**:

**First 10 minutes**:
- Check that students are planning before coding
- Ensure they're creating memory maps
- Help with initial setup

**Middle 15 minutes**:
- Debug syntax errors
- Help students organize their code
- Encourage proper commenting
- Check memory addresses (avoiding 254, 255)

**Final 10 minutes**:
- Remind students to test their programs
- Ensure memory maps are complete
- Have students review rubric
- Encourage adding more than minimum requirements

**Common Issues to Watch For**:

1. **Not using memory** (all registers)
   - Guide: "The rubric requires memory! Pick 2 pieces of data to store in memory addresses."

2. **Forgetting to retrieve from memory**
   - Check: "You stored data at address 10, but did you LDM it back?"

3. **No comments or memory map**
   - Remind: "Comments and memory map are 30% of your grade!"

4. **Syntax errors preventing execution**
   - Help debug: Check instruction spelling, commas, addresses

**Differentiation During Lab**:

**Struggling Students**:
- Provide template with blanks to fill in
- Reduce to 3 data points instead of 5
- Allow pair programming if needed
- Focus on getting SOMETHING working

**Advanced Students**:
- Challenge: Store 10 data points
- Extension: Output data in creative order or pattern
- Optimization: Minimize total instructions used
- Creativity: Spell name in ASCII, create number pattern

**Extension Ideas**:
- "Can you output your data in reverse order?"
- "Can you create a pattern with your numbers?"
- "Can you use all 4 registers AND 5 memory addresses?"

### Demonstration & Reflection (5 minutes)

**Quick Demos** (if time permits):
- 2-3 volunteers show their programs
- Run and explain what data they stored
- Class provides positive feedback

**Whole Class Reflection**:

"Let's think about what we learned this week."

**Questions to Discuss**:
1. "What's the difference between registers and memory?"
   - Registers: 4, fast, temporary
   - Memory: 256, persistent, organized by address

2. "When would you use LOAD vs MOV?"
   - LOAD: When you know the value
   - MOV: When copying from another register

3. "Why do we need both registers AND memory?"
   - Registers: Fast work
   - Memory: Long-term storage

**Week in Review**:
- Day 1: LOAD, OUT, registers
- Day 2: Multiple registers
- Day 3: MOV instruction
- Day 4: Memory (STM, LDM)
- Day 5: Putting it all together!

**Preview Next Week**:
"Next week we add MATH! Addition and subtraction with the ALU. You'll build a calculator!"

---

## Closure / Project Submission (5 minutes - may extend into next class)

**Submission Requirements**:

Save your file as: `week1_datacard_[YourName].asm`

**Self-Assessment Checklist**:
- [ ] Program runs without errors
- [ ] Uses at least 2 memory addresses
- [ ] Uses at least 2 registers
- [ ] Outputs all stored data
- [ ] Includes section comments
- [ ] Includes complete memory map
- [ ] Tested and works correctly

**Turn In**:
- Upload .asm file to class folder
- OR email to teacher
- OR demonstrate live during next class

**Late Policy**:
- Due today, but can submit Monday for -10%
- Must submit by Tuesday for credit

---

## Week 1 Quiz (if time, or beginning of next class)

**Quiz Format**: 10 minutes, 10 questions

**Sample Questions**:

1. What does LOAD A, 50 do? (2 pts)
2. How many general-purpose registers does BasCAT have? (1 pt)
3. Write an instruction to copy register A to register B. (2 pts)
4. What does STM 20, A do? (2 pts)
5. What's the difference between registers and memory? (3 pts)

**Or**: Postpone quiz to Monday if lab time runs over

---

## Assessment

### Project Rubric (50 points total)

**Functionality (15 points)**:
- 15: Perfect execution, all features work
- 12: Works with minor issues
- 9: Mostly works, some bugs
- 6: Significant problems
- 0: Doesn't run

**Data Storage (10 points)**:
- 10: Uses registers AND memory correctly (at least 2 of each)
- 7: Uses both but with minor errors
- 4: Uses only one type
- 0: Doesn't store data properly

**Code Quality (10 points)**:
- 10: Excellently organized, clear structure
- 7: Well organized
- 4: Somewhat organized
- 0: Disorganized/messy

**Comments (10 points)**:
- 10: Comprehensive comments explaining all sections
- 7: Good comments on most parts
- 4: Minimal comments
- 0: No comments

**Memory Map (5 points)**:
- 5: Complete, accurate memory map
- 3: Partial memory map
- 0: No memory map

---

## Differentiation

### For Struggling Students:
- Provide template with structure
- Reduce to 3 data points
- Allow extended time (submit Monday)
- One-on-one help during lab
- Accept hand-drawn memory map instead of typed

### For Advanced Students:
- Require 10+ data points
- Create patterns or sequences
- Optimize for fewest instructions
- Add "Easter egg" hidden message
- Create multiple data cards (family members)

### For ELL Students:
- Allow data labels in native language
- Provide vocabulary list
- Visual memory map template
- Partner with bilingual student
- Focus on functionality over comments (adjust rubric)

---

## Teacher Notes

### Time Management:
- This lesson may run long due to lab work
- Option 1: Extend lab time, move quiz to next class
- Option 2: Strict 35-minute lab, quiz today
- Option 3: Lab today, demos next class

### Grading Efficiency:
- Grade during next class while students work
- Quick rubric scoring (5 min per student)
- Focus on did it work + memory map + comments
- Can score functionality by just running programs

### Common Student Questions:

**"Can I use the same address twice?"**
- Yes, but second STM will overwrite first value
- Better to use different addresses

**"What if I want to store more than 5 things?"**
- Great! Extra data = bonus points
- Memory has 253 usable addresses

**"Can I output in different order than I stored?"**
- Absolutely! That's the point of storage

**"My program doesn't work!"**
- Step through with circuit view
- Check syntax
- Verify addresses
- Test one piece at a time

### Follow-Up:
- Grade projects over weekend
- Provide feedback on Monday
- Return graded work with comments
- Use common errors to inform Week 2 teaching

### Materials to Prepare for Week 2:
- [ ] Review arithmetic operations (ADD, SUB)
- [ ] Prepare ALU demonstration
- [ ] Create calculator project spec
- [ ] Plan I/O integration lessons

---

## Handout: Program Checklist

```
╔════════════════════════════════════════════╗
║   PERSONAL DATA CARD - CHECKLIST           ║
╠════════════════════════════════════════════╣
║                                            ║
║  BEFORE YOU START:                         ║
║  □ I know what 5+ data points to store     ║
║  □ I created a memory map plan             ║
║  □ I know which data goes in memory        ║
║  □ I know which data goes in registers     ║
║                                            ║
║  WHILE CODING:                             ║
║  □ Stored data in memory (STM)             ║
║  □ Stored data in registers (LOAD/MOV)     ║
║  □ Retrieved from memory (LDM)             ║
║  □ Output all data (OUT)                   ║
║  □ Added HALT at end                       ║
║                                            ║
║  CODE QUALITY:                             ║
║  □ Comments explain each section           ║
║  □ Comments show what each number means    ║
║  □ Memory map included in comments         ║
║  □ Code is organized (storage, then output)║
║                                            ║
║  TESTING:                                  ║
║  □ Program runs without errors             ║
║  □ All expected values output correctly    ║
║  □ Tested in BasCAT Step mode              ║
║  □ Verified memory map matches actual code ║
║                                            ║
║  FINAL CHECK:                              ║
║  □ File named correctly                    ║
║  □ Self-assessed against rubric            ║
║  □ Ready to submit or demonstrate          ║
║                                            ║
║  BONUS (OPTIONAL):                         ║
║  □ Used more than 5 data points            ║
║  □ Created interesting pattern/sequence    ║
║  □ Optimized for efficiency                ║
║  □ Added creative element                  ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms to solve computational problems
- 3A-AP-17: Decompose problems into sub-problems
- 3A-CS-01: Explain how abstractions hide implementation details

**Learning Objectives Addressed (Week 1)**:
- LO2.1: Write functional assembly programs ✓
- LO2.2: Use registers effectively ✓
- LO1.4: Explain how memory addresses map to data storage ✓
- LO4.1: Decompose problems into computational steps ✓
- LO4.4: Design data structures using available memory ✓

---

*End of Week 1, Day 5 Lesson Plan*
*End of Week 1 Complete Lesson Series*
