# Arithmetic Operations in 8085 Microprocessor

- The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement  .
- These arithmetic operations have the following mnemonics  :

| Mnemonic | Operand | Explanation |
| --- | --- | --- |
| ADD | r/M | Add register or memory to accumulator |
| ADC | r/M | Add register or memory to accumulator with carry |
| ADI | data | Add immediate data to accumulator |
| ACI | data | Add immediate data to accumulator with carry |
| DAD | rp | Add register pair to HL register pair |
| SUB | r/M | Subtract register or memory from accumulator |
| SBB | r/M | Subtract register or memory from accumulator with borrow |
| SUI | data | Subtract immediate data from accumulator |
| SBI | data | Subtract immediate data from accumulator with borrow |
| INR | r/M | Increment register or memory by 1 |
| INX | rp | Increment register pair by 1 |
| DCR | r/M | Decrement register or memory by 1 |
| DCX | rp | Decrement register pair by 1 |

- The arithmetic operations affect the flags of the 8085 microprocessor, such as the sign flag, zero flag, auxiliary carry flag, parity flag, and carry flag .
- The arithmetic operations are performed by the arithmetic and logic unit (ALU) of the 8085 microprocessor, which is a part of the internal architecture.
- The arithmetic operations are classified as data transfer instructions, as they transfer data between the registers, memory, and accumulator .