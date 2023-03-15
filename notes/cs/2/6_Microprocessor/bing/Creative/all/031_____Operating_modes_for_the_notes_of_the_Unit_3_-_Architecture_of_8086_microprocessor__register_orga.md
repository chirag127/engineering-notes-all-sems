# Operating modes for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

## Architecture of 8086 microprocessor

- The 8086 microprocessor is a 16-bit, N-channel, HMOS microprocessor.
- It has a 20-bit address bus and a 16-bit data bus .
- It has a two-stage pipeline that can prefetch up to six bytes of instructions from memory and store them in a queue .
- It has a bus interface unit (BIU) and an execution unit (EU) that work in parallel .
- The BIU is responsible for fetching instructions, generating addresses, and transferring data to and from memory and I/O devices .
- The EU is responsible for decoding and executing instructions, performing arithmetic and logical operations, and managing flags and registers .
- The 8086 has 14 registers, divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register .
- The general-purpose registers are AX, BX, CX, and DX, each 16 bits wide and can be accessed as two 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL) .
- The segment registers are CS, DS, SS, and ES, each 16 bits wide and used to form the 20-bit physical address of a memory location .
- The pointer and index registers are SP, BP, SI, and DI, each 16 bits wide and used for addressing memory locations using different addressing modes .
- The flag register is a 16-bit register that contains nine flags that indicate the status of the EU after an operation .
- The flags are: carry flag (CF), parity flag (PF), auxiliary carry flag (AF), zero flag (ZF), sign flag (SF), trap flag (TF), interrupt flag (IF), direction flag (DF), and overflow flag (OF) .

## Memory addressing and memory segmentation

- The 8086 can address up to 1 MB of memory using a 20-bit address .
- The 20-bit address is formed by adding a 16-bit segment address and a 16-bit offset address, with the segment address shifted left by four bits .
- The segment address is stored in one of the segment registers (CS, DS, SS, or ES), and the offset address is specified by an instruction or a register .
- The memory is divided into segments of up to 64 KB each, and each segment has a base address and a limit .
- The base address is the starting address of the segment, and the limit is the number of bytes in the segment minus one .
- The segment registers point to the base address of the segment, and the offset address is added to the base address to get the physical address of a memory location .
- The memory segmentation allows the 8086 to access more memory than its address bus width, and also provides a logical organization of the memory into different types of data .
- The CS register points to the code segment, which contains the instructions to be executed .
- The DS register points to the data segment, which contains the data to be used by the instructions .
- The SS register points to the stack segment, which contains the stack data structure used for storing return addresses, parameters, and local variables of subroutines .
- The ES register points to the extra segment, which can be used for additional data or code .

## Operating modes

- The 8086 has two operating modes: minimum mode and maximum mode .
- The minimum mode is used when the