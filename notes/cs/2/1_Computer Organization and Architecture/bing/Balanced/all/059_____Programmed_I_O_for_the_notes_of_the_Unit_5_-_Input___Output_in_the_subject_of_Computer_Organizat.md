# Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a keyboard, a mouse, a disk, or a network adapter   .
- Programmed I/O operations are the result of I/O instructions written in the computer program .
- In programmed I/O, each data transfer is initiated by the CPU, and the CPU is in continuous monitoring of the interface  .
- Programmed I/O is very cheap and easy to implement, but it has some disadvantages:
  - It consumes a lot of CPU time and resources, as the CPU has to wait for the I/O device to be ready and to perform the data transfer   .
  - It is not suitable for high-speed devices, as the CPU may not be able to keep up with the data rate of the device   .
  - It is not scalable, as the number of I/O devices increases, the CPU will have to handle more I/O instructions and polling loops  .
- Programmed I/O can be implemented in two ways: synchronous and asynchronous:
  - In synchronous programmed I/O, the CPU executes an I/O instruction and then waits for the I/O operation to complete before resuming the execution of the program.
  - In asynchronous programmed I/O, the CPU executes an I/O instruction and then continues to execute the program, until it checks the status of the I/O device periodically or receives a signal from the device indicating the completion of the I/O operation.
- Programmed I/O can be improved by using buffering techniques, such as double buffering or circular buffering, which allow the CPU to transfer data to or from a buffer in memory, while the I/O device transfers data to or from another buffer in memory.