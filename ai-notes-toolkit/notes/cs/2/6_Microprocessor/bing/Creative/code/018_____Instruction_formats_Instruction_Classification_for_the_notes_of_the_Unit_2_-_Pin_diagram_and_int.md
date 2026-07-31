### Instruction formats and classification

The instruction set of 8085 microprocessor consists of various types of instructions that can perform different operations on data, memory, registers, and I/O devices. The instructions can be classified based on the following criteria:

- Word size: The number of bytes required to store the instruction in memory.
- Addressing mode: The way of specifying the operands for the instruction.
- Function: The type of operation performed by the instruction.

#### Word size

The 8085 instruction set is classified into the following three groups according to word size:

- One-word or 1-byte instructions: These instructions have only one byte, which is the opcode. For example, `MOV A, B` whose opcode is `78H` is a one-byte instruction.
- Two-word or 2-byte instructions: These instructions have two bytes, the first one is the opcode and the second one is usually data. For example, `MVI A, 32H` whose opcode is `3EH` and data is `32H` is a two-byte instruction.
- Three-word or 3-byte instructions: These instructions have three bytes, the first one is the opcode and the last two bytes present address or 16-bit data. For example, `LXI H, 1234H` whose opcode is `21H` and data is `1234H` is a three-byte instruction.

#### Addressing mode

The addressing mode of an instruction specifies how the operands are accessed for the instruction. The 8085 instruction set supports the following five addressing modes:

- Immediate addressing mode: The operand is specified as a constant value in the instruction itself. For example, `MVI A, 32H` uses immediate addressing mode to load the value `32H` into the accumulator.
- Register addressing mode: The operand is specified as one of the registers in the 8085 microprocessor. For example, `MOV A, B` uses register addressing mode to copy the contents of register B into the accumulator.
- Direct addressing mode: The operand is specified as a 16-bit address in the instruction itself. The operand is located in the memory location specified by the address. For example, `LDA 2000H` uses direct addressing mode to load the accumulator with the contents of memory location `2000H`.
- Register indirect addressing mode: The operand is specified as a register pair in the instruction. The operand is located in the memory location whose address is stored in the register pair. For example, `MOV A, M` uses register indirect addressing mode to load the accumulator with the contents of memory location whose address is in the HL register pair.
- Implicit addressing mode: The operand is implied by the instruction itself. For example, `CMA` uses implicit addressing mode to complement the accumulator.

#### Function

The function of an instruction specifies the type of operation performed by the instruction. The 8085 instruction set can be classified into the following six functional groups:

- Data transfer instructions: These instructions are used to transfer data between registers, memory, and I/O devices. For example, `MOV`, `MVI`, `LDA`, `STA`, `IN`, `OUT`, etc.
- Arithmetic instructions: These instructions are used to perform arithmetic operations on data in registers and memory. For example, `ADD`, `SUB`, `INR`, `DCR`, `DAD`, `SUI`, etc.
- Logical instructions: These instructions are used to perform logical operations on data in registers and memory. For example, `AND`, `OR`, `XOR`, `CMA`, `RLC`, `RAL`, etc.
- Branching instructions: These instructions are used to alter the sequence of execution of instructions based on certain conditions. For example, `JMP`, `JNZ`, `JC`, `CALL`, `RET`, etc.
- Machine control instructions: These instructions are used to control the operation of the microprocessor and its peripherals. For example, `HLT`, `NOP`, `EI`, `DI`, etc.
- Assembler directives: These are not instructions but commands to the assembler to perform certain tasks during the assembly process. For example, `ORG`, `END`, `EQU`, `DB`, etc.