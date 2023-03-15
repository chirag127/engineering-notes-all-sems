### Architecture of 8086 Microprocessor

- The 8086 is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines.
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  .
- The Bus Interface Unit (BIU) provides the interface of 8086 to external memory and I/O devices via the System Bus. It handles all the data transfer functions .
- The BIU consists of the following components :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code, data, stack, and extra. Each segment can be up to 64 KB in size.
  - Instruction pointer: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O device.
  - Prefetch queue: This is a 6-byte buffer that stores the prefetched instructions from the code segment. It helps to speed up the execution by providing the instructions to the EU in advance.
- The Execution Unit (EU) performs the arithmetic and logical operations on the data. It also controls the flow of the program execution .
- The EU consists of the following components :
  - General purpose registers: These are eight 16-bit registers that can be used for various purposes, such as data storage, address calculation, or operand manipulation. They can be accessed as 16-bit registers (AX, BX, CX, DX) or as 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL).
  - Pointer and index registers: These are four 16-bit registers that are used for addressing modes, such as base, index, or relative. They are: stack pointer (SP), base pointer (BP), source index (SI), and destination index (DI).
  - Arithmetic and logic unit (ALU): This is a circuit that performs the arithmetic and logical operations on the operands, such as addition, subtraction, multiplication, division, and, or, xor, etc.
  - Flag register: This is a 16-bit register that stores the status of the EU after an operation. It consists of nine flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
  - Control unit: This is a circuit that controls the operation of the EU. It consists of the following components:
    - Decode unit: This is a circuit that decodes the instructions from the prefetch queue and generates the control signals for the ALU and the registers.
    - Instruction queue: This is a 4-byte buffer that stores the decoded instructions from the decode unit. It helps to speed up the execution by providing the instructions to the ALU and the registers in advance.
    - Timing and control unit: This is a circuit that generates the timing and control signals for the EU and the BIU. It also handles the interrupts and the operating modes of the 8086.

- The 8086 has two operating modes: minimum mode and maximum mode.
  - Minimum mode: This is the mode when the 8086 operates as a single processor in a system. It uses the MN/MX pin as an output to enable the external bus drivers and control signals.
  - Maximum mode: This is the mode when the 8086 operates as a master processor in a multiprocessor system. It uses the MN/MX pin as an input to select the operating mode and uses the S2, S1, S0 pins as outputs to indicate the status of the current bus cycle.

- The 8086 has a rich instruction set that can be classified into the following types:
  - Data transfer instructions: These are the instructions that transfer data between registers, memory, and I/O devices, such as MOV, PUSH, POP, IN, OUT, etc.
  - Arithmetic instructions: These are the instructions that perform arithmetic operations on the operands, such as ADD, SUB, MUL, DIV, INC, DEC, etc.
  - Logical instructions: These