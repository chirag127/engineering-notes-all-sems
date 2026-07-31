### Modes of Data Transfer

Data transfer is the process of moving data between the internal storage and the external input/output (I/O) devices of a computer system. Data transfer can be handled in one of three possible modes:

- **Programmed I/O**: In this mode, the CPU executes I/O instructions written in the computer program to initiate and control each data item transfer. The CPU monitors the status of the I/O device and waits for the device to be ready before transferring the data. This mode is simple but inefficient, as it wastes CPU time and slows down the program execution.
- **Interrupt-initiated I/O**: In this mode, the CPU executes I/O instructions written in the computer program to initiate the data transfer, but does not wait for the device to be ready. Instead, the CPU proceeds to execute other tasks and the I/O device sends an interrupt signal to the CPU when it is ready to transfer the data. The CPU then suspends the current task and handles the data transfer. This mode is more efficient than programmed I/O, as it allows the CPU to perform other operations while the I/O device is busy.
- **Direct memory access (DMA)**: In this mode, the CPU does not execute any I/O instructions to initiate or control the data transfer. Instead, the CPU delegates the data transfer to a special hardware device called the DMA controller, which communicates directly with the I/O device and the memory unit. The CPU only supplies the DMA controller with the starting address and the number of words to be transferred, and then proceeds to execute other tasks. The DMA controller transfers the data in blocks or bursts, and sends an interrupt signal to the CPU when the transfer is complete. This mode is the most efficient of all, as it frees the CPU from any involvement in the data transfer.

The following diagram illustrates the three modes of data transfer:

![Diagram of modes of data transfer](https://image.slidesharecdn.com/modesofdatatransfer-140929011823-phpapp02/95/modes-of-data-transfer-8-638.jpg?cb=1411958365)

: https://upscfever.com/upsc-fever/en/gatecse/en-gatecse-chp164.html
: https://www.slideshare.net/ShahIshtiyaqMehfooze/modes-of-data-transfer