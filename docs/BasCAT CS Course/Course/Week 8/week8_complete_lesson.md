# Week 8: Advanced BASIC Programming

**Theme**: Subroutines, Functions, and Complex Programs
**Duration**: 5 days (50 minutes each)

---

## Week 8, Day 1: GOSUB and RETURN

**Topic**: Subroutines in BASIC
**Duration**: 50 minutes

### Key Concepts

**GOSUB Statement**:
```basic
10 GOSUB 100     REM Call subroutine
20 PRINT "Back from subroutine"
30 END
100 REM Subroutine starts here
110 PRINT "In subroutine"
120 RETURN       REM Return to caller
```

**Multiple Subroutines**:
```basic
10 GOSUB 100     REM Call first
20 GOSUB 200     REM Call second
30 END
100 PRINT "Subroutine 1"
110 RETURN
200 PRINT "Subroutine 2"
210 RETURN
```

**Parameter Passing** (via variables):
```basic
10 LET X = 5
20 LET Y = 10
30 GOSUB 100     REM Call add subroutine
40 PRINT "Sum: "; Z
50 END
100 REM Add subroutine
110 LET Z = X + Y
120 RETURN
```

**Comparison to Assembly**:
- Assembly: CALL/RET (uses stack)
- BASIC: GOSUB/RETURN (simpler syntax)
- Both do same thing underneath!

**Lab Exercise**: Create calculator with subroutines for each operation

---

## Week 8, Day 2: String Manipulation

**Topic**: Working with Text in BASIC
**Duration**: 50 minutes

### Key Concepts

**String Variables**:
```basic
10 LET A$ = "Hello"
20 LET B$ = "World"
30 PRINT A$; " "; B$
```

**String Functions**:
```basic
10 LET NAME$ = "Alice"
20 LET L = LEN(NAME$)      REM Length
30 LET FIRST$ = LEFT$(NAME$, 1)  REM First char
40 LET LAST$ = RIGHT$(NAME$, 1)  REM Last char
50 LET MID$ = MID$(NAME$, 2, 3)  REM Middle chars
```

**String Comparison**:
```basic
10 INPUT "Password: "; PASS$
20 IF PASS$ = "SECRET" THEN PRINT "Access Granted"
30 IF PASS$ <> "SECRET" THEN PRINT "Access Denied"
```

**Applications**:
- Text processing
- Password checking
- Name formatting
- Data validation

---

## Week 8, Day 3: File Operations (Conceptual)

**Topic**: Data Persistence Concepts
**Duration**: 50 minutes

### Key Concepts

**Why Files?**:
- Programs end, data disappears
- Need to save/load data
- Real applications use files

**Conceptual File Operations**:
```basic
10 REM Open file for writing
20 OPEN "DATA.TXT" FOR OUTPUT AS #1
30 PRINT #1, "Data line 1"
40 PRINT #1, "Data line 2"
50 CLOSE #1
60 REM Open file for reading
70 OPEN "DATA.TXT" FOR INPUT AS #1
80 INPUT #1, LINE$
90 PRINT LINE$
100 CLOSE #1
```

**Note**: BasCAT may have limited file support - focus on concepts

**Memory as File Substitute**:
```basic
10 DIM DATA$(10)     REM "Save" to array
20 DATA$(1) = "Record 1"
30 DATA$(2) = "Record 2"
```

---

## Week 8, Day 4: Program Design Patterns

**Topic**: Structured Programming in BASIC
**Duration**: 50 minutes

### Key Patterns

**Pattern 1: Menu System**:
```basic
10 REM Main Menu
20 PRINT "1. Add"
30 PRINT "2. Subtract"
40 PRINT "3. Quit"
50 INPUT "Choice: "; C
60 IF C = 1 THEN GOSUB 100
70 IF C = 2 THEN GOSUB 200
80 IF C = 3 THEN END
90 GOTO 20
100 REM Add routine
110 INPUT A, B
120 PRINT A + B
130 RETURN
200 REM Subtract routine
210 INPUT A, B
220 PRINT A - B
230 RETURN
```

**Pattern 2: Input Validation**:
```basic
10 REM Get valid input
20 INPUT "Enter 1-10: "; N
30 IF N < 1 OR N > 10 THEN GOTO 20
40 PRINT "Valid: "; N
```

**Pattern 3: Data Processing Pipeline**:
```basic
10 GOSUB 100   REM Read data
20 GOSUB 200   REM Process data
30 GOSUB 300   REM Display results
40 END
```

---

## Week 8, Day 5: Lab Day - Complete Application

**Topic**: Week 8 Capstone Project
**Duration**: 50 minutes

### Project Options

**Option 1: Contact Manager**
- Store names, phones in arrays
- Menu: Add, View, Search, Delete
- Input validation
- Subroutines for each function

**Option 2: Quiz Program**
- Store questions and answers
- Present questions
- Check answers
- Calculate score
- Show results

**Option 3: Simple Accounting**
- Track income/expenses
- Categorize transactions
- Calculate totals
- Show balance

**Option 4: Text Adventure**
- Room descriptions in arrays
- User choices move between rooms
- Inventory system
- Win/lose conditions

### Requirements

**Structure**:
- Main menu loop
- At least 3 subroutines
- Arrays for data storage
- Input validation
- Clear output formatting

**BASIC Features**:
- Arrays and variables
- FOR loops
- IF-THEN logic
- GOSUB/RETURN
- String handling (if applicable)

### Rubric (50 points)

**Functionality (20)**:
- All features work
- Proper error handling
- User-friendly

**Subroutines (10)**:
- Well-organized
- Clear purpose
- Proper RETURN

**Code Quality (10)**:
- Comments
- Structure
- Readability

**Design (5)**:
- Good UX
- Clear menus
- Helpful prompts

**Documentation (5)**:
- User guide
- Code comments
- Algorithm description

**Bonus (+10)**:
- Advanced features
- Exceptional quality
- Creative implementation

---

## Week 8 Assessment

**Concept Quiz** (25 pts):
1. GOSUB vs GOTO (5)
2. String operations (5)
3. Array usage (5)
4. Program structure (5)
5. Code tracing (5)

**Practical Challenge** (25 pts):
- Build specific program
- Use required features
- 40-minute time limit

---

## Reflection

**Discussion Questions**:
1. How do subroutines improve programs?
2. What makes BASIC easier than assembly?
3. When would you use arrays vs simple variables?
4. How does structure help large programs?

**Next Week**: "Computer Architecture - How It All Works!"

---

## Standards Alignment

**CSTA**: 3A-AP-13, 3A-AP-16, 3A-AP-17, 3A-AP-21
**LO**: LO3.1, LO3.2, LO3.3, LO4.1, LO4.2

---

*End of Week 8 Complete Lesson Series*
