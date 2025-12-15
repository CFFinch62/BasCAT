; Stack Swap Demo
; Demonstrates using the stack to swap register values
; without needing a temporary register

; Load initial values
LOAD A, 65        ; A = 65 (ASCII 'A')
LOAD B, 66        ; B = 66 (ASCII 'B')

; Output original order: A then B
OUT A             ; Output 'A'
OUT B             ; Output 'B'

; Use stack to swap A and B
PUSH A            ; Stack: [65]
PUSH B            ; Stack: [65, 66]
POP A             ; A = 66 (was B), Stack: [65]
POP B             ; B = 65 (was A), Stack: []

; Output swapped order: A then B (now reversed)
OUT A             ; Output 'B' (66)
OUT B             ; Output 'A' (65)

HALT
