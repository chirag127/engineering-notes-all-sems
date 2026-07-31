# I/O Devices

- I/O devices are the hardware components that allow the operating system to interact with the external world, such as users, networks, and storage devices.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc. 
- I/O devices can be classified into two categories: **block devices** and **character devices**.
  - Block devices are devices that transfer data in fixed-size blocks, such as disk drives, CD-ROMs, and flash drives. Block devices support random access to any block of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, and serial ports. Character devices do not support random access to data.
- I/O devices are managed by the operating system using three components: **I/O hardware**, **device drivers**, and **I/O subsystems**.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus.
  - Device drivers are the software modules that control the specific I/O devices. They provide a uniform interface to the operating system and hide the details of the device hardware.
  - I/O subsystems are the software components that handle the common tasks of I/O management, such as buffering, caching, spooling, scheduling, and error handling.
- I/O devices can communicate with the processor using three techniques: **polling**, **interrupts**, and **direct memory access (DMA)**.
  - Polling is a software technique that uses a program to check the status of devices. The device can be a disk drive or any other peripheral device. The program loops through a set of status registers, one for each device, to determine which device needs service.
  - Interrupts are a hardware technique that allows a device to signal the processor that it needs service. The device sends an interrupt request to the processor, which suspends its current execution and jumps to a predefined interrupt handler routine. The interrupt handler performs the necessary I/O operations and returns control to the processor.
  - DMA is a hardware technique that allows a device to transfer data directly to or from the main memory, without involving the processor. The device uses a special hardware controller, called a DMA controller, to perform the data transfer. The DMA controller generates an interrupt to the processor when the transfer is complete.