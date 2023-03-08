### Instruction Format in 8086 Microprocessor

- The instructions in 8086 microprocessor are 1 to 6 bytes long depending on the addressing mode and the operands involved.
- The first byte of every instruction is called the **opcode** byte, which specifies the operation to be performed and the addressing mode to be used.
- The opcode byte consists of two parts: the **opcode** field and the **mode** field.
- The opcode field is 6 bits long and contains a unique binary code for each instruction.
- The mode field is 2 bits long and indicates whether the instruction is a **register** instruction, a **memory** instruction, or an **immediate** instruction.
- The mode field also determines the size and number of the following bytes in the instruction.
- The following bytes in the instruction may contain one or more of the following components:
  - **Register/memory operand**: This specifies a register or a memory location as an operand. It consists of three subfields: the **mod** field, the **reg** field, and the **r/m** field.
  - The mod field is 2 bits long and indicates whether the operand is a register or a memory location, and whether a displacement is present or not.
  - The reg field is 3 bits long and specifies a register as an operand or as a part of the memory address.
  - The r/m field is 3 bits long and specifies a register as an operand or as a part of the memory address.
  - **Displacement**: This is an 8-bit or a 16-bit value that is added to the contents of a register or a segment register to form a memory address.
  - **Immediate operand**: This is an 8-bit or a 16-bit constant value that is directly used as an operand.
- Depending on the combination of the mode field and the components, there are six general instruction formats in 8086 microprocessor:
  - **One byte instruction**: This is only one byte long and may have implied data and register. For example, `CLC` (clear carry flag) is a one byte instruction with opcode `F8`.
  - **Register to register**: This instruction is 2 bytes long. The first byte contains the opcode and the mode field, and the second byte contains the register/memory operand. The mod field is `11`, indicating that both operands are registers. For example, `MOV AX, BX` (move the contents of BX to AX) is a register to register instruction with opcode `8B` and register/memory operand `C3`.
  - **Register to/from memory with no displacement**: This format is also 2 bytes long and similar to the register to register format, except that the mod field is `00`, indicating that one of the operands is a memory location with no displacement. For example, `MOV AX, [BX]` (move the contents of the memory location pointed by BX to AX) is a register to/from memory instruction with no displacement, with opcode `8B` and register/memory operand `07`.
  - **Register to/from memory with displacement**: This format is 3 or 4 bytes long, depending on the size of the displacement. The first byte contains the opcode and the mode field, the second byte contains the register/memory operand, and the third byte (or the third and fourth bytes) contains the displacement. The mod field is `01` or `10`, indicating that one of the operands is a memory location with an 8-bit or a 16-bit displacement, respectively. For example, `MOV AX, [BX+4]` (move the contents of the memory location pointed by BX plus 4 to AX) is a register to/from memory instruction with an 8-bit displacement, with opcode `8B`, register/memory operand `47`, and displacement `04`.
  - **Immediate operand to register**: This format is 3 or 4 bytes long, depending on the size of the immediate operand. The first byte contains the opcode and the mode field, the second byte contains the register/memory operand, and the third byte (or the third and fourth bytes) contains the immediate operand. The mod field is `11`, indicating that the destination operand is a register, and the opcode field is `1011`, indicating that the source operand is an immediate

Some possible mnemonics and learning tricks for the topic are:

- To remember the six general instruction formats, you can use the acronym **RRRMDI**, which stands for Register to Register, Register to/from Memory with no Displacement, Register to/from Memory with Displacement, Immediate operand to Register, Immediate operand to Memory, and Immediate operand to Accumulator.
- To remember the meaning of the mod field values, you can use the following table:

| mod | Meaning |
| --- | ------- |
| 00  | Memory with no displacement |
| 01  | Memory with 8-bit displacement |
| 10  | Memory with 16-bit displacement |
| 11  | Register |

- To remember the meaning of the reg field values, you can use the following table:

| reg | Register |
| --- | -------- |
| 000 | AL/AX    |
| 001 | CL/CX    |
| 010 | DL/DX    |
| 011 | BL/BX    |
| 100 | AH/SP    |
| 101 | CH/BP    |
| 110 | DH/SI    |
| 111 | BH/DI    |

- To remember the meaning of the r/m field values, you can use the following table:

| r/m | Register | Memory |
| --- | -------- | ------ |
| 000 | AL/AX    | [BX+SI] |
| 001 | CL/CX    | [BX+DI] |
| 010 | DL/DX    | [BP+SI] |
| 011 | BL/BX    | [BP+DI] |
| 100 | AH/SP    | [SI] |
| 101 | CH/BP    | [DI] |
| 110 | DH/SI    | [BP] or [disp16] |
| 111 | BH/DI    | [BX] |

- To remember the opcode field values for the immediate operand instructions, you can use the following table:

| Opcode | Instruction |
| ------ | ----------- |
| 1011   | Immediate to register |
| 1100   | Immediate to memory |
| 0100   | Immediate to accumulator |