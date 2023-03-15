# Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a particular microprocessor, such as intel 8085 or 8086.
- An assembler is a program that converts assembly language to machine language, which is a binary code that the microprocessor can execute.
- Assembly language programming requires knowledge of the microprocessor architecture, instruction set, addressing modes, registers, flags, memory organization, and interfacing devices.

## Instructions

- An instruction is a command that tells the microprocessor what to do.
- An instruction consists of two parts: an opcode and an operand.
- An opcode is a mnemonic that specifies the operation to be performed, such as ADD, MOV, JMP, etc.
- An operand is the data or the address of the data on which the operation is performed. An operand can be a register, a memory location, an immediate value, or a label.
- An instruction can have zero, one, or two operands, depending on the opcode.
- An instruction can be classified into four types: data transfer, arithmetic, logic, and branch.

## Data transfer instructions

- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- The most common data transfer instruction is MOV, which copies the data from the source operand to the destination operand.
- The source and destination operands can be registers, memory locations, or immediate values, but both operands cannot be memory locations at the same time.
- The MOV instruction does not affect any flags in the flag register.
- Some examples of data transfer instructions are:

| Instruction | Description |
| --- | --- |
| MOV A, B | Copy the contents of register B to register A |
| MOV A, M | Copy the contents of the memory location pointed by HL pair to register A |
| MOV M, A | Copy the contents of register A to the memory location pointed by HL pair |
| MOV A, 55H | Copy the immediate value 55H to register A |
| MVI A, 55H | Same as MOV A, 55H |
| LXI H, 1234H | Load the immediate value 1234H to HL pair |
| LDA 2000H | Load the contents of the memory location 2000H to register A |
| STA 3000H | Store the contents of register A to the memory location 3000H |
| LHLD 4000H | Load the contents of the memory locations 4000H and 4001H to HL pair |
| SHLD 5000H | Store the contents of HL pair to the memory locations 5000H and 5001H |
| XCHG | Exchange the contents of HL pair and DE pair |

## Arithmetic instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, and division.
- The arithmetic instructions affect the flags in the flag register, such as the carry flag, the sign flag, the zero flag, the parity flag, and the auxiliary carry flag.
- The arithmetic instructions can operate on registers, memory locations, or immediate values, but the result is always stored in the accumulator (register A).
- Some examples of arithmetic instructions are:

| Instruction | Description |
| --- | --- |
| ADD B | Add the contents of register B to the contents of register A and store the result in register A |
| ADD M | Add the contents of the memory location pointed by HL pair to the contents of register A and store the result in register A |
| ADI 55H | Add the immediate value 55H to the contents of register A and store the result in register A |
| ADC B | Add the contents of register B and the carry flag to the contents of register A and store the result in register A |
| ADC M | Add the contents of the memory location pointed by HL pair and the carry flag to the contents of register A and store the result in register A |
| ACI 55H | Add the immediate value 55H and the carry flag to the contents of register A and store the result in register A |
| SUB B | Subtract the contents of register B from the contents of register A and store the result in register A |
| SUB M | Subtract the contents of the memory location pointed by HL pair from the contents of register A and store the result in register A |
| SUI 55H | Subtract the immediate value 55H from the contents of register A and store the result in register