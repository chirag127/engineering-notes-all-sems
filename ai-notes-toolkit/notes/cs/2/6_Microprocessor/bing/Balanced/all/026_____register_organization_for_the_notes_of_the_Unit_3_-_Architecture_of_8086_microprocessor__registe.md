# Unit 3 - Architecture of 8086 microprocessor

## Register organization

- The 8086 microprocessor has 14 user-accessible 16-bit registers, which are divided into four groups: data, pointer and index, segment, and instruction pointer .
- The data registers are AX, BX, CX, and DX, which can store 16-bit data or two 8-bit data in their high (H) and low (L) parts. For example, AX can store AH and AL .
- The data registers are used for arithmetic, logic, data transfer, and I/O operations. AX is also called the accumulator, which is used by default for many operations.
- The pointer and index registers are SP, BP, SI, and DI, which are used for addressing memory locations. SP and BP are called stack pointer and base pointer, which are used for stack operations and accessing data in the stack segment. SI and DI are called source index and destination index, which are used for string operations and accessing data in the data segment .
- The segment registers are CS, DS, SS, and ES, which are used for defining the memory segments where the code, data, stack, and extra data are located. Each segment register can store a 16-bit segment base address, which is combined with a 16-bit offset address from a pointer or index register to form a 20-bit physical address .
- The instruction pointer register is IP, which is used for storing the offset address of the next instruction to be executed within the code segment. IP is automatically incremented by the length of the current instruction after each instruction execution .

## Bus interface unit

- The bus interface unit (BIU) is responsible for interfacing the 8086 microprocessor with the external memory and I/O devices via the system bus.
- The system bus consists of three parts: the address bus, the data bus, and the control bus. The address bus is 20-bit wide and can address up to 1 MB of memory. The data bus is 16-bit wide and can transfer 16-bit data or two 8-bit data in one cycle. The control bus consists of various signals that control the timing and direction of data transfer.
- The BIU contains a 6-byte instruction queue, which prefetches and stores the instructions from the code segment before they are executed by the execution unit (EU). This improves the performance of the 8086 by overlapping instruction fetch and execution.
- The BIU also contains the segment registers and the instruction pointer register, which are used for generating the physical addresses for memory access.

## Execution unit

- The execution unit (EU) is responsible for decoding and executing the instructions fetched by the BIU.
- The EU contains the data registers, the pointer and index registers, and the arithmetic logic unit (ALU), which are used for performing various operations on the data.
- The EU also contains the flags register, which is a 16-bit register that contains 9 status and control flags. The status flags are CF (carry flag), PF (parity flag), AF (auxiliary carry flag), ZF (zero flag), SF (sign flag), and OF (overflow flag), which are set or reset according to the result of an operation. The control flags are TF (trap flag), IF (interrupt flag), and DF (direction flag), which are used for controlling the execution mode and direction of the 8086.

## Memory addressing and memory segmentation

- The 8086 microprocessor can address up to 1 MB of memory, which is divided into four segments: code, data, stack, and extra.
- Each segment can be up to 64 KB in size, and can be located anywhere in the memory. Each segment is identified by a 16-bit segment base address, which is stored in a segment register.
- To access a memory location within a segment, a 16-bit offset address is required, which is stored in a pointer or index register or provided as an immediate operand. The offset address is relative to the start of the segment.
- To form a 20-bit physical address, the segment base address is shifted left by 4 bits and added to the offset address. For example, if CS = 1000H and IP = 2000