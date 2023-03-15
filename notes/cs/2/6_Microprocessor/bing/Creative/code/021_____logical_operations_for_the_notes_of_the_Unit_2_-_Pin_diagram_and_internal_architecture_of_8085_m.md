### Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the binary data stored in the registers or memory locations.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register. The source operand can be another register, an immediate data, or a memory location.
- The logical operations work on a bitwise level, meaning that each bit of the operands is compared and the result is stored in the corresponding bit of the accumulator.
- The logical instructions also affect the flags of the 8085 microprocessor, such as the zero flag, the sign flag, the parity flag, and the carry flag. The auxiliary carry flag is always reset by the logical instructions.
- The logical instructions in the 8085 microprocessor are summarized in the following table:

| Mnemonic | Description | Example |
| --- | --- | --- |
| ANA | Logical AND with accumulator | ANA B (A <- A AND B) |
| ANI | Logical AND with immediate data | ANI 0F (A <- A AND 0F) |
| ORA | Logical OR with accumulator | ORA C (A <- A OR C) |
| ORI | Logical OR with immediate data | ORI 0A (A <- A OR 0A) |
| XRA | Logical XOR with accumulator | XRA D (A <- A XOR D) |
| XRI | Logical XOR with immediate data | XRI 0B (A <- A XOR 0B) |
| CMA | Complement accumulator | CMA (A <- NOT A) |
| RLC | Rotate accumulator left | RLC (A <- A << 1, bit 0 <- bit 7, CY <- bit 7) |
| RRC | Rotate accumulator right | RRC (A <- A >> 1, bit 7 <- bit 0, CY <- bit 0) |
| RAL | Rotate accumulator left through carry | RAL (A <- A << 1, bit 0 <- CY, CY <- bit 7) |
| RAR | Rotate accumulator right through carry | RAR (A <- A >> 1, bit 7 <- CY, CY <- bit 0) |
| CMC | Complement carry flag | CMC (CY <- NOT CY) |
| STC | Set carry flag | STC (CY <- 1) |