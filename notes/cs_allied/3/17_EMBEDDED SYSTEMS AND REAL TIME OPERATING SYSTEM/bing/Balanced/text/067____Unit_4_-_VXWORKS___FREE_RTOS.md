## Unit 4 - VXWORKS / FREE RTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- An RTOS is a software that manages the execution of tasks on a processor, ensuring that they meet their deadlines and priorities.
- VxWorks and FreeRTOS have different features, advantages, and disadvantages that make them suitable for different applications and scenarios.

### VxWorks

- VxWorks is a commercial RTOS developed by Wind River Systems, Inc. since 1987.
- VxWorks is widely used in aerospace, defense, industrial, medical, and automotive domains, as well as in NASA's Mars rovers and SpaceX's rockets.
- VxWorks supports various architectures, such as x86, ARM, PowerPC, MIPS, and RISC-V, and provides a rich set of features, such as:

  - Preemptive, priority-based scheduling with optional round-robin time slicing.
  - Symmetric multiprocessing (SMP) and asymmetric multiprocessing (AMP) modes for multicore processors.
  - Inter-process communication (IPC) mechanisms, such as message queues, semaphores, mutexes, events, pipes, and shared memory.
  - Memory management, including dynamic memory allocation, memory protection, and virtual memory.
  - File system, network stack, device drivers, and security features.
  - POSIX compatibility and support for various programming languages, such as C, C++, Ada, Java, and Python.
  - Integrated development environment (IDE) and debugging tools.

- Some of the advantages of VxWorks are:

  - High performance, reliability, and scalability.
  - Wide range of supported platforms and devices.
  - Comprehensive documentation and technical support.
  - Compliance with various industry standards and certifications, such as DO-178B/C, IEC 61508, ISO 26262, and Common Criteria.

- Some of the disadvantages of VxWorks are:

  - High cost and licensing fees.
  - Proprietary and closed-source code.
  - Complexity and steep learning curve.

### FreeRTOS

- FreeRTOS is a free and open-source RTOS developed by Richard Barry since 2003 and maintained by Amazon Web Services (AWS) since 2017.
- FreeRTOS is designed to be simple, portable, and lightweight, and is widely used in education, hobby, and low-cost embedded projects, as well as in some commercial products.
- FreeRTOS supports various architectures, such as x86, ARM, AVR, PIC, MSP430, and RISC-V, and provides a basic set of features, such as:

  - Preemptive, priority-based scheduling with optional co-operative and hybrid modes.
  - Inter-task communication and synchronization mechanisms, such as queues, semaphores, mutexes, and software timers.
  - Static and dynamic memory allocation with optional memory protection.
  - Modular and configurable kernel design with optional extensions, such as file system, network stack, USB support, and security features.
  - Support for various programming languages, such as C, C++, Rust, and Assembly.
  - Debugging and tracing tools.

- Some of the advantages of FreeRTOS are:

  - Free and open-source code with permissive MIT license.
  - Simplicity and ease of use.
  - Portability and flexibility.
  - Large and active community and online resources.

- Some of the disadvantages of FreeRTOS are:

  - Limited performance, functionality, and scalability.
  - Lack of official documentation and technical support.
  - Non-compliance with industry standards and certifications.