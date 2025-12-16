; Example 2: Add Two Numbers
; Reads two single-digit numbers and outputs their sum
;
; Instructions:
; 1. Input first number (e.g., type "5")
; 2. Input second number (e.g., type "3")
; 3. See the sum appear in output
;
; Note: This works with ASCII values, so input '5' (ASCII 53)
; + '3' (ASCII 51) = ASCII 104 (which is 'h')
; For numeric addition, subtract 0x30 from each digit first

IN A          ; Read first number to A
IN B          ; Read second number to B  
ADD A, B      ; Add A + B, result in A
OUT A         ; Output the sum
HALT
