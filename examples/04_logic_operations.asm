; Logic Operations Demo
; Demonstrates AND, OR, XOR, NOT instructions
; Shows how to manipulate bits

; Load test values
LOAD A, 0xF0    ; Binary: 11110000
LOAD B, 0x0F    ; Binary: 00001111

; AND Operation - should give 0x00
MOV A, A        ; Copy A to A (no-op but demonstrates MOV)
AND A, 0x0F     ; A = A AND 00001111 = 00000000
OUT A           ; Output 0

; OR Operation - should give 0xFF
LOAD A, 0xF0    ; Reload: 11110000
OR A, 0x0F      ; A = A OR 00001111 = 11111111
OUT A           ; Output 255

; XOR Operation - should give 0xFF
LOAD A, 0xF0    ; Reload: 11110000
XOR A, 0x0F     ; A = A XOR 00001111 = 11111111
OUT A           ; Output 255

; NOT Operation - should give 0x0F
LOAD A, 0xF0    ; Reload: 11110000
NOT A           ; A = NOT A = 00001111
OUT A           ; Output 15

HALT
