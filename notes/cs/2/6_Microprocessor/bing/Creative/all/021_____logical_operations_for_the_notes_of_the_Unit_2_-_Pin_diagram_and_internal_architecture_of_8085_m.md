# Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the binary data stored in the registers or memory locations.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register. The logical operations work on a bitwise level, meaning that each bit of the operands is compared and the result is stored in the corresponding bit of the accumulator.
- The logical instructions also affect the flags of the 8085 microprocessor, such as the zero flag (Z), the sign flag (S), the parity flag (P), the carry flag (CY), and the auxiliary carry flag (AC).
- The logical instructions in the 8085 microprocessor are:

  - **AND** instructions: These instructions perform the bitwise logical AND operation between the accumulator and the source operand. The source operand can be a register, an immediate data, or a memory location. The syntax of the AND instructions is:

    - `ANI data`: This instruction performs the bitwise AND operation between the accumulator and the 8-bit immediate data. The result is stored in the accumulator. For example, `ANI 0Fh` performs the bitwise AND operation between the accumulator and the hexadecimal number 0Fh.
    - `ANA r`: This instruction performs the bitwise AND operation between the accumulator and the register r, where r can be B, C, D, E, H, or L. The result is stored in the accumulator. For example, `ANA B` performs the bitwise AND operation between the accumulator and the register B.
    - `ANA M`: This instruction performs the bitwise AND operation between the accumulator and the memory location pointed by the HL register pair. The result is stored in the accumulator. For example, `ANA M` performs the bitwise AND operation between the accumulator and the memory location pointed by the HL register pair.

  - **OR** instructions: These instructions perform the bitwise logical OR operation between the accumulator and the source operand. The source operand can be a register, an immediate data, or a memory location. The syntax of the OR instructions is:

    - `ORI data`: This instruction performs the bitwise OR operation between the accumulator and the 8-bit immediate data. The result is stored in the accumulator. For example, `ORI 0Fh` performs the bitwise OR operation between the accumulator and the hexadecimal number 0Fh.
    - `ORA r`: This instruction performs the bitwise OR operation between the accumulator and the register r, where r can be B, C, D, E, H, or L. The result is stored in the accumulator. For example, `ORA B` performs the bitwise OR operation between the accumulator and the register B.
    - `ORA M`: This instruction performs the bitwise OR operation between the accumulator and the memory location pointed by the HL register pair. The result is stored in the accumulator. For example, `ORA M` performs the bitwise OR operation between the accumulator and the memory location pointed by the HL register pair.

  - **XOR** instructions: These instructions perform the bitwise logical XOR (exclusive OR) operation between the accumulator and the source operand. The source operand can be a register, an immediate data, or a memory location. The syntax of the XOR instructions is:

    - `XRI data`: This instruction performs the bitwise XOR operation between the accumulator and the 8-bit immediate data. The result is stored in the accumulator. For example, `XRI 0Fh` performs the bitwise XOR operation between the accumulator and the hexadecimal number 0Fh.
    - `XRA r`: This instruction performs the bitwise XOR operation between the accumulator and the register r, where r can be B, C, D, E, H, or L. The result is stored in the accumulator. For example, `XRA B` performs the bitwise XOR operation between the accumulator and the register B.
    - `XRA M`: This instruction performs the bitwise XOR operation between the accumulator and the memory location pointed by the HL register pair. The result is stored in the accumulator. For example, `XRA M` performs the bitwise XOR operation between the accumulator and the memory location pointed by the HL register pair.

  - **NOT** instruction: This instruction performs the bitwise logical NOT (complement) operation on the accumulator. The syntax of the NOT instruction is:

    - `CMA`: This instruction complements each bit of the accumulator. For example, if the accumulator contains 1010 0101, then after executing `CMA`, the accumulator will