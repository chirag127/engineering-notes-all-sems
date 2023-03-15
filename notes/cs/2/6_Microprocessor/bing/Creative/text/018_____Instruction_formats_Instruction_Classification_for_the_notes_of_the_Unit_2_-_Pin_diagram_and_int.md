### Instruction formats and classification

- An instruction is a binary pattern that specifies a specific operation to be performed by the microprocessor.
- The instruction format of 8085 microprocessor consists of one, two or three bytes, depending on the type of instruction.
- The first byte is always the opcode, which specifies the operation to be performed and the operands involved.
- The second byte, if present, is usually data, which is either an immediate value or a memory address.
- The third byte, if present, is either the high-order byte of a 16-bit data or a 16-bit memory address.
- The instruction set of 8085 microprocessor is classified into the following five groups according to the functions they perform:

  - Data transfer instructions: These instructions are used to transfer data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. Examples are ADD, SUB, INR, DCR, etc.
  - Logical instructions: These instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branching instructions: These instructions are used to alter the sequence of execution of the program based on certain conditions. Examples are JMP, JNZ, JC, CALL, RET, etc.
  - Machine control instructions: These instructions are used to control the operation of the microprocessor such as enabling or disabling interrupts, halting the processor, etc. Examples are EI, DI, HLT, NOP, etc.