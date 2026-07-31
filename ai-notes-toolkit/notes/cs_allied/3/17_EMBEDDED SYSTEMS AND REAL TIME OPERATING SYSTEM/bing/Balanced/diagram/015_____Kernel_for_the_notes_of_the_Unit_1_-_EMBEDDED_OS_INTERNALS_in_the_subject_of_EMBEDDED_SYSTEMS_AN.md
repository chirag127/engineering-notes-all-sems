### Kernel for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A kernel is the core component of an operating system that manages the hardware and software resources, provides services for applications, and handles system calls and interrupts  .
- A kernel can be classified into two types: monolithic and modular .
  - A monolithic kernel is a single large program that contains all the core functions of the operating system, such as memory management, process management, file system, device drivers, etc. It runs in a single address space and has direct access to the hardware.
  - A modular kernel is a kernel that consists of several modules that can be dynamically loaded and unloaded as needed. Each module provides a specific functionality, such as a device driver, a file system, a network protocol, etc. The modules communicate with each other and with the core kernel through well-defined interfaces .
- An embedded operating system is a specialized operating system that is designed for embedded systems, which are devices that have limited resources, such as memory, CPU, power, etc. and perform specific functions, such as sensors, controllers, smart phones, etc.
- An embedded operating system has some characteristics that distinguish it from a general-purpose operating system, such as:
  - Real-time performance: An embedded operating system must be able to respond to events and tasks within a specified time limit, otherwise the system may fail or cause damage.
  - Small footprint: An embedded operating system must be able to fit in the limited memory and storage space of the embedded device, and use the minimum amount of CPU and power resources.
  - Reliability and security: An embedded operating system must be able to handle errors and faults gracefully, and protect the system from unauthorized access or malicious attacks.
  - Customizability and scalability: An embedded operating system must be able to adapt to the specific requirements and constraints of the embedded device, and support different hardware platforms and configurations.