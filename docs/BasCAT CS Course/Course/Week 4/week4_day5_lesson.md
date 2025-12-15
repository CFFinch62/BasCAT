# Week 4, Day 5: Lab Day - Interactive Game

**Topic**: Week 4 Capstone - Build a Game
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all control flow concepts
- Create interactive program with loops and decisions
- Design complete algorithm
- Debug complex control structures

---

## Materials

- Computers with BasCAT
- Project rubric
- Handout: "Game Project Spec"

---

## Lab Project: Interactive Game

### Project Options

**Option 1: Number Guessing Game**
- Generate/choose secret number
- Loop: Get user guess
- Compare, give hints (higher/lower)
- Repeat until correct
- Count attempts

**Option 2: Quiz Game**
- Store 5 "questions" (expected answers)
- Loop through questions
- Check answers
- Track score
- Output final score

**Option 3: Simple Calculator Menu**
- Loop: Show menu (1=add, 2=sub, 3=quit)
- Read choice
- Perform operation
- Repeat until quit

**Option 4: Number Pattern Game**
- Generate pattern (even, odd, multiples)
- User guesses next number
- Check if correct
- Loop until N correct answers

---

## Lesson Outline

### Project Launch (10 min)

**Requirements**:
- Uses CMP
- Uses at least 2 conditional jumps
- Contains at least 1 loop
- Interactive (IN instructions)
- Multiple outputs
- Comments and documentation

**Example - Guessing Game**:
```assembly
; Number Guessing Game
; Secret number: 42

LOAD B, 42     ; Secret
LOAD C, 0      ; Attempt counter

game_loop:
  IN A         ; Get guess
  ADD C, 1     ; Count attempt
  
  CMP A, B
  JZ correct   ; If equal, won!
  
  JC too_low   ; If less, give hint
  
  ; Too high
  LOAD A, 1
  OUT A
  JMP game_loop
  
too_low:
  LOAD A, 0
  OUT A
  JMP game_loop
  
correct:
  OUT C        ; Output attempts
  HALT
```

### Independent Work (35 min)

**Students create chosen project**

**Teacher Support**:
- Design verification (first 5 min)
- Algorithm help
- Debug control flow
- Test edge cases

**Common Issues**:
- Infinite loops
- Missing HALT
- Off-by-one errors
- Wrong jump conditions

### Demonstrations (5 min - if time)

**Volunteer demos**

---

## Project Rubric (50 points)

**Functionality (20 pts)**:
- Program works correctly
- All features implemented
- Handles multiple cases

**Control Flow (15 pts)**:
- CMP used correctly (5)
- Conditional jumps work (5)
- Loop functions properly (5)

**Interactivity (10 pts)**:
- Uses IN effectively
- Responds to user input
- Multiple iterations

**Documentation (5 pts)**:
- Comments explain logic
- Algorithm described
- Clear structure

**Bonus (+10 pts)**:
- Extra features
- Multiple loops
- Complex logic
- Exceptional quality

---

## Week 4 Quiz (if time)

**Sample Questions** (25 pts):
1. What does CMP do? (3)
2. JZ jumps when? (2)
3. JC jumps when? (2)
4. Write loop 1-10 (8)
5. Write if-else structure (8)
6. Debug given code (5)

---

## Closure

**Submit**: `week4_game_[Name].asm`

**Next Week**: "Stack operations and procedures!"

---

## Assessment

**Success Indicators**:
- Working control flow
- Proper comparisons
- Functional loops
- Interactive responses

---

## Differentiation

**Struggling**: Simple linear game, provided template
**Advanced**: Complex multi-level game, optimization
**ELL**: Visual flowcharts, documented examples

---

## Standards Alignment
**CSTA**: 3A-AP-13, 3A-AP-16
**LO**: LO2.1, LO4.1, LO4.2

---

*End of Week 4, Day 5 Lesson Plan*
*End of Week 4 Complete Lesson Series*
