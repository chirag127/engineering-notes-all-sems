### Memory Addressing for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

- Memory addressing is the process of specifying the location of data or instructions in the main memory of the microprocessor.
- The 8086 microprocessor has 20 address lines, which allows it to access up to 1 MB (2^20 bytes) of memory.
- The 8086 microprocessor can transfer 8-bit (byte) or 16-bit (word) data to or from the memory.
- The 8086 microprocessor uses a segmented memory model, which means that the memory is divided into four segments: code, data, stack, and extra.
- Each segment has a 64 KB (2^16 bytes) size and a 16-bit base address, which is stored in a segment register: CS (code segment), DS (data segment), SS (stack segment), and ES (extra segment).
- The 8086 microprocessor uses a 16-bit offset address to specify the location of data or instructions within a segment. The offset address is also called the effective address or the displacement.
- The 8086 microprocessor combines the base address and the offset address to form a 20-bit physical address, which is sent to the memory. The physical address is calculated as: Physical address = (Base address * 16) + Offset address
- The 8086 microprocessor has various addressing modes, which are the ways of specifying the offset address of an operand. The addressing modes are: register, immediate, direct, register indirect, based, indexed, based indexed, and relative.
- Register addressing mode: The operand is stored in a register. Example: MOV AX, BX
- Immediate addressing mode: The operand is a constant value, which is part of the instruction. Example: MOV AX, 1234H
- Direct addressing mode: The operand is stored in a memory location, whose offset address is given in the instruction. Example: MOV AX, [1000H]
- Register indirect addressing mode: The operand is stored in a memory location, whose offset address is stored in a register. Example: MOV AX, [BX]
- Based addressing mode: The operand is stored in a memory location, whose offset address is the sum of a base register and a displacement. Example: MOV AX, [BP+10H]
- Indexed addressing mode: The operand is stored in a memory location, whose offset address is the sum of an index register and a displacement. Example: MOV AX, [SI+20H]
- Based indexed addressing mode: The operand is stored in a memory location, whose offset address is the sum of a base register, an index register, and a displacement. Example: MOV AX, [BP+SI+30H]
- Relative addressing mode: The operand is a memory location, whose offset address is the sum of the current instruction pointer and a displacement. This mode is used for branching instructions. Example: JMP 40H