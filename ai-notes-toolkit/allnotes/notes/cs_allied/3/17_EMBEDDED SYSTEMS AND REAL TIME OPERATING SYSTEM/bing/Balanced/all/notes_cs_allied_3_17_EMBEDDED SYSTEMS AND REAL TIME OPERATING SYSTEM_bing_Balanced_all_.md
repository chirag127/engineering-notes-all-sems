

# EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded system is a computer system that is designed to perform a specific function within a larger system or device. Embedded systems typically have limited resources, such as memory, processing power, and input/output capabilities. Embedded systems are often used in applications that require high reliability, performance, and efficiency, such as automotive, industrial, medical, and consumer electronics.
- A real-time operating system (RTOS) is a type of operating system that is specialized for embedded systems that operate in real-time environments. A real-time environment is one where the system must respond to events or stimuli within a predictable and bounded time frame, otherwise the system may fail or cause undesirable consequences. For example, a pacemaker, a flight control system, or a robotic arm are examples of real-time embedded systems that use RTOSes.
- An RTOS is different from a general-purpose operating system (GPOS) in several ways. Some of the main differences are:

  - An RTOS has a deterministic and preemptive scheduler that assigns priorities to tasks and executes them according to their deadlines. A GPOS has a non-deterministic and cooperative scheduler that may not guarantee timely execution of tasks.
  - An RTOS has a minimal and modular kernel that provides only the essential services and features for real-time applications, such as task management, synchronization, communication, and interrupt handling. A GPOS has a large and complex kernel that provides many additional services and features, such as file system, networking, graphics, and security.
  - An RTOS has a low and fixed overhead for system calls and context switches, which reduces the latency and jitter of the system. A GPOS has a high and variable overhead for system calls and context switches, which increases the latency and jitter of the system.
  - An RTOS has a small and static memory footprint that can fit in the limited memory of embedded systems. A GPOS has a large and dynamic memory footprint that may require external memory or virtual memory.

- Some of the benefits of using an RTOS for real-time embedded systems are:

  - An RTOS can improve the performance, reliability, and safety of the system by ensuring that the critical tasks are executed within their deadlines and that the system can handle unexpected events or faults.
  - An RTOS can simplify the design, development, and testing of the system by providing a standard and consistent interface and abstraction for the hardware and software components of the system.
  - An RTOS can facilitate the portability and scalability of the system by allowing the system to run on different hardware platforms and architectures and to support different numbers and types of tasks.

- Some of the challenges of using an RTOS for real-time embedded systems are:

  - An RTOS may introduce some limitations and constraints on the system, such as the maximum number of tasks, the minimum task period, the maximum interrupt latency, and the minimum stack size.
  - An RTOS may require some trade-offs and optimizations on the system, such as the choice of scheduling algorithm, the allocation of resources, the partitioning of tasks, and the synchronization of data.
  - An RTOS may increase the complexity and cost of the system, such as the need for additional hardware support, the licensing and maintenance fees, the learning curve and training, and the debugging and verification tools.

- Some of the examples of RTOSes that are commonly used for real-time embedded systems are:

  - FreeRTOS: An open-source and cross-platform RTOS that supports various microcontrollers and architectures. It provides a simple and lightweight kernel that supports preemptive and cooperative multitasking, inter-task communication, and software timers.
  - VxWorks: A proprietary and commercial RTOS that supports various processors and platforms. It provides a comprehensive and robust kernel that supports preemptive and priority-based multitasking, inter-process communication, memory management, file system, networking, and graphics.
  - QNX: A proprietary and commercial RTOS that supports various processors and platforms. It provides a microkernel architecture that supports modular and distributed multitasking, message passing, fault tolerance, security, and real-time performance.



## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system is a computer operating system designed for use in embedded computer systems .
- Embedded computer systems are devices that are installed as built-in components of a wider system, in which they serve a special, functional purpose.
- Examples of embedded computer systems are smart TVs, digital cameras, smart watches, routers, medical devices, etc.
- An embedded operating system is engineered and optimized to improve the efficiency of controlling the hardware resources, drive graphics processing, and decrease response time for the tasks performed by the device.
- An embedded operating system is also designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications.
- An embedded operating system is essentially the brain of an embedded computer system, which defines the functionality of a product.
- An embedded operating system is a combination of software and hardware. It produces an easily understandable result by humans in many formats such as images, text, and voice.
- Embedded operating systems are developed with programming code, which helps convert hardware languages into software languages like C and C++.
- An embedded operating system achieves these functions via a kernel that includes, at a minimum: process management, memory management, and I/O system management components.
- Process management is the function of creating, scheduling, and terminating processes or threads that execute the application code.
- Memory management is the function of allocating, deallocating, and protecting the memory space used by the processes, the kernel, and the device drivers.
- I/O system management is the function of interfacing with the hardware devices, such as sensors, actuators, displays, keyboards, etc., and providing services for data transfer, device control, and error handling.
- An embedded operating system may also include other components, such as file system, network stack, security, graphics, etc., depending on the requirements and features of the embedded device.
- An embedded operating system aims to perform with certainty specific task(s) regularly that help the device operate.
- How the OS fits into an embedded system depends on the architecture and design of the system, which can be classified into three types: monolithic, microkernel, and hybrid.
- A monolithic architecture is one where the OS and the application code are tightly coupled and run in the same address space. This architecture is simple, fast, and efficient, but also prone to errors, security risks, and difficult to maintain and update.
- A microkernel architecture is one where the OS is divided into a minimal kernel that provides the basic services, and a set of modules that run in separate address spaces and provide the additional services. This architecture is modular, flexible, and secure, but also complex, slow, and resource-intensive.
- A hybrid architecture is one where the OS combines the features of both monolithic and microkernel architectures, and allows the developer to choose the best trade-off between performance and reliability.



# Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, routers, smart TVs, etc. 
- Embedded Linux systems consist of the following main components: 
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It is responsible for initializing the hardware, loading the Linux kernel, and passing the kernel parameters.
  - Linux Kernel: The core of the operating system that manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system calls and drivers for the user applications to interact with the hardware.
  - Device Tree: A data structure that describes the hardware configuration and properties of the embedded system. It is used by the Linux kernel to initialize and configure the devices.
  - Root File System: A collection of files and directories that provide the basic functionality and environment for the user applications. It contains the system configuration files, libraries, binaries, etc.
  - Configuration Files: Files that store the settings and preferences of the system and the user applications. They can be modified to customize the behavior and appearance of the system.
- Embedded Linux systems have some advantages over other operating systems for embedded applications, such as:  
  - Open-source: Linux is free and open-source, which means that anyone can access, modify, and distribute the source code. This allows for more flexibility, customization, and innovation in the development process.
  - Scalability: Linux can run on a wide range of hardware platforms, from low-end microcontrollers to high-end servers. It can also be configured and optimized to meet the specific requirements and constraints of the embedded system, such as memory footprint, performance, power consumption, etc.
  - Developer Support: Linux has a large and active community of developers and users who contribute to the development and improvement of the kernel and the user applications. There are also many online resources, such as documentation, tutorials, forums, etc., that provide guidance and assistance for the developers.
  - Tooling: Linux offers a rich set of tools and frameworks for the development, testing, debugging, and deployment of the embedded system. Some of these tools include cross-compilers, debuggers, profilers, emulators, etc.



# Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the embedded operating system (EOS) manages and views other software in the embedded system  .
- A process is a unit of execution that has its own state, memory, and resources .
- A process can be in one of the following states: ready, running, waiting, or terminated .
- A process can communicate with other processes through interprocess communication (IPC) mechanisms, such as message passing, shared memory, or semaphores .
- A process can synchronize with other processes through mutual exclusion, critical sections, or monitors .
- A process can be created, suspended, resumed, or killed by the EOS or by another process .
- A process can be assigned a priority, which determines its order of execution by the EOS scheduler .
- A process can be preempted by a higher-priority process or by an interrupt .
- An interrupt is a signal from a hardware device or a software event that causes the EOS to temporarily suspend the current process and execute an interrupt handler  .
- An interrupt handler is a special type of process that performs a specific task related to the interrupt source and then returns control to the previous process .
- An error is an unexpected or abnormal condition that occurs during the execution of a process and may cause the process to fail or behave incorrectly .
- An error handler is a special type of process that detects, reports, and recovers from errors .
- Process management in embedded systems is challenging because of the limited resources, real-time constraints, and complex interactions with the physical world .
- Process management in embedded systems requires careful design, implementation, and testing of the EOS and the application software .



# File Management

File management is the process of manipulating files in a computer system, such as creating, modifying, deleting, and organizing them into folders. Files are collections of data that are stored on a device or a storage system, such as flash memory, RAM, or hard disk. File management is important for embedded systems because it allows the system to access, store, and manage the data that is needed for its operation and functionality.

Some of the tasks performed by file management in an operating system are:

- Creating and deleting files and directories
- Opening and closing files
- Reading and writing data to and from files
- Moving and copying files and directories
- Renaming and modifying attributes of files and directories
- Searching and sorting files and directories
- Providing security and protection for files and directories
- Providing an interface for users and applications to access files and directories

Some of the challenges and requirements for file management in embedded systems are :

- Reliability: The file system should be able to handle power failures, system crashes, and hardware errors without losing or corrupting data.
- Fail-safety: The file system should be able to recover from failures and restore the data to a consistent state.
- Data integrity: The file system should be able to ensure that the data is not modified or corrupted by unauthorized or malicious actions.
- Performance: The file system should be able to provide fast and efficient access to data, especially for real-time applications.
- Certifiability: The file system should be able to comply with the standards and regulations for safety-critical embedded systems, such as automotive, aerospace, and medical devices.
- Compatibility: The file system should be able to support different types of devices, storage systems, and operating systems, and allow interoperability with other systems and platforms.

Some of the examples of file systems that are designed for embedded systems are :

- FAT (File Allocation Table): A simple and widely used file system that supports different types of devices and operating systems, but has limitations in reliability, performance, and security.
- NTFS (New Technology File System): A more advanced and secure file system that supports features such as encryption, compression, and journaling, but has higher complexity and overhead, and may not be compatible with some embedded systems.
- TxF (Transactional File System): A file system that provides transactional semantics for file operations, ensuring atomicity, consistency, isolation, and durability, but has higher memory and CPU requirements, and may not be suitable for real-time applications.
- Reliance Edge: A transactional file system that is specifically designed for embedded systems, providing fail-safety, data integrity, and certifiability, but has lower performance and compatibility than FAT or NTFS.



# Memory Management

Memory management is the process of allocating and deallocating memory resources to programs and processes in an efficient and effective way. Memory management is essential for embedded systems, which have limited and constrained memory resources. Memory management can affect the performance, reliability, and functionality of embedded systems.

Some of the topics related to memory management in embedded systems are:

- **Memory types**: Embedded systems typically use different types of memory, such as static random access memory (SRAM), dynamic random access memory (DRAM), flash memory, and read-only memory (ROM). Each type of memory has its own characteristics, such as speed, cost, size, volatility, and endurance. Embedded systems designers need to choose the appropriate memory type for their application requirements and constraints.
- **Memory pools**: Memory pools are a technique of managing dynamic memory allocation in embedded systems. A memory pool allocates a fixed number of fixed-sized blocks of memory that can be used by the application. Memory pools can reduce memory fragmentation, overhead, and complexity, but they also limit the flexibility and scalability of memory allocation.
- **Memory mapping**: Memory mapping is a technique of mapping a logical address space to a physical address space. Memory mapping can enable a program to use a large virtual address space that exceeds the physical memory size. Memory mapping can also provide memory protection, isolation, and sharing among different processes and tasks.
- **Memory management unit (MMU)**: An MMU is a hardware device that performs memory mapping and translation. An MMU can support features such as paging, segmentation, caching, and memory access control. An MMU can improve the performance, security, and functionality of embedded systems, but it also introduces complexity, overhead, and compatibility issues.
- **Memory management in operating systems**: Operating systems provide memory management services to applications and processes, such as memory allocation, deallocation, protection, and sharing. Operating systems can use different memory management schemes, such as fixed partitioning, variable partitioning, paging, segmentation, or hybrid schemes. Operating systems can also use different memory allocation algorithms, such as first fit, best fit, worst fit, or buddy system.



# I/O Management

- I/O management is the process of controlling the input and output devices of an embedded system.
- I/O devices can be classified into two types: character devices and block devices.
  - Character devices transfer data one byte at a time, such as keyboards, mice, serial ports, etc.
  - Block devices transfer data in fixed-size blocks, such as disks, flash memory, etc.
- I/O management involves the following tasks:
  - Device driver development: A device driver is a software module that interacts with a specific device and provides a uniform interface to the operating system.
  - Device driver registration: A device driver must register itself with the operating system and provide information about its capabilities, such as device name, device type, device number, etc.
  - Device file creation: A device file is a special file that represents a device in the file system. It allows applications to access devices using standard file operations, such as open, read, write, close, etc.
  - Device file access: A device file can be accessed by applications using system calls, such as open, read, write, close, etc. The operating system forwards these calls to the corresponding device driver, which performs the actual I/O operations on the device.
  - Device file management: A device file can be created, deleted, renamed, moved, etc. using file system commands, such as mkdir, rm, mv, etc. The operating system maintains the mapping between device files and device drivers.
  - Device file protection: A device file can have permissions, such as read, write, execute, etc. that control the access rights of different users and groups. The operating system enforces these permissions using access control mechanisms, such as user IDs, group IDs, etc.
  - Device file synchronization: A device file can be synchronized with the device to ensure data consistency and integrity. The operating system provides synchronization mechanisms, such as buffers, caches, locks, etc. to coordinate the access of multiple processes to the same device.



# Overview of POSIX APIs

- POSIX stands for **Portable Operating System Interface** . It is a family of standards specified by **IEEE** for maintaining compatibility among operating systems.
- POSIX defines both the **system** and **user-level** application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a **trademark** of the IEEE. POSIX is intended to be used by both application and system developers.
- POSIX APIs are an increasingly popular OSAL (operating system abstraction layer) for IoT and embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX. Benefits of POSIX support in Zephyr include:
  - Offering a familiar API to non-embedded programmers, especially from Linux.
  - Enabling the use of existing libraries and middleware that use POSIX APIs.
  - Reducing the learning curve and development time for new applications.
- POSIX APIs can be divided into several categories, such as:
  - Process control: APIs for creating, terminating, and synchronizing processes, such as fork, exec, wait, and pthread.
  - File and directory operations: APIs for manipulating files and directories, such as open, close, read, write, and mkdir.
  - Input and output: APIs for performing input and output operations, such as printf, scanf, and fprintf.
  - Device control: APIs for controlling devices, such as ioctl, tcsetattr, and tcgetattr.
  - Signals: APIs for handling signals, such as signal, sigaction, and sigprocmask.
  - Timers: APIs for measuring and setting time, such as clock, time, and alarm.
  - Interprocess communication: APIs for communicating between processes, such as pipe, socket, and message queue.
  - Memory management: APIs for allocating and freeing memory, such as malloc, free, and mmap.
  - Threads: APIs for creating and managing threads, such as pthread_create, pthread_join, and pthread_mutex.
  - Sockets: APIs for creating and using sockets, such as socket, bind, listen, and accept.
  - System information: APIs for obtaining system information, such as uname, sysconf, and gethostname.
- POSIX APIs are defined in various **headers** that are included in the C POSIX library. Some of the common headers are:
  - stdio.h: for input and output operations.
  - stdlib.h: for memory management and general utilities.
  - unistd.h: for file and directory operations and process control.
  - signal.h: for signal handling.
  - time.h: for timers and time-related functions.
  - pthread.h: for threads and synchronization.
  - sys/types.h: for basic data types and system types.
  - sys/stat.h: for file status and mode information.
  - sys/socket.h: for sockets and network communication.
  - sys/utsname.h: for system information.



# Threads - Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread is also known as a lightweight process that shares the same memory and resources as the program that created it.
- Threads can improve the performance and responsiveness of a program by dividing the workload among multiple execution units.
- Threads can also enable a program to take advantage of multiprocessor or multicore systems by running different threads on different cores or processors.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the program itself (user-level threads).
- The operating system provides system calls or APIs to create, terminate, suspend, resume, join, and synchronize threads.
- The program can also use libraries or frameworks that provide thread abstraction and management, such as POSIX threads (pthreads), Java threads, or Qt threads.
- The thread creation process involves allocating memory and resources for the thread, initializing the thread attributes and state, assigning a unique identifier and a priority to the thread, and adding the thread to the ready queue or the scheduler.
- The thread creation process may vary depending on the operating system, the programming language, and the thread library or framework used.
- The thread creation process may also involve specifying the function or the code segment that the thread will execute, the arguments or parameters that the thread will receive, and the options or flags that the thread will follow.
- The thread creation process may have some overhead or cost in terms of memory, CPU time, and system calls, which may affect the performance and scalability of the program.
- The thread creation process may also have some challenges or limitations in terms of security, portability, compatibility, and error handling, which may affect the reliability and robustness of the program.



Hello, I am Sydney, your AI assistant. I can help you with writing the notes for the topic of Cancellation for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM. Here is the content in markdown format:

# Cancellation

- Cancellation is the process of terminating a task or an operation before it is completed.
- Cancellation can be used to free up system resources, improve responsiveness, or handle errors and exceptions.
- Cancellation can be performed by the task itself, by another task, or by the operating system.
- Cancellation can be synchronous or asynchronous, depending on whether the task waits for the confirmation of the cancellation or not.
- Cancellation can be cooperative or preemptive, depending on whether the task checks for the cancellation request or not.
- Cancellation can be graceful or abrupt, depending on whether the task performs any cleanup or finalization actions or not.

## Types of Cancellation

- Synchronous cancellation: The task that requests the cancellation waits for the confirmation of the cancellation from the task that is being cancelled. This ensures that the cancelled task has completed its cleanup and finalization actions. However, this can cause delays and deadlocks if the cancelled task does not respond to the cancellation request or is blocked by another task.
- Asynchronous cancellation: The task that requests the cancellation does not wait for the confirmation of the cancellation from the task that is being cancelled. This allows the requesting task to continue its execution without delays. However, this can cause inconsistency and resource leaks if the cancelled task does not perform its cleanup and finalization actions.
- Cooperative cancellation: The task that is being cancelled checks for the cancellation request periodically or at certain points in its execution. This allows the task to perform its cleanup and finalization actions before terminating. However, this requires the task to be designed with cancellation in mind and to use cancellation points or cancellation tokens.
- Preemptive cancellation: The task that is being cancelled does not check for the cancellation request and is terminated by the operating system or another task. This allows the cancellation to be performed without the cooperation of the task. However, this can cause inconsistency and resource leaks if the task does not perform its cleanup and finalization actions.
- Graceful cancellation: The task that is being cancelled performs its cleanup and finalization actions before terminating. This ensures that the task releases any resources it has acquired, closes any files it has opened, and notifies any other tasks it has interacted with. However, this can cause delays and complexity in the task design and implementation.
- Abrupt cancellation: The task that is being cancelled does not perform its cleanup and finalization actions and is terminated immediately. This ensures that the cancellation is performed quickly and simply. However, this can cause inconsistency and resource leaks if the task does not release any resources it has acquired, close any files it has opened, or notify any other tasks it has interacted with.

## Cancellation Scenarios

- User-initiated cancellation: The user requests the cancellation of a task or an operation through a user interface element, such as a button, a menu, or a keyboard shortcut. This can be used to abort a long-running or unwanted task or operation, or to change the user's preferences or inputs.
- System-initiated cancellation: The system requests the cancellation of a task or an operation due to an error, an exception, a resource constraint, or a priority change. This can be used to handle failures, recover from faults, optimize performance, or enforce policies.
- Task-initiated cancellation: The task requests the cancellation of itself or another task due to a logical condition, a dependency, or a result. This can be used to implement conditional execution, synchronization, or coordination among tasks.



# POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same address space, file descriptors, stack, and other attributes, but have their own **thread ID**, **registers**, **stack pointer**, **priority**, **signal mask**, and **errno** variable.
- Threads can communicate with each other using **shared memory**, **mutexes**, **condition variables**, and **semaphores**.
- Threads can be created, joined, detached, canceled, and synchronized using the functions defined in the **pthread.h** header file.
- POSIX also defines a standard threading library API which is supported by most modern operating systems.



# Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions  .
- Processes can communicate with each other through both shared memory and message passing.
- Semaphores are counters which allow multiple threads or processes to synchronize by allocating or releasing resources .
- Semaphores can be used for both intra-process and inter-process communication.
- Semaphores can be implemented in two ways: binary semaphores and counting semaphores.
- Binary semaphores can have only two values: 0 or 1, and are used to implement mutual exclusion or critical sections.
- Counting semaphores can have any non-negative integer value, and are used to implement resource allocation or producer-consumer problems.
- To perform synchronization using semaphores, following are the steps:
  - Step 1: Create a semaphore or connect to an already existing semaphore (semget())
  - Step 2: Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
  - Step 3: Perform control operations on the semaphore i.e., set or get attributes or remove the semaphore (semctl())
- Semaphores are useful for inter-process communication because they provide a simple and efficient way of coordinating multiple processes that share common resources or data  .



# Pipes

Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner. Pipes are often used in embedded systems to pass simple messages between tasks or commands. Pipes have the following characteristics:

- A pipe is a channel with two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order.
- A pipe can be either named or unnamed. A named pipe has a unique identifier in the file system and can be accessed by any process that knows its name. An unnamed pipe is created by the system call `pipe` and can only be accessed by the processes that share it.
- A pipe can be either blocking or non-blocking. A blocking pipe waits until data is available or the pipe is closed before returning from a read or write operation. A non-blocking pipe returns immediately with an error code if data is not available or the pipe is full.
- A pipe can be either unidirectional or bidirectional. A unidirectional pipe only allows data to flow in one direction, from the write end to the read end. A bidirectional pipe allows data to flow in both directions, but requires two pipes to be created and connected.
- A pipe can be either synchronous or asynchronous. A synchronous pipe ensures that the data written to the pipe is delivered to the read end without loss or corruption. An asynchronous pipe does not guarantee the delivery or integrity of the data, but may offer higher performance or lower latency.

Some of the advantages of using pipes in embedded systems are:

- Pipes are simple and easy to use, requiring only basic system calls or library functions to create, open, close, read, and write.
- Pipes are portable and widely supported by various operating systems and platforms, such as Unix, Linux, Windows, and Nucleus SE.
- Pipes are flexible and can be combined with other IPC methods, such as message queues, mailboxes, signals, or sockets, to create complex communication schemes.

Some of the disadvantages of using pipes in embedded systems are:

- Pipes have limited capacity and buffer size, which may cause data loss or blocking if the pipe is full or empty. The capacity and buffer size of pipes depend on the operating system and the hardware configuration, and may not be adjustable by the user.
- Pipes have limited functionality and features, such as error handling, security, priority, or synchronization. Pipes do not provide any mechanism to detect or recover from errors, such as broken pipes, invalid data, or interrupted operations. Pipes do not provide any access control or encryption to protect the data from unauthorized or malicious access. Pipes do not provide any way to assign different priorities or deadlines to the data or the processes. Pipes do not provide any way to synchronize the data or the processes, such as waiting for a specific event or condition.
- Pipes have limited scalability and performance, especially for large or complex data or processes. Pipes may incur high overhead or latency due to the system calls, context switches, or data copying involved in the communication. Pipes may not be suitable for real-time or concurrent applications that require high throughput, low latency, or deterministic behavior.



# FIFO for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- FIFO stands for First In, First Out, a method for organizing the manipulation of a data structure (often, specifically a data buffer) where the oldest (first) entry, or "head" of the queue, is processed first.
- FIFO is a common technique for implementing data buffers in embedded systems, where data is transferred between different components or processes at different rates or with different timing requirements .
- FIFO can be implemented using hardware or software, depending on the application and the performance requirements. Hardware FIFOs are typically implemented using registers, flip-flops, or memory cells, while software FIFOs are implemented using arrays, linked lists, or circular buffers  .
- FIFO has several advantages for embedded systems, such as:
  - It can decouple the writing and reading systems, allowing them to operate at different speeds or with different timing constraints. This can improve the throughput and efficiency of the data transfer.
  - It can provide a simple and consistent interface for the data producer and consumer, abstracting away the details of the underlying implementation and reducing the complexity of the software or hardware design .
  - It can buffer the data in case of temporary overflows or underflows, preventing data loss or corruption. This can enhance the reliability and robustness of the system .
- FIFO has some limitations and challenges for embedded systems, such as:
  - It requires additional memory or hardware resources to store the data and manage the pointers or counters. This can increase the cost and power consumption of the system .
  - It can introduce latency and jitter in the data transfer, depending on the size and occupancy of the buffer and the frequency and variability of the writing and reading operations. This can affect the quality of service and the real-time performance of the system .
  - It can cause data coherency issues if the data is modified or accessed by multiple processes or components. This can lead to data inconsistency or race conditions, requiring synchronization mechanisms or protocols to ensure data integrity .



# Shared Memory

- Shared memory is a method of interprocess communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing, because it does not involve copying data or system calls.
- Shared memory can be implemented in different ways, such as:
  - Using a special system call (e.g., `shmget` in Linux) to create and attach a shared memory segment to the address space of a process.
  - Using memory-mapped files (e.g., `mmap` in Linux) to map a file or a device to the address space of a process, and then share the mapping with other processes.
  - Using a shared memory object (e.g., `shm_open` in POSIX) to create and open a named shared memory region that can be accessed by multiple processes.
- Shared memory can also be classified into two types, depending on the scope of sharing:
  - Local shared memory: The shared memory region is accessible only by processes on the same processor or the same multicore processor. This type of shared memory is usually implemented by hardware, such as caches or registers.
  - Distributed shared memory: The shared memory region is accessible by processes on different processors or different multicore processors. This type of shared memory is usually implemented by software, such as protocols or middleware, that provide the illusion of a single memory space.
- Shared memory has some advantages and disadvantages, such as:
  - Advantages:
    - High performance and low overhead.
    - Simple and natural programming model.
    - Flexible and dynamic allocation and deallocation of shared memory regions.
  - Disadvantages:
    - Potential for data inconsistency and race conditions.
    - Lack of protection and security mechanisms.
    - Difficulty in scaling and portability.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of Kernel for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# Kernel

- A kernel is the core component of an operating system that manages the system resources, such as memory, CPU, I/O devices, etc.
- A kernel provides the basic services and abstractions for the applications and the user interface, such as process management, file system, device drivers, inter-process communication, etc.
- A kernel can be classified into two types: monolithic and microkernel.

## Monolithic Kernel

- A monolithic kernel is a single large program that contains all the operating system functions and runs in a single address space.
- A monolithic kernel has the advantages of high performance, simplicity, and compatibility with legacy systems.
- A monolithic kernel has the disadvantages of low modularity, high complexity, and difficulty in debugging and maintenance.

## Microkernel

- A microkernel is a small program that provides only the essential services, such as memory management, process scheduling, and inter-process communication, and runs in a separate address space from the rest of the operating system.
- A microkernel has the advantages of high modularity, low complexity, and ease of debugging and maintenance.
- A microkernel has the disadvantages of low performance, high overhead, and compatibility issues with legacy systems.

## Embedded OS Kernel

- An embedded OS kernel is a specialized kernel that is designed for embedded systems, which are devices that have limited resources, such as memory, CPU, power, etc., and perform specific functions, such as sensors, controllers, etc.
- An embedded OS kernel has the following characteristics:
  - Small size: An embedded OS kernel should have a small memory footprint and code size to fit in the limited memory of the embedded device.
  - Real-time: An embedded OS kernel should provide real-time services, such as predictable and deterministic response time, priority-based scheduling, interrupt handling, etc., to meet the timing constraints of the embedded application.
  - Reliability: An embedded OS kernel should provide reliability services, such as fault tolerance, error detection and recovery, etc., to ensure the correct and continuous operation of the embedded device.
  - Configurability: An embedded OS kernel should provide configurability services, such as customization, scalability, portability, etc., to adapt to the diverse and changing requirements of the embedded device.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the structure for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

# Unit 1 - EMBEDDED OS INTERNALS

- Introduction
  - Define embedded systems and real-time operating systems (RTOS)
  - Explain the characteristics and challenges of embedded systems and RTOS
  - List the components and functions of an embedded OS
  - Compare and contrast different types of embedded OS, such as monolithic, microkernel, exokernel, etc.
- Process Management
  - Define processes, threads, and tasks in the context of embedded OS
  - Explain the process life cycle and state transitions
  - Describe the process scheduling algorithms and policies for embedded OS, such as priority-based, round-robin, earliest deadline first, etc.
  - Discuss the inter-process communication and synchronization mechanisms for embedded OS, such as message passing, shared memory, semaphores, mutexes, etc.
  - Analyze the performance and trade-offs of different process management techniques for embedded OS
- Memory Management
  - Define memory hierarchy and memory allocation methods for embedded OS
  - Explain the concepts of virtual memory, paging, and segmentation for embedded OS
  - Describe the memory management techniques and policies for embedded OS, such as static, dynamic, garbage collection, etc.
  - Discuss the memory protection and security mechanisms for embedded OS, such as memory mapping, access control, encryption, etc.
  - Analyze the performance and trade-offs of different memory management techniques for embedded OS
- Device Management
  - Define devices and device drivers in the context of embedded OS
  - Explain the device classification and characteristics for embedded OS, such as character, block, network, etc.
  - Describe the device management techniques and policies for embedded OS, such as polling, interrupt, direct memory access, etc.
  - Discuss the device communication and coordination mechanisms for embedded OS, such as serial, parallel, bus, etc.
  - Analyze the performance and trade-offs of different device management techniques for embedded OS
- File System
  - Define files and file systems in the context of embedded OS
  - Explain the file system structure and organization for embedded OS, such as hierarchical, flat, network, etc.
  - Describe the file system operations and services for embedded OS, such as create, delete, read, write, etc.
  - Discuss the file system reliability and consistency mechanisms for embedded OS, such as backup, recovery, journaling, etc.
  - Analyze the performance and trade-offs of different file system techniques for embedded OS
- Case Studies
  - Select and describe one or more examples of embedded OS, such as Linux, Windows CE, Android, iOS, etc.
  - Explain the design and implementation details of the selected embedded OS, such as architecture, kernel, modules, etc.
  - Evaluate the strengths and weaknesses of the selected embedded OS, such as functionality, performance, scalability, security, etc.
  - Compare and contrast the selected embedded OS with other embedded OS, such as features, compatibility, market share, etc.



# Kernel Module Programming

- Kernel module programming is a way of extending the functionality of the kernel without modifying the kernel source code or recompiling the kernel.
- Kernel modules are object files that contain code that can be loaded into or unloaded from the kernel at runtime.
- Kernel modules are useful for implementing device drivers, file systems, network protocols, system calls, and other features that are not part of the core kernel.
- Kernel modules must have at least two functions: a start (initialization) function called `init_module()` and an end (cleanup) function called `cleanup_module()`.
- Kernel modules can use kernel functions and data structures, but they must follow certain rules and conventions to avoid conflicts and errors.
- Kernel modules can communicate with each other and with user space programs through various mechanisms, such as system calls, ioctl, procfs, sysfs, netlink, etc.
- Kernel modules can be written in C or assembly language, and they must be compiled with the same compiler and flags as the kernel.
- Kernel modules can be loaded into the kernel using the `insmod` command, and unloaded from the kernel using the `rmmod` command.
- Kernel modules can be managed and configured using the `modprobe` command, which can also handle dependencies and parameters.
- Kernel modules can be debugged using tools such as `printk`, `kdb`, `kgdb`, `kprobes`, etc.



# Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is the software that determines which task should be run next by the processor in an embedded system.
- A scheduling algorithm is the logic and the mechanism that decides when the scheduler should be run and how to allocate the processor time among the tasks.
- Scheduling is a crucial aspect of embedded systems, especially for real-time systems that need to meet deadlines and ensure system stability.
- There are different types of schedulers and scheduling algorithms, depending on the system requirements, the task characteristics, and the design trade-offs.
- Some of the common types of schedulers are:

  - Time Slice (TS) Scheduler: This scheduler divides the time into slots and assigns each task a slot to execute. The tasks are executed in a round-robin fashion, meaning that each task gets a turn to run for the duration of its slot. This scheduler is simple and fair, but it does not consider the priority or the deadline of the tasks.
  - Priority Scheduler: This scheduler assigns a priority level to each task and runs the task with the highest priority at any given time. The priority can be static (fixed at design time) or dynamic (changing at run time). This scheduler can improve the responsiveness and the performance of the system, but it may also cause starvation (a situation where a low-priority task never gets to run) or priority inversion (a situation where a high-priority task is blocked by a low-priority task).
  - Composite Scheduler: This scheduler combines the features of the TS and the priority schedulers. It can use a priority-based algorithm to select a group of tasks to run, and then use a TS algorithm to run the tasks within the group. This scheduler can balance the advantages and disadvantages of the TS and the priority schedulers.

- Some of the common types of scheduling algorithms are:

  - Preemptive Scheduling: This algorithm allows the scheduler to interrupt the execution of a task and switch to another task, if the new task has a higher priority or a shorter deadline. This algorithm can improve the responsiveness and the timeliness of the system, but it also increases the overhead and the complexity of the scheduler.
  - Non-Preemptive Scheduling: This algorithm does not allow the scheduler to interrupt the execution of a task, unless the task voluntarily yields the processor or completes its execution. The scheduler can only select a new task when the current task is finished or suspended. This algorithm reduces the overhead and the complexity of the scheduler, but it also reduces the responsiveness and the timeliness of the system.
  - Cooperative Scheduling: This algorithm relies on the tasks to cooperate with the scheduler and yield the processor when they are idle or waiting for an event. The scheduler can only select a new task when the current task yields the processor. This algorithm is simple and efficient, but it also requires the tasks to be well-designed and well-behaved.

- Scheduling is a trade-off between the system performance, the system complexity, and the system predictability. Different schedulers and scheduling algorithms have different strengths and weaknesses, and the choice of the best scheduler and scheduling algorithm depends on the system requirements, the task characteristics, and the design constraints.



# Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals

Scheduling is the process of allocating CPU time to different tasks or processes in an embedded system. Scheduling can affect the performance, responsiveness, and predictability of the system. There are different types of scheduling algorithms that can be used in embedded systems, depending on the requirements and constraints of the system. Some of the common types of scheduling are:

- **Non-preemptive scheduling**: In this type of scheduling, the CPU executes a task until it completes or voluntarily relinquishes the CPU. The task cannot be interrupted by a higher priority task. This type of scheduling is simple and easy to implement, but it can cause long delays and poor responsiveness for some tasks. Non-preemptive scheduling is suitable for systems that do not have strict timing constraints or real-time requirements.

- **Preemptive scheduling**: In this type of scheduling, the CPU can interrupt a task to execute a higher priority task. The interrupted task is resumed later when the CPU is available. This type of scheduling can improve the responsiveness and predictability of the system, but it can also introduce overhead and complexity. Preemptive scheduling requires mechanisms to handle critical sections, synchronization, and communication among tasks. Preemptive scheduling is suitable for systems that have real-time requirements and need to meet deadlines .

- **Round-robin scheduling**: This is a special case of preemptive scheduling, where all the tasks have the same priority and are executed in a circular order. Each task is given a fixed amount of CPU time, called a time slice or a quantum, and then the CPU switches to the next task in the queue. This type of scheduling can provide fairness and balance among tasks, but it can also cause frequent context switches and poor performance for some tasks. Round-robin scheduling is suitable for systems that have multiple tasks with similar characteristics and importance .

- **Time slice scheduling**: This is a variation of round-robin scheduling, where the tasks have different priorities and are executed in a priority-based order. Each task is given a time slice proportional to its priority, and then the CPU switches to the next task in the queue. This type of scheduling can provide a trade-off between priority and fairness, but it can also cause starvation and poor performance for some tasks. Time slice scheduling is suitable for systems that have multiple tasks with different characteristics and importance.

- **Priority scheduling**: This is a type of preemptive scheduling, where the tasks have different priorities and are executed in a priority-based order. The CPU always executes the highest priority task that is ready to run, and preempts any lower priority task. This type of scheduling can provide fast response and predictability for high priority tasks, but it can also cause starvation and poor performance for low priority tasks. Priority scheduling is suitable for systems that have real-time requirements and need to meet deadlines .

- **Composite scheduling**: This is a type of scheduling that combines different scheduling algorithms to achieve the best results for the system. For example, a system can use priority scheduling for real-time tasks and round-robin scheduling for non-real-time tasks, or use time slice scheduling for high priority tasks and non-preemptive scheduling for low priority tasks. Composite scheduling can provide flexibility and adaptability for the system, but it can also increase the complexity and overhead of the system. Composite scheduling is suitable for systems that have diverse and dynamic requirements and constraints.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Interfacing for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# Interfacing

- Interfacing is the process of connecting and communicating between different hardware and software components in an embedded system.
- Interfacing can be classified into two types: internal and external.
- Internal interfacing refers to the communication between the processor and the memory, peripherals, and other devices on the same board or chip.
- External interfacing refers to the communication between the embedded system and the external devices, such as sensors, actuators, displays, keyboards, etc.
- Interfacing can be done using various methods, such as parallel, serial, analog, digital, wired, wireless, etc.
- Interfacing can also be done using various protocols, such as SPI, I2C, UART, USB, CAN, Ethernet, Bluetooth, Wi-Fi, etc.
- Interfacing requires the use of appropriate hardware and software components, such as connectors, cables, drivers, libraries, APIs, etc.
- Interfacing can affect the performance, reliability, security, and power consumption of the embedded system, depending on the choice of the method, protocol, and components.
- Interfacing can also pose some challenges, such as compatibility, scalability, synchronization, error handling, etc.



# Serial for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a combination of software and hardware that is designed to perform a specific task or function with reliability and efficiency .
- An embedded operating system is usually a real-time operating system that can respond to events or inputs within a predictable and bounded time.
- An embedded operating system consists of a kernel and optional components such as device drivers, libraries, middleware, and applications .
- The kernel is the core of the embedded operating system that provides the basic services such as process management, memory management, and I/O system management.
- Process management is the function of the kernel that creates, schedules, and terminates processes or threads that execute the application code.
- Memory management is the function of the kernel that allocates, deallocates, and protects the memory space for the processes, the kernel, and the device drivers.
- I/O system management is the function of the kernel that handles the communication between the processes and the external devices such as sensors, actuators, and network interfaces.
- Device drivers are the software modules that interface with the hardware devices and provide a uniform and abstract access to the I/O system management.
- Libraries are the software modules that provide common and reusable functions such as mathematical operations, string manipulation, and data structures.
- Middleware is the software layer that provides higher-level services and protocols such as networking, database, graphics, and security.
- Applications are the software modules that implement the specific functionality and logic of the embedded system.
- Embedded operating systems differ from general-purpose operating systems by their optimized design, which aims to reduce the resource consumption, increase the performance, and ensure the reliability and predictability of the system .
- Embedded operating systems are often tailored to the specific hardware and software requirements of the embedded system, which may involve customizing or modifying the kernel, the device drivers, the libraries, the middleware, and the applications .
- Embedded operating systems are used in a wide range of embedded devices and systems, such as smartphones, smart watches, smart TVs, industrial controllers, automotive systems, medical devices, and aerospace systems .



# Parallel Computing for Embedded Systems

- Parallel computing is a type of computation in which many calculations or processes are carried out simultaneously.
- Parallel computing can improve the performance, efficiency, and scalability of embedded systems, which are devices that have a dedicated function and are part of a larger system.
- Parallel computing can be achieved by using multiple processors, cores, or threads in a single device, or by using a network of devices that communicate and cooperate to solve a computational problem .
- Parallel computing can be classified into different forms, such as bit-level, instruction-level, data, and task parallelism.
  - Bit-level parallelism: increasing the size of the processor word, which allows more bits to be processed in a single instruction.
  - Instruction-level parallelism: executing multiple instructions simultaneously or out of order within a single processor or core.
  - Data parallelism: distributing the same operation or task to multiple processors or cores, each working on a different subset of the data.
  - Task parallelism: assigning different operations or tasks to different processors or cores, each working on a different part of the problem.
- Parallel computing can be implemented by using different architectures, such as symmetric multiprocessor (SMP), massively parallel processor (MPP), parallel vector processor (PVP), distributed shared memory (DSM), and cluster of workstations (COW).
  - SMP: a system with multiple processors or cores that share the same memory and bus.
  - MPP: a system with a large number of processors or cores, each with its own memory and bus, connected by a network .
  - PVP: a system with one or more processors or cores that can execute vector operations on multiple data elements in parallel.
  - DSM: a system with multiple processors or cores that share a distributed memory, accessed by a common address space.
  - COW: a system with multiple workstations or devices, each with its own processor, memory, and bus, connected by a network.
- Parallel computing can be applied to various domains and applications of embedded systems, such as image processing, signal processing, machine learning, robotics, and control systems .
- Parallel computing can pose some challenges and limitations for embedded systems, such as synchronization, communication, load balancing, scalability, power consumption, and debugging .



# Interrupt Handling

- Interrupts are signals that alter the normal flow of execution of a program by the processor.
- Interrupts can be generated by hardware devices (such as timers, buttons, serial ports, etc.) or by software instructions (such as system calls, exceptions, etc.).
- Interrupts are useful for handling asynchronous events that require immediate attention or for performing periodic tasks without polling .
- Interrupts can be classified into two types: maskable and non-maskable.
  - Maskable interrupts can be disabled or enabled by the processor using special instructions or registers.
  - Non-maskable interrupts cannot be disabled and have the highest priority.
- Interrupts can be handled by two methods: vectored and non-vectored.
  - Vectored interrupts have a predefined address in memory where the interrupt service routine (ISR) is located.
  - Non-vectored interrupts require the processor to fetch the address of the ISR from an external device or memory location.
- Interrupt handling involves the following steps :
  - The processor detects the interrupt request signal after completing the current instruction.
  - The processor saves the current context (such as program counter, stack pointer, registers, flags, etc.) on the stack or in a special memory area .
  - The processor jumps to the ISR address, either from a predefined vector table or from an external source .
  - The ISR performs the necessary actions to service the interrupt, such as reading or writing data, clearing the interrupt flag, etc. .
  - The ISR returns control to the processor by executing a return from interrupt instruction .
  - The processor restores the saved context and resumes the execution of the interrupted program .
- Interrupt handling can be affected by several factors, such as priority, latency, nesting, sharing, etc. .
  - Priority determines the order in which interrupts are serviced when multiple interrupts occur simultaneously .
  - Latency is the time delay between the occurrence of an interrupt and the execution of the ISR .
  - Nesting is the ability to interrupt an ISR by a higher priority interrupt .
  - Sharing is the situation where multiple devices use the same interrupt line or vector .
- Interrupt handling is an essential feature of embedded systems, as it allows the processor to respond to external events in a timely and efficient manner   .
- Interrupt handling requires careful design and implementation, as it can affect the performance, reliability, and correctness of the system .



# Linux Device Drivers for Embedded Systems

Linux device drivers are software modules that enable the communication between the Linux kernel and the hardware devices. They provide the critical link between applications and IoT devices themselves. In this unit, we will learn about the following topics:

- The components of an embedded Linux system and their roles
- The types and categories of Linux device drivers and their interfaces
- The methods of discovering and configuring the hardware devices
- The steps of writing a kernel device driver and loading it into the system
- The pin control subsystem and its usage in embedded systems

## Components of an Embedded Linux System

An embedded Linux system consists of the following components:

- A Bootloader (U-Boot): This is a small program that runs before the Linux kernel and initializes the hardware, loads the kernel image from a storage device, and passes some parameters to the kernel.
- The Linux kernel: This is the core of the Linux system that manages the hardware resources, provides system services, and implements the device drivers.
- System call interface: This is the interface between the user space applications and the kernel space services. It allows the applications to request the kernel to perform certain operations, such as opening a file, sending a signal, or accessing a device.
- A C-runtime library (libc): This is a library that provides the basic functions and data types for the C programming language, such as memory allocation, string manipulation, and input/output operations.
- System shared libraries: These are libraries that provide additional functionality and services for the applications, such as networking, graphics, or multimedia.
- The Root filesystem: This is the file system that contains the essential files and directories for the Linux system, such as /bin, /etc, /lib, /usr, and /dev. It can be stored in various types of storage devices, such as flash memory, SD card, or hard disk.

## Types and Categories of Linux Device Drivers

In Linux, there are three main types of device driver :

- Character: This is for an unbuffered I/O with a rich range of functions and a thin layer between the application code and the driver. It is the first choice when implementing custom device drivers.
- Block: This has an interface tailored for block I/O to and from mass storage devices, such as hard disks, flash memory, or CD-ROMs. It has a buffer cache mechanism that improves the performance and reliability of the I/O operations.
- Network: This is for network devices, such as Ethernet cards, wireless adapters, or modems. It has a packet-based interface that handles the transmission and reception of network data.

Each type of device driver has a specific interface that defines the operations and data structures that the driver must implement. For example, a character device driver must implement the file_operations structure, which contains pointers to functions that handle the open, read, write, close, and ioctl operations.

Linux device drivers can also be categorized into two groups based on their location in the system:

- Built-in drivers: These are drivers that are compiled into the kernel image and loaded into the memory when the kernel boots. They are usually for essential devices that are required for the system to function, such as serial ports, timers, or interrupt controllers.
- Loadable drivers: These are drivers that are compiled as separate modules and can be loaded into and unloaded from the kernel memory dynamically. They are usually for optional or removable devices that are not always present or needed, such as USB devices, sound cards, or cameras.

Loadable drivers have some advantages over built-in drivers, such as saving memory space, reducing kernel size, and allowing updates without recompiling the kernel. However, they also have some disadvantages, such as requiring a module loader program, depending on the kernel version and configuration, and having less security and stability.

## Methods of Discovering and Configuring the Hardware Devices

In order to communicate with the hardware devices, the Linux kernel must first discover and configure them. There are two main methods of doing this:

- Static configuration: This is when the kernel has the information about the hardware devices and their parameters hardcoded in the source code or the configuration files. This method is simple and fast, but it is not flexible and scalable. It is suitable for embedded systems that have a fixed and known hardware configuration.
- Dynamic configuration: This is when the kernel probes the hardware devices and obtains their information and parameters from the devices themselves or from external sources, such as device trees or firmware. This method is more complex and slow, but it is more flexible and scalable. It is suitable for embedded systems



# Characteristics of Embedded Operating Systems

- An embedded operating system is a computer operating system designed for use in embedded computer systems.
- Embedded operating systems are designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications .
- Some of the main characteristics of embedded operating systems are:
  - Direct use of interrupts: Embedded operating systems use interrupts to handle events from hardware devices or software applications in a timely and efficient manner.
  - Reactive operation: Embedded operating systems respond to external stimuli and perform the required actions without delay.
  - Real-time operation: Embedded operating systems meet the deadlines and timing constraints of the applications and guarantee predictable behavior.
  - Streamlined protection mechanisms: Embedded operating systems provide minimal or no protection features such as memory management, user authentication, or access control, as they are not needed or can be implemented by the applications.
  - I/O device flexibility: Embedded operating systems support a variety of input/output devices such as sensors, actuators, displays, keyboards, etc. and provide device drivers or interfaces for them.
- Some of the skills and knowledge required to work with embedded operating systems are:
  - Introduction to embedded systems software and development environments: Embedded operating systems require specialized tools and methods for development, testing, debugging, and deployment.
  - Unified Modeling Language: UML is a graphical language for modeling and documenting the structure and behavior of embedded systems and their components.
  - Multiprocessor design skills: Embedded operating systems may run on multiple processors or cores to achieve higher performance, parallelism, or fault tolerance.
  - Understanding of embedded systems design patterns: Design patterns are reusable solutions to common problems in embedded systems design, such as concurrency, synchronization, communication, etc.
  - Ability to work with modeling programs and languages like MATLAB: MATLAB is a software environment for numerical computation, visualization, and programming that can be used for modeling, simulating, and testing embedded systems and their algorithms.
  - Knowledge of user experience (UX) and user interface (UI) design: Embedded operating systems may have graphical or textual user interfaces that require design principles and techniques to ensure usability, accessibility, and aesthetics.
- Some of the common uses of embedded operating systems are:
  - ATMs: ATMs have basic operating systems that enable the machine to read a user's debit card and personal identification number input and perform bank account transactions.
  - Cellphones: Cellphones require operating systems like Android or iOS to boot the phone and enable applications to communicate with the hardware and the network.
  - Smart TVs: Smart TVs have operating systems that allow the user to access various online and offline media content and services, such as streaming, gaming, browsing, etc.
  - Medical devices: Medical devices such as pacemakers, insulin pumps, or ventilators have operating systems that monitor and control the vital functions of the patients and communicate with other devices or systems.



# USB

- USB stands for **Universal Serial Bus**, a standardized technology for attaching peripheral devices to a computer  .
- USB enables communication between devices and a host controller such as a personal computer (PC) or smartphone.
- USB connects peripheral devices such as digital cameras, mice, keyboards, printers, scanners, media devices, external hard drives and flash drives .
- USB establishes specifications for cables, connectors and protocols for connection, communication and power supply (interfacing) between computers, peripherals and other computers.
- USB allows simplified attachment of peripherals especially in a daisy chain, which is a series of devices connected together in sequence.
- USB was first introduced in 1996 and was developed by a number of American companies, including IBM, Intel Corporation, and Microsoft Corporation.
- USB has undergone several revisions and enhancements, such as USB 2.0, USB 3.0, USB 3.1, USB 3.2, USB 4, and USB Type-C.
- USB is widely used and supported by various operating systems, devices, and applications.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of Block & Network for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# Block & Network

- A block device is a device that stores or transfers data in fixed-sized units called blocks. Examples of block devices are hard disks, flash drives, CD-ROMs, etc.
- A network device is a device that communicates with other devices over a network using protocols such as TCP/IP, UDP, etc. Examples of network devices are routers, switches, modems, network cards, etc.
- Block and network devices are important components of embedded systems, as they provide storage and communication capabilities for the system.
- Embedded OS internals are the low-level mechanisms and structures that manage the interaction between the OS and the block and network devices.
- Some of the embedded OS internals related to block and network devices are:

  - Device drivers: These are software modules that control the operation of a specific device. They provide a uniform interface for the OS to access the device, and handle the device-specific details such as commands, interrupts, errors, etc.
  - Device files: These are special files that represent the devices in the file system. They allow the OS and the applications to access the devices using standard file operations such as open, read, write, close, etc.
  - Device nodes: These are data structures that store information about the devices, such as their name, type, major and minor numbers, permissions, etc. They are used by the OS to identify and locate the devices in the system.
  - Device classes: These are categories of devices that share common characteristics and functionalities. They allow the OS to group and manage the devices based on their class, rather than their individual properties. Examples of device classes are block, network, character, etc.
  - Device model: This is a representation of the physical and logical structure of the devices in the system. It shows how the devices are connected, configured, and organized in the system. It also provides information about the device attributes, capabilities, and status.
  - Device management: This is the process of detecting, registering, configuring, and controlling the devices in the system. It involves creating and deleting device files and nodes, loading and unloading device drivers, allocating and freeing device resources, etc.
  - Device communication: This is the process of transferring data between the devices and the OS or the applications. It involves using device files, device drivers, and device protocols to send and receive data blocks or packets over the devices.



# Unit 2 - OPEN SOURCE RTOS

- An open source RTOS is a real-time operating system whose source code is publicly available and can be modified and distributed by anyone.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, meaning that tasks are completed within a specified time frame and with predictable results.
- Some advantages of using open source RTOS are:
  - Cost savings: open source RTOS are usually free or low-cost, and do not require licensing fees or royalties.
  - Reliability and security: open source RTOS can be more reliable and secure than proprietary RTOS, because the source code is open and available for anyone to review and improve. Bugs and vulnerabilities can be detected and fixed faster by the community of developers and users.
  - Customization and innovation: open source RTOS can be customized and adapted to meet the specific needs and preferences of the users and developers. New features and functionalities can be added and integrated easily by modifying the source code.
  - Compatibility and interoperability: open source RTOS can be compatible and interoperable with various hardware platforms, software applications, and standards, because they are based on common and open protocols and interfaces.
- Some examples of open source RTOS are:
  - FreeRTOS: a market-leading RTOS for microcontrollers and small microprocessors, distributed freely under the MIT open source license. It includes a kernel and a growing set of IoT libraries suitable for use across all industry sectors.
  - Linux: a widely used and popular open source operating system that can also function as an RTOS by using extensions and modifications such as PREEMPT_RT, Xenomai, and RTLinux. It supports a large variety of hardware architectures, devices, and applications.
  - Zephyr: a small, scalable, and secure RTOS for resource-constrained devices and IoT applications. It is hosted by the Linux Foundation and supports multiple hardware platforms, protocols, and standards.
- Some challenges and risks of using open source RTOS are:
  - Quality and stability: open source RTOS may not have the same level of quality and stability as proprietary RTOS, because they may not undergo rigorous testing and verification processes. They may also have more bugs and errors, and less documentation and support.
  - Legal and ethical issues: open source RTOS may have different and conflicting licensing terms and conditions, which may affect the rights and obligations of the users and developers. They may also raise ethical issues such as plagiarism, intellectual property, and privacy.
  - Security and safety: open source RTOS may be more vulnerable to cyberattacks and malicious code, because the source code is exposed and accessible to anyone. They may also pose safety risks for critical and sensitive applications, such as medical devices, automotive systems, and aerospace systems.



# Basics of RTOS

- RTOS stands for Real-Time Operating System     .
- It is a software system that provides the necessary hard real-time computing capabilities, and it does so in an embedded environment.
- It is used for controlling devices that require timing synchronization with their environment or with other devices.
- It creates multiple threads of software execution and a scheduler for managing these threads.
- It also creates a multi-tasking and deterministic run-time environment.
- It is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- It can be classified into three types based on the time constraints of the tasks:
  - Hard Real-Time operating system: These operating systems guarantee that critical tasks be completed within a range of predefined deadlines.
  - Soft real-time operating system: This operating system provides some relaxation in the time limit. For example, a video streaming application can tolerate some delay in the data transmission.
  - Firm Real-time Operating System: RTOS of this type have to complete the task within the deadline, otherwise, the task is discarded. For example, a sensor data collection application can discard the old data if it is not processed in time.
- Some of the features of an RTOS are :
  - Preemptive scheduling: The scheduler can interrupt a running task and switch to a higher priority task at any time.
  - Fast context switching: The time required to save and restore the state of a task is minimal.
  - Low interrupt latency: The time required to respond to an external event is minimal.
  - Inter-task communication: The tasks can communicate with each other using mechanisms such as message queues, semaphores, mutexes, etc.
  - Memory management: The RTOS can allocate and deallocate memory for the tasks dynamically or statically.
  - Device drivers: The RTOS can provide interfaces to interact with the hardware devices such as sensors, actuators, etc.
  - Debugging and testing tools: The RTOS can provide tools to monitor, debug, and test the performance and functionality of the tasks.



# Real-time concepts for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real-time system is a system that must respond to events within a certain time frame, otherwise it may fail or cause undesirable consequences.
- A real-time operating system (RTOS) is a specialized operating system that provides deterministic and predictable behavior for real-time systems.
- An RTOS typically supports features such as:
  - Preemptive multitasking: the ability to switch between tasks based on their priority and deadlines, without waiting for them to finish or yield.
  - Inter-task communication and synchronization: the ability to exchange data and coordinate actions between tasks using mechanisms such as message queues, semaphores, mutexes, etc.
  - Memory management: the ability to allocate and deallocate memory for tasks and data structures, with minimal overhead and fragmentation.
  - Interrupt handling: the ability to respond to external events and signals, such as timers, sensors, etc., and execute interrupt service routines (ISRs) with low latency and high priority.
  - Device drivers: the ability to interface with hardware devices and peripherals, such as serial ports, network interfaces, etc., and provide a uniform and abstracted access to them.
- An open source RTOS is an RTOS that is developed and distributed under a free or open source license, such as GNU GPL, BSD, MIT, etc. This means that the source code of the RTOS is available to the public and can be modified, reused, and redistributed by anyone, subject to the terms of the license.
- Some examples of open source RTOS are:
  - FreeRTOS: a popular and widely used RTOS that supports many architectures and platforms, such as ARM, x86, PIC, Arduino, etc. It provides a simple and lightweight API for creating and managing tasks, queues, semaphores, timers, etc. It also supports optional features such as memory allocation, software timers, event groups, etc. 
  - Linux: a general-purpose operating system that can be configured and customized for real-time applications, using extensions such as PREEMPT_RT, Xenomai, RTAI, etc. These extensions provide mechanisms for reducing the latency and jitter of the Linux kernel, such as preemptible kernel, priority inheritance, high-resolution timers, etc. Linux also supports POSIX real-time extensions, such as pthreads, semaphores, message queues, etc. 
  - Zephyr: a scalable and modular RTOS that targets embedded systems and IoT devices, such as sensors, actuators, gateways, etc. It supports multiple architectures and platforms, such as ARM, x86, RISC-V, Arduino, etc. It provides a rich set of features, such as kernel services, device drivers, networking, security, file systems, etc. It also supports various protocols and standards, such as Bluetooth, LoRa, MQTT, CoAP, etc.



# Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-world applications.
- A real-time system is one where the correctness of the system depends not only on the logical results of the computations, but also on the time at which the results are produced.
- A real-time system can be classified into two types: hard real-time and soft real-time, based on the consequences of missing a deadline.

## Hard Real Time

- A hard real-time system is one where the time taken is deterministic to an exact moment.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- A hard real-time system is highly restrictive and doesn’t tolerate any system failure.
- Examples of hard real-time systems are air traffic control systems, nuclear power plant control systems, missile guidance systems, etc.

## Soft Real Time

- A soft real-time system is one where the time taken is deterministic to a range of values.
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system continues to function but with undesirable lower quality of output.
- A soft real-time system is less strict and can stand the system failure.
- Examples of soft real-time systems are multimedia systems, online gaming systems, video conferencing systems, etc.

## Key Differences

- Hard real-time systems are deterministic in nature while soft real-time systems are probabilistic.
- Hard real-time systems have strict deadlines while soft real-time systems have flexible deadlines.
- Hard real-time systems have catastrophic consequences of missing a deadline while soft real-time systems have degraded performance of missing a deadline.
- Hard real-time systems require specialized hardware and software while soft real-time systems can use general-purpose hardware and software.



# Differences between General Purpose OS and RTOS

- A General Purpose OS (GPOS) is an operating system that can run various applications and processes on a system, such as a personal computer, a workstation, or a server. A Real-Time OS (RTOS) is an operating system that can execute tasks within a specified time limit, such as an embedded system, a vending machine, or a robot.
- A GPOS is optimized for maximizing the throughput and utilization of the system resources, such as CPU, memory, disk, and network. A RTOS is optimized for minimizing the latency and jitter of the task execution, such as response time, deadline, and priority.
- A GPOS uses a preemptive or non-preemptive scheduling algorithm to allocate CPU time to processes based on their priority, arrival time, or resource requirements. A RTOS uses a deterministic scheduling algorithm to assign CPU time to tasks based on their urgency, deadline, or criticality.
- A GPOS may have a non-deterministic behavior, meaning that the execution time of a process may vary depending on the system load, interrupts, or resource contention. A RTOS must have a deterministic behavior, meaning that the execution time of a task must be predictable and consistent regardless of the system state, interrupts, or resource availability.
- A GPOS may have a complex and large kernel that provides various services and features to the user applications, such as memory management, file system, networking, security, and graphical user interface. A RTOS may have a simple and small kernel that provides only the essential services and features to the real-time applications, such as task management, synchronization, communication, and interrupt handling.



# Basic architecture of an RTOS

- An RTOS (Real-Time Operating System) is a specialized operating system that provides deterministic and predictable behavior for time-critical applications.
- An RTOS typically consists of a kernel and optional modules, such as device drivers, network protocols, file systems, debugging tools, etc.
- The kernel is the core component of the RTOS that manages the tasks, resources, interrupts, and timers of the system.
- The kernel provides the following services to the application:
  - Task management: The kernel creates, deletes, schedules, and synchronizes tasks, which are the basic units of execution in an RTOS. Tasks can have different priorities, states, and attributes. The kernel uses a preemptive or cooperative scheduling algorithm to assign CPU time to tasks based on their priorities and deadlines.
  - Memory management: The kernel allocates and deallocates memory for tasks and other system components. The kernel can use static or dynamic memory allocation methods, depending on the requirements and constraints of the system. The kernel also provides mechanisms for memory protection and sharing among tasks.
  - Interrupt management: The kernel handles the interrupts from external or internal sources, such as hardware devices, timers, or software exceptions. The kernel can use different interrupt handling techniques, such as polling, vectored, or nested interrupts, to minimize the interrupt latency and overhead.
  - Timer management: The kernel provides timers for measuring time intervals, generating periodic events, or implementing timeouts. The kernel can use hardware or software timers, depending on the availability and accuracy of the system clock. The kernel also provides mechanisms for adjusting the system time and synchronizing it with external sources.
  - Communication and synchronization: The kernel provides inter-task communication and synchronization mechanisms, such as message queues, semaphores, mutexes, event flags, pipes, signals, etc. These mechanisms allow tasks to exchange data, coordinate actions, or access shared resources in a safe and efficient way.
  - Other services: The kernel may also provide other services, such as power management, fault tolerance, security, logging, tracing, etc., depending on the needs and features of the system.

- The modules are optional components of the RTOS that extend the functionality of the kernel and provide higher-level services to the application. Some examples of modules are:
  - Device drivers: These are software components that interface with the hardware devices of the system, such as sensors, actuators, displays, keyboards, etc. Device drivers abstract the details of the device operation and provide a uniform and consistent interface to the kernel and the application.
  - Network protocols: These are software components that implement the communication protocols for data transmission and reception over various network interfaces, such as Ethernet, Wi-Fi, Bluetooth, etc. Network protocols enable the system to communicate with other systems or devices over the network.
  - File systems: These are software components that manage the storage and retrieval of data on various storage media, such as flash memory, hard disk, SD card, etc. File systems provide a hierarchical and logical organization of the data and support different file formats and attributes.
  - Debugging tools: These are software components that assist the development, testing, and debugging of the system. Debugging tools provide features such as breakpoints, watchpoints, single-stepping, variable inspection, stack trace, etc. Debugging tools can use different communication channels, such as serial port, USB, JTAG, etc., to connect to the system.
  - Other modules: The RTOS may also include other modules, such as graphical user interface (GUI), multimedia, encryption, compression, etc., depending on the application domain and requirements of the system.

- The RTOS architecture can be classified into two main types: monolithic kernel and microkernel.
  - A monolithic kernel is a single and large kernel that contains all the services and modules of the RTOS. A monolithic kernel runs in a single address space and has direct access to the hardware and memory. A monolithic kernel has the advantages of high performance, low overhead, and simplicity, but also has the disadvantages of low modularity, high complexity, and low reliability.
  - A microkernel is a small and minimal kernel that contains only the essential services of the RTOS, such as task management, memory management, and interrupt management. A microkernel runs in a separate address space and communicates with the modules and the application through message passing. A microkernel has the advantages of high modularity, low complexity, and high reliability, but also has the disadvantages of low performance, high overhead, and difficulty.

- The choice of the RTOS architecture depends on the trade-offs between the performance, functionality, reliability, and



# Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a mechanism that determines which task or process should run on a processor at a given time, based on some criteria and constraints.
- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing requirements of real-time applications, such as embedded systems, industrial control, robotics, etc.
- An open source RTOS is a RTOS that is freely available for anyone to use, modify, and distribute, under a specific license.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, RIOT, and NuttX.
- These RTOSes differ in their features, such as scheduling, inter-process communication, memory management, and interrupt latency.
- Scheduling is the process of assigning priorities and time slots to tasks or processes, and switching between them, to ensure that they meet their deadlines and performance goals.
- Some commonly used RTOS scheduling algorithms are:
  - Cooperative scheduling: A task runs until it voluntarily yields the processor to another task or it completes. This is simple and fast, but not suitable for hard real-time applications, as a task can block the execution of other tasks indefinitely.
  - Preemptive scheduling: A task can be interrupted by a higher priority task or by a timer, and resume later. This is more flexible and responsive, but introduces overhead and complexity, such as context switching and synchronization issues.
  - Rate-monotonic scheduling: A preemptive scheduling algorithm that assigns fixed priorities to tasks based on their periods, such that the shorter the period, the higher the priority. This is optimal for periodic tasks with hard deadlines, but not for aperiodic or sporadic tasks.
  - Round-robin scheduling: A preemptive scheduling algorithm that assigns equal priorities to tasks, and switches between them in a circular order, using a fixed time slice. This is fair and simple, but not efficient for real-time applications, as it does not consider the deadlines or the execution times of the tasks.
  - Fixed priority pre-emptive scheduling: A preemptive scheduling algorithm that assigns fixed priorities to tasks based on some criteria, such as user input, task importance, etc., and switches between them based on their priorities, using a fixed time slice. This is more flexible and adaptable, but requires careful priority assignment and analysis to avoid priority inversion or starvation.
  - Fixed priority scheduling with deferred preemption: A variant of fixed priority pre-emptive scheduling that allows a lower priority task to continue running until it reaches a preemption point, such as a blocking operation or a voluntary yield, before switching to a higher priority task. This reduces the context switching overhead and improves the cache performance, but increases the response time of the higher priority task.
  - Fixed priority non-preemptive scheduling: A variant of fixed priority pre-emptive scheduling that does not allow preemption at all, and only switches to a higher priority task when the current task completes or blocks. This eliminates the context switching overhead and the synchronization issues, but increases the response time and the deadline miss ratio of the higher priority task.



# Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS .
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- Some of the common IPC methods are  :
  - Shared memory: a region of memory that can be accessed by multiple processes.
  - Pipes: a unidirectional or bidirectional channel that can transfer data between processes.
  - Queues: a data structure that can store and retrieve data in a first-in first-out (FIFO) order.
  - Mailbox: a message buffer that can send and receive fixed-size messages between processes.
  - Signals: a notification mechanism that can interrupt a process and invoke a handler function.
  - Remote procedure calls: a method that can invoke a function in another process and return the result.
- Different open source RTOSes may implement different IPC methods or use different names for them  .
  - For example, FreeRTOS supports queues, mailboxes, semaphores, mutexes, event groups, and software timers.
  - Bern RTOS supports queues, mailboxes, signals, semaphores, mutexes, and event flags.
  - Zephyr RTOS supports queues, pipes, mailboxes, message queues, signals, semaphores, mutexes, and condition variables.
  - Linux RTOS supports shared memory, pipes, message queues, signals, semaphores, mutexes, and sockets.
- IPC methods have different advantages and disadvantages in terms of performance, complexity, reliability, and scalability  .
  - For example, shared memory is fast and simple, but it requires synchronization and protection mechanisms to avoid data corruption and race conditions.
  - Pipes are easy to use and portable, but they have limited capacity and can cause blocking and deadlock.
  - Queues are flexible and robust, but they consume memory and CPU resources and can introduce latency and overhead.
  - Mailboxes are convenient and efficient, but they can only handle fixed-size messages and may lose data if the buffer is full.
  - Signals are lightweight and asynchronous, but they have limited information and can be lost or ignored.
  - Remote procedure calls are powerful and transparent, but they are complex and prone to errors and security issues.



# Performance Metric in Scheduling Models for Open Source RTOS

- A performance metric is a quantitative measure of how well a real-time operating system (RTOS) meets the timing requirements of the tasks it manages.
- A scheduling model is a set of rules and algorithms that determine how the RTOS assigns priorities and resources to the tasks.
- An open source RTOS is a RTOS that is freely available and can be modified and distributed by anyone.
- Some of the common performance metrics for RTOS scheduling models are:
  - Task switching time: the time it takes for the RTOS to switch from one task to another.
  - Pre-emption time: the time it takes for the RTOS to interrupt a lower-priority task and start executing a higher-priority task.
  - Semaphore shuffling time: the time it takes for the RTOS to transfer a semaphore (a synchronization mechanism) from one task to another.
  - Inter-task messaging latency: the time it takes for the RTOS to deliver a message from one task to another.
- These metrics can be used to evaluate and compare the performance of different open source RTOSs, such as Keil RTX5, FreeRTOS, Zephyr, NuttX, etc.
- Some of the factors that affect the performance metrics of RTOSs are:
  - The hardware architecture and configuration of the system, such as the processor speed, memory size, cache size, etc.
  - The software design and implementation of the RTOS, such as the data structures, algorithms, interrupt handlers, etc.
  - The workload and behavior of the tasks, such as the number, priority, frequency, duration, synchronization, communication, etc.
- To measure the performance metrics of RTOSs, various benchmarking techniques and tools can be used, such as:
  - The Thread-Metric Benchmark Suite, an open-source, vendor-neutral, free benchmark suite that measures RTOS performance on single-core, multicore, or multithreaded architectures.
  - The RTOSBench, a tool that measures the task switching time, pre-emption time, semaphore shuffling time, and inter-task messaging latency of RTOSs on ARM Cortex-M4 microcontrollers.
  - The RTOS Performance Analyzer, a tool that measures the performance parameters of RTOSs, such as the CPU utilization, memory utilization, response time, etc..



# Interrupt management in RTOS environment

- An interrupt is a signal that causes the processor to temporarily stop its current execution and switch to a predefined handler routine.
- Interrupts are useful for handling time-critical events, such as input/output, timers, sensors, etc.
- Interrupts can also be used for inter-task communication and synchronization in a multitasking system.
- However, interrupts can also introduce latency and unpredictability in a real-time operating system (RTOS), which is designed to meet strict timing constraints and deadlines.
- Therefore, interrupt management is a crucial aspect of RTOS design and implementation, which involves balancing the trade-off between responsiveness and determinism.

## Interrupt management techniques in RTOS

- There are different techniques for managing interrupts in an RTOS environment, depending on the type and priority of the interrupt, the architecture of the processor and the RTOS, and the application requirements.
- Some of the common techniques are:

  - **Direct ISR**: The interrupt service routine (ISR) is executed directly by the processor in response to an interrupt. This is the simplest and fastest technique, but it can also cause high interrupt latency for lower-priority interrupts, as well as blocking the RTOS scheduler and other tasks. Therefore, direct ISR should only be used for very short and time-critical interrupts, such as timers or watchdogs.
  - **Deferred ISR**: The ISR is split into two parts: a short and fast part that runs directly in interrupt context, and a longer and slower part that runs in task context. The first part acknowledges the interrupt, clears the interrupt flag, and posts a message or a semaphore to the second part, which is executed by a dedicated task or a thread. This technique reduces the interrupt latency for lower-priority interrupts, as well as allowing the RTOS scheduler and other tasks to run. However, it also introduces some overhead and complexity, as well as potential synchronization issues between the two parts of the ISR.
  - **Nested ISR**: The processor supports multiple levels of interrupt priority, and allows higher-priority interrupts to preempt lower-priority interrupts. This technique improves the responsiveness of the system, as well as reducing the interrupt latency for higher-priority interrupts. However, it also increases the stack usage and the context switching overhead, as well as complicating the interrupt handling logic and the RTOS scheduler.
  - **Maskable ISR**: The processor supports masking or disabling certain interrupts, either globally or selectively. This technique allows the system to temporarily block or defer some interrupts, such as during critical sections or atomic operations, to ensure data integrity and consistency. However, it also increases the interrupt latency and the risk of missing or losing some interrupts, as well as requiring careful management of the interrupt mask.

## Interrupt management examples in RTOS

- Different RTOSes may implement different interrupt management techniques, or a combination of them, depending on their design goals and features.
- Some examples of popular RTOSes and their interrupt management techniques are:

  - **FreeRTOS**: FreeRTOS is an open source RTOS that supports direct ISR, deferred ISR, and nested ISR techniques. FreeRTOS also provides an API for managing the interrupt mask, as well as a tick interrupt that assists the scheduling of other tasks. FreeRTOS has an interrupt called Tick which accounts the time passage and assists the scheduling of other tasks. This is the only task with periodic behavior found as part of the RTOS itself.
  - **Linux**: Linux is an open source operating system that supports deferred ISR and nested ISR techniques. Linux also provides an API for managing the interrupt mask, as well as a timer interrupt that triggers the scheduler. Linux uses a mechanism called softirqs to defer some interrupt processing to a later time, such as network or disk I/O. Linux also supports threaded interrupts, which are similar to deferred ISR, but run in kernel threads instead of user threads.
  - **VxWorks**: VxWorks is a commercial RTOS that supports direct ISR, deferred ISR, and nested ISR techniques. VxWorks also provides an API for managing the interrupt mask, as well as a clock interrupt that triggers the scheduler. VxWorks uses a mechanism called interrupt service tasks (ISTs) to defer some interrupt processing to a later time, such as network or disk I/O. VxWorks also supports interrupt threads, which are similar to deferred ISR, but run in kernel threads instead of user threads.



# Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in an RTOS.
- Memory management can be done in two ways: static or dynamic.
- Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This method is simple, fast, and deterministic, but it can waste memory and limit flexibility.
- Dynamic memory management means that the memory is allocated and freed at run time, depending on the needs of the application. This method is more flexible and efficient, but it can introduce overhead, fragmentation, and non-determinism.
- An open source RTOS is an RTOS that is freely available and can be modified and distributed by anyone. Some examples of open source RTOS are FreeRTOS, Zephyr, and Azure RTOS.
- An open source RTOS may use different memory management options, depending on the features and requirements of the RTOS and the application.
- Some of the memory management options for open source RTOS are:

  - Heap: A heap is a pool of memory that can be dynamically allocated and freed by the RTOS or the application. A heap can be implemented using different algorithms, such as first fit, best fit, or worst fit. A heap can provide flexibility and efficiency, but it can also cause fragmentation, overhead, and non-determinism.
  - Stack: A stack is a region of memory that is allocated and freed in a last-in first-out (LIFO) order. A stack is typically used to store local variables and function call information for each task. A stack can provide fast and deterministic memory management, but it can also cause stack overflow or underflow if the size is not adequate.
  - Pool: A pool is a collection of fixed-size memory blocks that can be allocated and freed by the RTOS or the application. A pool can reduce fragmentation and overhead, but it can also limit the size and number of memory blocks available.
  - Static: Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This can be done by using global variables, constants, or macros. Static memory management can provide simplicity and determinism, but it can also waste memory and limit flexibility.

- The choice of memory management option for an open source RTOS depends on several factors, such as:

  - The memory size and availability of the target device.
  - The performance and reliability requirements of the application.
  - The complexity and modularity of the application code.
  - The trade-off between memory usage and execution time.
  - The compatibility and portability of the RTOS and the application.



# File systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or SD card.
- A file system organizes data into files and directories, and provides an interface to access, create, delete, modify, and rename them.
- A file system also maintains metadata, such as file attributes, permissions, timestamps, and allocation information.
- A file system can be implemented as part of the operating system kernel, as a user-level library, or as a separate service or process.
- A file system can be designed for different purposes, such as performance, reliability, security, portability, scalability, or compatibility.
- A file system can support different file formats, such as FAT, NTFS, ext4, or exFAT, depending on the features and limitations of the underlying device and the application requirements.
- A file system can also support different file system features, such as encryption, compression, journaling, transactions, snapshots, or quotas.

## File systems for open source RTOS

- An open source RTOS is a real-time operating system that is distributed under a free or open source license, such as GPL, BSD, or MIT.
- An open source RTOS typically provides features such as preemptive multitasking, inter-task communication, synchronization, memory management, timers, and device drivers.
- An open source RTOS can also support various file systems, either as built-in components or as external modules or libraries.
- Some examples of file systems for open source RTOS are:

  - Reliance Edge: a transactional, fail-safe, and MISRA compliant file system that supports FAT and exFAT formats. It is designed for FreeRTOS, but can be ported to other RTOS.
  - Azure RTOS FileX: a high-performance, FAT-compatible file system that supports FAT12, FAT16, FAT32, and exFAT formats. It is fully integrated with Azure RTOS ThreadX, but can also work with other RTOS .
  - IMFS: an in-memory file system that provides a small, memory-resident root file system for RTEMS. It supports POSIX and BSD interfaces, and can mount other file systems, such as FAT or NFS.
  - Mini-IMFS: a stripped-down version of IMFS that aims for lower memory overhead. It is also used as a root file system for RTEMS.
  - JFFS2: a log-structured file system that is designed for flash memory devices. It supports compression, wear leveling, and bad block management. It is widely used in Linux, but can also be ported to other RTOS, such as FreeRTOS or eCos.
  - LittleFS: a fail-safe file system that is designed for low-power embedded devices with limited RAM and ROM. It supports power-loss resilience, dynamic wear leveling, and bounded RAM/ROM usage. It can be used with any RTOS or bare-metal system.



# I/O Systems

- I/O systems are the components that enable an embedded system to interact with the external world, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
- Parallel I/O systems transfer multiple bits of data simultaneously using multiple wires or pins. They are faster but require more hardware resources and wiring complexity. Examples of parallel I/O systems are GPIO (General Purpose Input/Output), LCD (Liquid Crystal Display), etc.
- Serial I/O systems transfer one bit of data at a time using one or two wires or pins. They are slower but require less hardware resources and wiring complexity. Examples of serial I/O systems are UART (Universal Asynchronous Receiver/Transmitter), SPI (Serial Peripheral Interface), I2C (Inter-Integrated Circuit), USB (Universal Serial Bus), etc.
- I/O systems can also be classified into two modes: polling and interrupt.
- Polling mode is when the embedded system continuously checks the status of the I/O device to see if there is any data available or any action required. Polling mode is simple but consumes more CPU time and power. It can also cause delays or missed events if the polling frequency is not high enough.
- Interrupt mode is when the embedded system is notified by the I/O device when there is any data available or any action required. Interrupt mode is complex but saves CPU time and power. It can also handle events more promptly and reliably. However, interrupt mode can cause concurrency issues or priority inversion if the interrupt handlers are not well designed.
- I/O systems can also be classified into two types: synchronous and asynchronous.
- Synchronous I/O systems are those that operate at a fixed or predetermined rate or frequency. They are easier to program and synchronize but require more accurate timing and clock signals. Examples of synchronous I/O systems are SPI, I2C, etc.
- Asynchronous I/O systems are those that operate at a variable or unpredictable rate or frequency. They are harder to program and synchronize but require less accurate timing and clock signals. Examples of asynchronous I/O systems are UART, USB, etc.
- I/O systems are essential for embedded systems and real time operating systems (RTOS) to perform their specific functions in a much larger system. RTOS are operating systems that provide deterministic and timely responses to events or tasks. RTOS can handle multiple I/O devices and prioritize them according to their importance or urgency. RTOS can also provide features such as multitasking, inter-task communication, synchronization, memory management, etc. for embedded systems. Examples of RTOS are FreeRTOS, VxWorks, QNX, etc.



# Advantage and Disadvantage of RTOS

A Real Time Operating System (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system that is designed to make sure that a specific object is available to a robot on the assembly line is an example of an RTOS.

Some of the advantages and disadvantages of RTOS are:

## Advantages

- **Maximum consumption**: RTOS can utilize the system resources and devices efficiently and produce more output while keeping all devices in active state. There is little or no downtime in these systems   .
- **Task shifting**: RTOS can switch between tasks quickly and with minimal overhead. The time assigned for shifting tasks in these systems is very less. For example, in older systems, it takes about 10 microseconds, whereas in newer systems, it takes about 3 to 5 microseconds .
- **Predictable and reliable**: RTOS can ensure that the system produces an accurate and consistent output within the specified time limit. RTOS can handle critical and time-sensitive tasks without compromising the quality or performance of the system .

## Disadvantages

- **Longer wait for low-priority tasks**: RTOS is programmed to execute priority tasks within specific deadlines, which means that lower priority tasks may have to wait longer than in a general-purpose operating system. This can affect the responsiveness and user experience of the system.
- **Minimal task capacity**: RTOS is not suitable for multi-tasking or running complex applications that require a lot of memory and processing power. RTOS can only run a limited number of tasks simultaneously, and each task has to be carefully designed and optimized for the system.
- **Complex and costly**: RTOS requires a high level of expertise and skill to develop and maintain. RTOS also needs specialized hardware and software tools that can increase the cost and complexity of the system .



# POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX stands for Portable Operating System Interface, and it is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines both the system and user-level application programming interfaces (APIs), along with command line shells and utility programs, for software compatibility.
- POSIX is especially relevant for the development of real-time and embedded systems, as it promotes interoperability and portability of applications across Unix-like operating systems  .
- POSIX consists mainly of definitions for core OS services and real-time extensions, which are divided into four major components:
  - Base Definitions: General terms, concepts, and interfaces common to all volumes of the standard, including utility conventions and C-language header definitions.
  - System Interfaces: Definitions for system services and functions, such as process management, file operations, signals, timers, threads, synchronization, and communication.
  - Shell and Utilities: Definitions for a standard command language interpreter (shell) and common utility programs, such as cp, ls, grep, etc.
  - Rationale: Explanations of the reasons behind the design choices and the relationship between different parts of the standard.
- POSIX also defines several profiles for different types of systems, such as POSIX.1 (for general-purpose systems), POSIX.1b (for real-time systems), POSIX.1c (for threaded systems), and POSIX.1d (for additional real-time features) .
- POSIX compliance can be verified by using test suites, such as VSX4, VSRT, and VSTH, which are adapted for embedded devices by The Open Group.



# RTOS Issues

- An RTOS (Real-Time Operating System) is a software platform that provides predictable and deterministic behavior for embedded applications that have real-time constraints.
- However, using an RTOS also introduces some challenges and issues that developers need to be aware of and address in their design and implementation.
- Some of the common RTOS issues are:

  - **Priority inversion**: This occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, while a medium-priority task preempts the low-priority task. This results in the high-priority task being delayed longer than expected. To prevent this, an RTOS should provide mechanisms such as priority inheritance or priority ceiling to ensure that the low-priority task can temporarily increase its priority and release the resource as soon as possible .
  - **Deadlock**: This occurs when two or more tasks are waiting for each other to release a resource that they hold, creating a circular dependency that prevents any of them from making progress. To avoid this, an RTOS should provide tools such as mutexes, semaphores, and message queues to coordinate and synchronize access to shared resources, and follow best practices such as acquiring resources in a consistent order and releasing them as soon as possible .
  - **Task jitter**: This occurs when a periodic task experiences variations in its execution time or start time, due to factors such as interrupts, context switches, or scheduling policies. This can affect the quality of service and performance of the application, especially if the task has strict timing requirements. To minimize this, an RTOS should provide features such as preemptive scheduling, time slicing, and interrupt latency control to ensure that the tasks can meet their deadlines and run with minimal interference .
  - **Control-flow complexity**: This occurs when the logic and flow of the application becomes difficult to understand and debug, due to the dynamic and concurrent nature of the RTOS tasks. Unlike a bare-metal or sequential program, an RTOS-based program does not have a clear and predictable execution order, since the RTOS decides which task to run at any given moment, based on factors such as priorities, events, and timers. This can lead to errors, bugs, and unexpected behaviors that are hard to reproduce and fix. To cope with this, an RTOS should provide techniques such as tracing, logging, and debugging tools to help the developers monitor and analyze the behavior and state of the tasks and the system .
  - **Security risks**: This occurs when the application or the RTOS is vulnerable to attacks or breaches that can compromise the confidentiality, integrity, or availability of the data or the system. For example, an attacker can exploit a buffer overflow, a memory leak, or a weak encryption algorithm to gain unauthorized access, inject malicious code, or cause a denial of service. To protect against this, an RTOS should provide features such as secure boot, secure storage, secure communication, and secure update to ensure that the application and the RTOS are authenticated, encrypted, and verified .



# Selecting a Real-Time Operating System

A real-time operating system (RTOS) is an operating system that is designed to meet the timing requirements of real-time applications. Real-time applications are those that need to respond to events or inputs within a specified time limit, such as control systems, multimedia, robotics, etc. An RTOS provides features such as preemptive multitasking, priority-based scheduling, inter-task communication, and synchronization mechanisms to enable real-time behavior.

Selecting an RTOS for an embedded system depends on several factors, such as:

- **Embedded system usage**: The RTOS should be suitable for the target hardware platform, such as the processor architecture, memory size, peripheral devices, etc. The RTOS should also be compatible with the development tools, such as compilers, debuggers, etc. The RTOS should have a small footprint and low overhead to fit in the limited resources of the embedded system.
- **Error-free**: The RTOS should be reliable and robust, and should not cause any errors or failures in the system. The RTOS should have mechanisms to detect and handle errors, such as exceptions, faults, watchdogs, etc. The RTOS should also support testing and debugging features, such as trace, logging, breakpoints, etc.
- **Maximum utilization**: The RTOS should be able to utilize the available resources of the system efficiently, such as CPU, memory, power, etc. The RTOS should have a fast context switch time, low interrupt latency, and minimal system calls to reduce the overhead and improve the performance. The RTOS should also support power management features, such as sleep modes, dynamic voltage and frequency scaling, etc.
- **Middleware**: The RTOS should provide support for the middleware components that are required by the application, such as network protocols, file systems, graphical user interfaces, etc. The RTOS should also provide a standard interface for the middleware to communicate with the kernel and the hardware. The RTOS should ensure that the middleware does not interfere with the real-time behavior of the system.
- **Performance**: The RTOS should be able to meet the performance requirements of the application, such as the response time, throughput, jitter, etc. The RTOS should provide a deterministic and predictable scheduling algorithm that guarantees the execution of the tasks according to their priorities and deadlines. The RTOS should also support features such as real-time clocks, timers, interrupts, etc. to enable accurate timing measurements and control.
- **Task switching**: The RTOS should be able to switch between the tasks quickly and smoothly, without causing any delays or disruptions in the system. The RTOS should support features such as preemption, priority inheritance, priority ceiling, etc. to avoid priority inversion and deadlock problems. The RTOS should also support features such as task creation, deletion, suspension, resumption, etc. to enable dynamic task management.



# RTOS Comparative Study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the features and characteristics of different RTOSs and compare them based on various criteria.

## Features of RTOS

Some of the common features of RTOS are:

- Preemptive multitasking: The ability of the operating system to interrupt a running task and switch to another task.
- Priority-based scheduling: The ability of the operating system to assign different priorities to different tasks and execute them accordingly.
- Inter-task communication and synchronization: The ability of the operating system to provide mechanisms for tasks to communicate and coordinate with each other, such as message queues, semaphores, mutexes, etc.
- Memory management: The ability of the operating system to allocate and deallocate memory for tasks and data structures.
- Interrupt handling: The ability of the operating system to respond to external events and signals, such as timers, sensors, etc.
- Device drivers: The ability of the operating system to interface with hardware devices, such as serial ports, network interfaces, etc.

## Criteria for Comparison

Some of the criteria that can be used to compare different RTOSs are:

- Size: The amount of memory (RAM and ROM) required by the operating system and its components.
- Performance: The speed and efficiency of the operating system in executing tasks and handling interrupts.
- Scalability: The ability of the operating system to support a large number of tasks and devices.
- Portability: The ability of the operating system to run on different hardware platforms and architectures.
- Reliability: The ability of the operating system to handle errors and faults and ensure correct operation.
- Security: The ability of the operating system to protect the system and data from unauthorized access and manipulation.
- Licensing: The terms and conditions under which the operating system can be used and modified.

## Examples of RTOS

Some of the examples of RTOSs are:

- FreeRTOS: An open source RTOS that supports a wide range of microcontrollers and architectures. It is designed to be small, simple, and easy to use. It provides basic features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, and interrupt handling. It does not provide device drivers or networking support, but relies on external libraries and modules. It has a permissive MIT license that allows free use and modification of the source code.
- Zephyr: An open source RTOS that targets small and resource-constrained devices, such as IoT and wearable devices. It is designed to be modular, scalable, and secure. It provides features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, interrupt handling, device drivers, networking support, and security mechanisms. It has a permissive Apache 2.0 license that allows free use and modification of the source code.
- LynxOS: A proprietary RTOS that targets high-performance and safety-critical applications, such as aerospace, defense, and industrial systems. It is designed to be fast, reliable, and secure. It provides features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, memory management, interrupt handling, device drivers, networking support, security mechanisms, and POSIX compliance. It has a proprietary license that requires a fee for use and modification of the source code.

## Comparison Table

The following table summarizes some of the features and characteristics of the three RTOSs mentioned above:

| Feature | FreeRTOS | Zephyr | LynxOS |
| --- | --- | --- | --- |
| Size | 8 KB - 1.5 MB | 16 KB - 1.5 MB | 1.4 MB - 2.5 MB |
| Performance | Moderate | High | High |
| Scalability | Moderate | High | High |
| Portability | High | High | Moderate |
| Reliability | Moderate | High | High |
| Security | Low | High | High |
| Licensing | MIT | Apache 2.0 | Proprietary |

: https://en.wikipedia.org/wiki/FreeRTOS
: https://en.wikipedia.org/wiki/Zephyr_(operating_system)
: https://www.lynx.com/embedded-systems-learning-center/how-to-choose-a-real-time-operating-system-rtos



# Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal latency and jitter .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks.
- A real-time kernel supports different scheduling algorithms, such as priority-based, round-robin, or deadline-based, to assign CPU time to tasks.
- A real-time kernel provides mechanisms for inter-task communication and synchronization, such as semaphores, message queues, mutexes, and event flags.
- A real-time kernel can be classified into two types: hard real-time and soft real-time.
  - A hard real-time kernel guarantees that all tasks will meet their deadlines, regardless of the system load.
  - A soft real-time kernel tries to meet the deadlines of most tasks, but may occasionally miss some deadlines due to high system load or unpredictable events.
- A real-time kernel can be identified by the rt keyword in the kernel version, such as kernel-rt or preempt-rt.
- A real-time kernel is suitable for applications that require deterministic response times, such as telco, industrial automation, robotics, and gaming.



# Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that can guarantee a deterministic response time to events, such as interrupts, system calls, or user inputs.
- A normal Linux kernel is not fully preemptible, meaning that some critical sections of code cannot be interrupted by higher priority tasks, resulting in unpredictable latencies.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a set of patches that modify the kernel code to make it fully preemptible and reduce the duration of critical sections.
- The most widely used set of patches for real time Linux is the PREEMPT_RT patchset, maintained by the Linux Foundation Real-Time Linux project.
- The steps to apply the PREEMPT_RT patchset to a normal Linux kernel are as follows:

  - Download the source code of the normal Linux kernel and the corresponding PREEMPT_RT patch from https://www.kernel.org/ and https://mirrors.edge.kernel.org/pub/linux/kernel/projects/rt/, respectively.
  - Extract the kernel source code and apply the patch using the patch command, e.g., `patch -p1 < patch-5.15.6-rt21.patch`.
  - Configure the kernel options using the `make menuconfig` command. In the config options, set the `Fully Preemptible kernel (RT)` option.
  - Build the kernel using the `make` command and install the modules using the `make modules_install` command.
  - Update the grub boot loader and reboot into the newly installed real-time patched kernel.

- Alternatively, one can install a pre-built real time kernel from a repository, such as the CERN-RT repo for CentOS or the Ubuntu-RT repo for Ubuntu.
- To verify that the real time kernel is running, one can use the `uname -a` command and check for the `PREEMPT_RT` string in the output.



# Xenomai basics

- Xenomai is a software framework that provides hard real-time computing support to user space applications on Linux-based systems .
- Xenomai allows real-time threads to run either in kernel space or in user space, bypassing the Linux scheduler and using the RT-Nucleus scheduler instead .
- Xenomai uses Linux as a background task that can be preempted by any real-time thread .
- Xenomai can be installed by patching the Linux kernel with the I-pipe patch and compiling the Xenomai source code.
- Xenomai provides various APIs for real-time programming, such as POSIX, RTDM, Alchemy, and Cobalt .
- Xenomai threads can switch between primary mode (real-time) and secondary mode (non-real-time) depending on the system state and the services they invoke .



# Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An RTOS (Real-Time Operating System) is a software platform that provides deterministic and predictable execution of tasks on embedded devices.
- An open source RTOS is an RTOS that is freely available under a license that allows users to modify, distribute and use the software without restrictions.
- Some of the benefits of using an open source RTOS are:
  - Cost savings: no need to pay for licenses or royalties.
  - Flexibility: users can customize the software to fit their specific needs and preferences.
  - Innovation: users can benefit from the collective knowledge and contributions of the open source community.
  - Compatibility: users can avoid vendor lock-in and ensure interoperability with other open source software and hardware.
- Some of the challenges of using an open source RTOS are:
  - Quality: users may encounter bugs, errors or vulnerabilities in the software that are not fixed or patched by the developers.
  - Support: users may have difficulty finding documentation, tutorials or technical assistance for the software.
  - Liability: users may not have any legal protection or warranty for the software in case of malfunction or damage.
- Two examples of open source RTOS for embedded systems are FreeRTOS and ChibiOS/RT.
- FreeRTOS is a market-leading RTOS for microcontrollers and small microprocessors that was created in 2003 by Richard Barry.
  - It is a minimalistic RTOS that supports multiple architectures and provides methods for multiple threads or tasks, mutexes, semaphores and software timers.
  - It also offers a tickless mode for low power applications and supports thread priorities.
  - It can be statically or dynamically allocated with five schemes of memory management.
  - It is distributed under the MIT open source license and includes a kernel and a growing set of software libraries and tools.
- ChibiOS/RT is a compact and fast RTOS for embedded devices that was developed by Giovanni Di Sirio.
  - It is a feature-complete RTOS that supports multiple architectures and provides a rich set of services, such as threads, timers, queues, semaphores, mutexes, events, messages, memory pools and heaps .
  - It also offers a modular approach, a HAL (Hardware Abstraction Layer), a portable debugger, a shell and a test suite .
  - It is released under a mix of the GNU General Public License version 3 (GPL3) and the Apache License 2.0, depending on the module. Commercial licenses are also available from ChibiOS.
- Application development for embedded systems using an open source RTOS involves the following steps:
  - Choosing an RTOS that suits the requirements and constraints of the project, such as performance, memory, power, functionality and compatibility.
  - Downloading and installing the RTOS software and the necessary tools, such as compilers, debuggers and IDEs (Integrated Development Environments).
  - Configuring the RTOS software and the hardware platform, such as setting the clock frequency, the stack size, the heap size and the peripheral drivers.
  - Writing the application code using the RTOS APIs (Application Programming Interfaces) and libraries, such as creating and managing tasks, synchronizing and communicating between tasks, and using timers and interrupts.
  - Building, testing and debugging the application code using the tools provided by the RTOS software and the hardware platform, such as breakpoints, watchpoints, tracepoints and logs.
  - Deploying and running the application code on the target device and monitoring its behavior and performance.



# Real Time Operating Systems

## Unit 3 - REAL TIME KERNEL BASICS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS has two key features: predictability and determinism. Predictability means that repeated tasks are performed within a tight time boundary, while determinism means that the system responds to events in a fixed and known amount of time.
- An RTOS typically consists of a kernel, which provides the core functionality of the system, such as task management, inter-task communication and synchronization, memory management, interrupt handling, and timer services.
- A task is a basic unit of execution in an RTOS. A task can be created, deleted, suspended, resumed, or terminated by the kernel or by another task. A task can also have a priority, which determines its order of execution relative to other tasks.
- Inter-task communication and synchronization are essential for coordinating the activities of multiple tasks in an RTOS. There are various methods for achieving this, such as message queues, semaphores, mutexes, event flags, and pipes.
- Memory management in an RTOS is responsible for allocating and deallocating memory blocks for tasks and other system components. An RTOS may use static or dynamic memory allocation, depending on the requirements and constraints of the system.
- Interrupt handling in an RTOS is the mechanism for responding to external or internal events that require immediate attention. An interrupt can be triggered by a hardware device, a software exception, or a timer. An interrupt handler is a special function that executes when an interrupt occurs and performs the necessary actions to service the interrupt.
- Timer services in an RTOS are used for measuring and controlling the passage of time. A timer can be used to generate periodic or one-shot events, to delay the execution of a task, or to measure the execution time of a task or a function.
- An RTOS can be classified into two types: hard real-time and soft real-time. A hard real-time system is one that must meet all its deadlines, otherwise it may cause catastrophic consequences. A soft real-time system is one that can tolerate some missed deadlines, but with a degradation in performance or quality.
- An RTOS can be designed and implemented in various ways, depending on the target platform, the application domain, and the system requirements. Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, QNX, VxWorks, and Zephyr .



# Event based real time kernel basics

- Events in a real-time system are the actions or the result of the actions that are generated by the system or the environment.
- An event in a real-time system can be either instantaneous or have a certain duration.
- Events can be classified based on different criteria, such as:
  - Internal or external: Internal events are generated by the system itself, such as timer interrupts, system calls, or exceptions. External events are generated by the environment, such as sensor inputs, user inputs, or network packets.
  - Periodic or aperiodic: Periodic events occur at regular intervals, such as clock ticks, sensor readings, or control loops. Aperiodic events occur at irregular intervals, such as user commands, alarms, or faults.
  - Synchronous or asynchronous: Synchronous events are predictable and depend on the execution of the system, such as system calls, exceptions, or inter-process communication. Asynchronous events are unpredictable and independent of the execution of the system, such as interrupts, signals, or messages.
- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel provides deterministic response times to service events, meaning that the maximum delay between the occurrence of an event and the start of its service is bounded and known.
- A real-time kernel is also known as kernel-rt or preempt-rt.
- A real-time kernel can be identified by executing the `uname -r` command on the terminal, and then looking for the `rt` keyword in the kernel version.
- A real-time kernel is based on the principle of preemption, which means that a higher priority task can interrupt a lower priority task at any time.
- A real-time kernel can be classified into two types, based on the degree of preemption:
  - Fully preemptive: The kernel can be interrupted at any point by a higher priority task, even during critical sections or system calls. This type of kernel provides the lowest latency and the highest responsiveness, but it requires careful synchronization and locking mechanisms to avoid data corruption or inconsistency .
  - Preemptible: The kernel can be interrupted by a higher priority task, except during certain non-preemptible sections, such as interrupt handlers, spin locks, or atomic operations. This type of kernel provides a trade-off between latency and stability, but it requires careful identification and minimization of the non-preemptible sections .
- A real-time kernel has several components, such as:
  - Scheduler: The component that decides which task to run next, based on the priority, deadline, and resource requirements of the tasks.
  - Interrupt handler: The component that responds to hardware or software interrupts, and invokes the appropriate service routine or task.
  - Timer: The component that provides periodic or one-shot timers, and generates timer interrupts to trigger tasks or events.
  - Memory manager: The component that allocates and deallocates memory for tasks, data, and kernel structures.
  - Synchronization primitives: The component that provides mechanisms for mutual exclusion, synchronization, and communication among tasks, such as semaphores, mutexes, message queues, or signals.
  - System calls: The component that provides an interface for tasks to access kernel services, such as task creation, termination, suspension, or resumption.



# Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, especially for applications that have strict timing constraints.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel can provide features such as multitasking, inter-task communication, synchronization, memory management, and interrupt handling.
- A real-time kernel can be classified into two types: preemptive and cooperative.
  - A preemptive kernel allows a task to be interrupted by a higher priority task at any time, thus ensuring that the highest priority task is always running.
  - A cooperative kernel requires a task to voluntarily relinquish the CPU to allow other tasks to run, thus avoiding the overhead of context switching.
- A real-time kernel can also be distinguished by the level of determinism it provides.
  - A hard real-time kernel guarantees that a task will meet its deadline, regardless of the system load or the occurrence of interrupts.
  - A soft real-time kernel tries to meet the deadlines of tasks, but does not guarantee it, and may tolerate some degree of latency or jitter.
- A real-time kernel can be implemented in different ways, such as in kernel space or in user space.
  - A kernel space real-time kernel runs as part of the operating system, and has direct access to the hardware and the system resources.
  - A user space real-time kernel runs as a separate process, and relies on the operating system to provide access to the hardware and the system resources.
- A real-time kernel can be used for various applications, such as industrial control, robotics, multimedia, gaming, and embedded systems  .



# Graph Based Models for Real Time Kernel Basics

- A graph is a data structure that consists of a set of nodes (or vertices) and a set of edges (or links) that connect pairs of nodes.
- A graph can be used to model various kinds of real-time systems, such as networks, sensors, processes, tasks, etc.
- A graph kernel is a function that measures the similarity of pairs of graphs, based on their structure, attributes, or labels.
- A graph kernel can be used to apply kernelized learning algorithms, such as support vector machines, to graphs, without having to extract fixed-length, real-valued feature vectors from them.
- A graph kernel can be computed by various methods, such as counting common subgraphs, comparing graph spectra, or aggregating node features.
- A graph kernel can be used to perform predictive learning tasks, such as classification, regression, or clustering, on graphs or graph nodes.
- A graph kernel can also be used to analyze the properties of real-time kernels, such as schedulability, performance, or robustness.
- A real-time kernel is a software component that manages the time and resources of a CPU or MPU in a real-time system.
- A real-time kernel can be identified by the rt keyword in the kernel version, as shown by the uname -r command.
- A real-time kernel can provide various mechanisms, such as priority-based scheduling, preemption, synchronization, interrupt handling, or memory management, to ensure the timely execution of real-time tasks.
- A real-time kernel can be classified into two types: hard real-time and soft real-time, depending on the degree of tolerance for deadline misses.
- A real-time kernel can be evaluated by various metrics, such as latency, jitter, throughput, or utilization, to measure its quality of service.



# Petri net models for embedded systems

- A Petri net is a graphical and mathematical model that can be used to describe the behaviour of concurrent and distributed systems.
- A Petri net consists of places, transitions, arcs, and tokens. Places represent the states or conditions of the system, transitions represent the events or actions that change the system, arcs connect places and transitions, and tokens represent the resources or data of the system.
- A Petri net can be used to model embedded systems, which are systems that interact with the physical world and have limited resources, such as memory, power, and processing speed.
- Petri net models can capture the features of embedded systems, such as concurrency, synchronization, communication, timing, and hierarchy.
- Some examples of Petri net models for embedded systems are:

  - PRES, which stands for Petri net based Representation for Embedded Systems, is an extension of the classical Petri nets that includes timing information, data transformation, and hierarchical decomposition.
  - PRES+, which is an improvement of PRES that supports the concept of modules, which are reusable components that can be composed to form larger systems.
  - IPNES, which stands for Interpreted Petri Nets for Embedded Systems, is a new model that allows describing both single-module and distributed systems that require process synchronization and data exchange .

- Petri net models can be used for the design, analysis, and verification of embedded systems, as they can express the functional and non-functional requirements, detect and avoid errors, and generate code or hardware.



# Real time languages for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real time language is a programming language that supports the development of real time systems, which are systems that must respond to events within strict time constraints.
- Real time languages typically provide features such as concurrency, synchronization, memory management, scheduling, and exception handling, that are tailored for real time applications.
- Some examples of real time languages are:

  - Ada: A general-purpose language that supports concurrency, object-orientation, generics, and exception handling. Ada has a subset called Ravenscar that is designed for high-integrity real time systems.
  - C: A low-level language that is widely used for embedded systems development. C has several extensions and libraries that support real time programming, such as POSIX, MISRA C, and RTOS APIs.
  - C++: An object-oriented language that is based on C, with additional features such as inheritance, polymorphism, templates, and exceptions. C++ also has extensions and libraries for real time programming, such as Real-Time C++ and Boost.
  - Java: An object-oriented language that runs on a virtual machine, with features such as garbage collection, threads, and exceptions. Java has a subset called Real-Time Specification for Java (RTSJ) that defines extensions for real time systems, such as real time threads, memory areas, and scheduling.
  - Rust: A modern language that focuses on safety and concurrency, with features such as ownership, borrowing, traits, and macros. Rust has a subset called Embedded Rust that is suitable for real time embedded systems, with support for low-level hardware access, no-std libraries, and RTOS APIs.

- Real time languages are used to implement the real time kernel, which is the core component of a real time operating system (RTOS).
- A real time kernel provides the basic services and mechanisms for managing the execution of real time tasks, such as:

  - Task management: The creation, deletion, activation, and termination of real time tasks, which are units of execution that have specific timing requirements and priorities.
  - Scheduling: The allocation of processor time to ready tasks, according to a predefined scheduling policy, such as rate-monotonic, earliest-deadline-first, or priority-based.
  - Synchronization: The coordination of concurrent tasks that share resources or communicate with each other, using primitives such as semaphores, mutexes, message queues, and events.
  - Interrupt handling: The processing of external or internal events that trigger the execution of interrupt service routines (ISRs), which are special tasks that have the highest priority and preempt the normal tasks.
  - Memory management: The allocation and deallocation of memory for tasks and data structures, using techniques such as static, dynamic, or hybrid memory allocation, and memory protection or partitioning.
  - Time management: The measurement and control of time, using timers, clocks, and counters, and providing services such as delays, timeouts, and periodic activations.

- A real time kernel can be implemented in different ways, such as:

  - Monolithic kernel: A single program that runs in privileged mode and provides all the kernel services and mechanisms, as well as device drivers and system calls.
  - Microkernel: A minimal program that runs in privileged mode and provides only the essential kernel services and mechanisms, such as task management and inter-process communication, while the other services and mechanisms are implemented by user-level processes or servers.
  - Exokernel: A thin layer that runs in privileged mode and provides only the low-level hardware access and protection, while the other services and mechanisms are implemented by user-level libraries or applications.



# Real Time Kernel

A real time kernel is a software component that manages the time and resources of a CPU or MPU in a way that ensures predictable and deterministic behavior. A real time kernel is often used in embedded systems and real time operating systems that have strict timing requirements and need to respond quickly to external events.

Some of the main concepts and features of a real time kernel are:

- **Task**: A task is a basic unit of execution that runs on the CPU. A task can be a thread, a process, or a function. A task can have different states, such as ready, running, blocked, or suspended. A task can also have different attributes, such as priority, stack size, or deadline.
- **Scheduler**: A scheduler is a component that decides which task to run on the CPU at any given time. A scheduler can use different algorithms, such as round-robin, priority-based, or earliest deadline first. A scheduler can also be preemptive or cooperative. A preemptive scheduler can interrupt a running task to switch to a higher priority task, while a cooperative scheduler requires a running task to voluntarily yield the CPU to another task.
- **Interrupt**: An interrupt is a signal that notifies the CPU of an external event that requires immediate attention. An interrupt can be generated by hardware devices, such as timers, sensors, or keyboards, or by software, such as system calls or exceptions. An interrupt can cause the CPU to save the current context of the running task and jump to an interrupt handler, which is a special function that performs the necessary actions to service the interrupt.
- **Semaphore**: A semaphore is a synchronization mechanism that controls the access to a shared resource by multiple tasks. A semaphore can be binary or counting. A binary semaphore can have only two values, 0 or 1, and can be used to implement mutual exclusion or signaling. A counting semaphore can have any non-negative value and can be used to implement resource allocation or synchronization.
- **Message Queue**: A message queue is a communication mechanism that allows tasks to exchange data or messages. A message queue can have a fixed or variable size and can store messages of different types or lengths. A message queue can be used to implement inter-task communication, data buffering, or event notification.



# OS Tasks for the Notes of the Unit 3 - Real Time Kernel Basics in the Subject of Embedded Systems and Real Time Operating Systems

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. A task is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the embedded OS that decides which task should run at any given time. The task scheduler can use different algorithms to make this decision, such as priority-based, round-robin, or preemptive.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their deadlines, which are the time constraints imposed by the application or the environment.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time. A hard real-time kernel ensures that tasks will never miss their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel can provide various services to tasks, such as task creation, deletion, synchronization, communication, and timing.



# Task States for the Notes of the Unit 3 - Real Time Kernel Basics

- A task is a unit of execution in a real time operating system (RTOS) that can be scheduled and preempted by the kernel .
- A task state is the condition of a task at a given point of time, which determines its readiness and eligibility to run on the processor  .
- The task state consists of a snapshot of all the processor registers, along with an individual heap and stack memory allocation for each task.
- The task state can change due to various events, such as system timer interrupts, task creation and deletion, task synchronization and communication, task priority changes, etc .
- The common task states in a real time kernel are:

  - **Running**: The task is currently executing on the processor or is ready to execute on the processor as soon as it gets the opportunity  . This is the only possible state for a task executing in user space. It can also apply to a task in kernel space that is actively running.
  - **Ready**: The task is not running but is eligible to run as soon as the processor becomes available or a higher priority task finishes its execution . The ready tasks are usually maintained in a run queue according to their priorities .
  - **Blocked**: The task is not running and is not eligible to run until a certain event occurs, such as a timer expiration, a semaphore release, a message arrival, etc . The blocked tasks are usually maintained in a wait queue according to the event they are waiting for .
  - **Suspended**: The task is not running and is not eligible to run until another task explicitly resumes it . The suspended tasks are usually maintained in a separate list . Suspension is a way of temporarily disabling a task without deleting it .
  - **Terminated**: The task is not running and is not eligible to run ever again, as it has completed its execution or has been deleted by another task . The terminated tasks are usually removed from the system and their resources are freed .

- The task state diagram shows the possible transitions between the task states and the events that cause them:

Task State Diagram

: https://forum.arduino.cc/t/what-is-task-state-in-real-time-operating-system/651877
: http://www.on-time.com/rtkernel-dos.htm
: https://www.humblec.com/proccess-states-in-linux-kernel/
: https://www.redhat.com/sysadmin/real-time-kernel
: https://en.wikipedia.org/wiki/Sun#:~:text=The%20core%20of%20the%20Sun%20extends%20from%20the,the%20Sun%27s%20surface%20temperature%20is%20approximately%205800%20K.
: https://www.freertos.org/a00015.html



# Task scheduling for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Task scheduling is the process of determining how the various tasks are executed by the operating system in a real time system .
- A real time system is a system that has to respond to events within a specified time limit .
- A real time operating system (RTOS) is an operating system that supports real time applications by providing features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization .
- A task is a unit of work that can be executed by the RTOS. A task can be periodic, aperiodic or sporadic, depending on its arrival pattern and deadline .
- A periodic task is a task that arrives at regular intervals and has a fixed deadline equal to its period .
- An aperiodic task is a task that arrives at irregular intervals and has a variable deadline .
- A sporadic task is a task that arrives at unpredictable intervals and has a minimum inter-arrival time and a fixed deadline .
- A task scheduler is a component of the RTOS that decides which task to run at any given time, based on some criteria such as priority, deadline, resource availability, etc  .
- There are different types of task scheduling algorithms for real time systems, such as    :
  - Run to completion (RTC): A simple scheduler that runs each task until it finishes or blocks, without preemption. It is suitable for systems with low task complexity and low concurrency .
  - Round robin (RR): A scheduler that runs each task for a fixed time slice and then switches to the next task in a circular order. It is suitable for systems with equal priority tasks and high concurrency .
  - Time slice (TS): A scheduler that runs each task for a fixed time slice and then switches to the next task in order of priority. It is a preemptive scheduler that can handle tasks with different priorities and deadlines .
  - Time slice with background task (TSBG): A scheduler that runs each task for a fixed time slice and then switches to the next task in order of priority, except for the lowest priority task, which is run only when no other task is ready. It is a preemptive scheduler that can handle tasks with different priorities and deadlines, as well as a background task that can perform low-priority work .
  - Priority (PRI): A scheduler that runs the highest priority task that is ready at any time, and preempts any lower priority task that is running. It is a preemptive scheduler that can handle tasks with different priorities and deadlines, but may suffer from priority inversion or starvation problems .
  - Earliest deadline first (EDF): A scheduler that runs the task that has the earliest absolute deadline at any time, and preempts any task that has a later deadline. It is a preemptive scheduler that can handle tasks with different periods and deadlines, but may suffer from overload or deadline misses problems  .
  - Rate monotonic (RM): A scheduler that assigns a fixed priority to each task based on its period, such that the shorter the period, the higher the priority. It is a preemptive scheduler that can handle periodic tasks with different periods and deadlines, but may suffer from priority inversion or deadline misses problems  .
  - Least laxity first (LLF): A scheduler that runs the task that has the least laxity at any time, and preempts any task that has a greater laxity. The laxity of a task is the difference between its deadline and its remaining execution time. It is a preemptive scheduler that can handle tasks with different periods and deadlines, but may suffer from overload or deadline misses problems  .



# Interrupt Processing

- An interrupt is a signal from a hardware device or a software program that requests the attention of the CPU.
- Interrupts are used to handle events that require immediate or timely response from the CPU, such as keyboard input, mouse movement, network packets, timers, etc.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are generated by external devices, such as keyboards, mice, disks, network cards, etc. They are delivered to the CPU through a network of interrupt controllers and interrupt lines.
- Software interrupts are generated by software programs, such as system calls, exceptions, traps, etc. They are delivered to the CPU through instructions or signals.
- Interrupts can also be classified into two types based on their priority: maskable interrupts and non-maskable interrupts.
- Maskable interrupts are those that can be disabled or enabled by the CPU using special instructions or registers. They are used for normal or low-priority events that can be deferred or ignored if necessary.
- Non-maskable interrupts are those that cannot be disabled or enabled by the CPU. They are used for critical or high-priority events that must be handled immediately and cannot be deferred or ignored.
- When an interrupt occurs, the CPU suspends its current execution and saves its state (such as program counter, registers, flags, etc.) on the stack. Then, it jumps to a predefined address in memory where the interrupt handler or the interrupt service routine (ISR) is located. The ISR is a small program that performs the necessary actions to service the interrupt, such as reading or writing data, sending or receiving signals, acknowledging or clearing the interrupt, etc. After the ISR is finished, the CPU restores its state from the stack and resumes its previous execution.
- Interrupts can affect the performance and predictability of real-time systems, as they introduce latency, jitter, and overhead in the execution of tasks. Therefore, real-time kernels must handle interrupts efficiently and effectively to meet the timing constraints and quality of service requirements of real-time applications.
- Real-time kernels can use different strategies to handle interrupts, such as:
  - Assigning interrupts to real-time threads. In this approach, each interrupt is associated with a real-time thread that runs at a fixed priority. When an interrupt occurs, the kernel dispatches the corresponding thread to service the interrupt. This allows the kernel to handle multiple interrupts concurrently and to preempt lower-priority threads if necessary. However, this approach also introduces context switching and scheduling overhead, as well as potential priority inversion problems.
  - Using a dual-kernel or a co-kernel. In this approach, the system uses two kernels: a standard kernel for non-real-time processes and a specialized kernel for real-time processes. The co-kernel handles all the interrupts and executes the ISRs at the highest priority. The standard kernel handles the non-real-time processes and executes them at lower priorities. This allows the co-kernel to ensure that the interrupts are serviced promptly and predictably, without being affected by the standard kernel. However, this approach also introduces complexity and synchronization issues, as well as potential resource contention problems.
  - Using a nanokernel or a microkernel. In this approach, the system uses a minimal kernel that handles only the interrupts and the basic hardware operations. The nanokernel forwards the interrupts to the appropriate kernel module or user space process, depending on the type and source of the interrupt. This allows the system to handle the interrupts flexibly and dynamically, without being constrained by a fixed priority scheme. However, this approach also introduces latency and overhead, as the interrupts have to pass through the nanokernel and the kernel module or user space process.



# Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time in the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts, and can be accessed by the kernel or the user space applications. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The hardware clock and the software clock may not be synchronized, especially if the system is subject to clock drift, frequency scaling, or time adjustments. Therefore, the kernel provides different interfaces for accessing different types of clocks, such as:

- `clock_gettime()`: This is a system call that returns the current value of a specified clock. The clock can be one of the following constants :
  - `CLOCK_REALTIME`: This is the clock that corresponds to the hardware clock, and reflects the wall clock time. This clock can be set or adjusted by the user or by a network time protocol (NTP) daemon.
  - `CLOCK_MONOTONIC`: This is the clock that corresponds to the software clock, and reflects the elapsed time since the system was booted. This clock cannot be set or adjusted by the user, and is not affected by changes in the hardware clock.
  - `CLOCK_REALTIME_HR`: This is a high resolution version of `CLOCK_REALTIME`, which provides nanosecond precision. This clock may not be available on all platforms.
  - `CLOCK_MONOTONIC_HR`: This is a high resolution version of `CLOCK_MONOTONIC`, which provides nanosecond precision. This clock may not be available on all platforms.
- `gettimeofday()`: This is a system call that returns the current value of the `CLOCK_REALTIME` clock, along with the time zone information. This system call is obsolete and should be replaced by `clock_gettime()`.
- `time()`: This is a library function that returns the current value of the `CLOCK_REALTIME` clock, in seconds since the Unix epoch (January 1, 1970). This function is less precise than `clock_gettime()` and does not provide the time zone information.
- `rtc_read_time()`: This is a kernel function that reads the current value of the hardware clock, and returns it as a `struct rtc_time` structure. This function is used by the kernel to initialize or update the software clock.
- `rtc_set_time()`: This is a kernel function that writes the current value of the software clock to the hardware clock. This function is used by the kernel to synchronize the hardware clock with the software clock.

Clocking is important for real time kernels because it enables the following features:

- **Scheduling**: The kernel uses the software clock to determine when to switch between tasks, and to enforce deadlines and priorities. The kernel also uses the hardware clock to implement periodic or absolute timers, and to wake up tasks that are sleeping or waiting for events.
- **Timing**: The kernel and the user space applications use the clocks to measure the execution time and the latency of tasks, and to generate timestamps and logs. The clocks also help to synchronize the system with external devices or networks that rely on a common time reference.
- **Performance analysis**: The kernel and the user space applications use the clocks to collect and report statistics and metrics about the system's behavior and performance, and to identify and diagnose bottlenecks and anomalies. The clocks also help to compare and evaluate different configurations and algorithms.



# Communication and Synchronization

Communication and synchronization are two important aspects of real-time kernel design. They allow tasks to exchange information and coordinate their execution in a timely and predictable manner.

## Communication

Communication is the process of transferring data or messages between tasks. There are two main types of communication: shared memory and message passing.

### Shared memory

Shared memory is a communication method that uses a common memory area that is accessible by all tasks. Tasks can read or write data to the shared memory using pointers or variables. Shared memory is fast and simple, but it requires careful synchronization to avoid data inconsistency or race conditions.

### Message passing

Message passing is a communication method that uses explicit messages to transfer data between tasks. Tasks can send or receive messages using system calls or library functions. Message passing is more flexible and modular, but it requires more overhead and complexity.

## Synchronization

Synchronization is the process of controlling the order and timing of task execution. There are two main types of synchronization: mutual exclusion and event synchronization.

### Mutual exclusion

Mutual exclusion is a synchronization method that ensures that only one task can access a shared resource at a time. Mutual exclusion prevents data corruption or deadlock, but it may introduce blocking or priority inversion. Mutual exclusion can be implemented using various mechanisms, such as semaphores, mutexes, monitors, or locks.

### Event synchronization

Event synchronization is a synchronization method that allows tasks to wait for or signal the occurrence of certain events. Event synchronization enables tasks to coordinate their execution based on the state of the system or the environment. Event synchronization can be implemented using various mechanisms, such as flags, signals, events, or condition variables.



# Control Blocks for the Notes of the Unit 3 - Real Time Kernel Basics

- A control block is a data structure that contains information about a system entity, such as a process, a task, a file, a device, etc.
- A control block is used by the operating system or the kernel to manage and control the entity, such as creating, terminating, scheduling, communicating, etc.
- A control block typically has a unique identifier, a state, a priority, and other attributes that are relevant to the entity.
- In a real time kernel, a control block is often used to represent a real time task, which is a unit of execution that performs a specific function in a real time system.
- A real time task control block (TCB) has information about the task id, the task state, the task priority, the task deadline, the task stack, the task context, the task resources, the task events, the task timers, etc.
- A real time task control block is created by the kernel when a task is created, and is deleted by the kernel when a task is terminated.
- A real time task control block is updated by the kernel when a task changes its state, priority, deadline, resources, events, timers, etc.
- A real time task control block is used by the kernel to select the next task to run, to switch the context between tasks, to handle the interrupts and exceptions, to synchronize and communicate between tasks, to monitor and enforce the timing constraints, etc.
- A real time task control block is usually stored in a protected memory area that is inaccessible by the normal user tasks, to prevent unauthorized or accidental modification or corruption of the task information.
- A real time task control block is usually located at the beginning of the kernel stack for the task, as it is a safe and convenient location for the kernel to access and manipulate the task information.



# Memory Requirements and Control for Real Time Kernel

- A real time kernel is a special type of kernel that provides deterministic and predictable behavior for real time applications that require low latency and high responsiveness.
- A real time kernel has to manage the memory resources efficiently and safely, as memory is a critical resource for real time systems.
- Some of the memory requirements and control techniques for real time kernel are:

  - **Memory allocation**: The real time kernel has to allocate memory for processes, threads, data structures, buffers, etc. The memory allocation can be static or dynamic, depending on the design and requirements of the system. Static allocation is done at compile time or boot time, and it avoids memory fragmentation and allocation overhead. Dynamic allocation is done at run time, and it allows more flexibility and adaptability, but it introduces memory fragmentation and allocation overhead. The real time kernel has to use appropriate memory allocation algorithms and data structures to minimize the memory allocation latency and maximize the memory utilization.
  - **Memory protection**: The real time kernel has to protect the memory from unauthorized or erroneous access by processes, threads, devices, etc. The memory protection can be done by using hardware mechanisms, such as memory management unit (MMU), or software mechanisms, such as memory mapping, segmentation, or paging. The memory protection can prevent memory corruption, memory leaks, memory faults, etc. The real time kernel has to use appropriate memory protection mechanisms to ensure the memory integrity and security.
  - **Memory reservation**: The real time kernel has to reserve memory for critical processes, threads, or devices that require guaranteed memory availability and performance. The memory reservation can be done by using hugepages, which are large contiguous blocks of memory that are pre-allocated and pinned in physical memory. The memory reservation can reduce the memory access latency and improve the memory throughput by avoiding page faults, page swapping, or page migration. The real time kernel has to use appropriate memory reservation techniques to ensure the memory quality of service (QoS) for real time workloads.
  - **Memory tuning**: The real time kernel has to tune the memory parameters and settings to optimize the memory performance and behavior for real time systems. The memory tuning can be done by adjusting the kernel boot parameters, kernel configuration options, kernel runtime parameters, or user space parameters. The memory tuning can affect the memory allocation, protection, reservation, and management policies and strategies. The real time kernel has to use appropriate memory tuning techniques to achieve the desired memory performance and behavior for real time systems .



# Kernel Services

- The kernel is the core component of an operating system that provides basic services for all other parts of the OS.
- The kernel is typically a small, highly optimized set of libraries that offer an abstraction layer between the OS and the underlying hardware.
- The kernel is responsible for tasks such as process and memory management, file systems, device control, interrupt handling, networking, and time management.
- In a real-time operating system (RTOS), the kernel is designed to meet the requirements of real-time computing applications that process data and events that have critically defined time constraints.
- An RTOS kernel must provide predictable and deterministic behavior, meaning that the system must respond to inputs and outputs within a known and bounded time frame.
- An RTOS kernel must also support concurrency and parallelism, meaning that the system must be able to execute multiple tasks simultaneously and efficiently.
- An RTOS kernel implements a micro-kernel architecture, which means that it provides only the essential functionalities and allows the user to configure the rest of the services according to the application needs.
- The common services that an RTOS kernel provides to the application software are:

  - Task management: The kernel creates, deletes, suspends, resumes, and prioritizes tasks that run on the system.
  - Task scheduling: The kernel allocates CPU time to the tasks based on their priorities and deadlines, using algorithms such as preemptive, cooperative, or hybrid scheduling.
  - Task synchronization: The kernel coordinates the access and sharing of resources among the tasks, using mechanisms such as semaphores, mutexes, message queues, and events.
  - Memory management: The kernel allocates and deallocates memory for the tasks and the kernel itself, using techniques such as static, dynamic, or hybrid memory allocation.
  - Time management: The kernel keeps track of the system time and provides timers and delays for the tasks, using hardware or software clocks and interrupts.
  - Interrupt handling: The kernel handles the interrupts from the hardware devices and the software events, using interrupt service routines (ISRs) and interrupt handlers.
  - Device I/O management: The kernel manages the input and output operations of the hardware devices, using drivers and interfaces.



# Basic Design using RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system; it creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides a multi-tasking and deterministic run-time environment, which means that tasks can be executed in a predictable and timely manner.
- An RTOS can be used to design embedded systems that have real-time constraints, such as deadlines, response times, throughput, etc.
- Some basic design principles using RTOS are:

  - Write short interrupt routines, but not too short. Interrupt routines should perform the minimum necessary work and then return to the main program or signal a task to handle the rest.
  - Use a suitable number of tasks. Too many tasks can increase the overhead of context switching, data sharing, synchronization, and communication. Too few tasks can reduce the modularity, readability, and maintainability of the code.
  - Avoid creating and destroying tasks while the system is running, because it is time consuming and may cause memory leaks or fragmentation. It may be better to create all the tasks at system startup and leave them suspended or dormant until they are needed.
  - Use RMS to verify your design. RMS, or Rate Monotonic Scheduling, is an analysis technique that can help you determine the feasibility of your task set and the optimal priority assignment for each task.
  - Use appropriate synchronization and communication mechanisms. Depending on the RTOS, you may have access to different types of primitives, such as semaphores, mutexes, queues, mailboxes, pipes, etc. Choose the ones that best suit your needs and avoid common pitfalls, such as priority inversion, deadlock, starvation, etc.



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



# VxWorks/ Free RTOS Scheduling and Task Management

- VxWorks and Free RTOS are two popular real-time operating systems (RTOS) that are used for embedded systems and real-time applications.
- Scheduling and task management are two important aspects of RTOS that determine how the system allocates CPU time and resources to different tasks or processes.
- A task is a basic unit of execution in an RTOS. A task can have different attributes, such as priority, state, stack, and context.
- A scheduler is a component of the RTOS kernel that decides which task to run next based on some criteria, such as task priority, deadline, or fairness.
- A task management system is a component of the RTOS kernel that creates, deletes, suspends, resumes, and controls the tasks in the system.

## VxWorks Scheduling and Task Management

- VxWorks is a deterministic, priority-based preemptive RTOS with low latency and minimal jitter.
- VxWorks supports both POSIX and a proprietary scheduling mechanism (wind scheduling). Both preemptive priority and round-robin scheduling mechanism are available.
- VxWorks uses 256 priority levels, where 0 is the highest and 255 is the lowest. When a task with a higher priority is ready to run, the current task running is preempted. The lower priority task's context is saved and the kernel loads the context of the new task.
- In preemptive priority-based scheduling, the first-come first-served (FCFS) rule is used when tasks with the same priority want to use the CPU. In round-robin scheduling, ready tasks with the same priority share the CPU equally for a fixed time slice.
- VxWorks provides a set of APIs for task management, such as taskSpawn, taskDelete, taskSuspend, taskResume, taskPrioritySet, taskDelay, and taskLock.
- VxWorks also supports inter-task communication and synchronization mechanisms, such as semaphores, message queues, pipes, signals, and events.

## Free RTOS Scheduling and Task Management

- Free RTOS is a portable, open source, mini real time kernel that is designed for small embedded systems.
- Free RTOS supports preemptive or cooperative scheduling, where tasks can voluntarily yield the CPU or be preempted by higher priority tasks.
- Free RTOS uses 256 priority levels, where 0 is the lowest and 255 is the highest. The scheduler always runs the highest priority task that is ready to run.
- Free RTOS provides a set of APIs for task management, such as xTaskCreate, vTaskDelete, vTaskSuspend, vTaskResume, vTaskPrioritySet, vTaskDelay, and vTaskSuspendAll.
- Free RTOS also supports inter-task communication and synchronization mechanisms, such as queues, semaphores, mutexes, event groups, and software timers.



# Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and execution times to tasks in a real-time system, such that the system can meet its timing constraints and performance goals.
- A real-time operating system (RTOS) is a software platform that provides the core functionality for a real-time system, such as task management, inter-task communication, timing and synchronization, interrupt handling, memory management, and device drivers.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.

## VXWORKS

- VXWORKS is a commercial RTOS developed by Wind River Systems, Inc. It supports various architectures, such as x86, ARM, PowerPC, MIPS, and SPARC, and various platforms, such as aerospace, defense, industrial, medical, and automotive.
- VXWORKS provides a preemptive priority-based scheduler, which allows the user to assign up to 256 priority levels to tasks. The scheduler always runs the highest priority ready task, and preempts the current task if a higher priority task becomes ready.
- VXWORKS also supports various scheduling policies, such as round-robin, time-slicing, and deadline-based scheduling, which can be applied to tasks with the same priority level. The user can configure the scheduling policy and the time slice for each task.
- VXWORKS provides various kernel services and features, such as task creation, deletion, suspension, and resume, task stack overflow detection, task information query, task hook routines, inter-task communication mechanisms (such as message queues, semaphores, mutexes, and events), timers, interrupts, memory management, and device drivers.

## FREE RTOS

- FREE RTOS is an open source RTOS developed by Richard Barry and maintained by Amazon Web Services. It supports various architectures, such as x86, ARM, AVR, PIC, and MSP430, and various platforms, such as IoT, automotive, industrial, and medical.
- FREE RTOS provides a preemptive priority-based scheduler, which allows the user to assign up to 255 priority levels to tasks. The scheduler always runs the highest priority ready task, and preempts the current task if a higher priority task becomes ready.
- FREE RTOS also supports round-robin scheduling, which can be applied to tasks with the same priority level. The user can configure the time slice for each task.
- FREE RTOS provides the core real-time scheduling functionality, inter-task communication mechanisms (such as message queues, semaphores, mutexes, and events), timing and synchronization primitives (such as timers, delays, and tick hooks), and memory management. Additional features, such as a command console interface and network stack, can be included as add-ons.



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



# Intertask Communication for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Intertask communication is the process of exchanging data or signals between tasks in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources, data or events.
- Intertask communication can also be used to implement concurrency, parallelism, synchronization and mutual exclusion in a multitasking system.
- VXWORKS and FREE RTOS are two popular RTOS that support various methods of intertask communication.

## VXWORKS Intertask Communication

- VXWORKS supports several different methods for intertask communication . They are:
  - Shared memory: Tasks can access a common memory region to read or write data. Shared memory is fast and simple, but requires explicit synchronization and mutual exclusion mechanisms to avoid data corruption or inconsistency.
  - Message queues: Tasks can send and receive messages of fixed or variable size through message queues. Message queues are thread-safe and can be used to communicate between user space and kernel space tasks. Message queues can also be used to implement priority inheritance and priority ceiling protocols to avoid priority inversion.
  - Pipes: Tasks can send and receive data streams through pipes. Pipes are similar to message queues, but they do not preserve message boundaries. Pipes are useful for transferring large amounts of data or binary data.
  - Signals: Tasks can send and receive signals to notify each other of events or conditions. Signals are asynchronous and can interrupt the execution of the receiving task. Signals can also be used to implement timers, alarms or exceptions.

## FREE RTOS Intertask Communication

- FREE RTOS can easily be extended to include other intertask communication mechanisms in the same manner. As all communication mechanisms are based on the same underlying queue concept, the API functions provided for each mechanism are in fact relatively interoperable. The intertask communication methods supported by FREE RTOS are:
  - Queues: Queues are the primary form of intertask communication in FREE RTOS. They can be used to send messages between tasks, and between interrupts and tasks. Queues are thread-safe and can be used to implement blocking or non-blocking communication. Queues can also be used to implement semaphores and mutexes.
  - Semaphores: Semaphores are a special type of queue that can be used to synchronize or coordinate the execution of tasks. Semaphores can be binary or counting, depending on the number of resources or events they represent. Semaphores can also be used to implement mutual exclusion or critical sections.
  - Mutexes: Mutexes are a special type of binary semaphore that can be used to protect shared resources or data from concurrent access by multiple tasks. Mutexes can also be used to implement priority inheritance and priority ceiling protocols to avoid priority inversion. Mutexes can also be recursive, allowing a task to take the same mutex multiple times.



# Pipes for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional way.
- Pipes are often implemented as circular buffers or queues that can store a fixed amount of data until it is read by the receiver or overwritten by the sender.
- Pipes can be used to implement various communication patterns, such as producer-consumer, client-server, or filter-chain.
- Pipes can be either named or unnamed, depending on whether they have a unique identifier in the file system or not.
- Pipes can be either blocking or non-blocking, depending on whether they wait for data to be available or not.

## Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that is widely used in embedded systems and critical applications.
- VxWorks supports pipes as a form of IPC, along with other mechanisms such as message queues, semaphores, signals, shared memory, and sockets.
- VxWorks pipes are implemented as message queues with a fixed message size of one byte, which means they can only transfer byte streams.
- VxWorks pipes can be created with the pipeDevCreate() function, which takes the name, maximum number of bytes, and options as parameters.
- VxWorks pipes can be opened with the open() function, which returns a file descriptor that can be used to read or write data with the read() or write() functions.
- VxWorks pipes can be closed with the close() function, which releases the file descriptor and the resources associated with the pipe.
- VxWorks pipes can be deleted with the pipeDevDelete() function, which removes the pipe from the file system and frees the memory allocated for it.
- VxWorks pipes can be configured with the ioctl() function, which can set or get various attributes of the pipe, such as the blocking mode, the number of bytes available, or the number of readers or writers.
- VxWorks pipes can be used to communicate between tasks within the same or different processes, or between processes and device drivers.

## Pipes in FreeRTOS

- FreeRTOS is another RTOS that is designed for small and simple embedded systems.
- FreeRTOS does not support pipes as a native form of IPC, but it provides a similar feature called stream buffers.
- Stream buffers are circular buffers that can store variable-length messages or byte streams, and can be used to transfer data between tasks or between tasks and interrupts.
- Stream buffers can be created with the xStreamBufferCreate() function, which takes the buffer size and the trigger level as parameters.
- Stream buffers can be written to with the xStreamBufferSend() function, which takes the buffer handle, the data pointer, the data length, and the block time as parameters.
- Stream buffers can be read from with the xStreamBufferReceive() function, which takes the buffer handle, the data pointer, the data length, and the block time as parameters.
- Stream buffers can be deleted with the vStreamBufferDelete() function, which takes the buffer handle as a parameter.
- Stream buffers can be queried with the xStreamBufferBytesAvailable() function, which returns the number of bytes available in the buffer, or the xStreamBufferSpacesAvailable() function, which returns the number of free spaces in the buffer.
- Stream buffers can be used to communicate between tasks within the same or different processes, or between tasks and interrupts.



# Semaphore for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A semaphore is a synchronization object that can be used to control access to a shared resource by multiple tasks or processes  .
- A semaphore has an internal variable that represents the state of the semaphore, such as available or taken .
- A semaphore can be binary or counting. A binary semaphore can only have two states: 0 or 1. A counting semaphore can have any non-negative integer value .
- A semaphore can be created, taken, given, and deleted using the FreeRTOS and VxWorks APIs   .
- A task can take a semaphore to gain access to a shared resource or to wait for a signal from another task. A task can give a semaphore to release the access to a shared resource or to send a signal to another task  .
- A task can block on a semaphore if the semaphore is not available when the task tries to take it. The task will be unblocked when the semaphore is given by another task  .
- A semaphore can have different queueing policies, such as FIFO or priority, to determine the order of unblocking the tasks that are waiting for the semaphore .
- A mutex is a special type of binary semaphore that can be used to implement mutual exclusion. A mutex can only be given by the task that took it. A mutex can also have a priority inheritance mechanism to prevent priority inversion  .
- A recursive mutex is a special type of mutex that can be taken multiple times by the same task. The task must give the mutex the same number of times as it took it before the mutex becomes available for other tasks.



# Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive messages by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task that is waiting to receive a message.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task that is waiting to send a message.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.

## Message Queue in VxWorks

- VxWorks provides a message queue library that implements the POSIX message queue standard.
- A message queue can be created using the `mq_open()` function, which returns a descriptor to the queue.
- A message can be sent to a queue using the `mq_send()` function, which copies the message into the queue and notifies any thread that is waiting to receive a message.
- A message can be received from a queue using the `mq_receive()` function, which copies the message from the queue and notifies any thread that is waiting to send a message.
- A message queue can be deleted using the `mq_close()` and `mq_unlink()` functions, which close the descriptor and remove the queue from the system.

## Message Queue in FreeRTOS

- FreeRTOS provides a queue library that is similar to the VxWorks message queue library, but with some differences .
- FreeRTOS does not support the `mq_notify()` function, which notifies a thread when a message is available in the queue.
- FreeRTOS does not support the `mq_setattr()` and `mq_getattr()` functions, which set and get the attributes of the queue.
- FreeRTOS does not use descriptors to identify queues, but handles that are of type `QueueHandle_t`.
- FreeRTOS provides additional functions to query the status of the queue, such as `uxQueueMessagesWaiting()`, `uxQueueSpacesAvailable()`, and `xQueueIsQueueEmptyFromISR()`.



# Signals for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Signals are a form of inter-process communication (IPC) that allow a process to send a notification to another process or to itself.
- Signals can be used to indicate events such as termination, segmentation fault, alarm, user input, etc.
- Signals can be handled by the default handler provided by the operating system, or by a user-defined handler function.
- Signals can be masked or blocked to prevent them from being delivered to a process until they are unmasked or unblocked.
- Signals can be queued or pending if they are sent to a process that is already handling another signal or has blocked the signal.
- Signals can be synchronous or asynchronous depending on whether they are generated by the execution of an instruction or by an external event.

## VXWORKS

- VXWORKS is a real-time operating system (RTOS) that supports signals as one of the IPC mechanisms.
- VXWORKS provides a POSIX-compliant signal API that allows tasks to send and receive signals using functions such as `sigsend()`, `sigqueue()`, `sigwaitinfo()`, `sigaction()`, etc.
- VXWORKS supports 32 signals, numbered from 1 to 32, with predefined names and meanings. For example, `SIGINT` is signal 2, which indicates an interrupt from the keyboard.
- VXWORKS allows tasks to register user-defined handler functions for signals using the `sigaction()` function, which also specifies the signal mask and flags for the handler.
- VXWORKS allows tasks to block or unblock signals using the `sigprocmask()` function, which also returns the previous signal mask of the task.
- VXWORKS allows tasks to wait for signals using the `sigwaitinfo()` function, which also returns the signal number and value of the received signal.
- VXWORKS allows tasks to send signals to other tasks using the `sigsend()` function, which takes the task ID and the signal number as arguments.
- VXWORKS allows tasks to send signals with values to other tasks using the `sigqueue()` function, which takes the task ID, the signal number, and a union of data types as arguments.
- VXWORKS allows tasks to send signals to themselves using the `kill()` function, which takes the task ID and the signal number as arguments.

## FREE RTOS

- FREE RTOS is a real-time operating system (RTOS) that does not support signals as a native IPC mechanism.
- FREE RTOS provides a POSIX-compliant layer called FreeRTOS+POSIX that emulates some of the POSIX features, including signals, using the native FreeRTOS features.
- FREE RTOS supports 32 signals, numbered from 1 to 32, with predefined names and meanings. For example, `SIGINT` is signal 2, which indicates an interrupt from the keyboard.
- FREE RTOS allows tasks to register user-defined handler functions for signals using the `signal()` function, which also returns the previous handler of the signal.
- FREE RTOS allows tasks to block or unblock signals using the `sigprocmask()` function, which also returns the previous signal mask of the task.
- FREE RTOS allows tasks to wait for signals using the `sigwait()` function, which also returns the signal number of the received signal.
- FREE RTOS allows tasks to send signals to other tasks using the `kill()` function, which takes the task ID and the signal number as arguments.
- FREE RTOS does not allow tasks to send signals with values to other tasks, as the `sigqueue()` function is not supported by FreeRTOS+POSIX.
- FREE RTOS allows tasks to send signals to themselves using the `raise()` function, which takes the signal number as an argument.



# Sockets for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A socket is an endpoint of communication between two processes or devices over a network.
- Sockets can be used to send and receive data using different protocols, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that ensures data delivery and error recovery. UDP is an unreliable, connectionless protocol that does not guarantee data delivery or error recovery, but is faster and more efficient.
- Both VXWORKS and FREE RTOS support sockets as a way of implementing network communication.
- VXWORKS is a proprietary, UNIX-like real-time operating system that is widely used in safety-critical applications, such as aerospace, defense, and industrial automation .
- FREE RTOS is an open source, scalable, and thread-safe real-time operating system that can be configured for various embedded systems, from small devices with memory constraints to complex systems with more functions.
- To use sockets in VXWORKS, the following steps are required:
  - Initialize the network stack by calling the usrNetInit() function.
  - Create a socket by calling the socket() function, specifying the domain (AF_INET for IPv4), the type (SOCK_STREAM for TCP or SOCK_DGRAM for UDP), and the protocol (0 for default).
  - Bind the socket to a local address and port by calling the bind() function, passing the socket descriptor, a pointer to a sockaddr_in structure, and the size of the structure.
  - For TCP sockets, listen for incoming connections by calling the listen() function, passing the socket descriptor and the backlog (the maximum number of pending connections).
  - For TCP sockets, accept an incoming connection by calling the accept() function, passing the socket descriptor, a pointer to a sockaddr_in structure, and a pointer to the size of the structure. The function returns a new socket descriptor for the connection.
  - For UDP sockets, no listen or accept functions are needed, as UDP is connectionless.
  - Send data to the remote endpoint by calling the send() function for TCP sockets, or the sendto() function for UDP sockets, passing the socket descriptor, a pointer to the data buffer, the size of the data, the flags (0 for default), and optionally, a pointer to a sockaddr_in structure and the size of the structure for UDP sockets.
  - Receive data from the remote endpoint by calling the recv() function for TCP sockets, or the recvfrom() function for UDP sockets, passing the socket descriptor, a pointer to the data buffer, the size of the buffer, the flags (0 for default), and optionally, a pointer to a sockaddr_in structure and a pointer to the size of the structure for UDP sockets.
  - Close the socket by calling the close() function, passing the socket descriptor.
- To use sockets in FREE RTOS, the following steps are required  :
  - Initialize the network stack by calling the FreeRTOS_IPInit() function, passing the IP address, netmask, gateway address, DNS server address, and MAC address of the device.
  - Create a socket by calling the FreeRTOS_socket() function, specifying the domain (FREERTOS_AF_INET for IPv4), the type (FREERTOS_SOCK_STREAM for TCP or FREERTOS_SOCK_DGRAM for UDP), and the protocol (FREERTOS_IPPROTO_TCP for TCP or FREERTOS_IPPROTO_UDP for UDP).
  - Bind the socket to a local port by calling the FreeRTOS_bind() function, passing the socket handle, a pointer to a FreeRTOS_sockaddr structure, and the size of the structure.
  - For TCP sockets, listen for incoming connections by calling the FreeRTOS_listen() function, passing the socket handle and the backlog (the maximum number of pending connections).
  - For TCP sockets, accept an incoming connection by calling the FreeRTOS_accept() function, passing the socket handle, a pointer to a FreeRTOS_sockaddr structure, and a pointer to the size of the structure. The function returns a new socket handle for the connection.
  - For UDP sockets, no listen or accept functions are needed, as UDP is connectionless.
  - Send data to the remote endpoint by calling the FreeRTOS_send() function for TCP sockets, or the FreeRTOS_sendto() function for UDP sockets, passing the socket handle, a pointer to the data buffer, the size of



# Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and notify the CPU that it should take some action.
- Interrupts can be triggered by hardware devices, such as timers, sensors, keyboards, etc., or by software exceptions, such as division by zero, illegal instruction, etc.
- Interrupts are handled by interrupt service routines (ISRs), which are special functions that run when an interrupt occurs and perform the necessary actions to service the interrupt.
- Interrupts are important for real-time embedded systems, as they allow the system to respond quickly and deterministically to external stimuli and events.
- Interrupts can also be used to wake up blocked tasks in a real-time operating system (RTOS), which are tasks that are waiting for some condition or event to occur before resuming execution.
- Interrupts can affect the performance and behavior of an RTOS, as they can preempt the running task and delay the scheduling of other tasks. Therefore, interrupts need to be managed carefully and efficiently by the RTOS.
- Different RTOSes have different methods and mechanisms to handle interrupts, such as interrupt priority levels, interrupt masking, interrupt nesting, interrupt latency, interrupt synchronization, etc.
- VxWorks and FreeRTOS are two popular RTOSes that are used for embedded systems. They have some similarities and differences in how they handle interrupts.

## VxWorks

- VxWorks is a preemptive, deterministic RTOS that prioritizes real-time embedded applications.
- VxWorks has low latency and minimal jitter, which means that it can respond to interrupts quickly and consistently.
- VxWorks has many security features that address the evolving security threats connected devices face at every stage, from boot-up to operation to data transfer to powered off.
- VxWorks supports multiple interrupt priority levels, which can be configured by the user. Higher priority interrupts can preempt lower priority interrupts, and lower priority interrupts can be masked by higher priority interrupts.
- VxWorks supports interrupt nesting, which means that an ISR can be interrupted by another ISR of higher priority. This allows the system to handle multiple interrupts without losing any interrupt requests.
- VxWorks supports interrupt synchronization, which means that an ISR can communicate with a task or another ISR using semaphores, message queues, signals, etc. This allows the system to coordinate the actions of different components in response to an interrupt.
- VxWorks supports interrupt-driven task activation, which means that an ISR can wake up a blocked task using a semaphore, a message queue, a signal, etc. This allows the system to resume the execution of a task that is waiting for an interrupt event.

## FreeRTOS

- FreeRTOS is a free, open-source, and portable RTOS that supports a wide range of embedded platforms.
- FreeRTOS is designed to be simple, small, and scalable, which means that it can run on constrained devices with limited resources.
- FreeRTOS offers various methods to handle interrupts that differ in both latency and the consumption of resources. These methods include, Standard ISR processing, Application Controlled Deferred Interrupt Handling, and Centralised Deferred Interrupt Handling.
- Standard ISR processing is the simplest and fastest method, which involves writing the ISR code directly in the interrupt vector table. This method has the lowest latency, but it also consumes the most resources and can interfere with the RTOS scheduler.
- Application Controlled Deferred Interrupt Handling is a more flexible and efficient method, which involves writing the ISR code in a separate function and calling it from the interrupt vector table using a macro. This method allows the ISR to defer some of its actions to a lower priority task, which reduces the interrupt latency and the resource consumption. However, this method requires the user to manage the synchronization and communication between the ISR and the deferred task.
- Centralised Deferred Interrupt Handling is a more advanced and automated method, which involves using a generic ISR that handles all interrupts and passes the interrupt requests to a queue. This method allows the RTOS to manage the synchronization and communication between the ISR and the deferred task, which simplifies the user code and reduces the interrupt latency and the resource consumption. However, this method requires the user to configure the RTOS tick interrupt and the interrupt queue.
- FreeRTOS supports interrupt-driven task activation, which means that an ISR can wake up a blocked task using a semaphore, a message queue, a signal,



# I/O Systems for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An I/O system is a set of components that enable communication between an embedded system and external devices or users.
- An I/O system typically consists of I/O devices, I/O controllers, I/O drivers, I/O libraries, and I/O applications.
- I/O devices are the physical components that perform input or output operations, such as sensors, actuators, keyboards, displays, etc.
- I/O controllers are the hardware interfaces that connect the I/O devices to the embedded system, such as serial ports, parallel ports, USB ports, etc.
- I/O drivers are the software modules that manage the communication between the I/O controllers and the embedded system, such as device initialization, data transfer, error handling, etc.
- I/O libraries are the software modules that provide a high-level abstraction of the I/O devices and drivers, such as file system, network stack, graphical user interface, etc.
- I/O applications are the software modules that use the I/O libraries to perform specific tasks, such as data acquisition, data processing, data display, etc.

- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOSs) that support I/O systems for embedded systems.
- An RTOS is an operating system that guarantees timely and predictable response to events, such as interrupts, timers, messages, etc.
- An RTOS typically provides features such as multitasking, inter-task communication, synchronization, memory management, exception handling, etc.
- VXWORKS is a commercial RTOS developed by Wind River that is widely used in mission-critical embedded systems, such as aerospace, defense, industrial, medical, etc.
- VXWORKS is a deterministic, priority-based preemptive RTOS that has low latency and minimal jitter  .
- VXWORKS supports various I/O devices and controllers, such as serial, parallel, USB, Ethernet, PCI, etc.
- VXWORKS provides a device driver framework that allows developers to create and integrate custom I/O drivers.
- VXWORKS also provides I/O libraries, such as file system, network stack, graphical user interface, etc., that can be used by I/O applications.

- FREE RTOS is an open-source RTOS developed by Richard Barry that is widely used in embedded systems, such as microcontrollers, IoT devices, etc.
- FREE RTOS can be thought of as a thread library rather than an operating system, although command line interface and POSIX-like I/O abstraction are available.
- FREE RTOS implements multiple threads by having the host program call a thread tick method at regular short intervals.
- FREE RTOS supports various I/O devices and controllers, such as serial, parallel, USB, Ethernet, etc., depending on the hardware platform and the porting layer.
- FREE RTOS provides a device driver framework that allows developers to create and integrate custom I/O drivers.
- FREE RTOS also provides I/O libraries, such as file system, network stack, graphical user interface, etc., that can be used by I/O applications.



# General Architecture of VxWorks

- VxWorks is a real-time operating system (RTOS) that provides deterministic, priority-based preemptive scheduling, low latency, and minimal jitter for embedded systems.
- VxWorks is built on a modular, scalable, and upgradable architecture that supports multiple hardware architectures, such as Intel, Power, ARM, and RISC-V, and multiple processor modes, such as asymmetric multiprocessing (AMP), symmetric multiprocessing (SMP), and mixed modes and multi-OS (via Type 1 hypervisor) on 32- and 64-bit processors .
- VxWorks consists of three main components: the VxWorks kernel, the VxWorks libraries, and the VxWorks applications.
  - The VxWorks kernel is the core of the RTOS that provides the basic services, such as task management, intertask communication, memory management, interrupt handling, timer services, and device drivers.
  - The VxWorks libraries are a set of optional modules that extend the functionality of the kernel, such as networking, file systems, security, graphics, and POSIX compatibility.
  - The VxWorks applications are the user-defined programs that run on top of the kernel and the libraries, and can be written in C, C++, Ada, or Java.
- VxWorks supports a variety of development tools, such as the Wind River Workbench, the Wind River Compiler, the Wind River Debugger, and the Wind River Simics simulator, that enable developers to create, debug, test, and deploy VxWorks applications.
- VxWorks is designed to meet the high standards of safety, security, and reliability for mission-critical computing systems in various domains, such as aerospace and defense, industrial, medical, automotive, and consumer electronics .



# Device Driver Studies for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A device driver is a software component that allows an operating system to communicate with a hardware device, such as a keyboard, mouse, disk, network card, etc.
- A device driver typically implements a standard interface defined by the operating system, such as read, write, open, close, ioctl, etc.
- A device driver may also provide additional functionality specific to the device, such as configuration, calibration, power management, etc.
- A device driver may be implemented as a kernel module, a user-space library, or a combination of both.
- A device driver may be static or dynamic, meaning that it can be loaded and unloaded at runtime or compiled into the kernel image.
- A device driver may be generic or specific, meaning that it can support multiple devices of the same type or only one device of a particular model.

## VXWORKS

- VXWORKS is a real-time operating system (RTOS) developed by Wind River Systems for embedded systems.
- VXWORKS is a deterministic, priority-based preemptive RTOS with low latency and minimal jitter  .
- VXWORKS is built on an upgradable, future-proof architecture to help you rapidly respond to changing market requirements and technology advancements .
- VXWORKS supports a variety of hardware platforms, including x86, ARM, PowerPC, MIPS, etc.
- VXWORKS supports a variety of communication protocols, such as TCP/IP, UDP, Ethernet, CAN, USB, etc.
- VXWORKS supports a variety of file systems, such as FAT, DOSFS, HRFS, NFS, etc.
- VXWORKS supports a variety of development tools, such as Wind River Workbench, GNU Compiler Collection, Eclipse, etc.
- VXWORKS supports a variety of standards, such as POSIX, ARINC 653, FACE, etc.

### Device Driver Development in VXWORKS

- To develop a device driver in VXWORKS, you need to follow these steps:
  - Define the device structure, which contains the device name, driver number, and function pointers to the driver routines.
  - Implement the driver routines, such as devCreate, devDelete, devOpen, devClose, devRead, devWrite, devIoctl, etc.
  - Register the device driver with the operating system using iosDrvInstall, iosDevAdd, etc.
  - Load the device driver into the kernel using ld or loadModule.
  - Test the device driver using the shell commands or a user application.

## FREE RTOS

- FREE RTOS is a market-leading real-time operating system (RTOS) for microcontrollers and small microprocessors.
- FREE RTOS is developed in partnership with the world’s leading chip companies over an 18-year period, and now downloaded every 170 seconds.
- FREE RTOS is a portable, open source, mini real-time kernel that supports multiple architectures, such as ARM, AVR, PIC, MSP430, etc.
- FREE RTOS provides basic features, such as tasks, queues, semaphores, mutexes, timers, event groups, etc.
- FREE RTOS also provides optional features, such as software timers, tickless mode, trace tools, memory management, etc.
- FREE RTOS can be extended with additional components, such as TCP/IP stack, FAT file system, USB stack, etc.

### Device Driver Development in FREE RTOS

- To develop a device driver in FREE RTOS, you need to follow these steps:
  - Define the device structure, which contains the device name, device handle, and function pointers to the driver routines.
  - Implement the driver routines, such as devInit, devDeinit, devRead, devWrite, devIoctl, etc.
  - Register the device driver with the operating system using xRegisterDevice, xDeviceOpen, xDeviceClose, etc.
  - Load the device driver into the kernel using xLoadModule or xLoadLibrary.
  - Test the device driver using the shell commands or a user application.



# Driver Module Explanation for the Notes of the Unit 4 - VXWORKS / FREE RTOS in the Subject of Embedded Systems and Real Time Operating Systems

- A driver module is a software component that interacts with a specific hardware device or peripheral, such as a keyboard, mouse, printer, network card, etc.
- A driver module provides a uniform interface to the device, hiding the details of its implementation and operation from the application layer.
- A driver module typically consists of two parts: a device driver and a device controller.
- A device driver is the part of the driver module that communicates with the operating system kernel, such as VxWorks or FreeRTOS, and handles requests from user applications to access the device.
- A device controller is the part of the driver module that communicates with the hardware device directly, using the device-specific protocols and commands.
- A driver module may also include a device library, which is a set of functions or APIs that provide higher-level abstractions and functionalities for the device, such as printing a document, scanning an image, sending a packet, etc.
- A driver module may be implemented in different ways, depending on the operating system, the hardware platform, and the device characteristics.
- Some common types of driver modules are:
  - Character device drivers: These drivers handle devices that transfer data in a byte-by-byte or character-by-character manner, such as serial ports, keyboards, mice, etc.
  - Block device drivers: These drivers handle devices that transfer data in fixed-size blocks, such as hard disks, floppy disks, CD-ROMs, etc.
  - Network device drivers: These drivers handle devices that transfer data over a network, such as Ethernet cards, Wi-Fi adapters, Bluetooth modules, etc.
  - USB device drivers: These drivers handle devices that use the Universal Serial Bus (USB) protocol, such as flash drives, webcams, printers, etc.
  - PCI device drivers: These drivers handle devices that use the Peripheral Component Interconnect (PCI) bus, such as sound cards, video cards, network cards, etc.
- VxWorks and FreeRTOS are two examples of real-time operating systems (RTOS) that support driver modules for various devices and peripherals.
- VxWorks is a proprietary RTOS developed by Wind River Systems, which is widely used in embedded systems for aerospace, defense, industrial, medical, and automotive applications.
- FreeRTOS is an open-source RTOS developed by Real Time Engineers Ltd., which is popular in embedded systems for education, hobby, and commercial purposes.
- VxWorks and FreeRTOS have different approaches to driver module development and integration, as follows:
  - VxWorks provides a comprehensive set of board support packages (BSPs) and device drivers for various hardware platforms and devices, which are available from Wind River or third-party vendors.
  - VxWorks also provides a standard driver model (SDM) and a device driver interface (DDI) that define the common interfaces and structures for driver modules, which enable portability and compatibility across different devices and platforms.
  - VxWorks driver modules are typically written in C or C++, and are compiled and linked with the VxWorks kernel image, which is then loaded into the target device's memory at boot time.
  - FreeRTOS does not provide any official BSPs or device drivers, but relies on the hardware vendors or the community to provide them.
  - FreeRTOS also does not have a standard driver model or a device driver interface, but rather allows the driver modules to use the native APIs and services of the FreeRTOS kernel, such as tasks, queues, semaphores, etc.
  - FreeRTOS driver modules are typically written in C, and are compiled and linked with the FreeRTOS kernel image, which is then loaded into the target device's memory at boot time.
  - FreeRTOS also supports a POSIX-like peripheral driver library extension called FreeRTOS-Plus-IO, which provides a common interface to driver modules using the open(), read(), write(), and ioctl() functions.



# Implementation of Device Driver for a Peripheral

- A device driver is a software application that allows a hardware device (such as a printer or a keyboard) to interact with the operating system (such as Windows or Linux) of a computer system.
- A device driver acts as a translator between the operating system and the peripheral device, and communicates with the device through the computer bus (such as USB or PCI) that connects the device with the computer .
- A device driver consists of a physical structure of modes that represent the peripheral device and its functions, and a logical structure of routines that implement the device driver's operations.
- The implementation of a device driver for a peripheral device depends on the type of the device, the type of the bus, the type of the operating system, and the programming language used to write the driver.
- Some general steps for implementing a device driver for a peripheral device are:
  - Identify the device specifications, such as the device model, the device features, the device commands, and the device registers.
  - Identify the bus specifications, such as the bus type, the bus protocol, the bus address, and the bus speed.
  - Identify the operating system specifications, such as the operating system version, the operating system interface, the operating system services, and the operating system requirements.
  - Choose a programming language that is compatible with the operating system and the device, such as C, C++, or Assembly.
  - Write the device driver code that defines the device modes, the device routines, the device initialization, the device configuration, the device communication, the device error handling, and the device termination.
  - Compile and link the device driver code into a device driver file, such as a .sys, .dll, or .ko file, depending on the operating system.
  - Install and load the device driver file into the operating system, using the operating system tools, such as Device Manager, modprobe, or insmod.
  - Test and debug the device driver using the operating system tools, such as Device Manager, dmesg, or klogd, and the device tools, such as a device simulator or a device tester.

