## Unit 1 - EMBEDDED OS INTERNALS

An embedded operating system is a specialized OS for use in the computers built into larger systems. An embedded system is a computer system with a dedicated function within a larger mechanical or electrical system, often with real-time computing constraints.

1. **Real-time operating systems (RTOS)**: An RTOS is an operating system intended to serve real-time applications that process data as it comes in, typically without buffer delays. The main objective of an RTOS is to manage the resources of the computer so that a particular operation executes in precisely the same amount of time, every time it occurs.

2. **Memory management**: Memory management is the process of controlling and coordinating computer memory, assigning portions called blocks to various running programs to optimize overall system performance.

3. **Process management**: Process management is an integral part of any modern-day operating system (OS). The OS must allocate resources to processes, enable processes to share and exchange information, protect the resources of each process from other processes, and enable synchronization among processes.

4. **Device drivers**: A device driver is a computer program that operates or controls a particular type of device that is attached to a computer. A driver provides a software interface to hardware devices, enabling operating systems and other computer programs to access hardware functions without needing to know precise details about the hardware being used.

5. **File systems**: A file system is a method and data structure that an operating system uses to control how data is stored and retrieved. Without a file system, information placed in a storage medium would be one large body of data with no way to tell where one piece of information stops and the next begins.

6. **Interrupt handling**: An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention. An interrupt alerts the processor to a high-priority condition requiring the interruption of the current code the processor is executing. The processor responds by suspending its current activities, saving its state, and executing a function called an interrupt handler to deal with the event.

7. **Multitasking**: Multitasking is the concurrent execution of multiple tasks (also known as processes) over a certain period of time. New tasks can interrupt already started ones before they finish, instead of waiting for them to end. As a result, a computer executes segments of multiple tasks in an interleaved manner, while the tasks share common processing resources such as central processing units (CPUs) and main memory.

8. **Inter-process communication (IPC)**: Inter-process communication (IPC) is a set of programming interfaces that allow a programmer to coordinate activities among different program processes that can run concurrently in an operating system. This allows a program to handle many user requests at the same time.

9. **Bootloaders**: A bootloader is a computer program that loads an operating system (OS) or runtime environment for the computer after completion of the power-on self-tests (POST); it is the loader for the operating system itself. Within the hard reboot process, it runs after completion of the self-tests performed by the BIOS, and before the operating system itself starts.

10. **Power management**: Power management is a feature of some electrical appliances, especially copiers, computers, GPUs, and computer peripherals such as monitors and printers, that turns off the power or switches the system to a low-power state when inactive. In computing, this is known as PC power management and is built around a standard called ACPI. This supersedes APM. All recent (consumer) computers have ACPI support.