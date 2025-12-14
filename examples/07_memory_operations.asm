; Memory Operations Demo
; Demonstrates LDM (Load from Memory) and STM (Store to Memory)
; Shows how to use memory as variables

; Store values to memory locations
LOAD A, 42
STM 10, A       ; Memory[10] = 42

LOAD B, 84
STM 11, B       ; Memory[11] = 84

LOAD C, 126
STM 12, C       ; Memory[12] = 126

; Clear registers
LOAD A, 0
LOAD B, 0
LOAD C, 0

; Load values back from memory
LDM A, 10       ; A = Memory[10] = 42
LDM B, 11       ; B = Memory[11] = 84
LDM C, 12       ; C = Memory[12] = 126

; Output to verify
OUT A           ; Should output 42
OUT B           ; Should output 84
OUT C           ; Should output 126

HALT
