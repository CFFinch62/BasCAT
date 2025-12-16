# Week 12: Real-World Computer Systems

**Theme**: Modern Computing and Professional Applications
**Duration**: 5 days (50 minutes each)

---

## Week 12, Day 1: Operating Systems Concepts

**Topic**: How Operating Systems Work
**Learning Objectives**: Understand OS role, processes, memory management

### Key Concepts
- **OS Responsibilities**: Process management, memory, I/O, file systems
- **BasCAT Connection**: Simple OS-like behavior (single program execution)
- **Scheduling**: How multiple programs share CPU
- **Protection**: Isolating programs from each other

**Activity**: Design simple task scheduler on paper

---

## Week 12, Day 2: Embedded Systems

**Topic**: Computers in Everyday Devices
**Learning Objectives**: Understand embedded programming, resource constraints

### Key Concepts
- **What are Embedded Systems**: Car controllers, appliances, IoT
- **Constraints**: Limited memory, power, speed
- **Assembly Advantage**: Direct hardware control, efficiency
- **Real Examples**: Arduino, Raspberry Pi Pico

**Activity**: Design washing machine controller logic

---

## Week 12, Day 3: Network Communication

**Topic**: How Computers Talk to Each Other
**Learning Objectives**: Understand protocols, packets, networking

### Key Concepts
- **Network Basics**: IP, TCP/UDP, packets
- **I/O Parallel**: Like BasCAT's IN/OUT but over network
- **Protocols**: Rules for communication
- **Internet Architecture**: Layers of abstraction

**Activity**: Simulate packet transmission with students

---

## Week 12, Day 4: Security Fundamentals

**Topic**: Computer Security Basics
**Learning Objectives**: Understand vulnerabilities, encryption, safe coding

### Key Concepts
- **Buffer Overflow**: Memory safety (stack/memory corruption)
- **Encryption**: XOR cipher (students know this from Week 3!)
- **Access Control**: Permission bits
- **Safe Coding**: Validate input, check bounds

**Activity**: Exploit simple buffer overflow, then fix it

---

## Week 12, Day 5: Lab Day - System Simulation

**Project Options**:
1. **Simple OS Simulator**: Round-robin scheduler
2. **Network Protocol**: Simple message passing
3. **Security Tool**: Encryption/decryption system
4. **Embedded Controller**: Traffic light controller

**Rubric** (50 pts): Functionality (20), Concepts (15), Code (10), Documentation (5)

---

# Week 13: Advanced BASIC Programming

**Theme**: Complex Applications and Software Engineering
**Duration**: 5 days (50 minutes each)

---

## Week 13, Day 1: Modular Programming

**Topic**: Breaking Programs into Modules
**Learning Objectives**: Design with subroutines, separation of concerns

### Key Concepts
```basic
100 REM Main program
110 GOSUB 1000   REM Initialize
120 GOSUB 2000   REM Get input
130 GOSUB 3000   REM Process
140 GOSUB 4000   REM Output
150 END

1000 REM Initialize module
1010 LET X = 0
1020 RETURN

2000 REM Input module
2010 INPUT A, B
2020 RETURN
```

---

## Week 13, Day 2: Error Handling

**Topic**: Robust Programming
**Learning Objectives**: Validate input, handle errors gracefully

```basic
10 INPUT "Enter 1-10: "; N
20 IF N < 1 OR N > 10 THEN GOTO 100
30 PRINT "Valid!"
40 END
100 REM Error handler
110 PRINT "Invalid input!"
120 GOTO 10
```

---

## Week 13, Day 3: Algorithm Implementation

**Topic**: Classic Algorithms in BASIC
**Learning Objectives**: Implement search, sort, other algorithms

- Linear search
- Bubble sort (simplified)
- Finding min/max
- Calculating statistics

---

## Week 13, Day 4: User Interface Design

**Topic**: Creating User-Friendly Programs
**Learning Objectives**: Menu design, prompts, formatting

```basic
10 REM Menu system
20 PRINT "===== CALCULATOR ====="
30 PRINT "1. Add"
40 PRINT "2. Subtract"
50 PRINT "3. Exit"
60 PRINT "======================"
70 INPUT "Choice: "; C
```

---

## Week 13, Day 5: Lab Day - Complete Application

**Project**: Build comprehensive BASIC application
- Menu-driven interface
- Multiple features
- Error handling
- Good UX

**Rubric** (50 pts): Same as Week 8 project

---

# Week 14: Integration & Cross-Language Programming

**Theme**: Combining Assembly and BASIC
**Duration**: 5 days (50 minutes each)

---

## Week 14, Day 1: When to Use Each Language

**Topic**: Language Selection Criteria
**Learning Objectives**: Choose appropriate language for task

### Decision Matrix

| Criterion | Assembly | BASIC |
|-----------|----------|-------|
| Speed critical? | ✓ | |
| Hardware control? | ✓ | |
| Quick development? | | ✓ |
| Easy maintenance? | | ✓ |
| Complex logic? | | ✓ |
| Limited resources? | ✓ | |

---

## Week 14, Day 2: Translation Practice

**Topic**: Converting Between Languages
**Learning Objectives**: Translate BASIC ↔ Assembly

**Exercise**: Given BASIC program, write assembly equivalent
**Exercise**: Given assembly, write BASIC equivalent

---

## Week 14, Day 3: Performance Comparison

**Topic**: Measuring and Analyzing Performance
**Learning Objectives**: Compare execution speed, code size

**Activity**:
- Same algorithm in both languages
- Count instructions (assembly)
- Measure development time
- Analyze trade-offs

---

## Week 14, Day 4: Optimization Across Languages

**Topic**: Writing Efficient Code in Any Language
**Learning Objectives**: Universal optimization principles

- Algorithm choice matters most
- Avoid redundant work
- Minimize I/O
- Cache results

---

## Week 14, Day 5: Lab Day - Hybrid Project

**Project**: Create program demonstrating both languages
- Core logic in assembly
- User interface in BASIC
- OR: Performance-critical parts in assembly
- OR: Comparison project showing both

**Rubric** (50 pts): Both languages (20), Integration (15), Analysis (10), Documentation (5)

---

# Week 15: Final Projects & Course Conclusion

**Theme**: Capstone Projects and Reflection
**Duration**: 5 days (50 minutes each)

---

## Week 15, Day 1: Final Project Kick-off

**Topic**: Project Planning and Specification

### Project Options

**Option 1: Advanced Game**
- Complex logic
- Multiple levels/states
- Score tracking
- Assembly or BASIC

**Option 2: Utility Program**
- Calculator with many functions
- Data analysis tool
- Text processor
- Any language

**Option 3: Educational Tool**
- Tutorial program
- Quiz system
- Demonstration
- Mixed languages

**Option 4: Original Creation**
- Student's choice
- Must demonstrate mastery
- Requires approval

### Requirements
- Demonstrates 5+ major concepts from course
- Well-documented
- Polished, user-friendly
- Presentation ready

**Day 1 Activity**: Design and get approval

---

## Week 15, Day 2: Project Work Day

**Full class period for development**

**Teacher Support**:
- Code review
- Debugging help
- Design feedback
- Scope management

**Checkpoint**: Core functionality working

---

## Week 15, Day 3: Project Work Day

**Continued development**

**Focus**:
- Polish features
- Test thoroughly
- Complete documentation
- Prepare presentation

**Checkpoint**: Feature complete, testing in progress

---

## Week 15, Day 4: Presentations & Peer Review

**Format**: 5-minute presentations
- Demo program
- Explain design decisions
- Show code highlights
- Answer questions

**Peer Feedback**: Written forms
**Teacher Assessment**: Using final rubric

---

## Week 15, Day 5: Course Conclusion & Final Exam

### Morning: Final Exam (2 hours if available)

**Written Portion** (100 pts):
- Assembly programming (25)
- BASIC programming (25)
- Architecture concepts (25)
- Compilation/translation (25)

**Practical Portion** (100 pts):
- Implement algorithm in assembly (50)
- Implement algorithm in BASIC (50)

### Afternoon: Course Reflection

**Discussion Topics**:
1. What was most valuable?
2. What was most challenging?
3. How did learning order help?
4. Where will you use this knowledge?
5. What would you teach differently?

**Student Presentations**: Course highlights

**Celebration**: Recognize achievements
- Most optimized code
- Most creative project
- Most improved
- Best documentation
- Helping others award

**Looking Forward**:
- Next steps in CS
- Recommended courses
- Project ideas
- Career paths

---

## Week 15 Final Project Rubric (150 points)

**Functionality** (50 pts):
- All features work (25)
- Handles edge cases (15)
- No critical bugs (10)

**Technical Depth** (40 pts):
- Demonstrates multiple concepts (15)
- Appropriate complexity (15)
- Efficient implementation (10)

**Code Quality** (30 pts):
- Well-organized (10)
- Properly commented (10)
- Good style (10)

**Documentation** (15 pts):
- User guide (8)
- Code comments (7)

**Presentation** (15 pts):
- Clear demonstration (8)
- Explains choices (7)

**Bonus** (+20 pts):
- Exceptional quality (+10)
- Creative innovation (+5)
- Helps classmates (+5)

---

## Course Final Grades

**Breakdown**:
- Projects (4 major): 40%
- Quizzes (weekly): 20%
- Final Exam: 20%
- Final Project: 15%
- Participation: 5%

**Total**: 100%

---

## Teacher Notes - Course Completion

### Successful Completion Indicators

**Students Should**:
- Write assembly confidently
- Understand computer architecture
- Appreciate high-level languages
- Make informed design choices
- Debug systematically
- Think about performance
- Document professionally

### Common Final Project Issues
- Scope too ambitious
- Last-minute debugging
- Presentation anxiety
- Integration challenges

### Celebration Ideas
- Code showcase event
- Invite parents/admin
- Portfolio creation
- GitHub publication
- Certificate of completion

### Future Directions

**Recommend Next Courses**:
- Data Structures (Python/Java)
- Operating Systems
- Computer Architecture (university level)
- Embedded Systems
- Compiler Design
- Software Engineering

**Self-Study Resources**:
- Modern assembly (x86, ARM)
- C programming
- Arduino/Raspberry Pi
- Competitive programming

---

## Standards Alignment (Complete Course)

**CSTA 3A Standards - All Addressed**:
- ✓ 3A-AP-13: Create prototypes using algorithms
- ✓ 3A-AP-16: Design and develop computational artifacts
- ✓ 3A-AP-17: Decompose problems
- ✓ 3A-AP-21: Evaluate and refine artifacts
- ✓ 3A-CS-01: Explain abstractions
- ✓ 3A-CS-02: Compare levels of abstraction
- ✓ 3A-DA-09: Translate between representations
- ✓ 3A-DA-10: Evaluate trade-offs

**All 20 Learning Objectives**: ✓ Completed

---

## Course Success Metrics

**By End of Course, Students Can**:
- ✓ Write complete assembly programs
- ✓ Write complete BASIC programs
- ✓ Explain CPU architecture
- ✓ Trace program execution
- ✓ Optimize code for performance
- ✓ Debug effectively
- ✓ Choose appropriate languages
- ✓ Design complex algorithms
- ✓ Document professionally
- ✓ Present technical work

**This Course Provides**:
- Foundation for all CS study
- Understanding of computer fundamentals
- Appreciation for abstraction
- Practical programming skills
- Problem-solving abilities
- Professional development practices

---

*END OF 15-WEEK BASCAT CURRICULUM*
*COMPLETE COURSE - ALL WEEKS DONE!*

## Summary

**Weeks 1-6**: Assembly Programming Foundation
**Weeks 7-8**: BASIC Programming
**Week 9**: Computer Architecture
**Week 10**: Compiler Design
**Week 11**: Advanced Assembly
**Week 12**: Real-World Systems
**Week 13**: Advanced BASIC
**Week 14**: Integration
**Week 15**: Final Projects & Conclusion

**Total**: 75 complete lesson plans across 15 weeks!
