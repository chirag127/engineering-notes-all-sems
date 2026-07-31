### Addressing Modes

- Addressing modes are the different ways of specifying the location of an operand in an instruction .
- Operand is the data on which the operation specified by the instruction is performed.
- Different types of addressing modes exist, each with its own advantages and disadvantages .
- The syntax of addressing mode is the way of representing the addressing mode used.
- The choice of addressing mode affects the instruction format, the instruction set, and the performance of the processor .

#### Types of Addressing Modes

- There are many types of addressing modes, but some of the common ones are   :

  - **Immediate**: The operand is specified in the instruction itself. For example, `ADD #5, R1` means add 5 to the contents of register R1.
  - **Direct**: The operand is stored in a memory location, and the address of that location is specified in the instruction. For example, `ADD 1000, R1` means add the contents of memory location 1000 to the contents of register R1.
  - **Register**: The operand is stored in a register, and the register number is specified in the instruction. For example, `ADD R2, R1` means add the contents of register R2 to the contents of register R1.
  - **Register Indirect**: The operand is stored in a memory location, and the address of that location is stored in a register. The register number is specified in the instruction. For example, `ADD (R2), R1` means add the contents of the memory location pointed by register R2 to the contents of register R1.
  - **Displacement**: The operand is stored in a memory location, and the address of that location is calculated by adding a constant displacement to the contents of a register. The register number and the displacement are specified in the instruction. For example, `ADD 10(R2), R1` means add the contents of the memory location obtained by adding 10 to the contents of register R2 to the contents of register R1.
  - **Indexed**: The operand is stored in a memory location, and the address of that location is calculated by adding the contents of an index register to the contents of a base register. The register numbers are specified in the instruction. For example, `ADD (R2+R3), R1` means add the contents of the memory location obtained by adding the contents of register R2 and register R3 to the contents of register R1.
  - **Relative**: The operand is stored in a memory location, and the address of that location is calculated by adding a constant displacement to the contents of the program counter. The displacement is specified in the instruction. For example, `ADD PC+10, R1` means add the contents of the memory location obtained by adding 10 to the program counter to the contents of register R1.
  - **Base Register**: The operand is stored in a memory location, and the address of that location is calculated by adding a constant displacement to the contents of a base register. The register number and the displacement are specified in the instruction. For example, `ADD 10(R4), R1` means add the contents of the memory location obtained by adding 10 to the contents of register R4 to the contents of register R1.
  - **Stack**: The operand is stored at the top of the stack, and the stack pointer is used to access it. The stack pointer is automatically incremented or decremented as the stack is pushed or popped. For example, `ADD (SP), R1` means add the contents of the top of the stack to the contents of register R1.