# Real Time System

A real time system is a system that has to respond to events or data within a specific time limit. The system must guarantee that the response is correct and timely, otherwise the system may fail or cause undesirable consequences. Real time systems are often used for applications that involve safety, security, or performance-critical tasks, such as industrial control, avionics, robotics, or multimedia.

## Operating System and Functions

An operating system (OS) is a software that manages the hardware and software resources of a computer system. It provides an interface between the user and the system, and between the system and the external devices. The main functions of an operating system are:

- Process management: The OS creates, schedules, and terminates processes, which are units of execution that run programs or applications. The OS also handles inter-process communication and synchronization, and provides mechanisms for concurrency and parallelism.
- Memory management: The OS allocates, deallocates, and protects the main memory and the secondary memory (such as disks) of the system. The OS also implements techniques such as paging, segmentation, and virtual memory to optimize the use of memory and improve the performance of the system.
- Device management: The OS controls the input/output devices (such as keyboards, mice, printers, scanners, etc.) and the communication devices (such as network cards, modems, etc.) of the system. The OS also provides drivers, which are software components that enable the communication between the OS and the devices.
- File management: The OS organizes, stores, and retrieves the files and directories on the secondary memory of the system. The OS also provides file systems, which are data structures and algorithms that define how the files and directories are named, accessed, and manipulated.
- Security and protection: The OS ensures the confidentiality, integrity, and availability of the data and the resources of the system. The OS also enforces policies and mechanisms to prevent unauthorized or malicious access, use, or modification of the system.
- User interface: The OS provides a user interface, which is a way for the user to interact with the system. The user interface can be graphical (such as windows, icons, menus, etc.) or command-line (such as commands, arguments, etc.).

## Real Time Operating System (RTOS)

A real time operating system (RTOS) is a special type of operating system that is designed for real time systems. An RTOS has two key features: predictability and determinism. Predictability means that the RTOS can guarantee that the response time of the system is bounded and known in advance. Determinism means that the RTOS can guarantee that the system will always produce the same output for the same input, regardless of the external conditions or the internal state of the system.

An RTOS differs from a general-purpose operating system (GPOS), such as Windows, Linux, or MacOS, in several aspects, such as:

- Scheduling: An RTOS uses a priority-based preemptive scheduling algorithm, which means that the highest priority task is always executed first, and a lower priority task can be interrupted by a higher priority task at any time. A GPOS uses a time-sharing scheduling algorithm, which means that the tasks are executed in a round-robin fashion, and each task is given a fixed amount of time (called a time slice or a quantum) to run. A GPOS may also use a priority-based scheduling algorithm, but it is not preemptive, which means that a lower priority task can finish its time slice before being interrupted by a higher priority task.
- Latency: An RTOS has a low latency, which means that the time between an event or a data arrival and the system response is short and consistent. A GPOS has a high latency, which means that the time between an event or a data arrival and the system response is long and variable, depending on the system load and the scheduling algorithm.
- Overhead: An RTOS has a low overhead, which means that the resources (such as CPU time, memory space, etc.) consumed by the OS itself are minimal and constant. A GPOS has a high overhead, which means that the resources consumed by the OS itself are significant and variable, depending on the system load and the OS features.
- Functionality: An RTOS has a limited functionality, which means that it provides only the essential services and features that are required for the real time system, such as process management, memory management, device management, and inter-process communication. A GPOS has a rich functionality, which means that it provides many additional services and features that are not required for the real time system, such as file management,