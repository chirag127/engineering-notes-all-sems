# Unit 1 - Introduction: Addressing Modes

Addressing modes are the ways in which the location of an operand is specified within an instruction. The operand is the data that the instruction will operate on. Different addressing modes provide flexibility in accessing operands, allowing for more efficient and versatile instruction execution.

Here are some common addressing modes:

1. **Immediate addressing:** The operand is specified as a constant value within the instruction itself.
2. **Direct addressing:** The address of the operand is specified directly within the instruction.
3. **Indirect addressing:** The instruction specifies the address of a memory location that contains the address of the operand.
4. **Register addressing:** The operand is located in a specific register.
5. **Register indirect addressing:** The instruction specifies a register that contains the address of the operand.
6. **Indexed addressing:** The instruction specifies the base address of the operand, and an index register is used to provide an offset from the base address.
7. **Base-plus-index addressing:** Similar to indexed addressing, but the instruction specifies both the base address and the index register.
8. **Relative addressing:** The instruction specifies an offset from the current instruction pointer.

Different processors may support different addressing modes, and the choice of addressing mode can affect the efficiency and performance of the instruction execution. It is important to understand the addressing modes supported by a particular processor when writing assembly language programs or optimizing code for that processor.