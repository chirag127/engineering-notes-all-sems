## Unit 4 - Assembly language programming based on intel 8085/8086. Instructions, data transfer, arithmetic, logic, branch operations, looping, counting, indexing, programming techniques, counters and time delays, stacks and subroutines, conditional call and return instructions.

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that the microprocessor can execute.
- Assembly language is specific to a given processor. For example, the assembly language of 8085 is different from that of 8086.
- Assembly language programming requires an assembler, which is a software tool that converts the assembly code into machine code and stores it in the memory.
- Assembly language programming also requires a debugger, which is a software tool that allows the programmer to test and correct the errors in the code.
- Assembly language programming has some advantages and disadvantages over high-level languages. Some of the advantages are:
  - It gives more control over the hardware and allows direct access to the registers, memory and I/O ports.
  - It is faster and more efficient than high-level languages, as it uses fewer instructions and memory space.
  - It is easier to understand the working of the microprocessor and the interfacing of the peripherals.
- Some of the disadvantages are:
  - It is difficult to write, read and debug, as it uses symbols and numbers instead of words and operators.
  - It is not portable, as it depends on the architecture and instruction set of the microprocessor.
  - It is not standardized, as different assemblers may have different syntax and conventions.

- The 8085 and 8086 are two popular microprocessors developed by Intel in the late 1970s and early 1980s. They have some similarities and differences in their architecture and instruction set.
- The 8085 is an 8-bit microprocessor, which means it can process 8 bits of data at a time. It has a 16-bit address bus, which means it can access 2^16 or 64 KB of memory. It has a 8-bit data bus, which means it can transfer 8 bits of data at a time. It has 74 instructions, divided into five groups: data transfer, arithmetic, logic, branch and control.
- The 8086 is a 16-bit microprocessor, which means it can process 16 bits of data at a time. It has a 20-bit address bus, which means it can access 2^20 or 1 MB of memory. It has a 16-bit data bus, which means it can transfer 16 bits of data at a time. It has 133 instructions, divided into six groups: data transfer, arithmetic, logic, branch, string and miscellaneous.
- The 8086 has some features that the 8085 does not have, such as segmentation, pipelining, instruction queue, addressing modes and registers.
- Segmentation is a technique that divides the memory into four segments: code, data, stack and extra. Each segment has a 64 KB size and a 16-bit address. The 8086 uses two 16-bit registers, called segment registers, to store the base address of each segment. The segment registers are CS (code segment), DS (data segment), SS (stack segment) and ES (extra segment).
- Pipelining is a technique that allows the 8086 to fetch the next instruction while executing the current one. This improves the speed and performance of the microprocessor. The 8086 has two units, called the bus interface unit (BIU) and the execution unit (EU), that work in parallel. The BIU is responsible for fetching the instructions from the memory and storing them in a 6-byte instruction queue. The EU is responsible for decoding and executing the instructions from the queue.
- Addressing modes are the ways of specifying the location of the operands in an instruction. The 8086 has 12 addressing modes, which are: immediate, register, direct, register indirect, based, indexed, based indexed, relative, based relative, indexed relative, intrinsic and implied.
- Registers are the internal storage locations of the microprocessor that can hold data, address or control information. The 8086 has 14 registers, which are: four segment registers (CS, DS, SS, ES), four general purpose registers (AX, BX, CX, DX), four index registers (SI, DI, BP, SP) and two pointer registers (IP, FLAGS). The general purpose registers can be used as 16-bit or 8-bit registers. For example, AX can be used as AH

Some of the mnemonics and learning tricks for the topic are:

- To remember the segment registers, use the acronym CDES (Code, Data, Extra, Stack).
- To remember the general purpose registers, use the acronym ABCD (AX, BX, CX, DX).
- To remember the index registers, use the acronym SIBS (SI, DI, BP, SP).
- To remember the 8085 instruction groups, use the acronym DALBC (Data transfer, Arithmetic, Logic, Branch, Control).
- To remember the 8086 instruction groups, use the acronym DALBSM (Data transfer, Arithmetic, Logic, Branch, String, Miscellaneous).
- To remember the 8086 addressing modes, use the acronym IRDBIRBIRI (Immediate, Register, Direct, Register Indirect, Based, Indexed, Based Indexed, Relative, Based Relative, Indexed Relative, Intrinsic, Implied).