### Direct Memory Access

- Direct memory access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA can improve the performance and efficiency of memory operations by reducing the CPU involvement and allowing the CPU to perform other tasks while the data transfer is in progress.
- DMA is managed by a dedicated hardware device called a DMA controller (DMAC), which communicates with the CPU, the memory, and the input/output (I/O) devices.
- The basic steps of DMA are:
  - The CPU initiates a DMA transfer by sending the following information to the DMAC: the source and destination addresses, the number of bytes to be transferred, and the direction of the transfer (read or write).
  - The DMAC requests the bus from the CPU and takes control of it once the CPU grants the bus.
  - The DMAC initiates the data transfer by sending the appropriate signals to the memory and the I/O device.
  - The DMAC transfers one word of data at a time until the specified number of bytes is transferred.
  - The DMAC releases the bus and sends an interrupt signal to the CPU to indicate the completion of the transfer.
- DMA can be classified into different modes based on the degree of CPU involvement and the timing of the data transfer:
  - Single-cycle DMA: The DMAC transfers the entire block of data in one bus cycle, blocking the CPU from accessing the bus until the transfer is complete. This mode is fast but may cause delays for the CPU.
  - Burst DMA: The DMAC transfers a fixed number of words in one bus cycle, then releases the bus and requests it again for the next burst. This mode allows the CPU to access the bus between the bursts, but may cause bus contention.
  - Cycle-stealing DMA: The DMAC transfers one word of data in one bus cycle, then releases the bus and requests it again for the next word. This mode minimizes the delay for the CPU, but may slow down the overall transfer rate.
  - Block DMA: The DMAC transfers a block of data in one bus cycle, then waits for a synchronization signal from the I/O device before transferring the next block. This mode is suitable for devices that have variable data rates, such as disk drives.