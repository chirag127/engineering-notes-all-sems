### I/O Interface

- The I/O interface is the part of the computer system that supports the communication between the internal storage (memory) and the external I/O devices (peripherals)  .
- The I/O interface consists of one or more I/O ports, which are registers that can be accessed by the CPU or the I/O devices  .
- The I/O ports can be classified into two types: memory-mapped I/O and isolated I/O  .
  - Memory-mapped I/O: The I/O ports are assigned addresses in the same address space as the memory, and the CPU can access them using the same instructions as for memory access  .
  - Isolated I/O: The I/O ports are assigned separate addresses from the memory, and the CPU can access them using special I/O instructions  .
- The I/O interface can operate in different modes, depending on how the data transfer between the CPU and the I/O devices is controlled  .
  - Programmed I/O: The CPU initiates and monitors the data transfer, and waits for the I/O device to be ready before sending or receiving data  .
  - Interrupt-driven I/O: The CPU initiates the data transfer, but does not wait for the I/O device to be ready. Instead, the I/O device sends an interrupt signal to the CPU when it is ready, and the CPU resumes the data transfer  .
  - Direct memory access (DMA) I/O: The CPU delegates the data transfer to a special hardware device called the DMA controller, which can access the memory and the I/O ports directly, without involving the CPU  .
- The I/O interface is designed to provide a systematic means of controlling the interaction with the outside world and to provide the operating system with the information it needs to manage I/O activity effectively .