### Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives. in the subject of Microprocessor KCS

- Addressing modes are the ways of specifying data to be operated by an instruction in a microprocessor.
- The 8085 microprocessor has five addressing modes: immediate, register, register indirect, direct, and implied.
- Immediate addressing mode: the operand is given in the instruction itself. For example, MVI A, 07H means load the accumulator with the value 07H .
- Register addressing mode: the operand is stored in one of the registers. For example, MOV B, C means copy the value of register C to register B .
- Register indirect addressing mode: the operand is stored in a memory location whose address is given by a register pair. For example, MOV A, M means copy the value of the memory location pointed by the register pair HL to the accumulator .
- Direct addressing mode: the operand is stored in a memory location whose address is given in the instruction. For example, LDA 2000H means load the accumulator with the value of the memory location 2000H .
- Implied addressing mode: the operand is implied by the instruction. For example, CMA means complement the accumulator .
- Instruction formats: the 8085 microprocessor has three types of instruction formats: one-byte, two-byte, and three-byte instructions. The first byte is always the opcode, which specifies the operation to be performed. The second and third bytes are optional and may contain operands or addresses.
- Instruction classification: the 8085 microprocessor has six types of instructions: data transfer, arithmetic operations, logical operations, branching operations, machine control, and assembler directives.
- Data transfer instructions: these instructions are used to move data between registers, memory, and I/O devices. For example, MOV, MVI, LDA, STA, IN, OUT, etc.
- Arithmetic operations: these instructions are used to perform arithmetic operations on data. For example, ADD, SUB, INR, DCR, DAD, etc.
- Logical operations: these instructions are used to perform logical operations on data. For example, AND, OR, XOR, CMA, RLC, RRC, etc.
- Branching operations: these instructions are used to change the sequence of execution of instructions based on certain conditions. For example, JMP, JZ, JNZ, JC, JNC, CALL, RET, etc.
- Machine control instructions: these instructions are used to control the operation of the microprocessor. For example, HLT, NOP, EI, DI, etc.
- Assembler directives: these are not instructions but commands to the assembler to perform certain tasks during the assembly process. For example, ORG, EQU, DB, DW, END, etc.