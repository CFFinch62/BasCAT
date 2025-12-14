; MOV Instruction Demo
; Demonstrates register-to-register and immediate-to-register moves

; Load initial value
LOAD A, 100

; Copy between registers
MOV B, A        ; B = A = 100
MOV C, B        ; C = B = 100
MOV D, C        ; D = C = 100

; Output all registers to verify
OUT A           ; Should output 100
OUT B           ; Should output 100
OUT C           ; Should output 100
OUT D           ; Should output 100

; Use MOV with immediate values
MOV A, 50       ; A = 50 (immediate value)
MOV B, 60       ; B = 60
MOV C, 70       ; C = 70
MOV D, 80       ; D = 80

; Output to verify immediate moves
OUT A           ; Should output 50
OUT B           ; Should output 60
OUT C           ; Should output 70
OUT D           ; Should output 80

HALT
