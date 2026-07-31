### Modes of Data Transfer

In the subject of Computer Organization and Architecture, Unit 5 - Input / Output, one of the topics covered is the modes of data transfer. There are three main modes of data transfer:

1. **Programmed I/O:** In this mode, the processor executes a program that includes instructions to transfer data between the memory and the I/O module. The processor repeatedly checks the status of the I/O module until it is ready for data transfer.

2. **Interrupt-driven I/O:** In this mode, the processor issues an I/O command to the I/O module and then continues to execute other instructions. When the I/O module is ready for data transfer, it interrupts the processor, which then suspends its current activity and executes an interrupt service routine to transfer the data.

3. **Direct Memory Access (DMA):** In this mode, the I/O module transfers data directly to or from the memory, without the intervention of the processor. The processor only initiates the transfer by sending the starting address and the number of words to be transferred to the DMA controller.
