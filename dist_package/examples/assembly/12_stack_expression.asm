; Stack Expression Evaluation
; Demonstrates using the stack for expression evaluation
; Calculates: (3 + 7) * 2 = 20

; Step 1: Push operands for addition
LOAD A, 3
PUSH A            ; Stack: [3]
LOAD A, 7
PUSH A            ; Stack: [3, 7]

; Step 2: Pop, add, push result
POP B             ; B = 7, Stack: [3]
POP A             ; A = 3, Stack: []
ADD A, B          ; A = 10 (3 + 7)
PUSH A            ; Stack: [10] - intermediate result

; Step 3: Push multiplier
LOAD B, 2         ; Multiplier is 2

; Step 4: Pop intermediate, multiply (via repeated addition)
POP A             ; A = 10, Stack: []
; Since we don't have MUL, double it (10 * 2 = 10 + 10)
ADD A, A          ; A = 20

; Step 5: Output final result
OUT A             ; Output: 20

; For comparison, output individual components
LOAD A, 3
OUT A             ; Output: 3 (first operand)
LOAD A, 7
OUT A             ; Output: 7 (second operand)
LOAD A, 10
OUT A             ; Output: 10 (sum before multiply)

HALT
