### Memory Segmentation

- Memory segmentation is a technique of dividing the memory into logical segments of equal size (64 KB) to facilitate the management and protection of memory.
- The 8086 microprocessor has 20 address lines, which means it can access 1 MB (2^20 bytes) of physical memory. However, the 8086 can only work with 16-bit registers, which means it can only manipulate 64 KB (2^16 bytes) of memory at a time.
- To overcome this limitation, the 8086 uses a scheme called memory segmentation, which allows it to access any of the 1 MB memory locations using two 16-bit registers: a segment register and an offset register.
- The segment register contains the upper 16 bits of the starting address of a 64 KB memory segment, while the offset register contains the lower 16 bits of the address of a specific location within that segment.
- The 8086 has four segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). Each segment register can point to any of the 16 possible segments in the 1 MB memory space.
- The 8086 uses a special arithmetic unit called the segment adder to calculate the effective physical address from the segment and offset registers. The segment adder shifts the segment register value four bits to the left and adds it to the offset register value, resulting in a 20-bit physical address.
- For example, if CS = 1000H and IP = 2000H, then the physical address of the next instruction to be executed is (1000H << 4) + 2000H = 12000H.
- The 8086 uses different segment and offset registers for different types of memory accesses. For instruction fetching, it uses CS and IP (instruction pointer). For data access, it uses DS and one of the general-purpose registers (BX, SI, DI, or BP). For stack operations, it uses SS and SP (stack pointer). For string operations, it uses ES and DI as the destination segment and offset, and DS and SI as the source segment and offset.
- Memory segmentation allows the 8086 to access more memory than its register size, but it also introduces some drawbacks. For instance, memory segmentation makes it difficult to access data that spans across two segments, or to use more than 64 KB of code or data in a single segment. Moreover, memory segmentation does not provide any protection or isolation between segments, as any program can access any segment with no restrictions.

Some possible mnemonics and learning tricks for the topic are:

- To remember the four segment registers, use the acronym CDES (Code, Data, Extra, Stack).
- To remember the formula for calculating the physical address, use the phrase "Segment shifted left four, plus offset gives you more".
- To remember the default segment and offset registers for different types of memory accesses, use the following table:

| Memory Access | Segment Register | Offset Register |
|---------------|------------------|-----------------|
| Instruction Fetching | CS | IP |
| Data Access | DS | BX, SI, DI, or BP |
| Stack Operations | SS | SP |
| String Operations | ES (destination) | DI |
|  | DS (source) | SI |