### Arithmetic Instructions in 8085 Microprocessor

- Arithmetic instructions are the instructions that perform basic arithmetic operations such as addition, subtraction, increment, and decrement on the data stored in the registers or memory locations.
- The destination operand of the arithmetic instructions is generally the accumulator, which holds the result of the operation.
- The arithmetic instructions can be classified into four categories: addition, subtraction, increment, and decrement.
- The following table summarizes the arithmetic instructions in 8085 microprocessor with their mnemonics, operands, and functions.

| Mnemonic | Operands | Function |
| --- | --- | --- |
| ADD r | A <- A + r | Add the contents of register r to the accumulator |
| ADD M | A <- A + M | Add the contents of memory location pointed by HL pair to the accumulator |
| ADI data | A <- A + data | Add the 8-bit immediate data to the accumulator |
| ADC r | A <- A + r + CY | Add the contents of register r and the carry flag to the accumulator |
| ADC M | A <- A + M + CY | Add the contents of memory location pointed by HL pair and the carry flag to the accumulator |
| ACI data | A <- A + data + CY | Add the 8-bit immediate data and the carry flag to the accumulator |
| SUB r | A <- A - r | Subtract the contents of register r from the accumulator |
| SUB M | A <- A - M | Subtract the contents of memory location pointed by HL pair from the accumulator |
| SUI data | A <- A - data | Subtract the 8-bit immediate data from the accumulator |
| SBB r | A <- A - r - CY | Subtract the contents of register r and the borrow flag from the accumulator |
| SBB M | A <- A - M - CY | Subtract the contents of memory location pointed by HL pair and the borrow flag from the accumulator |
| SBI data | A <- A - data - CY | Subtract the 8-bit immediate data and the borrow flag from the accumulator |
| INR r | r <- r + 1 | Increment the contents of register r by 1 |
| INR M | M <- M + 1 | Increment the contents of memory location pointed by HL pair by 1 |
| INX rp | rp <- rp + 1 | Increment the contents of register pair rp by 1 |
| DCR r | r <- r - 1 | Decrement the contents of register r by 1 |
| DCR M | M <- M - 1 | Decrement the contents of memory location pointed by HL pair by 1 |
| DCX rp | rp <- rp - 1 | Decrement the contents of register pair rp by 1 |

- The arithmetic instructions affect the following flags: sign, zero, auxiliary carry, parity, and carry.
- The sign flag is set if the result is negative, and reset if the result is positive.
- The zero flag is set if the result is zero, and reset if the result is non-zero.
- The auxiliary carry flag is set if there is a carry from the lower nibble (4 bits) of the result, and reset otherwise.
- The parity flag is set if the result has even number of 1s in its binary representation, and reset if the result has odd number of 1s.
- The carry flag is set if there is a carry from the higher nibble (4 bits) of the result, and reset otherwise.

- The following are some examples of arithmetic instructions in 8085 microprocessor:

```assembly
; Example 1: Add the contents of registers B and C and store the result in the accumulator
MOV A, B ; Move the contents of B to A
ADD C ; Add the contents of C to A
; The result is in A

; Example 2: Subtract the contents of memory location 2000H from the accumulator and store the result in the accumulator
LXI H, 2000H ; Load the address 2000H in HL pair
SUB M ; Subtract the contents of memory location pointed by HL pair from A
; The result is in A

; Example 3: Increment the contents of register D by 1 and store the result in register D
INR D ; Increment the contents of D by 1
; The result is in D

; Example 4: Decrement the contents of register pair BC by 1 and store the result in register pair BC
DCX B ; Decrement the contents of BC by 1
; The

```
