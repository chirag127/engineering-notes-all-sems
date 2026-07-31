# Data Transfer for the Notes of the Unit 2 - Pin Diagram and Internal Architecture of 8085 Microprocessor, Registers, ALU, Control & Status, Interrupt and Machine Cycle. Instruction Sets. Addressing Modes. Instruction Formats Instruction Classification: Data Transfer, Arithmetic Operations, Logical Operations, Branching Operations, Machine Control and Assembler Directives.

## Data Transfer

- Data transfer is the process of moving data from one location to another in the microprocessor.
- Data transfer can be done in different ways, such as parallel, serial, or direct memory access (DMA).
- Data transfer instructions are the instructions that perform data transfer operations in the 8085 microprocessor.
- Data transfer instructions can be classified into the following types:

### MOV Instruction

- This instruction copies the contents of the source register or memory location into the destination register or memory location without any alteration.
- The syntax of this instruction is `MOV destination, source`.
- The destination and source can be any of the following: A, B, C, D, E, H, L, M.
- M stands for the memory location pointed by the HL register pair.
- The MOV instruction takes one byte of machine code and one machine cycle to execute.
- For example, `MOV A, B` copies the contents of the B register into the A register.

### MVI Instruction

- This instruction loads an 8-bit immediate data into the specified register or memory location.
- The syntax of this instruction is `MVI destination, data`.
- The destination can be any of the following: A, B, C, D, E, H, L, M.
- The data can be any 8-bit value from 00H to FFH.
- The MVI instruction takes two bytes of machine code and two machine cycles to execute.
- For example, `MVI A, 05H` loads the value 05H into the A register.

### LDA Instruction

- This instruction loads an 8-bit data from the specified 16-bit memory address into the accumulator (A) register.
- The syntax of this instruction is `LDA address`.
- The address can be any 16-bit value from 0000H to FFFFH.
- The LDA instruction takes three bytes of machine code and four machine cycles to execute.
- For example, `LDA 1234H` loads the data from the memory location 1234H into the A register.

### STA Instruction

- This instruction stores the contents of the accumulator (A) register into the specified 16-bit memory address.
- The syntax of this instruction is `STA address`.
- The address can be any 16-bit value from 0000H to FFFFH.
- The STA instruction takes three bytes of machine code and four machine cycles to execute.
- For example, `STA 5678H` stores the data from the A register into the memory location 5678H.

### LHLD Instruction

- This instruction loads a 16-bit data from the specified memory address and its next memory address into the HL register pair.
- The syntax of this instruction is `LHLD address`.
- The address can be any 16-bit value from 0000H to FFFFH.
- The LHLD instruction takes three bytes of machine code and five machine cycles to execute.
- For example, `LHLD 1234H` loads the data from the memory location 1234H into the L register and the data from the memory location 1235H into the H register.

### SHLD Instruction

- This instruction stores the contents of the HL register pair into the specified memory address and its next memory address.
- The syntax of this instruction is `SHLD address`.
- The address can be any 16-bit value from 0000H to FFFFH.
- The SHLD instruction takes three bytes of machine code and five machine cycles to execute.
- For example, `SHLD 5678H` stores the data from the L register into the memory location 5678H and the data from the H register into the memory location 5679H.

### LXI Instruction

- This instruction loads a 16-bit immediate data into the specified register pair.
- The syntax of this instruction is `LXI register pair, data`.
- The register pair can be any of the following: BC, DE, HL, SP.
- SP stands for the stack pointer register.
- The data can be any 16-bit value from 0000H to FFFFH.
- The LXI instruction takes three bytes of machine code and three machine cycles