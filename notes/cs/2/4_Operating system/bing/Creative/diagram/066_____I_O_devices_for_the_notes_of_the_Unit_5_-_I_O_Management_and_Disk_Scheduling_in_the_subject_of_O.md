### I/O devices

- I/O devices are the hardware components that allow the operating system to interact with the external environment, such as users, networks, and other peripherals.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc. 
- I/O devices can be classified into two categories: **block devices** and **character devices**.
  - Block devices are devices that transfer data in fixed-size blocks, such as disk drives, CD-ROMs, etc. They support random access and can store large amounts of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, terminals, etc. They do not support random access and are usually used for interactive input/output.
- I/O devices are managed by the operating system using three components: **I/O hardware**, **device drivers**, and **I/O subsystem**.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus.
  - Device drivers are the software modules that control the specific I/O devices. They provide a uniform interface to the operating system and hide the details of the device hardware.
  - I/O subsystem is the part of the operating system that handles the I/O requests from the user programs and the device drivers. It provides services such as buffering, caching, spooling, scheduling, etc.
- I/O devices can communicate with the processor using three techniques: **polling**, **interrupts**, and **direct memory access (DMA)**.
  - Polling is a software technique that uses a program to check the status of devices. The device can be a disk drive or any other peripheral device. The program repeatedly reads a status register of the device until it becomes ready for I/O.
  - Interrupts are a hardware technique that allows the device to signal the processor when it is ready for I/O. The device sends an interrupt request to the processor, which suspends the current execution and invokes an interrupt handler to service the device.
  - DMA is a hardware technique that allows the device to transfer data directly to or from the main memory without involving the processor. The device uses a DMA controller to access the memory bus and perform the data transfer.