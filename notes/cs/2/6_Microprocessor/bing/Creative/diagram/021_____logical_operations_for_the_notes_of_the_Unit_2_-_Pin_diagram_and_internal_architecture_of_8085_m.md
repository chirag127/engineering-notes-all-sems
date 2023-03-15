### Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the bits of the operands.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register (A).
- The result of the logical operation is also stored in the accumulator register (A).
- The logical operations affect the flags of the 8085 microprocessor as follows:
  - The zero flag (Z) is set if the result is zero, otherwise it is reset.
  - The sign flag (S) is set if the most significant bit of the result is 1, otherwise it is reset.
  - The parity flag (P) is set if the result has even number of 1s, otherwise it is reset.
  - The carry flag (CY) and the auxiliary carry flag (AC) are always reset after a logical operation.
- The 8085 microprocessor supports the following logical instructions:

| Mnemonic | Operand | Description | Example |
| --- | --- | --- | --- |
| ANA | r or M | Performs bitwise AND operation between the accumulator and the register r or the memory location M. | ANA B |
| ANI | data | Performs bitwise AND operation between the accumulator and the immediate data. | ANI 0Fh |
| ORA | r or M | Performs bitwise OR operation between the accumulator and the register r or the memory location M. | ORA C |
| ORI | data | Performs bitwise OR operation between the accumulator and the immediate data. | ORI 55h |
| XRA | r or M | Performs bitwise XOR operation between the accumulator and the register r or the memory location M. | XRA D |
| XRI | data | Performs bitwise XOR operation between the accumulator and the immediate data. | XRI 99h |
| CMA | - | Complements the bits of the accumulator. | CMA |
| CMC | - | Complements the carry flag. | CMC |
| STC | - | Sets the carry flag. | STC |
| RLC | - | Rotates the bits of the accumulator left by one position. The leftmost bit is copied to the carry flag and the rightmost bit. | RLC |
| RRC | - | Rotates the bits of the accumulator right by one position. The rightmost bit is copied to the carry flag and the leftmost bit. | RRC |
| RAL | - | Rotates the bits of the accumulator left through the carry flag. The leftmost bit is copied to the carry flag and the carry flag is copied to the rightmost bit. | RAL |
| RAR | - | Rotates the bits of the accumulator right through the carry flag. The rightmost bit is copied to the carry flag and the carry flag is copied to the leftmost bit. | RAR |