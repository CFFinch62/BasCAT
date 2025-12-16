; Stack Subroutine Demo
; Demonstrates using the stack to pass parameters
; and simulate subroutine calls without CALL/RET

; === Main Program ===
; We'll "call" a subroutine to double a number

; First call: double 5
LOAD A, 5
PUSH A            ; Pass parameter (5) on stack
JMP double_it     ; "Call" the subroutine
return1:
OUT A             ; Output result: 10

; Second call: double 21
LOAD A, 21
PUSH A            ; Pass parameter (21) on stack
JMP double_it     ; "Call" the subroutine
return2:
OUT A             ; Output result: 42

HALT

; === Subroutine: double_it ===
; Input: Value on top of stack
; Output: Result in register A
; Doubles the input value
double_it:
  POP A           ; Get parameter from stack
  ADD A, A        ; Double it (A = A + A)
  ; Determine which return point based on caller
  ; (For simplicity, we use a conditional approach)
  CMP A, 10
  JZ return1      ; If result is 10, came from first call
  JMP return2     ; Otherwise, came from second call
