# Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Instructions

- An instruction is a binary pattern that tells the microprocessor to perform a specific operation on some data.
- An instruction consists of two parts: an **opcode** and an **operand**.
- The opcode specifies the type of operation to be performed, such as add, subtract, move, jump, etc.
- The operand specifies the data or the location of the data on which the operation is to be performed.
- An operand can be a register, a memory address, an immediate value, or a label.
- An instruction can have zero, one, or two operands depending on the opcode.
- For example, `MOV A, B` is an instruction that moves the contents of register B to register A. The opcode is `MOV` and the operands are `A` and `B`.
- An instruction can be written in binary, hexadecimal, or mnemonic form.
- Binary form is the actual bit pattern that the microprocessor understands and executes.
- Hexadecimal form is a convenient way of representing binary numbers using 16 symbols (0-9 and A-F).
- Mnemonic form is a symbolic representation of the instruction using abbreviations and names that are easy to remember and understand by humans.
- For example, the binary form of `MOV A, B` is `01111000`, the hexadecimal form is `78`, and the mnemonic form is `MOV A, B`.
- An assembly language is a low-level programming language that uses mnemonics to represent instructions and operands.
- An assembly language program consists of a sequence of assembly language statements, each of which corresponds to one machine instruction.
- An assembly language statement consists of four fields: a **label**, an **instruction**, an **operand**, and a **comment**.
- A label is an optional field that gives a name to a memory location or a program segment. It is followed by a colon (:).
- An instruction is a mandatory field that specifies the opcode of the machine instruction.
- An operand is an optional field that specifies the operand(s) of the machine instruction.
- A comment is an optional field that starts with a semicolon (;) and provides additional information or explanation about the statement.
- For example, `LOOP: MOV A, B ; Move B to A` is an assembly language statement that has a label `LOOP`, an instruction `MOV`, an operand `A, B`, and a comment `Move B to A`.
- An assembler is a program that converts an assembly language program into a machine language program.
- An assembler performs two tasks: **translation** and **linking**.
- Translation is the process of converting each assembly language statement into a corresponding machine instruction.
- Linking is the process of resolving the addresses of labels and external references and combining the translated code segments into a single executable file.

## Data Transfer

- Data transfer instructions are used to move data between registers, memory, and input/output devices.
- The general format of a data transfer instruction is `MOV destination, source`, where destination and source are operands that specify the location of the data to be moved.
- The destination operand can be a register or a memory address, but not an immediate value or a label.
- The source operand can be a register, a memory address, an immediate value, or a label, but not a segment register.
- The data transfer instructions do not affect any flags in the flag register.
- Some examples of data transfer instructions are:

  - `MOV A, B` : Move the contents of register B to register A.
  - `MOV A, M` : Move the contents of the memory location pointed by the HL register pair to register A.
  - `MOV M, A` : Move the contents of register A to the memory location pointed by the HL register pair.
  - `MOV A, 55H` : Move the immediate value 55H to register A.
  - `MOV A, DATA` : Move the contents of the memory location labeled as DATA to register A.
  - `MOV B, C` : Move the contents of register C to register B.
  - `MOV B, 32H` : Move the immediate value 32H to register B.
  - `MOV B, DATA` : Move the contents of the memory location labeled as DATA to register B.
  - `MOV C, A` : Move the contents of register A to register C.
  - `MOV C, M` : Move the contents of the memory location pointed by the HL register pair to register C.
  - `MOV