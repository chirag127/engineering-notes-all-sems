# Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, set-top boxes, smart TVs, routers, etc. 
- Embedded Linux is built on the same Linux kernel, available from kernel.org, as all Linux systems, but it has some modifications and adaptations to meet the specific requirements and constraints of embedded systems, such as higher reliability, security, performance, resource availability, and long-term support.
- The main components of an embedded Linux system are:
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It initializes the hardware, loads the Linux kernel into memory, and passes some parameters to the kernel.
  - Linux Kernel: The core of the Linux system, which manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system services, such as process management, file system, networking, etc.
  - Device Tree: A data structure that describes the hardware configuration and properties of the embedded system. It is used by the Linux kernel to initialize and communicate with the devices.
  - Root File System: A collection of files and directories that contain the user applications, libraries, configuration files, and other data that are needed for the Linux system to run. It can be stored in different types of media, such as flash memory, SD card, hard disk, etc.
  - Configuration Files: Files that store the settings and preferences of the Linux system and the user applications. They can be edited to customize the behavior and appearance of the system.