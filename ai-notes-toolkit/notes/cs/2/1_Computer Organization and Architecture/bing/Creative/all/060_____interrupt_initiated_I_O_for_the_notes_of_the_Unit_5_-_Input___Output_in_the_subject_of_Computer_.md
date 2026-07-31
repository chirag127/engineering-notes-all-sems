# Interrupt Initiated I/O

- Interrupt initiated I/O is a mode of data transfer between the CPU and the I/O devices that uses an interrupt facility and special commands.
- In this mode, the CPU issues an I/O command to the I/O module and then resumes its normal execution of other tasks.
- The I/O module performs the data transfer independently of the CPU and raises an interrupt signal when the data is ready or the transfer is complete.
- The CPU responds to the interrupt by saving its current state and executing an interrupt service routine (ISR) that handles the I/O operation.
- The ISR may read or write the data from or to the I/O module, acknowledge the interrupt, and restore the CPU state to resume the normal execution.
- Interrupt initiated I/O has the following advantages over programmed I/O:
  - It reduces the CPU involvement and overhead in the I/O process.
  - It allows the CPU to perform other tasks while the I/O module is busy with the data transfer.
  - It improves the performance and efficiency of the system by avoiding the wastage of CPU cycles in polling or looping.
- Interrupt initiated I/O has the following challenges and limitations:
  - It requires a mechanism to identify the source and type of the interrupt, which may be done by using interrupt vectors or priority levels.
  - It requires a mechanism to handle multiple or simultaneous interrupts, which may be done by using interrupt masking or nesting.
  - It may cause latency or delay in the CPU response to the interrupt, which may affect the real-time or critical applications.
  - It may still involve the CPU in the data transfer if the I/O module does not have a direct memory access (DMA) capability.