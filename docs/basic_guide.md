# SimpleBASCAT Language Guide

Complete guide to the SimpleBASCAT programming language.

---

## Introduction

SimpleBASCAT is a BASIC-like high-level language that compiles to BasCAT assembly. It provides an easier way to write programs while teaching how high-level code translates to machine instructions.

**Key Features**:
- Line numbers (10, 20, 30, ...)
- 26 variables (A-Z)
- Arithmetic and logic operators
- Control flow (IF, GOTO, FOR)
- Input/output (INPUT, PRINT)

---

## Program Structure

Every SimpleBASCAT program consists of numbered lines:

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

## Expressions

### Arithmetic Operators

SimpleBASCAT supports basic arithmetic:

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

SimpleBASCAT provides 26 variables named A through Z.

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

When you compile SimpleBASCAT to assembly:

1. **Lexer** breaks code into tokens
2. **Parser** builds Abstract Syntax Tree (AST)
3. **Code Generator** emits assembly instructions
4. **Assembler** converts to bytecode

**Example Transformation**:

**SimpleBASCAT**:
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
  STM 10, A
L20:
  ; BASIC line 20
  LDM A, 10
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
LDM A, 10     ; Load variable A from memory
ADD A, 1      ; Add 1
STM 10, A     ; Store back to memory
```

### Memory Layout

Understanding where variables live:

| Variable | Address | Usage |
|----------|---------|-------|
| A | 10 | General purpose |
| B | 11 | General purpose |
| ... | ... | ... |
| Z | 35 | General purpose |

**I/O Ports**:
- 254 (0xFE): Output
- 255 (0xFF): Input

### Optimization

SimpleBASCAT generates simple but potentially verbose code:

**Less Efficient**:
```basic
LET A = A + 1
```

**Generates**:
```assembly
LDM A, 10
ADD A, 1
STM 10, A     ; 3 instructions
```

**More Efficient** (in pure assembly):
```assembly
LDM A, 10
ADD A, 1
STM 10, A     ; Same, but you could optimize manually
```

For learning, the verbose code is actually good - it shows all steps clearly!

---

*SimpleBASCAT Language Reference - Version 1.0*

*Part of the BasCAT Educational Computer Simulator*
