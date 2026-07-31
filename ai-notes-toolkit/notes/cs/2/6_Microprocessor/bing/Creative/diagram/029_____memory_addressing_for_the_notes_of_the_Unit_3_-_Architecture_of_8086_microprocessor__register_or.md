Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on memory addressing for the unit 3 of microprocessor KCS:

### Memory Addressing for the Unit 3 - Architecture of 8086 Microprocessor

- The 8086 microprocessor provides 20-bit memory addressing that allows up to 1 Mbyte main memory.
- The memory is byte-oriented, meaning each memory location can store only one byte of data.
- The 8086 is a 16-bit microprocessor, meaning it can transfer 16-bit data. So in addition to byte, word (16-bit) has to be stored in the memory.
- The memory is divided into four segments: code, data, stack and extra.
- The four segment registers (CS, DS, SS and ES) contain the upper 16 bits of the starting addresses of the four memory segments.
- The lower 16 bits of the memory address are provided by an offset register or an immediate value.
- The effective address of a memory location is calculated by adding the segment address (multiplied by 16) and the offset address.
- The 8086 has seven addressing modes: register, immediate, direct, register indirect, based, indexed and based indexed.
- The register addressing mode involves the use of registers to hold the operands.
- The immediate addressing mode involves the use of an immediate value as an operand.
- The direct addressing mode involves the use of a 16-bit offset address as an operand.
- The register indirect addressing mode involves the use of a register that contains the offset address of an operand.
- The based addressing mode involves the use of a base register (BX or BP) and an offset value to calculate the effective address of an operand.
- The indexed addressing mode involves the use of an index register (SI or DI) and an offset value to calculate the effective address of an operand.
- The based indexed addressing mode involves the use of a base register, an index register and an offset value to calculate the effective address of an operand.