# I/O Interface

- The I/O interface is the method that is used to transfer information between internal storage and external I/O devices.
- The I/O interface supports the communication between the CPU and the peripherals connected to the computer system.
- The I/O interface is part of the computer system's I/O architecture, which is its interface to the outside world .
- The I/O interface is designed to provide a systematic means of controlling interaction with the outside world and to provide the operating system with the information it needs to manage I/O activity effectively.
- The I/O interface consists of the following components:
  - I/O bus: The communication link between the CPU, memory and I/O devices.
  - I/O module: The device that controls the data transfer between the I/O bus and the I/O device.
  - I/O device: The external device that provides input or output for the computer system.
- The I/O interface can operate in different modes, such as programmed I/O, interrupt-driven I/O and direct memory access (DMA) I/O.
  - Programmed I/O: The CPU initiates and monitors the data transfer between the memory and the I/O device. The CPU is busy during the entire I/O operation and cannot perform other tasks.
  - Interrupt-driven I/O: The CPU initiates the data transfer between the memory and the I/O device and then resumes other tasks. The I/O device interrupts the CPU when the data transfer is complete or when an error occurs. The CPU then handles the interrupt and completes the I/O operation.
  - Direct memory access (DMA) I/O: The CPU initiates the data transfer between the memory and the I/O device and then resumes other tasks. The I/O device transfers the data directly to or from the memory without involving the CPU. The I/O device interrupts the CPU only when the data transfer is complete or when an error occurs. The CPU then handles the interrupt and completes the I/O operation.