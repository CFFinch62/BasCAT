# SimpleBASCAT: From BASIC to Assembly

## Original BASIC Program

```basic
10 REM SimpleBASCAT Demo
20 LET A = 0
30 INPUT B
40 LET A = A + B
50 PRINT A
60 IF A < 100 THEN GOTO 30
70 END
```

## Compiled Assembly Output

### Line 10: Comment (REM statement)
Comments are stripped during compilation - they don't generate any executable code.

```assembly
L10:
    ; BASIC line 10
    ; REM: SimpleBASCAT Demo
```

---

### Line 20: Initialize variable A to 0

**What happens:**
- Load the literal value 0 into register A
- Store the contents of register A into memory location 0x80 (where variable A lives)

```assembly
L20:
    ; BASIC line 20
    LOAD A, 0            ; Literal 0
    STM 0x80, A          ; A = result
```

**Memory state after execution:**
- Memory[0x80] = 0
- Register A = 0

---

### Line 30: Get input for variable B

**What happens:**
- Read input value into register A
- Store the contents of register A in memory location 0x81 (where variable B lives)

```assembly
L30:
    ; BASIC line 30
    IN A                 ; Input B
    STM 0x81, A          ; Store in B
```

**Memory state after execution:**
- Memory[0x81] = (user input value)
- Register A = (user input value)

---

### Line 40: Add B to A

**What happens:**
- Load the contents of memory location 0x80 into register A (get current value of A)
- Load the contents of memory location 0x81 into register B (get current value of B)
- Add the contents of register B to register A (result goes into register A)
- Store the contents of register A back into memory location 0x80 (save new value of A)

```assembly
L40:
    ; BASIC line 40
    LDM A, 0x80          ; Load A
    LDM B, 0x81          ; Load B
    ADD A, B             ; Add registers (A = A + B)
    STM 0x80, A          ; A = result
```

**Important:** The `ADD A, B` instruction is destructive - it adds B to A and stores the result in register A. Register B keeps its original value.

**Register state after ADD:**
- Register A = (original A value) + (B value)
- Register B = (B value) - unchanged

---

### Line 50: Print the value of A

**What happens:**
- Load the contents of memory location 0x80 into register A (get current value of A)
- Output the contents of register A to the display

```assembly
L50:
    ; BASIC line 50
    LDM A, 0x80          ; Load A
    OUT A                ; Print value
```

---

### Line 60: Loop if A is less than 100

**What happens:**
- Load the contents of memory location 0x80 into register A (get current value of A)
- Compare the contents of register A with the literal value 100
- If the comparison shows A < 100, jump back to label L30 (continue the loop)

```assembly
L60:
    ; BASIC line 60
    LDM A, 0x80          ; Load A
    CMP A, 0x64          ; Compare: <
    JC L30               ; Jump if less than
```

**The CMP instruction** sets internal flags based on the comparison. The JC (Jump if Carry/Condition) instruction checks these flags and jumps if the "less than" condition is true.

---

### Line 70: Stop the program

**What happens:**
- Halt execution

```assembly
L70:
    ; BASIC line 70
    HALT                 ; END
```

---

## Program Summary

This program will:
1. Initialize A to 0
2. Get input for B
3. Add B to A
4. Print the new value of A
5. If A is less than 100, go back to step 2 (get another input)
6. When A reaches 100 or more, halt

## Key Learning Points

### Variable Storage
- Variables live in memory at fixed addresses
- Variable A is stored at memory location 0x80
- Variable B is stored at memory location 0x81

### Register vs Memory
- Registers (A and B) are fast temporary storage inside the CPU
- Memory is slower but persistent storage
- Every operation on variables requires: **Load from memory → Operate in registers → Store back to memory**

### The Cost of `A = A + B`
In BASIC, this looks like one simple operation. But the CPU must:
1. Load A from memory into a register
2. Load B from memory into another register
3. Add them together
4. Store the result back to memory

That's **4 instructions** for what looks like 1 line of code!

### Control Flow
- Labels (L10, L20, etc.) mark locations in the program
- Comparison + conditional jump implements IF...THEN logic
- GOTO becomes an unconditional jump to a label
