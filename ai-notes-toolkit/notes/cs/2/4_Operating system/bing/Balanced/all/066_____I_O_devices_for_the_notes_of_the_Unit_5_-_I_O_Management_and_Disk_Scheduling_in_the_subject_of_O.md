# I/O Devices

- I/O devices are the hardware components that allow the operating system to interact with the user and other peripherals.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc. 
- I/O devices can be classified into two categories: **block devices** and **character devices**.
  - Block devices are devices that transfer data in fixed-size blocks, such as disk drives, CD-ROMs, etc. They support random access and can store large amounts of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, terminals, etc. They do not support random access and are usually used for interactive input/output.
- I/O devices are managed by the operating system using three components: **I/O hardware**, **device drivers**, and **I/O subsystem**.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus.
  - Device drivers are the software modules that communicate with the I/O hardware and provide a uniform interface to the I/O subsystem. They are responsible for handling device interrupts, initiating data transfers, and controlling device operations.
  - I/O subsystem is the part of the operating system that provides services and interfaces for I/O operations. It includes components such as I/O scheduling, buffering, caching, spooling, device allocation, error handling, etc.