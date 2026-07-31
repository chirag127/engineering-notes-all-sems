# Registers for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Registers
- A register is a small storage unit that can hold data or instructions temporarily.
- The 8085 microprocessor has eight addressable 8-bit registers: A, B, C, D, E, H, L, F, and two 16-bit registers PC and SP .
- These registers can be classified as:
  - General Purpose Registers
  - Temporary Registers
  - Special Purpose Registers
  - Stack Pointer and Program Counter

### General Purpose Registers
- The 8085 has six general-purpose registers to store 8-bit data; these are identified as- B, C, D, E, H, and L .
- They are less important than the accumulator.
- They can be used individually or in pairs to store data, address or operands .
- The pairs are BC, DE and HL .
- The HL pair is often used to store the address of a memory location, and hence it is also called the Memory Address Register (MAR) .

### Temporary Registers
- The 8085 has two temporary registers that are not accessible to the programmer.
- They are:
  - Temporary Data Register: It is used to hold the data during arithmetic and logical operations.
  - W and Z Registers: They are used to store the 8-bit data during the execution of some instructions, such as CALL, RET, RST, etc.

### Special Purpose Registers
- The 8085 has two special purpose registers that are accessible to the programmer .
- They are:
  - Accumulator: It is an 8-bit register that is a part of the arithmetic and logic unit (ALU) .
  - It is used to store the result of any operation performed by the ALU .
  - It can also be used to store or transfer data .
  - It is also called the A register .
  - Flag Register: It is an 8-bit register that is used to indicate the status of the microprocessor after an operation .
  - It has five flags that are affected by the arithmetic and logical operations .
  - They are: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P) and Carry (CY) .
  - The other three bits of the flag register are not used .
  - The flag register is also called the F register .

### Stack Pointer and Program Counter
- The 8085 has two 16-bit registers that are used to store the address of a memory location .
- They are:
  - Stack Pointer: It is used to point to the top of the stack in the memory .
  - The stack is a section of memory that is used to store the return address and data during the execution of subroutines and interrupts .
  - The stack pointer is decremented by two when a data or address is pushed onto the stack, and incremented by two when a data or address is popped from the stack .
  - The stack pointer is also called the SP register .
  - Program Counter: It is used to point to the address of the next instruction to be executed by the microprocessor .
  - The program counter is incremented by one or more depending on the size of the instruction .
  - The program counter is also called the PC register .

## Pin diagram and internal architecture of 8085 microprocessor
- The 8085 microprocessor is a 40-pin integrated