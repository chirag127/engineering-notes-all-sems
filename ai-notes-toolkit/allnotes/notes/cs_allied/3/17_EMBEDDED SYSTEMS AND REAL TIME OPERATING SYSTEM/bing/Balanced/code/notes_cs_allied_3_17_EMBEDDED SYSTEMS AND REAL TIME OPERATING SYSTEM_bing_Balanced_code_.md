

# EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded system is a computer system that is designed to perform a specific function within a larger system or device. It typically has limited hardware resources, such as memory, processing power, and input/output devices. It often runs on a microcontroller or a microprocessor that is integrated with the hardware components of the system.  
- A real-time operating system (RTOS) is a type of operating system that is specialized for embedded systems that operate in real-time environments. A real-time environment is one where the system must respond to events or stimuli within a predictable and bounded time limit, such as milliseconds or microseconds.   
- Some examples of embedded systems that use RTOS are industrial control systems, automotive systems, medical devices, robotics, aerospace systems, and telecommunications systems. These systems have strict timing requirements and need to perform tasks such as data acquisition, signal processing, control, communication, and user interface.   
- Some of the features and characteristics of RTOS are:
  - Task scheduling: RTOS can manage multiple tasks or threads that run concurrently on the system. It can assign priorities to tasks and allocate CPU time to them according to different scheduling algorithms, such as rate monotonic, earliest deadline first, or priority ceiling protocol. RTOS can also handle task preemption, synchronization, and communication.   
  - Interrupt handling: RTOS can respond to external or internal interrupts that occur during the execution of tasks. Interrupts are signals that indicate the occurrence of an event that requires immediate attention. RTOS can save the context of the interrupted task, execute an interrupt service routine, and resume the interrupted task or switch to another task.  
  - Memory management: RTOS can allocate and deallocate memory for tasks and data structures. It can also provide mechanisms for memory protection, fragmentation, and sharing. RTOS can use different memory models, such as static, dynamic, or hybrid.  
  - Device drivers: RTOS can interface with the hardware devices that are part of the embedded system, such as sensors, actuators, displays, keyboards, and network interfaces. Device drivers are software modules that abstract the details of the hardware and provide a uniform interface for the tasks to access the devices.   
  - Application programming interface (API): RTOS can provide a set of functions or commands that the tasks can use to interact with the operating system and the hardware devices. The API can be standardized, such as POSIX, or vendor-specific, such as FreeRTOS or VxWorks. The API can also support different programming languages, such as C, C++, or Java.



## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system is a type of OS that is used in embedded computing devices, such as microcontrollers, sensors, smart appliances, etc.   
- An embedded OS aims to perform specific tasks with certainty and reliability, often under real-time constraints.  
- An embedded OS consists of a kernel and optional components, such as device drivers, middleware, libraries, and applications. 
- The kernel is the core of the embedded OS that manages the basic functions, such as process management, memory management, and I/O system management. 
- Process management is the function that creates, schedules, and terminates processes or threads that execute the tasks of the embedded system. 
- Memory management is the function that allocates, deallocates, and protects the memory space for the processes, the kernel, and the data. 
- I/O system management is the function that handles the communication between the processes and the external devices, such as sensors, actuators, displays, etc. 
- The optional components of the embedded OS provide additional functionality and services, such as file systems, network protocols, graphical user interfaces, etc. 
- The embedded OS is designed to be optimized for the specific hardware and software requirements of the embedded system, such as memory size, processor speed, power consumption, etc.   
- The embedded OS is usually developed with programming languages, such as C and C++, that allow low-level access and control of the hardware.  
- The embedded OS can be classified into different types, such as monolithic, microkernel, exokernel, hybrid, etc., based on the structure and organization of the kernel and the components.



### Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, set-top boxes, smart TVs, routers, etc. 
- Embedded Linux systems consist of the following main components:
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It initializes the hardware, loads the Linux kernel, and passes control to it.
  - Linux Kernel: The core of the operating system that manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system calls for user applications to interact with the hardware and the OS.
  - Device Tree: A data structure that describes the hardware configuration of the embedded system, such as the CPU type, memory size, peripheral devices, etc. It is used by the Linux kernel to initialize and configure the hardware.
  - Root File System: A collection of files and directories that provide the basic functionality of the OS, such as user applications, libraries, configuration files, etc. It can be stored in various types of storage media, such as flash memory, SD card, etc.
  - Configuration Files: Files that store the settings and parameters of the OS and the user applications, such as network configuration, user accounts, etc. They can be modified by the user or the system administrator to customize the behavior of the embedded system.
- Linux is the premier choice for embedded applications for several reasons:
  - Open-source: Linux is free and open-source, which means that anyone can access, modify, and distribute its source code. This gives developers more flexibility and control over the OS and reduces the licensing costs and dependencies on proprietary vendors.
  - Scalability: Linux can run on various types of hardware platforms, from low-end microcontrollers to high-end servers. It can also be customized and optimized for specific embedded applications by selecting the appropriate kernel features, modules, and drivers.
  - Developer Support: Linux has a large and active community of developers and users who contribute to its development, testing, and documentation. It also has a rich set of tools and frameworks that facilitate the development, debugging, and deployment of embedded applications.
  - Tooling: Linux provides a standard and consistent environment for developing and running embedded applications. It supports various programming languages, such as C, C++, Python, etc. It also offers a variety of utilities and libraries that simplify common tasks, such as file manipulation, network communication, data processing, etc.



### Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the OS manages and views other software in the embedded system (via processes)  .
- A process is a program in execution, which has a unique process identifier, a set of registers, a stack, a program counter, and a memory space .
- A process can be in one of the following states: ready, running, waiting, or terminated .
- Process management involves the following functions :
  - Process creation: allocating memory and resources for a new process, initializing its attributes, and adding it to the ready queue.
  - Process scheduling: selecting the next process to run based on a scheduling algorithm, such as round-robin, priority, or shortest job first.
  - Process switching: saving the context of the current process and restoring the context of the next process, which involves changing the program counter, the stack pointer, and the registers.
  - Process synchronization: coordinating the execution of multiple processes that share data or resources, using mechanisms such as semaphores, mutexes, or message queues.
  - Process communication: enabling the exchange of data or signals between processes, using mechanisms such as pipes, sockets, or shared memory.
  - Process termination: releasing the memory and resources of a process, removing it from the ready queue, and notifying its parent or other processes.
- Process management in embedded systems differs from general-purpose systems in the following aspects :
  - Embedded systems usually have limited memory and resources, which require efficient and optimized process management techniques.
  - Embedded systems often have strict real-time and event-driven requirements, which require predictable and deterministic process scheduling and switching.
  - Embedded systems may have different types of processors, such as microcontrollers, digital signal processors, or application-specific integrated circuits, which require different process management strategies and architectures.
  - Embedded systems may have different types of operating systems, such as bare-metal, monolithic, microkernel, or hybrid, which provide different levels of process management functionality and abstraction.



### File Management

- File management is the process of organizing, storing, accessing, and manipulating files in a file system.
- A file system is a logical structure that defines how files are named, grouped, and located on a storage device.
- An embedded system is a computer system that is designed for a specific purpose and has limited resources, such as memory, processing power, and battery life.
- An embedded operating system (OS) is a specialized OS that runs on an embedded system and provides basic services, such as file management, to the applications and devices.
- File management in an embedded OS is different from a general-purpose OS in several aspects, such as:

  - The file system may be simpler, smaller, and more efficient to fit the constraints of the embedded system.
  - The file system may be read-only, write-once, or have limited write operations to prevent data corruption or wear-out of the storage device.
  - The file system may be embedded in the firmware, stored in a flash memory, or accessed through a network or a removable media.
  - The file system may support different file formats, such as binary, text, or executable, depending on the application requirements.
  - The file system may have different security and reliability features, such as encryption, checksum, or backup, to protect the data and the system.

- Some examples of file systems used in embedded OS are:

  - FAT (File Allocation Table): A simple and widely used file system that supports various storage devices and platforms. It has a fixed-size table that maps the file names to the clusters of data blocks on the device. It has limitations, such as file size, fragmentation, and performance.
  - JFFS2 (Journaling Flash File System 2): A file system designed for flash memory devices that supports wear-leveling, compression, and journaling. It has a dynamic structure that allows appending new data blocks to the device without erasing the old ones. It has advantages, such as robustness, flexibility, and efficiency.
  - NFS (Network File System): A file system that allows accessing files over a network as if they were local. It has a client-server architecture that uses remote procedure calls (RPC) to communicate between the nodes. It has benefits, such as scalability, portability, and transparency.



### Memory Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory resources to programs and processes in an efficient and effective way.
- Memory management is essential for embedded systems, which have limited and constrained memory resources, such as RAM, ROM, flash, and cache.
- Memory management can affect the performance, reliability, security, and functionality of embedded systems.
- Memory management can be divided into two categories: static and dynamic.
  - Static memory management allocates memory at compile time or before the program execution. Static memory management is simple, fast, and deterministic, but it can waste memory and limit flexibility.
  - Dynamic memory management allocates memory at run time or during the program execution. Dynamic memory management is complex, slow, and non-deterministic, but it can save memory and increase flexibility.
- Memory management can be performed by the hardware, the software, or both.
  - Hardware memory management uses dedicated hardware components, such as memory management units (MMUs), to manage memory. Hardware memory management can provide memory protection, virtual memory, and memory mapping, but it can also introduce overhead and complexity.
  - Software memory management uses software components, such as memory allocators, to manage memory. Software memory management can provide memory pools, memory fragmentation, and memory leaks, but it can also introduce bugs and errors.
- Memory management can be influenced by the operating system, the programming language, and the application requirements.
  - Operating system memory management provides the interface and the services for memory management to the applications. Operating system memory management can be based on different models, such as monolithic, microkernel, or exokernel.
  - Programming language memory management provides the syntax and the semantics for memory management to the programmers. Programming language memory management can be based on different paradigms, such as imperative, functional, or object-oriented.
  - Application memory management provides the logic and the strategy for memory management to the system. Application memory management can be based on different criteria, such as performance, reliability, security, or functionality.



### I/O Management

- I/O management is the process of controlling the input and output devices of an embedded system, such as sensors, actuators, displays, keyboards, etc.
- I/O management involves the following tasks:
  - Device driver development: A device driver is a software module that interacts with a specific hardware device and provides a uniform interface to the operating system and the application programs.
  - Device driver installation: A device driver must be installed in the system memory and registered with the operating system, so that it can be invoked when needed.
  - Device driver configuration: A device driver may need to be configured with some parameters, such as device address, interrupt number, baud rate, etc., depending on the device characteristics and the system requirements.
  - Device driver communication: A device driver must communicate with the device and the operating system using appropriate mechanisms, such as polling, interrupt, DMA, etc.
  - Device driver synchronization: A device driver must synchronize the access to the device and the data transfer with the operating system and the application programs, using appropriate mechanisms, such as mutex, semaphore, queue, etc.
  - Device driver error handling: A device driver must handle any errors or exceptions that may occur during the device operation or the data transfer, such as device failure, data corruption, buffer overflow, etc.
- I/O management is an important aspect of embedded system design, as it affects the system performance, reliability, and usability.



### Overview of POSIX APIs

- POSIX stands for **Portable Operating System Interface** . It is a family of standards specified by **IEEE** for maintaining compatibility among operating systems.
- POSIX defines both the **system** and **user-level** application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a **trademark** of the IEEE. POSIX is intended to be used by both application and system developers.
- POSIX APIs are an increasingly popular OSAL (operating system abstraction layer) for IoT and embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX. Benefits of POSIX support in Zephyr include:
  - Offering a familiar API to non-embedded programmers, especially from Linux.
  - Enabling the use of existing libraries and middleware that use POSIX APIs.
  - Reducing the learning curve and development time for new applications.
- POSIX APIs are divided into several categories, such as:
  - Process control: functions for creating, terminating, and synchronizing processes, such as fork, exec, wait, and exit.
  - Signals: functions for sending and receiving signals between processes, such as kill, sigaction, and sigprocmask.
  - File and directory operations: functions for manipulating files and directories, such as open, close, read, write, and mkdir.
  - Pipes and FIFOs: functions for creating and using pipes and FIFOs for interprocess communication, such as pipe, mkfifo, and dup.
  - Sockets: functions for creating and using sockets for network communication, such as socket, bind, listen, accept, and connect.
  - Threads: functions for creating and managing threads, such as pthread_create, pthread_join, pthread_mutex, and pthread_cond.
  - Timers: functions for measuring and setting time, such as clock, time, alarm, and sleep.
  - Semaphores: functions for creating and using semaphores for synchronization, such as sem_init, sem_wait, and sem_post.
  - Shared memory: functions for creating and using shared memory segments for interprocess communication, such as shm_open, shm_unlink, and mmap.
  - Message queues: functions for creating and using message queues for interprocess communication, such as mq_open, mq_send, and mq_receive.
- POSIX APIs are defined in a number of **header files** that are included in the C POSIX library. Some of the common header files are:
  - stdio.h: input/output operations, such as printf, scanf, and fopen.
  - stdlib.h: memory management, random numbers, and system calls, such as malloc, free, rand, and system.
  - string.h: string manipulation, such as strcpy, strcat, and strcmp.
  - math.h: mathematical functions, such as sin, cos, and sqrt.
  - unistd.h: POSIX system calls, such as fork, exec, and pipe.
  - signal.h: signal handling, such as kill, sigaction, and sigprocmask.
  - fcntl.h: file control, such as open, close, and fcntl.
  - dirent.h: directory operations, such as opendir, readdir, and closedir.
  - sys/stat.h: file status, such as stat, fstat, and chmod.
  - sys/socket.h: socket operations, such as socket, bind, and connect.
  - pthread.h: thread operations, such as pthread_create, pthread_join, and pthread_mutex.
  - time.h: time operations, such as clock, time, and sleep.
  - semaphore.h: semaphore operations, such as sem_init, sem_wait, and sem_post.
  - mqueue.h: message queue operations, such as mq_open, mq_send, and mq_receive.
  - sys/mman.h: memory mapping, such as shm_open, shm_unlink, and mmap.

: https://docs.zephyrproject.org/latest/services/portability



### Threads – Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread shares the same memory and resources as the program that created it, which enables multiple threads to collaborate and work efficiently within a single program.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the user-level program (user-level threads).
- Kernel-supported threads are supported by the operating system, which stores multiple thread control blocks (TCBs) per process and is involved in dispatching and switching between threads (even between threads in the same process).
- User-level threads are created and managed by the user-level program, which uses its own data structures and libraries to implement threads without involving the kernel.
- Some operating systems, such as Windows, MacOS X, Linux, and some embedded operating systems, provide a hybrid approach that combines kernel-supported and user-level threads, such as the POSIX threads (pthreads) library.
- To create a thread, the program needs to specify the function or code segment that the thread will execute, as well as any parameters or arguments that the thread needs.
- The operating system or the user-level library will then allocate a stack and a TCB for the new thread, and add it to the ready list of threads that are waiting to run.
- The operating system or the user-level library will also assign a unique identifier to the new thread, which can be used to refer to the thread later.
- The operating system or the user-level library will then schedule the new thread to run on an available processor or core, or preempt an existing thread to make room for the new thread.
- The thread will start executing the specified function or code segment, and will terminate when the function returns or when the thread explicitly calls a termination function.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Embedded Systems and Real Time Operating Systems. Here are some notes on the topic of Cancellation for the Unit 1 - Embedded OS Internals.

### Cancellation

- Cancellation is the mechanism by which a thread can terminate the execution of another thread before it completes normally.
- Cancellation can be either **asynchronous** or **deferred**.
- Asynchronous cancellation means that the target thread is terminated immediately when the cancellation request is issued.
- Deferred cancellation means that the target thread can control when and how it responds to the cancellation request.
- The target thread can set its own **cancellation state** and **cancellation type** using the functions `pthread_setcancelstate()` and `pthread_setcanceltype()`.
- The cancellation state can be either **enabled** or **disabled**. If the state is enabled, the thread can receive cancellation requests. If the state is disabled, the thread ignores cancellation requests.
- The cancellation type can be either **asynchronous** or **deferred**. If the type is asynchronous, the thread is terminated immediately when a cancellation request is received. If the type is deferred, the thread can defer the cancellation until it reaches a **cancellation point**.
- A cancellation point is a function or a point in the code where the thread checks for pending cancellation requests and acts accordingly. Some examples of cancellation points are `pthread_testcancel()`, `pthread_join()`, `pthread_cond_wait()`, etc.
- The thread that wants to cancel another thread can use the function `pthread_cancel()` to send a cancellation request to the target thread. The function returns 0 on success and an error code on failure.
- The target thread can use the function `pthread_cleanup_push()` to register a **cleanup handler** that will be executed when the thread is cancelled. The function takes a pointer to a function and a pointer to an argument as parameters. The cleanup handler can perform any necessary actions to release resources or restore the state of the system before the thread exits.
- The target thread can use the function `pthread_cleanup_pop()` to deregister a cleanup handler that was previously registered with `pthread_cleanup_push()`. The function takes an integer parameter that specifies whether to execute the cleanup handler or not.
- The target thread can use the function `pthread_exit()` to terminate its execution and return a value to the thread that joined it. The function takes a pointer to a value as a parameter. The value can be retrieved by the joining thread using the function `pthread_join()`.
- The target thread can also be cancelled by the system if it receives a signal that is not blocked or ignored. The signal handler can use the function `pthread_exit()` to terminate the thread gracefully.



### POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995) .
- A single process can contain multiple threads, all of which are executing the same program. Each thread has its own **stack**, **registers**, **thread ID**, **priority**, **signal mask**, and **errno** variable.
- Threads share the same **address space**, **heap**, **global variables**, **file descriptors**, and **signal handlers** as the process that created them.
- Threads can communicate with each other using **shared memory**, **message passing**, or **synchronization primitives** such as **mutexes**, **condition variables**, **semaphores**, and **barriers**.
- The pthreads API provides functions for creating, joining, detaching, canceling, and synchronizing threads, as well as setting and getting thread attributes .
- The pthreads API is implemented by various **libraries** for different operating systems, such as **libpthread** for Linux, **libc** for BSD, and **pthreadVC2** for Windows.



### Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions.
- IPC can be achieved through two methods: shared memory and message passing.
- Shared memory allows processes to access a common memory region for reading and writing data.
- Message passing allows processes to exchange messages through a communication channel such as a queue, a pipe, or a socket.
- A semaphore is a special type of IPC that uses a counter to control access to a shared resource by multiple processes.
- A semaphore can be initialized to a positive integer value that represents the number of available units of the resource.
- A process that wants to use the resource must perform a wait operation on the semaphore, which decrements the counter by one.
- If the counter is zero or negative, the process is blocked until another process releases the resource by performing a signal operation on the semaphore, which increments the counter by one.
- A semaphore can be used to implement mutual exclusion, synchronization, and deadlock prevention among processes.
- There are two types of semaphores: binary and counting.
- A binary semaphore can only have two values: 0 or 1, and is used to implement mutual exclusion.
- A counting semaphore can have any non-negative value, and is used to implement synchronization.
- Semaphores can be implemented in different ways, such as using atomic instructions, busy waiting, or blocking queues.
- Semaphores can also be classified as local or global, depending on whether they are shared by processes within the same address space or across different address spaces.
- Semaphores can be created, accessed, and manipulated using system calls such as semget, semop, and semctl.



### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems, where memory and CPU resources are limited, and tasks need to communicate efficiently and reliably.
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and can only be accessed by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available.
- Pipes can be used to implement simple message passing protocols, such as sending fixed-size messages or using delimiters to separate messages.
- Pipes have some advantages and disadvantages compared to other IPC methods, such as sockets, message queues, or shared memory. Some of the advantages are:
  - Pipes are easy to use and require minimal system calls.
  - Pipes are portable across different operating systems and platforms.
  - Pipes can be used to create pipelines of commands or processes that process data sequentially.
- Some of the disadvantages are:
  - Pipes have limited capacity and can cause data loss or deadlock if not handled properly .
  - Pipes are unidirectional and require two pipes for bidirectional communication.
  - Pipes are not suitable for complex or structured data, such as objects or records.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of FIFO for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

```markdown
# FIFO

- FIFO stands for First In First Out, which is a queue data structure that follows the principle of serving the elements in the order they arrive.
- FIFO is often used in embedded systems and real-time operating systems to implement inter-process communication, buffering, scheduling, and synchronization mechanisms.
- FIFO can be implemented using arrays, linked lists, circular buffers, or hardware registers, depending on the requirements and constraints of the system.
- FIFO has two basic operations: enqueue and dequeue. Enqueue adds an element to the rear of the queue, and dequeue removes an element from the front of the queue.
- FIFO has some advantages and disadvantages compared to other data structures, such as:

  - Advantages:
    - FIFO is simple and easy to implement and understand.
    - FIFO preserves the order of arrival of the elements, which is important for some applications, such as event handling, message passing, and stream processing.
    - FIFO can be used to implement fair scheduling algorithms, such as round-robin, that give equal priority to all elements.
    - FIFO can be used to implement producer-consumer patterns, where one process produces data and another process consumes it, without blocking or overwriting the data.
  - Disadvantages:
    - FIFO may not be optimal for some applications, such as priority-based scheduling, where some elements need to be served before others, regardless of their arrival order.
    - FIFO may suffer from performance issues, such as memory fragmentation, cache misses, and pipeline stalls, if the size of the queue is not fixed or optimized for the system.
    - FIFO may introduce latency and jitter, which are variations in the delay between the arrival and the service of the elements, which can affect the quality of service and the responsiveness of the system.
```



### Shared Memory

- Shared memory is a method of interprocess communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it does not involve copying data or system calls.
- Shared memory can be implemented in different ways, such as:
  - Using a special system call, such as `shmget` or `mmap`, to create and map a shared memory segment in the address space of each process.
  - Using a memory-mapped file, which is a file that is mapped to a region of memory and can be accessed by multiple processes.
  - Using a shared memory object, which is a named object that can be created and opened by multiple processes and can be resized dynamically.
- Shared memory systems can be classified into two types, depending on how the memory is accessed by the processes:
  - Uniform memory access (UMA), where all processes have the same view of the memory and can access any location with the same latency and bandwidth.
  - Non-uniform memory access (NUMA), where different processes have different views of the memory and may experience different latencies and bandwidths depending on the location of the memory.
- Shared memory systems can also be classified into two types, depending on how the memory is distributed among the processors:
  - Centralized shared memory, where all the processors share a single physical memory and communicate through a common bus or interconnect.
  - Distributed shared memory, where each processor has its own local memory and can access the memory of other processors through a network or special hardware.
- Shared memory systems have advantages and disadvantages, such as:
  - Advantages:
    - High performance and low overhead for IPC.
    - Simple and natural programming model for data sharing and parallelism.
    - No need for explicit message passing or serialization.
  - Disadvantages:
    - Potential for data inconsistency and race conditions due to concurrent access.
    - Need for synchronization mechanisms, such as locks, semaphores, or barriers, to ensure data integrity and coordination.
    - Scalability and reliability issues due to memory contention and single point of failure.



### Kernel for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A kernel is the core component of an operating system that manages the hardware and software resources, provides services for applications, and handles system calls and interrupts  .
- A kernel can be classified into two types: monolithic and modular .
  - A monolithic kernel is a single large program that contains all the core functions of the operating system, such as memory management, process management, file system, device drivers, etc. A monolithic kernel runs in a single address space and has direct access to the hardware.
  - A modular kernel is a kernel that consists of several modules that can be dynamically loaded and unloaded from the kernel. A modular kernel has a small core that provides basic services, such as inter-module communication, and relies on external modules for other functions, such as device drivers, file system, network protocols, etc. A modular kernel can reduce the size and complexity of the kernel, improve the reliability and security of the system, and allow for customization and extensibility .
- An embedded operating system is a specialized operating system that is designed for embedded systems, which are devices that have limited resources, such as memory, CPU, power, etc., and perform specific functions, such as sensors, controllers, smart appliances, etc. An embedded operating system has to meet the requirements of the embedded system, such as real-time performance, low power consumption, small footprint, high reliability, etc. An embedded operating system may use a monolithic or a modular kernel, depending on the trade-off between performance and flexibility.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is a possible structure for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

```markdown
# Unit 1 - EMBEDDED OS INTERNALS

## Introduction
- Define embedded systems and real-time operating systems (RTOS)
- Explain the characteristics and challenges of embedded systems and RTOS
- List some examples and applications of embedded systems and RTOS

## Embedded OS Architecture
- Describe the components and layers of an embedded OS
- Compare and contrast different types of embedded OS, such as monolithic, microkernel, exokernel, etc.
- Discuss the advantages and disadvantages of each type of embedded OS

## Embedded OS Services
- Identify the main services provided by an embedded OS, such as task management, memory management, inter-task communication, synchronization, etc.
- Explain how each service works and why it is important for embedded systems and RTOS
- Demonstrate how to use each service with code examples and diagrams

## Embedded OS Design and Implementation
- Outline the steps and principles of embedded OS design and implementation
- Explain the trade-offs and criteria for embedded OS selection and optimization
- Discuss the tools and techniques for embedded OS development and debugging
```



### Kernel Module Programming

- Kernel module programming is a way of extending the functionality of the kernel without modifying the source code or recompiling the kernel.
- Kernel modules are object files that contain code that can be loaded into or unloaded from the kernel at runtime.
- Kernel modules are useful for implementing device drivers, file systems, network protocols, system calls, and other features that are not part of the core kernel.
- Kernel modules must have at least two functions: a start (initialization) function called `init_module()` and an end (cleanup) function called `cleanup_module()`.
- Kernel modules can communicate with the kernel and other modules using symbols, parameters, and sysfs.
- Kernel modules can be written in C or assembly language, and must follow the kernel coding style and conventions.
- Kernel modules can be compiled using the `make` command and the kernel headers.
- Kernel modules can be inserted into the kernel using the `insmod` command and removed from the kernel using the `rmmod` command.
- Kernel modules can be listed using the `lsmod` command and their information can be displayed using the `modinfo` command.
- Kernel modules can be debugged using tools such as `printk`, `kdb`, `kgdb`, and `kprobes`.



### Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is the software that determines which task should be run next by the processor in an embedded system.
- A scheduling algorithm is the logic and the mechanism that decides when the scheduler should be run and which task should be selected.
- Scheduling algorithms can be classified into two categories: preemptive and non-preemptive.
  - Preemptive scheduling allows a higher priority task to interrupt a lower priority task that is currently running and take over the processor.
  - Non-preemptive scheduling does not allow a lower priority task to be interrupted by a higher priority task once it starts running.
- Some common types of schedulers in embedded systems are:
  - Round Robin (RR) scheduler: A simple scheduler that gives each task a fixed amount of processor time in a circular order.
  - Time Slice (TS) scheduler: A scheduler that divides time into slots and assigns each task a slot based on its priority.
  - Priority scheduler: A scheduler that always selects the task with the highest priority to run next.
  - Composite scheduler: A scheduler that combines different scheduling algorithms to achieve the best performance and meet the system requirements.
- Schedulers in embedded systems must also consider the real-time constraints and deadlines of the tasks, as well as the resource utilization and power consumption of the system.
- Schedulers can be implemented using different techniques, such as function pointers, state machines, or real-time operating systems (RTOS).



# Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals

Scheduling is the process of allocating CPU time to different tasks or processes in an embedded system. Scheduling can affect the performance, responsiveness, and predictability of the system. There are different types of scheduling algorithms that can be used in embedded systems, depending on the system requirements and constraints. Some of the common types of scheduling are:

- **Non-preemptive scheduling**: In this type of scheduling, the CPU executes a task until it completes or voluntarily relinquishes the CPU. The task cannot be interrupted by another task with higher priority. This type of scheduling is simple and easy to implement, but it can cause long delays and poor responsiveness for high-priority tasks. Non-preemptive scheduling is suitable for systems that do not have strict timing constraints or real-time requirements. 

- **Preemptive scheduling**: In this type of scheduling, the CPU can interrupt a task that is currently executing and switch to another task with higher priority. The interrupted task is suspended and resumed later when the CPU is available. This type of scheduling can improve the responsiveness and predictability of the system, but it can also introduce overhead and complexity. Preemptive scheduling is suitable for systems that have real-time requirements and need to meet deadlines.  

- **Round-robin scheduling**: This is a special case of preemptive scheduling, where the tasks have equal priority and are executed in a circular order. Each task is given a fixed amount of CPU time, called a time slice or a quantum, and then the CPU switches to the next task in the queue. This type of scheduling can provide fairness and balance among the tasks, but it can also cause frequent context switches and poor performance for tasks that need longer execution time. Round-robin scheduling is suitable for systems that have multiple tasks with similar importance and characteristics.  

- **Priority scheduling**: This is a general case of preemptive scheduling, where the tasks have different priority levels and are executed according to their priority. The task with the highest priority is always selected by the CPU, and the lower-priority tasks are executed only when the higher-priority tasks are not ready or waiting. This type of scheduling can ensure that the most important tasks are executed first, but it can also cause starvation and deadlock for the lower-priority tasks. Priority scheduling is suitable for systems that have diverse tasks with different importance and urgency.  

- **Time slice scheduling**: This is a variation of priority scheduling, where the tasks are executed in priority order, but each task is given a limited amount of CPU time, called a time slice. The time slice can be fixed or variable, depending on the task priority. This type of scheduling can combine the advantages of priority scheduling and round-robin scheduling, but it can also increase the complexity and overhead of the system. Time slice scheduling is suitable for systems that have multiple tasks with different priority and execution time. 

- **Real-time scheduling**: This is a category of scheduling that is designed for systems that have real-time requirements, meaning that the tasks have to meet certain deadlines or timing constraints. Real-time scheduling can be divided into two types: hard and soft. Hard real-time scheduling guarantees that the tasks will meet their deadlines, otherwise the system will fail. Soft real-time scheduling tries to meet the deadlines, but it can tolerate some occasional misses. Real-time scheduling can use different algorithms, such as rate-monotonic, earliest deadline first, or least laxity first, to assign priority and CPU time to the tasks. Real-time scheduling is suitable for systems that have critical or time-sensitive tasks, such as control systems, multimedia systems, or communication systems.



### Interfacing for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interfacing is the process of connecting and communicating between different hardware and software components in an embedded system.
- Interfacing can be classified into two types: internal and external.
- Internal interfacing refers to the communication between the embedded processor and the internal peripherals, such as memory, timers, interrupt controllers, etc.
- External interfacing refers to the communication between the embedded processor and the external devices, such as sensors, actuators, displays, keyboards, etc.
- Interfacing can be done using various methods, such as parallel, serial, analog, digital, wireless, etc.
- Interfacing can be done using various protocols, such as SPI, I2C, UART, USB, CAN, etc.
- Interfacing can be done using various standards, such as RS-232, RS-485, IEEE 802.11, Bluetooth, etc.
- Interfacing can be done using various levels of abstraction, such as hardware, firmware, drivers, middleware, applications, etc.
- Interfacing can be done using various tools, such as compilers, assemblers, linkers, debuggers, simulators, emulators, etc.
- Interfacing can be done using various techniques, such as polling, interrupt, DMA, etc.
- Interfacing can be done using various challenges, such as synchronization, concurrency, latency, throughput, reliability, security, etc.
- Interfacing can be done using various solutions, such as RTOS, OS services, libraries, APIs, etc.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of Serial for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Serial
- Serial communication is a method of transferring data between devices using a single wire or a pair of wires.
- Serial communication is widely used in embedded systems and real time operating systems because it is simple, reliable, and low-cost.
- Serial communication can be synchronous or asynchronous, depending on whether the sender and receiver use a common clock signal or not.
- Synchronous serial communication requires a clock signal to synchronize the data transmission and reception. Examples of synchronous serial protocols are SPI, I2C, and CAN.
- Asynchronous serial communication does not require a clock signal, but uses start and stop bits to mark the beginning and end of each data frame. Examples of asynchronous serial protocols are UART, RS-232, and USB.
- Serial communication can be full-duplex or half-duplex, depending on whether the data can be transmitted and received simultaneously or not.
- Full-duplex serial communication allows both devices to send and receive data at the same time. Examples of full-duplex serial protocols are SPI, I2C, and USB.
- Half-duplex serial communication allows only one device to send or receive data at a time. Examples of half-duplex serial protocols are UART, RS-232, and CAN.
- Serial communication can be point-to-point or point-to-multipoint, depending on whether the data is sent to one or multiple devices.
- Point-to-point serial communication connects two devices directly using a single wire or a pair of wires. Examples of point-to-point serial protocols are UART, RS-232, and SPI.
- Point-to-multipoint serial communication connects one device to multiple devices using a shared bus or a network. Examples of point-to-multipoint serial protocols are I2C, CAN, and USB.



### Parallelism

Parallelism is the ability to perform multiple operations or tasks simultaneously, using multiple processors or cores. Parallelism can improve the performance, efficiency, and scalability of embedded systems, especially for applications that require intensive computation or data processing. Parallelism can be achieved at different levels of abstraction, such as instruction level, task level, or data level.

Some of the topics that are related to parallelism in embedded systems are:

- **Concurrency**: Concurrency is the property of a system that allows multiple activities to happen at the same time, without necessarily being synchronized or coordinated. Concurrency can be implemented by using threads, processes, or distributed systems. Concurrency can enable parallelism, but it can also introduce challenges such as synchronization, communication, and deadlock.
- **Multicore architectures**: Multicore architectures are systems that have more than one processor or core on a single chip. Multicore architectures can provide parallelism by allowing multiple threads or processes to run on different cores, or by using specialized cores for different functions. Multicore architectures can also reduce power consumption, heat dissipation, and cost compared to single-core architectures.
- **Model-driven design**: Model-driven design is a methodology that uses high-level models to describe the structure and behavior of a system, and then generates code or configuration files for the target platform. Model-driven design can facilitate the development of parallel embedded systems by providing abstraction, automation, and verification tools. For example, the MARTE (Modeling and Analysis of Real-time and Embedded systems) standard profile is a model-driven framework that supports the description and analysis of parallel embedded systems.
- **Instruction level parallelism**: Instruction level parallelism (ILP) is the degree to which multiple instructions can be executed simultaneously by a single processor or core, without depending on each other. ILP can be achieved by using techniques such as pipelining, superscalar execution, out-of-order execution, or vector processing. ILP can improve the performance and efficiency of embedded systems, but it can also increase the complexity and power consumption of the processor or core.



### Interrupt Handling for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts are indispensable when writing any practical embedded firmware, as they allow the CPU to respond to external events that are not synchronized to the software running on the system .
- Interrupts can be classified into two types: software interrupts and hardware interrupts.
  - Software interrupts are called from software, using a specified command. They are used to invoke system calls or exception handlers.
  - Hardware interrupts are triggered by peripheral devices outside the micro-controller. For instance, your embedded system may contain a timer that sends a pulse to the controller every second, or a button that generates a signal when pressed.
- Interrupts have several advantages over polling, such as reducing CPU overhead, improving responsiveness, and simplifying the software design.
- Interrupts also have some challenges, such as handling multiple interrupts, prioritizing interrupts, saving and restoring the CPU context, and synchronizing with the main program .
- Interrupt handling in embedded systems involves the following steps :
  - When an interrupt occurs, the CPU executes the current running instruction then stores the necessary stack pointer and program counter (PC) information somewhere in RAM allocated for the current function.
  - The CPU then jumps to a predefined address in the memory, called the interrupt vector table, which contains the addresses of the interrupt service routines (ISRs) for each interrupt source.
  - The CPU executes the ISR corresponding to the interrupt source, which performs the necessary actions to handle the interrupt, such as reading or writing data from or to the peripheral device, clearing the interrupt flag, and sending an acknowledgment to the device.
  - The ISR then returns from the interrupt, restoring the CPU context from the RAM and resuming the execution of the main program from where it was interrupted.
- Interrupt handling in embedded systems requires careful design and testing, as it can affect the performance, reliability, and security of the system . Some of the best practices for interrupt handling are:
  - Keep the ISRs as short and simple as possible, and avoid blocking or waiting operations in them.
  - Use interrupt priorities to handle multiple interrupts and avoid missing or delaying critical interrupts.
  - Use semaphores, mutexes, or flags to synchronize the ISRs with the main program and prevent data corruption or race conditions.
  - Use interrupt masking or disabling to protect critical sections of code from being interrupted by lower priority interrupts.
  - Use nested interrupts to allow higher priority interrupts to interrupt lower priority interrupts, if supported by the hardware and the OS.
  - Use interrupt latency analysis to measure and optimize the time taken by the CPU to respond to an interrupt and complete the ISR.



### Linux Device Drivers

- A device driver is a piece of software that enables the kernel to communicate with a specific piece of hardware, such as a disk, a network card, a printer, etc.
- Device drivers are usually written in C and follow the Linux kernel coding style.
- Device drivers can be built as loadable modules, which are pieces of code that can be added to or removed from the kernel at runtime, or as static modules, which are compiled into the kernel image and cannot be changed without recompiling the kernel.
- Device drivers interact with the kernel through a well-defined internal programming interface (API), which consists of data structures, functions, macros, and constants that are defined in various header files.
- Device drivers also interact with the user space through a device file, which is a special file that represents the device and allows the user to read from or write to the device using standard system calls, such as open, read, write, close, etc.
- Device drivers can be classified into different types according to the nature of the device they control, such as character devices, block devices, network devices, etc. Each type of device has its own set of functions and data structures that the driver must implement and register with the kernel.
- Device drivers can also use various kernel services and subsystems to perform their tasks, such as memory management, interrupt handling, DMA, locking, scheduling, etc. These services and subsystems provide abstractions and mechanisms that simplify the driver development and ensure the correct and efficient operation of the device and the kernel.



### Characteristics of Embedded Operating Systems

- An embedded operating system is a computer operating system designed for use in embedded computer systems  .
- Embedded operating systems are designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications .
- Embedded operating systems have the following characteristics:
  - Direct use of interrupts: Embedded operating systems can handle interrupts from various sources, such as sensors, timers, or communication devices, without using complex mechanisms like system calls or context switches.
  - Reactive operation: Embedded operating systems can respond quickly to external events and stimuli, such as user inputs, sensor readings, or network messages, and execute the appropriate tasks or actions.
  - Real-time operation: Embedded operating systems can meet the timing constraints and deadlines of the applications, such as controlling a motor, displaying a video, or sending a message, and ensure the correctness and predictability of the system behavior.
  - Streamlined protection mechanisms: Embedded operating systems can provide basic security and protection features, such as memory management, access control, or encryption, without compromising the performance or efficiency of the system.
  - I/O device flexibility: Embedded operating systems can support a variety of input/output devices, such as keyboards, touchscreens, cameras, speakers, or wireless modules, and provide the necessary drivers and interfaces for them.
- Embedded operating systems are used in various types of embedded systems, such as ATMs, cellphones, smart TVs, medical devices, industrial controllers, or IoT devices .



### USB

- USB stands for Universal Serial Bus  and is a common interface that enables communication between devices and a host controller such as a personal computer (PC) or smartphone .
- USB was designed to standardize the connection of peripherals to personal computers, both to communicate with and to supply electric power. It has largely replaced interfaces such as serial ports and parallel ports and has become commonplace on a wide range of devices.
- USB provides both data transmission and low voltage (5V) power over a single cable. It also supports plug-and-play and hot swapping of devices, meaning that they can be connected and disconnected without rebooting the host or installing drivers.
- USB has several versions, each with different specifications and features. The most common ones are USB 1.1, USB 2.0, USB 3.0, USB 3.1, USB 3.2, and USB 4.0. The main differences among them are the data transfer rates, the power delivery, and the connector types.
- USB devices can be classified into different device classes, such as human interface devices (HID), mass storage devices, audio devices, video devices, printers, scanners, and hubs. Each device class has a set of standard protocols and commands that the host and the device use to communicate with each other.
- USB devices can be connected in a tree-like topology, with a single host at the root and up to 127 devices at the branches. A USB hub is a device that allows multiple devices to be connected to a single port on the host or another hub. Each device has a unique address assigned by the host during the enumeration process.
- USB devices communicate with the host using packets, which are units of data that contain information such as the device address, the endpoint number, the data length, the data payload, and the error detection code. The host initiates all the transactions and the devices respond accordingly. There are four types of transactions: control, bulk, interrupt, and isochronous.
- USB devices have one or more endpoints, which are logical entities that represent the source or destination of data. Each endpoint has a number, a direction (in or out), and a type (control, bulk, interrupt, or isochronous). The endpoint 0 is reserved for control transfers, which are used to configure and manage the device. The other endpoints are used for data transfers, which are based on the device class and function.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of Block & Network for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Block & Network

- A block device is a device that stores or transfers data in fixed-sized units called blocks. Examples of block devices are hard disks, flash drives, CD-ROMs, etc.
- A network device is a device that communicates with other devices over a network using protocols such as TCP/IP, UDP, etc. Examples of network devices are network interface cards, routers, switches, etc.
- Block and network devices are important components of embedded systems, as they provide the means to store, retrieve, and exchange data with other systems.
- Embedded OS internals are the low-level mechanisms and structures that manage the interaction between the OS and the block and network devices. They include drivers, buffers, caches, queues, protocols, etc.
- Some of the challenges and issues that embedded OS internals have to deal with are:

  - Resource constraints: Embedded systems often have limited memory, CPU, power, and bandwidth, which require efficient and optimized use of the available resources.
  - Real-time requirements: Embedded systems often have to meet strict timing and performance constraints, which require fast and predictable response from the OS and the devices.
  - Reliability and security: Embedded systems often have to operate in harsh and critical environments, which require high levels of reliability and security from the OS and the devices.
  - Diversity and compatibility: Embedded systems often have to support a wide range of devices and protocols, which require standardization and interoperability from the OS and the devices.



## Unit 2 - OPEN SOURCE RTOS

- An open source RTOS (real-time operating system) is a software platform that provides the basic services and features for real-time applications, such as scheduling, synchronization, memory management, communication, and device drivers.
- An open source RTOS is typically distributed under a license that allows anyone to access, modify, and redistribute the source code, subject to certain conditions and obligations.
- Some of the benefits of using an open source RTOS are:
  - Cost savings: An open source RTOS can be obtained for free or at a low cost, reducing the development and maintenance expenses.
  - Customization: An open source RTOS can be tailored to the specific needs and requirements of the application, improving the performance and functionality.
  - Innovation: An open source RTOS can benefit from the contributions and feedback of a large and diverse community of developers and users, enhancing the quality and reliability of the software.
  - Compatibility: An open source RTOS can support a wide range of hardware platforms and devices, facilitating the portability and interoperability of the application.
- Some of the challenges of using an open source RTOS are:
  - Support: An open source RTOS may not have a dedicated or reliable support service, making it difficult to resolve issues and bugs.
  - Documentation: An open source RTOS may not have a comprehensive or updated documentation, making it hard to learn and use the software.
  - Licensing: An open source RTOS may have a complex or restrictive license, imposing legal and ethical obligations on the developers and users of the software.
  - Security: An open source RTOS may have vulnerabilities or flaws that can compromise the safety and privacy of the application and the data.
- Some of the examples of open source RTOS are:
  - FreeRTOS: A popular and widely used open source RTOS that supports multiple architectures and platforms, and provides a rich set of features and services.
  - Zephyr: A scalable and modular open source RTOS that supports various IoT devices and protocols, and offers a low memory footprint and high performance.
  - RIOT: A lightweight and user-friendly open source RTOS that supports multiple network stacks and standards, and enables rapid prototyping and development.
  - NuttX: A compact and configurable open source RTOS that supports POSIX and ANSI standards, and provides a high degree of compatibility and functionality.
  - RT-Thread: A powerful and flexible open source RTOS that supports multiple components and frameworks, and provides a user-friendly and interactive interface.



### Basics of RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system.
- An RTOS creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides the necessary hard real-time computing capabilities, and it does so in an embedded environment.
- An RTOS is used for controlling devices that require timing synchronization with their environment or with other devices.
- An RTOS is a program that acts as an interface between the system hardware and the user.
- An RTOS handles all the interactions between the software and the hardware.
- An RTOS processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS can be classified into three types based on the time limit for completing the tasks:
  - Hard Real-Time operating system: These operating systems guarantee that critical tasks be completed within a range of time. For example, a missile launch system.
  - Soft real-time operating system: This operating system provides some relaxation in the time limit. For example, a video streaming system.
  - Firm Real-time Operating System: RTOS of this type have to meet deadlines but missing a deadline is not a total system failure. For example, a stock market system.
- An RTOS consists of the following basic components:
  - Kernel: The core of the RTOS that provides the basic services, such as thread management, memory management, inter-thread communication, and synchronization.
  - Device drivers: The software modules that interface with the hardware devices, such as sensors, actuators, and communication ports.
  - Middleware: The software layer that provides additional services, such as file system, network stack, graphics, and security.
  - Application: The software that implements the specific functionality of the system, such as user interface, control logic, and data processing.



### Real-time concepts for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real-time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail or cause undesirable consequences.
- A real-time operating system (RTOS) is an operating system that provides the rigorous resource management and scheduling required to meet the demands of real-time applications.
- An RTOS typically has a small footprint and is optimized for performance, with features such as multi-tasking, priority-driven pre-emptive scheduling, fast context-switching, and interrupt handling .
- An RTOS can be classified into two types: hard real-time and soft real-time. A hard real-time system must meet all the deadlines, otherwise it is considered a failure. A soft real-time system can tolerate some missed deadlines, but the quality of service may degrade.
- An RTOS can also be classified into two types: proprietary and open source. A proprietary RTOS is owned and licensed by a company or organization, and may have restrictions on its use, modification, and distribution. An open source RTOS is free and publicly available, and can be modified and distributed by anyone under certain terms and conditions.
- Some examples of open source RTOSs are FreeRTOS, SAFERTOS, Zephyr, NuttX, and RIOT . These RTOSs can be used in embedded systems based on microcontrollers, such as Arduino, Raspberry Pi, STM32, and ESP32 .
- Some benefits of using open source RTOSs are: lower cost, greater flexibility, faster development, wider community support, and easier integration with other open source software .
- Some challenges of using open source RTOSs are: lack of certification, limited documentation, variable quality, legal issues, and security risks .



# Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-time applications.
- A real-time application is one that requires a timely and predictable response from the system.
- There are two types of real-time systems: hard real-time and soft real-time .

## Hard Real Time

- A hard real-time system is one where the time taken is deterministic to an exact moment.
- A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
- A hard real-time system is highly restrictive and does not tolerate any system failure.
- Examples of hard real-time systems are nuclear power plants, air traffic control systems, pacemakers, etc.

## Soft Real Time

- A soft real-time system is one where the time taken is deterministic to a range of values.
- A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- A soft real-time system is less strict and can stand the system failure.
- Examples of soft real-time systems are multimedia applications, online gaming, video conferencing, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some differences between General Purpose OS and RTOS:

- **Task Scheduling**: General Purpose OS are capable of handling various applications and are optimized to run variety of applications at the same time. They use preemptive or non-preemptive scheduling algorithms to switch between processes. RTOS are designed to run specific tasks with strict deadlines and high priority. They use priority-based scheduling algorithms to ensure that the most important tasks are executed first and within the specified time .
- **Response Time**: General Purpose OS do not guarantee a fixed response time for any task, as they may be interrupted by other processes or events. They are suitable for applications that do not require real-time performance. RTOS guarantee a bounded response time for any task, as they have minimal or no interruptions from other processes or events. They are suitable for applications that require real-time performance, such as embedded systems, robotics, or industrial control  .
- **Memory Management**: General Purpose OS use various techniques, such as memory segmentation, paging, and swapping, to manage the memory allocation and deallocation for the processes. They may also use virtual memory to extend the physical memory. RTOS use static memory allocation and fixed-size memory blocks to manage the memory for the tasks. They do not use virtual memory, as it may introduce unpredictability and latency in the system .
- **User Interface**: General Purpose OS provide a user-friendly graphical interface for the users, as they contain multiple menus, buttons, icons, and more for easy navigation. They also support various input and output devices, such as keyboards, mice, monitors, printers, etc. RTOS do not provide a graphical interface for the users, as they are mainly focused on the functionality and performance of the tasks. They also have limited support for input and output devices, such as sensors, actuators, LEDs, etc .
- **Examples**: Some examples of General Purpose OS are Windows, Linux, MacOS, Android, etc. Some examples of RTOS are FreeRTOS, VxWorks, QNX, RTLinux, etc .



### Basic architecture of an RTOS

- An RTOS is a Real-Time Operating System that provides predictable and deterministic behavior for embedded and IoT applications.
- An RTOS typically consists of a kernel and various modules that provide additional functionality, such as networking, debugging, device I/O, etc.
- The kernel is the core component of the RTOS that manages the tasks, memory, timers, interrupts, and synchronization mechanisms.
- The tasks are the basic units of execution in an RTOS. They have a priority, a stack, a context, and a state. The state can be ready, running, blocked, or suspended.
- The scheduler is the part of the kernel that decides which task to run next based on the priority and the state of the tasks. The scheduler can be preemptive or cooperative, depending on the RTOS design.
- The memory management module is responsible for allocating and deallocating memory for the tasks and the kernel. It can use static or dynamic memory allocation, depending on the RTOS design.
- The timer module provides the ability to measure time and trigger events at specific intervals. It can use hardware or software timers, depending on the RTOS design.
- The interrupt module handles the external and internal interrupts that occur during the execution of the tasks. It can use interrupt service routines (ISRs) or deferred interrupt handlers, depending on the RTOS design.
- The synchronization module provides the mechanisms to coordinate the access to shared resources and data among the tasks. It can use semaphores, mutexes, queues, events, or message passing, depending on the RTOS design.
- The modules that provide additional functionality, such as networking, debugging, device I/O, etc., are usually implemented as libraries or drivers that interface with the kernel and the tasks. They can use standard or proprietary protocols, depending on the RTOS design.

The following diagram shows a general architecture of an RTOS:

```
+-----------------+
|   Application   |
+-----------------+
|   Networking    |
|   Debugging     |
|   Device I/O    |
+-----------------+
|      Kernel     |
+-----------------+
|  Task Manager   |
| Memory Manager  |
|  Timer Manager  |
| Interrupt Manager|
|Sync. Mechanisms |
+-----------------+
|     Hardware    |
+-----------------+
```

References:

: RTOS - Real Time Operating System - Engineers Garage
: What Is A Real-Time Operating Systems (RTOS) | Wind River
: RTOS Introduction - Real Time Operating System with Examples
: Understand Azure RTOS ThreadX | Microsoft Learn
: Real-time operating system - Wikipedia
: Architecture of RTOS - Part 1 - Robocraze



### Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a mechanism that determines which task or process should run on a processor at a given time, based on some criteria and constraints.
- A real-time operating system (RTOS) is an operating system that guarantees a certain level of performance and responsiveness for time-critical applications.
- An open source RTOS is a RTOS that is freely available and can be modified and distributed by anyone, subject to the terms of its license.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, RIOT, and NuttX.
- Some of the factors that affect the choice of a scheduling system for an open source RTOS are:
  - The type of tasks or processes: periodic, aperiodic, or sporadic.
  - The timing requirements: hard, firm, or soft real-time.
  - The resource constraints: memory, power, or CPU utilization.
  - The system architecture: single-core, multi-core, or distributed.
  - The application domain: automotive, aerospace, industrial, or IoT.
- Some commonly used RTOS scheduling algorithms are:
  - Cooperative scheduling: tasks voluntarily yield the processor to other tasks when they are idle or waiting for an event.
  - Preemptive scheduling: tasks can be interrupted and replaced by higher priority tasks at any time.
  - Rate-monotonic scheduling: tasks are assigned fixed priorities based on their periods, with shorter periods having higher priorities.
  - Round-robin scheduling: tasks with equal priorities are executed in a circular order, with each task getting a fixed time slice.
  - Fixed priority pre-emptive scheduling: tasks are assigned fixed priorities and preempted by higher priority tasks, but can also use time slicing within each priority level.
  - Fixed-Priority Scheduling with Deferred Preemption: tasks are assigned fixed priorities and preempted by higher priority tasks, but can defer preemption until they reach a preemption point.
  - Fixed-Priority Non-preemptive Scheduling: tasks are assigned fixed priorities and executed until completion, without being preempted by higher priority tasks.
- The advantages and disadvantages of each scheduling algorithm depend on the characteristics and requirements of the system and the application. Some general trade-offs are:
  - Cooperative scheduling is simple and easy to implement, but can cause long delays and missed deadlines if tasks do not yield the processor frequently or appropriately.
  - Preemptive scheduling is responsive and can handle dynamic and unpredictable events, but can cause high overhead and complexity due to context switching and synchronization.
  - Rate-monotonic scheduling is optimal for periodic tasks with hard real-time constraints, but can suffer from priority inversion and resource contention.
  - Round-robin scheduling is fair and balanced for tasks with equal priorities, but can cause poor performance and jitter for tasks with different priorities or periods.
  - Fixed priority pre-emptive scheduling is flexible and widely used, but can be difficult to analyze and verify for schedulability and correctness.
  - Fixed-Priority Scheduling with Deferred Preemption can reduce the preemption overhead and improve the resource utilization, but can increase the blocking time and the response time of lower priority tasks.
  - Fixed-Priority Non-preemptive Scheduling can eliminate the preemption overhead and the priority inversion problem, but can cause long delays and missed deadlines for higher priority tasks.



### Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS.
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- IPC can be implemented using different techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls.
- Shared memory is a technique where processes access a common memory region to exchange data.
- Pipes are unidirectional or bidirectional channels that allow processes to send and receive data in a stream.
- Queues are data structures that store data in a FIFO (first-in, first-out) order and allow processes to send and receive messages .
- Mailboxes are similar to queues, but they store only one message at a time and overwrite the previous message if a new one arrives.
- Signals are events that notify processes about the occurrence of a condition or a change in the system state.
- Remote procedure calls are a technique where processes invoke functions or procedures in another process and receive the results.

- Different open source RTOSes provide different IPC APIs and features. For example, FreeRTOS supports queues, binary semaphores, counting semaphores, recursive semaphores, mutexes, event groups, and software timers .
- IPC APIs can have different parameters, return values, and error codes depending on the RTOS implementation .
- IPC APIs can also have different performance, reliability, and security characteristics depending on the RTOS design .
- IPC APIs should be used carefully and correctly to avoid common problems, such as deadlock, starvation, priority inversion, buffer overflow, and data corruption .



### Performance Metric in Scheduling Models

- A performance metric is a measure of how well a project is performing against its objectives, such as quality, cost and time.
- A scheduling model is a representation of the activities, resources and constraints involved in a project, such as a Gantt chart, a network diagram or a critical path method.
- A performance metric in a scheduling model is a way of evaluating the progress and efficiency of a project based on its schedule, such as the earned value, the schedule variance or the schedule performance index.
- Some common performance metrics in scheduling models are:

  - Earned Value (EV): The value of the work completed so far, based on the planned value and the percentage of completion.
  - Planned Value (PV): The value of the work that should have been completed by a certain date, based on the baseline schedule and the budget.
  - Actual Cost (AC): The amount of money spent on the project so far.
  - Schedule Variance (SV): The difference between the earned value and the planned value, indicating whether the project is ahead or behind schedule. SV = EV - PV.
  - Schedule Performance Index (SPI): The ratio of the earned value to the planned value, indicating how efficiently the project is using its time. SPI = EV / PV.
  - Critical Path: The sequence of activities that determines the minimum duration of the project, based on the dependencies and the durations of each activity.
  - Critical Chain: The sequence of activities that determines the minimum duration of the project, based on the dependencies, the durations and the resource availability of each activity.
  - Slack or Float: The amount of time that an activity can be delayed without affecting the project completion date, based on the earliest and latest start and finish times of each activity.
  - Resource Leveling: The process of adjusting the start and finish times of activities to balance the demand and supply of resources, such as labor, equipment or materials.
  - Resource Allocation: The process of assigning resources to activities based on their availability, priority and suitability.



### Interrupt management in RTOS environment

- An interrupt is a signal that causes the processor to temporarily suspend its current execution and switch to a predefined handler routine.
- Interrupts are useful for handling time-critical events, such as input/output, timers, sensors, etc.
- Interrupts can also be a source of latency and unpredictability in real-time systems, especially when using an RTOS.
- An RTOS is a software that manages the execution of multiple tasks on a single processor, according to some scheduling policy and priority scheme.
- An RTOS typically provides services such as task creation, synchronization, communication, memory management, etc.
- An RTOS also handles interrupts by providing an interrupt dispatcher that invokes the appropriate user-defined interrupt service routine (ISR) for each interrupt source.
- An ISR is a function that performs the minimal amount of work required to acknowledge and service the interrupt, and then returns control to the RTOS.
- An ISR should not call any RTOS function that might cause a task switch, such as blocking, yielding, or sending a message, unless the RTOS is aware that an ISR is running and can handle it safely.
- An ISR should also not perform any long or complex operations that might delay the execution of other ISRs or tasks, or violate the real-time constraints of the system.
- An ISR should defer most of the processing to another thread, such as a task or a deferred interrupt handler (DHI), that can use the RTOS services and has a lower priority than the ISR.
- A DHI is a special type of task that is activated by an ISR and runs in the background to complete the interrupt processing.
- A DHI can be implemented using various mechanisms, such as semaphores, queues, software timers, event flags, etc.
- A DHI can also be preempted by other tasks or ISRs, depending on the RTOS scheduling policy and priority scheme.
- The main advantages of using DHIs are:
  - Reducing the interrupt latency, which is the time between the occurrence of an interrupt and the execution of its ISR.
  - Reducing the interrupt jitter, which is the variation in the interrupt latency.
  - Reducing the interrupt blocking time, which is the time during which an ISR disables other interrupts to prevent interference.
  - Improving the modularity and maintainability of the interrupt code, by separating the ISR and the DHI into different functions or modules.
  - Improving the portability and compatibility of the interrupt code, by using the RTOS services and abstractions instead of the hardware-specific details.
- The main challenges of using DHIs are:
  - Ensuring the correct synchronization and communication between the ISR and the DHI, to avoid data corruption, race conditions, or missed events.
  - Ensuring the correct priority assignment and scheduling of the DHI, to avoid priority inversion, deadlock, or starvation.
  - Ensuring the correct error handling and recovery of the DHI, to avoid system instability, inconsistency, or failure.



### Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in a real-time operating system (RTOS).
- Memory management is important for ensuring the performance, reliability, and security of an RTOS and its applications.
- Memory management can be done in different ways, depending on the design and requirements of the RTOS and the hardware platform.
- Some of the common memory management options for open source RTOS are:

  - **Static memory allocation**: This option allocates memory for the tasks and objects at compile time, and does not use any dynamic memory allocation at run time. This option is suitable for systems with limited memory and deterministic behavior, as it avoids memory fragmentation and overhead. However, this option also limits the flexibility and scalability of the system, as the memory size and layout are fixed and cannot be changed at run time. An example of an open source RTOS that supports static memory allocation is FreeRTOS .
  - **Dynamic memory allocation**: This option allocates memory for the tasks and objects at run time, using a heap or a pool of memory blocks. This option is suitable for systems that need to adapt to changing workloads and resource demands, as it allows the creation and deletion of tasks and objects at run time. However, this option also introduces the risk of memory fragmentation, memory leaks, and memory corruption, as well as the overhead of memory allocation and deallocation. An example of an open source RTOS that supports dynamic memory allocation is Azure RTOS.
  - **Hybrid memory allocation**: This option combines static and dynamic memory allocation, by allowing the application writer to choose the best option for each task and object. This option is suitable for systems that need to balance the trade-offs between static and dynamic memory allocation, as it allows the optimization of memory usage and performance for different scenarios. An example of an open source RTOS that supports hybrid memory allocation is FreeRTOS .

- Memory management in open source RTOS also involves the use of various features and techniques, such as:

  - **Preemptive multitasking**: This feature allows the RTOS to switch between tasks based on their priority and timing requirements, ensuring that the most important and urgent tasks are executed first. This feature improves the responsiveness and predictability of the system, but also requires careful management of the memory resources shared by the tasks, such as stack, heap, and global variables. An example of an open source RTOS that supports preemptive multitasking is FreeRTOS .
  - **Interrupt handling**: This feature allows the RTOS to respond to external events, such as hardware signals, timers, or user inputs, by temporarily suspending the current task and executing a special function called an interrupt service routine (ISR). This feature improves the reactivity and efficiency of the system, but also requires careful management of the memory resources used by the ISR, such as stack, registers, and local variables. An example of an open source RTOS that supports interrupt handling is Azure RTOS.
  - **Real-time scheduling**: This feature allows the RTOS to assign the CPU time to the tasks based on their priority and deadline, ensuring that the tasks meet their timing constraints and quality of service. This feature improves the performance and reliability of the system, but also requires careful management of the memory resources needed by the scheduler, such as queue, semaphore, mutex, and event group. An example of an open source RTOS that supports real-time scheduling is FreeRTOS .
  - **Memory protection**: This feature allows the RTOS to isolate and protect the memory regions used by different tasks and objects, preventing unauthorized access, modification, or deletion of memory. This feature improves the security and robustness of the system, but also requires additional hardware support, such as memory management unit (MMU) or memory protection unit (MPU). An example of an open source RTOS that supports memory protection is Azure RTOS.
  - **Memory optimization**: This technique allows the RTOS to reduce the memory footprint and overhead of the system, by using various methods, such as memory pooling, memory compression, memory reuse, and memory trimming. This technique improves the efficiency and scalability of the system, but also requires careful analysis and testing of the memory behavior and performance of the system. An example of an open source RTOS that supports memory optimization is FreeRTOS[^



### File systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A file system is a software component that organizes and manages the storage and retrieval of data on a storage device, such as a flash memory, hard disk, or SD card.
- A file system provides an abstraction layer for applications to access data using logical names, directories, and file attributes, instead of physical addresses or sectors.
- A file system also maintains the integrity and consistency of the data, especially in the case of power failures, system crashes, or unexpected removals of the storage device.
- A file system for an open source RTOS should be compatible with the RTOS's design goals, such as small footprint, high performance, reliability, portability, and scalability.
- Some examples of file systems for open source RTOS are:

  - Reliance Edge: a transactional, fail-safe, and MISRA compliant file system for FreeRTOS. It supports FAT12, FAT16, and FAT32 formats, and can protect critical data from corruption.
  - Azure RTOS FileX: a high-performance, FAT-compatible file system for Azure RTOS. It supports FAT12, FAT16, FAT32, and exFAT formats, and is fully integrated with Azure RTOS ThreadX .
  - IMFS: an in-memory file system for RTEMS. It provides a small, memory-resident root file system to facilitate mounting other file systems and to ensure a file system is available even if storage devices are not connected.
  - Mini-IMFS: a stripped-down version of IMFS for RTEMS, aiming toward lower memory overhead.
  - JFFS2: a log-structured, flash-friendly file system for Linux. It supports wear leveling, compression, and power fail recovery.
  - YAFFS: a NAND flash file system for Linux. It supports wear leveling, bad block handling, and power fail recovery.

- Some factors to consider when choosing a file system for an open source RTOS are:

  - The type and size of the storage device
  - The compatibility with existing file formats and standards
  - The performance and memory requirements
  - The reliability and robustness
  - The licensing and support options



### I/O Systems

- I/O systems are the components that enable an embedded system to interact with the external world, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
- Parallel I/O systems use multiple wires to transfer data simultaneously, while serial I/O systems use one or a few wires to transfer data sequentially.
- Parallel I/O systems are faster but require more hardware resources, while serial I/O systems are slower but require less hardware resources.
- Some examples of parallel I/O systems are GPIO (General Purpose Input/Output), LCD (Liquid Crystal Display), and memory buses.
- Some examples of serial I/O systems are UART (Universal Asynchronous Receiver/Transmitter), SPI (Serial Peripheral Interface), I2C (Inter-Integrated Circuit), and USB (Universal Serial Bus).
- I/O systems can also be classified into two modes: polling and interrupt.
- Polling mode is when the embedded system continuously checks the status of the I/O device to determine if there is any data to read or write.
- Interrupt mode is when the embedded system is notified by the I/O device when there is any data to read or write, using a signal called an interrupt.
- Polling mode is simpler but consumes more CPU time, while interrupt mode is more complex but consumes less CPU time.
- I/O systems can also be classified into two types: synchronous and asynchronous.
- Synchronous I/O systems are those that operate at a fixed rate or frequency, such as timers, PWM (Pulse Width Modulation), and ADC (Analog to Digital Converter).
- Asynchronous I/O systems are those that operate at a variable rate or frequency, such as keyboards, mice, and sensors.
- Synchronous I/O systems are easier to program but require more hardware resources, while asynchronous I/O systems are harder to program but require less hardware resources.
- I/O systems are essential for embedded systems and real time operating systems (RTOS) to perform their specific functions in a much larger system.
- RTOS are operating systems that provide a worst case time estimate for critical situations and guarantee to finish a task in a defined period.
- RTOS are used in embedded systems that work within strict time constraints and require high reliability, such as medical devices, industrial machines, and automotive systems.
- RTOS can be provided under a paid license or an open source license, depending on the vendor and the user's needs.
- Some examples of RTOS are FreeRTOS, VxWorks, QNX, and Embedded Linux.



### Advantage and disadvantage of RTOS

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what is usually called a "hard" real-time operating system, if the calculation could not be performed for making the object available at the designated time, the operating system would terminate with a failure. In a "soft" real-time operating system, the assembly line would continue to function but the production output might be lower as objects failed to appear at their designated time, causing the robot to be temporarily unproductive. Some real-time operating systems are created for a special application and others are more general purpose. Some existing general purpose operating systems claim to be real-time operating systems. To some extent, almost any general purpose operating system such as Microsoft's Windows 2000 or IBM's OS/390 can be evaluated for its real-time operating system qualities. That is, even if an operating system doesn't qualify, it may have characteristics that enable it to handle some real-time situations.

Some of the advantages and disadvantages of RTOS are:

- Advantages:
  - Maximum consumption: RTOS can utilize the system resources efficiently and produce more output while keeping all devices in active state. There is little or no downtime in these systems  .
  - Task shifting: RTOS can switch between tasks quickly and with minimal overhead. The time assigned for shifting tasks in these systems is very low. For example, in older systems, it takes about 10 microseconds, whereas in newer systems, it takes about 3 to 5 microseconds.
  - Deterministic behavior: RTOS can guarantee that a certain task will be completed within a specified time limit, regardless of the system load or other factors. This is essential for applications that require high reliability and predictability, such as medical devices, industrial control, aerospace, etc .
  - High performance: RTOS can achieve high performance by using specialized algorithms and data structures, such as priority queues, preemptive scheduling, fast interrupt handling, etc. RTOS can also optimize the system for a specific hardware platform, such as using memory-mapped I/O, direct memory access, etc .

- Disadvantages:
  - Longer wait for low-priority tasks: As an RTOS is programmed to execute priority tasks within specific deadlines, lower priority tasks may have to wait longer versus an OS. This may affect the responsiveness and quality of service of some applications that are not time-critical, such as user interfaces, multimedia, etc.
  - Minimal task capacity: As well as a lack of suitability with multi-tasking, an RTOS can only run minimal tasks simultaneously. This is because each task requires a certain amount of memory, stack, and CPU time, which are limited resources in an embedded system. Therefore, an RTOS may not be able to handle complex applications that require many concurrent tasks, such as web servers, databases, etc.
  - High development cost: Developing an RTOS is a challenging and expensive task, as it requires a deep understanding of the system requirements, hardware specifications, and software design. An RTOS also needs to be thoroughly tested and verified for its correctness and robustness, as any error or failure can have severe consequences. Moreover, an RTOS may need to be customized or modified for different applications or platforms, which adds to the development cost and time .



### POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX stands for Portable Operating System Interface, which is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines both the system and user-level application programming interfaces (APIs), along with command line shells and utility programs, for software compatibility.
- POSIX also provides real-time extensions for supporting real-time and embedded systems, such as scheduling, synchronization, timers, signals, message queues, shared memory, semaphores, etc.
- The benefits of POSIX for embedded systems are:
  - Interoperability: POSIX enables applications to run on different operating systems that support the POSIX standard, without requiring major modifications.
  - Portability: POSIX allows developers to use the same tools and libraries across different platforms, reducing the learning curve and development time.
  - Scalability: POSIX supports a range of system sizes and configurations, from small embedded devices to large distributed systems, with minimal overhead and complexity.
  - Reliability: POSIX provides well-defined and tested interfaces and behaviors, ensuring consistent and predictable results.
- The POSIX standards relevant to real-time and embedded systems are:
  - 1003.1a: This standard defines the core OS services, such as process management, file operations, signals, pipes, etc.
  - 1003.1b: This standard defines the real-time extensions, such as priority scheduling, timers, clocks, asynchronous I/O, etc.
  - 1003.1c: This standard defines the threads extensions, such as thread creation, synchronization, cancellation, etc.
  - 1003.1d: This standard defines the additional real-time extensions, such as message passing, shared memory, semaphores, etc.
  - 1003.1j: This standard defines the advanced real-time extensions, such as sporadic server, trace, etc.
  - 1003.13: This standard defines the profiles for real-time systems, such as minimal, deferrable, and preemptible.
  - 1003.26: This standard defines the device control and management interfaces, such as device drivers, configuration, etc.
- The current version of the POSIX standard is POSIX.1-2017, which is also known as IEEE Std 1003.1-2017 or ISO/IEC 9945:2009.
- The Open Group is the organization that publishes and maintains the POSIX standard, along with other test suites and certification programs.



### RTOS Issues

- An RTOS (Real-Time Operating System) is a software platform that provides predictable and deterministic behavior for embedded applications that have real-time constraints.
- However, using an RTOS also introduces some challenges and issues that developers need to be aware of and address in their design and implementation.
- Some of the common RTOS issues are:

  - **Priority inversion**: This occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task. This results in the high-priority task waiting longer than expected for the resource, violating its timing requirements .
  - **Deadlock**: This occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed. This leads to a system-wide stall and wasted CPU cycles .
  - **Task jitter**: This occurs when a task experiences variable execution times due to factors such as preemption, interrupts, cache misses, or memory access delays. This can affect the accuracy and performance of the task, especially if it is time-sensitive .
  - **Control-flow complexity**: This occurs when the control-flow of the program is not apparent from the source code, since the RTOS decides which task to execute at any given moment. This makes it harder to debug, test, and maintain the code, as well as to reason about its behavior and timing.
  - **Security risks**: This occurs when the RTOS or the application does not implement or use security features such as encryption, authentication, authorization, or integrity checks. This can expose the system to attacks such as data theft, tampering, denial-of-service, or remote control.
  - **Interrupt latency**: This occurs when the RTOS takes too long to respond to an interrupt request, potentially missing or delaying the handling of critical events. This can be caused by factors such as disabling interrupts, long-running tasks, or nested interrupts.
  - **Resource management**: This occurs when the RTOS or the application does not allocate, deallocate, or reuse resources such as memory, CPU, or peripherals efficiently or correctly. This can lead to memory leaks, fragmentation, starvation, or contention .



### Selecting a Real-Time Operating System

A real-time operating system (RTOS) is a software platform that provides predictable and deterministic behavior for embedded systems that have strict timing constraints. An RTOS can manage the concurrent execution of multiple tasks, prioritize them according to their deadlines, and handle interrupts and inter-task communication efficiently. Choosing the right RTOS for a specific application can be a challenging task, as there are many factors to consider. Here are some steps that can help in the selection process:

- Step 1: Requirements review. The very first step is to thoroughly review the requirements for the OS, such as the target hardware platform, the required functionality, the performance metrics, the memory footprint, the power consumption, the security, and the reliability. These requirements will help to narrow down the list of potential candidates and eliminate those that do not meet the minimum criteria.
- Step 2: Availability on target platform. The next step is to check if the RTOS is available and compatible with the chosen hardware platform, such as the processor architecture, the peripherals, and the development tools. Most RTOSs are only available for a limited set of processor architectures, such as x86, Power Architecture, MIPS, and ARM. Some RTOSs may also require specific hardware features, such as memory management units, timers, or interrupt controllers. It is important to verify that the RTOS can run on the target hardware and support its features.
- Step 3: Support of required functions. The third step is to evaluate the RTOS based on the support of the required functions, such as the task scheduling algorithm, the inter-task communication mechanisms, the interrupt handling, the memory management, the file system, the network stack, the device drivers, the debugging and testing tools, and the application programming interfaces (APIs). These functions will determine the functionality, the performance, the usability, and the portability of the RTOS. It is important to compare the RTOSs based on their features and capabilities, and not just on their marketing claims.
- Step 4: Portability. The fourth step is to assess the portability of the RTOS, which is the ability to run the same application code on different hardware platforms with minimal or no changes. Portability can reduce the development time and cost, as well as increase the reusability and maintainability of the code. Portability depends on the level of abstraction and standardization of the RTOS APIs, as well as the availability of the RTOS source code and documentation. It is important to choose an RTOS that follows industry standards, such as POSIX, and provides clear and comprehensive documentation and support.
- Step 5: Being future-proof. The fifth step is to consider the future-proofness of the RTOS, which is the ability to adapt to the changing needs and requirements of the application and the market. Future-proofness depends on the scalability, the modularity, the extensibility, and the upgradability of the RTOS. It is important to choose an RTOS that can scale up or down to meet the performance and resource demands, that can be customized and configured to suit the application needs, that can be extended with new features and functions, and that can be upgraded with new versions and patches.
- Step 6: Existing internal experience. The sixth step is to leverage the existing internal experience and expertise of the development team with the RTOS. Having prior knowledge and familiarity with the RTOS can reduce the learning curve and the risk of errors and bugs, as well as increase the productivity and efficiency of the development process. It is important to choose an RTOS that matches the skill level and the preferences of the developers, and that provides adequate training and support resources.
- Step 7: Evaluate alternatives. The seventh step is to evaluate the alternatives to the RTOS, such as using a general-purpose operating system (GPOS), a bare-metal system, or a custom-built OS. These alternatives may offer some advantages over the RTOS, such as lower cost, higher performance, or more flexibility, but they may also have some disadvantages, such as less predictability, less functionality, or more complexity. It is important to weigh the pros and cons of each alternative, and to compare them with the RTOS based on the application requirements and constraints.
- Step 8: Support, partnerships, working together. The final step is to consider the support, the partnerships, and the working relationship with the RTOS vendor or provider. The quality and availability of the support, such as the technical assistance, the documentation, the forums, and the updates, can affect the success and the satisfaction of the development project. The partnerships and the



### RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we provide a brief description and comparison of some of the most popular and widely used RTOSs.

- **FreeRTOS**: FreeRTOS is a free and open source RTOS that supports multiple architectures and platforms. It is designed to be small, simple, and scalable. It provides basic features such as tasks, queues, semaphores, timers, and event groups. It also supports advanced features such as memory management, software timers, tickless mode, and trace tools. FreeRTOS is suitable for embedded systems that require minimal overhead and high reliability. Some of the advantages of FreeRTOS are:

  - It is free and open source, which means that users can modify and customize it according to their needs and preferences.
  - It is widely used and supported by a large community of developers and users, which means that there are many resources and examples available online.
  - It is portable and adaptable, which means that it can run on various hardware platforms and architectures with minimal changes.
  - It is lightweight and efficient, which means that it consumes less memory and CPU resources than other RTOSs.

  Some of the disadvantages of FreeRTOS are:

  - It lacks some features that are available in other RTOSs, such as file system, networking, graphics, and security.
  - It has a steep learning curve, which means that users need to have a good understanding of the RTOS concepts and APIs to use it effectively.
  - It has limited documentation and support, which means that users may encounter difficulties and challenges when developing and debugging their applications.

- **Zephyr**: Zephyr is a free and open source RTOS that supports multiple architectures and platforms. It is designed to be modular, secure, and scalable. It provides basic features such as threads, synchronization, timers, and interrupts. It also supports advanced features such as memory protection, networking, Bluetooth, USB, file system, and shell. Zephyr is suitable for embedded systems that require low power consumption, high performance, and connectivity. Some of the advantages of Zephyr are:

  - It is free and open source, which means that users can modify and customize it according to their needs and preferences.
  - It is actively developed and maintained by a large community of developers and users, which means that it is constantly updated and improved.
  - It is modular and configurable, which means that users can select and enable the features and components that they need for their applications.
  - It is secure and robust, which means that it provides mechanisms to protect the system and the applications from errors and attacks.

  Some of the disadvantages of Zephyr are:

  - It is relatively new and immature, which means that it may have some bugs and issues that need to be resolved.
  - It has a complex architecture and design, which means that users need to have a good understanding of the RTOS concepts and APIs to use it effectively.
  - It has limited documentation and support, which means that users may encounter difficulties and challenges when developing and debugging their applications.

- **LynxOS**: LynxOS is a proprietary and commercial RTOS that supports multiple architectures and platforms. It is designed to be POSIX-compliant, reliable, and scalable. It provides basic features such as processes, threads, synchronization, signals, and timers. It also supports advanced features such as memory management, networking, USB, file system, graphics, and shell. LynxOS is suitable for embedded systems that require high performance, compatibility, and functionality. Some of the advantages of LynxOS are:

  - It is POSIX-compliant, which means that it follows the industry standard for operating systems and provides compatibility with other POSIX systems and applications.
  - It is reliable and stable, which means that it has been tested and certified for various safety and security standards and applications.
  - It is scalable and flexible, which means that it can run on various hardware platforms and architectures with minimal changes.
  - It is feature-rich and functional, which means that it provides a comprehensive set of features and components that can meet the diverse needs and requirements of the users.

  Some of the disadvantages of LynxOS are:

  - It is proprietary and commercial, which means that users need to pay a license fee and follow the terms and conditions of the vendor to use it.
  - It is less popular and supported than other RTOSs, which



## Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal and predictable delays .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports two types of tasks: periodic and aperiodic.
  - Periodic tasks are tasks that execute at regular intervals and have deadlines to meet.
  - Aperiodic tasks are tasks that execute in response to external events and have variable execution times.
- A real-time kernel provides mechanisms for task creation, deletion, synchronization, communication, scheduling, and resource management.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time .
  - Hard real-time kernels guarantee that all tasks meet their deadlines, even in the worst-case scenario .
  - Soft real-time kernels allow some tasks to miss their deadlines occasionally, but try to minimize the number and magnitude of deadline violations .
- A real-time kernel can be implemented in different ways, such as modifying the standard kernel, adding a real-time layer to the standard kernel, or developing a separate real-time kernel .
  - Modifying the standard kernel involves changing the kernel source code to reduce the latency and increase the responsiveness of the system .
  - Adding a real-time layer to the standard kernel involves inserting a module between the kernel and the hardware that intercepts and prioritizes the interrupts and system calls .
  - Developing a separate real-time kernel involves creating a standalone kernel that runs on a dedicated CPU or core and communicates with the standard kernel via shared memory or message passing .



### Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that provides a bounded response time to an external event, regardless of the system load or complexity.
- A normal Linux kernel is not designed for real time applications, as it may incur unpredictable delays due to scheduling, interrupts, locking, memory management, and other factors.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a patch that modifies the existing kernel code to increase predictability and reduce latencies.
- One such patch is the PREEMPT_RT patch, which aims to make the Linux kernel fully preemptible, meaning that any task can be interrupted at any time by a higher priority task.
- The PREEMPT_RT patch also introduces other features, such as priority inheritance, high resolution timers, threaded interrupts, and improved locking mechanisms, to enhance the real time performance of the kernel.
- To install a real time kernel on a Linux system, one needs to follow these steps:

  - Download the PREEMPT_RT patch that matches the kernel version and architecture of the system.
  - Apply the patch to the kernel source code using the patch command.
  - Configure the kernel options using the make menuconfig command, and enable the CONFIG_PREEMPT_RT option under the General setup menu.
  - Compile and install the patched kernel using the make and make install commands, and update the bootloader configuration.
  - Reboot the system and select the real time kernel from the GRUB menu.

- Alternatively, one can install a pre-built real time kernel from a repository, such as the -ml series kernel from CERN, or the kernel-rt package from Red Hat, using the package manager of the system, such as yum or apt.
- After installing a real time kernel, one can verify its functionality by using tools such as rt-tests, which provides a set of tests to measure the latency and jitter of the kernel, or tuned, which provides a set of profiles to optimize the system settings for real time applications.



### Xenomai basics

Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications . Some of the basic concepts of Xenomai are:

- **Real-time threads**: Xenomai allows to run real-time threads either strictly in kernel space, or within the address space of a Linux process. A real-time thread in user space is scheduled by Xenomai directly, and no longer by the Linux kernel. Real-time threads have higher priority than any Linux process and can preempt them at any time.
- **Primary and secondary modes**: A Xenomai thread can switch between two modes of execution: primary mode and secondary mode. In primary mode, the thread is served by the Xenomai scheduler and has access to the real-time services of Xenomai. In secondary mode, the thread is served by the Linux scheduler and has access to the standard Linux services. A thread can switch from primary to secondary mode voluntarily (e.g. by calling a Linux system call) or involuntarily (e.g. by a page fault or a signal). A thread can switch from secondary to primary mode by calling a Xenomai system call or by receiving a Xenomai signal.
- **Skins**: Xenomai provides different interfaces or skins to the real-time services, such as POSIX, VxWorks, or RTAI . A skin defines the API and the semantics of the real-time operations, such as thread creation, synchronization, communication, timers, etc. A user can choose the skin that best suits their needs or preferences, or even create their own skin.
- **Dual kernel approach**: Xenomai uses a dual kernel approach, where the Linux kernel is treated as a background task and is preempted by a smaller and simpler real-time kernel, called the RT-Nucleus . The RT-Nucleus handles the real-time threads and interrupts, while the Linux kernel handles the non-real-time tasks and devices . The RT-Nucleus and the Linux kernel communicate through a mechanism called the Adeos/I-pipe patch, which allows to share the hardware resources and to switch the execution mode .



# Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An open source RTOS is a real-time operating system that is freely available for developers to use, modify, and distribute under a license that allows such actions.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, preemptive scheduling, interrupt handling, inter-task communication, and memory management.
- An embedded system is a computer system that is integrated with a specific hardware device and performs a dedicated function or functions. Embedded systems often have limited resources, such as memory, processing power, and battery life, and require high reliability and efficiency.
- Some examples of embedded systems are smart watches, medical devices, industrial controllers, automotive systems, and IoT devices.
- There are many open source RTOS options for embedded systems, such as FreeRTOS, ChibiOS/RT, RTOS, Zephyr, NuttX, and eCos. Each of them has different features, advantages, and disadvantages, depending on the application requirements and the target platform.
- FreeRTOS is one of the most popular and widely used open source RTOS for embedded systems. It is a market-leading RTOS that has been developed in partnership with the world's leading chip companies over an 18-year period. It is designed to be simple and easy to use, with only 3 source files that are common to all RTOS ports, and one microcontroller specific source file. It has a tick-less mode to directly support low power applications. It supports over 40 architectures and development tools, and has a large and active community of users and contributors.
- ChibiOS/RT is another open source RTOS for embedded systems that is designed to be fast, compact, and portable. It supports over 30 architectures and development tools, and has a modular structure that allows the user to select only the components that are needed for the application. It has a rich set of features, such as dynamic threads, semaphores, mutexes, queues, timers, event flags, memory pools, and heap allocators. It also has a HAL (Hardware Abstraction Layer) that provides a uniform interface to access the hardware peripherals of different platforms.
- Application development for embedded systems using open source RTOS involves several steps, such as selecting the target platform and the RTOS, configuring the RTOS parameters and options, writing the application code, compiling and linking the code, debugging and testing the code, and deploying the code to the device. Depending on the RTOS and the platform, different tools and methods may be used for each step. For example, FreeRTOS provides a configuration header file (FreeRTOSConfig.h) that allows the user to customize the RTOS behavior and features. ChibiOS/RT provides a graphical configuration tool (ChibiStudio) that allows the user to configure the RTOS and the HAL parameters, and also provides an integrated development environment (IDE) for writing, compiling, and debugging the code.



# Real Time Operating Systems

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints .
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism.
  - Predictability means that repeated tasks are performed within a tight time boundary, while in a general-purpose operating system, this is not necessarily so.
  - Determinism means that the system can guarantee a certain response time for a given event or input stimulus.
- An RTOS typically consists of the following components:
  - A kernel that provides the core functionality of the RTOS, such as task scheduling, inter-task communication and synchronization, interrupt handling, and memory management.
  - A set of libraries and APIs that provide additional services and features, such as networking, file system, device drivers, graphical user interface, and security.
  - A development environment that supports the creation, debugging, and testing of real-time applications.
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, and Zephyr.



### Event based real time kernel basics

- A real time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real time kernel can provide deterministic response times to service events, meaning that the system can guarantee to meet certain deadlines or latency requirements.
- A real time kernel is either event based or time based. An event based kernel switches tasks based on priority, while a time based kernel switches tasks based on clock interrupts.
- Events in a real time system are the actions or the results of the actions that are generated by the system or the environment.
- Events in a real time system can be classified into four types:
  - External events: These are events that are generated by the external environment and are independent of the system. For example, a user pressing a button, a sensor detecting a change, or a network packet arriving.
  - Internal events: These are events that are generated by the system itself and are dependent on the system state. For example, a timer expiring, a task completing, or a message being sent or received.
  - Temporal events: These are events that are related to the passage of time and are either periodic or aperiodic. For example, a periodic event occurs at regular intervals, such as a clock tick, while an aperiodic event occurs at irregular intervals, such as a deadline or a sporadic request.
  - Logical events: These are events that are related to the logical conditions of the system and are either true or false. For example, a logical event occurs when a variable reaches a certain value, a flag is set or cleared, or a condition is satisfied or violated.
- An event based real time kernel uses an event queue to store the events that are pending to be serviced by the system.
- An event based real time kernel uses a priority based scheduler to select the highest priority task that is ready to run and preempts the current task if necessary.
- An event based real time kernel can handle both hard and soft real time requirements, depending on the design and implementation of the system.
- An event based real time kernel can provide advantages such as faster response time, lower overhead, and higher flexibility, but also disadvantages such as higher complexity, lower predictability, and higher risk of priority inversion.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of process based for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM. Here is the content I have generated for you in markdown format:

### Process Based
- A process is a program in execution that has its own address space, stack, registers, and other resources.
- A process can be in one of the following states: ready, running, blocked, or terminated.
- A process can create other processes, called child processes, using the fork() system call.
- A process can communicate with other processes using inter-process communication (IPC) mechanisms, such as pipes, message queues, shared memory, semaphores, or sockets.
- A process can be scheduled by the kernel using different scheduling algorithms, such as round-robin, priority-based, or preemptive.
- A process can be terminated by itself using the exit() system call, by another process using the kill() system call, or by the kernel due to an error or a signal.
- A process can be suspended or resumed by another process using the kill() system call with the SIGSTOP or SIGCONT signals, respectively.
- A process can be monitored by another process using the wait() or waitpid() system calls, which return the exit status of the child process.
- A process can be traced by another process using the ptrace() system call, which allows the parent process to control the execution of the child process and examine its memory and registers.



# Graph Based Models for Embedded Systems

- Graph based models are a way of representing the structure and behavior of embedded systems using nodes and edges.
- Nodes can represent components, variables, states, events, or functions of the system, while edges can represent connections, dependencies, transitions, or interactions between nodes.
- Graph based models can be used to analyze, simulate, prototype, specify, and deploy software algorithms within a variety of embedded systems and applications, which is closer to real-world implementation .
- Graph based models can also be used to generate graph embeddings, which are low-dimensional vector representations of the nodes that capture their semantic and structural features.
- Graph embeddings can be used for tasks such as similarity search, recommendation, clustering, classification, or anomaly detection on graph data.
- Graph based models can be classified into different types based on the nature and complexity of the graphs, such as bipartite graphs, general graphs, or knowledge graphs.
- Bipartite graphs are graphs that have two sets of nodes, such that no two nodes within the same set are connected by an edge. For example, a user-item graph in a recommender system is a bipartite graph, where one set of nodes represents users and the other set represents items.
- General graphs are graphs that can have any number of nodes and edges, and can be directed or undirected, weighted or unweighted, cyclic or acyclic. For example, a social network graph is a general graph, where nodes represent users and edges represent friendships, likes, comments, or other interactions.
- Knowledge graphs are graphs that represent structured and semantic information about entities and their relationships, using nodes and edges with labels and attributes. For example, a knowledge graph of movies can have nodes for actors, directors, genres, and movies, and edges for roles, awards, ratings, or reviews.
- Graph based models can be created and manipulated using graphical modeling environments, such as MATLAB/Simulink, Stateflow, or LabVIEW, which provide block diagrams and state machines as graphical elements.
- Graph based models can also be created and manipulated using graph databases, such as Neo4j, TigerGraph, or Amazon Neptune, which provide query languages and APIs for storing and accessing graph data.
- Graph based models can benefit from graph theory and dynamic visualization techniques, which can help understand the properties, patterns, and behaviors of the system, such as connectivity, centrality, modularity, stability, or resilience.



### Petri net models for embedded systems

- Petri nets are a graphical and mathematical tool for modeling and analyzing concurrent and distributed systems.
- Petri nets consist of places, transitions, arcs, and tokens. Places represent conditions or states, transitions represent events or actions, arcs connect places and transitions, and tokens represent resources or data.
- Petri nets can capture features of embedded systems such as concurrency, synchronization, communication, data manipulation, timing, and hierarchy.
- Petri nets can be used for different purposes in embedded system design, such as specification, verification, simulation, and synthesis.
- Petri nets can be classified into different types based on their extensions and properties, such as timed Petri nets, colored Petri nets, hierarchical Petri nets, stochastic Petri nets, etc.
- Petri nets can be combined with other formalisms, such as state machines, automata, logic, etc., to form hybrid models for embedded systems.
- Petri nets can be translated into executable code or hardware description languages for implementing embedded systems.
- Petri nets can be analyzed using various methods, such as reachability analysis, state space analysis, model checking, etc., to ensure the correctness and performance of embedded systems.

Some examples of Petri net models for embedded systems are:

- IPNES (Interpreted Petri Nets for Embedded Systems)  is a new model that allows describing both single-module and distributed embedded systems that require process synchronization and data exchange. IPNES uses a graphical notation and an interpreter to execute the model.
- PRES (Petri net based Representation for Embedded Systems)  is a Petri net based model that can represent several levels of detail using hierarchical decomposition. PRES includes an explicit notion of time, tokens that hold information, and transitions that perform data transformation.
- VHDL-PN (VHDL-based Petri Net)  is a language for high-level synthesis of embedded systems based on Petri nets. VHDL-PN has constructs for message passing, mutual data protection, concurrency, and synchronization. VHDL-PN can be translated into VHDL code for synthesis.
- PRES+ (Petri net based Representation for Embedded Systems with extensions)  is an extension to PRES that improves the expressiveness and analysis capabilities of the model. PRES+ supports the concept of modules, which are reusable components that can be instantiated and connected. PRES+ also allows the specification of timing constraints and properties for verification.



### Real time languages for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real time language is a programming language that supports the development of real time systems, which are systems that must respond to events within strict time constraints.
- Real time languages typically provide features such as concurrency, synchronization, memory management, exception handling, and timing analysis.
- Some examples of real time languages are:

  - Ada: A general-purpose language that supports object-oriented, concurrent, and distributed programming. Ada has a strong focus on reliability, safety, and efficiency. Ada provides a real time annex that defines features such as tasking, scheduling, timing, interrupts, and real time systems.
  - C/C++: The most widely used languages for embedded systems development. C and C++ offer low-level access to hardware, high performance, and portability. C and C++ can be used with real time operating systems (RTOS) and real time libraries that provide features such as threads, semaphores, mutexes, timers, and queues.
  - Java: A high-level, object-oriented language that supports concurrency, exception handling, and garbage collection. Java can be used for real time systems with the Real Time Specification for Java (RTSJ), which defines features such as real time threads, priority inheritance, memory areas, asynchronous events, and real time clocks.
  - Rust: A relatively new language that aims to provide memory safety, concurrency, and performance. Rust has a unique ownership and borrowing system that prevents data races and memory errors. Rust can be used for embedded systems with the Embedded Rust project, which provides tools, libraries, and documentation for developing embedded applications.
  - Python: A high-level, interpreted, and dynamic language that supports multiple programming paradigms. Python is known for its readability, simplicity, and productivity. Python can be used for real time embedded systems with MicroPython, which is a lean and efficient implementation of Python for microcontrollers. MicroPython supports features such as concurrency, interrupts, timers, and modules.



# Real Time Kernel

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible .
- A real-time kernel is optimized for low latency, consistent response time, and determinism .
- A real-time kernel can meet different business or system requirements, such as telco applications, industrial automation, and robotics .
- A real-time kernel is also known as kernel-rt or preempt-rt.
- A real-time kernel can be identified by the rt keyword in the kernel version.
- A real-time kernel can be installed by downloading the ISO image or enabling the repository and performing a group installation.
- A real-time kernel requires some dependent packages, such as rt-setup, rt-tests, and tuned-profiles-realtime.



### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. It is created by the OS to encapsulate all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc.
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the OS that decides which task should run at any given time, based on factors such as priority, deadline, resource availability, etc.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their timing constraints, such as deadlines, response times, etc.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time.
- A hard real-time kernel ensures that tasks will always meet their deadlines, even in the worst-case scenario. A missed deadline can result in a catastrophic failure of the system.
- A soft real-time kernel allows some tasks to miss their deadlines occasionally, without compromising the overall functionality of the system. A missed deadline can result in a degraded performance of the system.
- A real-time kernel can use different scheduling algorithms to manage tasks, such as rate-monotonic, earliest deadline first, round-robin, etc.
- A real-time kernel can also provide features such as inter-task communication, synchronization, memory management, interrupt handling, etc.



### Task States for the Notes of the Unit 3 - Real Time Kernel Basics in the Subject of Embedded Systems and Real Time Operating System

- A task is a basic unit of execution in a real time operating system (RTOS). A task can be a process, a thread, or a coroutine, depending on the implementation of the RTOS.
- A task state is the condition of a task at a given point of time. It indicates whether the task is running, ready, waiting, suspended, or terminated.
- A real time kernel is the core component of an RTOS that manages the tasks and their states, as well as the resources and the interrupts of the system.
- A real time kernel typically supports the following task states:

  - **Running**: The task is currently executing on the processor. Only one task can be in this state at a time, unless the system supports multicore or multiprocessor architectures.
  - **Ready**: The task is eligible to run, but it is not currently running. It is placed in a ready queue, which is a data structure that stores the tasks according to their priorities. The scheduler of the kernel selects the highest priority task from the ready queue to run next.
  - **Waiting**: The task is blocked by an event or a resource that is not available. It is placed in a waiting queue, which is a data structure that stores the tasks according to the event or the resource they are waiting for. The kernel moves the task to the ready queue when the event occurs or the resource becomes available.
  - **Suspended**: The task is temporarily stopped by an external command or a self-request. It is removed from the ready or the waiting queue, and it does not consume any processor time. The kernel resumes the task when the command or the request is reversed.
  - **Terminated**: The task has completed its execution or has been aborted by an error or an exception. It is removed from the system and its resources are freed.

- The task state diagram shows the possible transitions between the task states and the events or the actions that trigger them.

Task State Diagram

- The task state diagram is based on the following assumptions:

  - The system has a single processor and a preemptive scheduler, which means that a higher priority task can interrupt a lower priority task at any time.
  - The system supports dynamic task creation and deletion, which means that new tasks can be created or existing tasks can be deleted at run time.
  - The system supports task suspension and resumption, which means that tasks can be stopped and restarted by external commands or self-requests.
  - The system supports task synchronization and communication, which means that tasks can wait for or signal events, and share or exchange data with other tasks.



# Task scheduling for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Task scheduling is the process of determining how the various tasks are executed by the operating system in a real time system .
- A real time system is a system that has to respond to events within a specified time constraint.
- A real time operating system (RTOS) is an operating system that can guarantee the timely execution of tasks in a real time system.
- A task is a unit of work that can be executed by the RTOS. A task can be periodic, aperiodic, or sporadic, depending on its arrival pattern .
- A periodic task is a task that arrives at regular intervals and has a fixed deadline .
- An aperiodic task is a task that arrives at irregular intervals and has a variable deadline .
- A sporadic task is a task that arrives at unpredictable intervals and has a hard deadline .
- A hard deadline is a deadline that must be met, otherwise the system may fail .
- A soft deadline is a deadline that can be missed, but the system performance may degrade .
- A task scheduler is a component of the RTOS that decides which task to run at any given time  .
- A task scheduler can be classified into two types: preemptive and non-preemptive .
- A preemptive task scheduler is a task scheduler that can interrupt a running task and switch to another task with higher priority .
- A non-preemptive task scheduler is a task scheduler that can only switch to another task when the current task is completed or blocked .
- A priority is a numerical value assigned to a task that indicates its importance or urgency .
- A task scheduler can use different algorithms to assign priorities and select tasks, such as:
  - Run to completion (RTC): A simple algorithm that runs each task until it is finished or blocked, without preemption.
  - Round robin (RR): An algorithm that runs each task for a fixed time slice, and then switches to the next task in a circular order, without considering priorities.
  - Time slice (TS): An algorithm that runs each task for a fixed time slice, and then switches to the next task with the same or higher priority, with preemption.
  - Time slice with background task (TSBG): An algorithm that runs each task for a fixed time slice, and then switches to the next task with the same or higher priority, with preemption, and also runs a low priority background task when no other tasks are ready.
  - Priority (PRI): An algorithm that runs the task with the highest priority at any time, with preemption.
  - Earliest deadline first (EDF): An algorithm that runs the task with the earliest deadline at any time, with preemption .
  - Rate monotonic (RM): An algorithm that assigns priorities to periodic tasks based on their periods, such that the shorter the period, the higher the priority, and runs the task with the highest priority at any time, with preemption .
- A task scheduler should ensure that the system is schedulable, meaning that all the tasks can meet their deadlines under the given algorithm and workload .
- A task scheduler should also consider the overhead of context switching, which is the time and resources required to save and restore the state of a task when switching between tasks .
- A task scheduler should also consider the synchronization and communication between tasks, which may involve shared resources, message passing, semaphores, mutexes, or other mechanisms .
- A task scheduler should also consider the power consumption and energy efficiency of the system, which may involve dynamic voltage and frequency scaling, sleep modes, or other techniques .



### Interrupt Processing

- An interrupt is a signal from a hardware device or a software program that requests the attention of the CPU.
- Interrupts are used to handle events that require immediate or timely response from the CPU, such as keyboard input, mouse movement, network packets, timers, etc.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are generated by external devices, such as keyboards, mice, disks, network cards, etc. They are delivered to the CPU through a network of interrupt controllers and interrupt lines.
- Software interrupts are generated by software programs, such as system calls, exceptions, traps, etc. They are delivered to the CPU through instructions or registers.
- Interrupts can also be classified into two types based on their priority: maskable interrupts and non-maskable interrupts.
- Maskable interrupts are those that can be disabled or enabled by the CPU using special instructions or registers. They are used for normal or low-priority events that can be deferred or ignored if necessary.
- Non-maskable interrupts are those that cannot be disabled or enabled by the CPU. They are used for critical or high-priority events that must be handled immediately and cannot be deferred or ignored.
- When an interrupt occurs, the CPU suspends the execution of the current program and saves its state (such as program counter, registers, flags, etc.) on the stack. Then, the CPU jumps to a predefined address in memory, called the interrupt vector, which contains the address of the interrupt handler or the interrupt service routine (ISR).
- The ISR is a small program that performs the necessary actions to service the interrupt, such as reading or writing data from or to the device, sending or receiving network packets, updating the system clock, etc. The ISR may also acknowledge the interrupt to the interrupt controller or the device, to signal that the interrupt has been handled and the device can generate another interrupt if needed.
- After the ISR finishes its job, the CPU restores the state of the previous program from the stack and resumes its execution.

- Interrupt processing is a crucial aspect of real-time kernel design, as it affects the responsiveness and predictability of the system.
- A real-time kernel must be able to handle interrupts with low latency and high throughput, meaning that it must be able to respond to interrupts quickly and process them efficiently, without interfering with the execution of real-time tasks or processes.
- A real-time kernel must also be able to handle multiple interrupts concurrently or in parallel, meaning that it must be able to service more than one interrupt at a time, without blocking or delaying other interrupts or tasks.
- A real-time kernel must also be able to handle nested interrupts, meaning that it must be able to service an interrupt while another interrupt is being serviced, without corrupting the state of the system or the tasks.
- A real-time kernel must also be able to handle priority inversion, meaning that it must be able to prevent a low-priority interrupt from blocking or delaying a high-priority interrupt or task, by using mechanisms such as priority inheritance, priority ceiling, etc.
- A real-time kernel must also be able to handle interrupt sharing, meaning that it must be able to handle multiple devices or sources that share the same interrupt line, by using mechanisms such as interrupt chaining, polling, etc.
- A real-time kernel must also be able to handle interrupt masking, meaning that it must be able to disable or enable interrupts selectively, based on the current context or mode of the system or the tasks, by using mechanisms such as interrupt disable, interrupt enable, etc.
- A real-time kernel must also be able to handle interrupt affinity, meaning that it must be able to assign interrupts to specific CPUs or cores in a multiprocessor or multicore system, by using mechanisms such as interrupt routing, interrupt binding, etc.



### Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time in the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts or other sources of time information. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The software clock and the hardware clock may not be synchronized, especially if the system is subject to clock drift, time zone changes, daylight saving time adjustments, or manual corrections. Therefore, the kernel provides various mechanisms to synchronize the clocks, such as the Network Time Protocol (NTP), the adjtimex system call, or the clock_settime system call .

The kernel also provides various interfaces to access the clocks, such as the clock_gettime system call, the gettimeofday system call, the time system call, or the /proc and /sys file systems   . The kernel supports different clock IDs to specify which clock to use, such as CLOCK_REALTIME, CLOCK_MONOTONIC, CLOCK_BOOTTIME, or CLOCK_PROCESS_CPUTIME_ID  . Each clock may have different properties, such as resolution, precision, accuracy, stability, and drift .

Clocking is important for real time kernels because it affects the following aspects:

- **Scheduling**: The kernel uses the software clock to determine when to switch between tasks, when to run periodic or sporadic tasks, when to enforce deadlines or priorities, and when to handle timer events or signals .
- **Timing**: The kernel and the user space applications use the clocks to measure the duration or frequency of events, to implement delays or timeouts, to generate timestamps or logs, and to coordinate actions or communications  .
- **Performance analysis**: The kernel and the user space applications use the clocks to monitor the resource utilization, the throughput, the latency, the jitter, the overhead, and the quality of service of the real time system  .

Therefore, clocking is a fundamental concept in real time kernel basics.



### Communication and Synchronization

- Communication and synchronization are essential aspects of real-time kernel design and implementation, as they enable the coordination and cooperation of multiple tasks that share resources and data.
- Communication refers to the transfer of data or messages between tasks, either directly or indirectly, using various methods such as shared memory, message passing, pipes, signals, or sockets.
- Synchronization refers to the control of the execution order and timing of tasks, either explicitly or implicitly, using various mechanisms such as semaphores, mutexes, monitors, condition variables, or events.
- Communication and synchronization methods and mechanisms have different properties and trade-offs in terms of performance, complexity, overhead, scalability, and suitability for different types of tasks and applications.
- Some of the challenges and issues that arise in communication and synchronization in real-time kernel are:
  - Ensuring the correctness and consistency of data and resources that are accessed by multiple tasks concurrently, avoiding data corruption, deadlock, or race conditions.
  - Providing the guarantees and bounds on the communication and synchronization latency and jitter, meeting the timing constraints and deadlines of real-time tasks.
  - Balancing the trade-off between the flexibility and expressiveness of communication and synchronization methods and mechanisms, and the simplicity and efficiency of their implementation and execution.
  - Adapting to the dynamic and unpredictable changes in the workload and environment of real-time applications, such as task arrival, termination, preemption, or migration.
  - Supporting the heterogeneity and diversity of real-time tasks and applications, such as hard, soft, or non real-time tasks, periodic, aperiodic, or sporadic tasks, or single-processor, multiprocessor, or distributed systems.



### Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures used by the real time kernel to store and manage information about the tasks and resources in the system  .
- Control blocks are usually kept in a protected memory area that is inaccessible to the normal user tasks.
- Control blocks can be classified into two types: task control blocks (TCB) and resource control blocks (RCB).
- Task control blocks are used to store information about each task in the system, such as task id, priority, state, stack pointer, program counter, registers, etc  .
- Resource control blocks are used to store information about each resource in the system, such as resource id, type, owner, waiting list, etc.
- The real time kernel uses control blocks to perform various operations, such as task creation, termination, scheduling, synchronization, communication, etc .
- The real time kernel also uses control blocks to handle interrupts, timers, network messages, etc .
- Control blocks are essential for the real time kernel to achieve concurrency, responsiveness, and predictability in the system .



### Memory requirements and control for real time kernel

- A real time kernel is a special type of kernel that provides deterministic and predictable performance for real time applications. Real time applications are those that have strict deadlines and require fast and consistent response times.
- A real time kernel has to manage the memory resources of the system efficiently and effectively, as memory is a critical resource for real time applications. Memory management involves allocating, deallocating, and protecting the memory for different processes and devices.
- Some of the memory requirements and control techniques for real time kernel are:

  - **Memory reservation**: A real time kernel can reserve a certain amount of memory for real time processes and devices, and prevent other non-real time processes from using it. This can ensure that the real time processes have enough memory to run without delays or failures. Memory reservation can be done as a kernel boot parameter or by changing the kernel’s page count at runtime.
  - **Memory protection**: A real time kernel can protect the memory of real time processes from being corrupted or overwritten by other processes or devices. This can prevent errors or crashes that can affect the real time performance. Memory protection can be done by using virtual addressing, paging, or segmentation.
  - **Memory allocation**: A real time kernel can allocate the memory for real time processes and devices in a fast and deterministic way, avoiding fragmentation and overhead. This can reduce the latency and jitter of the real time performance. Memory allocation can be done by using static, dynamic, or hybrid methods, depending on the characteristics and requirements of the real time processes and devices.
  - **Memory deallocation**: A real time kernel can deallocate the memory of real time processes and devices when they are no longer needed, freeing up the memory for other uses. This can improve the memory utilization and efficiency of the system. Memory deallocation can be done by using explicit, implicit, or garbage collection methods, depending on the characteristics and requirements of the real time processes and devices.



### Kernel Services

- The kernel is the core component of an operating system that provides basic services for all other parts of the OS.
- The kernel is typically a small, highly optimized set of libraries that offer an abstraction layer to the application software .
- The kernel services in a real time operating system (RTOS) are those that enable the OS to process data and events that have critically defined time constraints.
- The kernel services in an RTOS include:
  - Task management: This service creates, deletes, suspends, resumes, and prioritizes tasks that run on the system.
  - Task scheduling: This service determines which task should run at any given time based on their priorities and deadlines.
  - Task synchronization: This service coordinates the access of tasks to shared resources, such as memory, files, or devices, using mechanisms such as semaphores, mutexes, or message queues.
  - Memory management: This service allocates and deallocates memory for tasks and manages the memory protection and fragmentation.
  - Time management: This service provides timers, clocks, and delays for tasks and events.
  - Interrupt handling: This service handles the interrupts from hardware devices and software exceptions and dispatches them to the appropriate tasks or handlers.
  - Device I/O management: This service manages the input and output of data from devices, such as sensors, actuators, or communication interfaces, using drivers, buffers, or protocols.



### Basic Design using RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system; it creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides a multi-tasking and deterministic run-time environment, which means that tasks can be executed in a predictable and timely manner.
- An RTOS can be used to design embedded systems that have real-time constraints, such as deadlines, responsiveness, reliability, and performance.
- Some basic design principles using RTOS are :
  - Write short interrupt routines, but not too short. Interrupt routines should perform the minimum necessary work and then return to the main program. Too long interrupt routines can cause delays and jitter in the system. Too short interrupt routines can cause overhead and inefficiency in the system.
  - Use a suitable number of tasks. Tasks are the basic units of execution in an RTOS. The number of tasks should be balanced between the pros and cons of having more or less tasks. More tasks can provide better control of the priorities and response times, better modularity and cleaner code, and more effective encapsulation of data. Less tasks can reduce data sharing, semaphores, message passing, and bugs, and save time on handling them.
  - Avoid creating and destroying tasks while the system is running. Creating and destroying tasks is time consuming and may cause memory leaks or fragmentation. It may be better to create all the tasks at system startup and leave them. If a task is not needed, it can be suspended or blocked until it is needed again.
  - Use RMS to verify your design. RMS, or Rate Monotonic Scheduling, is an analysis technique that designers can use to test their assumptions about whether the tasks in their system can be scheduled successfully. RMS assigns priorities to tasks based on their periods, and guarantees that all tasks will meet their deadlines if the system utilization is less than a certain value.
  - Use semaphores and message queues to synchronize and communicate between tasks. Semaphores are synchronization mechanisms that can be used to protect shared resources or signal events between tasks. Message queues are communication mechanisms that can be used to pass data between tasks. Both semaphores and message queues should be used carefully and correctly to avoid deadlocks, starvation, or data loss.



## Unit 4 - VXWORKS / FREE RTOS

- VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems.
- RTOS are designed to provide deterministic and predictable behavior, low latency, and high reliability for applications that require real-time performance.
- VxWorks and FreeRTOS have some similarities and differences in terms of features, cost, support, and target market.

### Similarities

- Both VxWorks and FreeRTOS are based on the preemptive priority-based scheduling algorithm, which allows tasks to be executed according to their assigned priority and preempted by higher priority tasks when necessary.
- Both VxWorks and FreeRTOS support inter-process communication mechanisms such as message queues, semaphores, mutexes, and event flags, which enable tasks to synchronize and exchange data with each other.
- Both VxWorks and FreeRTOS provide memory management functions such as memory allocation, deallocation, and protection, which allow tasks to use dynamic memory safely and efficiently.
- Both VxWorks and FreeRTOS have low interrupt latency, which means the time between the occurrence of an interrupt and the execution of the corresponding interrupt service routine is minimal.

### Differences

- VxWorks is a proprietary RTOS developed by Wind River Systems, while FreeRTOS is an open-source RTOS created by Richard Barry and maintained by Amazon Web Services.
- VxWorks is a more mature and feature-rich RTOS than FreeRTOS, as it has been in the market since 1987 and supports advanced capabilities such as multicore processing, networking, security, graphics, and file systems.
- VxWorks is a more expensive and complex RTOS than FreeRTOS, as it requires a license fee, a development environment, and a dedicated hardware platform, while FreeRTOS is free, simple, and portable to various architectures and compilers.
- VxWorks is a more widely used and supported RTOS than FreeRTOS, as it has a large customer base, a professional technical support team, and a comprehensive documentation and training resources, while FreeRTOS has a smaller community, a limited support options, and a less extensive documentation and training resources.
- VxWorks is a more suitable RTOS for high-end and mission-critical applications that require high performance, reliability, and security, such as aerospace, defense, automotive, and industrial control, while FreeRTOS is a more suitable RTOS for low-end and cost-sensitive applications that require simplicity, flexibility, and portability, such as IoT, education, and hobby projects.



### VxWorks/ Free RTOS Scheduling and Task Management

- VxWorks and Free RTOS are two popular real-time operating systems (RTOS) that provide multitasking and scheduling capabilities for embedded systems.
- Scheduling is the process of allocating CPU time to different tasks based on their priority, deadline, and resource requirements.
- Task management is the process of creating, deleting, suspending, resuming, and synchronizing tasks in an RTOS.
- VxWorks and Free RTOS have different features and advantages for scheduling and task management, which are summarized below.

#### VxWorks Scheduling and Task Management
- VxWorks uses a priority-based preemptive scheduling algorithm with 256 priority levels, where 0 is the highest and 255 is the lowest .
- VxWorks supports both POSIX and a proprietary scheduling mechanism (wind scheduling) .
- VxWorks also supports round-robin scheduling for tasks with the same priority, where each task gets an equal share of the CPU time  .
- VxWorks provides a rich set of APIs for task management, such as taskSpawn, taskDelete, taskSuspend, taskResume, taskDelay, taskPrioritySet, and taskPriorityGet  .
- VxWorks allows tasks to communicate and synchronize with each other using semaphores, message queues, pipes, signals, events, and shared memory  .
- VxWorks is a deterministic, low-latency, and minimal-jitter RTOS that can handle complex and demanding applications .

#### Free RTOS Scheduling and Task Management
- Free RTOS uses a priority-based preemptive scheduling algorithm with a configurable number of priority levels, where higher numbers indicate higher priority .
- Free RTOS also supports round-robin scheduling for tasks with the same priority, where each task gets a time slice of the CPU time .
- Free RTOS provides a simple and consistent set of APIs for task management, such as xTaskCreate, vTaskDelete, vTaskSuspend, vTaskResume, vTaskDelay, vTaskPrioritySet, and uxTaskPriorityGet .
- Free RTOS allows tasks to communicate and synchronize with each other using queues, semaphores, mutexes, event groups, and software timers .
- Free RTOS is a lightweight, portable, and scalable RTOS that can run on various microcontrollers and architectures .



### Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of allocating CPU time to tasks that have timing constraints and need to be executed in a predictable and deterministic manner.
- A real-time operating system (RTOS) is a software platform that provides the features and services needed to support realtime scheduling and execution of tasks.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.
- VXWORKS is a commercial RTOS developed by Wind River Systems that supports various architectures, such as x86, ARM, PowerPC, and MIPS. It offers a rich set of features, such as preemptive priority-based scheduling, memory protection, inter-process communication, networking, file system, device drivers, and graphical user interface.
- FREE RTOS is an open source RTOS that is designed to be simple, portable, and scalable. It supports many architectures, such as x86, ARM, AVR, and PIC. It provides the core real-time scheduling functionality, inter-task communication, timing and synchronization primitives only. It does not include additional features, such as a command console interface and network stack, but they can be added as optional components.
- The main difference between VXWORKS and FREE RTOS is the level of complexity and functionality they offer. VXWORKS is a more comprehensive and mature RTOS that can handle complex and demanding real-time applications, but it also requires more resources and licensing fees. FREE RTOS is a more lightweight and flexible RTOS that can be easily customized and adapted to different needs, but it also requires more development and integration effort.
- The main similarity between VXWORKS and FREE RTOS is that they both use preemptive priority-based scheduling as the default scheduling algorithm. This means that the scheduler always runs the highest priority task that is ready to run, and preempts the lower priority tasks if necessary. This ensures that the tasks with the most urgent timing requirements are executed first and meet their deadlines.
- The main challenge of realtime scheduling is to deal with priority inversion, which is a situation where a high priority task is blocked by a lower priority task that holds a shared resource. This can cause the high priority task to miss its deadline and compromise the system performance and reliability. Both VXWORKS and FREE RTOS provide mechanisms to prevent or mitigate priority inversion, such as priority inheritance, priority ceiling, and mutexes.



### Task Creation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real-time operating system (RTOS) is a software platform that provides predictable and deterministic behavior for embedded systems that have strict timing and performance requirements .
- An RTOS typically consists of a kernel, which manages the tasks, interrupts, memory, and synchronization primitives, and optional middleware components, such as file systems, networking stacks, and graphical user interfaces.
- VxWorks and FreeRTOS are two popular RTOSes that are widely used in various domains, such as aerospace, defense, automotive, industrial, and medical  .
- VxWorks is a proprietary RTOS developed by Wind River Systems, which offers a proven, secure, and scalable platform for mission-critical embedded systems .
- FreeRTOS is an open source RTOS that is designed to be simple, portable, and lightweight, and supports a large number of architectures and compilers.
- The main differences between VxWorks and FreeRTOS are:

  - VxWorks has a more mature and comprehensive feature set, including advanced security, safety, and multicore support, while FreeRTOS is more focused on simplicity and minimal footprint .
  - VxWorks provides a modern development environment based on the Eclipse IDE, Wind River Linux, and Wind River Simics, while FreeRTOS relies on third-party tools and libraries for development and debugging.
  - VxWorks is a commercial product that requires a license fee and offers professional services and support, while FreeRTOS is free to use and modify under the MIT license and has a community-based support model .
  - VxWorks supports a wider range of hardware platforms and industry standards, such as POSIX, ARINC 653, and FACE, while FreeRTOS has a more limited hardware and standards compatibility .

- The main similarities between VxWorks and FreeRTOS are:

  - Both are preemptive, priority-based RTOSes that offer low latency and minimal jitter for real-time applications .
  - Both support task creation, scheduling, synchronization, communication, and memory management.
  - Both have a modular and configurable architecture that allows users to customize and optimize the RTOS for their specific needs and constraints .
  - Both have a large and active user base and a long history of successful deployments in various domains and projects  .



### Intertask Communication

- Intertask communication is the process of exchanging data or signals between tasks in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources or depend on each other.
- Intertask communication can also be used for event notification, data transfer, synchronization, mutual exclusion, and task management.
- Different RTOSs may provide different mechanisms for intertask communication, such as shared memory, message queues, pipes, semaphores, mutexes, events, signals, etc.
- In this section, we will compare and contrast the intertask communication mechanisms of two popular RTOSs: VxWorks and FreeRTOS.

#### Shared Memory

- Shared memory is a region of memory that can be accessed by multiple tasks concurrently.
- Shared memory is a fast and simple way of intertask communication, but it requires careful synchronization and mutual exclusion to avoid data corruption and race conditions.
- VxWorks supports shared memory communication between tasks in the same or different address spaces, as well as between user space and kernel space .
- FreeRTOS does not provide a specific shared memory mechanism, but tasks can access global variables or memory allocated from the heap.

#### Message Queues

- Message queues are data structures that store messages sent by one task and received by another task in a FIFO (first-in, first-out) order.
- Message queues are useful for transferring data between tasks, especially when the data size and frequency are variable.
- Message queues can also be used for synchronization, as tasks can block on sending or receiving messages until the queue is not full or not empty, respectively.
- VxWorks provides message queues as a kernel object that can be created, deleted, and manipulated by various API functions .
- FreeRTOS provides message queues as a wrapper around the queue primitive, which is the basis of all intertask communication mechanisms in FreeRTOS  .

#### Pipes

- Pipes are data structures that allow one task to write data to a buffer and another task to read data from the buffer in a FIFO order.
- Pipes are similar to message queues, but they have some differences:
  - Pipes can only transfer bytes, while message queues can transfer any data type.
  - Pipes do not have a fixed size, while message queues have a fixed number of messages and message size.
  - Pipes do not support blocking on send or receive, while message queues do.
- VxWorks provides pipes as a kernel object that can be created, deleted, and manipulated by various API functions .
- FreeRTOS does not provide pipes as a separate mechanism, but they can be implemented using the queue primitive .

#### Semaphores

- Semaphores are synchronization mechanisms that use a counter to control the access to a shared resource or a critical section by multiple tasks.
- Semaphores can be either binary or counting, depending on the range of the counter:
  - Binary semaphores have a counter that can only be 0 or 1, and are used for mutual exclusion or event notification.
  - Counting semaphores have a counter that can be any non-negative integer, and are used for resource management or task synchronization.
- VxWorks provides semaphores as a kernel object that can be created, deleted, and manipulated by various API functions .
- FreeRTOS provides semaphores as a wrapper around the queue primitive, and also supports recursive semaphores, which allow a task to take the same semaphore multiple times without blocking  .

#### Mutexes

- Mutexes are synchronization mechanisms that are similar to binary semaphores, but have some additional features:
  - Mutexes support priority inheritance, which prevents priority inversion, a situation where a high-priority task is blocked by a low-priority task that holds a mutex.
  - Mutexes are owned by tasks, which means that only the task that took the mutex can release it, and the mutex is automatically released when the task exits or is deleted.
- VxWorks provides mutexes as a kernel object that can be created, deleted, and manipulated by various API functions .
- FreeRTOS provides mutexes as a wrapper around the queue primitive, and also supports recursive mutexes, which allow a task to take the same mutex multiple times without blocking [^3



### Pipes

Pipes are a form of interprocess communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional way. Pipes are often used to implement filters, where the output of one process is fed as the input of another process.

Some of the characteristics and features of pipes are:

- Pipes are implemented as circular buffers in memory, with a fixed size and a read and write pointer.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the pipe() system call and are only accessible by the parent and child processes that created them.
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available or the pipe is full.
- Pipes can be either synchronous or asynchronous. Synchronous pipes guarantee that the data written to the pipe is read by the other end in the same order and without any loss. Asynchronous pipes do not guarantee any ordering or reliability of the data transfer.
- Pipes can be either byte-stream or message-oriented. Byte-stream pipes treat the data as a continuous stream of bytes, while message-oriented pipes preserve the boundaries of the data units written to the pipe.

#### Pipes in VxWorks

VxWorks is a real-time operating system (RTOS) that supports pipes as a form of IPC. VxWorks pipes have the following features:

- VxWorks pipes are named pipes that are created by the pipeDevCreate() system call. The name of the pipe is a device name that can be used by any process to open the pipe with the open() system call.
- VxWorks pipes are blocking by default, but can be made non-blocking by setting the O_NONBLOCK flag in the open() system call.
- VxWorks pipes are synchronous and byte-stream oriented. The data written to the pipe is guaranteed to be read by the other end in the same order and without any loss. The data is treated as a stream of bytes, without any message boundaries.
- VxWorks pipes have a fixed size that is specified in the pipeDevCreate() system call. The size of the pipe can be between 128 and 65536 bytes. The pipe size can be changed by the pipeDevDelete() and pipeDevCreate() system calls.
- VxWorks pipes have a read and write pointer that indicate the position of the data in the pipe. The read pointer is incremented by the amount of data read from the pipe, and the write pointer is incremented by the amount of data written to the pipe. The pointers wrap around when they reach the end of the pipe buffer.
- VxWorks pipes use semaphores to synchronize the access to the pipe. The pipe has a read semaphore and a write semaphore that are initialized to the size of the pipe. The read semaphore is decremented by the amount of data read from the pipe, and the write semaphore is decremented by the amount of data written to the pipe. The read semaphore is incremented by the write task when it writes data to the pipe, and the write semaphore is incremented by the read task when it reads data from the pipe. The read task blocks on the read semaphore if there is no data available in the pipe, and the write task blocks on the write semaphore if the pipe is full.

#### Pipes in FreeRTOS

FreeRTOS is another RTOS that supports pipes as a form of IPC. FreeRTOS pipes have the following features:

- FreeRTOS pipes are implemented as stream buffers, which are a type of software queue that can store a variable amount of data. Stream buffers can be created by the xStreamBufferCreate() system call, which returns a handle to the stream buffer.
- FreeRTOS pipes are unnamed and can only be accessed by the tasks that have the handle to the stream buffer. The handle can be passed to other tasks by using message queues or other IPC mechanisms.
- FreeRTOS pipes are non-blocking by default, but can be made blocking by specifying a timeout value in the xStreamBufferSend() and xStreamBufferReceive() system calls. The timeout value indicates how long the task should wait for data to be available or for space to be available in the stream buffer.
- FreeRTOS pipes are asynchronous and message-oriented. The data written to the pipe is not guaranteed to be read by the other end in the same order or without any loss. The data is treated as a discrete message, with a length field that indicates the size of the message.
- FreeRTOS pipes have a variable size



### Semaphore for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have a value of 0 or 1, indicating whether the resource is available or not.
- A semaphore can be used to implement mutual exclusion (mutex) or synchronization between threads or processes.
- A mutex is a special type of semaphore that can only be owned by one thread or process at a time. A mutex can be used to protect a critical section of code or data from concurrent access.
- A semaphore can also be used to signal the occurrence of an event or condition to one or more waiting threads or processes. A semaphore can be used to implement a producer-consumer pattern, where one thread or process produces data and another thread or process consumes it.
- In VXWORKS, a semaphore can be created by calling semBCreate() for a binary semaphore, semCCreate() for a counting semaphore, or semMCreate() for a mutex semaphore. A semaphore can be deleted by calling semDelete().
- In VXWORKS, a semaphore can be taken by calling semTake(), which blocks the calling thread or process until the semaphore is available or a timeout occurs. A semaphore can be given by calling semGive(), which releases the semaphore and wakes up any waiting thread or process.
- In VXWORKS, a semaphore can also be given from an interrupt service routine (ISR) by calling semGiveFromISR(), which does not block the ISR but posts the semaphore to a queue for later processing by the kernel.
- In FREE RTOS, a semaphore can be created by calling xSemaphoreCreateBinary() for a binary semaphore, xSemaphoreCreateCounting() for a counting semaphore, xSemaphoreCreateMutex() for a mutex semaphore, or xSemaphoreCreateRecursiveMutex() for a recursive mutex semaphore. A semaphore can be deleted by calling vSemaphoreDelete().
- In FREE RTOS, a semaphore can be taken by calling xSemaphoreTake() or xSemaphoreTakeRecursive(), which blocks the calling task until the semaphore is available or a timeout occurs. A semaphore can be given by calling xSemaphoreGive() or xSemaphoreGiveRecursive(), which releases the semaphore and wakes up any waiting task.
- In FREE RTOS, a semaphore can also be given from an ISR by calling xSemaphoreGiveFromISR(), which does not block the ISR but posts the semaphore to a queue for later processing by the kernel.
- In FREE RTOS, a semaphore is built on a queue, which is a data structure that can store multiple items in a first-in first-out (FIFO) order. A queue can be used to pass data or messages between tasks or ISRs.
- In FREE RTOS+POSIX, a semaphore can be created by calling sem_init() for a named or unnamed semaphore. A semaphore can be deleted by calling sem_destroy() or sem_unlink().
- In FREE RTOS+POSIX, a semaphore can be taken by calling sem_wait() or sem_trywait(), which blocks the calling thread until the semaphore is available or a timeout occurs. A semaphore can be given by calling sem_post(), which releases the semaphore and wakes up any waiting thread.
- In FREE RTOS+POSIX, a semaphore can also be given from an ISR by calling sem_post_from_isr(), which does not block the ISR but posts the semaphore to a queue for later processing by the kernel.
- In FREE RTOS+POSIX, a semaphore is built on a FreeRTOS queue, which is wrapped by a POSIX layer that provides compatibility with the POSIX standard.



### Message Queue

- A message queue is a form of inter-task communication that allows tasks and interrupts to send and receive data by copy.
- A message queue can store multiple messages of the same size, which can be a pointer to larger buffers or structures.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task waiting to receive from the queue.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task waiting to send to the queue.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it or unblocking any task.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.

### VXWORKS

- VXWORKS is a real-time operating system (RTOS) that supports message queues as a kernel object.
- A message queue can be created using the `msgQCreate()` function, which returns an ID to the queue.
- A message can be sent to a queue using the `msgQSend()` function, which copies the message into the queue and wakes up any task pending on the queue.
- A message can be received from a queue using the `msgQReceive()` function, which copies the message from the queue and wakes up any task pending on the queue.
- A message can be peeked from a queue using the `msgQShow()` function, which copies the message from the queue without removing it or waking up any task.
- A message queue can be deleted using the `msgQDelete()` function, which frees the memory allocated for the queue.

### FREE RTOS

- FREE RTOS is a portable, open source, mini RTOS that supports message queues as a core feature.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and unblock any task waiting to receive from the queue.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and unblock any task waiting to send to the queue.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it or unblocking any task.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- FREE RTOS also supports POSIX message queues through the FREE RTOS+POSIX library, which provides a subset of the POSIX API for message queues.



# Signals for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Signals are a form of inter-process communication (IPC) that allow a process to send a notification to another process or to itself.
- Signals can be used to indicate events such as alarms, termination requests, segmentation faults, etc.
- Signals are asynchronous, meaning that they can occur at any time and interrupt the normal flow of execution of the process.
- Signals are identified by integer numbers, usually defined by macros in the header file <signal.h>.
- Signals can be handled in different ways by the process, such as ignoring them, executing a default action, or executing a user-defined function (called a signal handler).

## Signals in VXWORKS

- VXWORKS is a real-time operating system (RTOS) that supports signals as one of the IPC mechanisms.
- VXWORKS signals are similar to UNIX signals, but with some differences and limitations.
- VXWORKS signals can only be sent to tasks, not to processes. A task is a unit of execution that can be created, deleted, suspended, resumed, etc. by the RTOS.
- VXWORKS signals can only be sent within the same address space, not across different address spaces. This means that signals cannot be used for communication between tasks that run in different memory partitions or protection domains.
- VXWORKS signals are not queued, meaning that if multiple signals of the same type are sent to a task, only one of them will be delivered. The order of delivery is not guaranteed.
- VXWORKS signals can be masked, meaning that a task can block the delivery of certain signals until it is ready to handle them. Masking can be done at the task level or at the system level.
- VXWORKS signals can be handled by the default action, which is usually to terminate the task, or by a user-defined signal handler, which is a function that is executed when the signal is delivered.
- VXWORKS signals can be generated by software (using the kill() or sigqueue() functions) or by hardware (using the intConnect() or sigConnect() functions). Hardware signals are usually associated with interrupts, such as timers, serial ports, etc.

## Signals in FREE RTOS

- FREE RTOS is another RTOS that supports signals as one of the IPC mechanisms.
- FREE RTOS signals are different from UNIX or VXWORKS signals, and are more similar to binary semaphores or event flags.
- FREE RTOS signals are also called task notifications, and they are used to notify a task of an event or a condition.
- FREE RTOS signals are 32-bit values that can be sent to a task by another task or by an interrupt service routine (ISR).
- FREE RTOS signals are queued, meaning that multiple signals can be sent to a task and stored in a queue until they are processed. The queue size is configurable and can be set to 1 for binary signals or more for counting signals.
- FREE RTOS signals can be masked, meaning that a task can block the delivery of certain signals until it is ready to handle them. Masking can be done by specifying a bit mask in the xTaskNotifyWait() or xTaskNotify() functions.
- FREE RTOS signals can be handled by the task itself, which can wait for a signal to arrive using the xTaskNotifyWait() function, or by a callback function, which can be registered using the vTaskSetNotificationCallback() function.
- FREE RTOS signals can be generated by software (using the xTaskNotify() or xTaskNotifyFromISR() functions) or by hardware (using the xTimerPendFunctionCallFromISR() or xQueueSendFromISR() functions). Hardware signals are usually associated with peripherals, such as GPIO, ADC, etc.



### Sockets for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A socket is an endpoint of a bidirectional communication channel between two processes or devices over a network.
- Sockets can be used to send and receive data using various protocols, such as TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that ensures data integrity and delivery. UDP is an unreliable, connectionless protocol that offers low latency and high throughput.
- Both VXWORKS and FREE RTOS support sockets as a way of implementing network communication in embedded systems and real-time operating systems.
- VXWORKS is a proprietary, UNIX-like real-time operating system that is widely used in safety-critical applications, such as aerospace, defense, and industrial automation.
- FREE RTOS is an open source, scalable, and thread-safe real-time operating system that is designed for small embedded systems with limited resources.
- VXWORKS and FREE RTOS have different APIs for creating and using sockets, but they both follow the standard Berkeley sockets interface, which is familiar to most programmers .
- To create a socket in VXWORKS, the function `socket()` is used, which takes three parameters: the domain (AF_INET for IPv4), the type (SOCK_STREAM for TCP or SOCK_DGRAM for UDP), and the protocol (0 for default or IPPROTO_TCP or IPPROTO_UDP for specific protocols).
- To create a socket in FREE RTOS, the function `FreeRTOS_socket()` is used, which takes the same three parameters as VXWORKS, but with different names: xDomain (FREERTOS_AF_INET for IPv4), xType (FREERTOS_SOCK_STREAM for TCP or FREERTOS_SOCK_DGRAM for UDP), and xProtocol (0 for default or FREERTOS_IPPROTO_TCP or FREERTOS_IPPROTO_UDP for specific protocols).
- To bind a socket to a specific port number and IP address, the function `bind()` is used in both VXWORKS and FREE RTOS, which takes a socket descriptor, a pointer to a sockaddr_in structure, and the size of the structure as parameters.
- To listen for incoming connections on a TCP socket, the function `listen()` is used in both VXWORKS and FREE RTOS, which takes a socket descriptor and a backlog (the maximum number of pending connections) as parameters.
- To accept a connection on a TCP socket, the function `accept()` is used in both VXWORKS and FREE RTOS, which takes a socket descriptor, a pointer to a sockaddr_in structure, and a pointer to the size of the structure as parameters. It returns a new socket descriptor for the accepted connection.
- To connect to a remote server on a TCP socket, the function `connect()` is used in both VXWORKS and FREE RTOS, which takes a socket descriptor, a pointer to a sockaddr_in structure, and the size of the structure as parameters.
- To send data on a TCP or UDP socket, the function `send()` or `sendto()` is used in both VXWORKS and FREE RTOS, which take a socket descriptor, a pointer to a buffer, the size of the buffer, some flags, and optionally a pointer to a sockaddr_in structure and the size of the structure as parameters.
- To receive data on a TCP or UDP socket, the function `recv()` or `recvfrom()` is used in both VXWORKS and FREE RTOS, which take a socket descriptor, a pointer to a buffer, the size of the buffer, some flags, and optionally a pointer to a sockaddr_in structure and a pointer to the size of the structure as parameters.
- To close a socket, the function `close()` is used in both VXWORKS and FREE RTOS, which takes a socket descriptor as a parameter.



### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and notify the CPU that it should take some action.
- Interrupts can be generated by hardware devices, such as timers, sensors, keyboards, etc., or by software, such as system calls, exceptions, etc.
- Interrupts can be classified into two types: maskable and non-maskable. Maskable interrupts can be disabled or enabled by the CPU, while non-maskable interrupts cannot be ignored by the CPU.
- Interrupts can have different priorities, which determine the order in which they are handled by the CPU. Higher priority interrupts can preempt lower priority interrupts, while lower priority interrupts can be delayed or queued until higher priority interrupts are completed.
- Interrupts can be handled by two methods: polling and vectored. Polling is a method where the CPU periodically checks a status register to see if any interrupt has occurred. Vectored is a method where the CPU jumps to a specific address in memory that contains the interrupt handler code for each interrupt.
- Interrupts can have different effects on the execution of an RTOS task. Depending on the type and priority of the interrupt, the RTOS task can be preempted, resumed, blocked, or woken up by the interrupt.
- Interrupts can also affect the timing and performance of an RTOS task. Interrupts can introduce latency, jitter, and overhead to the RTOS task, which can degrade the quality of service and the determinism of the RTOS.
- Interrupts can be measured by various methods, such as using oscilloscopes, logic analyzers, timers, counters, etc. The measurement of interrupts can help to optimize the RTOS task scheduling, synchronization, and communication.
- Interrupts can be handled by different RTOSes in different ways. Some RTOSes, such as VxWorks, provide a preemptive, deterministic, and secure interrupt handling mechanism that prioritizes real-time embedded applications. Other RTOSes, such as FreeRTOS, provide various methods to handle interrupts that differ in both latency and the consumption of resources. These methods include, standard ISR processing, application controlled deferred interrupt handling, and centralised deferred interrupt handling.



### I/O Systems for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- I/O systems are the mechanisms that enable communication between the embedded system and the external devices or networks.
- I/O systems can be classified into two types: synchronous and asynchronous.
- Synchronous I/O systems are those that operate at a fixed rate and require the embedded system to wait for the completion of the I/O operation before proceeding to the next task.
- Asynchronous I/O systems are those that operate independently of the embedded system and allow the embedded system to perform other tasks while the I/O operation is in progress.
- I/O systems can also be classified into two modes: polling and interrupt-driven.
- Polling mode is when the embedded system periodically checks the status of the I/O device to determine if an I/O operation is needed or completed.
- Interrupt-driven mode is when the embedded system is notified by the I/O device through an interrupt signal when an I/O operation is needed or completed.
- Polling mode is simpler to implement but consumes more CPU time and may cause delays in the embedded system.
- Interrupt-driven mode is more efficient but requires more complex programming and may cause conflicts with other interrupts in the embedded system.
- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that provide I/O systems for embedded systems.
- VXWORKS is a commercial RTOS that supports a wide range of I/O devices and protocols, such as serial, parallel, USB, Ethernet, CAN, I2C, SPI, etc.
- VXWORKS also provides an I/O framework that allows developers to create custom I/O drivers and libraries for specific I/O devices and applications.
- FREE RTOS is an open source RTOS that supports a limited set of I/O devices and protocols, such as serial, USB, Ethernet, etc.
- FREE RTOS also provides an I/O abstraction layer that allows developers to use standard POSIX-like I/O functions for accessing I/O devices.
- Both VXWORKS and FREE RTOS support synchronous and asynchronous I/O systems, as well as polling and interrupt-driven modes.   
- However, the choice of the I/O system type and mode depends on the requirements and constraints of the embedded system, such as performance, reliability, safety, security, power consumption, memory usage, etc.



# General Architecture for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that are used for embedded systems and real-time applications.
- RTOS are designed to meet the performance requirements and timing constraints of time-sensitive systems, such as industrial control, robotics, aerospace, and defense.
- RTOS differ from general purpose operating systems (GPOS) in terms of scheduling, kernel, and priority inversion handling.
- The general architecture of VXWORKS and FREE RTOS can be compared as follows:

## Scheduling
- Scheduling is the process of allocating CPU time to tasks based on their priority and deadlines.
- VXWORKS supports preemptive priority-based scheduling, which means that a higher priority task can interrupt a lower priority task at any time.
- VXWORKS also supports round-robin scheduling, which means that tasks with the same priority are executed in a circular order for a fixed time slice.
- FREE RTOS supports preemptive priority-based scheduling as well, but it also allows the user to configure the scheduler as cooperative, which means that tasks can voluntarily yield the CPU to other tasks.
- FREE RTOS does not support round-robin scheduling, but it provides a mechanism called time slicing, which allows tasks with the same priority to share the CPU time equally.

## Kernel
- Kernel is the core component of an operating system that manages the system resources, such as memory, devices, and interrupts.
- VXWORKS has a monolithic kernel, which means that all the kernel functions are executed in the same address space and memory protection domain.
- VXWORKS kernel is modular, which means that the user can select the components and features that are needed for the application and exclude the rest.
- VXWORKS kernel is also scalable, which means that it can run on different hardware platforms and architectures, such as x86, ARM, PowerPC, and MIPS.
- FREE RTOS has a microkernel, which means that the kernel functions are executed in separate address spaces and memory protection domains.
- FREE RTOS kernel is minimal, which means that it only provides the basic functionality of task management, synchronization, and communication.
- FREE RTOS kernel is also portable, which means that it can run on various microcontrollers and processors, such as AVR, PIC, MSP430, and Cortex-M.

## Priority Inversion
- Priority inversion is a situation where a lower priority task holds a resource that is needed by a higher priority task, causing the higher priority task to be blocked and the lower priority task to be executed instead.
- VXWORKS handles priority inversion by using a mechanism called priority inheritance, which means that the lower priority task inherits the priority of the highest priority task that is waiting for the resource, and releases the resource as soon as possible.
- VXWORKS also provides an option to use priority ceiling, which means that the priority of the task that acquires the resource is raised to the highest priority level of any task that may use the resource, and lowered to its original level when the resource is released.
- FREE RTOS handles priority inversion by using a mechanism called priority inheritance as well, but it also allows the user to disable this feature if it is not needed or desired.
- FREE RTOS does not support priority ceiling, but it provides a mechanism called mutexes, which are mutual exclusion locks that can be used to protect critical sections of code from concurrent access by multiple tasks.



### Device Driver Studies for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A device driver is a software component that allows an operating system to communicate with a hardware device.
- A device driver typically implements a standard interface, such as POSIX, to provide access to the device's features and functionality.
- A device driver may also perform tasks such as initialization, configuration, error handling, and interrupt handling for the device.
- A device driver may be written in C, C++, or assembly language, depending on the requirements and constraints of the device and the operating system.
- A device driver may be static or dynamic, meaning that it may be linked with the operating system kernel at compile time or loaded at run time, respectively.
- A device driver may be specific to a particular device model, or generic to a class of devices that share a common interface or protocol.

- VXWORKS is a real-time operating system (RTOS) developed by Wind River Systems for embedded systems and devices.
- VXWORKS is a deterministic, priority-based preemptive RTOS with low latency and minimal jitter.
- VXWORKS is built on an upgradable, future-proof architecture to help you rapidly respond to changing market requirements and technology advancements.
- VXWORKS supports a variety of hardware platforms, such as ARM, Intel, PowerPC, and MIPS, and provides board support packages (BSPs) for many popular devices and boards .
- VXWORKS provides a standard device driver interface that is compatible with the POSIX standard and allows you to access devices using open(), read(), write(), ioctl(), and close() functions.
- VXWORKS also provides a device driver development kit (DDK) that helps you create, debug, and test your own device drivers for VXWORKS.

- FREE RTOS is an open source RTOS for embedded systems and devices.
- FREE RTOS is a lightweight, portable, and scalable RTOS that supports multiple architectures, such as ARM, AVR, PIC, and x86.
- FREE RTOS provides a simple and intuitive API for creating tasks, queues, semaphores, timers, and other RTOS primitives.
- FREE RTOS also provides optional extensions, such as FreeRTOS-Plus-IO, that provide a Linux/POSIX like interface to peripheral driver libraries.
- FreeRTOS-Plus-IO sits between a peripheral driver library and a user application to provide a single, common, interface to all supported peripherals across all supported platforms.
- FreeRTOS-Plus-IO allows you to access devices using open(), read(), write(), ioctl(), and close() functions, similar to VXWORKS.



### Driver Module explanation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A driver module is a software component that interacts with a specific hardware device or peripheral, such as a keyboard, mouse, printer, network card, etc.
- A driver module provides a uniform interface to the device, hiding the details of the hardware implementation and protocol from the application layer.
- A driver module typically consists of two parts: a device driver and a device controller.
- A device driver is the part of the driver module that communicates with the operating system kernel, such as VxWorks or FreeRTOS, and handles requests from user applications or system services.
- A device controller is the part of the driver module that communicates with the hardware device directly, using the device-specific registers, commands, and interrupts.
- A driver module can be implemented in different ways, depending on the operating system, the hardware device, and the design requirements.
- Some common driver module implementation methods are:
  - Polling: The device driver periodically checks the status of the device controller and the hardware device, and performs the necessary actions based on the status. This method is simple but inefficient, as it consumes CPU cycles and may miss some events.
  - Interrupt: The device controller generates an interrupt signal when an event occurs, such as data ready, error, or completion. The device driver registers an interrupt handler with the operating system kernel, which is invoked when the interrupt signal is received. This method is efficient but complex, as it requires synchronization and concurrency control between the interrupt handler and the device driver.
  - DMA: The device controller uses direct memory access (DMA) to transfer data between the hardware device and the system memory, without involving the CPU. The device driver sets up the DMA parameters and monitors the DMA completion status. This method is fast and scalable, as it reduces the CPU overhead and allows parallel data transfers.
- VxWorks and FreeRTOS are two examples of real-time operating systems (RTOS) that support driver modules for various hardware devices and peripherals.
- VxWorks is a commercial RTOS that offers a rich set of features and services, such as networking, security, file system, graphics, etc. VxWorks provides a standard device driver interface (DDI) that defines the common functions and data structures for driver modules. VxWorks also provides a board support package (BSP) framework that facilitates the porting of driver modules to different hardware platforms .
- FreeRTOS is an open source RTOS that focuses on simplicity and portability, with minimal memory footprint and low overhead. FreeRTOS does not provide a standard device driver interface, but rather relies on the peripheral driver libraries provided by the hardware vendors or the developers. FreeRTOS also provides a POSIX-like extension called FreeRTOS Plus IO, which offers a common interface to driver modules based on the open (), read (), write (), and ioctl () functions.



### Implementation of Device Driver for a Peripheral

- A device driver is a software application that allows a hardware device (such as a printer or a keyboard) to interact with the operating system (such as Windows or Linux) of a computer system.
- A device driver acts as a translator between the operating system and the peripheral device, and communicates with the device through the computer bus (such as PCI or USB) that connects the device with the computer .
- A device driver consists of a physical structure of modes that will make up the process of allowing the operating system to control the peripheral device.
- The steps for implementing a device driver for a peripheral are as follows:
  - Identify the type of peripheral device and the bus that connects it to the computer system.
  - Choose a programming language and a development environment that are compatible with the operating system and the device specifications.
  - Write the code for the device driver, following the guidelines and standards of the operating system and the device manufacturer.
  - Compile and debug the code, and test the device driver on a simulated or real device.
  - Package and distribute the device driver, and provide documentation and support for the users.
- The types of device drivers and their applications are as follows:
  - Kernel-mode device drivers: These drivers run in the kernel space of the operating system, and have direct access to the hardware and the system resources. They are faster and more efficient, but also more complex and risky. They are used for critical devices such as disk drives, network adapters, or graphics cards.
  - User-mode device drivers: These drivers run in the user space of the operating system, and communicate with the hardware through the kernel-mode device drivers. They are simpler and safer, but also slower and less flexible. They are used for non-critical devices such as mice, keyboards, or printers.
  - Virtual device drivers: These drivers emulate the behavior of a hardware device in software, and provide a virtual interface for the operating system and the applications. They are used for devices that are not physically present, such as virtual disks, virtual printers, or virtual network adapters.
  - Plug and play device drivers: These drivers are able to detect and configure the hardware device automatically, without requiring user intervention or manual installation. They are used for devices that are connected or disconnected frequently, such as USB devices, Bluetooth devices, or cameras.
  - Power management device drivers: These drivers are able to control the power consumption and the performance of the hardware device, depending on the system state and the user preferences. They are used for devices that are battery-powered, such as laptops, tablets, or smartphones.

