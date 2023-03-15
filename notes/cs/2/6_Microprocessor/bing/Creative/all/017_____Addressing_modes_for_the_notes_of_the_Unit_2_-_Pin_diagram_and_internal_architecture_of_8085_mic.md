# Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Addressing modes

- The way of specifying data to be operated by an instruction is called **addressing mode** .
- The 8085 microprocessor uses five addressing modes :
  - **Immediate addressing mode**: The instruction includes the operand along with the operation. For example: `MVI A, 07H` means load the value 07H into the accumulator .
  - **Register addressing mode**: The instruction mentions a register which stores the data. For example: `MOV A, B` means copy the contents of register B into the accumulator .
  - **Register indirect addressing mode**: The instruction mentions a register pair which holds the address of the memory location where the data is stored. For example: `MOV A, M` means copy the contents of the memory location pointed by the register pair HL into the accumulator .
  - **Direct addressing mode**: The instruction specifies the address of the memory location where the data is stored. For example: `LDA 2000H` means load the contents of the memory location 2000H into the accumulator .
  - **Implicit addressing mode**: The instruction does not specify any operand. The data is implied by the operation. For example: `CMA` means complement the accumulator .