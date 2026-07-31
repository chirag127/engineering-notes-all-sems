### Instruction formats and classification

An instruction is a binary pattern that specifies a certain operation to be performed by the microprocessor. An instruction consists of two parts: an **opcode** and an **operand**. The opcode is the part that specifies the operation, such as add, subtract, move, etc. The operand is the part that specifies the data or the address of the data on which the operation is to be performed.

The 8085 microprocessor has a total of 246 instructions, which can be classified into the following five types:

- Data transfer instructions
- Arithmetic instructions
- Logical instructions
- Branching instructions
- Control instructions

Each type of instruction has a different format, depending on the number of bytes, the addressing mode, and the data involved. The 8085 instruction set is classified into the following three groups according to word size:

- One-word or 1-byte instructions
- Two-word or 2-byte instructions
- Three-word or 3-byte instructions

The first byte is always the opcode; in two-byte instructions the second byte is usually data; in three-byte instructions the last two bytes present address or 16-bit data.

The following table shows the general format of the 8085 instructions:

| Instruction type | Format | Example |
|------------------|--------|---------|
| One-byte | Opcode | MOV A, B |
| Two-byte | Opcode, Data | MVI A, 05H |
| Three-byte | Opcode, Address | LDA 2000H |

The following table shows the classification of the 8085 instructions based on the functions they perform:

| Instruction type | Description | No. of opcodes | No. of instruction types | Example |
|------------------|-------------|----------------|--------------------------|---------|
| Data transfer instructions | These instructions are used to transfer data between registers, memory locations, I/O devices, etc. | 83 | 13 | MOV, MVI, LDA, STA, etc. |
| Arithmetic instructions | These instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. | 62 | 14 | ADD, SUB, INR, DCR, etc. |
| Logical instructions | These instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. | 23 | 9 | ANA, ORA, XRA, CMA, RLC, etc. |
| Branching instructions | These instructions are used to change the sequence of execution of the program based on certain conditions, such as jump, call, return, etc. | 50 | 17 | JMP, JNZ, CALL, RET, etc. |
| Control instructions | These instructions are used to control the operation of the microprocessor, such as halt, interrupt, enable, disable, etc. | 28 | 11 | HLT, EI, DI, RIM, SIM, etc. |

: Instruction Format of 8085 | Opcode Format and Data Format - EEEGUIDE.COM

: Instruction Format - Programming of 8085 Processor - BrainKart

: Instruction Set Classification of 8085 Microprocessor - tutorialspoint.com