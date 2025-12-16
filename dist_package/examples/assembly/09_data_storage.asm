; Data Storage Demo
; Demonstrates using the free RAM area (0x9A-0xED) for data storage
; This is the assembly equivalent of POKE and PEEK in BASIC

; Store some values in the data area
LOAD A, 42          ; Value to store
STM 0x9A, A         ; Store at address 154 (first free byte)

LOAD A, 100         ; Another value
STM 0x9B, A         ; Store at address 155

LOAD A, 255         ; Maximum byte value
STM 0x9C, A         ; Store at address 156

; Read and print the stored values
LDM A, 0x9A         ; Load from address 154
OUT A               ; Output: 42

LDM A, 0x9B         ; Load from address 155
OUT A               ; Output: 100

LDM A, 0x9C         ; Load from address 156
OUT A               ; Output: 255

HALT
