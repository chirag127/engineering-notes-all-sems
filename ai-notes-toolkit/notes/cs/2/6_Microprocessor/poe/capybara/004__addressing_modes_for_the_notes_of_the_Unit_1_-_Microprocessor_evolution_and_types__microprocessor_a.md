### Addressing Modes

Addressing modes are techniques used by microprocessors to access memory locations or data operands. Different addressing modes have different advantages and disadvantages, depending on the specific application. Here are some of the most common addressing modes:

1. Immediate Addressing Mode
- The operand is directly specified in the instruction
- Example: MOV AX, #1234H

2. Direct Addressing Mode
- The operand is stored in a memory location, and the instruction specifies the memory address of the operand
- Example: MOV AX, [2000H]

3. Register Addressing Mode
- The operand is stored in a register, and the instruction specifies the register that contains the operand
- Example: MOV AX, BX

4. Indirect Addressing Mode
- The operand is stored in a memory location, and the instruction specifies the memory address of the memory location that contains the operand
- Example: MOV AX, [BX]

5. Indexed Addressing Mode
- The operand is stored in a memory location, and the instruction specifies the memory address of the memory location that contains the operand, plus an offset value stored in a register
- Example: MOV AX, [SI+10H]

6. Relative Addressing Mode
- The operand is stored in a memory location, and the instruction specifies the relative offset of the memory location from the current instruction pointer value
- Example: JMP LABEL

7. Base-Indexed Addressing Mode
- The operand is stored in a memory location, and the instruction specifies the memory address of the memory location that contains the operand, plus an offset value stored in a register, plus a base value stored in another register
- Example: MOV AX, [BX+SI+10H]

These addressing modes are used to access memory locations or data operands in microprocessors. Understanding them is important for programming and optimizing microprocessor applications.