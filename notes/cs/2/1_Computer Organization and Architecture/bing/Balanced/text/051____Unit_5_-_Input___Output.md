## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer system and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: character devices and block devices.
  - Character devices transfer data one character (or byte) at a time, such as keyboards and terminals.
  - Block devices transfer data in fixed-size blocks, such as disks and tapes.
- I/O operations can be performed in different modes, such as synchronous, asynchronous, buffered, unbuffered, direct, and indirect.
  - Synchronous I/O means that the process that initiates the I/O operation waits until it is completed before resuming execution.
  - Asynchronous I/O means that the process that initiates the I/O operation can continue execution while the I/O operation is in progress.
  - Buffered I/O means that the data is temporarily stored in a memory buffer before being transferred to or from the device.
  - Unbuffered I/O means that the data is transferred directly to or from the device without using a buffer.
  - Direct I/O means that the data is transferred directly between the device and the user space of the process, bypassing the kernel space.
  - Indirect I/O means that the data is transferred between the device and the kernel space of the process, and then copied to or from the user space.
- I/O operations can be performed using different methods, such as polling, interrupt-driven, DMA, and I/O channels.
  - Polling means that the CPU repeatedly checks the status of the device to determine when it is ready for data transfer.
  - Interrupt-driven means that the device sends a signal to the CPU when it is ready for data transfer, and the CPU executes an interrupt handler to perform the I/O operation.
  - DMA (direct memory access) means that the device can directly access the main memory to transfer data, without involving the CPU.
  - I/O channels are special-purpose processors that can handle I/O operations independently from the CPU, and communicate with the CPU using commands and status signals.