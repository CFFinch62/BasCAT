; SimpleBASCAT Compiled Program

L10:
                     ; BASIC line 10
                     ; REM: Simple Addition
L20:
                     ; BASIC line 20
                     ; REM: Demonstrates arithmetic operations
L30:
                     ; BASIC line 30
LOAD A, 5            ; Literal 5
STM 10, A            ; A = result
L40:
                     ; BASIC line 40
LOAD A, 3            ; Literal 3
STM 11, A            ; B = result
L50:
                     ; BASIC line 50
LDM A, 10            ; Load A
LDM B, 11            ; Load B
ADD A, B             ; Add registers
STM 12, A            ; C = result
L60:
                     ; BASIC line 60
LDM A, 12            ; Load C
OUT A                ; Print value
L70:
                     ; BASIC line 70
HALT                 ; END