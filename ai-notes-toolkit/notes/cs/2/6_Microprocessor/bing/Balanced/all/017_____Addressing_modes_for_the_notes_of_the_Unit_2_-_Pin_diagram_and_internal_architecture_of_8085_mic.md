# Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Addressing modes

- The way of specifying data to be operated by an instruction is called addressing mode.
- The 8085 microprocessor uses five addressing modes: 
  - Immediate addressing mode
  - Register addressing mode
  - Register indirect addressing mode
  - Direct addressing mode
  - Implicit addressing mode

### Immediate addressing mode

- In this mode, the 8/16-bit data is specified in the instruction itself as one of its operand.
- For example: MVI A, 32H means load the accumulator with the data 32H.
- The advantage of this mode is that it is fast and simple.
- The disadvantage of this mode is that it can only operate on 8/16-bit data and it occupies more memory space.

### Register addressing mode

- In this mode, the data to be operated is available inside the register(s) specified in the instruction.
- For example: MOV B, C means copy the data from register C to register B.
- The advantage of this mode is that it is fast and does not require any memory access.
- The disadvantage of this mode is that it can only operate on the data stored in the registers.

### Register indirect addressing mode

- In this mode, the effective address of the data is stored in a register pair specified in the instruction.
- The data is then accessed from the memory location pointed by the register pair.
- For example: MOV A, M means copy the data from the memory location pointed by the register pair HL to the accumulator.
- The advantage of this mode is that it can access any memory location using a register pair.
- The disadvantage of this mode is that it requires an extra memory access and it can only use the register pairs BC, DE and HL.

### Direct addressing mode

- In this mode, the effective address of the data is specified in the instruction itself as a 16-bit operand.
- The data is then accessed from the memory location pointed by the 16-bit operand.
- For example: LDA 2000H means load the accumulator with the data from the memory location 2000H.
- The advantage of this mode is that it can access any memory location directly.
- The disadvantage of this mode is that it occupies more memory space and it requires an extra memory access.

### Implicit addressing mode

- In this mode, the data to be operated is implied by the instruction itself and is not specified explicitly.
- For example: CMA means complement the accumulator, i.e., change 0 to 1 and 1 to 0 in the accumulator.
- The advantage of this mode is that it is simple and does not require any operand.
- The disadvantage of this mode is that it can only perform some predefined operations.