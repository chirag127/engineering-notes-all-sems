# Unit 3 - Architecture of 8086 microprocessor

The 8086 microprocessor is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines. It was designed by Intel between 1976 and 1978 and released on June 8, 1978.

The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  . The figure below shows the block diagram of the architectural representation of the 8086 microprocessor:

![8086 architecture](https://www.electronicsmind.com/wp-content/uploads/2022/01/8086-architecture.png)

## Bus Interface Unit (BIU)

The bus interface unit interfaces 8086 with the external world. It handles all the data transfer functions. It consists of the following components:

- **Segment registers**: These are four 16-bit registers that store the starting addresses of four memory segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). Each segment can be up to 64 KB in size.
- **Instruction pointer (IP)**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
- **Address adder**: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O devices.
- **Instruction queue**: This is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory. This increases the speed of instruction execution by reducing the wait states.
- **Data bus buffer**: This is a 16-bit bidirectional buffer that transfers data between the BIU and the EU.
- **Control bus**: This is a set of control signals that control the operation of the BIU and the EU.

## Execution Unit (EU)

The execution unit executes the instructions fetched by the BIU. It consists of the following components:

- **Arithmetic and logic unit (ALU)**: This is a 16-bit unit that performs arithmetic and logical operations on the operands.
- **General purpose registers**: These are eight 16-bit registers that can be used for various purposes. They are: accumulator (AX), base (BX), counter (CX), data (DX), source index (SI), destination index (DI), base pointer (BP), and stack pointer (SP). Each register can be accessed as a whole (16 bits) or as two halves (8 bits each).
- **Flag register**: This is a 16-bit register that stores the status of the EU after an operation. It has nine flags: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).
- **Instruction decoder**: This is a circuit that decodes the instructions fetched by the BIU and generates the appropriate control signals for the EU.

## Memory addressing and memory segmentation

The 8086 microprocessor can address up to 1 MB of memory using 20 address lines. However, the 8086 uses a segmented memory model, which means that the memory is divided into segments of up to 64 KB each. Each segment has a base address and an offset address. The base address is stored in one of the segment registers (CS, DS, SS, or ES), and the offset address is stored in one of the general purpose registers or the instruction pointer. The physical address is calculated by adding the base address and the offset address, as shown below:

![memory addressing](https://www.geeksforgeeks.org/wp-content/uploads/8086-memory-addressing.png)

The advantage of memory segmentation is that it allows the programmer to access different types of data (code, data, stack, or extra) in different segments, and to relocate the segments easily. The disadvantage is that it limits the size of each segment to 64 KB, and requires more instructions to access the memory.

## Operating modes

The 8086 microprocessor has two operating modes: minimum mode and maximum mode. The minimum mode is used when the 8086 is the only processor in the system, and the maximum mode is used when the 8086 is part of a multiprocessor system.

In the minimum mode, the 8086 generates all the control signals for the memory and I/O devices, and uses