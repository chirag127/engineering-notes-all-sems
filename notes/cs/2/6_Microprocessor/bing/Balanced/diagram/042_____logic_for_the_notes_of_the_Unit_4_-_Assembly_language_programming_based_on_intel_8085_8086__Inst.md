# Logic for the notes of the Unit 4 - Assembly language programming based on intel 8085/8086

## Introduction

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a given processor. For example, assembly language of 8085 is different than that of Motorola 6800 microprocessors.
- Assembly language programming requires an assembler, a software tool that converts assembly code to machine code and stores it in the memory.
- Assembly language programming is useful for writing time-critical and hardware-specific routines that cannot be easily done in high-level languages.

## Instructions

- An instruction is a command that tells the processor what to do.
- An instruction consists of two parts: an opcode and an operand.
- An opcode is a mnemonic that specifies the operation to be performed, such as ADD, MOV, JMP, etc.
- An operand is the data or the address of the data on which the operation is performed. An operand can be a register, a memory location, an immediate value, or a label.
- An instruction can have zero, one, or two operands, depending on the opcode.
- An instruction can be classified into four types: data transfer, arithmetic, logic, and branch.

## Data Transfer Instructions

- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- Data transfer instructions do not affect the flags, except for the HLT instruction, which sets the INTR flag to enable interrupts.
- Some examples of data transfer instructions are:

| Mnemonic | Description |
| --- | --- |
| MOV Rd, Rs | Move the contents of register Rs to register Rd |
| MVI R, data | Move the immediate data to register R |
| LDA addr | Load the accumulator with the contents of memory location addr |
| STA addr | Store the contents of the accumulator to memory location addr |
| IN port | Input data from the I/O port to the accumulator |
| OUT port | Output data from the accumulator to the I/O port |
| HLT | Halt the processor and wait for an interrupt |

## Arithmetic Instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, increment, decrement, etc.
- Arithmetic instructions affect the flags, such as the carry flag (CY), the auxiliary carry flag (AC), the zero flag (Z), the sign flag (S), and the parity flag (P).
- Some examples of arithmetic instructions are:

| Mnemonic | Description |
| --- | --- |
| ADD R | Add the contents of register R to the accumulator |
| ADI data | Add the immediate data to the accumulator |
| SUB R | Subtract the contents of register R from the accumulator |
| SUI data | Subtract the immediate data from the accumulator |
| INR R | Increment the contents of register R by 1 |
| DCR R | Decrement the contents of register R by 1 |
| DAD Rp | Add the contents of register pair Rp to the HL register pair |

## Logic Instructions

- Logic instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, etc.
- Logic instructions affect the flags, such as the zero flag (Z), the sign flag (S), and the parity flag (P). The carry flag (CY) and the auxiliary carry flag (AC) are always cleared by logic instructions.
- Some examples of logic instructions are:

| Mnemonic | Description |
| --- | --- |
| ANA R | AND the contents of register R with the accumulator |
| ANI data | AND the immediate data with the accumulator |
| ORA R | OR the contents of register R with the accumulator |
| ORI data | OR the immediate data with the accumulator |
| XRA R | XOR the contents of register R with the accumulator |
| XRI data | XOR the immediate data with the accumulator |
| CMA | Complement the accumulator |
| CMC | Complement the carry flag |

## Branch Instructions

- Branch instructions are used to alter the sequence of execution of instructions, based on certain conditions or unconditionally.
- Branch instructions affect the program counter (PC), which holds the address of the next instruction to be executed.
- Branch instructions can be classified into three types: unconditional jump, conditional jump, and call and return.
- Some examples of branch instructions are:

| Mnemonic | Description |
| --- | --- |
| JMP addr | Jump unconditionally to the memory location addr |
| JZ addr | Jump to the memory location addr if the zero flag (Z) is set |
|