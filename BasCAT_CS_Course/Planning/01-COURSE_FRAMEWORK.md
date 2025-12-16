# BasCAT Computer Architecture Course Framework

**Course Title**: Understanding Computers from the Ground Up **Platform**: BasCAT (Basic Computer Architecture Trainer) **Duration**: 15 weeks (semester) or 6 weeks (intensive summer) **Level**: High School / College Freshman / Advanced Middle School

------

## Course Philosophy

### Core Principle

**Concrete before Abstract**: Students learn assembly language first to understand what computers *actually do*, then learn high-level languages to see how abstraction works. No magic, no black boxes.

### Educational Approach

- **Visual Learning**: Circuit animations show data flow in real-time
- **Hands-On First**: Programming from day one
- **Progressive Complexity**: Each concept builds on previous understanding
- **Critical Thinking**: Why do computers work this way? What are the tradeoffs?

### Chuck's Pedagogical Values (Built Into Course)

- Understanding over memorization
- Process over product
- Questions encouraged
- Multiple paths to solutions
- Struggle is part of learning

------

## Course-Level Learning Objectives

By the end of this course, students will be able to:

### 1. Computer Architecture Understanding

- **LO1.1**: Explain the purpose and function of CPU components (ALU, registers, control unit)
- **LO1.2**: Trace data flow through a computer system (buses, memory, I/O)
- **LO1.3**: Describe the fetch-decode-execute cycle
- **LO1.4**: Explain how memory addresses map to data storage
- **LO1.5**: Differentiate between volatile and non-volatile memory

### 2. Assembly Programming

- **LO2.1**: Write functional assembly programs using the BasCAT instruction set
- **LO2.2**: Use registers effectively for data manipulation
- **LO2.3**: Implement control structures (loops, conditionals) in assembly
- **LO2.4**: Manage stack operations for data storage and function calls
- **LO2.5**: Debug assembly programs using circuit visualization

### 3. High-Level Programming

- **LO3.1**: Write programs in SimpleBASCAT language
- **LO3.2**: Understand compilation process (source → assembly → machine code)
- **LO3.3**: Predict assembly output for given BASIC code
- **LO3.4**: Recognize performance implications of high-level constructs

### 4. Problem-Solving & Algorithms

- **LO4.1**: Decompose problems into computational steps
- **LO4.2**: Implement algorithms efficiently given hardware constraints
- **LO4.3**: Optimize code for size and speed tradeoffs
- **LO4.4**: Design data structures using available memory

### 5. Systems Thinking

- **LO5.1**: Explain abstraction layers in computer systems
- **LO5.2**: Understand tradeoffs between hardware and software solutions
- **LO5.3**: Connect BasCAT concepts to real-world computers
- **LO5.4**: Articulate why computer architecture matters for programmers

------

## Course Structure Overview

### Part 1: Assembly Programming (Weeks 1-6)

**Philosophy**: Learn how computers *really* work before adding abstraction layers

| Week | Topic            | Key Concepts                        | BasCAT Features Used         |
| ---- | ---------------- | ----------------------------------- | ---------------------------- |
| 1    | Data Movement    | Registers, memory, addressing modes | LOAD, MOV, LDM, STM          |
| 2    | Arithmetic & I/O | ALU operations, input/output        | ADD, SUB, IN, OUT            |
| 3    | Logic Operations | Bit manipulation, Boolean algebra   | AND, OR, XOR, NOT            |
| 4    | Control Flow     | Jumps, conditionals, loops          | CMP, JMP, JZ, JNZ, JC, JNC   |
| 5    | Stack & Memory   | LIFO structures, data organization  | PUSH, POP, memory management |
| 6    | Complex Programs | Combining all concepts              | Full instruction set         |

**Culminating Assessment**: Assembly-based game or application

### Part 2: BASIC Programming (Weeks 7-10)

**Philosophy**: Now that you know what's underneath, see how abstraction makes programming easier

| Week | Topic              | Key Concepts                | Focus                 |
| ---- | ------------------ | --------------------------- | --------------------- |
| 7    | BASIC Basics       | Variables, I/O, assignment  | LET, PRINT, INPUT     |
| 8    | Control Structures | Conditionals, loops         | IF...THEN, FOR...NEXT |
| 9    | Compilation        | How BASIC becomes assembly  | Dual-view execution   |
| 10   | Complex Programs   | Applying all BASIC features | Full language         |

**Culminating Assessment**: Same program in BASIC that was done in assembly (Week 6)

### Part 3: Computer Architecture Concepts (Weeks 11-15)

**Philosophy**: Connect BasCAT understanding to broader CS and real-world systems

| Week | Topic              | Key Concepts                 | Connection                     |
| ---- | ------------------ | ---------------------------- | ------------------------------ |
| 11   | CPU Deep Dive      | Pipeline, cache, modern CPUs | BasCAT vs modern architectures |
| 12   | Memory Hierarchy   | RAM, cache, virtual memory   | Extending BasCAT concepts      |
| 13   | I/O Systems        | Peripherals, interrupts, DMA | Beyond memory-mapped I/O       |
| 14   | Real Architectures | 6502, Z80, ARM, x86          | BasCAT in historical context   |
| 15   | Final Projects     | Student choice programs      | Demonstrate mastery            |

**Culminating Assessment**: Original program + architecture analysis presentation

------

## Three-Track Differentiation

### Track A: High School (Primary Track)

**Assumed Background**: None; basic computer use **Pace**: Standard (15 weeks) **Depth**: Core concepts with practical applications **Projects**: Games, tools, creative applications **Assessment**: 60% projects, 20% quizzes, 20% participation

**Modifications**:

- More guided examples
- Collaborative work encouraged
- Visual emphasis
- Real-world connections
- Career exploration

### Track B: College Freshman

**Assumed Background**: Some programming (any language) **Pace**: Accelerated (could compress to 12 weeks) **Depth**: Additional theory, architecture comparisons **Projects**: Performance optimization, compiler analysis **Assessment**: 50% projects, 30% exams, 20% participation

**Enhancements**:

- Additional readings on architecture history
- Comparative analysis (RISC vs CISC)
- Compiler design introduction
- Industry connections
- Research paper component (optional)

### Track C: Advanced Middle School

**Assumed Background**: Curiosity and strong reading skills **Pace**: Careful (full 15 weeks or longer) **Depth**: Focus on understanding over terminology **Projects**: Game-based, creative, tangible **Assessment**: 70% projects, 10% quizzes, 20% participation

**Modifications**:

- Simplified vocabulary (explain jargon)
- More scaffolding in projects
- Gamification elements
- Shorter programs
- Success emphasis over speed

------

## Assessment Philosophy

### Formative Assessment (Ongoing)

**Purpose**: Guide learning, not judge students

- **Daily Check-ins**: Quick concept reviews
- **Code Reviews**: Peer and teacher feedback
- **Circuit Tracing**: Visual understanding checks
- **Reflection Journals**: What confused you? What clicked?
- **Pair Programming**: Collaboration and communication

### Summative Assessment (Grading)

**Purpose**: Demonstrate mastery

- **Weekly Quizzes** (15%): Short, focused on concepts
- **Programming Projects** (50%): Major assessments
  - Week 3: Simple Calculator (10%)
  - Week 6: Assembly Application (15%)
  - Week 10: BASIC Application (15%)
  - Week 15: Final Project (10%)
- **Midterm Exam** (15%): Week 8, covers assembly programming
- **Final Exam** (20%): Week 15, comprehensive architecture

**Alternative Portfolio Assessment**:

- Collection of best programs
- Narrative explaining growth
- Circuit analysis diagrams
- Presentation of learning journey
- Self and peer evaluation

------

## Weekly Schedule Template

### Standard Week Structure (5 class periods)

**Day 1: Introduction & Demonstration** (50 minutes)

- Warm-up review (5 min)
- New concept introduction (15 min)
- Live demonstration with BasCAT (20 min)
- Q&A and discussion (10 min)

**Day 2: Guided Practice** (50 minutes)

- Review previous day (5 min)
- Guided coding session (30 min)
- Partner work on variations (15 min)

**Day 3: Independent Practice** (50 minutes)

- Mini-quiz on concepts (10 min)
- Individual programming time (35 min)
- Share solutions (5 min)

**Day 4: Application & Extension** (50 minutes)

- Challenge problems (25 min)
- Circuit analysis activity (20 min)
- Preview next concept (5 min)

**Day 5: Lab Day & Reflection** (50 minutes)

- Open lab for project work (40 min)
- Weekly reflection writing (10 min)

### Homework Expectations

- **Time**: 1-2 hours per week
- **Type**: Programming practice, reading, reflection
- **Support**: Office hours, online forum, peer help

------

## Required Materials

### For Students

- Computer with BasCAT installed (provided or BYOD)
- Notebook for circuit diagrams and notes
- Graph paper for memory maps
- Access to course materials (digital or printed)

### For Teachers

- Computer with BasCAT and projection capability
- This curriculum package
- Example student work (built over time)
- Assessment answer keys
- Grading rubrics

### Optional Enhancements

- Physical manipulatives (register cards, bus ropes)
- Posters of architecture diagrams
- Guest speakers from industry
- Field trip to computer museum or data center

------

## Prerequisite Skills

### Required

- Basic computer operation (keyboard, mouse, file management)
- Reading comprehension at grade level
- Willingness to think logically
- Comfort with frustration and debugging

### Helpful But Not Required

- Prior programming experience (any language)
- Comfort with mathematics
- Familiarity with binary numbers

### NOT Required

- Advanced math beyond basic arithmetic
- Computer science background
- Electronics knowledge

------

## Learning Environment Setup

### Physical Classroom

- Computers for each student or pair
- Projector/screen for demonstrations
- Whiteboard for circuit diagrams
- Flexible seating for collaboration

### Virtual/Hybrid Options

- BasCAT runs on Windows/Mac/Linux
- Screen sharing for demonstrations
- Breakout rooms for pair programming
- Online forum for asynchronous help

### Lab Time Requirements

- Minimum: 2 periods/week of computer access
- Ideal: 4-5 periods/week (daily access)
- Alternative: Longer lab sessions (2-hour blocks)

------

## Success Metrics

### For Students

- Can write working assembly programs independently
- Understand compilation from BASIC to assembly
- Can explain computer architecture concepts clearly
- Demonstrate growth mindset and debugging skills

### For Course

- 80%+ of students complete final project successfully
- Students report increased confidence in CS
- Students can explain "how computers work" to others
- Students express interest in further CS study

------

## Standards Alignment

### CSTA K-12 Computer Science Standards

- **3A-CS-01**: Explain how abstractions hide implementation details
- **3A-CS-02**: Compare levels of abstraction in computing
- **3A-AP-13**: Create prototypes using algorithms
- **3A-AP-17**: Decompose problems into sub-problems
- **3B-CS-01**: Categorize types of computing devices

### ISTE Standards for Students

- **Computational Thinker (5)**: Formulate problem definitions
- **Innovative Designer (4)**: Use design process
- **Knowledge Constructor (3)**: Evaluate information

*(Full alignment matrix in Phase 6)*

------

## Course Calendar

### Semester Format (15 weeks)

**Weeks 1-6**: Assembly Programming

- Build from data movement to complex programs
- Daily hands-on coding
- Weekly quizzes
- **Midpoint Project**: Week 3 Calculator

**Weeks 7-10**: BASIC Programming

- Rapid progression (already know assembly)
- Emphasis on compilation understanding
- **Major Project**: Week 6 Assembly Application

**Week 8**: Midterm Exam

**Weeks 11-14**: Architecture Concepts

- Broader context and connections
- Less coding, more analysis
- Readings and discussions
- **Major Project**: Week 10 BASIC Application

**Week 15**: Final Project & Exam

- Student presentations
- Comprehensive assessment
- **Final Project**: Original Program

### Summer Intensive Format (6 weeks)

**Week 1**: Assembly Basics (compress Weeks 1-2) **Week 2**: Advanced Assembly (compress Weeks 3-4) **Week 3**: Assembly Projects + BASIC Intro (Weeks 5-7) **Week 4**: BASIC Programming (Weeks 8-10) **Week 5**: Architecture Concepts (Weeks 11-13) **Week 6**: Real Architectures + Finals (Weeks 14-15)

**Adjustments**:

- Longer class periods (2-3 hours/day)
- More intensive homework
- Fewer but larger projects
- Compressed assessment schedule

------

## Grading Breakdown

### Standard Distribution

| Component                | Percentage | Purpose                        |
| ------------------------ | ---------- | ------------------------------ |
| Programming Projects (4) | 50%        | Demonstrate applied skills     |
| Weekly Quizzes (14)      | 15%        | Check conceptual understanding |
| Midterm Exam             | 15%        | Assess assembly mastery        |
| Final Exam               | 15%        | Comprehensive architecture     |
| Participation/Labs       | 5%         | Engagement and effort          |

### Alternative Grading Schemes

**Portfolio-Based** (for Track C - Middle School):

- Project Portfolio: 70%
- Self-Assessment: 10%
- Peer Reviews: 10%
- Teacher Observation: 10%

**Standards-Based Grading**:

- Rate each learning objective 1-4
- Must demonstrate proficiency (3+) on 80% of objectives
- Can revise and resubmit work

------

## Course Communication

### With Students

- Weekly announcements (what's coming)
- Office hours (debugging help)
- Online forum for questions
- Email for individual concerns

### With Parents/Guardians

- Course syllabus at start
- Mid-semester progress reports
- Communication about struggles early
- Showcase student work

### With Administration

- Alignment with standards
- Success metrics reporting
- Equipment and resource needs
- Student achievement data

------

## Potential Challenges & Solutions

### Challenge 1: Wide Skill Range

**Solution**:

- Differentiated tracks (3 levels)
- Extension activities for advanced
- Support materials for struggling
- Peer tutoring encouraged

### Challenge 2: Debugging Frustration

**Solution**:

- Normalize struggle as learning
- Pair programming for support
- Circuit visualization shows *what* is wrong
- Incremental programming approach

### Challenge 3: Abstract Concepts

**Solution**:

- BasCAT's visual approach
- Concrete examples first
- Physical manipulatives
- Multiple representations

### Challenge 4: Limited Computer Access

**Solution**:

- Partner programming
- Homework alternatives (written problems)
- Extended lab times
- Take-home BasCAT installation

------

## Extension Opportunities

### For Interested Students

- Independent study projects
- Competition participation (USACO, CyberPatriot)
- Arduino/Raspberry Pi connection
- Guest lecture opportunities
- Summer CS camps
- Internship preparation

### For Course Evolution

- Add more example programs
- Create additional projects
- Develop advanced topics modules
- Build student program library
- Create video tutorials
- Develop mobile app version

------

## Next Steps After This Course

### Recommended Follow-Ups

- AP Computer Science A (Java)
- Data Structures and Algorithms
- Web Development
- Embedded Systems / Robotics
- Cybersecurity
- Computer Engineering

### Skills Transferable To

- Any programming language
- Systems programming (C, C++, Rust)
- Operating systems concepts
- Compiler design
- Computer engineering
- Electrical engineering

------

*This framework establishes the foundation for all subsequent curriculum materials.*
