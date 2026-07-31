# Register Organization of 8086 Microprocessor

- The 8086 microprocessor has 14 internal registers that are accessible to the programmer .
- The registers are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and instruction pointer and flags register .
- Each register is 16 bits wide and can store one word (two bytes) of data .
- Some registers can be further divided into two 8-bit registers to perform byte operations .

## General-Purpose Registers

- The general-purpose registers are AX, BX, CX, and DX .
- They can be used to store data, operands, and results of arithmetic and logical operations.
- They can also be used as base or index registers for memory addressing.
- Each general-purpose register can be split into two 8-bit registers: AH and AL for AX, BH and BL for BX, CH and CL for CX, and DH and DL for DX .
- For example, AX can store 16-bit data such as 1234H, or AH can store the high byte (12H) and AL can store the low byte (34H) separately.

## Segment Registers

- The segment registers are CS, DS, SS, and ES .
- They are used to define the memory segments for code, data, stack, and extra data respectively .
- They store the 16-bit segment addresses that are combined with the offset addresses from the pointer and index registers to form the 20-bit physical addresses for memory access .
- For example, if CS = 1000H and IP = 0100H, then the physical address of the next instruction to be executed is 1000H * 10H + 0100H = 10010H.

## Pointer and Index Registers

- The pointer and index registers are SP, BP, SI, and DI .
- They are used to store the offset addresses within the memory segments defined by the segment registers .
- SP and BP are used as stack pointer and base pointer for the stack segment .
- SI and DI are used as source index and destination index for the data segment .
- They can also be used as general-purpose registers for arithmetic and logical operations .

## Instruction Pointer and Flags Register

- The instruction pointer (IP) register is used to store the offset address of the next instruction to be executed within the code segment defined by the CS register .
- The flags register is used to store the status and control flags that reflect the outcome of the previous instruction or affect the execution of the current or future instructions .
- The flags register has 16 bits, but only 9 bits are used for flags .
- The flags are: carry flag (CF), parity flag (PF), auxiliary carry flag (AF), zero flag (ZF), sign flag (SF), trap flag (TF), interrupt flag (IF), direction flag (DF), and overflow flag (OF) .

# Bus Interface Unit

- The bus interface unit (BIU) is responsible for the communication between the 8086 microprocessor and the external memory and I/O devices via the system bus.
- The system bus consists of three buses: the data bus, the address bus, and the control bus.
- The data bus is a bidirectional bus that carries the data to be read or written between the microprocessor and the memory or I/O devices.
- The address bus is a unidirectional bus that carries the 20-bit physical address from the microprocessor to the memory or I/O devices.
- The control bus is a bidirectional bus that carries the control signals to synchronize the data transfer and indicate the type of operation.
- The BIU has four components: the segment registers, the instruction pointer, the instruction queue, and the bus control logic.

## Segment Registers

- The segment registers are the same