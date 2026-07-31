### Interrupt Initiated I/O

Interrupt Initiated I/O is a mode of data transfer between the CPU and an I/O device. This mode uses an interrupt facility and special commands to inform the interface to issue the interrupt command when data becomes available and the interface is ready for the data transfer. In the meantime, the CPU keeps on executing other tasks and need not check for the flag.

In contrast to programmed I/O, where the CPU stays in the program loop until the I/O unit indicates that it is ready for data transfer, interrupt initiated I/O is less time-consuming as it does not keep the CPU busy needlessly.

When there is an I/O request available, the CPU is immediately notified using interrupts, and the request is immediately handled using an interrupt service routine. The use of DMA (Direct Memory Access) allows interrupt-driven I/O to be used. Otherwise, a system must use programmed I/O if DMA is not available.