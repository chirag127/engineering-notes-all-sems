# Direct Memory Access for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Direct Memory Access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA can improve the performance and efficiency of data transfer between I/O devices and memory, as well as between different memory locations, by freeing the CPU from involvement with the data transfer.
- DMA can be used for "memory to memory" copying or moving data in memory, or for "peripheral to memory" data transfer from an I/O device to memory or vice versa.
- DMA requires a hardware device called a DMA controller (DMAC) that can communicate with the CPU and the I/O devices, and can control the data transfer on the bus.
- The DMA controller can operate in different modes, such as single transfer mode, block transfer mode, demand transfer mode, or cascade mode, depending on the amount and type of data to be transferred.
- The DMA controller can also support different types of DMA, such as single-channel DMA, multi-channel DMA, or bus mastering DMA, depending on the number and capability of the devices involved in the data transfer.
- The DMA controller can initiate a DMA transfer by sending a DMA request signal to the CPU, which can grant the request by sending a DMA acknowledge signal to the DMA controller.
- The DMA controller can then take control of the bus and transfer the data between the source and the destination, either directly or through an intermediate buffer.
- The DMA controller can notify the CPU of the completion of the data transfer by sending an interrupt signal to the CPU, which can then resume its normal operation.
- The advantages of DMA are that it can reduce the CPU overhead, increase the data transfer rate, and allow parallel processing of data.
- The disadvantages of DMA are that it can increase the hardware complexity, cause bus contention, and introduce security risks.