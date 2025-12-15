# BasCAT Assembly Instruction Reference

Complete reference for all 23 assembly instructions supported by BasCAT.

---

## Data Movement Instructions

### LOAD reg, value
**Opcode**: 0x01

Loads an immediate value into a register.

**Format**: `LOAD A, 42`

**Example**:
```assembly
LOAD A, 10    ; Load 10 into register A
LOAD B, 255   ; Load 255 into register B
```

**Flags**: None affected

---

### MOV dest, src
**Opcode**: 0x10

Moves data between registers or from immediate value to register.

**Formats**:
- `MOV A, B` - Copy register B to register A
- `MOV A, 5` - Load immediate value 5 into register A

**Example**:
```assembly
LOAD A, 10
MOV B, A      ; Copy A to B (B now contains 10)
MOV C, 20     ; Load 20 into C
```

**Flags**: None affected

---

### LDM reg, [address]
**Opcode**: 0x0F

Load from memory address into register.

**Format**: `LDM A, [50]` or `LDM A, 50`

**Example**:
```assembly
LDM A, 0x80   ; Load value from memory address 0x80 into A (variable A)
LDM B, 0xFE   ; Load from I/O port (address 0xFE)
```

**Flags**: None affected

---

### STM [address], reg
**Opcode**: 0x11

Store register value to memory address.

**Format**: `STM [50], A` or `STM 50, A`

**Example**:
```assembly
LOAD A, 42
STM 0x64, A   ; Store value 42 to memory address 0x64 (100 decimal)
STM 0xFE, A   ; Write to output port
```

**Flags**: None affected

---

## Arithmetic Instructions

### ADD reg, value/reg
**Opcode**: 0x02

Adds a value or register to a register.

**Formats**:
- `ADD A, 5` - Add immediate value to register
- `ADD A, B` - Add register B to register A

**Example**:
```assembly
LOAD A, 10
ADD A, 5      ; A = 15 (immediate mode)

LOAD A, 5
LOAD B, 3
ADD A, B      ; A = 8 (register mode)
```

**Flags**: Z (if result is 0), C (if overflow), O (if overflow), N (if negative)

**Note**: Immediate values are limited to 0-127 when using the standard instruction encoding.

---

### SUB reg, value
**Opcode**: 0x03

Subtracts a value from a register.

**Format**: `SUB A, 3`

**Example**:
```assembly
LOAD A, 10
SUB A, 3      ; A = 7
```

**Flags**: Z, C, O, N

---

### CMP reg, value
**Opcode**: 0x0D

Compares register with value (performs subtraction but doesn't store result).

**Format**: `CMP A, 10`

**Example**:
```assembly
LOAD A, 15
CMP A, 10     ; Sets flags based on A - 10
JZ equal      ; Jump if A == 10
```

**Flags**: Z (if equal), C (if reg < value), N

**Used with**: JZ, JNZ, JC, JNC

---

## Logical Instructions

### AND reg, value
**Opcode**: 0x09

Bitwise AND operation.

**Format**: `AND A, 15`

**Example**:
```assembly
LOAD A, 0b11110000
AND A, 0b00001111  ; A = 0b00000000 (result: 0)
```

**Flags**: Z, N

---

### OR reg, value
**Opcode**: 0x0A

Bitwise OR operation.

**Format**: `OR A, 8`

**Example**:
```assembly
LOAD A, 0b00001111
OR A, 0b11110000   ; A = 0b11111111 (result: 255)
```

**Flags**: Z, N

---

### XOR reg, value
**Opcode**: 0x0B

Bitwise XOR (exclusive OR) operation.

**Format**: `XOR A, 255`

**Example**:
```assembly
LOAD A, 0b10101010
XOR A, 0b11111111  ; A = 0b01010101 (flips all bits)
```

**Flags**: Z, N

---

### NOT reg
**Opcode**: 0x0C

Bitwise NOT operation (inverts all bits).

**Format**: `NOT A`

**Example**:
```assembly
LOAD A, 0b00001111
NOT A             ; A = 0b11110000
```

**Flags**: Z, N

---

## Control Flow Instructions

### JMP address
**Opcode**: 0x04

Unconditional jump to address.

**Format**: `JMP 100` or `JMP loop_start`

**Example**:
```assembly
JMP start
; ... code ...
start:
  LOAD A, 10
```

**Flags**: None affected

---

### JZ address
**Opcode**: 0x0E

Jump if Zero flag is set (result was zero).

**Format**: `JZ target`

**Example**:
```assembly
LOAD A, 10
CMP A, 10
JZ equal      ; Jumps because 10 == 10
equal:
  LOAD B, 1
```

**Flags**: None affected
**Condition**: Z flag = 1

---

### JNZ address
**Opcode**: 0x12

Jump if Zero flag is clear (result was not zero).

**Format**: `JNZ target`

**Example**:
```assembly
loop:
  SUB A, 1
  JNZ loop    ; Keep looping while A != 0
```

**Flags**: None affected
**Condition**: Z flag = 0

---

### JC address
**Opcode**: 0x13

Jump if Carry flag is set.

**Format**: `JC overflow`

**Example**:
```assembly
LOAD A, 255
ADD A, 1
JC overflow   ; Jumps because 255+1 overflows
```

**Flags**: None affected
**Condition**: C flag = 1

---

### JNC address
**Opcode**: 0x14

Jump if Carry flag is clear.

**Format**: `JNC no_overflow`

**Example**:
```assembly
LOAD A, 10
ADD A, 5
JNC no_overflow  ; Jumps because no overflow
```

**Flags**: None affected
**Condition**: C flag = 0

---

## Understanding the Stack

The **stack** is a Last-In-First-Out (LIFO) data structure essential for temporary storage, register preservation, and subroutine organization.

### Stack Memory Layout

```
Memory Address    Contents         Notes
─────────────────────────────────────────────────
   0xFD          [first push]  ← SP starts here (top of stack)
   0xFC          [second push]
   0xFB          [third push]  ← SP moves DOWN as you push
   ...
   0xEE          [max depth]      Stack limit (16 bytes total)
─────────────────────────────────────────────────
```

### How PUSH Works

When you execute `PUSH A`:
1. The value in register A is stored at the current SP address
2. SP is **decremented** (moves down in memory)

```
Before PUSH A (A=42, SP=0xFD):     After PUSH A (A=42, SP=0xFC):
┌─────────┐                        ┌─────────┐
│ 0xFD: ? │ ← SP                   │ 0xFD: 42│   (value stored)
├─────────┤                        ├─────────┤
│ 0xFC: ? │                        │ 0xFC: ? │ ← SP (decremented)
└─────────┘                        └─────────┘
```

### How POP Works

When you execute `POP A`:
1. SP is **incremented** (moves up in memory)
2. The value at the new SP address is loaded into register A

```
Before POP A (SP=0xFC):            After POP A (SP=0xFD, A=42):
┌─────────┐                        ┌─────────┐
│ 0xFD: 42│                        │ 0xFD: 42│ ← SP (incremented)
├─────────┤                        ├─────────┤    A now = 42
│ 0xFC: ? │ ← SP                   │ 0xFC: ? │
└─────────┘                        └─────────┘
```

---

## Stack Instructions

### PUSH reg
**Opcode**: 0x15

Push register value onto stack.

**Format**: `PUSH A`

**Example**:
```assembly
LOAD A, 42
PUSH A        ; Save A on stack, SP decrements
LOAD A, 99    ; Overwrite A with new value
POP A         ; Restore A (A = 42 again)
```

**Flags**: None affected
**Side Effect**: SP decremented

---

### POP reg
**Opcode**: 0x16

Pop value from stack into register.

**Format**: `POP A`

**Example**:
```assembly
PUSH A
PUSH B
; ... do work that modifies A and B ...
POP B         ; Restore B first (LIFO order!)
POP A         ; Then restore A
```

**Flags**: None affected
**Side Effect**: SP incremented

---

## Stack Practical Examples

### Pattern 1: Register Preservation

Save registers before doing work, restore them after:

```assembly
; === Preserve all registers before work ===
PUSH A
PUSH B
PUSH C
PUSH D

; Do complex calculations that modify all registers
LOAD A, 100
ADD A, 50
MOV B, A
; ... more work ...

; === Restore all registers (reverse order!) ===
POP D         ; Must pop in REVERSE order
POP C
POP B
POP A         ; Original values restored
```

### Pattern 2: Temporary Storage

Use the stack to hold intermediate values:

```assembly
; Calculate (A + B) * 2 and store result
LOAD A, 10
LOAD B, 15
ADD A, B      ; A = 25
PUSH A        ; Save intermediate result (25)

ADD A, A      ; A = 50 (doubled)
OUT A         ; Output 50

POP B         ; Retrieve original sum into B (B = 25)
OUT B         ; Output 25

HALT
```

### Pattern 3: Swap Two Registers

Swap A and B without a temporary register:

```assembly
LOAD A, 10
LOAD B, 20

; Swap using stack
PUSH A        ; Stack: [10]
PUSH B        ; Stack: [10, 20]
POP A         ; A = 20, Stack: [10]
POP B         ; B = 10, Stack: []

; Now A=20, B=10
HALT
```

### Pattern 4: Subroutine Simulation

While BasCAT doesn't have CALL/RET, you can simulate subroutine behavior:

```assembly
; Main program
LOAD A, 5
PUSH A            ; Pass parameter on stack
JMP multiply_by_2 ; "Call" subroutine
return_point:
OUT A             ; A now contains result (10)
HALT

; Subroutine: Multiply stack value by 2
multiply_by_2:
  POP A           ; Get parameter
  ADD A, A        ; Double it
  JMP return_point ; "Return" to caller
```

---

## Stack Pitfalls

### ⚠️ Stack Underflow
Popping more than you pushed reads garbage data:
```assembly
PUSH A
POP A
POP B         ; DANGER! Nothing was pushed for B
              ; B gets undefined value
```

### ⚠️ Stack Overflow
Pushing too much overwrites program memory:
```assembly
; Stack only has 16 bytes (0xFD down to 0xEE)
; Pushing more than 16 values corrupts memory!
loop:
  PUSH A      ; Infinite push = memory corruption
  JMP loop
```

### ⚠️ Wrong Pop Order
LIFO means pop in **reverse** order of push:
```assembly
PUSH A        ; Stack: [A_value]
PUSH B        ; Stack: [A_value, B_value]

; WRONG - values are swapped!
POP A         ; A gets B's value!
POP B         ; B gets A's value!

; CORRECT order:
POP B         ; B gets B's value
POP A         ; A gets A's value
```

---

## I/O Instructions

### IN reg
**Opcode**: 0x06

Read from input port (address 0xFF) into register.

**Format**: `IN A`

**Example**:
```assembly
IN A          ; Read user input into A
OUT A         ; Echo it back
```

**Flags**: None affected
**Note**: Blocks until input is available

---

### OUT reg
**Opcode**: 0x07

Write register value to output port (address 0xFE).

**Format**: `OUT A`

**Example**:
```assembly
LOAD A, 65    ; ASCII 'A'
OUT A         ; Display 'A'
```

**Flags**: None affected

---

## System Instructions

### HALT
**Opcode**: 0x05

Stops program execution.

**Format**: `HALT`

**Example**:
```assembly
LOAD A, 10
OUT A
HALT          ; End program
```

**Flags**: None affected
**Effect**: Sets CPU halted flag, stops clock

---

### NOP
**Opcode**: 0x00

No operation (does nothing).

**Format**: `NOP`

**Example**:
```assembly
NOP           ; Placeholder or timing delay
NOP
LOAD A, 10
```

**Flags**: None affected

---

## Flags Register

The CPU maintains four status flags:

- **Z (Zero)**: Set when result is 0
- **N (Negative)**: Set when result is negative (bit 7 = 1)
- **C (Carry)**: Set on arithmetic overflow/carry
- **O (Overflow)**: Set on signed overflow

**Instructions that affect flags**: ADD, SUB, CMP, AND, OR, XOR, NOT

**Instructions that use flags**: JZ, JNZ, JC, JNC

---

## Memory Map

| Address Range | Usage |
|---------------|-------|
| 0x00 - 0xFC | User program and data (253 bytes) |
| 0xFD | Stack Pointer (SP) |
| 0xFE | Output Port |
| 0xFF | Input Port |

---

## Example Programs

### Hello World (Output 72)
```assembly
LOAD A, 72    ; ASCII 'H'
OUT A
HALT
```

### Count to 5
```assembly
LOAD A, 0
loop:
  OUT A
  ADD A, 1
  CMP A, 6
  JNZ loop
HALT
```

### Echo Input
```assembly
loop:
  IN A
  OUT A
  JMP loop
```

### Addition
```assembly
LOAD A, 5
LOAD B, 3
ADD A, B      ; Add B to A (register mode)
STM 0x80, A   ; Store result to variable A location
HALT
```

---

## Programming Tips

1. **Use labels** instead of absolute addresses: `JMP loop` not `JMP 10`
2. **Save registers** with PUSH/POP before subroutines
3. **Check flags** after CMP before conditional jumps
4. **Memory-mapped I/O**: 0xFE (OUT), 0xFF (IN)
5. **Stack grows down**: SP starts at 0xFD, decrements on PUSH
6. **Comments**: Use `;` for comments in your code

---

*BasCAT Assembly Language - Version 1.0*

*Part of the BasCAT Educational Computer Simulator*
