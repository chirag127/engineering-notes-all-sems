
### Interrupt Initiated I/O

* Interrupts are signals sent to the CPU by hardware or software indicating an event that needs immediate attention. 
* When an interrupt is received, the CPU suspends its current activities and begins executing a special set of instructions called an interrupt service routine (ISR). 
* Interrupts can be used to initiate input/output (I/O) operations. 
* Interrupt-driven I/O is a method of managing I/O operations in which the CPU is interrupted when an I/O device needs service. 
* The CPU then executes the ISR to service the device, allowing the device to operate independently of the CPU. 
* This allows the CPU to perform other tasks while the I/O device is being serviced. 
* The disadvantage of interrupt-driven I/O is that the CPU must wait for the device to signal that it needs service before it can be serviced.