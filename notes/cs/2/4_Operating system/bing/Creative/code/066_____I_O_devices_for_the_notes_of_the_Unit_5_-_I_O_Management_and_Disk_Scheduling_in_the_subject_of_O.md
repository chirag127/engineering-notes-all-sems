# I/O Devices

- I/O devices are the hardware components that allow the operating system to interact with the user and other peripherals.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc.  
- I/O devices can be classified into two categories: block devices and character devices.
  - Block devices store and transfer data in fixed-size blocks, such as disk drives, CD-ROMs, etc.
  - Character devices deal with data one character at a time, such as keyboards, mice, terminals, etc.
- I/O devices can also be classified into two types: input devices and output devices.
  - Input devices are used to provide data and commands to the operating system, such as keyboards, mice, scanners, etc.
  - Output devices are used to display or print the results of the operating system, such as monitors, printers, speakers, etc.
- I/O devices can communicate with the operating system using different methods, such as polling, interrupts, and direct memory access (DMA).
  - Polling is a software technique that uses a program to check the status of devices periodically. The device can be a disk drive or any other peripheral device. 
  - Interrupts are signals sent by the devices to the processor when they need attention. The processor then saves its current state and executes an interrupt handler routine to service the device. 
  - DMA is a hardware technique that allows the devices to transfer data directly to or from the main memory without involving the processor. The processor only initiates the transfer and then resumes its normal execution. 
- I/O devices are managed by the operating system using different components, such as device drivers, device controllers, and I/O schedulers.
  - Device drivers are software modules that provide a uniform interface between the operating system and the device. They hide the details of the device and handle the device-specific operations. 
  - Device controllers are hardware components that control the operation of the device. They have registers to store commands, status, and data. They also generate interrupts to signal the completion of I/O operations. 
  - I/O schedulers are algorithms that decide the order of servicing the I/O requests from different processes. They aim to optimize the performance and efficiency of the I/O system.