### Arithmetic Operations

- The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement .
- These arithmetic operations have the following mnemonics :

| Mnemonic | Operand | Explanation |
| --- | --- | --- |
| ADD | r/M/data | Add register, memory or data to accumulator |
| ADC | r/M/data | Add register, memory or data to accumulator with carry |
| SUB | r/M/data | Subtract register, memory or data from accumulator |
| SBB | r/M/data | Subtract register, memory or data from accumulator with borrow |
| INR | r/M | Increment register or memory by 1 |
| DCR | r/M | Decrement register or memory by 1 |
| INX | rp | Increment register pair by 1 |
| DCX | rp | Decrement register pair by 1 |
| DAD | rp | Add register pair to HL register pair |
| DAA | - | Decimal adjust accumulator |

- The 8085 microprocessor also performs multiplication and division operations by using repeated addition and subtraction instructions.
- The arithmetic operations affect the flags in the flag register, such as the zero flag, the sign flag, the parity flag, the carry flag, and the auxiliary carry flag .
- The arithmetic operations are performed by the arithmetic and logic unit (ALU) of the 8085 microprocessor, which is a part of the internal architecture.
- The arithmetic operations are classified as data transfer instructions, as they transfer data between the accumulator and other registers, memory or data .