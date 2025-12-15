# BasCAT BASIC Language Guide

Complete guide to the BasCAT BASIC programming language.

---

## Introduction

BasCAT BASIC is a BASIC-like high-level language that compiles to BasCAT Assembly. It provides an easier way to write programs while teaching how high-level code translates to machine instructions.

**Key Features**:
- Line numbers (10, 20, 30, ...)
- 26 variables (A-Z)
- Arithmetic and logic operators
- Control flow (IF, GOTO, FOR)
- Input/output (INPUT, PRINT)

---

## Program Structure

Every BasCAT program consists of numbered lines:

```basic
10 REM This is a comment
20 LET A = 5
30 PRINT A
40 END
```

**Rules**:
- Lines must start with a number (10-9999)
- Lines are executed in numerical order
- Line numbers don't have to be consecutive
- Conventionally increment by 10 (allows inserting lines later)

---

## Statements

### REM - Comments

Add comments to explain your code.

**Syntax**: `REM comment text`

**Example**:
```basic
10 REM This is my first program
20 REM Calculate the sum of two numbers
```

**Note**: Comments are ignored by the compiler but appear in generated assembly.

---

### LET - Variable Assignment

Assign values to variables.

**Syntax**: `LET variable = expression`

**Variables**: A, B, C, D, ... Z (26 total)

**Examples**:
```basic
10 LET A = 5
20 LET B = 10
30 LET C = A + B        ; C = 15
40 LET D = C - A        ; D = 10
```

**Notes**:
- Variables hold values 0-255 (8-bit)
- Initial value is undefined
- Overflow wraps around (255 + 1 = 0)

---

### PRINT - Output

Display a variable's value.

**Syntax**: `PRINT variable`

**Example**:
```basic
10 LET A = 72
20 PRINT A              ; Outputs 72 (ASCII 'H')
```

**Notes**:
- Outputs to I/O panel
- Displays numeric value (0-255)
- One value per PRINT statement

---

### INPUT - Input

Read user input into a variable.

**Syntax**: `INPUT variable`

**Example**:
```basic
10 INPUT A
20 PRINT A              ; Echo input
```

**Notes**:
- Reads from I/O panel input field
- User must enter number and press Send
- Program waits (blocks) until input arrives

---

### IF...THEN GOTO - Conditional

Conditional jump based on comparison.

**Syntax**: `IF variable comparison value THEN GOTO line`

**Comparisons**:
- `=` - Equal
- `<>` - Not equal
- `<` - Less than
- `>` - Greater than
- `<=` - Less than or equal
- `>=` - Greater than or equal

**Examples**:
```basic
10 INPUT A
20 IF A = 10 THEN GOTO 50
30 PRINT 0
40 GOTO 60
50 PRINT 1
60 END
```

```basic
10 INPUT A
20 IF A > 100 THEN GOTO 50
30 IF A < 10 THEN GOTO 70
40 PRINT 50             ; Between 10 and 100
45 GOTO 80
50 PRINT 99             ; Greater than 100
60 GOTO 80
70 PRINT 1              ; Less than 10
80 END
```

---

### GOTO - Unconditional Jump

Jump to a specific line.

**Syntax**: `GOTO line_number`

**Example**:
```basic
10 LET A = 0
20 PRINT A
30 LET A = A + 1
40 IF A < 5 THEN GOTO 20    ; Loop back
50 END
```

**Uses**:
- Create loops
- Skip sections of code
- Implement flow control

**Warning**: Excessive GOTOs can make code hard to follow!

---

### FOR...NEXT - Loop

Count from start to end value.

**Syntax**:
```basic
FOR variable = start TO end
  ...statements...
NEXT variable
```

**Example**:
```basic
10 FOR I = 0 TO 5
20   PRINT I
30 NEXT I
40 END
```

**Output**: 0, 1, 2, 3, 4, 5

**Rules**:
- Loop variable must be a letter (A-Z)
- Start is evaluated once before loop
- End must be a literal number (current limitation)
- Increment is always 1
- Loop executes end-start+1 times

**Example - Nested Loops**:
```basic
10 FOR I = 0 TO 2
20   FOR J = 0 TO 2
30     PRINT J
40   NEXT J
50 NEXT I
60 END
```

**Current Limitation**: End value must be a literal number, not a variable.

---

### END - Program Termination

Stop program execution.

**Syntax**: `END`

**Example**:
```basic
10 LET A = 10
20 PRINT A
30 END
```

**Notes**:
- Every program should end with END
- Generates HALT instruction
- CPU stops executing

---

### POKE - Direct Memory Write

Write a value directly to a memory address.

**Syntax**: `POKE address, value`

**Example**:
```basic
10 POKE 154, 42         ; Store 42 at memory address 154
20 POKE 155, 100        ; Store 100 at memory address 155
30 END
```

**Notes**:
- Address must be 0-255 (use 154-237 for data storage)
- Value must be 0-255
- Generates `STM` assembly instruction
- Useful for storing data arrays or lookup tables

**Memory Map for POKE**:
- **Safe data area**: 154-237 (0x9A-0xED) - 83 bytes free for your data
- Avoid 0-127 (program code), 128-153 (variables A-Z), 254-255 (I/O)

---

### PEEK - Direct Memory Read

Read a value directly from a memory address.

**Syntax**: `PEEK(address)` (used in expressions)

**Example**:
```basic
10 POKE 154, 42         ; Store 42 at address 154
20 LET A = PEEK(154)    ; Read value from address 154 into A
30 PRINT A              ; Outputs 42
40 END
```

**Notes**:
- PEEK is an expression, not a statement
- Use with LET: `LET A = PEEK(address)`
- Generates `LDM` assembly instruction
- Returns 8-bit value (0-255)

**Example - Simple Array**:
```basic
10 REM Store 3 values
20 POKE 154, 10
30 POKE 155, 20
40 POKE 156, 30
50 REM Read them back
60 LET A = PEEK(154)
70 LET B = PEEK(155)
80 LET C = PEEK(156)
90 PRINT A
100 PRINT B
110 PRINT C
120 END
```

---

## Expressions

### Arithmetic Operators

BasCAT BASIC supports basic arithmetic:

| Operator | Operation | Example | Result |
|----------|-----------|---------|--------|
| `+` | Addition | `A + 5` | Sum |
| `-` | Subtraction | `A - 3` | Difference |

**Examples**:
```basic
10 LET A = 10
20 LET B = A + 5        ; B = 15
30 LET C = B - 3        ; C = 12
40 LET D = C + A        ; D = 22
```

**Current Limitations**:
- No multiplication or division (v1.0)
- No parentheses for precedence
- Operations evaluated left-to-right
- Complex expressions may generate verbose assembly

---

### Logical Operators

Use in expressions (not in IF statements):

| Operator | Operation | Example |
|----------|-----------|---------|
| `AND` | Bitwise AND | `A AND 15` |
| `OR` | Bitwise OR | `A OR 128` |
| `XOR` | Bitwise XOR | `A XOR 255` |
| `NOT` | Bitwise NOT | `NOT A` |

**Examples**:
```basic
10 LET A = 0b11110000
20 LET B = A AND 0b00001111    ; B = 0
30 LET C = A OR 15             ; C = 255
40 LET D = NOT A               ; D = 0b00001111
```

---

## Variables

BasCAT BASIC provides 26 variables named A through Z.

**Memory Layout**:
- Variable A → Memory address 10
- Variable B → Memory address 11
- Variable C → Memory address 12
- ...
- Variable Z → Memory address 35

**Properties**:
- 8-bit (0-255)
- No type (all numbers)
- No arrays (v1.0)
- No strings (v1.0)

---

## Complete Examples

### Example 1: Hello World

```basic
10 REM Hello World
20 PRINT 72             ; ASCII 'H'
30 END
```

---

### Example 2: Addition

```basic
10 REM Add two numbers
20 LET A = 5
30 LET B = 3
40 LET C = A + B
50 PRINT C              ; Outputs 8
60 END
```

---

### Example 3: Echo Input

```basic
10 REM Echo user input
20 INPUT A
30 PRINT A
40 GOTO 20              ; Loop forever
```

---

### Example 4: Counter

```basic
10 REM Count from 0 to 10
20 FOR I = 0 TO 10
30   PRINT I
40 NEXT I
50 END
```

---

### Example 5: Maximum of Two Numbers

```basic
10 REM Find maximum
20 INPUT A
30 INPUT B
40 IF A > B THEN GOTO 70
50 PRINT B              ; B is larger
60 GOTO 80
70 PRINT A              ; A is larger
80 END
```

---

### Example 6: Accumulator

```basic
10 REM Sum until > 100
20 LET A = 0
30 INPUT B
40 LET A = A + B
50 PRINT A
60 IF A < 100 THEN GOTO 30
70 END
```

---

### Example 7: Countdown

```basic
10 REM Countdown from 10
20 LET A = 10
30 PRINT A
40 LET A = A - 1
50 IF A > 0 THEN GOTO 30
60 PRINT 0
70 END
```

---

## Compilation Process

When you compile BasCAT BASIC to assembly:

1. **Lexer** breaks code into tokens
2. **Parser** builds Abstract Syntax Tree (AST)
3. **Code Generator** emits assembly instructions
4. **Assembler** converts to bytecode

**Example Transformation**:

**BasCAT BASIC**:
```basic
10 LET A = 5
20 PRINT A
30 END
```

**Generated Assembly**:
```assembly
L10:
  ; BASIC line 10
  LOAD A, 5
  STM 0x80, A
L20:
  ; BASIC line 20
  LDM A, 0x80
  OUT A
L30:
  ; BASIC line 30
  HALT
```

---

## Tips and Best Practices

### 1. Use Meaningful Variable Names

Since variables are single letters, document their purpose:

```basic
10 REM A = counter
20 REM B = total
30 REM C = input value
40 FOR A = 0 TO 10
50   INPUT C
60   LET B = B + C
70 NEXT A
```

### 2. Increment Line Numbers by 10

Leaves room to insert lines later:

```basic
10 LET A = 0
20 PRINT A
30 END

; Later, you want to add something between 10 and 20:
10 LET A = 0
15 LET B = 5        ; Inserted
20 PRINT A
30 END
```

### 3. Use Comments

Explain your logic:

```basic
10 REM This program finds the maximum of two numbers
20 REM A = first number
30 REM B = second number
40 INPUT A
50 INPUT B
60 IF A > B THEN GOTO 90
70 PRINT B
80 GOTO 100
90 PRINT A
100 END
```

### 4. Test with Simple Inputs

Start with small, known values:

```basic
10 REM Test with A=5, expect output 5
20 INPUT A
30 PRINT A
40 END
```

### 5. Use Step-Over for Debugging

When running in BasCAT:
- Use "Step Over" to execute one BASIC line at a time
- Watch both BASIC and Assembly views
- See how your code translates to machine instructions

---

## Current Limitations (v1.0)

The following features are NOT supported in version 1.0:

**Not Supported**:
- ❌ Multiplication and division
- ❌ Parentheses in expressions
- ❌ String variables
- ❌ Arrays
- ❌ Subroutines (GOSUB/RETURN)
- ❌ FOR loops with variable end values
- ❌ Functions (SIN, COS, etc.)
- ❌ DATA/READ statements

**Workarounds**:
- **Multiplication**: Use repeated addition in a loop
- **Division**: Use repeated subtraction
- **Strings**: Use ASCII codes (72 = 'H')
- **FOR with variable end**: Use a literal upper bound and exit early with IF

**Example - FOR with variable end**:
```basic
10 REM Count from 0 to N (where N is in variable C)
20 INPUT C              ; Get the desired end value
30 FOR I = 0 TO 100     ; Use safe upper bound
40   IF I >= C THEN GOTO 70
50   PRINT I
60 NEXT I
70 END
```

This approach:
- Uses a literal value (100) as the FOR end
- Checks each iteration if we've reached the desired limit
- Exits the loop early using GOTO
- Works for any value of N up to 100

---

## Error Messages

Common compilation errors:

### "Undefined label"
You referenced a line number that doesn't exist.
```basic
10 GOTO 50    ; Error: Line 50 doesn't exist
20 END
```

### "FOR loops currently only support literal end values"
You used a variable as the end value in FOR:
```basic
10 INPUT A
20 FOR I = 0 TO A    ; Error: A is not a literal
```
**Fix**: Use a literal number: `FOR I = 0 TO 10`

### "Invalid syntax"
General syntax error. Check:
- Line numbers present
- Keywords spelled correctly
- Expressions valid

### "Variable names must be single letters A-Z"

You tried to use a multi-letter variable name.

**Error Example**:
```basic
10 LET COUNT = 5        ; Error: COUNT is not a valid variable
20 LET Total = 10       ; Error: Total is not a valid variable
30 LET X1 = 15          ; Error: X1 is not a valid variable
```

**Fix**: Use single letters and document their meaning:
```basic
10 REM C = count, T = total, X = result
20 LET C = 5            ; Correct
30 LET T = 10           ; Correct
40 LET X = 15           ; Correct
```

**Why Single Letters?**
- Simplifies the compiler
- Mirrors early computer limitations
- Teaches resource constraints
- Encourages planning and documentation

**Best Practice**: Always use REM comments to document what each variable represents.

---

## Getting Help

**In BasCAT**:
- Menu → Help → BASIC Language Guide (this document)
- Menu → Help → Instruction Reference (assembly reference)
- Menu → Examples → Load sample programs

**Learning Path**:
1. Start with "Hello World"
2. Try arithmetic examples
3. Experiment with loops
4. Learn conditionals
5. Combine concepts in complex programs

---

## Advanced Topics

### Understanding Compilation

Watch how BASIC compiles to assembly:

1. Write BASIC code (left pane)
2. Click "Compile"
3. See assembly (right pane)
4. Run with "Step Over" to see execution

**Example**:
```basic
10 LET A = A + 1
```

**Compiles to**:
```assembly
LDM A, 0x80   ; Load variable A from memory
ADD A, 1      ; Add 1
STM 0x80, A   ; Store back to memory
```

### Memory Layout

Understanding where variables live:

```
┌──────────────┬────────────┬──────────────────┐
│ Address      │ Purpose    │ BASIC Name       │
├──────────────┼────────────┼──────────────────┤
│ 0x00-0x7F    │ Program    │ Code Area (128B) │
│ 0x80         │ Variable   │ A                │
│ 0x81         │ Variable   │ B                │
│ 0x82         │ Variable   │ C                │
│ 0x83         │ Variable   │ D                │
│ 0x84         │ Variable   │ E                │
│ ...          │ ...        │ ...              │
│ 0x97         │ Variable   │ X                │
│ 0x98         │ Variable   │ Y                │
│ 0x99         │ Variable   │ Z                │
│ 0x9A-0xED    │ Available  │ Free RAM (~83B)  │
│ 0xEE-0xFD    │ Stack      │ Stack (16B)      │
│ 0xFE         │ I/O Port   │ Output           │
│ 0xFF         │ I/O Port   │ Input            │
└──────────────┴────────────┴──────────────────┘
```

**Key Points**:
- Program area: 0x00-0x7F (128 bytes max for compiled code)
- Variables A-Z occupy addresses 0x80-0x99 (26 consecutive locations)
- Formula: Variable address = 0x80 + (letter position in alphabet - 1)
  - A = 0x80 + (1-1) = 0x80
  - B = 0x80 + (2-1) = 0x81
  - Z = 0x80 + (26-1) = 0x99
- Stack: 0xEE-0xFD (16 bytes, grows downward from 0xFD)
- I/O ports are at the top of memory (0xFE-0xFF)

**Why This Matters**:
When you see assembly code like `STM 0x80, A`, you now know exactly where variable A lives in the computer's memory.

### Optimization Philosophy

BasCAT BASIC intentionally generates **unoptimized** assembly code. This is not a bug - it's a deliberate design choice for educational purposes.

**What BasCAT BASIC Does**:
```basic
10 LET A = A + 1
```

**Generated Assembly** (unoptimized):
```assembly
LDM A, 0x80   ; Load variable A from memory
ADD A, 1      ; Add 1 to A (result stored in A - destructive operation)
STM 0x80, A   ; Store back to memory
```
**3 instructions** - Every step is visible and traceable.

**Important**: The `ADD A, B` instruction is a *destructive operation*. It adds the value in register B (or an immediate value) to register A and stores the result back in register A. The original value in A is lost. This is why we must reload A from memory each time.

**What an Optimizing Compiler Might Do**:
```assembly
INC [0x80]    ; Increment memory location 0x80 directly
```
**1 instruction** - Faster, but hides what's happening.

**Why Unoptimized is Better for Learning**:
- Each BASIC operation maps to clear, separate assembly instructions
- The compilation process is transparent and predictable
- Students can trace every step of execution
- The "cost" of high-level operations becomes visible

**The Trade-off**:
- Real compilers optimize aggressively for speed and size
- BasCAT optimizes for **understanding**

When you're ready to learn about optimization, you can:
1. Write BasCAT BASIC code
2. Study the generated assembly
3. Hand-optimize the assembly yourself
4. Compare the results

This teaches both *what computers do* and *how to make them do it efficiently*.

---

### Reading Assembly Code

Understanding the assembly output is key to learning how computers work. Here's a detailed walkthrough:

**BasCAT BASIC Program**:
```basic
10 REM Add two numbers
20 LET A = 0
30 INPUT B
40 LET A = A + B
50 PRINT A
60 IF A < 100 THEN GOTO 30
70 END
```

**Generated Assembly** (with detailed explanation):

```assembly
L10:
    ; BASIC line 10
    ; REM: Add two numbers
    ; (Comments generate no code)

L20:
    ; BASIC line 20: LET A = 0
    LOAD A, 0            ; Load literal value 0 into register A
    STM 0x80, A          ; Store register A into memory address 0x80 (variable A)
    ; After: Memory[0x80] = 0, Register A = 0

L30:
    ; BASIC line 30: INPUT B
    IN A                 ; Read input from I/O port into register A
    STM 0x81, A          ; Store register A into memory address 0x81 (variable B)
    ; After: Memory[0x81] = (user input), Register A = (user input)

L40:
    ; BASIC line 40: LET A = A + B
    LDM A, 0x80          ; Load memory address 0x80 into register A (get A's value)
    LDM B, 0x81          ; Load memory address 0x81 into register B (get B's value)
    ADD A, B             ; Add B to A, result goes into A (A = A + B)
    STM 0x80, A          ; Store register A back into memory address 0x80
    ; After: Memory[0x80] = old_A + B, Register A = old_A + B, Register B = B

L50:
    ; BASIC line 50: PRINT A
    LDM A, 0x80          ; Load memory address 0x80 into register A (get A's value)
    OUT A                ; Output register A to I/O port
    ; After: Display shows value of A

L60:
    ; BASIC line 60: IF A < 100 THEN GOTO 30
    LDM A, 0x80          ; Load memory address 0x80 into register A (get A's value)
    CMP A, 0x64          ; Compare A with 0x64 (100), set condition flags
    JC L30               ; Jump to L30 if comparison is true (A < 100)
    ; If A < 100: execution jumps to L30
    ; If A >= 100: execution continues to next line

L70:
    ; BASIC line 70: END
    HALT                 ; Stop program execution
```

**Key Observations**:

1. **Every variable access requires memory operations**
   - Variables live in memory (addresses 10, 11, etc.)
   - Computation happens in registers (A, B)
   - Pattern: Load → Compute → Store

2. **Labels mark BASIC line numbers**
   - L10, L20, L30 correspond to lines 10, 20, 30
   - Used as jump targets (GOTO, IF...THEN)

3. **One BASIC line can become multiple assembly instructions**
   - Line 40 (`LET A = A + B`) becomes 4 instructions
   - This reveals the "hidden cost" of simple operations

4. **Registers are temporary**
   - Register values are lost unless stored to memory
   - This is why we reload A from memory at lines L50 and L60

**Learning Exercise**: 
Try modifying the BASIC program and predicting what assembly code will be generated before compiling. This builds intuition for how high-level code translates to machine operations.

---

*BasCAT BASIC Language Reference - Version 1.0*

*Part of the BasCAT Educational Computer Simulator*
