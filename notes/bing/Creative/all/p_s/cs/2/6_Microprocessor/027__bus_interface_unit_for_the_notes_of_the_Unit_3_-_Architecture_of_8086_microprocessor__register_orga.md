### Bus Interface Unit

- The bus interface unit (BIU) is one of the two sections or units of the 8086 microprocessor architecture. The other section is the execution unit (EU).
- The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions.
- The BIU performs read and write operations on data in the memory and on the external devices connected to the ports of the microprocessor, and it also sends out addresses.
- The BIU contains four 16-bit special purpose registers called as segment registers. They are:
  - Code segment register (CS): is used for addressing memory location in the code segment of the memory, where the executable program is stored.
  - Data segment register (DS): is used for addressing memory location in the data segment of the memory, where the data used by the program is stored.
  - Stack segment register (SS): is used for addressing memory location in the stack segment of the memory, where the stack data is stored.
  - Extra segment register (ES): is used for addressing memory location in the extra segment of the memory, which can be used for additional data storage.
- The BIU also contains a 16-bit instruction pointer (IP) register, which holds the offset address of the next instruction to be executed within the code segment.
- The BIU also contains a 6-byte instruction queue, which prefetches and stores the instructions from the memory before they are executed by the EU. This increases the speed of execution and allows pipelining.
- The BIU uses a technique called memory segmentation to divide the 1 MB physical memory into four logical segments of 64 KB each. Each segment is identified by a 16-bit segment address and a 16-bit offset address within the segment. The segment address and the offset address are combined by the BIU to form a 20-bit physical address, which is sent to the address bus.
- The BIU uses the following formula to calculate the physical address from the segment address and the offset address:

  `Physical address = (Segment address * 16) + Offset address`

- The BIU can access any of the four segments at a time by using the appropriate segment register and the offset address. For example, to access the code segment, the BIU uses the CS register and the IP register. To access the data segment, the BIU uses the DS register and an offset address specified by the instruction. To access the stack segment, the BIU uses the SS register and the stack pointer (SP) register. To access the extra segment, the BIU uses the ES register and an offset address specified by the instruction.

Some possible mnemonics and learning tricks for the topic are:

- To remember the names and order of the segment registers, use the acronym **CDES** (Code, Data, Extra, Stack).
- To remember the formula for calculating the physical address, use the phrase **SOS** (Segment * 16 + Offset).
- To remember the size of the segments and the physical memory, use the numbers **64** and **1024**. Each segment is 64 KB and the physical memory is 1024 KB (1 MB).
- To remember the function of the instruction queue, use the word **PIPE** (Prefetch, Increase, Pipeline, Execute). The BIU prefetches the instructions, increases the speed of execution, allows pipelining, and sends the instructions to the EU for execution.