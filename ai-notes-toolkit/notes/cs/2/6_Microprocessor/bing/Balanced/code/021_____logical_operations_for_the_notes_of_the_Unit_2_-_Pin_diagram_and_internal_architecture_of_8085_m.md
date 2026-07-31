### Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the binary data stored in the registers or memory locations.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register. The source operand can be another register, an immediate data, or a memory location.
- The logical operations work on a bitwise level, meaning that each bit of the operands is compared and the result is stored in the corresponding bit of the accumulator.
- The logical instructions also affect the flags of the 8085 microprocessor, such as the zero flag, the sign flag, the parity flag, and the carry flag. The auxiliary carry flag is always reset by the logical instructions.
- The logical instructions in the 8085 microprocessor are:

  - ANA: This instruction performs the bitwise AND operation between the accumulator and the source operand. The result is stored in the accumulator. The syntax is `ANA R/M/8-bit data`.
  - ORA: This instruction performs the bitwise OR operation between the accumulator and the source operand. The result is stored in the accumulator. The syntax is `ORA R/M/8-bit data`.
  - XRA: This instruction performs the bitwise XOR operation between the accumulator and the source operand. The result is stored in the accumulator. The syntax is `XRA R/M/8-bit data`.
  - CMA: This instruction performs the bitwise complement operation on the accumulator. The result is stored in the accumulator. The syntax is `CMA`.
  - RLC: This instruction performs the left circular shift operation on the accumulator. The leftmost bit of the accumulator is copied to the carry flag and the carry flag is copied to the rightmost bit of the accumulator. The syntax is `RLC`.
  - RRC: This instruction performs the right circular shift operation on the accumulator. The rightmost bit of the accumulator is copied to the carry flag and the carry flag is copied to the leftmost bit of the accumulator. The syntax is `RRC`.
  - RAL: This instruction performs the left arithmetic shift operation on the accumulator. The leftmost bit of the accumulator is copied to the carry flag and the carry flag is shifted to the rightmost bit of the accumulator. The syntax is `RAL`.
  - RAR: This instruction performs the right arithmetic shift operation on the accumulator. The rightmost bit of the accumulator is copied to the carry flag and the carry flag is shifted to the leftmost bit of the accumulator. The syntax is `RAR`.