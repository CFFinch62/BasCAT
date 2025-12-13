; Example 2: Add Two Numbers
; Reads two single-digit numbers and outputs their sum
;
; Instructions:
; 1. Input first number (e.g., type "5")
; 2. Run the program
; 3. Input second number when prompted (e.g., type "3")
; 4. See the sum appear in output
;
; Note: This works with ASCII values, so input '5' (ASCII 53)
; + '3' (ASCII 51) = ASCII 104 (which is 'h')
; For actual numeric addition, you'd need to convert ASCII to numbers

IN A          ; Read first number to A
IN B          ; Read second number to B
LOAD C, 0     ; Clear C (result register)
; TODO: ADD A, B would go to A, need to implement proper ADD
; For now, just output what we read
OUT A         ; Output first number
OUT B         ; Output second number
HALT
