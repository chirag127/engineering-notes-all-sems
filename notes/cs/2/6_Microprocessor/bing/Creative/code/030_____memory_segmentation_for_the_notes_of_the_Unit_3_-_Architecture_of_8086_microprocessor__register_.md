### Memory Segmentation

- Memory segmentation is a technique to allow programs to address more than 64 KB of memory on the 8086 microprocessor.
- The 8086 microprocessor has 20 address lines, which means it can interface 1 MB of memory. However, its internal registers are only 16 bits wide, which means they can only hold values up to 65,536.
- To overcome this limitation, the 8086 microprocessor segments the memory into 16 segments of 64 KB each. Each segment has a unique 16-bit segment number, which is stored in one of the four segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES).
- To access a memory location within a segment, the 8086 microprocessor uses a 16-bit offset address, which is added to the segment number to form a 20-bit physical address. The offset address is stored in one of the general-purpose registers or the instruction pointer (IP) register.
- The formula for calculating the physical address is:

    `Physical address = (Segment number * 16) + Offset address`

- For example, if CS = 1000h and IP = 2000h, then the physical address of the next instruction to be executed is:

    `Physical address = (1000h * 16) + 2000h = 12000h`

- The 8086 microprocessor can work with only four segments at a time, one for each segment register. To access a different segment, the segment register must be changed. This can be done by using instructions such as LDS, LES, PUSH, POP, etc.
- Memory segmentation allows the 8086 microprocessor to access different types of data and code in different segments, and to use the same offset address for different segments. However, it also introduces some disadvantages, such as memory fragmentation, segment overlap, and increased complexity of address calculation.