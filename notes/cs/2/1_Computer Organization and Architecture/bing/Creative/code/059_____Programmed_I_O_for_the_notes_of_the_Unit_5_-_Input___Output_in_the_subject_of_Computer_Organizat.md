### Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a keyboard, a mouse, a disk, or a network adapter   .
- In programmed I/O, each data transfer is initiated and controlled by an I/O instruction in the CPU .
- The CPU monitors the status of the peripheral device by reading its status flags or registers  .
- The CPU waits for the device to be ready for data transfer, and then reads or writes a data item from or to the device  .
- The CPU repeats this process until the entire data block is transferred  .
- Programmed I/O is simple and inexpensive to implement, but it has some disadvantages  :
  - It consumes a lot of CPU time and cycles, as the CPU has to constantly poll the device status and perform data transfer  .
  - It reduces the CPU performance and throughput, as the CPU cannot execute other instructions while waiting for the device  .
  - It is not suitable for high-speed devices or large data blocks, as the CPU may not be able to keep up with the device or the data rate  .