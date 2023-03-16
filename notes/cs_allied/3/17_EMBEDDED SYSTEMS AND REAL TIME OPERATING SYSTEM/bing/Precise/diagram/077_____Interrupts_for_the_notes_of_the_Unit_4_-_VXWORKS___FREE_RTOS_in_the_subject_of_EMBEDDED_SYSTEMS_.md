### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- **Interrupts** are an important aspect of real-time operating systems (RTOS) such as VxWorks and FreeRTOS.
- When using an RTOS, the typical approach for responding to an interrupt involves the RTOS interrupt dispatcher invoking a user-defined interrupt service routine (ISR), which does a minimal amount of work before deferring most processing to another thread such as a task.
- Interrupt routines in RTOS must follow two rules that do not apply to task code: An interrupt routine must not call any RTOS functions that might block. This could block the highest priority task.
- A timer interrupt (the RTOS tick interrupt) increments the tick count with strict temporal accuracy - allowing the real-time kernel to measure time to a resolution of the chosen timer interrupt frequency. Each time the tick count is incremented the real-time kernel must check to see if it is now time to unblock or wake a task.
- While using RTOS, it is very critical to handle interrupt service routines. Because the misuse of interrupts can lead to time constraint issues such as other periodic tasks failing to meet their deadlines. Note: Interrupts have higher priorities than other Tasks.
