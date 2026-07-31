### Bus Interface Unit

- The bus interface unit (BIU) is one of the two sections of the 8086 microprocessor architecture. The other section is the execution unit (EU).
- The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions.
- The BIU performs read and write operations on data in the memory and on the external devices connected to the ports of the microprocessor, and it also sends out addresses.
- The BIU contains four 16-bit special purpose registers called as segment registers. They are code segment register (CS), data segment register (DS), stack segment register (SS), and extra segment register (ES).
- The segment registers are used for memory segmentation, which is a technique to divide the memory into logical segments of 64 KB each. Each segment register holds the base address of one of the segments.
- The BIU also contains a 16-bit instruction pointer (IP) register, which holds the offset address of the next instruction to be executed within the code segment.
- The BIU also contains a 6-byte instruction queue, which prefetches and stores the instructions from the memory before they are executed by the EU. This increases the speed of execution and allows pipelining.
- The BIU uses three different buses to transfer data and instructions between the microprocessor and other components in a computer system. They are address bus, data bus, and control bus.
- The address bus is used to send the memory address of the instruction or data being read or written. It is 20-bit wide and can address up to 1 MB of memory.
- The data bus is used to transfer the actual data or instructions between the microprocessor and the memory or I/O devices. It is 16-bit wide and can transfer one word (16 bits) at a time.
- The control bus is used to send the control signals that synchronize the operations of the microprocessor and the external devices. It consists of various signals such as read, write, interrupt, etc.