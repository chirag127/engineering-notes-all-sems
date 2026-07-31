### I/O Ports

- I/O ports are the interfaces between the CPU and the external devices, such as keyboards, mice, printers, scanners, etc.
- I/O ports allow data to be transferred between the internal storage and the external I/O devices.
- I/O ports are controlled by I/O modules, which are special hardware components that coordinate the timing and control of I/O operations .
- I/O ports can be classified into two types: serial ports and parallel ports.
  - Serial ports transmit data one bit at a time, using a single wire or a pair of wires. Serial ports are used for external modems and older computer mice. Serial ports have two versions: 9-pin and 25-pin. Data travels at 115 kilobits per second on serial ports.
  - Parallel ports transmit data multiple bits at a time, using multiple wires. Parallel ports are used for scanners and printers. Parallel ports have a 25-pin model. Data travels at 2.4 megabits per second on parallel ports.
- I/O ports can also be categorized into two modes: programmed I/O and direct memory access (DMA).
  - Programmed I/O is a mode in which the CPU is directly involved in the I/O operations. The CPU initiates the I/O operation, checks the status of the I/O device, and transfers the data between the memory and the I/O device. Programmed I/O is simple but slow, as it consumes a lot of CPU time and cycles.
  - Direct memory access (DMA) is a mode in which a specialized I/O processor takes over control of an I/O operation to move a large block of data. The CPU initiates the DMA operation by sending the parameters of the data transfer, such as the source and destination addresses, the number of bytes, and the I/O device number, to the DMA controller. The DMA controller then performs the data transfer without the CPU's intervention, and notifies the CPU when the transfer is complete. DMA is faster and more efficient than programmed I/O, as it frees up the CPU for other tasks.
- Some examples of external I/O interfaces are FireWire and Infiniband.
  - FireWire is a high-speed serial interface that can connect up to 63 devices on a single bus. FireWire can support data rates of up to 800 megabits per second. FireWire is used for digital video cameras, external hard drives, and other multimedia devices.
  - Infiniband is a high-performance serial interface that can connect multiple processors, memory modules, and I/O devices on a switched fabric network. Infiniband can support data rates of up to 40 gigabits per second. Infiniband is used for cluster computing, storage area networks, and other high-end applications.