# Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, routers, smart TVs, etc. 
- Embedded Linux systems consist of the following main components: 
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It is responsible for initializing the hardware, loading the Linux kernel, and passing the kernel parameters.
  - Linux Kernel: The core of the operating system that manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system calls and drivers for the user applications to interact with the hardware.
  - Device Tree: A data structure that describes the hardware configuration and properties of the embedded system. It is used by the Linux kernel to initialize and configure the devices.
  - Root File System: A collection of files and directories that provide the basic functionality and environment for the user applications. It contains the system configuration files, libraries, binaries, etc.
  - Configuration Files: Files that store the settings and preferences of the system and the user applications. They can be modified to customize the behavior and appearance of the system.
- Embedded Linux systems have some advantages over other operating systems for embedded applications, such as:  
  - Open-source: Linux is free and open-source, which means that anyone can access, modify, and distribute the source code. This allows for more flexibility, customization, and innovation in the development process.
  - Scalability: Linux can run on a wide range of hardware platforms, from low-end microcontrollers to high-end servers. It can also be configured and optimized to meet the specific requirements and constraints of the embedded system, such as memory footprint, performance, power consumption, etc.
  - Developer Support: Linux has a large and active community of developers and users who contribute to the development and improvement of the kernel and the user applications. There are also many online resources, such as documentation, tutorials, forums, etc., that provide guidance and assistance for the developers.
  - Tooling: Linux offers a rich set of tools and frameworks for the development, testing, debugging, and deployment of the embedded system. Some of these tools include cross-compilers, debuggers, profilers, emulators, etc.