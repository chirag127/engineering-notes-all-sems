## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer system and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: character devices and block devices.
  - Character devices transfer data one character (or byte) at a time, such as keyboards and terminals.
  - Block devices transfer data in fixed-size blocks, such as disks and tapes.
- I/O operations can be performed in different modes, such as synchronous, asynchronous, buffered, unbuffered, direct, and indirect.
  - Synchronous I/O means that the process that initiates the I/O operation waits until it is completed before resuming execution.
  - Asynchronous I/O means that the process that initiates the I/O operation can continue execution while the I/O operation is in progress.
  - Buffered I/O means that the data transferred between the process and the device is temporarily stored in a buffer (or cache) in memory to improve performance and reduce device access.
  - Unbuffered I/O means that the data transferred between the process and the device is not stored in a buffer, but directly transferred to or from the device.
  - Direct I/O means that the data transferred between the process and the device bypasses the operating system and is handled by the device driver or the hardware controller.
  - Indirect I/O means that the data transferred between the process and the device goes through the operating system, which provides services such as security, protection, and abstraction.
- I/O operations can be performed using different methods, such as polling, interrupt-driven, and direct memory access (DMA).
  - Polling is a method where the CPU repeatedly checks the status of the device to determine when it is ready to perform an I/O operation.
  - Interrupt-driven is a method where the device signals the CPU when it is ready to perform an I/O operation, and the CPU executes an interrupt handler to service the device.
  - DMA is a method where a special hardware controller transfers data between the device and the memory without involving the CPU, and notifies the CPU when the transfer is completed.