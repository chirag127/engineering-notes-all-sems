### Bus Interface Unit

- The bus interface unit (BIU) is one of the two sections of the 8086 microprocessor architecture, along with the execution unit (EU).
- The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions. 
- The BIU performs read and write operations on data in the memory and on the external devices connected to the ports of the microprocessor, and it also sends out addresses.
- The BIU contains four 16-bit special purpose registers called as segment registers. They are:
  - Code segment register (CS): is used for addressing memory location in the code segment of the memory, where the executable program is stored.
  - Data segment register (DS): is used for addressing memory location in the data segment of the memory, where the data is stored.
  - Stack segment register (SS): is used for addressing memory location in the stack segment of the memory, where the stack is stored.
  - Extra segment register (ES): is used for addressing memory location in the extra segment of the memory, which is an additional data segment.
- The BIU also contains a 16-bit instruction pointer (IP) register, which holds the offset address of the next instruction to be executed.
- The BIU also contains a 6-byte instruction queue, which prefetches and stores the instructions from the memory before they are executed by the EU.
- The BIU uses a technique called memory segmentation, which divides the memory into four segments of 64 KB each, and uses the segment registers and the offset addresses to access any location in the 1 MB memory space.
- The BIU uses three different buses to transfer data and instructions between the microprocessor and other components in a computer system. They are:
  - Address bus: The address bus is used to send the memory address of the instruction or data being read or written. It is a 20-bit bus, which can address up to 1 MB of memory.
  - Data bus: The data bus is used to transfer the instruction or data between the microprocessor and the memory or I/O devices. It is a 16-bit bidirectional bus, which can transfer up to 16 bits of data at a time. 
  - Control bus: The control bus is used to send the control signals that determine the direction and timing of the data transfer. It consists of various signals such as read, write, interrupt, etc.