### I/O devices

- I/O devices are the hardware components that allow the operating system to interact with the external world, such as users, networks, and storage devices.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc. 
- I/O devices can be classified into two categories: block devices and character devices.
  - Block devices are devices that transfer data in fixed-size blocks, such as disk drives, CD-ROMs, and flash drives. Block devices support random access to any block of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, and serial ports. Character devices do not support random access to data.
- I/O devices are managed by the operating system using three components: I/O hardware, device drivers, and I/O subsystems.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus.
  - Device drivers are the software modules that communicate with the I/O hardware and control the specific functions of each I/O device. Device drivers are usually written by the device manufacturers and loaded by the operating system at boot time or on demand.
  - I/O subsystems are the software components that provide a uniform interface for the device drivers and the rest of the operating system. I/O subsystems handle tasks such as buffering, caching, spooling, scheduling, and error handling. 
- I/O scheduling is the process of deciding which I/O request to serve next from a queue of pending requests. I/O scheduling is used to improve the performance and efficiency of the I/O system by reducing the waiting time, increasing the throughput, and balancing the load among the I/O devices.