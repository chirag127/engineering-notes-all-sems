### Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the bits of the operands.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register (A).
- The logical operations work on a bitwise level, meaning that each bit of the accumulator is logically operated with the corresponding bit of the source operand.
- The source operand can be either a register, a memory location, or an immediate data.
- The result of the logical operation is stored in the accumulator register and the flags are affected accordingly.
- The logical instructions in 8085 microprocessor are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| ANA | Logical AND with accumulator | ANA B (A <- A AND B) |
| ANI | Logical AND with immediate data | ANI 0F (A <- A AND 0F) |
| ORA | Logical OR with accumulator | ORA C (A <- A OR C) |
| ORI | Logical OR with immediate data | ORI 0F (A <- A OR 0F) |
| XRA | Logical XOR with accumulator | XRA D (A <- A XOR D) |
| XRI | Logical XOR with immediate data | XRI 0F (A <- A XOR 0F) |
| CMA | Complement accumulator | CMA (A <- NOT A) |
| RLC | Rotate accumulator left | RLC (A <- A << 1, bit 0 <- bit 7) |
| RRC | Rotate accumulator right | RRC (A <- A >> 1, bit 7 <- bit 0) |
| RAL | Rotate accumulator left through carry | RAL (A <- A << 1, bit 0 <- CY, CY <- bit 7) |
| RAR | Rotate accumulator right through carry | RAR (A <- A >> 1, bit 7 <- CY, CY <- bit 0) |

- The flags affected by the logical instructions are:

| Flag | Condition |
| --- | --- |
| S | Set if the result is negative (MSB is 1) |
| Z | Set if the result is zero |
| P | Set if the result has even parity (even number of 1s) |
| CY | Set or reset according to the operation |
| AC | Set if there is a carry from bit 3 to bit 4 |