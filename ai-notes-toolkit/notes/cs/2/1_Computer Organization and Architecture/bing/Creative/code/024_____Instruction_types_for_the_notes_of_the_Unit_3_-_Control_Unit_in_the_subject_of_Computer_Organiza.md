### Instruction types for the notes of the Unit 3 - Control Unit in the subject of Computer Organization and Architecture

- An instruction is a binary code that controls how a computer performs micro-operations in a series.
- An instruction consists of an operation code (opcode) and one or more operands.
- The opcode specifies the type of operation to be performed, such as arithmetic, logic, data transfer, control, etc.
- The operands specify the location of the data to be used or the result to be stored, such as registers, memory addresses, constants, etc.
- The instruction set architecture (ISA) defines the format and meaning of the instructions supported by a processor.
- The instruction set architecture can be classified into three categories based on the number of operands in an instruction:
  - Zero-address instructions: These instructions do not have any operands in the instruction. They use a stack to store and access the data. The operands are implicitly specified by the top of the stack and the next location. For example, ADD pops two values from the stack, adds them, and pushes the result back to the stack.
  - One-address instructions: These instructions have one operand in the instruction, which is usually a memory address. The other operand is implicitly specified by a special register called the accumulator. The result of the operation is stored in the accumulator. For example, ADD X adds the value of memory location X to the accumulator and stores the result in the accumulator.
  - Two-address instructions: These instructions have two operands in the instruction, which are usually memory addresses or registers. The result of the operation is stored in one of the operands, which is overwritten. For example, ADD X, Y adds the value of memory location X to the value of memory location Y and stores the result in Y.
  - Three-address instructions: These instructions have three operands in the instruction, which are usually memory addresses or registers. The result of the operation is stored in a separate operand, which is not overwritten. For example, ADD X, Y, Z adds the value of memory location X to the value of memory location Y and stores the result in memory location Z.
- The instruction cycle is the sequence of steps that a processor follows to execute an instruction. It consists of four phases:
  - Fetch: The processor fetches the instruction from the memory and stores it in the instruction register (IR). The program counter (PC) is incremented to point to the next instruction.
  - Decode: The processor decodes the instruction in the IR and determines the opcode and the operands. It also checks for any interrupts or exceptions that may occur during the execution.
  - Execute: The processor executes the instruction by performing the specified operation on the operands. It may access the memory or the registers to read or write the data. It may also update the status flags or the PC based on the result of the operation.
  - Writeback: The processor writes the result of the execution to the memory or the register specified by the instruction. It may also update the PC if the instruction is a branch or a jump.