# Week 7, Day 2: BASIC Control Flow

**Topic**: IF-THEN and GOTO Statements
**Duration**: 50 minutes
**Learning Objectives**:
- Use IF-THEN for conditional logic
- Use GOTO for program flow
- Compare to assembly jumps
- Create decision-based programs

---

## Key Concepts

**IF-THEN Statement**:
```basic
10 INPUT A
20 IF A > 10 THEN PRINT "Big"
30 IF A <= 10 THEN PRINT "Small"
40 END
```

**GOTO Statement**:
```basic
10 INPUT A
20 IF A = 0 THEN GOTO 50
30 PRINT "Not zero"
40 GOTO 60
50 PRINT "Zero!"
60 END
```

**Comparison to Assembly**:
- Assembly: `CMP A, 10` then `JC label`
- BASIC: `IF A < 10 THEN GOTO 50`

Much more readable!

---

# Week 7, Day 3: BASIC Loops

**Topic**: FOR-NEXT Loops
**Duration**: 50 minutes
**Learning Objectives**:
- Use FOR-NEXT loops
- Understand loop counters
- Compare to assembly loops
- Create iterative programs

---

## Key Concepts

**FOR-NEXT Loop**:
```basic
10 FOR I = 1 TO 10
20   PRINT I
30 NEXT I
40 END
```

**With STEP**:
```basic
10 FOR I = 0 TO 100 STEP 10
20   PRINT I
30 NEXT I
40 END
```

**Nested Loops**:
```basic
10 FOR I = 1 TO 3
20   FOR J = 1 TO 3
30     PRINT I; " x "; J; " = "; I * J
40   NEXT J
50 NEXT I
60 END
```

**Comparison to Assembly**:
Assembly version needs:
- Counter initialization
- Loop body
- Counter increment
- Comparison
- Conditional jump

BASIC: Just FOR-NEXT!

---

# Week 7, Day 4: BASIC Arrays

**Topic**: Array Basics and DIM Statement
**Duration**: 50 minutes
**Learning Objectives**:
- Declare arrays with DIM
- Store multiple values
- Access array elements
- Process arrays with loops

---

## Key Concepts

**Array Declaration**:
```basic
10 DIM A(10)     REM Array of 10 elements
20 DIM B(5, 5)   REM 2D array
```

**Using Arrays**:
```basic
10 DIM SCORES(5)
20 FOR I = 1 TO 5
30   INPUT "Score: "; SCORES(I)
40 NEXT I
50 FOR I = 1 TO 5
60   PRINT "Score "; I; ": "; SCORES(I)
70 NEXT I
80 END
```

**Array Processing**:
```basic
10 DIM NUMS(10)
20 LET SUM = 0
30 FOR I = 1 TO 10
40   INPUT NUMS(I)
50   LET SUM = SUM + NUMS(I)
60 NEXT I
70 PRINT "Sum: "; SUM
80 PRINT "Average: "; SUM / 10
90 END
```

**Comparison to Assembly**:
- Assembly: Manual memory addressing
- BASIC: Automatic with arrays!

---

# Week 7, Day 5: Lab Day - BASIC Program

**Topic**: Week 7 Capstone Project
**Duration**: 50 minutes
**Learning Objectives**:
- Apply all BASIC concepts
- Create complete program
- Compare to assembly equivalent
- Demonstrate language mastery

---

## Lab Project Options

**Option 1: Grade Calculator**
- Read N test scores into array
- Calculate average, min, max
- Determine letter grade
- Show all scores and statistics

**Option 2: Number Game**
- Guess the number (1-100)
- Give hints (higher/lower)
- Count attempts
- Option to play again

**Option 3: Simple Database**
- Store names and ages in arrays
- Menu: Add, View, Search
- Loop until user quits
- Display formatted output

**Option 4: Math Tutor**
- Generate random problems
- Check answers
- Keep score
- Multiple difficulty levels

---

## Requirements

**Must Include**:
- Variables and arrays
- INPUT and PRINT
- IF-THEN statements
- FOR-NEXT loop (or GOTO loop)
- Comments (REM)
- END statement

**Bonus Features**:
- Nested loops
- 2D arrays
- Complex calculations
- User-friendly interface

---

## Rubric (50 points)

**Functionality (20 pts)**:
- Program works correctly
- All features implemented
- Handles user input

**BASIC Concepts (15 pts)**:
- Arrays (5)
- Loops (5)
- Conditionals (5)

**Code Quality (10 pts)**:
- Comments
- Organization
- Readability

**Documentation (5 pts)**:
- Algorithm explanation
- User instructions

**Bonus (+10 pts)**:
- Assembly comparison
- Advanced features
- Exceptional quality

---

## Week 7 Assessment

**Written Test** (25 pts):
1. Convert assembly to BASIC (10)
2. Write FOR loop (5)
3. Array manipulation (5)
4. IF-THEN logic (5)

**Practical Coding** (25 pts):
30-minute timed challenge:
- Implement specific algorithm
- Use required BASIC features
- Working, commented code

---

## Closure

**Reflection Questions**:
1. Which is easier: Assembly or BASIC?
2. When would you use each?
3. What surprised you about BASIC?

**Next Week**: "Advanced BASIC and Architecture Concepts!"

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-AP-16, 3A-CS-02
**LO**: LO3.1, LO3.2, LO5.1, LO5.2

---

*End of Week 7 Complete Lesson Series*
