# I/O Ports

- I/O ports are the interfaces between the CPU and the external devices, such as keyboards, monitors, printers, scanners, etc.
- I/O ports allow data to be transferred between the internal storage and the external I/O devices.
- I/O ports are controlled by I/O modules, which are special hardware components that supervise and synchronize all I/O operations.
- I/O modules perform the following functions:
  - Control and timing: coordinate the flow of traffic between internal resources and external devices.
  - Communication with the CPU: receive commands and report status.
  - Communication with the device: send commands and receive status.
  - Data buffering: store data temporarily to compensate for the speed difference between the CPU and the device.
  - Error detection: check for errors in the data or the device.
- There are different types of I/O ports, such as serial ports, parallel ports, USB ports, etc.
  - Serial ports: used for external modems and older computer mouse. Data travels one bit at a time. Two versions: 9-pin and 25-pin. Data rate: 115 kilobits per second.
  - Parallel ports: used for scanners and printers. Data travels eight bits at a time. One version: 25-pin. Data rate: 150 kilobytes per second.
  - USB ports: used for various devices, such as keyboards, mice, cameras, flash drives, etc. Data travels in packets. Two versions: USB 2.0 and USB 3.0. Data rate: up to 480 megabits per second for USB 2.0 and up to 5 gigabits per second for USB 3.0.
- There are different methods of I/O operations, such as programmed I/O, interrupt-driven I/O, and direct memory access (DMA).
  - Programmed I/O: the CPU executes a program that instructs the I/O module to perform an I/O operation. The CPU waits for the I/O module to complete the operation and then resumes the program.
  - Interrupt-driven I/O: the CPU executes a program that instructs the I/O module to perform an I/O operation and then continues with another program. The I/O module interrupts the CPU when the operation is completed and then the CPU resumes the original program.
  - DMA: the CPU instructs a specialized I/O processor to perform an I/O operation and then continues with another program. The I/O processor transfers a large block of data directly between the memory and the device without involving the CPU. The I/O processor interrupts the CPU when the operation is completed and then the CPU resumes the original program.