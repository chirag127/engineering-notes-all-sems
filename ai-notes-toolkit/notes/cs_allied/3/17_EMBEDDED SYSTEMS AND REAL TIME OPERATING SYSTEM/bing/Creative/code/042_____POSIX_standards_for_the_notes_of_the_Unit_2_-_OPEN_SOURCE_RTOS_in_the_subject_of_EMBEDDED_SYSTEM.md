### POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX stands for Portable Operating System Interface. It is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines a standard operating system interface and environment, including a command interpreter (or “shell”), and common utility programs to support applications portability at the source code level.
- POSIX also defines a standard threading API, known as POSIX threads or pthreads, which enables quicker execution of the software and is widely popular among developers.
- POSIX standards are useful for developing open source RTOS, which are real-time operating systems that have their source code available for anyone to inspect, modify, and enhance.
- Some examples of open source RTOS that implement POSIX standards are FreeRTOS-Plus-POSIX, LynxOS-178, and PX5.
- FreeRTOS-Plus-POSIX implements a small subset of the POSIX threading API and allows existing POSIX compliant applications to be easily ported to FreeRTOS ecosystem.
- LynxOS-178 is a native POSIX, hard real-time partitioning operating system developed and certified to FAA DO-178C DAL A safety standards. It is the only Commercial-off-the-Shelf (COTS) OS to be awarded a Reusable Software Component (RSC) certificate from the FAA for re-usability in DO-178C certification projects.
- PX5 is a new RTOS for real-time multithread scheduling that features a native implementation of the POSIX threads. It provides the pthread API support usually seen in embedded Linux but missing from most RTOSes. It also has a very small footprint of under 1KB.