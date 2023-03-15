# Bus Interface Unit

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
- The BIU uses a technique called memory segmentation to divide the 1 MB physical memory into four logical segments of 64 KB each. Each segment is identified by a 16-bit segment base address, which is stored in the corresponding segment register. The segment base address is also called the segment selector.
- The BIU generates a 20-bit physical address by adding a 16-bit offset address to the segment base address. The offset address is also called the effective address or the displacement. The physical address is also called the linear address or the absolute address.
- The physical address is calculated by the BIU as follows:

  - Physical address = (Segment base address * 16) + Offset address
  - For example, if CS = 1000H and IP = 2000H, then the physical address of the next instruction is:

    - Physical address = (1000H * 16) + 2000H
    - Physical address = 10000H + 2000H
    - Physical address = 12000H
- The BIU uses three different buses to transfer data and instructions between the microprocessor and other components in a computer system. These buses are:

  - Address bus: The address bus is used to send the memory address of the instruction or data being read or written. It is a unidirectional bus, which means it can only carry data from the BIU to the memory or I/O devices. The address bus of 8086 is 20-bit wide, which means it can address up to 2^20 or 1 MB of memory locations.
  - Data bus: The data bus is used to send or receive the instruction or data being read or written. It is a bidirectional bus, which means it can carry data both ways, from the BIU to the memory or I/O devices, and vice versa. The data bus of 8086 is 16-bit wide, which means it can transfer 16 bits or 2 bytes of data at a time.
  - Control bus: The control bus is used to send control signals that synchronize the data transfer between the BIU and the memory or I/O devices. It is a bidirectional bus, which means it can carry control signals both ways, from the BIU to the memory or I/O devices, and vice versa. The control bus of 8086 consists of several control lines, such as:

    - Memory/IO: This line indicates whether the BIU is accessing the memory or an I/O device. It is a unidirectional line, which means it can only carry data from the BIU to the memory or I/O devices. When this line is high, it means the BIU is accessing the memory. When this line is low, it means the BIU is accessing an I/O device.
    - Read/Write: This line indicates whether the BIU is performing a read or a write operation. It is a unidirectional line, which means it can only carry data from the BIU to