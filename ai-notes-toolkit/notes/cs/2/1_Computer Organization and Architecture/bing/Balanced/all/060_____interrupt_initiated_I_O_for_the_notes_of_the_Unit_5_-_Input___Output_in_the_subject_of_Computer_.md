# Interrupt Initiated I/O

- Interrupt initiated I/O is a method of data transfer between the CPU and the I/O devices that does not require the CPU to constantly check the status of the I/O devices.
- In this method, the CPU issues a command to the I/O device and then resumes its normal execution of other tasks.
- When the I/O device is ready for data transfer, it sends an interrupt signal to the CPU, which temporarily suspends its current task and transfers the control to an interrupt handler routine.
- The interrupt handler routine performs the necessary data transfer between the CPU and the I/O device and then returns the control to the CPU, which resumes its previous task.
- Interrupt initiated I/O improves the efficiency of the CPU by reducing the idle time and allowing the CPU to perform other tasks while the I/O device is busy.
- Interrupt initiated I/O also allows multiple I/O devices to communicate with the CPU in a priority-based manner, such that the interrupt from a higher priority device is serviced before the interrupt from a lower priority device.
- Interrupt initiated I/O requires an interrupt mechanism that consists of the following components:
  - An interrupt request line that connects the I/O device to the CPU and carries the interrupt signal.
  - An interrupt controller that receives the interrupt signals from multiple I/O devices and determines the priority and the source of the interrupt.
  - An interrupt vector that identifies the address of the interrupt handler routine for each I/O device.
  - An interrupt enable flag that allows the CPU to enable or disable the interrupt mechanism.
  - An interrupt service routine that performs the data transfer and other operations related to the interrupting I/O device.