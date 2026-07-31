# Unit 3 - Architecture of 8086 Microprocessor

## Register Organization

- The 8086 microprocessor has 14 registers, each of 16 bits.
- The registers are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, DX, which can be used for data manipulation and arithmetic operations. They can also be accessed as 8-bit registers by using their high (H) and low (L) bytes, such as AH, AL, BH, BL, etc.
- The segment registers are CS, DS, SS, ES, which are used to store the base addresses of the code, data, stack, and extra segments, respectively. Each segment register can hold a 16-bit value, which is multiplied by 16 to form a 20-bit physical address.
- The pointer and index registers are IP, SP, BP, SI, DI, which are used to store offsets within the segments. IP is the instruction pointer, which points to the next instruction to be executed. SP is the stack pointer, which points to the top of the stack. BP is the base pointer, which is used for accessing parameters and local variables on the stack. SI and DI are the source and destination index registers, which are used for string operations and memory copying.
- The flag register is a 16-bit register, which contains 9 flags that indicate the status of the processor and the result of the last arithmetic or logical operation. The flags are: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).

## Bus Interface Unit

- The bus interface unit (BIU) is responsible for interfacing the 8086 with the external world. It handles all the data transfer functions, such as fetching instructions, reading and writing data, and generating addresses.
- The BIU has a 16-bit data bus and a 20-bit address bus. It can access up to 1 MB of memory and 64 KB of I/O ports.
- The BIU has a 6-byte instruction queue, which prefetches and stores the instructions from the memory. This improves the performance of the processor by reducing the wait states.
- The BIU also has an address adder, which calculates the physical address from the segment and offset values. The physical address is given by: Physical address = Segment address * 16 + Offset address

## Execution Unit

- The execution unit (EU) is responsible for executing the instructions fetched by the BIU. It performs all the arithmetic and logical operations, as well as the control and branching operations.
- The EU has an arithmetic logic unit (ALU), which performs the arithmetic and logical operations on the data. The ALU can operate on 8-bit or 16-bit operands, and can also perform bit manipulation and shift operations.
- The EU also has a control unit, which decodes the instructions and generates the control signals for the ALU and the BIU. The control unit also handles the interrupts and exceptions that occur during the execution.
- The EU communicates with the BIU through an internal bus, which is 16 bits wide. The EU can access the registers and the instruction queue of the BIU, as well as the data bus and the address bus.

## Memory Addressing and Memory Segmentation

- The 8086 microprocessor uses a segmented memory model, which divides the memory into four segments: code, data, stack, and extra. Each segment can be up to 64 KB in size, and can be located anywhere in the 1 MB memory space.
- The memory addressing scheme of the 8086 uses two components: a segment address and an offset address. The segment address is stored in one of the segment registers, and the offset address is stored in one of the pointer or index registers, or in an immediate value. The segment address and the offset address are combined by the BIU to form a 20-bit physical address, which is used to access the memory.
- The memory segmentation allows the 8086 to access more than 64 KB of memory, and also provides a logical organization of the memory. However, it also introduces some limitations and complexities, such as the need to manage the segment registers, the possibility of segment overlap, and the restriction of the offset address to 16 bits.

## Operating Modes

- The 8086 microprocessor has two operating modes: minimum mode and maximum mode. The minimum mode is used when the