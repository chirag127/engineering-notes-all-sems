# Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, set-top boxes, smart TVs, routers, etc. 
- Embedded Linux is built on the same Linux kernel, available from kernel.org, as all Linux systems, but it has some specific features and constraints that make it different from enterprise or desktop systems.
- The main components of embedded Linux systems are:
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It initializes the hardware, loads the Linux kernel into memory, and passes some parameters to the kernel.
  - Linux Kernel: The core of the OS that manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system calls and drivers for the user applications to interact with the hardware.
  - Device Tree: A data structure that describes the hardware configuration and properties of the embedded system. It is used by the Linux kernel to initialize and configure the devices.
  - Root File systems: A collection of files and directories that provide the basic functionality and environment for the user applications. It contains the system configuration files, libraries, binaries, etc.
  - Configuration files: Files that store the settings and preferences of the embedded system, such as network, display, security, etc. They are usually located in the /etc directory of the root file system.
- Some of the advantages of using Linux for embedded applications are :
  - Open-source: Linux is free and open-source, which means that developers can access the source code, modify it, and distribute it as they wish. This also enables a large and active community of developers and users who contribute to the improvement and support of Linux.
  - Scalability: Linux can run on a wide range of hardware platforms, from low-end microcontrollers to high-end servers. It can also be customized and optimized for specific embedded applications and requirements, such as memory footprint, performance, security, etc.
  - Developer support: Linux provides a rich set of development tools and frameworks, such as compilers, debuggers, libraries, IDEs, etc. that facilitate the creation and testing of embedded applications. It also supports many programming languages, such as C, C++, Python, Java, etc.
  - Tooling: Linux offers many tools and utilities that help in the management and maintenance of embedded systems, such as bootloaders, file systems, configuration tools, package managers, etc. It also supports various protocols and standards, such as TCP/IP, USB, Bluetooth, etc.