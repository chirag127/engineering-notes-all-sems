### Interrupt Initiated I/O

- Interrupt initiated I/O is a mode of data transfer between the CPU and the I/O devices that uses an interrupt facility and special commands.
- In this mode, the CPU issues an I/O command to the I/O module and then resumes its normal execution of other tasks .
- The I/O module performs the data transfer independently of the CPU and raises an interrupt signal when the data is available or the transfer is completed .
- The CPU responds to the interrupt signal by suspending its current task and executing an interrupt service routine (ISR) that handles the I/O operation .
- The ISR may involve transferring the data between the I/O module and the memory, updating the status of the I/O device, and resuming the interrupted task .
- Interrupt initiated I/O has the advantage of reducing the CPU involvement and idle time in data transfer, as the CPU does not need to poll the I/O device or wait for the data to be ready .
- Interrupt initiated I/O also allows the CPU to handle multiple I/O devices with different speeds and priorities, by using interrupt vectors and priority levels .
- Interrupt vectors are addresses that point to the ISR for each I/O device, and are stored in a table in the memory .
- Priority levels are assigned to the I/O devices and the CPU, such that the interrupt from a higher priority device can be accepted even if the CPU is servicing a lower priority device .
- Interrupt initiated I/O has the disadvantage of increasing the complexity and overhead of the system, as the CPU has to save and restore the context of the interrupted task, and handle multiple interrupt requests and conflicts .
- Interrupt initiated I/O also requires the synchronization and coordination between the CPU and the I/O module, as the CPU has to acknowledge the interrupt and the I/O module has to clear the interrupt signal .

: https://www.studytonight.com/computer-architecture/input-output-organisation
: https://www.geeksforgeeks.org/difference-between-programmed-and-interrupt-initiated-i-o/
: https://binaryterms.com/interrupts-in-computer-architecture.html
: https://www.geeksforgeeks.org/io-interface-interrupt-dma-mode/
: https://www.geeksforgeeks.org/purpose-of-an-interrupt-in-computer-organization/
: https://www.geeksforgeeks.org/priority-interrupts-sw-polling-daisy-chaining/