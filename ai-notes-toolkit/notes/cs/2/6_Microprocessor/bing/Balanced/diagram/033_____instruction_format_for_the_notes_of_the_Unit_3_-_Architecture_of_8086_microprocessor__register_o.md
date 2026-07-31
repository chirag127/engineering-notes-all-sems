# Unit 3 - Architecture of 8086 Microprocessor

## Register Organization

- The 8086 microprocessor has 14 registers, each of 16 bits.
- The registers are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, DX, which can be used for data manipulation and arithmetic operations. They can also be accessed as 8-bit registers by using their high (H) and low (L) bytes, such as AH, AL, BH, BL, etc.
- The segment registers are CS, DS, SS, ES, which are used to store the base addresses of the code, data, stack, and extra segments, respectively. Each segment register can hold a 16-bit value, which is multiplied by 16 to form a 20-bit physical address.
- The pointer and index registers are SP, BP, SI, DI, which are used to store offsets within the segments. SP and BP are used as stack pointer and base pointer, respectively, while SI and DI are used as source and destination index registers, respectively, for string operations.
- The flag register is a 16-bit register that contains 9 flags, which indicate the status of the processor after an operation. The flags are: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).

## Bus Interface Unit

- The bus interface unit (BIU) is responsible for interfacing the 8086 with the external world. It handles all the data transfer functions, such as fetching instructions, reading and writing data, and generating addresses.
- The BIU consists of four components: instruction queue, segment registers, address adder, and bus control logic.
- The instruction queue is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory. This improves the performance of the 8086 by allowing the execution unit to execute instructions without waiting for the BIU to fetch them.
- The segment registers are used to store the base addresses of the four segments: code, data, stack, and extra. The BIU uses these registers to generate the physical addresses for the memory access.
- The address adder is a 20-bit adder that combines the segment base address and the offset address to form the physical address. The offset address can be provided by the pointer and index registers, or by the instruction itself.
- The bus control logic is used to control the timing and direction of the data transfer on the system bus. It also generates the control signals for the memory and I/O devices, such as M/IO, RD, WR, etc.

## Execution Unit

- The execution unit (EU) is responsible for executing the instructions fetched by the BIU. It performs the arithmetic and logical operations, and updates the flag register accordingly.
- The EU consists of four components: arithmetic logic unit (ALU), general-purpose registers, flag register, and instruction decoder.
- The arithmetic logic unit (ALU) is a 16-bit unit that performs the arithmetic and logical operations, such as addition, subtraction, multiplication, division, and, or, xor, etc. It also sets or clears the flags in the flag register based on the result of the operation.
- The general-purpose registers are used to store the operands and results of the operations. They can also be used as data pointers, counters, or accumulators.
- The flag register is used to store the status of the processor after an operation. It contains 9 flags, which can be tested or modified by the instructions.
- The instruction decoder is used to decode the instructions fetched by the BIU and generate the control signals for the EU. It also determines the length and format of the instructions, and the addressing modes of the operands.

## Memory Addressing

- The 8086 microprocessor can address up to 1 MB of memory, using a 20-bit physical address.
- The memory is divided into segments, each of 64 KB in size. A segment is identified by its base address, which is a multiple of 16.
- The 8086 microprocessor can access four segments at a time, using the segment registers: CS, DS, SS, ES. Each segment register can hold a 16-bit value, which is multiplied by 16 to form the high-order 16 bits of the physical address.
- The low-order 16 bits of the physical address are provided by the offset address, which is an offset within the segment