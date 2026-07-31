## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: character devices and block devices.
  - Character devices transfer data one character at a time, such as keyboards and printers. They are also called serial devices, because they send or receive data in a serial fashion.
  - Block devices transfer data in fixed-size blocks, such as disks and flash drives. They are also called random access devices, because they can access any block of data randomly, without reading or writing the preceding blocks.
- I/O operations can be performed in two modes: synchronous and asynchronous.
  - Synchronous I/O means that the program waits for the I/O operation to complete before continuing its execution. This mode is simple and easy to program, but it can waste CPU time if the I/O operation is slow or blocked.
  - Asynchronous I/O means that the program does not wait for the I/O operation to complete, but instead continues its execution while the I/O operation is performed in the background. This mode is more efficient and responsive, but it requires more complex programming and coordination.
- I/O operations can be handled by different components of the computer system, such as the CPU, the memory, the I/O controller, and the device driver.
  - The CPU is the central processing unit that executes the program instructions and initiates the I/O requests.
  - The memory is the main storage area that holds the program code and data, and acts as a buffer for the I/O data.
  - The I/O controller is a hardware device that controls the communication between the CPU and the I/O device, and performs the actual data transfer.
  - The device driver is a software module that provides an interface between the operating system and the I/O device, and handles the details of the device-specific operations.
- I/O operations can be implemented by different methods, such as polling, interrupt, direct memory access (DMA), and I/O channels.
  - Polling is a method where the CPU repeatedly checks the status of the I/O device to determine whether it is ready for data transfer. This method is simple and easy to implement, but it consumes a lot of CPU time and resources.
  - Interrupt is a method where the I/O device sends a signal to the CPU when it is ready for data transfer, and the CPU suspends its current execution and switches to a special routine to handle the I/O request. This method is more efficient and responsive, but it requires more complex programming and coordination.
  - DMA is a method where the I/O controller directly transfers the data between the I/O device and the memory, without involving the CPU. This method is the most efficient and fast, but it requires a dedicated hardware device and a special memory area.
  - I/O channels are special-purpose processors that handle the I/O operations independently from the CPU, and provide a high-level interface to the I/O devices. This method is the most advanced and flexible, but it requires a complex and expensive hardware system.