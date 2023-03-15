# Memory Addressing for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

## Memory Addressing Modes of 8086

- The 8086 microprocessor provides 20-bit memory addressing that allows up to 1 Mbyte main memory.
- Each memory location can store one byte of data, and the 8086 can transfer 16-bit data, so it can access memory locations in byte or word mode.
- The 8086 has seven addressing modes that specify how to calculate the effective address of an operand.
- The addressing modes are:
  - Register addressing mode: The operand is stored in a register.
  - Immediate addressing mode: The operand is a constant value that is part of the instruction.
  - Direct addressing mode: The operand is stored in a memory location whose address is given in the instruction.
  - Register indirect addressing mode: The operand is stored in a memory location whose address is stored in a register.
  - Indexed addressing mode: The operand is stored in a memory location whose address is the sum of a base register and an index register.
  - Based addressing mode: The operand is stored in a memory location whose address is the sum of a base register and a displacement value.
  - Based indexed addressing mode: The operand is stored in a memory location whose address is the sum of a base register, an index register, and a displacement value.

## Memory Segmentation in 8086

- The 8086 uses a technique called memory segmentation to divide the 1 Mbyte memory into four segments of 64 Kbytes each.
- The four segments are: code segment, data segment, stack segment, and extra segment.
- The code segment contains the instructions of the program, the data segment contains the data variables of the program, the stack segment contains the stack data structure for subroutine calls and returns, and the extra segment is used for additional data storage.
- The 8086 has four segment registers that store the upper 16 bits of the starting addresses of the four segments: CS (code segment), DS (data segment), SS (stack segment), and ES (extra segment).
- The lower 16 bits of the effective address are stored in an offset register, such as IP (instruction pointer), SI (source index), DI (destination index), BP (base pointer), or SP (stack pointer).
- The 20-bit physical address is calculated by adding the segment register value (shifted left by 4 bits) and the offset register value.
- For example, if CS = 1000H and IP = 2000H, then the physical address of the next instruction is 1000H * 10H + 2000H = 12000H.