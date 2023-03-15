### Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a disk, a keyboard, or a printer  .
- Programmed I/O operations are the result of I/O instructions written in the computer program .
- In programmed I/O, each data transfer is initiated by the CPU, and the CPU is in continuous monitoring of the interface .
- Programmed I/O is also known as polling or busy-waiting I/O, because the CPU has to repeatedly check the status of the device until it is ready for data transfer .
- Programmed I/O is very simple and cheap to implement, but it has some disadvantages :
  - It wastes CPU time and resources by constantly polling the device.
  - It slows down the overall performance of the system, especially if the device is slow or the data transfer is large.
  - It does not allow concurrency or parallelism, as the CPU cannot perform other tasks while waiting for the device.
  - It may introduce hazards or errors if the device status changes unexpectedly or the CPU misses a signal from the device.