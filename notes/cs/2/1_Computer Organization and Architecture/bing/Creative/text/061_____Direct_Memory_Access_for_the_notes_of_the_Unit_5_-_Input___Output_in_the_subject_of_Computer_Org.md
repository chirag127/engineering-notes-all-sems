### Direct Memory Access for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Direct Memory Access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA is used to improve the performance and efficiency of data transfer between I/O devices and memory, or between memory and memory, without involving the CPU in each operation .
- DMA can reduce the CPU overhead and latency of data transfer, and increase the throughput and concurrency of I/O operations .
- DMA can be implemented using a dedicated hardware device called a DMA controller (DMAC), which communicates with the CPU, memory, and I/O devices using control signals and buses .
- The DMA controller can operate in different modes, such as single transfer, block transfer, demand transfer, and burst transfer, depending on the amount and frequency of data to be transferred .
- The DMA controller can also support different types of data transfer, such as memory-to-memory, memory-to-I/O, I/O-to-memory, and I/O-to-I/O .
- The DMA controller can use different techniques to access the memory, such as cycle stealing, burst mode, and transparent mode, depending on the availability and priority of the memory and the CPU .
- The DMA controller can also use different methods to arbitrate the access to the memory and the bus, such as fixed priority, rotating priority, and dynamic priority, depending on the requirements and characteristics of the devices .
- The DMA controller can be integrated with the CPU, the memory controller, the I/O controller, or the system bus, depending on the architecture and design of the computer system .
- The DMA controller can be programmed by the CPU using registers, commands, and interrupts, or by the I/O devices using direct memory access channels (DMACs) .