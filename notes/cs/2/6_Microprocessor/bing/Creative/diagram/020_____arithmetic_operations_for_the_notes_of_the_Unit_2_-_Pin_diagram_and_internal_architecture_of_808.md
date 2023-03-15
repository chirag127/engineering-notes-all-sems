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

- The arithmetic operations can be classified into two types: binary and decimal.
- Binary arithmetic operations are performed on binary numbers and the result is also in binary form.
- Decimal arithmetic operations are performed on packed or unpacked BCD numbers and the result is also in BCD form.
- The DAA instruction is used to convert the binary result of an addition or subtraction operation into a valid BCD number.
- The arithmetic operations affect the flags of the 8085 microprocessor, such as the zero flag, the carry flag, the sign flag, the parity flag, and the auxiliary carry flag.
- The flags indicate the status of the result and can be used for conditional branching.
- The arithmetic and logic unit (ALU) is the part of the 8085 microprocessor that performs the arithmetic operations.
- The ALU can also perform logical operations, bit-shifting operations, and rotate operations.
- The ALU receives the operands from the accumulator and the temporary register, and sends the result to the accumulator.