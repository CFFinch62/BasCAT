; Complex Program Demo
; Combines multiple Phase 3 features
; Implements a simple accumulator that sums input values

; Initialize accumulator in memory
LOAD A, 0
STM 20, A       ; Memory[20] = accumulator = 0

; Input loop - read values and add to accumulator
input_loop:
IN B            ; Read input value
CMP B, 0        ; Check if input is 0 (terminator)
JZ done         ; If zero, we're done

; Add to accumulator
LDM A, 20       ; Load current accumulator value
ADD A, B        ; Add input value
STM 20, A       ; Store back to memory

; Continue loop
JMP input_loop

; Output result
done:
LDM A, 20       ; Load final accumulator value
OUT A           ; Output result

HALT

; Example usage:
; Input: 5, 10, 15, 0
; Output: 30 (sum of 5+10+15)
