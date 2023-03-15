### Addressing Modes

Addressing modes are the ways in which the location of an operand is specified within an instruction. The 8085 microprocessor supports several addressing modes. These include:

1. **Immediate Addressing**: In this mode, the operand is specified in the instruction itself. For example, `MVI A, 05H` loads the value `05H` into the accumulator.

2. **Register Addressing**: In this mode, the operand is located in one of the registers. For example, `MOV A, B` copies the contents of register B into the accumulator.

3. **Direct Addressing**: In this mode, the address of the operand is specified in the instruction. For example, `LDA 2050H` loads the accumulator with the contents of memory location `2050H`.

4. **Register Indirect Addressing**: In this mode, the instruction specifies a register that contains the address of the operand. For example, `MOV A, M` copies the contents of the memory location pointed to by the `HL` register pair into the accumulator.

5. **Indexed Addressing**: In this mode, the instruction specifies a base register and an index value. The effective address of the operand is calculated by adding the index value to the contents of the base register. This mode is not available in the 8085 microprocessor.

6. **Relative Addressing**: In this mode, the instruction specifies a relative address, which is added to the program counter to obtain the effective address of the operand. This mode is not available in the 8085 microprocessor.

These are the different addressing modes supported by the 8085 microprocessor. Understanding these modes is essential for programming the microprocessor effectively.