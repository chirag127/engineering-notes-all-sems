# Arithmetic Operations in 8085 Microprocessor

- The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement .
- These arithmetic operations have the following mnemonics :

| Mnemonic | Description |
| --- | --- |
| ADD r | Add register r to the accumulator |
| ADD M | Add memory location (HL) to the accumulator |
| ADI data | Add immediate data to the accumulator |
| ADC r | Add register r and carry flag to the accumulator |
| ADC M | Add memory location (HL) and carry flag to the accumulator |
| ACI data | Add immediate data and carry flag to the accumulator |
| SUB r | Subtract register r from the accumulator |
| SUB M | Subtract memory location (HL) from the accumulator |
| SUI data | Subtract immediate data from the accumulator |
| SBB r | Subtract register r and borrow flag from the accumulator |
| SBB M | Subtract memory location (HL) and borrow flag from the accumulator |
| SBI data | Subtract immediate data and borrow flag from the accumulator |
| INR r | Increment register r by 1 |
| INR M | Increment memory location (HL) by 1 |
| INX rp | Increment register pair rp by 1 |
| DCR r | Decrement register r by 1 |
| DCR M | Decrement memory location (HL) by 1 |
| DCX rp | Decrement register pair rp by 1 |
| DAA | Decimal adjust accumulator |

- The arithmetic operations affect the following flags in the flag register :

| Flag | Description |
| --- | --- |
| S | Set if the result is negative, reset otherwise |
| Z | Set if the result is zero, reset otherwise |
| AC | Set if there is a carry from the lower nibble, reset otherwise |
| P | Set if the result has even parity, reset otherwise |
| CY | Set if there is a carry from the higher nibble, reset otherwise |

- The arithmetic operations are classified into two types: direct and indirect.
- Direct operations involve the use of immediate data or register operands, while indirect operations involve the use of memory operands.
- The arithmetic operations are executed by the arithmetic and logic unit (ALU) of the 8085 microprocessor .
- The ALU performs the operations by using the accumulator as one of the operands and storing the result in the accumulator .
- The ALU can also perform logical operations, bit-shifting operations, and decimal adjustment operations.