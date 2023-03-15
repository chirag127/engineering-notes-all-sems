# I/O Ports

- I/O ports are the interface between the CPU and the external devices such as keyboards, mice, printers, scanners, etc.
- I/O ports allow data to be transferred between the internal storage and the external I/O devices.
- I/O ports are part of the I/O module, which is a special hardware component that controls and coordinates the I/O operations.
- I/O ports can be classified into two types: serial ports and parallel ports.
  - Serial ports transmit data one bit at a time over a single wire. They are used for external modems and older computer mice. They have two versions: 9-pin and 25-pin. Data travels at 115 kilobits per second.
  - Parallel ports transmit data multiple bits at a time over multiple wires. They are used for scanners and printers. They have a 25-pin model.
- I/O ports can also be classified into two modes: programmed I/O and direct memory access (DMA).
  - Programmed I/O is a mode in which the CPU is directly involved in the I/O operations. The CPU initiates the I/O operation, checks the status of the I/O device, and transfers the data between the memory and the I/O device. Programmed I/O is simple but slow and inefficient.
  - Direct memory access (DMA) is a mode in which a specialized I/O processor takes over control of an I/O operation to move a large block of data. The CPU initiates the I/O operation, but then delegates the task to the DMA controller, which transfers the data between the memory and the I/O device without involving the CPU. DMA is faster and more efficient than programmed I/O.
- Some examples of external I/O interfaces are FireWire and InfiniBand.
  - FireWire is a high-speed serial interface that can connect up to 63 devices. It can support data rates up to 800 megabits per second. It is used for digital video cameras, external hard drives, and other multimedia devices.
  - InfiniBand is a high-performance serial interface that can connect up to 64,000 devices. It can support data rates up to 2.5 gigabits per second per link. It is used for cluster computing, storage area networks, and other high-end applications.