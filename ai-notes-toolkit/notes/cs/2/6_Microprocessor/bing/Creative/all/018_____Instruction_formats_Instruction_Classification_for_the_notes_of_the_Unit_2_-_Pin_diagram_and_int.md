# Instruction formats Instruction Classification

## Instruction formats

- An instruction is a command to the microprocessor to perform a given task on a specified data.
- Each instruction has two parts: one is the task to be performed, called the **operation code (opcode)**, and the second is the data to be operated on, called the **operand**.
- The 8085 microprocessor has a set of 246 instructions (74 types) that can be classified into three groups according to word size :
  - **One-word or 1-byte instructions**: These instructions have only one byte, which is the opcode. For example, `MOV A, B` whose opcode is `78H`.
  - **Two-word or 2-byte instructions**: These instructions have two bytes, the first one is the opcode and the second one is usually data. For example, `MVI A, 32H` whose opcode is `3EH` and data is `32H`.
  - **Three-word or 3-byte instructions**: These instructions have three bytes, the first one is the opcode and the last two bytes present address or 16-bit data. For example, `LXI H, 1234H` whose opcode is `21H` and data is `1234H`.

## Instruction classification

- Based on the function of the instruction, the instructions are classified into the following five types :
  - **Data transfer instructions**: These instructions are used to transfer data between registers, memory and I/O devices. For example, `MOV`, `MVI`, `LDA`, `STA`, `IN`, `OUT`, etc.
  - **Arithmetic instructions**: These instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. For example, `ADD`, `ADC`, `SUB`, `SBB`, `INR`, `DCR`, etc.
  - **Logical and bit manipulation instructions**: These instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. For example, `ANA`, `ORA`, `XRA`, `CMA`, `RAL`, `RAR`, etc.
  - **Branch instructions**: These instructions are used to change the sequence of execution of the program based on certain conditions. For example, `JMP`, `JNZ`, `JC`, `CALL`, `RET`, etc.
  - **Machine control instructions**: These instructions are used to control the operation of the microprocessor such as enabling or disabling interrupts, halting the processor, etc. For example, `EI`, `DI`, `HLT`, `NOP`, etc.