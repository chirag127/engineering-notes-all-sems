# Instruction formats and classification

## Instruction formats

- An instruction is a binary pattern that specifies a certain operation to be performed by the microprocessor.
- An instruction consists of two parts: an **opcode** and an **operand**.
- The opcode is the part of the instruction that specifies the type of operation to be performed, such as add, subtract, move, etc.
- The operand is the part of the instruction that specifies the data or the address of the data on which the operation is to be performed.
- The operand can be a register, a memory location, an immediate data, or an I/O port.
- The 8085 microprocessor has three types of instruction formats: **one-byte**, **two-byte**, and **three-byte** instructions.
- The one-byte instructions have only the opcode and no operand. For example, `HLT` is a one-byte instruction that halts the microprocessor.
- The two-byte instructions have the opcode in the first byte and the operand in the second byte. For example, `MVI A, 05H` is a two-byte instruction that moves the immediate data `05H` to the accumulator register `A`.
- The three-byte instructions have the opcode in the first byte and the operand in the second and third bytes. For example, `LDA 2000H` is a three-byte instruction that loads the accumulator with the data from the memory location `2000H`.
- The following table shows the general formats of the three types of instructions:

| Instruction type | Format | Example |
| ---------------- | ------ | ------- |
| One-byte | OPCODE | HLT |
| Two-byte | OPCODE OPERAND | MVI A, 05H |
| Three-byte | OPCODE OPERAND OPERAND | LDA 2000H |

## Instruction classification

- The 8085 microprocessor has a set of 246 instructions, which are classified into five groups according to their functions: **data transfer**, **arithmetic**, **logical**, **branching**, and **machine control**.
- The data transfer instructions are used to move data between registers, memory, and I/O devices. For example, `MOV A, B` is a data transfer instruction that copies the contents of register `B` to register `A`.
- The arithmetic instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. on the data in the registers or memory. For example, `ADD B` is an arithmetic instruction that adds the contents of register `B` to the accumulator and stores the result in the accumulator.
- The logical instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. on the data in the registers or memory. For example, `ANA B` is a logical instruction that performs the bitwise AND operation between the contents of register `B` and the accumulator and stores the result in the accumulator.
- The branching instructions are used to alter the sequence of execution of the program based on certain conditions. For example, `JNZ 1000H` is a branching instruction that jumps to the memory location `1000H` if the zero flag is not set.
- The machine control instructions are used to control the operation of the microprocessor and the peripheral devices. For example, `EI` is a machine control instruction that enables the interrupt system of the microprocessor.
- The assembler directives are not instructions, but commands to the assembler that specify how to assemble the program. For example, `ORG 2000H` is an assembler directive that tells the assembler to start assembling the program from the memory location `2000H`.