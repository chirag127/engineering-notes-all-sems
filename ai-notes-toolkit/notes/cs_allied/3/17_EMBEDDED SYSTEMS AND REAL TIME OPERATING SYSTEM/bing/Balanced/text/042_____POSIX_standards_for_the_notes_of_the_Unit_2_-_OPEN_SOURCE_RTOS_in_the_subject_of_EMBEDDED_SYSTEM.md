### POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX stands for Portable Operating System Interface. It is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines both the system and user-level application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a trademark of the IEEE. POSIX is intended to be used by both application and system developers.
- POSIX.1-2017 is the latest edition of the POSIX standard. It comprises four major components (each in an associated volume):
  - Base Definitions: General terms, concepts, and interfaces common to all volumes of this standard, including utility conventions and C-language header definitions.
  - System Interfaces: Definitions for system services and functions, such as process management, file operations, signals, devices, timers, clocks, threads, synchronization, and memory management.
  - Shell and Utilities: Definitions for a standard command language interpreter (shell) and common utility programs, such as file manipulation, text processing, and system administration.
  - Rationale: Explanations for the contents of the other volumes, including the reasons for certain design choices and the implications for application portability and conformance.
- POSIX also defines real-time extensions and multi-threading in separate volumes. The real-time extensions provide additional interfaces for real-time applications, such as scheduling policies, priority inheritance, timers, message queues, semaphores, shared memory, and asynchronous I/O.
- POSIX-compliant operating systems can run POSIX-compliant applications without modification, as long as the applications do not use any non-standard features or libraries. POSIX-compliant applications can also be ported easily to different POSIX-compliant operating systems, as long as the applications follow the POSIX guidelines and conventions.
- Some examples of open source RTOS that are POSIX-compliant or partially POSIX-compliant are:  
  - FreeRTOS-Plus-POSIX: A small subset of the POSIX threading API implemented for FreeRTOS, a popular RTOS for embedded systems.
  - LynxOS-178: A native POSIX, hard real-time partitioning operating system developed and certified to FAA DO-178C DAL A safety standards for avionics systems.
  - Linux: A widely used open source operating system that supports POSIX.1-2008 and some of the real-time extensions. However, Linux is not a fully real-time operating system, as it does not guarantee deterministic response times for all tasks.