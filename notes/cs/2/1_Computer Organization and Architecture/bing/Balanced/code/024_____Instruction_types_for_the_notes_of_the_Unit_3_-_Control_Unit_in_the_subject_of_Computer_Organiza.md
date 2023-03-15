### Instruction types for the notes of the Unit 3 - Control Unit in the subject of Computer Organization and Architecture

- An instruction is a binary code that controls how a computer performs micro-operations in a series.
- An instruction consists of an operation code (opcode) and one or more operands.
- The opcode specifies the type of operation to be performed, such as arithmetic, logic, data transfer, control, etc.
- The operands specify the location of the data to be used or the result to be stored, such as registers, memory addresses, constants, etc.
- The instruction set architecture (ISA) defines the format and meaning of the instructions supported by a processor.
- The instruction set architecture can be classified into three categories based on the number of operands in an instruction:
  - Zero-address instructions: These instructions do not have any operands in the instruction. They use a stack to store and access the data. For example, PUSH, POP, ADD, etc.
  - One-address instructions: These instructions have one operand in the instruction, which is usually a memory address. The other operand is implicitly the accumulator, a special register that holds one of the operands or the result. For example, ADD M, SUB M, LOAD M, etc.
  - Two-address instructions: These instructions have two operands in the instruction, which are usually registers or memory addresses. The result is stored in one of the operands, which is overwritten. For example, ADD R1, R2, MOV R1, M, etc.
  - Three-address instructions: These instructions have three operands in the instruction, which are usually registers or memory addresses. The result is stored in a separate operand, which is not overwritten. For example, ADD R1, R2, R3, MOV R1, M1, etc.
- The instruction format also depends on the addressing mode, which specifies how the operands are accessed or located.
- The addressing mode can be classified into six types:
  - Immediate addressing: The operand is a constant value that is part of the instruction. For example, ADD #5, R1.
  - Register addressing: The operand is a register that holds the data. For example, ADD R1, R2.
  - Register indirect addressing: The operand is a register that holds the memory address of the data. For example, ADD (R1), R2.
  - Direct addressing: The operand is a memory address that holds the data. For example, ADD M, R1.
  - Indirect addressing: The operand is a memory address that holds another memory address of the data. For example, ADD (M), R1.
  - Indexed addressing: The operand is a memory address that is added to an index register to form the effective address of the data. For example, ADD M(X), R1.