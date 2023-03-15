### Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Addressing modes are the ways of specifying data to be operated by an instruction.
- The 8085 microprocessor supports five addressing modes: immediate, register, register indirect, direct, and implied.
- Immediate addressing mode: the operand is given in the instruction itself. For example, MVI A, 07H means load the accumulator with the value 07H .
- Register addressing mode: the operand is stored in one of the registers. For example, MOV A, B means copy the contents of register B to the accumulator .
- Register indirect addressing mode: the operand is stored in a memory location whose address is given by a register pair. For example, MOV A, M means copy the contents of the memory location pointed by the HL register pair to the accumulator .
- Direct addressing mode: the operand is stored in a memory location whose address is given in the instruction. For example, LDA 2000H means load the accumulator with the contents of the memory location 2000H .
- Implied addressing mode: the operand is implied by the instruction. For example, RLC means rotate the bits of the accumulator left in a circular manner .

: A Short Note on Addressing Modes in 8085 Microprocessor - Unacademy
: Addressing modes in 8085 microprocessor - GeeksforGeeks
: Addressing Modes in 8085 Microprocessor - Technobyte