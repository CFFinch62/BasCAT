; Conditional Loop Demo
; Demonstrates CMP and conditional jumps (JZ, JNZ)
; Counts from 0 to 5 and outputs each number

LOAD A, 0       ; Initialize counter to 0

; Loop: Output current count and increment
loop:
OUT A           ; Output current value
ADD A, 1        ; Increment counter
CMP A, 6        ; Compare with 6
JNZ loop        ; If not zero (A != 6), jump back to loop

; When A == 6, we exit the loop
LOAD A, 255     ; Signal end with 255
OUT A

HALT
