# Operating modes for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

## Architecture of 8086 microprocessor

- The 8086 microprocessor is a 16-bit, N-channel, HMOS microprocessor.
- It has a 20-bit address bus and a 16-bit data bus.
- It has a two-stage pipeline that can prefetch up to 6 bytes of instructions from memory and store them in a queue.
- It has a control bus that carries signals for executing instructions, accessing memory and I/O devices, and synchronizing with other devices.
- It has two functional units: the bus interface unit (BIU) and the execution unit (EU).

### Register organization

- The 8086 has 14 registers, each of 16 bits.
- Four of them are general-purpose registers: AX, BX, CX, and DX. They can be used as 16-bit registers or as two 8-bit registers by using their high (H) and low (L) parts.
- Four of them are segment registers: CS, DS, SS, and ES. They are used to form 20-bit physical addresses by adding a 16-bit offset to a 16-bit segment base.
- Two of them are index registers: SI and DI. They are used for indexed addressing and string operations.
- Two of them are pointer registers: SP and BP. They are used for stack operations and base-relative addressing.
- One of them is the instruction pointer register: IP. It holds the offset of the next instruction to be executed within the current code segment.
- One of them is the flag register: FLAGS. It holds the status of the processor and the result of the last arithmetic or logical operation.

### Bus interface unit

- The BIU is responsible for fetching instructions from memory, generating physical addresses, and interfacing with external devices.
- It contains the instruction queue, the segment registers, and the instruction pointer register.
- It uses a technique called **segmentation** to divide the 1 MB of physical memory into 64 KB segments.
- It generates a 20-bit physical address by adding a 16-bit offset (usually from an index or pointer register) to a 16-bit segment base (from a segment register).
- It fetches instructions from the memory location pointed by the CS:IP registers and stores them in the instruction queue.
- It transfers data between the EU and the memory or I/O devices using the data bus.

### Execution unit

- The EU is responsible for decoding and executing instructions, performing arithmetic and logical operations, and updating the flag register.
- It contains the general-purpose registers, the arithmetic logic unit (ALU), and the control circuitry.
- It decodes the instructions from the instruction queue and executes them according to their format and type.
- It performs arithmetic and logical operations using the ALU and the general-purpose registers.
- It updates the flag register according to the result of the operations.
- It communicates with the BIU through an internal bus.

## Operating modes

- The 8086 microprocessor has two operating modes: the minimum mode and the maximum mode.
- The minimum mode is used when the 8086 is the only processor in the system. It provides all the control signals for memory and I/O interfacing.
- The maximum mode is used when the 8086 is part of a multiprocessor system. It requires additional hardware to generate the control signals and to coordinate with other processors.
- The operating mode is selected by the MN/MX' pin. When it is high, the 8086 operates in the minimum mode. When it is low, the 8086 operates in the maximum mode.

### Minimum mode

- In the minimum mode, the 8086 generates the following control signals:
  - ALE (Address Latch Enable): It is used to latch the lower 16 bits of the address from the address/data bus into an external latch.
  - DT/R' (Data Transmit/Receive): It