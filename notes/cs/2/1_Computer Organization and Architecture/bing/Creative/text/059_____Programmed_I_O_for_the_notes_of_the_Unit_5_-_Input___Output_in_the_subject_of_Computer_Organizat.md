### Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a disk, a keyboard, a printer, etc.
- Programmed I/O operations are the result of I/O instructions written in the computer program that requests the I/O operation .
- In programmed I/O, each data transfer is initiated and controlled by the CPU. The CPU issues an I/O command to the device and then repeatedly checks the status of the device until the operation is completed.
- Programmed I/O is simple and inexpensive to implement, but it has some disadvantages:
  - It consumes a lot of CPU time and resources, as the CPU has to constantly monitor the device and wait for the data transfer to finish.
  - It limits the data transfer rate, as the CPU can only handle one I/O operation at a time and the device has to match the speed of the CPU.
  - It introduces latency and overhead, as the CPU has to execute multiple instructions for each data transfer and switch between the user program and the I/O program.
- Programmed I/O can be improved by using techniques such as buffering, handshaking, and polling.
  - Buffering is the use of a memory area to temporarily store the data before or after the transfer, to reduce the number of I/O operations and increase the efficiency.
  - Handshaking is the exchange of signals between the CPU and the device to coordinate the data transfer and avoid data loss or corruption.
  - Polling is the process of checking the status of multiple devices in a fixed order, to determine which device is ready for an I/O operation and to serve them accordingly.