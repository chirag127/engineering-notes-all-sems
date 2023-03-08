## Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 is a 16-bit microprocessor with a 16-bit internal and external data bus. With 20 address lines, it can access upto 2^20 = 1 MB of memory.
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  .
- The Bus Interface Unit (BIU) provides the interface of 8086 to external memory and I/O devices via the System Bus. It handles all the data transfer functions  .
- The BIU consists of the following components  :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES).
  - Instruction pointer (IP): This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O device.
  - Prefetch queue: This is a 6-byte buffer that stores the prefetched instructions from the memory. It helps to speed up the execution by providing the instructions to the EU without waiting for the memory access.
- The Execution Unit (EU) performs the arithmetic and logical operations on the data. It also controls the flow of execution by testing the condition codes and executing the jumps, loops, and calls  .
- The EU consists of the following components  :
  - General purpose registers: These are eight 16-bit registers that can be used for various purposes such as data storage, address calculation, and operand manipulation. They are: accumulator (AX), base (BX), counter (CX), data (DX), source index (SI), destination index (DI), base pointer (BP), and stack pointer (SP).
  - Arithmetic and logic unit (ALU): This is a circuit that performs the arithmetic and logical operations on the data, such as addition, subtraction, multiplication, division, and, or, xor, not, etc.
  - Flag register: This is a 16-bit register that stores the status of the EU after an operation. It consists of nine flags: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).
  - Control unit: This is a circuit that controls the operation of the EU by decoding the instructions, generating the control signals, and coordinating the timing of the EU and the BIU.
  - Decode unit: This is a circuit that decodes the instructions from the prefetch queue and sends them to the control unit.
- The 8086 has two operating modes: minimum mode and maximum mode.
  - Minimum mode: This is the mode in which the 8086 operates as a single processor in a system. It uses the MN/MX# pin as an output to enable the external bus drivers and buffers. It also generates the control signals for the memory and I/O devices, such as RD#, WR#, IO/M#, DT/R#, DEN#, etc.
  - Maximum mode: This is the mode in which the 8086 operates as a master processor in a multiprocessor system. It uses the MN/MX# pin as an input to select the mode. It also uses the S0, S1, and S2 pins as outputs to indicate the status of the current bus cycle. It requires an external bus controller, such as the 8288, to generate the control signals for the memory and I/O devices.
- The 8086 has a rich instruction set that can perform various operations on the data, such as data transfer, arithmetic, logical, shift, rotate, string, branch, loop, call, return, interrupt, etc.
- The instruction format of the 8086 consists of one to six

Some possible mnemonics and learning tricks for the topic are:

- To remember the names and order of the segment registers, use the acronym **C**o**D**e **S**tack **E**xtra (CS, DS, SS, ES).
- To remember the names and order of the general purpose registers, use the acronym **A** **B**ig **C**at **D**rank **S**ome **D**irty **B**rown **S**oup (AX, BX, CX, DX, SI, DI, BP, SP).
- To remember the names and order of the flag register bits, use the acronym **C**ows **P**refer **A** **Z**ebra **S**triped **T**ent **I**n **D**ecember **O**nly (CF, PF, AF, ZF, SF, TF, IF, DF, OF).
- To remember the difference between minimum and maximum mode, use the trick that minimum mode has minimum pins (MN/MX# as output) and maximum mode has maximum pins (MN/MX# as input, S0, S1, S2 as output).
- To remember the difference between IO/M# and DT/R# pins, use the trick that IO/M# indicates whether the bus cycle is for I/O or memory, and DT/R# indicates whether the data is being transferred or received.