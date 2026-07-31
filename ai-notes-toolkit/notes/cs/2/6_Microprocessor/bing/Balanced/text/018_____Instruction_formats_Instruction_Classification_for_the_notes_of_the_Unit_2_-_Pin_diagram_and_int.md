### Instruction formats and classification

- An instruction is a binary pattern that specifies a specific operation to be performed by the microprocessor.
- The instruction format of 8085 microprocessor consists of one, two or three bytes, depending on the type of instruction.
- The first byte is always the opcode, which specifies the operation code or the type of instruction.
- The second byte (if present) is usually the operand, which specifies the data or the address involved in the operation.
- The third byte (if present) is usually the higher-order byte of the 16-bit address or data.
- The instruction set of 8085 microprocessor is classified into the following five groups according to the function they perform:

  - Data transfer instructions: These instructions are used to transfer data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. Examples are ADD, SUB, INR, DCR, DAD, etc.
  - Logical instructions: These instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branching instructions: These instructions are used to change the sequence of execution of the program based on certain conditions. Examples are JMP, JNZ, JC, CALL, RET, etc.
  - Machine control instructions: These instructions are used to control the operation of the microprocessor such as halt, interrupt enable, interrupt disable, etc. Examples are HLT, EI, DI, NOP, etc.

- The instruction set of 8085 microprocessor is also classified into the following three groups according to the size they occupy in memory:

  - One-byte instructions: These instructions have only one byte, which is the opcode. Examples are CMA, DAA, EI, DI, etc.
  - Two-byte instructions: These instructions have two bytes, the first byte is the opcode and the second byte is the operand. Examples are MVI, IN, OUT, ADI, SUI, etc.
  - Three-byte instructions: These instructions have three bytes, the first byte is the opcode and the last two bytes are the operand. Examples are LDA, STA, LHLD, SHLD, LXI, etc.