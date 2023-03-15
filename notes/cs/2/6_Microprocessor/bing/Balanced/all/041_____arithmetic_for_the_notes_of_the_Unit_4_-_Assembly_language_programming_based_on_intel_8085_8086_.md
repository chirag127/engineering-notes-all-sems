# Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Arithmetic Instructions in 8085 Microprocessor

- Arithmetic instructions are the instructions that perform basic arithmetic operations such as addition, subtraction, increment, and decrement on data stored in registers or memory locations.
- The destination operand of arithmetic instructions is generally the accumulator (register A), which holds the result of the operation.
- The source operand can be a register, a memory location, or an immediate data (8-bit or 16-bit).
- Some arithmetic instructions also affect the flags of the 8085 microprocessor, such as the sign flag (S), the zero flag (Z), the auxiliary carry flag (AC), the parity flag (P), and the carry flag (CY).
- The following table summarizes the arithmetic instructions in 8085 microprocessor, their mnemonics, operands, and functions.

| Mnemonic | Operands | Function |
| --- | --- | --- |
| ADD | r or M | Add the contents of register r or memory location M to the accumulator |
| ADI | data | Add the 8-bit immediate data to the accumulator |
| ADC | r or M | Add the contents of register r or memory location M and the carry flag to the accumulator |
| ACI | data | Add the 8-bit immediate data and the carry flag to the accumulator |
| SUB | r or M | Subtract the contents of register r or memory location M from the accumulator |
| SUI | data | Subtract the 8-bit immediate data from the accumulator |
| SBB | r or M | Subtract the contents of register r or memory location M and the borrow (complement of carry flag) from the accumulator |
| SBI | data | Subtract the 8-bit immediate data and the borrow from the accumulator |
| INR | r or M | Increment the contents of register r or memory location M by 1 |
| INX | rp | Increment the contents of register pair rp by 1 |
| DCR | r or M | Decrement the contents of register r or memory location M by 1 |
| DCX | rp | Decrement the contents of register pair rp by 1 |
| DAD | rp | Add the contents of register pair rp to the HL register pair |
| DAA | - | Adjust the accumulator after a binary coded decimal (BCD) addition |

- The following are some examples of arithmetic instructions in 8085 microprocessor:

```
; Add the contents of register B to the accumulator
ADD B

; Add the 8-bit immediate data 25H to the accumulator
ADI 25H

; Subtract the contents of memory location 2000H from the accumulator
SUB M
LHLD 2000H

; Increment the contents of register C by 1
INR C

; Decrement the contents of register pair BC by 1
DCX B

; Add the contents of register pair DE to the HL register pair
DAD D

; Adjust the accumulator after a BCD addition
DAA
```