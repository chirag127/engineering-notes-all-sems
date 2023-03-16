# Task Creation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded system is a computer system that is designed for a specific purpose and has limited resources. It usually interacts with the physical world through sensors and actuators.
- A real-time operating system (RTOS) is a software platform that provides predictable and deterministic behavior for embedded systems that have strict timing constraints and high reliability requirements.
- VxWorks and FreeRTOS are two popular RTOSs for embedded systems. They have different features, advantages, and disadvantages.

## VxWorks
- VxWorks is a proprietary RTOS developed by Wind River Systems. It is widely used in mission-critical applications such as aerospace, defense, industrial, medical, and automotive.
- VxWorks is a preemptive, priority-based RTOS that supports multiple scheduling algorithms, such as round-robin, rate-monotonic, and earliest deadline first.
- VxWorks has a modular and scalable architecture that allows users to customize and optimize the kernel, middleware, and libraries according to their needs. It also supports various hardware platforms, such as x86, ARM, PowerPC, and MIPS.
- VxWorks has many security features that address the evolving threats of connected devices, such as secure boot, secure update, secure communication, and secure data storage.
- VxWorks has a modern development environment that supports C, C++, Ada, Python, and Java. It also integrates with various tools, such as Eclipse, Visual Studio, and Wind River Simics.
- VxWorks has a high licensing cost and requires a steep learning curve. It also has limited support for open source software and community resources.

## FreeRTOS
- FreeRTOS is an open source RTOS developed by Richard Barry and maintained by Amazon Web Services. It is widely used in low-cost and low-power applications, such as IoT, consumer electronics, and education.
- FreeRTOS is a cooperative, priority-based RTOS that supports preemptive multitasking with optional time slicing. It also supports tickless operation for low-power modes.
- FreeRTOS has a simple and portable architecture that consists of a small kernel and optional libraries, such as TCP/IP, USB, and file system. It also supports various hardware platforms, such as ARM, AVR, PIC, and MSP430.
- FreeRTOS has basic security features, such as memory protection and stack overflow detection. It also supports secure communication and cloud connectivity through AWS IoT Core and AWS FreeRTOS.
- FreeRTOS has a simple development environment that supports C and C++. It also integrates with various tools, such as FreeRTOS+Trace, FreeRTOS+CLI, and FreeRTOS+IO.
- FreeRTOS has a low licensing cost and requires a moderate learning curve. It also has a large support for open source software and community resources.