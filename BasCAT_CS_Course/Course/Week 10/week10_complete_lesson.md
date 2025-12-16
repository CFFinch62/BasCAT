# Week 10: Compiler Design & Translation

**Theme**: How High-Level Languages Become Machine Code
**Duration**: 5 days (50 minutes each)

---

## Week 10, Day 1: Compiler Basics

**Topic**: What Compilers Do
**Duration**: 50 minutes
**Learning Objectives**:
- Understand compilation process
- Identify compiler stages
- Trace BASIC to assembly translation
- Use BasCAT's compilation view

### Lesson Overview

**What is a Compiler?**:
"A translator from high-level language to machine code"

**Compilation Stages**:
```
Source Code (BASIC)
    ↓
1. LEXICAL ANALYSIS (tokenize)
    ↓
2. PARSING (build tree)
    ↓
3. CODE GENERATION (assembly)
    ↓
4. ASSEMBLY (machine code)
    ↓
Executable Program
```

**BasCAT Example**:
```basic
10 LET A = 5 + 3
```

**Compiles to**:
```assembly
LOAD A, 5
ADD A, 3
```

**Live Demo**: Use BasCAT's "Show Assembly" feature

**Activity**: Students compile various BASIC statements, analyze assembly output

---

## Week 10, Day 2: Expression Translation

**Topic**: How Math Becomes Machine Code
**Duration**: 50 minutes
**Learning Objectives**:
- Understand expression trees
- Trace arithmetic compilation
- Optimize expressions
- Hand-compile simple expressions

### Key Concepts

**Expression Tree**:
```
A = B + C * D

     =
    / \
   A   +
      / \
     B   *
        / \
       C   D
```

**Evaluation Order** (depth-first, right-to-left):
1. Load D
2. Multiply by C
3. Add B
4. Store in A

**Assembly Output**:
```assembly
LOAD A, D
MOV B, C
; (multiplication would need loop in BasCAT)
ADD A, B
; Store result
```

**Optimization Opportunity**:
```basic
10 LET A = B + C + B
```

**Naive**:
```assembly
LOAD A, B
ADD A, C
ADD A, B      ; B loaded again!
```

**Optimized**:
```assembly
LOAD A, B
ADD A, A      ; Double B
ADD A, C      ; Better!
```

**Activity**: Hand-compile expressions, compare to BasCAT output

---

## Week 10, Day 3: Control Flow Translation

**Topic**: Loops and Conditionals to Assembly
**Duration**: 50 minutes
**Learning Objectives**:
- Understand IF-THEN translation
- Understand FOR loop translation
- Trace control flow compilation
- Optimize conditionals

### Key Concepts

**IF-THEN Translation**:
```basic
10 IF A > 10 THEN PRINT "Big"
```

**Compiles to**:
```assembly
LOAD B, 10
CMP A, B
JNC skip       ; Jump if NOT >
; Print code here
skip:
```

**FOR Loop Translation**:
```basic
10 FOR I = 1 TO 10
20   PRINT I
30 NEXT I
```

**Compiles to**:
```assembly
LOAD I, 1      ; Initialize
loop:
  OUT I        ; Body
  ADD I, 1     ; Increment
  CMP I, 10
  JC loop      ; Continue if < 10
  JZ loop      ; Also if = 10
```

**Nested Loop**:
Multiple counters, multiple labels

**Activity**: Compile various control structures by hand

---

## Week 10, Day 4: Advanced Topics

**Topic**: Optimization and Advanced Compilation
**Duration**: 50 minutes
**Learning Objectives**:
- Understand common optimizations
- Identify optimization opportunities
- Compare optimization levels
- Analyze trade-offs

### Key Concepts

**Common Optimizations**:

1. **Constant Folding**:
```basic
10 LET A = 5 + 3
```
Compiler calculates 8 at compile time!

2. **Dead Code Elimination**:
```basic
10 LET A = 5
20 LET A = 10    ; Line 10 is dead!
```

3. **Common Subexpression**:
```basic
10 LET A = B + C
20 LET D = B + C  ; Reuse result!
```

4. **Loop Invariant**:
```basic
10 FOR I = 1 TO 10
20   LET A = 5 * 3    ; Move outside loop!
30 NEXT I
```

**Trade-offs**:
- Optimization takes time
- May make debugging harder
- Usually worth it for performance

**Activity**: Find optimization opportunities in code samples

---

## Week 10, Day 5: Final Project & Presentations

**Topic**: Comprehensive Course Review
**Duration**: 50 minutes
**Learning Objectives**:
- Synthesize all course concepts
- Demonstrate complete understanding
- Present technical knowledge
- Reflect on learning journey

### Final Project Options

**Option 1: Complete Compiler Analysis**
- Take complex BASIC program
- Show compilation at each stage
- Analyze optimizations
- Suggest improvements

**Option 2: Language Comparison**
- Same program in BASIC, Assembly, Python
- Compare lines of code
- Analyze performance
- Discuss trade-offs

**Option 3: Architecture + Compiler Integration**
- Explain full pipeline: BASIC → Assembly → Machine → Execution
- Show in BasCAT
- Demonstrate understanding
- Create teaching material

**Option 4: Custom Mini-Compiler**
- Design simple language
- Show translation rules
- Implement subset
- Demonstrate with examples

### Requirements

**All Projects**:
- 5-10 minute presentation
- Written report (3-5 pages)
- Working code examples
- Visual aids (diagrams, slides)

**Content Must Show**:
- Assembly knowledge (Weeks 1-6)
- BASIC knowledge (Weeks 7-8)
- Architecture understanding (Week 9)
- Compilation understanding (Week 10)

### Rubric (100 points - Major Project)

**Technical Content (40)**:
- Correct concepts (15)
- Depth of understanding (15)
- Integration of topics (10)

**Presentation (30)**:
- Clarity (10)
- Organization (10)
- Visual aids (10)

**Code/Examples (20)**:
- Working demonstrations (10)
- Well-documented (5)
- Appropriate complexity (5)

**Reflection (10)**:
- Learning growth
- Connections made
- Future applications

**Bonus (+20)**:
- Exceptional insight
- Creative approach
- Teaching quality
- Depth beyond requirements

---

## Course Final Assessment

### Written Exam (100 points)

**Part 1: Assembly (25 pts)**
- Write assembly program
- Debug assembly code
- Optimize assembly
- Trace execution

**Part 2: BASIC (25 pts)**
- Write BASIC program
- Convert assembly to BASIC
- Use arrays and loops
- Fix BASIC bugs

**Part 3: Architecture (25 pts)**
- Label CPU diagram
- Explain memory hierarchy
- Describe I/O systems
- Analyze performance

**Part 4: Compilation (25 pts)**
- Show compilation stages
- Hand-compile expressions
- Identify optimizations
- Explain trade-offs

### Practical Exam (100 points)

**Challenge 1: Assembly (30 pts)**
- Implement algorithm in assembly
- Working code
- Efficient solution
- Good documentation

**Challenge 2: BASIC (30 pts)**
- Create interactive program
- Use all major features
- Error handling
- User-friendly

**Challenge 3: Analysis (20 pts)**
- Given program, analyze
- Find bottlenecks
- Suggest improvements
- Justify choices

**Challenge 4: Integration (20 pts)**
- Show BASIC → Assembly
- Explain compilation
- Discuss architecture
- Demonstrate understanding

---

## Course Conclusion

### Reflection Activity

**Discussion Questions**:
1. What was most challenging?
2. What was most interesting?
3. How did assembly-first help?
4. What will you remember?
5. How will you use this knowledge?

### Student Accomplishments

**You Can Now**:
- ✓ Write assembly programs
- ✓ Write BASIC programs
- ✓ Understand CPU architecture
- ✓ Explain compilation
- ✓ Optimize code
- ✓ Debug low-level programs
- ✓ Make informed language choices
- ✓ Understand computer fundamentals

### Looking Forward

**Next Steps**:
- Learn modern languages (Python, JavaScript, C++)
- Study operating systems
- Explore compiler design
- Build embedded systems
- Understand computer engineering

**This Course Foundation**:
"You learned how computers REALLY work. This understanding will help you forever in programming!"

---

## Standards Alignment

**CSTA Standards** (Comprehensive):
- 3A-AP-13: Create prototypes using algorithms
- 3A-AP-16: Design and iteratively develop programs
- 3A-AP-17: Decompose problems
- 3A-AP-21: Evaluate and refine artifacts
- 3A-CS-01: Explain abstractions
- 3A-CS-02: Compare levels of abstraction
- 3A-DA-09: Translate between representations
- 3A-DA-10: Evaluate trade-offs

**All 20 Learning Objectives**: ✓ Complete

---

## Teacher Notes

### Course Success Indicators

**Students Should**:
- Feel confident with assembly
- Appreciate high-level languages
- Understand computer architecture
- Think about abstraction layers
- Debug at multiple levels

### Common Final Struggles:
- Integrating all concepts
- Time management on projects
- Presentation anxiety
- Scope of final project

### Celebrate**:
- This is a HARD course
- Students learned CS fundamentals
- Real, valuable knowledge
- Foundation for future learning

---

*End of Week 10 Complete Lesson Series*
*END OF 10-WEEK INTENSIVE CURRICULUM*

## Course Overview Complete

**Weeks 1-6**: Assembly Programming (30 lessons)
**Weeks 7-8**: BASIC Programming (10 lessons)
**Week 9**: Computer Architecture (5 lessons)
**Week 10**: Compiler Design (5 lessons)

**Total**: 50 complete lessons spanning 10 weeks!

**Remaining in 15-week course**:
- Weeks 11-15: Advanced topics, projects, review (can be flexible based on student needs)
