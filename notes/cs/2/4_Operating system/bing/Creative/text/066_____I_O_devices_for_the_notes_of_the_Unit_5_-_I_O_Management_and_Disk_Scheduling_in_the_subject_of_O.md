### I/O Devices

- I/O devices are the hardware components that allow the operating system to interact with the user and other peripherals.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc.  
- I/O devices can be classified into two categories: block devices and character devices.
  - Block devices are devices that store or transfer data in fixed-size blocks, such as disk drives, CD-ROMs, flash drives, etc. Block devices support random access to any block of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, terminals, printers, etc. Character devices do not support random access and usually operate in a sequential manner.
- I/O devices are managed by the operating system using three components: I/O hardware, I/O software, and I/O scheduling.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus. 
  - I/O software is the set of programs and modules that handle the I/O operations and provide a uniform interface to the user and application programs. I/O software consists of device drivers, device controllers, device-independent software, user-level I/O software, and system calls. 
  - I/O scheduling is the process of deciding which I/O request to serve next, based on some criteria such as priority, fairness, efficiency, etc. I/O scheduling is used to optimize the performance of the I/O system and avoid deadlock and starvation.