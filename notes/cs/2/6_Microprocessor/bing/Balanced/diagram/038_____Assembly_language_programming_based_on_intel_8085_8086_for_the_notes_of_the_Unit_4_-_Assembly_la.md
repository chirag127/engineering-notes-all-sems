# Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that a microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that can address 64 KB of memory and has 74 instructions  .
- 8086 is a 16-bit microprocessor that can address 1 MB of memory and has 133 instructions .
- Assembly language programming involves writing the source code in a text editor, assembling it into an object file, and linking it to create an executable file .
- An assembler is a program that converts the source code into machine code and generates an object file .
- A linker is a program that combines one or more object files and resolves the external references to create an executable file .
- A debugger is a program that allows the programmer to test and correct the errors in the executable file .
- A simulator is a program that mimics the behavior of a microprocessor and allows the programmer to run and debug the executable file without the actual hardware .

## Instructions

- An instruction is a command that tells the microprocessor what operation to perform  .
- An instruction consists of two parts: an opcode and an operand  .
- An opcode is a mnemonic that specifies the type of operation, such as MOV, ADD, JMP, etc  .
- An operand is a data value or an address that is involved in the operation, such as a register, a memory location, an immediate value, etc  .
- An instruction can have zero, one, or two operands, depending on the opcode  .
- An instruction can be classified into three types: data transfer, arithmetic, and logic  .

## Data Transfer

- Data transfer instructions are used to move data between registers, memory, and input/output devices  .
- The most common data transfer instruction is MOV, which copies the data from the source operand to the destination operand  .
- The syntax of MOV is: MOV destination, source  .
- The destination and source operands can be registers, memory locations, or immediate values, but both must be of the same size (8-bit or 16-bit)  .
- Some examples of MOV are:

  - MOV A, B: copies the contents of register B to register A .
  - MOV AX, 1234H: copies the hexadecimal value 1234H to register AX.
  - MOV M, A: copies the contents of register A to the memory location pointed by the register pair HL .
  - MOV [1000H], BX: copies the contents of register BX to the memory location 1000H.

- Other data transfer instructions include:

  - MVI: moves an immediate value to a register or a memory location .
  - LXI: loads a 16-bit immediate value to a register pair .
  - LDA: loads the accumulator with the data from a 16-bit memory address .
  - STA: stores the accumulator to a 16-bit memory address .
  - LDAX: loads the accumulator with the data from the memory location pointed by a register pair .
  - STAX: stores the accumulator to the memory location pointed by a register pair [^3