## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer system and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: **character devices** and **block devices**.
  - Character devices transfer data one character (or byte) at a time, such as keyboards and terminals.
  - Block devices transfer data in fixed-size blocks, such as disks and tapes.
- I/O operations can be performed in two modes: **synchronous** and **asynchronous**.
  - Synchronous I/O means that the process that initiates the I/O operation waits until it is completed before resuming its execution.
  - Asynchronous I/O means that the process that initiates the I/O operation can continue its execution while the I/O operation is in progress, and is notified when it is completed.
- I/O operations can also be performed in two ways: **programmed I/O** and **interrupt-driven I/O**.
  - Programmed I/O means that the CPU is directly involved in controlling the I/O device and transferring the data, by executing a sequence of instructions that check the status of the device and read or write the data.
  - Interrupt-driven I/O means that the CPU delegates the control of the I/O device to a special hardware unit called an **interrupt controller**, which generates an interrupt signal to the CPU when the device is ready for data transfer. The CPU then executes a special routine called an **interrupt handler** to service the device and transfer the data.
- I/O operations can also be performed by using a technique called **direct memory access (DMA)**, which allows an I/O device to transfer data directly to or from the main memory, without involving the CPU. The CPU only initiates the DMA transfer by specifying the source and destination addresses, the amount of data, and the direction of transfer. The DMA controller then takes over the bus and performs the data transfer, and notifies the CPU when it is done by generating an interrupt.