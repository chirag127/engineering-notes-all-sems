# Addressing Modes

- Addressing modes are the different ways of specifying the location of an operand in an instruction .
- The operand can be a data value, a memory address, or a register.
- The choice of addressing mode affects the instruction format, the instruction size, the instruction execution time, and the memory access time.
- Different types of addressing modes are:

  - **Implied / Implicit Addressing Mode**: The operand is specified in the instruction itself or implied by the instruction opcode  . For example, `CLC` (clear carry flag) instruction does not need any operand.
  - **Immediate Addressing Mode**: The operand is a constant value that is given in the instruction itself   . For example, `MOV AX, 10` (move 10 to AX register) instruction has an immediate operand of 10.
  - **Direct Addressing Mode**: The operand is a memory address that is given in the instruction itself   . For example, `MOV AX, [1000]` (move the content of memory location 1000 to AX register) instruction has a direct operand of 1000.
  - **Register Addressing Mode**: The operand is a register that is specified in the instruction itself or implied by the instruction opcode   . For example, `MOV AX, BX` (move the content of BX register to AX register) instruction has two register operands of AX and BX.
  - **Register Indirect Addressing Mode**: The operand is a memory address that is stored in a register   . For example, `MOV AX, [BX]` (move the content of memory location pointed by BX register to AX register) instruction has a register indirect operand of BX.
  - **Displacement Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to a base address   . For example, `MOV AX, [BX+10]` (move the content of memory location pointed by BX register plus 10 to AX register) instruction has a displacement operand of BX+10.
  - **Relative Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to the current program counter  . For example, `JMP 20` (jump to the instruction 20 bytes ahead of the current instruction) instruction has a relative operand of 20.
  - **Indexed Addressing Mode**: The operand is a memory address that is calculated by adding an index value to a base address  . For example, `MOV AX, [1000+SI]` (move the content of memory location 1000 plus the content of SI register to AX register) instruction has an indexed operand of 1000+SI.
  - **Base Register Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to a base address that is stored in a register  . For example, `MOV AX, [BP+10]` (move the content of memory location pointed by BP register plus 10 to AX register) instruction has a base register operand of BP+10.
  - **Stack Addressing Mode**: The operand is a memory address that is at the top of the stack  . For example, `POP AX` (pop the top of the stack to AX register) instruction has a stack operand of the top of the stack.