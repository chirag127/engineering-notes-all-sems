## Unit 4 - VxWorks / FreeRTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- An RTOS is a software that manages the execution of tasks on a hardware platform, providing services such as scheduling, synchronization, memory management, and interrupt handling.
- VxWorks and FreeRTOS have different features, advantages, and disadvantages, depending on the application and the requirements of the system.

### VxWorks
- VxWorks is a proprietary RTOS developed by Wind River Systems, first released in 1987.
- VxWorks is widely used in aerospace, defense, industrial, and automotive applications, such as the Mars rovers, the Boeing 787, and the Tesla Model S.
- VxWorks supports multiple architectures, such as x86, ARM, PowerPC, MIPS, and RISC-V, and multiple programming languages, such as C, C++, Ada, Java, and Python.
- VxWorks provides a rich set of features, such as:
  - Preemptive, priority-based scheduling with optional round-robin and time-slicing.
  - Inter-process communication mechanisms, such as message queues, semaphores, mutexes, and event flags.
  - Memory management with virtual memory and memory protection schemes, allowing address translation and isolation of tasks.
  - Interrupt latency of less than 10 microseconds, with support for nested interrupts and interrupt prioritization.
  - Networking stack with TCP/IP, UDP, IPv6, SSL, and other protocols.
  - File system with FAT, NFS, and other formats.
  - Graphical user interface with WindML and OpenGL libraries.
  - Security features, such as encryption, authentication, and secure boot.
  - Debugging and testing tools, such as Wind River Workbench, Wind River Simics, and Wind River Helix Virtualization Platform.
- VxWorks has some disadvantages, such as:
  - High cost and licensing fees, requiring a subscription or a per-unit royalty.
  - Complex configuration and customization, requiring a steep learning curve and extensive documentation.
  - Limited compatibility and portability, requiring specific hardware and software platforms and drivers.

### FreeRTOS
- FreeRTOS is a free, open-source RTOS developed by Richard Barry, first released in 2003.
- FreeRTOS is widely used in IoT, medical, consumer, and industrial applications, such as the Amazon Echo, the Fitbit, and the Raspberry Pi.
- FreeRTOS supports multiple architectures, such as x86, ARM, AVR, PIC, and MSP430, and multiple programming languages, such as C, C++, and Rust.
- FreeRTOS provides a simple and portable set of features, such as:
  - Preemptive, priority-based scheduling with optional round-robin and time-slicing.
  - Inter-task communication mechanisms, such as queues, semaphores, mutexes, and event groups.
  - Memory management with static and dynamic allocation, allowing heap and stack allocation of tasks.
  - Interrupt latency of less than 10 microseconds, with support for nested interrupts and interrupt prioritization.
  - Networking stack with TCP/IP, UDP, MQTT, and other protocols.
  - File system with FAT and SPIFFS formats.
  - Graphical user interface with FreeGLUT and LittlevGL libraries.
  - Security features, such as encryption, authentication, and secure boot.
  - Debugging and testing tools, such as FreeRTOS+Trace, FreeRTOS+CLI, and FreeRTOS+Simulator.
- FreeRTOS has some disadvantages, such as:
  - Limited functionality and scalability, requiring additional components and libraries for complex applications.
  - Low reliability and robustness, requiring careful testing and verification of the code and the hardware.
  - Limited support and documentation, relying on the community and the online resources.