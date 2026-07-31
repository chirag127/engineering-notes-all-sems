### Interrupt Initiated I/O

- Interrupt initiated I/O is a method of data transfer between the CPU and the I/O devices that does not require the CPU to constantly check the status of the I/O devices .
- In this method, the CPU issues a command to the I/O device and then resumes its normal execution of other tasks .
- When the I/O device is ready for data transfer, it sends an interrupt signal to the CPU, which temporarily suspends its current task and transfers the control to an interrupt handler routine  .
- The interrupt handler routine performs the necessary data transfer between the CPU and the I/O device, and then returns the control to the CPU, which resumes its previous task  .
- Interrupt initiated I/O allows the CPU to utilize its time more efficiently, as it does not have to waste cycles in polling the I/O devices or waiting for their readiness  .
- Interrupt initiated I/O also enables the CPU to handle multiple I/O devices simultaneously, by using a priority structure that determines which interrupt request should be serviced first .
- Interrupt initiated I/O requires the CPU to have an interrupt mechanism that can recognize the source and the type of the interrupt, and can save and restore the state of the CPU before and after the interrupt handling  .