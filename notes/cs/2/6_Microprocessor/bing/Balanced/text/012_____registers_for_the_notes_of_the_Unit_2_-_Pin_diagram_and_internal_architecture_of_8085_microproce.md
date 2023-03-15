### Registers of 8085 microprocessor

- A 8085 microprocessor is a second generation 8-bit microprocessor that is widely used for learning and programming microprocessors.
- It has eight addressable 8-bit registers: A, B, C, D, E, H, L, F, and two 16-bit registers PC and SP.
- These registers can be classified as:

  - General Purpose Registers (GPRs): These are B, C, D, E, H, and L. They can store 8-bit data and can be used for various operations. They are less important than the accumulator.
  - Accumulator: This is the most important register, also known as A. It is used to store the result of arithmetic and logical operations. It can also perform I/O operations.
  - Flag Register: This is also known as F. It is used to store the status of the microprocessor after an operation. It has five flags: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P), and Carry (CY).
  - Program Counter (PC): This is a 16-bit register that stores the address of the next instruction to be executed. It is incremented automatically after each instruction.
  - Stack Pointer (SP): This is a 16-bit register that stores the address of the top of the stack. The stack is a section of memory used to store data temporarily.
  - Temporary Registers: These are not directly accessible by the programmer. They are used by the microprocessor internally for various purposes. They are:

    - Temporary Data Register (TDR): This is an 8-bit register that holds the data during data transfer between the microprocessor and the memory or I/O devices.
    - W and Z Registers: These are two 8-bit registers that are used to form a 16-bit address during indirect addressing mode.
    - Serial Control Register (SC) and Serial Shift Register (SS): These are two 8-bit registers that are used to control and monitor the serial communication.

- The flow of an instruction cycle in 8085 architecture is as follows:

  - Fetch: The microprocessor fetches the instruction from the memory pointed by the PC and stores it in the TDR. The PC is incremented by one.
  - Decode: The microprocessor decodes the instruction in the TDR and identifies the operation code and the operands.
  - Execute: The microprocessor executes the instruction according to the operation code and the operands. The result is stored in the accumulator or the memory, and the flags are updated accordingly.
  - Interrupt: The microprocessor checks for any interrupt request from the external devices. If there is any, it saves the current state of the microprocessor and jumps to the interrupt service routine. Otherwise, it continues with the next instruction.