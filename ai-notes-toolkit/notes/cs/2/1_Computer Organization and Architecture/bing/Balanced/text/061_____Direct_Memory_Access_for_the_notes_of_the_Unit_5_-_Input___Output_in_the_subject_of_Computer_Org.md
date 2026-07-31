### Direct Memory Access for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Direct Memory Access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA is used to improve the performance and efficiency of data transfer between I/O devices and memory, or between memory and memory, without involving the CPU in each operation .
- DMA can reduce the CPU overhead and latency of data transfer, and increase the throughput and concurrency of I/O operations .
- DMA can be implemented using a dedicated hardware device called a DMA controller (DMAC), which communicates with the CPU, memory, and I/O devices using control signals, addresses, and data buses .
- The DMA controller can operate in different modes, such as single transfer, block transfer, demand transfer, and burst transfer, depending on the amount and frequency of data to be transferred .
- The DMA controller can also support different types of data transfer, such as one-to-one, one-to-many, many-to-one, and many-to-many, depending on the source and destination of data.
- The DMA controller can also perform scatter-gather operations, which involve transferring data from or to non-contiguous memory locations.
- The DMA controller can be programmed by the CPU using special registers or memory-mapped I/O, or by the I/O devices using bus mastering or direct memory access network-on-chip (DMANoC) .
- The DMA controller can generate interrupts to the CPU to indicate the completion or error of a data transfer operation .
- The DMA controller can also cooperate with the memory management unit (MMU) to handle virtual memory addresses and page faults.
- The DMA controller can also support cache coherence protocols to ensure data consistency between the CPU cache and the main memory.