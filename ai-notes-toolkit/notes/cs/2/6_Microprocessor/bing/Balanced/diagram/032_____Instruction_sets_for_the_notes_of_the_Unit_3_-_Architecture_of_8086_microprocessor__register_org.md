### Instruction sets for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)   .
- The BIU interfaces 8086 with the external world and handles all the data transfer functions  . It consists of the following components:
  - A 16-bit data bus and a 20-bit address bus that can access up to 1 MB of memory   .
  - Four 16-bit segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES) that store the base addresses of the corresponding memory segments   .
  - A 16-bit instruction pointer (IP) that points to the next instruction to be executed in the code segment   .
  - A 6-byte instruction queue that prefetches and stores the instructions from the code segment   .
- The EU executes the instructions fetched by the BIU and performs arithmetic and logical operations  . It consists of the following components:
  - An arithmetic and logic unit (ALU) that performs 8-bit and 16-bit arithmetic and logical operations   .
  - A flag register that contains 9 flags: 6 status flags (carry, parity, auxiliary carry, zero, sign, and overflow) and 3 control flags (trap, interrupt enable, and direction)   .
  - Four 16-bit general purpose registers: accumulator (AX), base (BX), counter (CX), and data (DX) that can be used as 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL)   .
  - Two 16-bit pointer registers: stack pointer (SP) and base pointer (BP) that point to the top and bottom of the stack segment   .
  - Two 16-bit index registers: source index (SI) and destination index (DI) that are used for string operations and memory addressing   .
- The memory addressing of the 8086 microprocessor is based on the concept of memory segmentation, which divides the memory into four segments: code, data, stack, and extra   . Each segment has a 64 KB size and a 16-bit offset address   . The physical address of any memory location is calculated by adding the base address of the segment (stored in the segment register) and the offset address of the location (specified by the instruction)   . The physical address is 20-bit long and is formed by shifting the base address 4 bits to the left and adding the offset address   .
- The operating modes of the 8086 microprocessor are the minimum mode and the maximum mode   . The minimum mode is used when the 8086 is the only processor in the system and the maximum mode is used when the 8086 is interfaced with a coprocessor such as 8087 or 8089   . The operating mode is selected by the MN/MX# pin of the 8086, which is low for the minimum mode and high for the maximum mode   .
- The instruction set of the 8086 microprocessor consists of various types of instructions that perform different operations on the data  [^2^