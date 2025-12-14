# SimpleBASCAT Language Specification

**Version**: 1.0
**Date**: December 14, 2025

---

## Overview

SimpleBASCAT is a BASIC-like high-level language designed for the BasCAT educational computer. It compiles to BasCAT assembly language, allowing students to see how high-level constructs map to low-level instructions.

---

## Language Features

### 1. Line Numbers

Every statement must start with a line number (1-9999).

```basic
10 REM This is line 10
20 LET A = 5
30 PRINT A
```

**Purpose**:
- Identifies statement order
- Provides jump targets for GOTO
- Traditional BASIC style

### 2. Variables

**Single-letter variables**: A-Z (26 variables maximum)

```basic
10 LET A = 10
20 LET B = 20
30 LET C = A + B
```

**Memory Mapping**:
- Variables stored in memory addresses 10-35
- A→10, B→11, C→12, ..., Z→35

### 3. Data Types

**Integers only**: 0-255 (8-bit unsigned)

```basic
10 LET X = 100
20 LET Y = 255
```

### 4. Arithmetic Operators

| Operator | Operation | Example |
|----------|-----------|---------|
| `+` | Addition | `A + B` |
| `-` | Subtraction | `A - B` |
| `*` | Multiplication | `A * 2` (limited) |
| `/` | Division | `A / 2` (limited) |

**Note**: Multiplication and division are simplified (powers of 2 only in v1.0)

### 5. Comparison Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal to | `A = 5` |
| `<>` | Not equal to | `A <> 0` |
| `<` | Less than | `A < 10` |
| `>` | Greater than | `A > 0` |
| `<=` | Less than or equal | `A <= 10` |
| `>=` | Greater than or equal | `A >= 5` |

### 6. Logical Operators

| Operator | Operation | Example |
|----------|-----------|---------|
| `AND` | Bitwise AND | `A AND B` |
| `OR` | Bitwise OR | `A OR B` |
| `XOR` | Bitwise XOR | `A XOR B` |
| `NOT` | Bitwise NOT | `NOT A` |

---

## Statements

### LET - Assignment

```basic
10 LET A = 10
20 LET B = A + 5
30 LET C = A * 2
```

**Syntax**: `LET variable = expression`

**Compilation**:
```assembly
; 10 LET A = 10
LOAD A, 10
STM 10, A

; 20 LET B = A + 5
LDM A, 10
ADD A, 5
STM 11, A
```

### PRINT - Output

```basic
10 PRINT A
20 PRINT 42
```

**Syntax**: `PRINT variable|value`

**Compilation**:
```assembly
; 10 PRINT A
LDM A, 10
OUT A

; 20 PRINT 42
LOAD A, 42
OUT A
```

### INPUT - Read Input

```basic
10 INPUT A
20 INPUT X
```

**Syntax**: `INPUT variable`

**Compilation**:
```assembly
; 10 INPUT A
IN A
STM 10, A
```

### IF...THEN

```basic
10 IF A = 5 THEN GOTO 100
20 IF B > 10 THEN GOTO 200
30 IF C <> 0 THEN GOTO 50
```

**Syntax**: `IF expression comparison expression THEN GOTO line`

**Compilation**:
```assembly
; 10 IF A = 5 THEN GOTO 100
LDM A, 10
CMP A, 5
JZ 100

; 20 IF B > 10 THEN GOTO 200
LDM A, 11
CMP A, 10
; (B-10 > 0, check carry/negative flags)
JC 200
```

### GOTO - Unconditional Jump

```basic
10 GOTO 100
```

**Syntax**: `GOTO line_number`

**Compilation**:
```assembly
; 10 GOTO 100
JMP 100
```

### FOR...NEXT - Counted Loop

```basic
10 FOR I = 0 TO 9
20   PRINT I
30 NEXT I
```

**Syntax**:
```
FOR variable = start TO end
  statements
NEXT variable
```

**Compilation**:
```assembly
; 10 FOR I = 0 TO 9
LOAD A, 0
STM 18, A        ; I stored at address 18

; 20   PRINT I
loop_start:
LDM A, 18
OUT A

; 30 NEXT I
LDM A, 18
ADD A, 1
STM 18, A
CMP A, 10        ; end+1
JNZ loop_start
```

### REM - Comment

```basic
10 REM This is a comment
20 REM Comments are ignored by compiler
```

**Syntax**: `REM any text`

**Compilation**: (ignored, no code generated)

### END - Program End

```basic
100 END
```

**Syntax**: `END`

**Compilation**:
```assembly
HALT
```

---

## Complete Example Programs

### Example 1: Hello World (Numbers)

```basic
10 REM Output 72 73 (H I in ASCII)
20 PRINT 72
30 PRINT 73
40 END
```

### Example 2: Simple Loop

```basic
10 REM Count from 0 to 9
20 FOR I = 0 TO 9
30   PRINT I
40 NEXT I
50 END
```

### Example 3: Input and Conditional

```basic
10 REM Read number and check if > 50
20 INPUT A
30 IF A > 50 THEN GOTO 60
40 PRINT 0
50 GOTO 70
60 PRINT 1
70 END
```

### Example 4: Accumulator

```basic
10 REM Sum numbers until 0 entered
20 LET S = 0
30 INPUT A
40 IF A = 0 THEN GOTO 80
50 LET S = S + A
60 GOTO 30
70 REM Never reached
80 PRINT S
90 END
```

### Example 5: Logic Operations

```basic
10 REM Demonstrate AND operation
20 LET A = 15
30 LET B = 7
40 LET C = A AND B
50 PRINT C
60 END
```

---

## Compilation Strategy

### Variable Allocation

| Variable | Memory Address |
|----------|---------------|
| A | 10 |
| B | 11 |
| C | 12 |
| ... | ... |
| Z | 35 |

**Temporary Variables**: 36-49 (for expression evaluation)

### Expression Evaluation

Expressions are evaluated left-to-right (no operator precedence in v1.0).

```basic
10 LET A = 5 + 3 + 2
```

Compiles to:
```assembly
LOAD A, 5
ADD A, 3
ADD A, 2
STM 10, A
```

### Label Generation

Compiler generates labels for:
- FOR loop starts
- GOTO targets
- IF THEN targets

Format: `L{line_number}` for user line numbers, `_loop_{N}` for generated loops

### Line Mapping

Compiler maintains mapping:
```
BASIC Line → Assembly Line Range
10 → [0-3]
20 → [4-7]
30 → [8-10]
```

---

## Limitations (v1.0)

1. **No Subroutines**: GOSUB/RETURN not implemented yet
2. **No Arrays**: Single variables only
3. **No Strings**: Numbers/characters only
4. **Simple Math**: No operator precedence, left-to-right evaluation
5. **No Multiplication/Division**: Will add in v1.1
6. **No STEP**: FOR loops increment by 1 only
7. **No Functions**: ABS(), RND(), etc. not implemented

---

## Grammar (EBNF)

```ebnf
program       = { statement } ;
statement     = line_number command ;
line_number   = digit { digit } ;

command       = "LET" assignment
              | "PRINT" expression
              | "INPUT" variable
              | "IF" condition "THEN" "GOTO" line_number
              | "GOTO" line_number
              | "FOR" variable "=" expression "TO" expression
              | "NEXT" variable
              | "REM" text
              | "END" ;

assignment    = variable "=" expression ;
condition     = expression comparison expression ;
comparison    = "=" | "<>" | "<" | ">" | "<=" | ">=" ;

expression    = term { ("+" | "-" | "AND" | "OR" | "XOR") term } ;
term          = "NOT" factor | factor ;
factor        = number | variable | "(" expression ")" ;

variable      = "A" | "B" | ... | "Z" ;
number        = digit { digit } ;
digit         = "0" | "1" | ... | "9" ;
text          = { any character } ;
```

---

## Token Types

```python
class TokenType(Enum):
    # Literals
    NUMBER = "NUMBER"
    VARIABLE = "VARIABLE"

    # Keywords
    LET = "LET"
    PRINT = "PRINT"
    INPUT = "INPUT"
    IF = "IF"
    THEN = "THEN"
    GOTO = "GOTO"
    FOR = "FOR"
    TO = "TO"
    NEXT = "NEXT"
    REM = "REM"
    END = "END"

    # Operators
    PLUS = "+"
    MINUS = "-"
    AND = "AND"
    OR = "OR"
    XOR = "XOR"
    NOT = "NOT"

    # Comparisons
    EQ = "="
    NEQ = "<>"
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="

    # Structure
    LPAREN = "("
    RPAREN = ")"
    NEWLINE = "NEWLINE"
    EOF = "EOF"
```

---

## Error Handling

### Compile-time Errors

- Syntax errors (invalid statements)
- Undefined variables
- Invalid line numbers
- Mismatched FOR/NEXT
- Invalid expressions

### Runtime Errors

- Division by zero
- Stack overflow
- Out of memory
- I/O errors

---

## Future Enhancements (v2.0)

- GOSUB/RETURN for subroutines
- Arrays: DIM A(10)
- String support
- Full arithmetic with precedence
- Functions: ABS(), RND(), etc.
- ON...GOTO
- DATA/READ/RESTORE
- Better error messages

---

## Compiler Architecture

```
Source Code (BASIC)
    ↓
[Lexer] → Tokens
    ↓
[Parser] → AST
    ↓
[Code Generator] → Assembly
    ↓
[Assembler] → Bytecode
```

**Components**:
1. **Lexer**: Converts source text to tokens
2. **Parser**: Builds Abstract Syntax Tree (AST)
3. **Code Generator**: Emits assembly from AST
4. **Symbol Table**: Tracks variables and labels
5. **Line Mapper**: Maps BASIC lines to assembly lines

---

This specification provides the foundation for implementing the SimpleBASCAT compiler in Phase 4!
