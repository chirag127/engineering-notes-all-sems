Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of Kernel for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# Kernel

- The kernel is the core component of an operating system that manages the system resources, such as memory, CPU, devices, processes, and inter-process communication.
- The kernel provides a set of services or system calls to the user applications, such as file operations, process creation and termination, scheduling, synchronization, and communication.
- The kernel also handles the interrupts and exceptions that occur during the execution of the system or the user applications.
- The kernel can be classified into two types: monolithic and microkernel.

## Monolithic Kernel

- A monolithic kernel is a single large program that contains all the functionality of the operating system, such as device drivers, file systems, network protocols, memory management, and process management.
- A monolithic kernel runs in the privileged mode of the CPU, which allows it to access all the hardware resources directly.
- A monolithic kernel has the advantages of high performance, simplicity, and compatibility, but also the disadvantages of low modularity, high complexity, and difficulty in debugging and maintenance.

## Microkernel

- A microkernel is a small program that contains only the essential functionality of the operating system, such as inter-process communication, memory management, and basic scheduling.
- A microkernel runs in the privileged mode of the CPU, but delegates most of the functionality to the user-level processes, called servers, that run in the unprivileged mode of the CPU.
- A microkernel has the advantages of high modularity, low complexity, and ease of debugging and maintenance, but also the disadvantages of low performance, high overhead, and compatibility issues.