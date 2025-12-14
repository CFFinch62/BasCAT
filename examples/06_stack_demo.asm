; Stack Operations Demo
; Demonstrates PUSH and POP instructions
; Shows LIFO (Last In, First Out) behavior

; Load some values into registers
LOAD A, 10
LOAD B, 20
LOAD C, 30
LOAD D, 40

; Push all values onto stack
PUSH A          ; Stack: [10]
PUSH B          ; Stack: [10, 20]
PUSH C          ; Stack: [10, 20, 30]
PUSH D          ; Stack: [10, 20, 30, 40]

; Clear all registers
LOAD A, 0
LOAD B, 0
LOAD C, 0
LOAD D, 0

; Pop values back - should come in reverse order
POP D           ; D = 40, Stack: [10, 20, 30]
POP C           ; C = 30, Stack: [10, 20]
POP B           ; B = 20, Stack: [10]
POP A           ; A = 10, Stack: []

; Output values to verify LIFO order
OUT D           ; Should output 40
OUT C           ; Should output 30
OUT B           ; Should output 20
OUT A           ; Should output 10

HALT
