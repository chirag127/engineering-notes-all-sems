# Overview of POSIX APIs

- POSIX stands for **Portable Operating System Interface**. It is a family of standards specified by **IEEE** for maintaining compatibility among operating systems.
- POSIX defines both the **system** and **user-level** application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a **trademark** of the IEEE. POSIX is intended to be used by both application and system developers.
- The POSIX API subset is an increasingly popular OSAL (operating system abstraction layer) for IoT and embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX.
- Benefits of POSIX support in embedded systems include:
  - Offering a familiar API to non-embedded programmers, especially from Linux
  - Enabling the use of existing, mature, and tested libraries
  - Reducing the learning curve and development time
  - Facilitating code reuse among different platforms
- The POSIX standard consists of several parts, each with a different number and name. For example, POSIX.1 defines the core services, POSIX.2 defines the shell and utilities, POSIX.4 defines real-time extensions, and so on.
- The C POSIX library is a specification of a C standard library for POSIX systems. It was developed at the same time as the ANSI C standard. Some effort was made to make POSIX compatible with standard C; POSIX includes additional functions to those introduced in standard C.
- The C POSIX library header files are prefixed with **unistd.h** and provide access to various POSIX functions, such as file operations, process management, signals, timers, threads, etc.
- References:
  - : https://docs.zephyrproject.org/latest/services/portability/posix.html
  - : https://codedocs.org/what-is/posix
  - : https://en.wikipedia.org/wiki/POSIX
  - : https://www.baeldung.com/linux/posix
  - : https://en.wikipedia.org/wiki/C_POSIX_library