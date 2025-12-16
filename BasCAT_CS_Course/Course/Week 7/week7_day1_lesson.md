# Week 7, Day 1: Introduction to BASIC

**Topic**: First BASIC Program and Language Comparison
**Duration**: 50 minutes
**Learning Objectives**:
- Understand high-level vs low-level languages
- Write first BASIC program
- Compare BASIC to assembly
- Use BasCAT's BASIC mode

---

## Materials Needed

- Computers with BasCAT
- Week 6 projects (graded, ready to return)
- Handout: "BASIC Quick Reference"
- Assembly vs BASIC comparison chart

---

## Lesson Outline

### Warm-Up / Week 6 Celebration & Bridge (8 minutes)

**Return Week 6 Projects**:
- Celebrate assembly mastery!
- Highlight exceptional projects
- "You now understand how computers REALLY work at the lowest level!"

**The Assembly Challenge**:
Show assembly code on board:
```assembly
; Add two numbers and output
IN A
IN B
ADD A, B
OUT A
HALT
```

"This took 5 lines. What if we want to add 100 numbers? Or do complex math?"

**The Solution**: High-Level Languages!

**Same Program in BASIC**:
```basic
10 INPUT A
20 INPUT B
30 PRINT A + B
40 END
```

"Same functionality, easier to read, faster to write!"

**Today's Mission**: "Learn BASIC while understanding what happens 'under the hood' in assembly!"

### Direct Instruction: BASIC Fundamentals (14 minutes)

**What is BASIC?**

"BASIC = Beginner's All-purpose Symbolic Instruction Code
- Created in 1964 for teaching
- High-level language (close to human language)
- Easier than assembly
- BUT: Computer still runs assembly underneath!"

**The Magic of BasCAT**:
"BasCAT compiles BASIC → Assembly → Machine Code
You can SEE both languages side-by-side!"

**BASIC Program Structure**:

1. **Line Numbers** (required in classic BASIC)
```basic
10 REM This is line 10
20 REM This is line 20
```
"Lines execute in order by number (10, 20, 30...)"

2. **REM Statements** (comments)
```basic
10 REM This is a comment
20 REM Compiler ignores this
```

3. **Variables** (no declaration needed)
```basic
10 LET A = 5
20 LET B = 10
```
"Variables A-Z available automatically!"

**First BASIC Program**:
```basic
10 REM My First BASIC Program
20 PRINT "Hello, World!"
30 END
```

**Line by Line**:
- Line 10: Comment (ignored)
- Line 20: Print text to screen
- Line 30: End program

**Run in BasCAT**:
1. Switch to BASIC mode
2. Type program
3. Click Compile
4. Watch: BASIC → Assembly → Execute
5. See "Hello, World!" in output

**Key Differences from Assembly**:

| Aspect | Assembly | BASIC |
|--------|----------|-------|
| Readability | Cryptic | Human-friendly |
| Variables | Registers (A-D) | Named (A-Z) |
| Math | ADD A, B | A = A + B |
| Output | OUT A | PRINT A |
| Input | IN A | INPUT A |
| Length | Many lines | Fewer lines |

**Under the Hood**:
```basic
10 LET A = 5
20 LET B = 10
30 LET C = A + B
40 PRINT C
50 END
```

**Compiles to Assembly** (show in BasCAT):
```assembly
LOAD A, 5      ; Line 10
LOAD B, 10     ; Line 20
MOV C, A       ; Line 30
ADD C, B       ; Line 30
OUT C          ; Line 40
HALT           ; Line 50
```

"BASIC is EASIER, but assembly still runs underneath!"

### Guided Practice: BASIC Programs (15 minutes)

**Challenge 1: Simple Output** (5 min)

"Write BASIC program to output your age"
```basic
10 REM Output my age
20 LET AGE = 16
30 PRINT AGE
40 END
```

**Run it**, then click "Show Assembly" to see compiled code!

**Challenge 2: Simple Math** (5 min)

"Calculate area of rectangle (length × width)"
```basic
10 REM Rectangle Area
20 LET LENGTH = 10
30 LET WIDTH = 5
40 LET AREA = LENGTH * WIDTH
50 PRINT AREA
60 END
```

**Key Point**: Multiplication with `*` symbol (assembly didn't have this!)

**Challenge 3: Interactive Input** (5 min)

"Read two numbers, output sum"
```basic
10 REM Add Two Numbers
20 INPUT A
30 INPUT B
40 LET SUM = A + B
50 PRINT SUM
60 END
```

**Compare to Assembly**:
- Assembly: `IN A`, `IN B`, `ADD A, B`, `OUT A`
- BASIC: `INPUT A`, `INPUT B`, `PRINT A + B`

"Notice: BASIC can do math in PRINT statement!"

### Independent Practice: BASIC Exploration (10 minutes)

**Level 1 - Basic: Personal Info**
```basic
10 REM Personal Information
20 LET NAME$ = "Your Name"
30 LET AGE = 16
40 PRINT "Name: "; NAME$
50 PRINT "Age: "; AGE
60 END
```

*Note: Some BASIC variants use $ for strings*

**Level 2 - Intermediate: Calculator**
```basic
10 REM Simple Calculator
20 INPUT "First number: "; A
30 INPUT "Second number: "; B
40 PRINT "Sum: "; A + B
50 PRINT "Difference: "; A - B
60 PRINT "Product: "; A * B
70 END
```

**Level 3 - Advanced: Temperature Converter**
```basic
10 REM Fahrenheit to Celsius
20 INPUT "Fahrenheit: "; F
30 LET C = (F - 32) * 5 / 9
40 PRINT "Celsius: "; C
50 END
```

"Notice: Complex math in one line! Assembly would need many instructions."

### Class Discussion: High-Level Abstraction (8 minutes)

**Why Learn Assembly First?**

"You've seen assembly for 6 weeks. Now BASIC seems EASY! Here's why this order matters:"

**Understanding**:
- You know what `A + B` really means (load, add, store)
- You appreciate what compiler does
- You understand performance implications
- You can debug better

**The Abstraction Ladder**:
```
High Level (Easy)  →  BASIC, Python, JavaScript
                      ↓ (compile/interpret)
Low Level (Hard)   →  Assembly
                      ↓ (assemble)
Machine Code       →  Binary (0s and 1s)
```

"Each level hides complexity but costs performance!"

**Performance Example**:
```basic
10 LET A = 5
20 LET B = 10
30 LET C = A + B + A * B
```

**Compiles to** ~8-10 assembly instructions!

**Trade-offs**:
- **BASIC**: Fast to write, easier to read, slower to run
- **Assembly**: Slow to write, harder to read, faster to run

**Real-World**:
- Operating systems: C/Assembly (speed critical)
- Applications: Python/JavaScript (development speed critical)
- Games: Mix of both (engines in C++, scripts in Lua/Python)

**Interactive Question**: "When would you use assembly vs BASIC?"

Answers:
- Assembly: Device drivers, embedded systems, performance-critical code
- BASIC/High-level: Apps, websites, most programming

---

## Closure / Exit Ticket (5 minutes)

**Quick Write**:

Write BASIC program to:
1. Store value 100 in variable
2. Add 50 to it
3. Print result

**Expected Answer**:
```basic
10 LET A = 100
20 LET B = A + 50
30 PRINT B
40 END
```

**Collect**: Exit tickets

**Preview Tomorrow**:
"BASIC control flow - IF statements and loops (much easier than assembly jumps!)"

---

## Homework

**Assignment**: "BASIC Practice"

**Program 1**: Personal Calculator
```basic
10 REM My Calculator
20 INPUT "Number 1: "; A
30 INPUT "Number 2: "; B
40 PRINT "Sum: "; A + B
50 PRINT "Product: "; A * B
60 PRINT "Average: "; (A + B) / 2
70 END
```

**Program 2**: Circle Calculations
```basic
10 REM Circle Area and Circumference
20 LET PI = 3.14159
30 INPUT "Radius: "; R
40 LET AREA = PI * R * R
50 LET CIRC = 2 * PI * R
60 PRINT "Area: "; AREA
70 PRINT "Circumference: "; CIRC
80 END
```

**Program 3**: Compare Assembly and BASIC
Write SAME program in both languages:
- Read a number
- Double it
- Output result

Compare line counts!

**Challenge**: Use BasCAT's "Show Assembly" feature to see what your BASIC programs compile to. How many assembly instructions does line 40 generate in Program 2?

**Due**: Next class
**Submit**: `week7_day1_homework.bas`

---

## Assessment

### Formative:
- ✓ Exit ticket (basic BASIC syntax)
- ✓ Program execution
- ✓ Language comparison understanding
- ✓ Compilation observation

### Success Criteria:
- Student can write simple BASIC program
- Student understands line numbers
- Student can use LET, PRINT, INPUT
- Student appreciates high-level abstraction

---

## Differentiation

### For Struggling Students:
- **Templates**: Provide program structures
- **Line-by-line**: Break down each statement
- **Buddy System**: Pair with assembly-strong student
- **Visual**: Color-code syntax

### For Advanced Students:
- **Efficiency**: Compare assembly output of different BASIC approaches
- **Optimization**: Write BASIC that generates minimal assembly
- **Research**: Other high-level languages
- **Extension**: String manipulation in BASIC

### For ELL Students:
- **Vocabulary**: Variable, assign, print, input, line number
- **Syntax Guide**: Always visible
- **Sentence Frames**:
  - "Line ___ does ___"
  - "PRINT displays ___"
- **Native Language**: Comments can be in native language

---

## Teacher Notes

### Common Errors:

1. **"I forgot line numbers!"**
   - Every line needs a number
   - Use increments of 10 (allows inserting lines later)

2. **"LET vs = confusion"**
   - Some BASIC: `LET A = 5`
   - Some BASIC: `A = 5`
   - BasCAT uses LET

3. **"My program doesn't end"**
   - Must have END statement
   - Like HALT in assembly

4. **"I can't see the assembly"**
   - Use "Show Assembly" button
   - Compile first, then view

### Time Management:
- If running short: Skip Level 3 practice
- If running long: More assembly comparison
- Ensure all students compile at least one program

### Setup:
- [ ] BasCAT in BASIC mode
- [ ] Test all example programs
- [ ] Print BASIC reference cards
- [ ] Assembly comparison ready

### Follow-Up:
- Review exit tickets - BASIC syntax clear?
- Prepare IF/GOTO for tomorrow
- Create control flow examples

---

## Handout: BASIC Quick Reference

```
╔════════════════════════════════════════════╗
║         BASIC QUICK REFERENCE              ║
╠════════════════════════════════════════════╣
║                                            ║
║  PROGRAM STRUCTURE:                        ║
║  10 REM Comment                            ║
║  20 LET A = 5                              ║
║  30 PRINT A                                ║
║  40 END                                    ║
║                                            ║
║  LINE NUMBERS:                             ║
║  • Required for every line                 ║
║  • Execute in numeric order                ║
║  • Use increments of 10                    ║
║  • Can insert lines later (15, 25, etc)    ║
║                                            ║
║  COMMENTS:                                 ║
║  10 REM This is a comment                  ║
║  • REM = Remark                            ║
║  • Ignored by compiler                     ║
║  • Use for documentation                   ║
║                                            ║
║  VARIABLES:                                ║
║  LET A = 5        Assign value             ║
║  LET B = A + 10   Calculate                ║
║  • Variables A-Z available                 ║
║  • No declaration needed                   ║
║  • Case insensitive (A = a)                ║
║                                            ║
║  INPUT/OUTPUT:                             ║
║  INPUT A          Read into A              ║
║  INPUT "Age: "; A Prompt and read          ║
║  PRINT A          Display value            ║
║  PRINT "Hello"    Display text             ║
║  PRINT A; B       Multiple values          ║
║                                            ║
║  ARITHMETIC:                               ║
║  +   Addition                              ║
║  -   Subtraction                           ║
║  *   Multiplication                        ║
║  /   Division                              ║
║  ^   Power (exponent)                      ║
║                                            ║
║  EXAMPLE PROGRAMS:                         ║
║                                            ║
║  Simple Math:                              ║
║  10 LET A = 5                              ║
║  20 LET B = 10                             ║
║  30 LET C = A + B                          ║
║  40 PRINT C                                ║
║  50 END                                    ║
║                                            ║
║  Interactive:                              ║
║  10 INPUT "Name: "; N$                     ║
║  20 INPUT "Age: "; A                       ║
║  30 PRINT "Hello "; N$                     ║
║  40 PRINT "You are "; A                    ║
║  50 END                                    ║
║                                            ║
║  KEY POINTS:                               ║
║  • Much easier than assembly!              ║
║  • Still compiles to assembly underneath   ║
║  • Can view compiled assembly in BasCAT    ║
║  • Trade-off: Easier to write, slower      ║
║                                            ║
╚════════════════════════════════════════════╝
```

---

## Standards Alignment

**CSTA Standards**:
- 3A-AP-13: Create prototypes using algorithms
- 3A-CS-02: Compare levels of abstraction

**Learning Objectives**:
- LO3.1: Write functional BASIC programs
- LO5.1: Explain abstraction layers
- LO5.2: Compare high-level vs low-level languages

---

*End of Week 7, Day 1 Lesson Plan*
