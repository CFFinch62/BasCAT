# Week 2, Day 5: Lab Day - Interactive Calculator

**Topic**: Week 2 Capstone Project - Build a Calculator
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all Week 2 concepts in complete application
- Design and implement interactive program
- Test and debug complex programs
- Document code professionally

---

## Materials Needed

- Computers with BasCAT
- Project rubric (printed)
- Handout: "Calculator Project Spec"
- Example calculator apps (for inspiration)

---

## Lab Project: Interactive Calculator

### Project Description

Students create a multi-function calculator that demonstrates mastery of Week 1-2 concepts.

**Core Requirements**:
1. Interactive (uses IN for input)
2. Multiple operations (at least 3: add, subtract, and one more)
3. Well-organized code with comments
4. Memory map documentation
5. Working demonstration

---

## Lesson Outline

### Introduction & Project Launch (10 minutes)

**Hook - Show Real Calculator**:
"Every calculator app does what you now know how to do:
- Gets input from user
- Does arithmetic
- Shows output
- Today YOU build one!"

**Project Overview**:

"You're creating an Interactive Calculator with three modes:
1. Addition Mode
2. Subtraction Mode
3. Your Choice (could be: double a number, triple it, add 100, etc.)"

**Show Example Calculator**:
```assembly
; Simple Calculator Example
; Mode 1: Add two numbers
; Mode 2: Subtract two numbers
; Mode 3: Double a number

; === INPUT SECTION ===
IN A           ; First number OR number to double
IN B           ; Second number (for add/subtract)

; === PROCESSING SECTION ===
; Addition
ADD A, B
STM 10, A      ; Store sum

; Subtraction (need to reload)
IN A           ; Re-read first number
SUB A, B       ; Calculate difference
STM 11, A      ; Store difference

; Double (need to reload)
IN A           ; Read number to double
ADD A, A       ; Double it
STM 12, A      ; Store doubled value

; === OUTPUT SECTION ===
LDM A, 10
OUT A          ; Output sum

LDM A, 11
OUT A          ; Output difference

LDM A, 12
OUT A          ; Output doubled value

HALT
```

"This is just an example - yours will be different!"

**Project Requirements**:

**Minimum (Basic Level - 40 points)**:
- Read at least 2 inputs
- Perform at least 2 different operations (add, subtract, etc.)
- Output all results
- Include comments
- Working memory map

**Proficient (50 points)**:
- Everything in Basic, PLUS:
- 3+ different operations
- Store intermediate results in memory
- Well-organized sections
- Comprehensive comments

**Advanced (60 points - with bonus)**:
- Everything in Proficient, PLUS:
- 4+ operations
- Creative/unique operation
- Optimized code
- Professional documentation

**Time Management**: "You have 35 minutes to work!"

### Independent Work Time (35 minutes)

**Students Work Independently** on calculators

**Teacher Circulates** - Focus areas:

**First 10 Minutes**:
- Check that students are planning before coding
- Ensure they're creating memory maps
- Help with design decisions
- Remind about IN for interactive input

**Middle 15 Minutes**:
- Debug syntax errors
- Help with arithmetic logic
- Verify memory usage
- Encourage testing as they go

**Final 10 Minutes**:
- Ensure programs actually run
- Check comments and documentation
- Remind about testing with different inputs
- Push students to add one more feature

**Common Student Questions**:

**"How do I do three operations?"**
```
Three options:
1. Use same inputs for all (easiest)
2. Ask for new inputs for each (more IN statements)
3. Mix - some operations use saved values
```

**"Can I add more than 3 operations?"**
"Yes! Bonus points for 4+!"

**"My program is too long!"**
"That's okay! Longer ≠ bad. Clear and working > short and broken."

**"What should my third operation be?"**
Ideas:
- Double a number (ADD A, A)
- Add 100 to a number
- Triple a number (ADD A, A, then ADD original again)
- Difference backwards (B - A instead of A - B)
- Sum of three numbers

**Differentiation During Lab**:

**Struggling Students**:
- Provide basic template
- Reduce to 2 operations only
- Allow pair programming
- Accept less documentation

**On-Level Students**:
- Encourage 3 operations
- Push for good comments
- Test with multiple inputs

**Advanced Students**:
- Challenge: 5+ operations
- Optimization challenge: Fewest instructions
- Creative operations (Fibonacci, powers, etc.)
- Help others when done

**Monitoring Progress**:
Walk around with checklist:
- [ ] Student has working IN instructions
- [ ] At least 2 operations implemented
- [ ] Comments present
- [ ] Program compiles without errors
- [ ] Student has tested program

### Demonstrations (If Time Permits) (5 minutes)

**Quick Demos**:
- 2-3 volunteers show their calculators
- Run with test inputs
- Explain what operations they included
- Class gives positive feedback

**Questions to Ask Demos**:
- "What was your third operation?"
- "What was the hardest part?"
- "How did you organize your code?"

---

## Week 2 Quiz (Beginning of Next Class or Last 10 min if time)

**Quiz Format**: 10 questions, 10 minutes

**Sample Questions**:

1. What does ADD A, 5 do? (2 pts)
2. What does SUB A, 10 do? (2 pts)
3. Write an instruction to read user input into register A. (2 pts)
4. What's the difference between LOAD and ADD? (3 pts)
5. Code: Write a program that reads a number, adds 10, outputs result. (6 pts)
6. What happens if you subtract 20 from 10? (2 pts)
7. What does the Zero flag indicate? (2 pts)
8. Name two ways to get data into a register. (2 pts)
9. Write code to output register A. (1 pt)
10. Why use memory instead of just registers? (3 pts)

**Total**: 25 points

---

## Closure / Project Submission (5 minutes)

**Submission Requirements**:

Save as: `week2_calculator_[YourName].asm`

**Self-Assessment Checklist**:
```
Before submitting, verify:
□ Program runs without errors
□ At least 2 operations work
□ Uses IN for input
□ Uses OUT for output
□ Comments explain sections
□ Memory map included
□ Tested with different numbers
```

**Turn In**:
- Upload .asm file
- OR demonstrate live next class
- OR email to teacher

**Late Policy**: -10% if submitted Monday

**Next Week Preview**:
"Week 3: LOGIC OPERATIONS! You'll learn AND, OR, XOR, NOT - the building blocks of computer thinking!"

---

## Assessment

### Project Rubric (50 points)

**Functionality (20 points)**:
- 20: All operations work perfectly
- 15: All operations work with minor issues
- 10: Most operations work
- 5: Some operations work
- 0: Doesn't run

**Interactive Input (10 points)**:
- 10: Uses IN correctly for all inputs
- 7: Uses IN with minor issues
- 4: Partial IN usage
- 0: No IN usage

**Code Organization (10 points)**:
- 10: Excellent sections, clear structure
- 7: Well organized
- 4: Somewhat organized
- 0: Disorganized

**Documentation (10 points)**:
- 10: Comprehensive comments, complete memory map
- 7: Good comments, memory map present
- 4: Minimal comments
- 0: No comments

**Bonus Points (up to +10)**:
- +3: Four or more operations
- +3: Creative/unique operation
- +2: Especially clear code
- +2: Handles edge cases well

---

## Differentiation

### For Struggling Students:
- **Simplified**: Only 2 operations required
- **Template**: Provide starter code
- **Extended Time**: Can finish Monday
- **Pair Option**: Work with partner (both submit)

### For Advanced Students:
- **More Operations**: 5+ for challenge
- **Optimization**: Minimize instruction count
- **Creative**: Unusual operations (factorial, powers)
- **Help Others**: Mentor struggling students

### For ELL Students:
- **Comments**: Can be in native language
- **Vocab Support**: Calculator terms glossary
- **Visual**: Provide flowchart template
- **Oral Demo**: Can explain program verbally instead of written docs

---

## Teacher Notes

### Grading Efficiency:
- Can grade during lab time (students working)
- Quick rubric scoring (5 min per student)
- Focus on: Does it run? Does it use IN? Are comments present?
- Full code review not needed for every student

### Common Project Issues:

1. **"I can't get three operations"**
   - Help simplify: Same inputs, different operations
   - Example: Add them, subtract them, double first one

2. **"My program doesn't work"**
   - Step through in debug mode
   - Check syntax
   - Verify logic
   - Test with simple numbers (like 10 and 5)

3. **"I'm done early"**
   - Add another operation
   - Improve comments
   - Test edge cases
   - Help a neighbor

4. **"I ran out of time"**
   - Submit what you have
   - Can improve for Monday
   - Partial credit for partial work

### What to Look For:
- Student understanding of IN instruction
- Proper use of arithmetic
- Code organization
- Problem-solving approach
- Testing and debugging skills

### Follow-Up for Week 3:
- [ ] Grade calculator projects over weekend
- [ ] Prepare logic operations intro
- [ ] Set up binary number lessons
- [ ] Plan AND/OR/XOR demonstrations

---

## Handout: Calculator Project Spec

```
╔════════════════════════════════════════════╗
║      INTERACTIVE CALCULATOR PROJECT        ║
╠════════════════════════════════════════════╣
║                                            ║
║  GOAL: Build a working calculator          ║
║                                            ║
║  REQUIREMENTS:                             ║
║  ┌──────────────────────────────────────┐ ║
║  │ 1. Interactive (use IN)              │ ║
║  │ 2. At least 2 operations             │ ║
║  │ 3. Output results                    │ ║
║  │ 4. Comments & memory map             │ ║
║  │ 5. Working demonstration             │ ║
║  └──────────────────────────────────────┘ ║
║                                            ║
║  SUGGESTED OPERATIONS:                     ║
║  • Addition                                ║
║  • Subtraction                             ║
║  • Double a number                         ║
║  • Triple a number                         ║
║  • Add 100                                 ║
║  • Difference (both ways)                  ║
║  • Sum of three numbers                    ║
║  • Your creative idea!                     ║
║                                            ║
║  CODE STRUCTURE:                           ║
║  ; === INPUT SECTION ===                   ║
║  ; Get numbers from user                   ║
║                                            ║
║  ; === PROCESSING SECTION ===              ║
║  ; Do calculations                         ║
║                                            ║
║  ; === OUTPUT SECTION ===                  ║
║  ; Display results                         ║
║                                            ║
║  ; === MEMORY MAP ===                      ║
║  ; Document what each address holds        ║
║                                            ║
║  TESTING:                                  ║
║  Test with at least 2 different sets:      ║
║  • Simple: 10, 5                           ║
║  • Larger: 50, 25                          ║
║  • Your choice: ?, ?                       ║
║                                            ║
║  GRADING (50 points):                      ║
║  • Functionality: 20 pts                   ║
║  • Interactive: 10 pts                     ║
║  • Organization: 10 pts                    ║
║  • Documentation: 10 pts                   ║
║  • Bonus: up to +10 pts                    ║
║                                            ║
║  TIPS:                                     ║
║  ✓ Plan before coding                      ║
║  ✓ Test each operation separately          ║
║  ✓ Comment as you go                       ║
║  ✓ Use Step mode to debug                  ║
║  ✓ Ask for help if stuck!                  ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms
- 3A-AP-16: Design and iteratively develop programs
- 3A-AP-17: Decompose problems

**Learning Objectives (Week 2)**:
- LO2.1: Write functional assembly programs ✓
- LO2.5: Debug assembly programs ✓
- LO4.1: Decompose problems ✓
- LO4.2: Implement algorithms efficiently ✓

---

*End of Week 2, Day 5 Lesson Plan*
*End of Week 2 Complete Lesson Series*
