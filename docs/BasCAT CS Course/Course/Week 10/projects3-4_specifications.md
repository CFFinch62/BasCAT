# Project 3: BASIC Application

**Week**: 10 (End of BASIC unit)
**Duration**: 3-4 class periods
**Points**: 100
**Type**: Individual project

---

## Project Overview

Create a comprehensive BASIC program demonstrating mastery of high-level programming concepts while understanding the assembly code it generates.

---

## Project Options

### Option 1: Grade Management System
- Store student names and grades
- Calculate averages
- Find highest/lowest
- Display formatted report

### Option 2: Inventory System
- Track items and quantities
- Add/remove items
- Search for items
- Display inventory

### Option 3: Text Adventure Game
- Multiple rooms/locations
- Player choices
- Inventory system
- Win/lose conditions

### Option 4: Math Tutor
- Generate practice problems
- Check answers
- Track score
- Multiple difficulty levels

---

## Requirements

**Must Include**:
1. Arrays (at least 2 arrays)
2. FOR loops (at least 2)
3. IF-THEN statements (at least 5)
4. GOSUB/RETURN (at least 3 subroutines)
5. INPUT statements (user interaction)
6. PRINT statements (formatted output)
7. String operations (if applicable)
8. Menu system
9. Error handling
10. Comments and documentation

**Bonus**:
- Assembly comparison (+10)
- Advanced features (+5)
- Exceptional UX (+5)

---

## Example: Grade Management System

```basic
100 REM ===================================
110 REM  GRADE MANAGEMENT SYSTEM
120 REM  Author: Solution Key
130 REM ===================================
140
150 REM Initialize
160 DIM NAMES$(10)
170 DIM GRADES(10)
180 LET COUNT = 0
190
200 REM Main Menu
210 PRINT "===== GRADE MANAGER ====="
220 PRINT "1. Add Student"
230 PRINT "2. View All"
240 PRINT "3. Calculate Average"
250 PRINT "4. Find Highest"
260 PRINT "5. Exit"
270 PRINT "======================"
280 INPUT "Choice: "; C
290
300 IF C = 1 THEN GOSUB 1000
310 IF C = 2 THEN GOSUB 2000
320 IF C = 3 THEN GOSUB 3000
330 IF C = 4 THEN GOSUB 4000
340 IF C = 5 THEN END
350 GOTO 200
360
1000 REM Add Student Subroutine
1010 IF COUNT >= 10 THEN PRINT "Full!": RETURN
1020 LET COUNT = COUNT + 1
1030 INPUT "Name: "; NAMES$(COUNT)
1040 INPUT "Grade: "; GRADES(COUNT)
1050 PRINT "Added!"
1060 RETURN
1070
2000 REM View All Subroutine
2010 IF COUNT = 0 THEN PRINT "No students!": RETURN
2020 FOR I = 1 TO COUNT
2030   PRINT NAMES$(I); ": "; GRADES(I)
2040 NEXT I
2050 RETURN
2060
3000 REM Calculate Average Subroutine
3010 IF COUNT = 0 THEN PRINT "No students!": RETURN
3020 LET SUM = 0
3030 FOR I = 1 TO COUNT
3040   LET SUM = SUM + GRADES(I)
3050 NEXT I
3060 PRINT "Average: "; SUM / COUNT
3070 RETURN
3080
4000 REM Find Highest Subroutine
4010 IF COUNT = 0 THEN PRINT "No students!": RETURN
4020 LET HIGH = GRADES(1)
4030 LET HIGHNAME$ = NAMES$(1)
4040 FOR I = 2 TO COUNT
4050   IF GRADES(I) > HIGH THEN HIGH = GRADES(I)
4060   IF GRADES(I) > HIGH THEN HIGHNAME$ = NAMES$(I)
4070 NEXT I
4080 PRINT "Highest: "; HIGHNAME$; " - "; HIGH
4090 RETURN
4100
9999 END
```

---

## Rubric (100 points)

**Functionality (40)**:
- All features work (40)
- Most features work (30)
- Some features work (20)

**BASIC Features (30)**:
- Arrays (5)
- Loops (5)
- Conditionals (5)
- Subroutines (5)
- I/O (5)
- Menu system (5)

**Code Quality (15)**:
- Organization (5)
- Comments (5)
- Style (5)

**User Experience (10)**:
- Clear prompts (5)
- Error handling (5)

**Documentation (5)**:
- Header complete (3)
- Instructions (2)

**Bonus (+20)**:
- Assembly analysis (+10)
- Advanced features (+5)
- Exceptional quality (+5)

---

# Project 4: Final Capstone Project

**Week**: 15 (Final project)
**Duration**: Full week (5 class periods)
**Points**: 150
**Type**: Individual project

---

## Project Overview

The ultimate demonstration of mastery - students create an original program showcasing everything learned across the entire course.

---

## Requirements

### Must Demonstrate

**From Assembly Unit**:
1. Understanding of low-level operations
2. Memory management concepts
3. Stack usage
4. Optimization awareness

**From BASIC Unit**:
5. High-level programming
6. Structured design
7. Modular programming

**From Architecture Unit**:
8. Understanding of compilation
9. Performance considerations
10. System design

**Integration**:
11. Choose appropriate language for task
12. Justify language choice
13. Demonstrate trade-offs

---

## Project Options

### Option A: Language Comparison Project
Create SAME program in both assembly and BASIC:
- Document development time
- Compare code size
- Analyze performance
- Discuss trade-offs
- Presentation showing both

### Option B: Educational Tool
Create program that teaches CS concept:
- Interactive tutorial
- Visual demonstrations
- Quiz component
- Help system
- Teaching effectiveness

### Option C: Complex Application
Build sophisticated program in chosen language:
- Multiple integrated features
- Professional quality
- Complete documentation
- User manual
- Technical writeup

### Option D: Research Project
Deep dive into specific topic:
- Computer architecture
- Compiler optimization
- Memory systems
- I/O architectures
- Write comprehensive report
- Create working demonstrations

---

## Deliverables

1. **Working Program** (50%)
2. **Written Report** (25%)
3. **Presentation** (15%)
4. **Documentation** (10%)

### Written Report Requirements
- 3-5 pages
- Design decisions explained
- Challenges and solutions
- Lessons learned
- Future improvements

### Presentation Requirements
- 5-10 minutes
- Live demonstration
- Technical explanation
- Q&A prepared

---

## Example: Language Comparison (Calculator)

**Same calculator in both languages**

**Assembly Version** (~50 lines):
```assembly
; Detailed assembly implementation
; Optimized for performance
```

**BASIC Version** (~20 lines):
```basic
100 REM Same functionality
110 REM Easier to write/maintain
```

**Report Sections**:
1. **Introduction**: Project goals
2. **Design**: Algorithm explanation
3. **Assembly**: Implementation details, line count, time
4. **BASIC**: Implementation details, line count, time
5. **Comparison**: Side-by-side analysis
6. **Performance**: Instruction count, optimization
7. **Conclusion**: When to use each

---

## Rubric (150 points)

### Program Functionality (50)
- **50**: Exceptional, exceeds requirements
- **40**: All features work perfectly
- **30**: Most features work well
- **20**: Core features work
- **10**: Minimal functionality

### Technical Depth (30)
- Demonstrates multiple concepts (10)
- Appropriate complexity (10)
- Shows understanding (10)

### Written Report (25)
- Clear writing (8)
- Technical accuracy (8)
- Depth of analysis (9)

### Presentation (15)
- Clear demonstration (5)
- Explains concepts (5)
- Answers questions (5)

### Documentation (10)
- Code comments (5)
- User guide (5)

### Integration (10)
- Shows course concepts (5)
- Makes connections (5)

### Creativity (10)
- Original thinking (5)
- Innovative approach (5)

### Bonus (+20)
- Exceptional quality (+10)
- Research beyond course (+5)
- Helps others (+5)

---

## Timeline

**Day 1**: Planning and approval
**Day 2-3**: Development
**Day 4**: Testing and documentation
**Day 5**: Presentations

---

## Grading Criteria

### Excellent (135-150)
- Publication-quality work
- Deep understanding
- Creative and thorough

### Good (120-134)
- Professional quality
- Solid understanding
- Well-executed

### Satisfactory (105-119)
- Meets requirements
- Demonstrates competency
- Adequate execution

### Needs Improvement (90-104)
- Partial requirements
- Basic understanding
- Incomplete

---

## Success Indicators

Students should:
- ✓ Integrate multiple concepts
- ✓ Write at professional level
- ✓ Debug independently
- ✓ Present confidently
- ✓ Explain design choices
- ✓ Reflect on learning

---

## Standards Alignment

**CSTA**: All course standards
**LOs**: All 20 learning objectives

---

*End of All Project Specifications*
*Phase 4 COMPLETE!*
