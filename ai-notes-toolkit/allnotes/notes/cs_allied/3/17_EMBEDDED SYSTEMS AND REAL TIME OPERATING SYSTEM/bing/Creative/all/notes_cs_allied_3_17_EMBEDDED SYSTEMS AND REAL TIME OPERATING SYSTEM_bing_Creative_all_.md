

# EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded system is a computer system that is designed to perform a specific function within a larger system or device. It typically has limited hardware resources, such as memory, processing power, and input/output devices. It often runs on a microcontroller or a microprocessor that is integrated with the hardware components of the system. 
- A real-time operating system (RTOS) is a type of operating system that is specialized for embedded systems that operate in real-time environments. A real-time environment is one where the system must respond to events or inputs within a predictable and bounded time limit, otherwise it may cause failure or damage.  
- Some examples of real-time embedded systems are:
  - Medical devices, such as pacemakers, ventilators, and infusion pumps.
  - Industrial control systems, such as robots, CNC machines, and PLCs.
  - Automotive systems, such as engine control, anti-lock braking, and airbag deployment.
  - Aerospace systems, such as flight control, navigation, and communication.
  - Consumer electronics, such as digital cameras, video games, and smart watches.  
- Some features of a real-time operating system are:
  - Task scheduling: An RTOS must be able to manage multiple tasks or processes that run concurrently on the system, and assign them priorities and deadlines based on their importance and urgency. An RTOS must also be able to switch between tasks efficiently and without causing delays or errors.  
  - Interrupt handling: An RTOS must be able to handle external or internal interrupts that occur during the execution of a task, and resume the task after servicing the interrupt. An interrupt is a signal that indicates an event or a change of state that requires immediate attention. An RTOS must also be able to prioritize interrupts and avoid interrupt latency or starvation.  
  - Memory management: An RTOS must be able to allocate and deallocate memory for tasks and data, and ensure that the memory is used efficiently and securely. An RTOS must also be able to handle memory fragmentation and garbage collection.  
  - Inter-task communication and synchronization: An RTOS must be able to facilitate the exchange of data and signals between tasks, and coordinate their execution and access to shared resources. An RTOS must also be able to prevent or resolve conflicts and deadlocks that may arise due to concurrency and resource contention.  
  - Device drivers and hardware abstraction: An RTOS must be able to interface with the hardware components of the embedded system, such as sensors, actuators, and communication modules, and provide a uniform and consistent way of accessing them. An RTOS must also be able to abstract the hardware details and provide a higher-level view of the system functionality.  
- Some examples of real-time operating systems are:
  - FreeRTOS: An open-source RTOS that is widely used for embedded systems. It supports various architectures, such as ARM, AVR, PIC, and x86. It provides basic features, such as task scheduling, interrupt handling, memory management, and inter-task communication. It also supports advanced features, such as event groups, queues, semaphores, mutexes, and software timers. 
  - VxWorks: A commercial RTOS that is widely used for embedded systems. It supports various architectures, such as ARM, MIPS, PowerPC, and x86. It provides basic features, such as task scheduling, interrupt handling, memory management, and inter-task communication. It also supports advanced features, such as file systems, networking, security, graphics, and multimedia. 
  - Linux: A general-purpose operating system that can be configured and customized for embedded systems. It supports various architectures, such as ARM, MIPS, PowerPC, and x86. It provides basic features, such as task scheduling, interrupt handling, memory management, and inter-task communication. It also supports advanced features, such as file systems, networking, security, graphics, and multimedia. It also supports various real-time extensions, such as PREEMPT_RT and Xenomai.



## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system (OS) is a specialized software that runs on a dedicated hardware device and provides a platform for running applications.
- Embedded OSes are designed to meet the specific requirements of the device, such as performance, reliability, security, power efficiency, and memory footprint.
- Embedded OSes can be classified into two categories: real-time and non-real-time.
  - A real-time OS (RTOS) is an embedded OS that guarantees to respond to events or tasks within a predefined time limit, regardless of the system load. RTOSes are suitable for time-critical applications, such as industrial control, robotics, and avionics.
  - A non-real-time OS (NRTOS) is an embedded OS that does not provide any timing guarantees, but offers more functionality and flexibility than an RTOS. NRTOSes are suitable for general-purpose applications, such as multimedia, networking, and user interfaces.
- Embedded OSes can be further classified into two types: monolithic and modular.
  - A monolithic OS is an embedded OS that consists of a single executable image that contains the kernel and all the drivers, libraries, and applications. Monolithic OSes are simple, fast, and compact, but difficult to maintain, debug, and update.
  - A modular OS is an embedded OS that consists of multiple components that can be loaded and unloaded dynamically. Modular OSes are more flexible, scalable, and secure, but require more memory and processing overhead.
- Embedded OSes have some common components, such as:
  - The kernel, which is the core of the OS that manages the hardware resources, such as CPU, memory, and I/O devices, and provides basic services, such as task scheduling, interrupt handling, and memory management.
  - The drivers, which are software modules that communicate with the hardware devices and abstract their functionality for the applications.
  - The libraries, which are collections of reusable functions that provide common functionality, such as math, string, and network operations.
  - The applications, which are software programs that perform specific tasks for the user or the device, such as user interface, data processing, and communication.
- Embedded OSes have some unique challenges, such as:
  - Limited hardware resources, such as CPU, memory, and power, which require the OS to be optimized for performance and efficiency.
  - Diverse hardware platforms, such as microcontrollers, microprocessors, and system-on-chips, which require the OS to be portable and adaptable.
  - High reliability and security requirements, which require the OS to be robust and resilient against errors and attacks.
  - Long life cycle and maintenance, which require the OS to be stable and compatible with future updates and changes.



# Linux internals for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Embedded Linux is a type of Linux kernel that is specially designed for embedded devices, such as smartphones, set-top boxes, smart TVs, routers, etc. 
- Embedded Linux is built on the same Linux kernel, available from kernel.org, as all Linux systems, but it has some modifications and adaptations to meet the specific requirements and constraints of embedded systems, such as higher reliability, security, performance, resource availability, and long-term support.
- The main components of an embedded Linux system are:
  - Toolchain: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, which are used to create source code for the target embedded hardware.
  - Bootloader: A piece of code that runs when we apply power to the embedded hardware first time. It initializes the hardware, loads the Linux kernel into memory, and passes some parameters to the kernel.
  - Linux Kernel: The core of the Linux system, which manages the hardware resources, such as CPU, memory, I/O devices, etc. It also provides system services, such as process management, file system, networking, etc.
  - Device Tree: A data structure that describes the hardware configuration and properties of the embedded system. It is used by the Linux kernel to initialize and communicate with the devices.
  - Root File System: A collection of files and directories that contain the user applications, libraries, configuration files, and other data that are needed for the Linux system to run. It can be stored in different types of media, such as flash memory, SD card, hard disk, etc.
  - Configuration Files: Files that store the settings and preferences of the Linux system and the user applications. They can be edited to customize the behavior and appearance of the system.



# Process Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Process management is how the OS manages and views other software in the embedded system (via processes)  .
- A process is a unit of execution that has its own state, memory, and resources .
- A process can be in one of the following states: ready, running, blocked, or terminated .
- A process can communicate with other processes via interprocess communication (IPC) mechanisms, such as message passing, shared memory, pipes, signals, or semaphores .
- A process can synchronize with other processes via mutual exclusion, critical sections, locks, or monitors .
- A process can be created, suspended, resumed, or killed by the OS or by other processes .
- A process can be scheduled by the OS according to different policies, such as priority-based, round-robin, or preemptive .
- A process can be assigned to different levels of privilege, such as user mode or kernel mode .
- A process can be classified into different types, such as foreground, background, daemon, or real-time .
- A process can be implemented by different techniques, such as threads, tasks, or coroutines .
- A process can be supported by different architectures, such as uniprocessor, multiprocessor, or distributed .
- A process can be affected by different challenges, such as concurrency, deadlock, starvation, or race conditions .
- A process can be optimized by different methods, such as caching, paging, or memory management .
- A process can be tested by different tools, such as debuggers, profilers, or simulators .



# File Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- File management is the process of manipulating files in a computer system, such as creating, modifying, deleting, storing, and retrieving files.
- Files are collections of data that are stored on a device or a storage system, such as Flash, RAM, or hard disk.
- File systems are the schemes that organize files into folders and provide an interface for users to access their files.
- Embedded systems are devices that have a dedicated function and run on a limited hardware and software platform.
- Embedded operating systems are specialized OSs that provide services and features for embedded systems, such as memory management, task scheduling, interrupt handling, and I/O management.
- File management in embedded systems is a challenging task because of the constraints and requirements of embedded systems, such as:
  - Limited memory and storage space
  - High reliability and data integrity
  - Real-time performance and responsiveness
  - Certifiability and compliance with standards
  - Compatibility with various hardware and software components
- Some embedded OSs provide file management support for a temporary or permanent file system storage scheme on various memory devices.
- Some examples of file systems and data storage management products for embedded systems are:
  - FAT (File Allocation Table): a simple and widely used file system that supports various storage devices and platforms, but has limitations in performance, reliability, and security.
  - Tuxera Reliance Edge: a transactional file system that is designed for applications where certifiability, fail safety, and data integrity are paramount, and works with a majority of safety-critical RTOSes.
  - Tuxera FlashFX Tera: a flash memory manager that handles the complexities of NAND and NOR flash devices, such as wear leveling, bad block management, and error correction.



# Memory Management

Memory management is the process of allocating and deallocating memory resources to programs and processes in an efficient and effective way. Memory management is essential for embedded systems, which have limited and constrained memory resources. Memory management can affect the performance, reliability, and functionality of embedded systems.

Some of the topics related to memory management in embedded systems are:

- **Memory types**: Embedded systems typically use different types of memory, such as static random access memory (SRAM), dynamic random access memory (DRAM), read-only memory (ROM), flash memory, etc. Each type of memory has its own characteristics, such as speed, cost, size, volatility, etc. Embedded systems need to choose the appropriate memory type for their specific requirements and constraints.
- **Memory pools**: Memory pools are a technique of managing dynamic memory allocation in embedded systems. Memory pools allocate a fixed number of fixed-sized blocks of memory that can be used by the application. Memory pools can reduce memory fragmentation, overhead, and complexity, and improve memory utilization and performance.
- **Memory mapping**: Memory mapping is a technique of mapping a logical address space to a physical address space. Memory mapping can enable a program to use a large virtual address space that exceeds the physical memory size. Memory mapping can also provide memory protection, isolation, and sharing among different processes.
- **Memory management unit (MMU)**: MMU is a hardware component that performs memory mapping and memory protection. MMU can translate logical addresses to physical addresses, check the validity and permissions of memory accesses, and generate exceptions or faults when memory violations occur. MMU can support features such as paging, segmentation, virtual memory, etc.
- **Memory management in operating systems**: Operating systems can provide memory management services to the applications and processes running on the embedded system. Operating systems can manage the memory allocation and deallocation, memory protection and isolation, memory sharing and communication, memory swapping and caching, etc. Operating systems can use different memory management schemes, such as fixed partitioning, variable partitioning, buddy system, etc.

: https://thesynchronousblog.wordpress.com/2013/05/20/dynamic-memory-management-in-embedded-systems/

: https://www.sciencedirect.com/topics/computer-science/memory-management

: https://www.edn.com/embedded-operating-systems-part-4-memory-management/

: https://www.qt.io/embedded-development-talk/memory-options-for-embedded-systems-how-to-select-the-right-memory-configuration

: https://www.embedded.com/using-a-memory-management-unit/



# I/O Management for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- I/O management is the process of controlling the input and output devices of an embedded system, such as sensors, actuators, keyboards, displays, network interfaces, etc.
- I/O management in embedded OSs provides an additional abstraction layer (to higher-level software) away from the system’s hardware and device drivers.
- I/O management in embedded OSs can be divided into two main components: device drivers and file systems.
- Device drivers are software modules that interact with the hardware devices and provide a uniform interface to the OS kernel and the user applications.
- File systems are software modules that organize the data stored on the memory devices (such as flash, RAM, ROM, etc.) and provide a logical view of the data to the user applications.
- Most OSs use their standard I/O interface between the file system and the memory device drivers. This allows for one or more file systems to operate in conjunction with the OS.
- In order to manage I/O, an OS may require all device driver code to contain a specific set of functions, such as startup, shutdown, enable, and disable. A kernel then manages I/O devices, and in some OSs file systems as well, as “black boxes” that are accessed by some set of generic APIs by higher-layer processes.
- I/O management in embedded OSs can be classified into two types: synchronous and asynchronous.
- Synchronous I/O is when the OS or the user application waits for the completion of an I/O operation before proceeding to the next instruction. This can simplify the programming logic, but can also cause blocking and performance degradation.
- Asynchronous I/O is when the OS or the user application initiates an I/O operation and then continues to execute other instructions without waiting for the completion of the I/O operation. This can improve the performance and responsiveness of the system, but can also introduce complexity and concurrency issues.
- I/O management in embedded OSs can also be classified into two modes: polling and interrupt-driven.
- Polling is when the OS or the user application periodically checks the status of an I/O device to determine if it is ready for data transfer. This can be simple and deterministic, but can also waste CPU cycles and cause latency.
- Interrupt-driven is when the OS or the user application relies on the hardware device to generate an interrupt signal when it is ready for data transfer. This can save CPU cycles and reduce latency, but can also introduce overhead and unpredictability.



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



# Threads - Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread is also known as a lightweight process that shares the same memory and resources as the program that created it.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the program (user-level threads).
- The advantages of using threads are:
  - Improved performance and responsiveness of the program
  - Better utilization of the CPU and other resources
  - Easier communication and synchronization among threads
  - Simplified program structure and modularity
- The challenges of using threads are:
  - Ensuring the re-entrancy and thread-safety of the code
  - Avoiding race conditions and deadlocks among threads
  - Managing the overhead and complexity of thread creation and switching
  - Choosing the appropriate thread model and library for the target platform
- In embedded systems, threads are often used to handle multiple tasks or events that require concurrent or parallel execution.
- Embedded systems may use no OS, RTOS, or general-purpose OS, depending on the requirements and constraints of the system.
- The thread model and library may vary depending on the OS and the programming language used for the embedded system.
- Some examples of thread models and libraries are:
  - POSIX threads (pthreads) - a standard API for creating and manipulating threads in C and C++ programs
  - Java threads - a built-in feature of the Java language that allows creating and managing threads as subclasses of the Thread class
  - Qt threads - a cross-platform framework for creating and managing threads as subclasses of the QThread class in C++ programs
  - FreeRTOS threads - a lightweight and portable API for creating and manipulating threads (also called tasks) in embedded systems using the FreeRTOS kernel
- The general steps for creating a thread are:
  - Define the function or method that the thread will execute
  - Create an instance of the thread object or structure and pass the function or method as a parameter
  - Start the thread by calling a specific function or method of the thread object or structure
  - Optionally, join or detach the thread to synchronize or terminate its execution
- The syntax and details of creating a thread may differ depending on the thread model and library used.



# Cancellation for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Cancellation is a technique to terminate a thread before it completes its execution.
- Cancellation can be useful to free up resources, handle errors, or respond to user requests.
- Cancellation can be initiated by another thread or by the thread itself.
- Cancellation can be either asynchronous or deferred.
  - Asynchronous cancellation means that the thread can be terminated at any point in its execution.
  - Deferred cancellation means that the thread can only be terminated at certain points, called cancellation points, where it checks for cancellation requests.
- Cancellation can be either enabled or disabled by the thread.
  - Enabled cancellation means that the thread can be cancelled if a cancellation request is received.
  - Disabled cancellation means that the thread ignores any cancellation requests and continues its execution.
- Cancellation can have different types of cleanup actions, depending on how the thread is terminated.
  - If the thread is terminated by a return statement, it can perform normal cleanup actions, such as closing files, releasing locks, or freeing memory.
  - If the thread is terminated by a cancellation request, it can perform additional cleanup actions, such as notifying other threads, restoring the state of the system, or logging the event.
  - The thread can register one or more cleanup handlers, which are functions that are executed when the thread is cancelled.
  - The thread can also use cancellation cleanup push and pop macros, which are used to manage a stack of cleanup handlers.
- Cancellation can have different effects on the thread's exit status and joinability.
  - If the thread is terminated by a return statement, it returns a value that can be obtained by another thread using the pthread_join function.
  - If the thread is terminated by a cancellation request, it returns a special value, PTHREAD_CANCELED, that indicates that the thread was cancelled.
  - The thread can also use the pthread_exit function to terminate itself and return a value.
  - The thread can also use the pthread_detach function to make itself unjoinable, meaning that its resources are automatically released when it terminates and no other thread can obtain its exit status.



# POSIX Threads

- POSIX Threads, or pthreads, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- POSIX Threads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same address space, file descriptors, stack, and other attributes, but have their own **thread ID**, **registers**, **stack pointer**, **priority**, and **return value**.
- Threads can communicate with each other using **shared memory**, **mutexes**, **condition variables**, and **semaphores** .
- Threads can be created, joined, detached, canceled, and synchronized using the functions provided by the pthreads API .
- The pthreads API consists of **functions**, **header files**, and **data types**.
- The functions have names that start with **pthread_**, such as `pthread_create`, `pthread_join`, `pthread_mutex_lock`, etc .
- The header files include **pthread.h**, which defines the functions, constants, and types for pthreads, and **sched.h**, which defines the scheduling policies and parameters.
- The data types include **pthread_t**, which represents a thread ID, **pthread_attr_t**, which represents a thread attribute object, **pthread_mutex_t**, which represents a mutex, **pthread_cond_t**, which represents a condition variable, and **pthread_key_t**, which represents a thread-specific data key .
- The pthreads API supports various features, such as **thread attributes**, **thread cancellation**, **thread cleanup**, **thread local storage**, **thread scheduling**, **thread signals**, and **thread synchronization** .
- The pthreads API is widely supported by various operating systems, such as **Linux**, **macOS**, **Windows**, and **RTOS**  .



# Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions.
- Processes can communicate with each other through both shared memory and message passing.
- Semaphores are counters which allow multiple threads or processes to synchronize by allocating or releasing resources .
- Semaphores can be either binary (0 or 1) or counting (any non-negative integer).
- Semaphores can be implemented in two ways: synchronization semaphores and process semaphores.
- Synchronization semaphores are used to coordinate the access of shared resources among threads within a single process.
- Process semaphores or system V semaphores are used to coordinate the access of shared resources among processes.
- Process semaphores are created and managed by the operating system.
- To perform synchronization using process semaphores, the following steps are required:
  - Create a semaphore or connect to an already existing semaphore using `semget()` system call.
  - Perform operations on the semaphore such as allocate, release, or wait for the resources using `semop()` system call.
  - Perform control operations on the semaphore such as set or get its value, permissions, or status using `semctl()` system call.
- Process semaphores can be used to implement mutual exclusion, producer-consumer, and reader-writer problems.



# Pipes

Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner. Pipes are often used in embedded systems to pass simple messages between tasks or commands. Pipes have the following characteristics and advantages:

- Pipes are unidirectional, meaning that data can only flow from one end (the writer) to the other end (the reader) of the pipe.
- Pipes are buffered, meaning that data can be stored temporarily in the pipe until the reader is ready to receive it. This can prevent data loss or blocking of the writer.
- Pipes are anonymous, meaning that they do not have a name or an identifier in the file system. They are created and accessed by using file descriptors that are returned by the system call `pipe`.
- Pipes are simple and efficient, meaning that they do not require complex protocols or synchronization mechanisms to operate. They are also fast and reliable, as they use kernel memory and avoid context switches.

Some of the basic services that pipes provide are:

- Creating a pipe: The system call `pipe` creates a new pipe and returns two file descriptors, one for reading and one for writing. The syntax is `int pipe(int fd[2])`, where `fd[0]` is the read end and `fd[1]` is the write end of the pipe. The function returns 0 on success and -1 on error.
- Writing to a pipe: The system call `write` can be used to write data to the write end of the pipe. The syntax is `ssize_t write(int fd, const void *buf, size_t count)`, where `fd` is the file descriptor of the write end of the pipe, `buf` is the pointer to the data buffer, and `count` is the number of bytes to write. The function returns the number of bytes written on success and -1 on error.
- Reading from a pipe: The system call `read` can be used to read data from the read end of the pipe. The syntax is `ssize_t read(int fd, void *buf, size_t count)`, where `fd` is the file descriptor of the read end of the pipe, `buf` is the pointer to the data buffer, and `count` is the number of bytes to read. The function returns the number of bytes read on success and -1 on error.
- Closing a pipe: The system call `close` can be used to close a file descriptor of a pipe. The syntax is `int close(int fd)`, where `fd` is the file descriptor of either the read or the write end of the pipe. The function returns 0 on success and -1 on error. Closing the write end of the pipe causes the reader to receive an end-of-file (EOF) signal. Closing the read end of the pipe causes the writer to receive a broken pipe (SIGPIPE) signal.

Some of the limitations and challenges of pipes are:

- Pipes are not bidirectional, meaning that data cannot flow in both directions simultaneously. To achieve bidirectional communication, two pipes are needed, one for each direction.
- Pipes are not persistent, meaning that they are destroyed when the processes that use them terminate. To create a persistent pipe, a named pipe or a FIFO can be used, which is a special file that can be accessed by multiple processes using a name in the file system.
- Pipes are not scalable, meaning that they can only connect two processes at a time. To connect more than two processes, a more complex IPC method such as sockets or message queues can be used, which allow multiple processes to communicate over a network or a shared memory.



# FIFO for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- FIFO stands for First In First Out, which means that the data that is inserted first will be extracted first.
- FIFOs are commonly used in embedded systems for buffering and flow control between hardware and software.
- FIFOs can be implemented in hardware or software, depending on the application requirements.
- Hardware FIFOs are usually built of registers, flip-flops, latches or SRAM, and have read and write pointers, storage and control logic .
- Hardware FIFOs can be exclusive read/write or concurrent read/write, depending on whether the reading and writing operations can occur simultaneously or not.
- Hardware FIFOs can reduce the power consumption, data loss and latency of the system by allowing the host MCU to interact with the sensor less frequently.
- Software FIFOs are usually implemented as circular buffers or queues, and have head and tail pointers, storage and control variables.
- Software FIFOs can be accessed by interrupts or polling, depending on the system design.
- Software FIFOs can provide flexibility, portability and scalability to the system, but may also introduce overhead, complexity and errors.



# Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it does not involve copying data or system calls.
- Shared memory can be implemented in different ways, such as:

  - **System V shared memory**: a POSIX-compliant API that creates and attaches segments of memory identified by keys.
  - **POSIX shared memory**: a newer API that creates and maps named or anonymous objects of memory in the file system.
  - **Memory-mapped files**: a technique that maps a file or a device into the virtual address space of a process, allowing direct access to the file contents as if they were in memory.
  - **Anonymous memory mapping**: a variation of memory-mapped files that does not use a file or a device, but allocates a region of memory that can be shared by multiple processes.

- Shared memory can also be classified into two types, depending on the scope of sharing:

  - **Local shared memory**: a region of memory that is shared by processes running on the same processor or the same multicore processor. Local shared memory can be accessed directly by the processes without any special hardware or software support.
  - **Distributed shared memory**: a region of memory that is shared by processes running on different processors or different multicore processors. Distributed shared memory requires special hardware or software mechanisms to ensure consistency and coherence of the shared data across the processors.

- Shared memory is widely used in embedded systems and real-time operating systems (RTOS) for various purposes, such as:

  - **Data exchange**: processes can share data structures, variables, or buffers through shared memory, avoiding the overhead of serialization and deserialization.
  - **Synchronization**: processes can use shared memory to implement mutual exclusion, semaphores, condition variables, or barriers, ensuring the correct order and timing of operations.
  - **Coordination**: processes can use shared memory to implement distributed algorithms, such as consensus, leader election, or distributed locking, achieving agreement and cooperation among processes.
  - **Performance**: processes can use shared memory to exploit parallelism, load balancing, or caching, improving the efficiency and scalability of the system.



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



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of Embedded OS Internals. Here is a possible structure for the notes of Unit 1:

# Unit 1 - Embedded OS Internals

## Introduction
- Define what is an embedded system and an embedded OS
- Explain the characteristics and challenges of embedded systems
- List some examples of embedded systems and their applications
- Compare and contrast embedded OS with general-purpose OS

## Embedded OS Architecture
- Describe the components and layers of an embedded OS
- Explain the functions and services of each component and layer
- Discuss the design trade-offs and criteria for choosing an embedded OS
- Compare and contrast different types of embedded OS, such as monolithic, microkernel, exokernel, etc.

## Embedded OS Components
- Explain the role and implementation of the following components in an embedded OS:
  - Bootloader
  - Kernel
  - Device drivers
  - File system
  - Network stack
  - User interface
  - Application programming interface (API)
- Discuss the advantages and disadvantages of each component
- Compare and contrast different implementations of each component, such as U-Boot, Linux, RTOS, FAT, TCP/IP, etc.

## Embedded OS Services
- Explain the role and implementation of the following services in an embedded OS:
  - Process management
  - Memory management
  - Inter-process communication (IPC)
  - Input/output (I/O) management
  - Interrupt handling
  - Scheduling
  - Power management
  - Security
- Discuss the challenges and requirements of each service in embedded systems
- Compare and contrast different algorithms and techniques for each service, such as priority-based, preemptive, round-robin, etc.

## Embedded OS Development
- Describe the steps and tools involved in developing an embedded OS
- Explain the concepts and methods of cross-compilation, debugging, testing, and deployment
- Discuss the best practices and standards for embedded OS development
- Compare and contrast different development environments and platforms, such as Eclipse, GNU, ARM, etc.



# Kernel Module Programming

Kernel module programming is a way of extending the functionality of the Linux kernel without modifying the source code or recompiling the kernel. Kernel modules are object files that contain code that can be loaded into or unloaded from the kernel at runtime. Kernel modules are typically used to implement device drivers, file systems, network protocols, and other features that are not part of the core kernel.

Some of the advantages of kernel module programming are:

- It allows the kernel to be customized according to the needs and preferences of the user or the system administrator.
- It reduces the size and complexity of the kernel, making it more stable and secure.
- It enables the kernel to support new hardware or software without requiring a reboot or a reinstallation.
- It facilitates the development and testing of new kernel features or enhancements.

Some of the challenges of kernel module programming are:

- It requires a good understanding of the kernel internals, such as data structures, algorithms, synchronization mechanisms, and interfaces.
- It must follow the coding standards and conventions of the kernel community, such as indentation, naming, commenting, and error handling.
- It must be compatible with the kernel version and configuration that it is intended to run on, as well as with other kernel modules that may interact with it.
- It must be careful not to introduce bugs, memory leaks, or security vulnerabilities into the kernel.

The basic steps of kernel module programming are:

- Write the source code of the kernel module in C, using the kernel headers and libraries.
- Compile the source code into an object file, using the kernel Makefile and the appropriate flags and options.
- Load the kernel module into the kernel, using the `insmod` command or the `modprobe` utility.
- Test the functionality and performance of the kernel module, using the appropriate tools and methods.
- Unload the kernel module from the kernel, using the `rmmod` command or the `modprobe` utility.
- Debug and fix any errors or issues that may arise, using the kernel log, the `dmesg` command, the `printk` function, or the `kdb` or `kgdb` debuggers.

A kernel module must have at least two functions: an initialization function and a cleanup function. The initialization function is called when the kernel module is loaded, and it is responsible for registering the module with the kernel, allocating any resources, and performing any initialization tasks. The cleanup function is called when the kernel module is unloaded, and it is responsible for deregistering the module from the kernel, freeing any resources, and performing any cleanup tasks. The initialization function and the cleanup function are usually named `init_module` and `cleanup_module`, respectively, or they can be specified using the `module_init` and `module_exit` macros.

A kernel module can also have other functions, variables, macros, and structures, depending on its purpose and functionality. A kernel module can communicate with the user space, the kernel space, or other kernel modules, using various mechanisms, such as system calls, ioctl, procfs, sysfs, netlink, or device files. A kernel module can also use some of the kernel services, such as memory management, scheduling, interrupt handling, locking, timers, or work queues.

A kernel module must follow some rules and guidelines, such as:

- It must include the `<linux/module.h>` header file, which defines the module-related macros and functions.
- It must declare the module license, author, description, and version, using the `MODULE_LICENSE`, `MODULE_AUTHOR`, `MODULE_DESCRIPTION`, and `MODULE_VERSION` macros, respectively.
- It must check the return values of the kernel functions and handle any errors or failures gracefully.
- It must avoid using floating-point operations, as they are not supported by the kernel.
- It must avoid using any user space libraries or functions, as they are not available in the kernel space.
- It must avoid using any global variables or static variables, as they may cause conflicts or inconsistencies with other kernel modules or the kernel itself.
- It must avoid using any blocking or sleeping functions, as they may cause deadlocks or performance degradation in the kernel.
- It must avoid using any non-reentrant or non-thread-safe functions, as they may cause race conditions or data corruption in the kernel.



# Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Schedulers are the core functionality of a kernel that allocate processor time among tasks in a multitasking embedded system.
- Schedulers can create the illusion that all the tasks are running concurrently by switching between them rapidly.
- Schedulers can also ensure that tasks can meet deadlines in real-time environments, which is crucial for keeping the system stable.
- Schedulers can be classified into different types based on the criteria and policies they use to select the next task to run.
- Some common types of schedulers are:

  - **Time Slice (TS) Scheduler**: A TS scheduler divides time into slots, with each task being allowed to execute for the duration of its slot. The tasks are arranged in a circular queue and the scheduler cycles through them in a round-robin fashion. A TS scheduler is simple and fair, but it does not consider the priority or the deadline of the tasks.
  - **Priority Scheduler**: A priority scheduler assigns a priority level to each task and selects the task with the highest priority to run. The priority can be static (fixed at design time) or dynamic (adjusted at run time). A priority scheduler can handle tasks with different importance and urgency, but it may suffer from priority inversion or starvation problems.
  - **Composite Scheduler**: A composite scheduler combines two or more scheduling policies to achieve a balance between performance and flexibility. For example, a composite scheduler may use a priority scheduler for real-time tasks and a TS scheduler for non-real-time tasks. A composite scheduler can handle complex and heterogeneous systems, but it may increase the overhead and complexity of the kernel.
- Schedulers can also be classified into two approaches based on the way they handle task switching: non-preemptive and preemptive scheduling.
  - **Non-preemptive scheduling**: Under non-preemptive scheduling, tasks are given control of the master CPU until they have finished execution, regardless of the length of time or the importance of the other tasks that are waiting. Non-preemptive scheduling is simple and predictable, but it may cause long delays and missed deadlines for high-priority tasks.
  - **Preemptive scheduling**: Under preemptive scheduling, tasks can be interrupted and suspended by the scheduler at any time to give way to higher-priority tasks. The interrupted tasks are resumed later when they become the highest-priority tasks again. Preemptive scheduling can improve the responsiveness and reliability of the system, but it may introduce context switching overhead and synchronization issues.
- Schedulers can be implemented in different ways depending on the requirements and constraints of the embedded system. Some examples are:
  - **RIOS**: RIOS is a lightweight task scheduler for embedded systems that provides real-time scheduling of tasks with only tens of lines of extra code directly inserted into an application C program, requiring no special compilation. RIOS is easy for students to understand and does not require an RTOS.
  - **FreeRTOS**: FreeRTOS is a popular open source RTOS for embedded systems that supports preemptive or cooperative multitasking, priority-based scheduling, inter-task communication and synchronization, and low-power modes. FreeRTOS is portable, scalable, and suitable for various applications.
  - **Linux**: Linux is a general-purpose operating system that can be used for embedded systems with some modifications and extensions. Linux supports preemptive multitasking, priority and deadline scheduling, real-time extensions, and a rich set of features and libraries. Linux is powerful, flexible, and widely supported, but it may have a large footprint and high overhead for some embedded systems.



# Types of Scheduling for the Notes of the Unit 1 - Embedded OS Internals in the Subject of Embedded Systems and Real Time Operating System

Scheduling is the process of allocating CPU time to different tasks or processes in an embedded system. Scheduling can be done in various ways, depending on the requirements and constraints of the system. Some of the common types of scheduling are:

- **Non-preemptive scheduling**: In this type of scheduling, the CPU executes a task until it completes or voluntarily relinquishes the CPU. The CPU cannot be taken away from a running task by another task with higher priority or urgency. This type of scheduling is simple and easy to implement, but it can cause long delays and missed deadlines for some tasks. Non-preemptive scheduling is suitable for systems that do not have strict timing constraints or real-time requirements. 

- **Preemptive scheduling**: In this type of scheduling, the CPU can be taken away from a running task by another task with higher priority or urgency. The running task is suspended and resumed later when the CPU is available. This type of scheduling can reduce the response time and improve the performance of the system, but it can also introduce overhead and complexity. Preemptive scheduling is suitable for systems that have strict timing constraints or real-time requirements.  

- **Round-robin scheduling**: This is a special case of preemptive scheduling, where the tasks are assigned equal priority and the CPU is allocated to them in a circular order. Each task is given a fixed amount of CPU time, called a time slice or a quantum, and then the CPU is switched to the next task in the queue. This type of scheduling is fair and simple, but it can cause poor performance for some tasks that need more CPU time than others. Round-robin scheduling is suitable for systems that have similar tasks or low priority tasks.  

- **Time slice scheduling**: This is a variation of round-robin scheduling, where the tasks are assigned different priority levels and the CPU is allocated to them in a priority-based order. Each task is given a fixed amount of CPU time, called a time slice or a quantum, and then the CPU is switched to the next task in the same priority level or a higher priority level. This type of scheduling can improve the performance and responsiveness of the system, but it can also cause starvation for some tasks that have low priority or long execution time. Time slice scheduling is suitable for systems that have mixed tasks or real-time tasks. 

- **Priority scheduling**: This is a general type of preemptive scheduling, where the tasks are assigned different priority levels and the CPU is allocated to them according to their priority. The task with the highest priority is always executed first, and the task with the lowest priority is executed last. This type of scheduling can ensure that the most important or urgent tasks are completed on time, but it can also cause starvation or deadlock for some tasks that have low priority or depend on other tasks. Priority scheduling is suitable for systems that have diverse tasks or critical tasks.  

- **Composite scheduling**: This is a combination of different types of scheduling, where the system can switch between them depending on the situation or the mode of operation. For example, the system can use non-preemptive scheduling for normal operation, and use preemptive scheduling for emergency or exception handling. This type of scheduling can provide flexibility and adaptability to the system, but it can also increase the complexity and overhead. Composite scheduling is suitable for systems that have dynamic or heterogeneous tasks or modes.



# Interfacing

- Interfacing is the process of connecting and communicating between different components of an embedded system, such as sensors, actuators, microcontrollers, memory, peripherals, and software.
- Interfacing is essential for the functionality and performance of an embedded system, as it determines how data and signals are transferred, processed, and controlled within the system.
- Interfacing can be classified into two types: digital and analog.
  - Digital interfacing involves the use of binary signals (0 or 1) to represent data and commands. Digital interfacing can be further divided into parallel and serial interfaces, depending on how many bits are transmitted at a time.
  - Analog interfacing involves the use of continuous signals (such as voltage or current) to represent data and commands. Analog interfacing requires the use of analog-to-digital converters (ADCs) and digital-to-analog converters (DACs) to convert between analog and digital domains.
- Interfacing can also be classified into two levels: hardware and software.
  - Hardware interfacing refers to the physical connection and communication between the components of an embedded system, such as wires, connectors, buses, protocols, and standards. Hardware interfacing requires the knowledge of electrical and electronic principles, such as voltage, current, resistance, impedance, noise, and signal integrity.
  - Software interfacing refers to the logical connection and communication between the components of an embedded system, such as drivers, libraries, APIs, and operating systems. Software interfacing requires the knowledge of programming languages, data structures, algorithms, and software engineering principles, such as modularity, abstraction, and encapsulation.
- Interfacing is a challenging and complex task that requires the skills of both electrical and computer engineering. Interfacing design involves the selection of appropriate components, interfaces, and protocols for a given application, as well as the implementation and testing of the interface functionality and performance. Interfacing design also involves the consideration of various factors, such as cost, power, speed, reliability, security, and compatibility.



# Serial for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system (OS) is a specialized OS for an embedded device or system. The operating system aims to perform with certainty specific task(s) regularly that help the device operate .
- An embedded OS often has limited features and functions. The OS may perform only a single action that allows the device to work, but it must execute that action consistently and on time every time. Embedded OSs are built into Internet of Things (IoT) devices. They are also part of many other devices and systems.
- An embedded OS is a combination of software and hardware. It produces an easily understandable result by humans in many formats such as images, text, and voice. Embedded OSs are developed with programming code, which helps convert hardware languages into software languages like C and C++.
- An embedded OS achieves its functions via a kernel that includes, at a minimum: process management, memory management, and I/O system management components.
- Process management is the component that handles the creation, execution, and termination of processes or tasks. It also manages the scheduling, synchronization, and communication of processes.
- Memory management is the component that allocates and deallocates memory for processes and data. It also manages the virtual and physical memory spaces, the memory protection, and the memory mapping.
- I/O system management is the component that handles the input and output operations of the device. It also manages the device drivers, the file system, and the network protocols.
- An embedded OS differs from other types of OSs by its optimized design. It is usually tailored for a specific hardware platform, application domain, and performance requirement. It also has a smaller footprint, lower power consumption, and higher reliability than general-purpose OSs.
- Some examples of embedded OSs are: Linux, Android, Windows Embedded, FreeRTOS, QNX, VxWorks, and RTOS.



# Parallel for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a combination of software and hardware that is designed to perform a specific task or function in a larger system.  
- An embedded operating system aims to provide reliability, efficiency, and predictability for the embedded device or system.  
- An embedded operating system consists of a kernel and optional components such as device drivers, middleware, libraries, and applications. 
- The kernel is the core of the embedded operating system that manages the basic functions such as process management, memory management, and I/O system management. 
- Process management is the function of the kernel that creates, schedules, and terminates processes or threads that execute the application code. 
- Memory management is the function of the kernel that allocates, deallocates, and protects the memory space for the processes, the kernel, and the device drivers. 
- I/O system management is the function of the kernel that handles the communication between the processes and the external devices such as sensors, actuators, and networks. 
- Device drivers are the software components that interface with the hardware devices and provide a uniform abstraction for the kernel and the applications. 
- Middleware is the software component that provides common services and functionalities for the applications such as communication protocols, databases, graphical user interfaces, and security. 
- Libraries are the software components that provide reusable code and data structures for the applications such as mathematical functions, string manipulation, and data compression. 
- Applications are the software components that implement the specific logic and functionality of the embedded system such as control algorithms, signal processing, and user interaction. 
- Embedded operating systems can be classified into different types based on their characteristics and requirements such as real-time, general-purpose, and specialized.  
- Real-time operating systems (RTOS) are embedded operating systems that guarantee a timely and predictable response to events and stimuli in the system.  
- General-purpose operating systems (GPOS) are embedded operating systems that provide a rich set of features and functionalities for the system but do not guarantee a timely and predictable response.  
- Specialized operating systems are embedded operating systems that are customized and optimized for a specific domain or application such as automotive, industrial, or medical.



# Interrupt Handling

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts are indispensable when writing any practical embedded firmware, as they allow the CPU to respond to external events that are not synchronized to the software running on the system .
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
  - Hardware interrupts are triggered by peripheral devices outside the micro-controller, such as timers, sensors, buttons, etc .
  - Software interrupts are called from software, using a specified command, such as a system call or an exception .
- Interrupts have several advantages over polling, such as reducing CPU overhead, improving responsiveness, and simplifying the program logic.
- Interrupts also have some challenges, such as handling multiple interrupts, prioritizing interrupts, saving and restoring the CPU context, and synchronizing with the main program .
- Interrupt handling involves the following steps :
  - Detecting the interrupt request signal and identifying the source of the interrupt.
  - Saving the current CPU state, such as the program counter, the stack pointer, and the registers.
  - Jumping to the interrupt service routine (ISR), which is a function that performs the specific task related to the interrupt source.
  - Executing the ISR and clearing the interrupt flag to acknowledge the interrupt.
  - Restoring the CPU state and returning to the main program.
- Interrupt handling can be affected by the operating system, the hardware architecture, and the application requirements .
- Some of the best practices for writing ISRs are :
  - Keep the ISR as short and simple as possible, and avoid blocking or waiting operations.
  - Use interrupt priorities and nested interrupts to handle multiple interrupts efficiently and avoid missing or losing interrupts.
  - Use semaphores, mutexes, or flags to synchronize the ISR with the main program and avoid data corruption or race conditions.
  - Use volatile qualifiers and memory barriers to ensure the compiler does not optimize away the variables or instructions that are accessed by the ISR.
  - Use atomic operations or disable interrupts temporarily to protect critical sections of code that should not be interrupted.



# Linux Device Drivers

Linux device drivers are software modules that enable the Linux kernel to interact with various hardware devices. They are responsible for translating the device-specific commands and data into a generic form that the kernel can understand and process. Linux device drivers also handle the device interrupts, errors, and power management.

Some of the main features of Linux device drivers are:

- They are **modular** and can be loaded and unloaded dynamically into the kernel as needed. This allows for flexibility and efficiency in managing the system resources and device availability.
- They are **portable** and can run on different architectures and platforms, as long as they conform to the Linux kernel interface and follow the coding standards and conventions.
- They are **open-source** and can be modified and improved by anyone with the necessary skills and knowledge. This fosters collaboration and innovation in the Linux community and ensures the quality and security of the drivers.
- They are **diverse** and can support a wide range of devices, from simple ones like keyboards and mice, to complex ones like network cards and graphics cards. They can also support different types of devices, such as character devices, block devices, network devices, and USB devices.

Some of the main challenges of Linux device drivers are:

- They are **complex** and require a deep understanding of the device hardware, the Linux kernel, and the device driver framework. They also need to handle various scenarios and edge cases, such as concurrency, synchronization, error handling, and memory management.
- They are **critical** and can affect the stability and performance of the system. A faulty or malicious driver can cause kernel crashes, data corruption, or security breaches. Therefore, they need to be tested and verified thoroughly before deployment.
- They are **dynamic** and need to adapt to the changes and updates in the device hardware, the Linux kernel, and the user requirements. They also need to comply with the licensing and distribution policies of the Linux kernel and the device manufacturers.

Some of the main components of Linux device drivers are:

- The **device file** is a special file in the filesystem that represents the device and provides a way for the user applications to access the device. It has a name, a type, and a major and minor number that identify the device driver and the device instance.
- The **device driver** is a software module that implements the device-specific logic and functionality. It registers itself with the kernel and provides a set of functions that the kernel can call to perform operations on the device. It also handles the device interrupts, errors, and power management.
- The **device class** is a logical grouping of devices that share some common characteristics or features. It provides a way for the kernel to organize and manage the devices and their drivers. It also provides a uniform interface for the user applications to access the devices.
- The **device model** is a representation of the devices and their drivers in the kernel. It describes the relationships and dependencies among the devices and their drivers, such as parent-child, master-slave, and bus-device. It also provides a way for the kernel to enumerate and configure the devices and their drivers.



# Characteristics of Embedded Operating Systems

- An embedded operating system is a computer operating system designed for use in embedded computer systems.
- Embedded operating systems are designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications .
- Some of the main characteristics of embedded operating systems are:
  - Direct use of interrupts: Embedded operating systems use interrupts to handle events from hardware devices or software applications in a timely and efficient manner.
  - Reactive operation: Embedded operating systems respond to external stimuli and perform the required actions without delay.
  - Real-time operation: Embedded operating systems meet the deadlines and timing constraints of the applications they support, such as control systems, multimedia, and gaming.
  - Streamlined protection mechanisms: Embedded operating systems provide minimal or no protection mechanisms, such as memory management, user authentication, and access control, to reduce the overhead and complexity of the system.
  - I/O device flexibility: Embedded operating systems support a wide range of input and output devices, such as sensors, actuators, displays, keyboards, and cameras, and provide device drivers and interfaces for them.
- Some examples of embedded operating systems are :
  - Android: An open-source operating system based on Linux that is used for smartphones, tablets, smart TVs, and other devices.
  - iOS: A proprietary operating system developed by Apple that is used for iPhones, iPads, iPods, and other devices.
  - Windows Embedded: A family of operating systems based on Windows that are used for industrial, medical, automotive, and other devices.
  - FreeRTOS: A free and open-source operating system that is designed for microcontrollers and small embedded systems.
  - QNX: A commercial and proprietary operating system that is used for safety-critical and mission-critical applications, such as automotive, aerospace, defense, and medical devices.



# USB

USB stands for Universal Serial Bus  . It is a common interface that enables communication between devices and a host controller such as a personal computer (PC) or smartphone. It connects peripheral devices such as digital cameras, mice, keyboards, printers, scanners, media devices, external hard drives and flash drives .

Some of the features of USB are:

- It is a standardized technology that establishes specifications for cables, connectors and protocols for connection, communication and power supply (interfacing) between computers, peripherals and other computers.
- It supports plug-and-play and hot swapping, which means that devices can be connected and disconnected without rebooting the system or installing drivers.
- It can support up to 127 devices on a single bus, and devices can be arranged in a tree-like topology or a daisy chain.
- It has different versions that offer different data transfer rates and power delivery capabilities. The latest version is USB 4, which can support up to 40 Gbps of data transfer and up to 100 W of power delivery.
- It is compatible with various operating systems and platforms, such as Windows, Linux, Mac OS, Android, iOS, etc.

USB is widely used in embedded systems and real-time operating systems, as it provides a simple and flexible way of connecting and communicating with various devices and sensors. Some of the applications of USB in embedded systems are:

- Data acquisition and logging: USB can be used to collect and store data from sensors, such as temperature, pressure, humidity, etc., and transfer them to a PC or a cloud server for analysis and visualization.
- Device control and monitoring: USB can be used to send commands and receive feedback from devices, such as motors, actuators, relays, etc., and monitor their status and performance.
- Firmware update and debugging: USB can be used to upload new firmware or software to devices, such as microcontrollers, microprocessors, etc., and debug them using tools, such as serial monitors, debuggers, etc.
- Human-machine interface: USB can be used to connect devices, such as keyboards, mice, touchscreens, etc., to embedded systems and provide a user-friendly interface for interaction and input.
- Multimedia and entertainment: USB can be used to connect devices, such as speakers, headphones, cameras, etc., to embedded systems and provide audio and video output and input.

USB is an important and versatile technology for embedded systems and real-time operating systems, as it enables easy and efficient communication and integration of various devices and components. It also offers high performance, reliability, scalability and compatibility for different applications and platforms.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of Block & Network for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# Block & Network

- A block device is a device that stores or transfers data in fixed-sized units called blocks. Examples of block devices are hard disks, flash drives, CD-ROMs, etc.
- A network device is a device that communicates with other devices over a network using protocols such as TCP/IP, UDP, etc. Examples of network devices are network interface cards, routers, switches, etc.
- Block and network devices are important components of embedded systems, as they provide the means to store, retrieve, and exchange data with other systems or devices.
- Embedded OS internals are the low-level software components that manage and control the block and network devices in an embedded system. They include drivers, file systems, network stacks, etc.
- Drivers are software modules that interface with the hardware devices and provide a uniform and abstract way of accessing them. Drivers hide the device-specific details and expose a common set of functions and data structures to the upper layers of the OS.
- File systems are software modules that organize and manage the data stored on block devices. File systems provide a logical view of the data and support operations such as creating, deleting, reading, and writing files and directories. File systems also maintain metadata such as file names, attributes, permissions, etc.
- Network stacks are software modules that implement the network protocols and enable the communication between network devices. Network stacks consist of multiple layers, each performing a specific function such as addressing, routing, error control, etc. Network stacks also provide application programming interfaces (APIs) such as sockets, which allow the applications to send and receive data over the network.



# Unit 2 - OPEN SOURCE RTOS

- An open source RTOS is a real-time operating system (RTOS) whose source code is publicly available and can be modified and distributed by anyone.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, meaning that tasks are completed within a specified time frame and with predictable results.
- An open source RTOS can have several advantages over a proprietary RTOS, such as:
  - Lower cost: An open source RTOS can be obtained for free or at a low cost, while a proprietary RTOS may require licensing fees or royalties.
  - Higher quality: An open source RTOS can be more reliable and secure than a proprietary RTOS, because the source code is open and available for anyone to review and improve.
  - Greater flexibility: An open source RTOS can be customized and adapted to suit the specific needs and preferences of the user, while a proprietary RTOS may have limited or no options for customization.
  - More compatibility: An open source RTOS can be more compatible with different hardware platforms and software applications, because it can be ported and integrated with various components, while a proprietary RTOS may have restricted or exclusive compatibility.
- Some examples of open source RTOSs are:
  - FreeRTOS: A market-leading RTOS for microcontrollers and small microprocessors, distributed freely under the MIT open source license, and developed in partnership with the world’s leading chip companies.
  - Linux: A widely used and popular RTOS for general-purpose computing, distributed under various open source licenses, and supported by a large and active community of developers and users.
  - OpenRTOS: A commercially licensed version of the FreeRTOS kernel that includes indemnification and dedicated support, and is provided by WITTENSTEIN high integrity systems - an AWS strategic partner.



# Basics of RTOS

A real-time operating system (RTOS) is a type of operating system that is designed to handle time-critical tasks and events in an embedded system. An RTOS provides the following features:

- **Determinism**: An RTOS guarantees that a task or an event will be executed within a specified time limit, regardless of the system load or other factors. This is essential for applications that require precise timing and synchronization with the external environment or other devices.
- **Multitasking**: An RTOS allows multiple tasks or threads to run concurrently on the same processor, and provides a scheduler for managing their execution. The scheduler can use different algorithms, such as priority-based, round-robin, or preemptive, to allocate CPU time to each task according to their requirements and constraints.
- **Inter-task communication and synchronization**: An RTOS provides mechanisms for tasks to communicate and synchronize with each other, such as message queues, semaphores, mutexes, events, signals, etc. These mechanisms help to coordinate the activities of different tasks and avoid conflicts or deadlocks.
- **Memory management**: An RTOS provides memory management functions, such as dynamic memory allocation, memory protection, memory mapping, etc. These functions help to optimize the use of memory resources and prevent memory leaks or corruption.
- **Interrupt handling**: An RTOS provides interrupt handling functions, such as interrupt service routines, interrupt nesting, interrupt masking, etc. These functions help to respond to external or internal events that require immediate attention and processing.
- **Device drivers**: An RTOS provides device drivers for interfacing with various hardware components, such as sensors, actuators, communication modules, etc. These drivers help to abstract the low-level details of the hardware and provide a uniform interface for the application layer.

There are different types of RTOS, depending on the degree of time sensitivity and reliability they offer. Some common types are:

- **Hard real-time operating system**: This type of RTOS guarantees that critical tasks will be completed within a specified deadline, and any failure to do so will result in a system failure or unacceptable consequences. Examples of hard real-time applications are air traffic control, nuclear power plant control, medical devices, etc.
- **Soft real-time operating system**: This type of RTOS provides some relaxation in the time limit, and allows some tasks to miss their deadlines occasionally, without causing a system failure or unacceptable consequences. However, the performance and quality of the system may degrade as a result. Examples of soft real-time applications are multimedia, gaming, video conferencing, etc.
- **Firm real-time operating system**: This type of RTOS lies between hard and soft real-time operating systems, and requires that tasks meet their deadlines most of the time, but not always. If a task misses its deadline, it is discarded and has no value for the system. Examples of firm real-time applications are stock market trading, online auctions, etc.

Some examples of RTOS are:

- **Azure RTOS**: This is a commercial RTOS developed by Microsoft, and it provides a suite of components, such as ThreadX, NetX, FileX, GUIX, etc., for developing real-time embedded applications. Azure RTOS can also be integrated with Azure IoT services for cloud connectivity and management.
- **FreeRTOS**: This is an open source RTOS that is widely used in the embedded industry, and it supports various architectures, such as ARM, AVR, PIC, etc. FreeRTOS provides a kernel, a scheduler, and various libraries for inter-task communication, memory management, etc.
- **VxWorks**: This is a commercial RTOS developed by Wind River, and it is used in many high-end and mission-critical applications, such as aerospace, defense, automotive, industrial, etc. VxWorks provides a kernel, a scheduler, and various libraries for inter-task communication, memory management, device drivers, networking, etc.



# Real-time concepts for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

## What is a real-time operating system (RTOS)?

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS provides the rigorous resource management and scheduling required to meet the demands of applications with multi-tasking, priority-driven pre-emptive scheduling and fast context-switching—all essential features of an embedded real-time system.
- An RTOS typically has a small footprint and is optimized for performance.

## What are the characteristics of an RTOS?

- An RTOS has two key features: predictability and determinism.
- Predictability means that an RTOS can guarantee that a task will be executed within a specified time frame, regardless of the system load or other factors.
- Determinism means that an RTOS can ensure that the same sequence of operations will be performed every time a task is executed, without any randomness or variation.
- An RTOS also has other characteristics, such as:
  - Low latency: the time between an event and the response of the system is minimal.
  - High throughput: the system can process a large amount of data or events in a given time.
  - Reliability: the system can handle errors and faults without compromising the functionality or safety of the application.
  - Scalability: the system can adapt to changing requirements or environments without affecting the performance or quality of the service.

## What are the advantages of using an RTOS in embedded systems?

- An RTOS is commonly used in embedded systems based on microcontrollers, which are devices that have limited resources, such as memory, processing power, or battery life.
- An RTOS can provide several benefits for embedded systems, such as:
  - Simplifying the development and debugging of complex applications that involve multiple tasks, interrupts, or communication protocols.
  - Improving the efficiency and responsiveness of the system by managing the allocation and sharing of resources among tasks.
  - Enhancing the quality and safety of the system by ensuring that critical tasks are executed on time and with the correct order.
  - Supporting the integration and interoperability of the system with other devices or networks by providing standard interfaces and protocols.

## What are some examples of open source RTOSs?

- An open source RTOS is an RTOS that is freely available and can be modified or distributed by anyone.
- Some examples of open source RTOSs are:
  - FreeRTOS: a popular and widely used RTOS that supports many architectures and platforms, and offers a rich set of features and services.
  - Zephyr: a scalable and modular RTOS that supports multiple hardware platforms and connectivity protocols, and aims to provide a secure and reliable environment for IoT applications.
  - RIOT: a lightweight and user-friendly RTOS that focuses on low-power and resource-constrained devices, and supports a variety of network stacks and protocols.
  - SAFERTOS: a functionally secure and certified RTOS that provides high performance and reliability while using a minimal amount of resources, and is designed for safety-critical applications.



# Hard Real Time and Soft Real Time

- A **real-time system** is a system that is designed to meet the timing requirements of the tasks it performs.
- A **real-time operating system (RTOS)** is a type of operating system that is designed to support real-time applications by providing features such as preemptive scheduling, priority-based scheduling, inter-task communication and synchronization.
- A **hard real-time system** is a system that has **absolute deadlines**, and if those allotted time spans are missed, a **system failure** will occur. For example, a missile control system, a pacemaker, or an airbag system are hard real-time systems.
- A **soft real-time system** is a system that has **relaxed deadlines**, and if those allotted time spans are missed, the system continues to function but with **undesirable lower quality of output**. For example, a video streaming system, a voice recognition system, or a web server are soft real-time systems.
- The main difference between hard and soft real-time systems is the **degree of determinism** and the **tolerance of system failure**. Hard real-time systems are **deterministic** in nature, meaning that they guarantee the completion of tasks within the specified time bounds. Soft real-time systems are **probabilistic**, meaning that they have a high probability of completing the tasks within the specified time bounds, but not a guarantee.
- Another difference between hard and soft real-time systems is the **scheduling algorithm** used by the RTOS. Hard real-time systems require a **fixed-priority scheduling algorithm**, such as rate-monotonic scheduling or deadline-monotonic scheduling, that assigns priorities to tasks based on their periods or deadlines. Soft real-time systems can use a **dynamic-priority scheduling algorithm**, such as earliest deadline first or least laxity first, that assigns priorities to tasks based on their current deadlines or slack times.
- A third difference between hard and soft real-time systems is the **performance metric** used to evaluate the system. Hard real-time systems use the **schedulability test**, which determines whether all the tasks can meet their deadlines under the given system parameters, such as task periods, execution times, and priorities. Soft real-time systems use the **quality of service (QoS)**, which measures the degree of satisfaction of the system output, such as throughput, latency, jitter, or error rate.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some differences between General Purpose OS and RTOS for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

# Differences between General Purpose OS and RTOS

- **Target devices**: A General Purpose OS (GPOS) is made for high-end, general purpose systems like a personal computer, a work station, a server system etc. An RTOS is usually designed for a low-end, stand-alone device like an ATM, Vending machines, Kiosks etc .
- **Size and weight**: A GPOS is heavy and large in size compared to an RTOS. An RTOS is light weight and small in size, as it has to fit in the limited memory and resources of the embedded system .
- **Task scheduling**: A GPOS is capable of handling various applications and are optimized to run a variety of applications at the same time. It switches between various processes very fast, creating an illusion that it all happens in real time. An RTOS schedules the tasks based on priority level and performs them within the deadline. It guarantees a deterministic response time for the critical tasks .
- **Kernel mode**: A GPOS has a non-preemptive kernel, which means that a high-priority thread cannot preempt a kernel call in a GPOS. A kernel call can block the execution of other threads until it finishes. An RTOS has a preemptive kernel, which means that a high-priority thread can interrupt a kernel call in an RTOS. A kernel call can be suspended and resumed later to allow other threads to run.
- **Performance**: A GPOS is optimized for high throughput and user experience, but not for meeting strict timing constraints. A GPOS may have unpredictable delays due to factors like paging, swapping, interrupts, etc. An RTOS is optimized for low latency and meeting hard real-time requirements. An RTOS has minimal or no delays due to factors like memory management, synchronization, etc.



# Basic architecture of an RTOS

An RTOS (Real-Time Operating System) is a specialized operating system that provides deterministic and predictable behavior for time-critical applications. An RTOS typically consists of the following components  :

- **The kernel**: The kernel is the core component of the RTOS that manages the basic functions such as task scheduling, interrupt handling, memory management, inter-task communication and synchronization, and timer services. The kernel can be either monolithic or microkernel, depending on the design philosophy and the trade-off between performance and modularity.
- **The tasks**: The tasks are the units of execution that run on the RTOS. Each task has a priority, a stack, a context, and a state. The tasks can be either periodic or aperiodic, depending on their timing requirements. The tasks can communicate with each other and with the kernel using various mechanisms such as message queues, semaphores, mutexes, event flags, pipes, signals, etc .
- **The device drivers**: The device drivers are the modules that interface with the hardware devices and provide a uniform abstraction for the tasks. The device drivers can be either integrated with the kernel or implemented as separate tasks, depending on the RTOS architecture and the device characteristics .
- **The middleware**: The middleware is the layer that provides additional services and functionalities to the tasks, such as networking, file system, graphical user interface, debugging, etc. The middleware can be either part of the RTOS or provided by third-party vendors, depending on the application requirements and the RTOS compatibility .

The following diagram illustrates the general architecture of an RTOS:

RTOS architecture

: https://www.engineersgarage.com/rtos-real-time-operating-system/
: https://www.windriver.com/solutions/learning/rtos
: https://microcontrollerslab.com/rtos-real-time-operating-system/



# Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a mechanism that determines which task or process should run on a processor at a given time, based on some criteria and constraints.
- A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint.
- An open source RTOS is a RTOS that has its source code available for anyone to inspect, modify, and enhance.
- Some of the most popular open source RTOSes are FreeRTOS, Zephyr, RIOT, and NuttX.
- These RTOSes differ in their features, such as scheduling, inter-process communication, memory management, and interrupt latency.
- Some commonly used RTOS scheduling algorithms are:
  - Cooperative scheduling: tasks voluntarily yield the processor to other tasks when they are idle or waiting for an event.
  - Preemptive scheduling: tasks can be interrupted by the scheduler to run a higher priority task.
  - Rate-monotonic scheduling: tasks are assigned fixed priorities based on their periodic execution rates, with higher rates having higher priorities.
  - Round-robin scheduling: tasks with the same priority are executed in a circular order, with each task getting a fixed time slice of the processor.
  - Fixed priority pre-emptive scheduling: tasks are assigned fixed priorities and can be preempted by higher priority tasks, but not by lower priority tasks.
  - Fixed priority scheduling with deferred preemption: tasks are assigned fixed priorities and can be preempted by higher priority tasks, but only at certain preemption points within the task code.
  - Fixed priority non-preemptive scheduling: tasks are assigned fixed priorities and run to completion once they start, without being preempted by any other task.
- The choice of scheduling algorithm depends on the requirements and characteristics of the application, such as the number of tasks, the deadline constraints, the resource utilization, and the predictability of the system behavior.



# Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS .
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and flexibly.
- IPC can be implemented using various techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls.
- Different open source RTOSes may offer different IPC APIs and features, depending on their design and architecture .
- One of the most popular open source RTOSes is FreeRTOS, which provides a rich set of IPC APIs, such as:
  - Binary and counting semaphores, which are used to synchronize tasks and share resources.
  - Mutexes, which are a special type of semaphore that provide priority inheritance and recursive locking.
  - Event groups, which are used to notify tasks of the occurrence of multiple events.
  - Message buffers, which are used to send and receive variable length messages between tasks or interrupts.
  - Stream buffers, which are used to send and receive streams of data between tasks or interrupts.
  - Notifications, which are used to send a single 32-bit value to a task or an interrupt.
  - Queues, which are used to send and receive fixed length messages between tasks or interrupts.
  - Queue sets, which are used to monitor multiple queues and semaphores for events.



# Performance Metrics in Scheduling Models for Open Source RTOS

- A real-time operating system (RTOS) is a software system that manages the execution of tasks and resources in a system with timing constraints.
- The performance of an RTOS depends on various parameters, such as memory usage, latency, throughput, scalability, reliability, and power consumption.
- Scheduling is one of the most important parameters that affects the performance of an RTOS, as it determines how tasks are assigned to processors and how they are preempted or suspended when higher priority tasks arrive.
- Scheduling models are the algorithms or policies that define the rules for scheduling tasks in an RTOS. There are different types of scheduling models, such as fixed priority, dynamic priority, earliest deadline first, rate monotonic, etc.
- Open source RTOSs are RTOSs that are freely available and can be modified and distributed by anyone. Some examples of open source RTOSs are FreeRTOS, RTEMS, Zephyr, etc.
- Performance metrics are the measures or indicators that are used to evaluate and compare the performance of different scheduling models and RTOSs. Some common performance metrics are:
  - Memory footprint: the amount of ROM and RAM required by the RTOS kernel and the application tasks.
  - Context switch time: the time required to save and restore the state of a task when it is preempted or resumed by the scheduler.
  - Interrupt latency: the time required to respond to an external or internal event that triggers a task or a handler.
  - Scheduling overhead: the time required to execute the scheduling algorithm and select the next task to run.
  - Task response time: the time elapsed from the arrival of a task to its completion.
  - Task deadline miss ratio: the percentage of tasks that fail to meet their deadlines.
  - Task utilization: the ratio of the execution time of a task to its period or inter-arrival time.
  - Processor utilization: the ratio of the total execution time of all tasks to the total available time of the processor.
  - Power consumption: the amount of energy consumed by the system during its operation.
- Performance metrics can be measured using different methods, such as analytical models, simulation tools, benchmarking techniques, or experimental tests.
- Performance metrics can be used to compare and select the best scheduling model and RTOS for a given application and system requirements.



# Interrupt management in RTOS environment

- Interrupts are events that occur asynchronously and require immediate attention from the processor.
- Interrupts can be triggered by external devices, such as sensors, timers, or communication interfaces, or by internal sources, such as software exceptions or system calls.
- Interrupts can improve the responsiveness and efficiency of an embedded system, but they can also introduce challenges and complexities, especially when using a real-time operating system (RTOS).
- An RTOS is a software layer that provides services for managing tasks, resources, synchronization, and communication in a real-time system.
- An RTOS typically uses a scheduler to determine which task should run at any given time, based on their priorities and deadlines.
- An RTOS also provides mechanisms for tasks to communicate and synchronize with each other, such as queues, semaphores, mutexes, and events.
- When an interrupt occurs, the processor suspends the current task and jumps to a predefined address, where an interrupt service routine (ISR) is executed.
- An ISR is a special function that handles the interrupt source and performs the necessary actions, such as reading or writing data, clearing flags, or sending signals.
- An ISR should be as short and simple as possible, to minimize the interrupt latency and the impact on the RTOS scheduler and other tasks.
- Interrupt latency is the time between the occurrence of an interrupt and the execution of the corresponding ISR.
- Interrupt latency can be affected by several factors, such as the processor architecture, the interrupt controller, the interrupt priority, the interrupt nesting, and the RTOS configuration.
- Interrupt nesting is the ability of the processor to handle multiple interrupts at the same time, by allowing higher priority interrupts to preempt lower priority ones.
- Interrupt nesting can reduce the interrupt latency for critical interrupts, but it can also increase the stack usage and the complexity of the ISR code.
- When using an RTOS, the ISR should not perform any complex or time-consuming operations, such as memory allocation, file access, or blocking calls.
- Instead, the ISR should defer most of the processing to another thread, such as a task, by using the RTOS services, such as queues, semaphores, events, or software timers.
- This way, the ISR can return quickly and allow the RTOS scheduler to resume the normal execution of the tasks, while the deferred processing can be done at a lower priority and with proper synchronization.
- The RTOS services that can be used from an ISR are usually marked as "fromISR" or "ISR safe" in the RTOS documentation or API.
- These services are designed to be fast and deterministic, and to avoid any conflicts or deadlocks with the RTOS scheduler or other tasks.
- Some examples of RTOS services that can be used from an ISR are:

  - xQueueSendFromISR: Sends a message to a queue from an ISR.
  - xSemaphoreGiveFromISR: Gives a semaphore from an ISR.
  - xEventGroupSetBitsFromISR: Sets one or more bits in an event group from an ISR.
  - xTimerPendFunctionCallFromISR: Defers the execution of a function to a timer service task from an ISR.

- The use of these services from an ISR may require some additional steps, such as:

  - Enabling the interrupt source and setting the interrupt priority in the interrupt controller.
  - Registering the ISR function with the RTOS interrupt dispatcher or the interrupt vector table.
  - Calling the RTOS yield function at the end of the ISR, to request a context switch if a higher priority task is ready to run.

- The following code snippet shows an example of an ISR that uses the FreeRTOS API to defer the processing of a UART interrupt to a task:

```c
// UART ISR
void vUARTHandler(void)
{
  // Declare a variable to hold the received byte
  char cRxedChar;
  // Declare a variable to indicate if a context switch is needed
  BaseType_t xHigherPriorityTaskWoken = pdFALSE;
  // Read the received byte from the UART register
  cRxedChar = UART_RX_REG;
  // Send the received byte to a queue
  xQueueSendFromISR(xRxQueue, &cRxedChar, &xHigherPriorityTaskWoken);
  // Clear the UART interrupt flag
  UART_INT_FLAG = 0;
  // Request a context switch if a higher priority task is ready to run
  portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}
```

- The following code snippet shows an example of a task that receives the bytes from the queue and processes them:



# Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in an RTOS.
- Memory management can be done in two ways: static or dynamic.
- Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This method is simple, fast, and deterministic, but it can waste memory and limit flexibility.
- Dynamic memory management means that the memory is allocated and freed at run time, depending on the needs of the application. This method is more flexible and efficient, but it can introduce overhead, fragmentation, and non-determinism.
- An open source RTOS is an RTOS that is freely available and can be modified and distributed by anyone. Some examples of open source RTOS are FreeRTOS, Zephyr, and Linux.
- An open source RTOS may use different memory management options, depending on the features and requirements of the system. Some of the common options are:
  - Heap: A heap is a pool of memory that can be dynamically allocated and freed by the RTOS or the application. A heap can be implemented using different algorithms, such as first-fit, best-fit, or worst-fit. A heap can provide flexibility and efficiency, but it can also cause fragmentation, overhead, and non-determinism.
  - Stack: A stack is a region of memory that is used to store the local variables and return addresses of the tasks. A stack is allocated and freed automatically by the RTOS when a task is created and deleted. A stack can provide speed and simplicity, but it can also cause overflow, underflow, and stack corruption.
  - Static: Static memory is memory that is allocated at compile time and cannot be changed at run time. Static memory can be used to store the global variables and constants of the application. Static memory can provide determinism and reliability, but it can also waste memory and limit flexibility.
  - Memory pool: A memory pool is a collection of fixed-size memory blocks that can be allocated and freed by the RTOS or the application. A memory pool can reduce fragmentation and overhead, but it can also waste memory and limit flexibility.
  - Memory protection: Memory protection is a mechanism that prevents unauthorized access or modification of the memory by the tasks or the RTOS. Memory protection can improve the security and reliability of the system, but it can also introduce complexity and overhead. Memory protection can be implemented using hardware or software techniques, such as memory management unit (MMU), memory protection unit (MPU), or memory access control list (MACL).



# File systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A file system is a software component that manages the storage and retrieval of data on a persistent device, such as a hard disk, flash memory, or SD card.
- A file system organizes data into files and directories, and provides an interface to access, create, modify, or delete them.
- A file system also maintains metadata, such as file names, attributes, permissions, timestamps, and allocation information.
- A file system can be formatted with different standards, such as FAT, exFAT, NTFS, ext4, etc. Each standard has its own advantages and disadvantages in terms of compatibility, performance, reliability, and features.
- An embedded file system is a file system that is designed for embedded systems, which are devices that have limited resources, such as memory, CPU, power, and storage.
- An embedded file system is typically optimized for speed, efficiency, robustness, and portability. It may also support features that are specific to embedded applications, such as wear leveling, power fail safety, encryption, compression, etc.
- An open source RTOS is a real-time operating system that is distributed under a free or open source license, such as MIT, GPL, BSD, etc.
- An open source RTOS allows developers to access, modify, and redistribute the source code of the operating system, which can facilitate customization, innovation, and collaboration.
- An open source RTOS may also provide a standard and consistent interface for application development, such as POSIX, CMSIS, or FreeRTOS API.
- Some examples of open source RTOS are FreeRTOS, Azure RTOS, RTEMS, Zephyr, etc.
- A file system for an open source RTOS is an embedded file system that is compatible with the open source RTOS and its supported devices and platforms.
- A file system for an open source RTOS may also integrate with the RTOS features, such as threads, mutexes, semaphores, queues, timers, etc.
- A file system for an open source RTOS may also support the file formats that are commonly used by the RTOS and its applications, such as FAT, exFAT, etc.
- Some examples of file systems for open source RTOS are Reliance Edge, Azure RTOS FileX, IMFS, Mini-IMFS, etc.



# I/O Systems

- I/O systems are the components that enable an embedded system to interact with the external environment, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
  - Parallel I/O systems transfer multiple bits of data simultaneously using multiple wires or pins. They are faster but require more hardware resources and wiring complexity.
  - Serial I/O systems transfer one bit of data at a time using a single wire or pin. They are slower but require less hardware resources and wiring complexity.
- I/O systems can also be classified into two modes: synchronous and asynchronous.
  - Synchronous I/O systems transfer data at a fixed rate and require a clock signal to synchronize the sender and receiver. They are more reliable but require more bandwidth and power consumption.
  - Asynchronous I/O systems transfer data at a variable rate and do not require a clock signal to synchronize the sender and receiver. They are more flexible but require more error detection and correction mechanisms.
- I/O systems can use different protocols to communicate data, such as UART, SPI, I2C, USB, etc.
  - UART (Universal Asynchronous Receiver/Transmitter) is a serial protocol that uses two wires: TX (transmit) and RX (receive). It is widely used for low-speed communication between devices, such as keyboards, modems, GPS, etc.
  - SPI (Serial Peripheral Interface) is a serial protocol that uses four wires: SCLK (serial clock), MOSI (master out slave in), MISO (master in slave out), and SS (slave select). It is widely used for high-speed communication between devices, such as microcontrollers, sensors, memory cards, etc.
  - I2C (Inter-Integrated Circuit) is a serial protocol that uses two wires: SDA (serial data) and SCL (serial clock). It is widely used for low-speed communication between devices, such as microcontrollers, sensors, LCDs, etc.
  - USB (Universal Serial Bus) is a serial protocol that uses four wires: VCC (power supply), GND (ground), D+ (data plus), and D- (data minus). It is widely used for high-speed communication between devices, such as computers, cameras, printers, etc.
- I/O systems can be controlled by different methods, such as polling, interrupt, DMA, etc.
  - Polling is a method that involves the CPU periodically checking the status of an I/O device to determine if it is ready to send or receive data. It is simple but inefficient and wasteful of CPU time and power.
  - Interrupt is a method that involves the I/O device sending a signal to the CPU when it is ready to send or receive data. It is efficient and saves CPU time and power, but requires more hardware and software complexity and overhead.
  - DMA (Direct Memory Access) is a method that involves a dedicated hardware controller transferring data between the I/O device and the memory without involving the CPU. It is very efficient and fast, but requires more hardware and software complexity and overhead.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points on the advantages and disadvantages of RTOS for your notes:

# Advantage and disadvantage of RTOS

## Advantages of RTOS

- **Less Downtime**: A RTOS makes sure that the system consumes more resources while keeping all devices in active state.
- **Maximum Consumption**: A RTOS provides maximum utilization of devices and systems, thus more output from all the resources .
- **Task Shifting**: A RTOS assigns very less time for shifting tasks, for example, in older systems, it takes about 10 microseconds, but in RTOS, it takes about 3 to 5 microseconds .
- **Accurate Output**: A RTOS produces an accurate output within no time, as it is programmed to execute priority tasks within specific deadlines.
- **Suitable for Time-Critical Applications**: A RTOS is suitable for applications that require real-time response, such as embedded systems, robotics, industrial automation, etc .

## Disadvantages of RTOS

- **Complex Design**: A RTOS requires a complex design and implementation, as it has to deal with multiple tasks, priorities, deadlines, interrupts, etc.
- **High Cost**: A RTOS is more expensive than a general-purpose operating system, as it requires more memory, processing power, and specialized hardware.
- **Longer Wait for Low-Priority Tasks**: A RTOS is programmed to execute priority tasks within specific deadlines, lower priority tasks may have to wait longer versus an OS.
- **Minimal Task Capacity**: A RTOS can only run minimal tasks simultaneously, as it is not suitable for multi-tasking.
- **Difficult to Test and Debug**: A RTOS is difficult to test and debug, as it involves real-time constraints, concurrency, synchronization, etc.



# POSIX standards for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- POSIX stands for Portable Operating System Interface, which is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines a standard operating system interface and environment, including a command interpreter (or “shell”), and common utility programs to support applications portability at the source code level.
- POSIX also defines a standard threading API, which is widely popular among developers for multithreading and concurrency  .
- POSIX threads, also known as pthreads, enable quicker execution of the software, and are implemented in many open source RTOSes, such as FreeRTOS, LynxOS, and PX5  .
- POSIX threads provide features such as thread creation, termination, synchronization, scheduling, and cancellation .
- POSIX threads can be written in C or C++, and are compatible with embedded Linux and other POSIX-compliant operating systems   .
- POSIX standards are intended to be used by both application developers and system implementors, and comprise four major components: Base Definitions, System Interfaces, Shell and Utilities, and Rationale.
- POSIX standards are periodically updated and revised, and the latest version is POSIX.1-2017, which incorporates IEEE Std 1003.1-2008 and ISO/IEC 9945:2009, as well as several technical corrigenda and interpretations.
- POSIX standards are beneficial for open source RTOSes, as they enable portability, interoperability, and compatibility among different platforms and devices   .



# RTOS Issues

- An RTOS (Real-Time Operating System) is an operating system that provides predictable and deterministic behavior for time-critical applications.
- However, using an RTOS also introduces some challenges and issues that developers need to be aware of and address in their design and implementation.
- Some of the common RTOS issues are:

  - **Priority inversion**: This occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task. This results in the high-priority task waiting longer than expected for the resource, violating its timing constraints .
  - **Deadlock**: This occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed. This leads to a system-wide halt and wasted CPU time .
  - **Task jitter**: This occurs when a periodic task experiences variations in its execution time or start time, due to factors such as scheduling, interrupts, or resource contention. This affects the quality of service and performance of the task, especially if it has strict timing requirements.
  - **Control-flow complexity**: This occurs when the control-flow of the program is not apparent from the source code, since the RTOS decides which task to execute at any given moment. This makes it harder to understand, debug, and test the program, and requires new tools and techniques such as tracing and state machines.
  - **Security risks**: This occurs when the RTOS or the application does not implement or use security features such as encryption, authentication, authorization, or secure boot. This exposes the system to potential attacks from malicious actors, such as data theft, tampering, or denial of service.
  - **Interrupt latency**: This occurs when the RTOS takes too long to respond to an interrupt request, due to factors such as disabling interrupts, context switching, or interrupt nesting. This can cause the system to miss or delay critical events, or violate real-time constraints .
  - **Resource management**: This occurs when the RTOS or the application does not allocate, deallocate, or reuse resources such as memory, CPU, or peripherals efficiently or correctly. This can lead to memory leaks, fragmentation, starvation, or corruption, affecting the system's reliability and performance.



# Selecting a Real-Time Operating System

A real-time operating system (RTOS) is a software platform that provides predictable and deterministic behavior for embedded systems that have strict timing constraints. An RTOS can manage the concurrent execution of multiple tasks, provide inter-task communication and synchronization mechanisms, and support various hardware interfaces and protocols. Choosing the right RTOS for a specific application is a crucial decision that can affect the performance, reliability, scalability, and maintainability of the system. Here are some steps and criteria that can help in selecting a suitable RTOS:

- Step 1: Requirements review. The very first step is to thoroughly review the requirements for the OS, such as the functional, performance, reliability, security, and safety requirements. The requirements should specify the expected behavior and characteristics of the system, such as the number and type of tasks, the worst-case execution time, the memory footprint, the power consumption, the fault tolerance, the security level, and the compliance with standards and regulations. The requirements should also identify the target hardware platform, such as the processor architecture, the memory size, the peripherals, and the communication interfaces. The requirements review can help to narrow down the list of potential RTOS candidates that can meet the needs of the system.

- Step 2: Availability on target platform. The next step is to check the availability of the RTOS on the selected target hardware platform. Most RTOSs are only available for a limited set of processor architectures, such as x86, Power Architecture, MIPS, and ARM. Some RTOSs may also require specific hardware features, such as memory management units, timers, interrupts, and caches. It is important to verify that the RTOS can run on the chosen hardware platform and that it can support all the required hardware interfaces and protocols.

- Step 3: Support of required functions. The third step is to evaluate the support of the RTOS for the required functions and features of the system. Some of the common functions and features that an RTOS may provide are:

  - Task management: The ability to create, delete, suspend, resume, and prioritize tasks, and to assign them to different cores or processors in a multicore or multiprocessor system.
  - Scheduling: The algorithm and policy that the RTOS uses to determine which task to run next, and how to handle task preemption, context switching, and deadline violations. The scheduling can be either preemptive or cooperative, and either fixed-priority or dynamic-priority. Some RTOSs may also support rate-monotonic, earliest-deadline-first, or other advanced scheduling algorithms.
  - Inter-task communication and synchronization: The mechanisms that the RTOS provides for tasks to exchange data and signals, and to coordinate their execution. These mechanisms may include message queues, mailboxes, pipes, semaphores, mutexes, events, signals, and condition variables.
  - Memory management: The methods that the RTOS uses to allocate, deallocate, and protect memory for tasks and data structures. The memory management can be either static or dynamic, and either partitioned or pooled. Some RTOSs may also support memory protection, virtual memory, or memory mapping.
  - Interrupt handling: The way that the RTOS handles hardware and software interrupts, and how it integrates them with the task management and scheduling. The interrupt handling can affect the interrupt latency, the interrupt response time, and the interrupt priority.
  - Input/output management: The support that the RTOS provides for various input/output devices and protocols, such as serial ports, USB, Ethernet, CAN, SPI, I2C, Bluetooth, Wi-Fi, and others. The input/output management can include device drivers, middleware, stacks, and libraries.
  - File system: The support that the RTOS provides for storing and accessing files and directories on various storage media, such as flash memory, SD cards, hard disks, and others. The file system can include file management, directory management, file attributes, file locking, and file encryption.
  - Graphical user interface: The support that the RTOS provides for creating and displaying graphical user interfaces on various display devices, such as LCDs, touchscreens, and others. The graphical user interface can include widgets, fonts, images, animations, and touch events.
  - Debugging and testing: The tools and features that the RTOS provides for debugging and testing the system, such as breakpoints, watchpoints, tracepoints, logging, profiling, code coverage, and unit testing.

- Step 4: Portability. The fourth step is to assess the portability of the RTOS, which is the ease of moving the system from one hardware platform



# RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the characteristics and features of different RTOSs and compare them based on various criteria.

## Characteristics of RTOS

Some of the common characteristics of RTOS are:

- **Determinism**: The ability to perform operations or tasks in a fixed amount of time, regardless of the system load or external factors.
- **Responsiveness**: The ability to respond quickly to external events or stimuli, such as interrupts or signals.
- **Reliability**: The ability to function correctly and consistently, even in the presence of faults or errors.
- **Scalability**: The ability to adapt to changing requirements or conditions, such as adding or removing tasks, devices, or resources.
- **Efficiency**: The ability to utilize the available resources, such as memory, CPU, or power, in an optimal way, without wasting or overloading them.

## Features of RTOS

Some of the common features of RTOS are:

- **Task management**: The ability to create, delete, suspend, resume, prioritize, and schedule tasks or threads, which are the basic units of execution in an RTOS.
- **Memory management**: The ability to allocate, deallocate, and protect memory regions for tasks, data, or code, as well as to support different types of memory, such as static, dynamic, or shared.
- **Inter-task communication**: The ability to exchange data or signals between tasks, using various mechanisms, such as message queues, semaphores, mutexes, events, or pipes.
- **Interrupt handling**: The ability to handle external or internal interrupts, which are requests for immediate attention from the hardware or software, and to dispatch them to the appropriate tasks or handlers.
- **Device management**: The ability to control and access various devices, such as sensors, actuators, or peripherals, using different protocols, such as serial, parallel, or USB.
- **File system**: The ability to store and retrieve data from persistent storage, such as disks, flash, or EEPROM, using different formats, such as FAT, NTFS, or EXT.
- **Network support**: The ability to communicate with other systems or devices over a network, using different protocols, such as TCP/IP, UDP, or MQTT.
- **Time management**: The ability to measure and manipulate time, using different units, such as ticks, milliseconds, or seconds, and to provide various services, such as timers, clocks, or alarms.

## Comparison of RTOS

There are many RTOSs available in the market, each with its own advantages and disadvantages. Some of the popular RTOSs are:

- **FreeRTOS**: An open source RTOS that is designed to be small, simple, and portable. It supports various architectures, such as ARM, AVR, PIC, and x86, and provides basic features, such as task management, memory management, inter-task communication, and interrupt handling. It does not provide advanced features, such as file system, network support, or graphical user interface. It is suitable for embedded systems that have limited resources and require low complexity.
- **Zephyr**: An open source RTOS that is designed to be scalable, modular, and secure. It supports various architectures, such as ARM, x86, RISC-V, and ARC, and provides basic and advanced features, such as task management, memory management, inter-task communication, interrupt handling, device management, file system, network support, and time management. It also supports Bluetooth communication, which doubles its footprint. It is suitable for embedded systems that have diverse requirements and require high performance.
- **LynxOS**: A proprietary RTOS that is designed to be reliable, deterministic, and POSIX-compliant. It supports various architectures, such as ARM, x86, PowerPC, and MIPS, and provides basic and advanced features, such as task management, memory management, inter-task communication, interrupt handling, device management, file system, network support, and time management. It also provides a graphical user interface, a bash shell, and a printf function. It is suitable for embedded systems that have critical applications and require high reliability.

The following table summarizes some of the criteria and features of the three RTOSs:

| Criteria | FreeRTOS | Zephyr | LynxOS |
| --- | --- | --- | --- |
| License | Open source | Open source | Proprietary |
| Architecture |



# Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with predictable and deterministic response times .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports different scheduling algorithms, such as priority-based, round-robin, or deadline-based, to assign CPU time to tasks according to their importance and urgency .
- A real-time kernel provides mechanisms for inter-task communication and synchronization, such as semaphores, message queues, mutexes, and event flags .
- A real-time kernel can be identified by the rt keyword in the kernel version, which indicates that the kernel has been patched with the PREEMPT_RT patch to reduce the latency and increase the responsiveness of the system .



# Converting a normal Linux kernel to real time kernel

- A real time kernel is a kernel that can guarantee a deterministic response time to events, such as interrupts, system calls, or user inputs.
- A normal Linux kernel is not designed for real time applications, as it may incur unpredictable delays due to factors such as process scheduling, memory management, or locking mechanisms.
- To convert a normal Linux kernel to a real time kernel, one needs to apply a set of patches that modify the kernel behavior and configuration to enable full preemption, priority inheritance, and high resolution timers.
- The steps to convert a normal Linux kernel to a real time kernel are as follows:

  1. Download the source code of the normal Linux kernel and the corresponding real time patches from the official websites or repositories.
  2. Apply the real time patches to the kernel source code using the patch command or a graphical tool such as git or quilt.
  3. Configure the kernel options using the make menuconfig or make xconfig command. In the config options, set the ‘Fully Preemptible kernel (RT)’ option . You may also adjust other options related to real time performance, such as CPU frequency scaling, tickless kernel, or CPU isolation.
  4. Build the kernel using the make command. You may need to install some dependencies, such as gcc, ncurses, or openssl, before building the kernel.
  5. Install the kernel using the make install command. This will copy the kernel image and modules to the appropriate directories and update the boot loader configuration.
  6. Reboot the system and select the real time kernel from the boot menu. You can verify that you are running the real time kernel by executing the uname -r command and looking for the rt keyword in the kernel version  .

- By converting a normal Linux kernel to a real time kernel, you can improve the responsiveness and predictability of your system for real time applications, such as audio or video processing, robotics, or industrial control. However, you may also encounter some trade-offs, such as increased overhead, reduced throughput, or compatibility issues with some drivers or modules. Therefore, you should test and benchmark your system before and after the conversion to ensure that it meets your requirements and expectations.



# Xenomai basics

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications .
- Xenomai allows real-time threads to run either in kernel space or in user space, with the benefit of memory protection and direct scheduling by Xenomai.
- Xenomai uses Linux as a background task that can be preempted by real-time tasks, and provides a dual kernel architecture with a real-time nucleus and a Linux kernel .
- Xenomai supports various real-time interfaces, such as POSIX, RTAI, VxWorks, and others, and provides a unified API for accessing them .
- Xenomai can be installed on a Linux system by patching the kernel with the Xenomai source code and compiling it with the Xenomai configuration options .



# Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An **open source RTOS** is a real-time operating system that is freely available for anyone to use, modify, and distribute under a permissive license.
- An **embedded system** is a computer system that is designed to perform a specific function within a larger system, often with limited resources and strict timing constraints.
- An **application development** is the process of creating software programs that run on an embedded system, using various tools and languages.
- Some of the most popular open source RTOS for embedded systems are **FreeRTOS** and **ChibiOS/RT**.

## FreeRTOS

- FreeRTOS is a market-leading RTOS for microcontrollers and small microprocessors.
- It is designed to be simple and easy to use, with only 3 source files that are common to all RTOS ports, and one microcontroller specific source file.
- It supports over 40 architectures and 18 toolchains, and has a large community of users and contributors.
- It provides basic features such as task management, inter-task communication, synchronization, timers, memory management, and hooks for application-specific functionality.
- It also supports advanced features such as tick-less mode, event groups, software timers, queue sets, trace and visualization tools, and kernel-aware debugging.
- It is distributed under the MIT license, which allows commercial use without any restrictions.

## ChibiOS/RT

- ChibiOS/RT is a compact and fast RTOS for embedded systems, with a rich set of features and a high level of portability.
- It is designed to be modular and configurable, with a kernel that can be tailored to the specific needs of the application.
- It supports over 30 architectures and 10 toolchains, and has a growing community of users and developers.
- It provides basic features such as task management, inter-task communication, synchronization, timers, memory management, and hooks for application-specific functionality.
- It also supports advanced features such as tick-less mode, event flags, software timers, binary semaphores, mutexes, condition variables, memory pools, heap allocators, dynamic threads, and kernel statistics.
- It is distributed under the GPL license, with an optional commercial license for closed-source projects.

## Application development

- Application development for embedded systems using open source RTOS requires a set of tools and skills that are different from general-purpose software development.
- Some of the common tools and steps involved are:

  - **Choosing an RTOS** that suits the requirements and constraints of the embedded system, such as performance, memory, power, functionality, license, and support.
  - **Choosing a hardware platform** that is compatible with the chosen RTOS, such as a microcontroller, a development board, or a custom board.
  - **Choosing a toolchain** that can compile, link, and debug the application code for the target hardware, such as GCC, IAR, Keil, or Eclipse.
  - **Downloading and installing the RTOS** source code and documentation, and configuring the RTOS options and parameters according to the application needs.
  - **Writing the application code** using the RTOS API and libraries, and following the RTOS coding style and conventions.
  - **Building and flashing the application** to the target hardware, using tools such as make, CMake, or IDEs.
  - **Testing and debugging the application** using tools such as serial console, logic analyzer, oscilloscope, or RTOS-specific tools.



# Real Time Operating Systems

## Unit 3 - REAL TIME KERNEL BASICS

### Introduction

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints .
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism.
- Predictability means that repeated tasks are performed within a tight time boundary, while determinism means that the outcome of an operation is known in advance.
- An RTOS can be classified into two types: hard real-time and soft real-time .
- A hard real-time system guarantees that tasks are completed on time, even in the worst-case scenario, and any missed deadline can result in a system failure .
- A soft real-time system tries to complete tasks on time, but it can tolerate some delays, and any missed deadline can result in a degraded performance, but not a system failure .

### Real Time Kernel

- A real-time kernel is the core component of an RTOS that provides the basic services for managing tasks, interrupts, timers, memory, and communication .
- A real-time kernel is also called a real-time executive or a real-time scheduler .
- A real-time kernel is responsible for creating, deleting, suspending, resuming, and switching tasks, as well as assigning priorities and allocating resources to them .
- A real-time kernel is also responsible for handling interrupts, which are signals from hardware devices or software events that require immediate attention .
- A real-time kernel is also responsible for managing timers, which are used to measure time intervals, generate periodic events, or trigger timeouts .
- A real-time kernel is also responsible for managing memory, which is used to store data and code for tasks and other kernel objects .
- A real-time kernel is also responsible for managing communication, which is used to exchange data and signals between tasks or other kernel objects .

### Real Time Kernel Design

- A real-time kernel can be designed using different approaches, such as monolithic, modular, microkernel, or hybrid .
- A monolithic kernel is a single large program that contains all the kernel functions and runs in a privileged mode .
- A monolithic kernel is fast and efficient, but it is complex, difficult to maintain, and prone to errors .
- A modular kernel is a collection of independent modules that can be loaded and unloaded dynamically as needed .
- A modular kernel is flexible and extensible, but it introduces some overhead and complexity in managing the modules .
- A microkernel is a minimal program that provides only the essential kernel functions, such as task management, interrupt handling, and inter-process communication .
- A microkernel is simple, reliable, and portable, but it requires more context switches and communication overhead than a monolithic kernel .
- A hybrid kernel is a combination of a microkernel and a monolithic kernel, where some kernel functions are implemented as modules that run in user mode, while others are implemented as part of the core kernel that runs in privileged mode .
- A hybrid kernel is a compromise between the advantages and disadvantages of a microkernel and a monolithic kernel .

### Real Time Kernel Examples

- Some examples of real-time kernels are:

  - Azure RTOS ThreadX: This is an advanced RTOS that is designed specifically for deeply embedded applications. It supports hard real-time, preemptive, priority-based scheduling, fast interrupt response, memory protection, event chaining, and many other features.
  - FreeRTOS: This is a popular open source RTOS that is designed for small and medium-sized



# Event based real time kernel basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel can provide deterministic response times to service events, which means it can guarantee that a certain task will be completed within a specified time bound.
- A real-time kernel is also known as kernel-rt or preempt-rt. The simplest way to identify a real-time kernel is to execute the `uname -r` command on the terminal, and then look for the `rt` keyword in the kernel version.
- A real-time kernel can be classified into two types: hard real-time and soft real-time. A hard real-time kernel must meet all the deadlines, otherwise the system may fail. A soft real-time kernel can tolerate some missed deadlines, but the quality of service may degrade.
- A real-time kernel can be implemented using different techniques, such as preemptive scheduling, priority inheritance, priority ceiling, interrupt handling, and synchronization mechanisms.
- Events in a real-time system are the actions or the results of the actions that are generated by the system or the environment. An event in a real-time system can be either instantaneous or have a certain duration.
- Events in a real-time system can be classified into four types: periodic, aperiodic, sporadic, and bursty. Periodic events occur at regular intervals, such as a timer interrupt. Aperiodic events occur at irregular intervals, such as a user input. Sporadic events occur randomly, such as a sensor reading. Bursty events occur in clusters, such as a network packet.
- A real-time kernel can handle events using different strategies, such as polling, interrupt-driven, hybrid, or event-driven. Polling is a technique where the kernel checks the status of each event periodically. Interrupt-driven is a technique where the kernel is notified by the hardware when an event occurs. Hybrid is a technique that combines polling and interrupt-driven. Event-driven is a technique where the kernel waits for an event to occur and then executes the corresponding task.



# Process Based Real Time Kernel Basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel can run on different CPU architectures and platforms, such as 8, 16 or 32-bit CPUs or DSP chips.
- A real-time kernel provides a real-time API (Application Programming Interface) that allows the application to create and manage tasks, semaphores, mutexes, queues, timers, etc .
- A real-time kernel also provides a scheduling algorithm that determines which task should run at any given time, based on the priority and state of each task .
- A real-time kernel can be classified into two types: preemptive and cooperative .
  - A preemptive kernel allows a higher priority task to interrupt a lower priority task at any time, ensuring that the most urgent task always gets the CPU .
  - A cooperative kernel requires a lower priority task to voluntarily yield the CPU to a higher priority task, which may result in longer delays and lower responsiveness .
- A real-time kernel can also be implemented in two ways: kernel model and user space model.
  - In a kernel model, the real-time kernel runs in the privileged mode of the CPU, and the application tasks run in the user mode.
  - In a user space model, the real-time kernel runs as a user space process, and the application tasks run as threads within the same process.
  - The advantages and disadvantages of each model are:
    - Kernel model: higher performance, lower overhead, simpler API, but limited kernel API, more complex development and debugging, less portability and compatibility.
    - User space model: lower performance, higher overhead, more complex API, but full Linux API, easier development and debugging, more portability and compatibility.
- A real-time kernel can be used for various applications that require deterministic and timely behavior, such as industrial control, robotics, multimedia, gaming, etc .
- A real-time kernel can be integrated with a standard Linux kernel, such as the Red Hat Enterprise Linux kernel, to provide both real-time and non-real-time functionality.
  - The real-time kernel is also known as kernel-rt or preempt-rt.
  - The real-time kernel can be identified by executing the uname -r command on the terminal, and then looking for the rt keyword in the kernel version.
  - The real-time kernel can be installed and configured using the yum or dnf commands, and the tuned-adm or rt-setup tools.



# Graph Based Models for Embedded Systems

- Graph based models are a way of representing the structure and behavior of embedded systems using nodes and edges.
- Nodes can represent components, variables, states, events, functions, or any other entity relevant to the system.
- Edges can represent connections, dependencies, transitions, flows, or any other relation between nodes.
- Graph based models can be used to analyze, simulate, prototype, specify, and deploy software algorithms within a variety of embedded systems and applications .
- Graph based models can also be used to generate graph embeddings, which are low-dimensional vector representations of nodes that capture their semantic and structural features.
- Graph embeddings can be used for tasks such as similarity search, clustering, classification, recommendation, or anomaly detection.
- Graph based models can be classified into different types based on the nature and complexity of the graphs, such as bipartite graphs, general graphs, and knowledge graphs.
- Bipartite graphs are graphs that have two sets of nodes, such that no edge connects nodes within the same set. They are often used to model user-item interactions, such as ratings, purchases, or clicks.
- General graphs are graphs that have no restrictions on the number or type of nodes and edges. They are often used to model complex systems, such as social networks, biological networks, or transportation networks.
- Knowledge graphs are graphs that have nodes representing entities and edges representing relations, such as facts, rules, or attributes. They are often used to model rich and structured information, such as ontologies, taxonomies, or schemas.
- Graph based models can be created and manipulated using graphical modeling environments, such as MATLAB, Simulink, Stateflow, or LabVIEW.
- Graphical modeling environments provide tools for drawing, editing, validating, simulating, and generating code from graph based models.
- Graphical modeling environments can also support 1D and 3D simulations, which are used to visualize and test the performance and behavior of the system under different scenarios and conditions.
- Graph based models can be integrated with other modeling approaches, such as finite state machines, Petri nets, or UML diagrams, to provide a comprehensive and consistent view of the system.
- Graph based models can also be combined with dynamic visualization techniques, such as animation, color coding, or interactive exploration, to enhance the understanding and communication of the system.



# Petri Net Models for Embedded Systems

- A **Petri net** is a graphical and mathematical model that can be used to describe the behaviour and interactions of concurrent and distributed systems.
- A Petri net consists of two types of nodes: **places** and **transitions**, connected by directed **arcs**. Places can hold a number of **tokens**, which represent the state or resources of the system. Transitions can fire when they have tokens in all their input places, and they consume and produce tokens according to the arcs.
- Petri nets can capture features of embedded systems such as time, data, concurrency, synchronization, and hierarchy  .
- There are different types of Petri nets, such as timed Petri nets, coloured Petri nets, stochastic Petri nets, and interpreted Petri nets, that can be used for different purposes and applications .
- Petri nets can be used for embedded system design, analysis, verification, and synthesis. They can also be used to model the real-time kernel and its components, such as tasks, interrupts, semaphores, queues, and schedulers  .



# Real time languages for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real time language is a programming language that supports the development of real time systems, which are systems that must respond to events within strict time constraints.
- Real time languages typically provide features such as concurrency, synchronization, memory management, scheduling, exception handling, and communication primitives that are suitable for real time applications.
- Some examples of real time languages are:

  - **C/C++**: C and C++ are widely used languages for embedded systems, as they offer low-level access to hardware, high performance, and portability. C and C++ can also be used with real time operating systems (RTOS) or real time extensions that provide real time services such as preemptive scheduling, priority-based interrupts, and inter-process communication. Some examples of RTOS or real time extensions for C/C++ are FreeRTOS, VxWorks, QNX, and RTLinux.
  - **Ada**: Ada is a high-level language that was designed with real time systems in mind. Ada supports concurrency, modularity, strong typing, exception handling, and generic programming. Ada also has a subset called Ravenscar Ada, which is a profile that restricts some features of Ada to ensure predictability and analyzability of real time systems. Some examples of RTOS or real time extensions for Ada are RTEMS, Ocarina, and PolyORB.
  - **Java**: Java is an object-oriented language that runs on a virtual machine, which provides portability, security, and automatic memory management. Java also has a subset called Real-Time Specification for Java (RTSJ), which is a set of extensions that enable real time programming in Java. RTSJ provides features such as real time threads, real time memory, real time clocks, and asynchronous event handling. Some examples of RTOS or real time extensions for Java are JamaicaVM, aJile, and JOP.
  - **Rust**: Rust is a modern language that focuses on safety and concurrency. Rust has a unique feature called ownership, which ensures that memory is managed without garbage collection or manual allocation. Rust also supports concurrency with features such as threads, channels, mutexes, and futures. Rust can be used for embedded systems with the help of libraries and frameworks such as embedded-hal, RTIC, and TockOS.

- The choice of a real time language depends on various factors, such as the requirements of the system, the available hardware and software resources, the development tools and environment, the developer's skills and preferences, and the trade-offs between performance, reliability, and maintainability.



# Real Time Kernel

A real time kernel is a software component that manages the time and resources of a CPU or MPU in a way that guarantees predictable and deterministic behavior. A real time kernel is also known as a real time operating system (RTOS) or a real time executive.

## Features of a Real Time Kernel

Some of the features of a real time kernel are:

- **Preemptive multitasking**: A real time kernel can switch between multiple tasks based on their priority and deadlines, and can interrupt a lower priority task to execute a higher priority task at any time.
- **Synchronization and communication**: A real time kernel provides mechanisms for tasks to synchronize and communicate with each other, such as semaphores, mutexes, message queues, event flags, etc.
- **Memory management**: A real time kernel can allocate and deallocate memory for tasks and data structures, and can prevent memory fragmentation and leaks.
- **Interrupt handling**: A real time kernel can handle hardware and software interrupts, and can assign priorities and handlers to them.
- **Timing services**: A real time kernel can provide accurate and reliable timing services, such as timers, delays, timeouts, etc.

## Types of Real Time Kernels

There are two main types of real time kernels:

- **Hard real time kernel**: A hard real time kernel guarantees that all tasks and interrupts will meet their deadlines, regardless of the system load and complexity. A hard real time kernel is suitable for applications that require strict timing constraints and high reliability, such as avionics, medical devices, robotics, etc.
- **Soft real time kernel**: A soft real time kernel tries to meet the deadlines of tasks and interrupts, but does not guarantee it. A soft real time kernel is suitable for applications that can tolerate some degree of latency and jitter, such as multimedia, gaming, networking, etc.

## Examples of Real Time Kernels

Some of the examples of real time kernels are:

- **FreeRTOS**: A free and open source real time kernel that supports various architectures and platforms, and provides a rich set of features and APIs.
- **Linux-rt**: A patch set that modifies the standard Linux kernel to make it more suitable for real time applications, by reducing the latency and improving the responsiveness of the kernel.
- **VxWorks**: A commercial real time kernel that is widely used in embedded and industrial systems, and offers high performance, scalability, and security.



# OS Tasks for Embedded Systems

- An **embedded system** is a computer that supports a machine and performs one specific task in the bigger machine .
- An **embedded operating system** is a specialized OS that runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS  .
- An **OS task** (also called a process or a thread) is a unit of execution that encapsulates all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc. .
- A **real-time kernel** is a type of embedded OS that guarantees a certain capability within a specified time constraint, such as responding to an event within a fixed amount of time.
- Some of the basic concepts and functions of a real-time kernel are:
  - **Task creation and deletion**: The kernel can create and delete tasks dynamically, depending on the application requirements. Each task has a unique identifier, a priority, and a set of attributes that define its behavior .
  - **Task scheduling and dispatching**: The kernel can decide which task to run next, based on the task priorities and the scheduling algorithm. The kernel can also switch from one task to another, saving and restoring the task context .
  - **Task synchronization and communication**: The kernel can provide mechanisms for tasks to coordinate their actions and exchange data, such as semaphores, mutexes, message queues, event flags, etc. .
  - **Task management and monitoring**: The kernel can provide functions for tasks to query and modify their own or other tasks' attributes, such as status, priority, stack usage, etc. The kernel can also detect and handle task errors, such as deadlock, overflow, etc. .
  - **Interrupt handling and timing services**: The kernel can handle hardware and software interrupts, and provide services for tasks to measure and control time, such as timers, delays, timeouts, etc. .



# Task States for the Notes of the Unit 3 - Real Time Kernel Basics

- A task is a basic unit of execution in a real time operating system (RTOS).
- A task can have different states depending on its current status and priority.
- The fundamental task states are:
  - **Current**: The task that is currently running on the processor. Only one task can be in this state at any time.
  - **Ready**: The task that is ready to run but is waiting for the processor to be available. A task can become ready when it is created, resumed, or unblocked by an event. A ready task can preempt a lower priority current task if the RTOS supports preemption.
  - **Suspended**: The task that is temporarily stopped from running and is not eligible for scheduling. A task can become suspended when it is explicitly paused by the application or the RTOS. A suspended task can be resumed by the application or the RTOS.
  - **Blocked**: The task that is waiting for an event to occur, such as a timer, a semaphore, a message, or an interrupt. A task can become blocked when it explicitly requests an event or a resource that is not available. A blocked task can be unblocked by the occurrence of the event or the availability of the resource.
- Some RTOS may have additional task states, such as :
  - **Zombie**: The task that has terminated its execution but has not been deleted by the RTOS. A zombie task can be deleted by the RTOS or the application.
  - **Interruptible**: The task that is running in kernel space and can be interrupted by a higher priority task or an interrupt. An interruptible task can resume its execution after the interruption is handled.
  - **Uninterruptible**: The task that is running in kernel space and cannot be interrupted by any other task or interrupt. An uninterruptible task can only be preempted by a non-maskable interrupt (NMI) or a system reset. An uninterruptible task should finish its execution as soon as possible to avoid blocking the system.
- The task state can be represented by a state diagram, such as the following:

Task State Diagram

- The task state can be changed by the RTOS scheduler, which is responsible for selecting the next task to run based on the task priority, the task state, and the system events.
- The task state can also be changed by the task itself, which can perform various operations, such as:
  - **Create**: The task can create a new task with a specified priority and parameters. The new task can be in ready or suspended state depending on the RTOS configuration.
  - **Delete**: The task can delete itself or another task. The deleted task can be in zombie state until it is removed by the RTOS.
  - **Suspend**: The task can suspend itself or another task. The suspended task can be resumed by the task or the RTOS.
  - **Resume**: The task can resume a suspended task. The resumed task can be in ready or blocked state depending on the RTOS configuration and the events.
  - **Yield**: The task can voluntarily relinquish the processor to allow another ready task to run. The yielded task can be in ready state until it is scheduled again by the RTOS.
  - **Delay**: The task can delay its execution for a specified amount of time. The delayed task can be in blocked state until the time expires or it is unblocked by the RTOS or an event.
  - **Wait**: The task can wait for an event or a resource to occur or become available. The waiting task can be in blocked state until the event or the resource is available or it is unblocked by the RTOS or another event.
  - **Signal**: The task can signal an event or a resource to another task or the RTOS. The signaling task can be in current or ready state depending on the RTOS configuration and the events. The signaled task can be in ready or blocked state depending on the RTOS configuration and the events.



# Task scheduling for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Task scheduling is the process of determining how the various tasks are executed by the operating system in a real time system .
- A real time system is a system that has to respond to events within a specified time constraint.
- A real time operating system (RTOS) is an operating system that can guarantee the timely execution of tasks in a real time system.
- A task is a unit of work that can be executed by the RTOS. A task can be periodic, aperiodic, or sporadic .
  - A periodic task is a task that has to be executed at regular intervals of time .
  - An aperiodic task is a task that has no fixed arrival time or deadline .
  - A sporadic task is a task that has a minimum inter-arrival time between successive instances .
- A task can also be classified as hard, soft, or firm .
  - A hard task is a task that has to meet its deadline, otherwise the system may fail .
  - A soft task is a task that can tolerate some degree of deadline miss, but the quality of service may degrade .
  - A firm task is a task that has no value if it misses its deadline, but does not affect the system's correctness .
- A task can have different attributes, such as arrival time, execution time, deadline, priority, resource requirements, and precedence constraints .
  - The arrival time of a task is the time when the task becomes ready for execution .
  - The execution time of a task is the time required by the task to complete its work .
  - The deadline of a task is the time by which the task has to finish its execution .
  - The priority of a task is a measure of its importance or urgency .
  - The resource requirements of a task are the resources that the task needs to access during its execution, such as CPU, memory, I/O devices, etc .
  - The precedence constraints of a task are the dependencies that the task has on other tasks, such as data or control flow .
- A task scheduler is a component of the RTOS that decides which task to run at any given time  .
- A task scheduler can use different algorithms or policies to make the scheduling decision, such as run to completion, round robin, time slice, priority, etc  .
  - A run to completion scheduler is a very simple scheduler that runs each task until it finishes or blocks.
  - A round robin scheduler is a scheduler that runs each task in sequence for a fixed amount of time, and then switches to the next task in a circular order .
  - A time slice scheduler is a scheduler that runs each task in sequence for a variable amount of time, depending on the task's priority or deadline .
  - A priority scheduler is a scheduler that runs the task with the highest priority at any given time .
- A task scheduler can also be classified as preemptive or non-preemptive .
  - A preemptive scheduler is a scheduler that can interrupt a running task and switch to another task if a higher priority or more urgent task arrives .
  - A non-preemptive scheduler is a scheduler that cannot interrupt a running task and has to wait until the task finishes or blocks before switching to another task .
- A task scheduler has to ensure that the tasks meet their deadlines and resource requirements, while maximizing the system's performance and efficiency .
- A task scheduler has to deal with various challenges and trade-offs, such as overhead



# Interrupt Processing

- Interrupts are signals that notify the CPU of an event that requires its attention.
- Interrupts can be generated by hardware devices, such as timers, keyboards, network cards, etc., or by software, such as system calls, exceptions, etc.
- Interrupts are essential for real-time systems, as they allow the system to respond quickly and predictably to external stimuli.
- Interrupts can also pose challenges for real-time systems, as they can interfere with the execution of critical tasks and introduce latency and jitter.
- Therefore, real-time kernels need to handle interrupts efficiently and effectively, while ensuring the correctness and timeliness of the system.

## Interrupt Handling Methods

- There are different methods for handling interrupts in real-time kernels, depending on the design and architecture of the kernel and the hardware platform.
- Some of the common methods are:

  - **Polling**: The kernel periodically checks a status register or a memory location to see if any interrupt has occurred. This method is simple and deterministic, but it wastes CPU cycles and introduces latency.
  - **Vectored**: The kernel uses a table of pointers to interrupt service routines (ISRs), which are invoked directly by the hardware when an interrupt occurs. This method is fast and efficient, but it requires a fixed number of interrupt vectors and may not support nested interrupts.
  - **Daisy-chaining**: The kernel uses a chain of interrupt controllers, each of which can handle a subset of interrupts. When an interrupt occurs, the controllers pass the interrupt signal along the chain until it reaches the appropriate controller, which then invokes the ISR. This method is flexible and scalable, but it adds complexity and overhead.
  - **Prioritized**: The kernel assigns a priority level to each interrupt source, and uses a priority encoder or a comparator to determine which interrupt has the highest priority. The kernel then invokes the ISR for the highest-priority interrupt, and masks or defers the lower-priority interrupts. This method is responsive and predictable, but it may cause starvation or deadlock for low-priority interrupts.

## Interrupt Processing Steps

- The typical steps involved in processing an interrupt in a real-time kernel are:

  - **Detection**: The hardware detects the occurrence of an interrupt and sends a signal to the CPU.
  - **Acknowledgement**: The CPU acknowledges the interrupt signal and suspends the current execution context (task or ISR).
  - **Identification**: The CPU identifies the source and type of the interrupt, and retrieves the address of the corresponding ISR from the interrupt vector table or the interrupt controller.
  - **Dispatching**: The CPU saves the current state of the registers and the program counter, and jumps to the ISR address.
  - **Servicing**: The ISR performs the necessary actions to handle the interrupt, such as reading or writing data, sending or receiving signals, clearing flags, etc.
  - **Termination**: The ISR returns control to the CPU by executing a return from interrupt instruction, which restores the previous state of the registers and the program counter.
  - **Resumption**: The CPU resumes the execution of the suspended context, or switches to a different context if a higher-priority task or ISR is ready to run.

## Interrupt Processing Challenges

- Some of the challenges that interrupt processing poses for real-time kernels are:

  - **Latency**: The time between the occurrence of an interrupt and the start of the ISR execution. Latency depends on factors such as the hardware architecture, the interrupt handling method, the interrupt priority, the interrupt nesting, the interrupt masking, the context switching, etc. Latency affects the responsiveness and accuracy of the system, and should be minimized and bounded.
  - **Jitter**: The variation in the latency of interrupt processing. Jitter depends on factors such as the interrupt frequency, the interrupt load, the interrupt interference, the interrupt synchronization, the interrupt scheduling, etc. Jitter affects the stability and quality of the system, and should be reduced and controlled.
  - **Overhead**: The CPU time and memory space consumed by the interrupt processing. Overhead depends on factors such as the interrupt handling method, the interrupt processing steps, the interrupt service routines, the interrupt context switching, the interrupt synchronization, etc. Overhead affects the performance and efficiency of the system, and should be optimized and balanced.
  - **Correctness**: The preservation of the functional and temporal properties of the system during and after the interrupt processing. Correctness depends on factors such as the interrupt priority, the interrupt nesting, the interrupt masking, the interrupt synchronization, the interrupt scheduling, the interrupt service routines, etc. Correctness affects the reliability and safety of the system, and should be ensured and verified.



# Clocking

Clocking is the process of measuring and synchronizing the passage of time in a real time kernel. Clocking is essential for scheduling, timing, and performance analysis of real time systems. There are two main types of clocks in a real time kernel:

- **Hardware clock**: This is a battery-backed device that keeps track of the wall clock time (the date and time of the real world) even when the system is powered off. The hardware clock is usually initialized by the BIOS or the bootloader, and can be accessed by the kernel or the user space applications. The hardware clock is also known as the Real Time Clock (RTC), the CMOS clock, or the BIOS clock .
- **Software clock**: This is a virtual device that keeps track of the elapsed time since the system was booted. The software clock is maintained by the kernel using timer interrupts or other sources of time information. The software clock is also known as the system clock, the kernel clock, or the monotonic clock .

The software clock and the hardware clock may have different resolutions, accuracies, and drifts. The software clock may also be affected by system load, frequency scaling, or clock adjustments. Therefore, the kernel may need to synchronize the software clock with the hardware clock periodically, or use other methods to improve the software clock's quality. The kernel may also provide different interfaces for accessing the software clock, such as:

- **CLOCK_REALTIME**: This is a software clock that represents the wall clock time. It can be set or adjusted by the user space applications or the kernel. It may be affected by time zone changes, daylight saving time changes, or leap seconds .
- **CLOCK_MONOTONIC**: This is a software clock that represents the elapsed time since an unspecified point in the past. It cannot be set or adjusted by the user space applications or the kernel. It is not affected by time zone changes, daylight saving time changes, or leap seconds. It is suitable for measuring intervals or durations .
- **CLOCK_REALTIME_HR**: This is a high resolution version of CLOCK_REALTIME. It may have a finer granularity than CLOCK_REALTIME, but it may also have a higher overhead or a lower availability.
- **CLOCK_MONOTONIC_HR**: This is a high resolution version of CLOCK_MONOTONIC. It may have a finer granularity than CLOCK_MONOTONIC, but it may also have a higher overhead or a lower availability.

The kernel may also provide other types of software clocks for specific purposes, such as:

- **CLOCK_PROCESS_CPUTIME_ID**: This is a software clock that measures the CPU time consumed by a process.
- **CLOCK_THREAD_CPUTIME_ID**: This is a software clock that measures the CPU time consumed by a thread.
- **CLOCK_BOOTTIME**: This is a software clock that represents the elapsed time since the system was booted, including the time spent in suspend or hibernation.
- **CLOCK_TAI**: This is a software clock that represents the International Atomic Time, which is a continuous and uniform time scale that does not have leap seconds.

The kernel provides various system calls and functions for accessing and manipulating the software clocks, such as:

- **clock_gettime()**: This function returns the current value of a specified software clock.
- **clock_settime()**: This function sets the current value of a specified software clock.
- **clock_getres()**: This function returns the resolution of a specified software clock.
- **clock_nanosleep()**: This function suspends the execution of the calling thread until a specified software clock reaches a certain value or a certain amount of time has passed.
- **clock_adjtime()**: This function adjusts the frequency or the offset of a specified software clock.
- **timer_create()**: This function creates a timer object that is associated with a specified software clock.
- **timer_settime()**: This function sets the expiration time and the interval of a timer object.
- **timer_gettime()**: This function returns the remaining time and the interval of a timer object.
- **timer_delete()**: This function deletes a timer object.
- **timer_getoverrun()**: This function returns the number of times a timer object has expired without being serviced.

The kernel may also provide other mechanisms for accessing and manipulating the software clocks, such as:

- **/proc/sys/kernel/hz**: This file contains the value of the kernel timer frequency, which is the number



# Communication and Synchronization

- Communication and synchronization are essential aspects of real-time kernel design and implementation, as they enable the coordination and cooperation of multiple tasks that share resources and data.
- Communication and synchronization mechanisms can be classified into two categories: message passing and shared memory.
- Message passing is a communication method that involves sending and receiving messages between tasks, either directly or through a message queue. Message passing can be synchronous or asynchronous, depending on whether the sender and receiver wait for each other or not.
- Shared memory is a communication method that involves accessing a common memory region by multiple tasks, either directly or through a semaphore. Shared memory can be faster than message passing, but requires careful synchronization to avoid data inconsistency and race conditions.
- Synchronization mechanisms are used to ensure that the communication between tasks is consistent and reliable, preventing data corruption, deadlock, or race conditions. Synchronization mechanisms can be classified into two categories: mutual exclusion and condition synchronization.
- Mutual exclusion is a synchronization method that ensures that only one task can access a shared resource at a time, protecting critical sections of code or data structures. Mutual exclusion can be implemented using mutexes, spinlocks, or monitors.
- Condition synchronization is a synchronization method that allows a task to wait for a certain condition to be satisfied before proceeding, or to signal other tasks that a condition has been met. Condition synchronization can be implemented using semaphores, events, or condition variables.



# Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures that store information about the processes or tasks in a real time kernel.
- A real time kernel is a software component that manages the execution of multiple tasks in a real time operating system (RTOS).
- A real time operating system is a system that can respond to events or inputs within a specified time constraint, such as in embedded systems or control systems.
- Some of the functions of a real time kernel are:
  - Task management: creating, terminating, scheduling, and prioritizing tasks.
  - Resource management: allocating and deallocating memory, I/O devices, and other resources to tasks.
  - Synchronization and communication: providing mechanisms for tasks to coordinate and exchange data, such as semaphores, message queues, and events.
  - Interrupt handling: servicing hardware or software interrupts and dispatching them to the appropriate tasks.
  - Timer management: providing services for tasks to measure time, set timeouts, and generate periodic events.

- A control block typically contains the following information about a task:
  - Task ID: a unique identifier for the task.
  - Task state: the current status of the task, such as running, ready, blocked, or terminated.
  - Task priority: the relative importance of the task, which affects its scheduling order.
  - Task context: the set of registers and memory locations that store the task's execution state, such as the program counter, the stack pointer, and the data segment.
  - Task resources: the list of resources that the task owns or requests, such as memory blocks, I/O devices, or semaphores.
  - Task attributes: the parameters that define the task's behavior, such as its deadline, period, or execution time.

- A control block is usually created by the kernel when a task is initialized, and is updated by the kernel during the task's lifetime. The control block is stored in a protected memory area that is inaccessible to the normal user. The kernel maintains a table or a list of all the control blocks in the system, and uses them to perform its functions.
- A control block is also known as a process control block (PCB) or a task control block (TCB) in some literature.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of memory requirements and control for the real time kernel.

# Memory requirements and control for the real time kernel

- A real time kernel is a special type of kernel that can handle time-critical tasks with minimal latency and predictable performance.
- A real time kernel has to manage the memory resources of the system efficiently and safely, as memory access is one of the main sources of latency and unpredictability.
- A real time kernel has to perform the following memory management functions:
  - Virtual addressing: This is the process of mapping the logical addresses used by the processes to the physical addresses of the memory. This can be done by paging or segmentation. Paging divides the memory into fixed-size blocks called pages, while segmentation divides the memory into variable-size segments. Paging is more commonly used in modern systems, as it reduces external fragmentation and simplifies memory allocation and protection. 
  - Memory allocation: This is the process of assigning memory to the processes that request it. A real time kernel has to allocate memory in a way that minimizes the overhead and the fragmentation of the memory. Fragmentation occurs when the memory is divided into small and non-contiguous chunks that cannot be used efficiently. A real time kernel can use different memory allocation algorithms, such as first fit, best fit, worst fit, buddy system, etc. 
  - Memory protection: This is the process of preventing unauthorized or erroneous access to the memory by the processes. A real time kernel has to ensure that each process can only access its own memory space and that the kernel memory is protected from the user processes. This can be done by using hardware mechanisms, such as page tables, page frames, page faults, etc. 
  - Memory sharing: This is the process of allowing multiple processes to access the same memory region for communication or efficiency purposes. A real time kernel has to ensure that the memory sharing does not compromise the isolation and the integrity of the processes. This can be done by using mechanisms, such as shared memory, memory mapping, copy-on-write, etc. 
  - Memory swapping: This is the process of moving some memory pages or segments from the main memory to the secondary storage, such as disk, when the main memory is full or low. This can free up some memory space for the active processes, but it can also introduce significant latency and unpredictability, as the swapped pages or segments have to be brought back to the main memory when they are needed. A real time kernel has to minimize the use of memory swapping and use it only as a last resort. This can be done by using mechanisms, such as priority-based swapping, working set model, etc. 
- A real time kernel can also use some techniques to improve the memory performance and reduce the latency, such as:
  - Hugepages: These are large memory pages that can reduce the number of page table entries and page faults, and thus improve the memory access speed. A real time kernel can reserve some memory for hugepages and allow the processes to use them for their critical tasks. 
  - Real-time scheduling: This is the process of assigning CPU time to the processes based on their priority and deadlines. A real time kernel can allow the processes to run with real-time scheduling policy, which can reduce the context switches and the preemption overhead, and thus improve the memory performance. 
  - Kernel tuning: This is the process of adjusting the kernel parameters and settings to optimize the system performance for the specific workload and environment. A real time kernel can be tuned to reduce the latency and increase the predictability, by using mechanisms, such as isolating CPUs, disabling interrupts, reducing kernel timers, etc.



# Kernel Services

The kernel is the core component of an operating system that provides basic services for all other parts of the OS. It is the main layer between the OS and the underlying hardware, and it helps with tasks such as process and memory management, file systems, device control and networking.

A real-time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints. An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities. An RTOS must provide its services within strict time deadlines to its users and to the surrounding world to which they interface.

A micro-kernel architecture is typically implemented in an RTOS with configurable functionalities. A micro-kernel is a small, highly optimized set of libraries that provides the minimal functionality required by an RTOS. A micro-kernel offers an abstraction layer that provides six main types of common services to the application software. They are:

- **Task management**: This service allows the creation, deletion, and control of tasks, which are the basic units of execution in an RTOS. A task can have attributes such as priority, state, stack size, and entry point.
- **Task scheduling**: This service determines which task should run next based on the task priority, state, and timing requirements. A task scheduler can be preemptive, which means that a higher priority task can interrupt a lower priority task, or cooperative, which means that a task can only be switched when it voluntarily yields the CPU.
- **Task synchronization**: This service enables the coordination and communication among tasks that share data or resources. A task synchronization mechanism can be a semaphore, a mutex, a message queue, an event flag, or a mailbox.
- **Memory management**: This service allocates and deallocates memory for tasks and data structures. A memory management mechanism can be static, which means that the memory is allocated at compile time, or dynamic, which means that the memory is allocated at run time.
- **Time management**: This service provides the ability to measure and control the time in an RTOS. A time management mechanism can be a timer, a clock, a delay, or a timeout.
- **Interrupt handling**: This service handles the external or internal events that occur asynchronously and require immediate attention. An interrupt handler is a special function that is executed when an interrupt occurs and performs the necessary actions to service the interrupt.
- **Device I/O management**: This service manages the input and output operations of the devices that are connected to the RTOS. A device I/O management mechanism can be a device driver, a device controller, or a device interface.

These are the kernel services that are essential for the functioning of an RTOS. They provide the foundation for the development of real-time and embedded applications that have strict timing and performance requirements.



# Basic Design using RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system; it creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides a multi-tasking and deterministic run-time environment, which means that tasks can be executed in a predictable and timely manner.
- An RTOS can be used to design embedded systems that have real-time constraints, such as deadlines, response times, or throughput requirements.
- Some basic design principles using RTOS are:

  - Write short interrupt routines, but not too short. Short interrupt routines reduce the latency and overhead of interrupt handling, but too short routines may not perform the necessary actions or may miss some events.
  - Use a large number of tasks, but not too many. A large number of tasks can improve the control of the priorities and the relative response times, as well as the modularity and the encapsulation of data. However, too many tasks can increase the data sharing, the semaphores, the message passing, and the bugs, as well as the time spent on handling them.
  - Avoid creating and destroying tasks while the system is running, because it is time consuming, it may be difficult to destroy a task without leaving something behind, and it may be better to create all the tasks at system startup and leave them.
  - Use RMS to verify your design. RMS, or Rate Monotonic Scheduling, is an analysis technique that designers can use to test their assumptions about whether the tasks in their system can be scheduled successfully. RMS assigns priorities to tasks based on their periods, and guarantees that all tasks will meet their deadlines if the CPU utilization is below a certain threshold.
  - Use the RTOS features and services appropriately. RTOS provides various features and services, such as timers, queues, semaphores, mutexes, event flags, mailboxes, etc. These features and services can simplify the design and implementation of the system, but they also have some costs and limitations. Designers should use them wisely and avoid overusing or misusing them.



# Unit 4 - VxWorks / FreeRTOS

VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems. They differ in many aspects, such as cost, features, support, and performance. Here is a brief comparison of the two RTOSes based on the information from the web search results    :

- **Cost**: VxWorks is a commercial RTOS that requires a license fee, while FreeRTOS is an open-source RTOS that is free to use and modify. However, FreeRTOS also offers a paid version called Amazon FreeRTOS that provides additional features and cloud integration.
- **Features**: VxWorks supports a wide range of features, such as multicore and SMP support, memory protection, POSIX compliance, networking, security, file system, graphics, and more. FreeRTOS is a simpler and more portable RTOS that provides basic features, such as preemptive and cooperative scheduling, inter-task communication, timers, queues, semaphores, mutexes, and event groups. Amazon FreeRTOS adds features such as OTA updates, MQTT, TLS, and AWS IoT integration.
- **Support**: VxWorks is backed by a professional company called Wind River that provides technical support, documentation, training, and consulting services. FreeRTOS is supported by a large community of developers and users, as well as by Amazon for the paid version. FreeRTOS also has a website that provides documentation, tutorials, and forums.
- **Performance**: VxWorks is known for its high performance, reliability, and scalability. It can handle complex and demanding applications, such as aerospace, defense, industrial, and automotive systems. FreeRTOS is designed for low-power and resource-constrained devices, such as microcontrollers and IoT devices. It has a small footprint and low overhead, but it may not be suitable for applications that require high performance, determinism, or advanced features.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on VxWorks/ Free RTOS Scheduling and Task Management for the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

# VxWorks/ Free RTOS Scheduling and Task Management

- VxWorks is a real-time operating system (RTOS) that provides a basic multitasking environment for embedded systems.
- Free RTOS is an open source RTOS that supports multiple architectures and platforms.
- Both VxWorks and Free RTOS use priority-based preemptive scheduling, which means that the scheduler runs the highest priority task that is ready to execute and preempts lower priority tasks if a higher priority task becomes ready .
- Both VxWorks and Free RTOS also support round-robin scheduling, which means that tasks with the same priority are executed in a circular order for a fixed time slice .
- A task is a runnable unit of code that has a task control block (TCB), a unique task space, and a specific priority.
- A task can be in one of the following states: ready, running, blocked, suspended, or deleted.
- A task can be created, deleted, suspended, resumed, changed priority, or queried using various API functions provided by the RTOS.
- A task can communicate with other tasks using inter-task communication mechanisms such as message queues, semaphores, mutexes, event flags, pipes, signals, or shared memory .
- A task can also use timers, interrupts, memory management, and device drivers to interact with the hardware and the system resources .
- A task can be optimized for performance by using the rtmStepTask macro, which eliminates redundant scheduling calls during the execution of tasks in a multirate, multitasking model.



# Realtime scheduling for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Realtime scheduling is the process of assigning priorities and deadlines to tasks that need to execute on a system with real-time constraints, such as timeliness, predictability and responsiveness.
- A real-time operating system (RTOS) is a software platform that provides the core functionality for managing the tasks, resources and events of a real-time system.
- VXWORKS and FREE RTOS are two examples of RTOS that are widely used in embedded systems and real-time applications.

## VXWORKS

- VXWORKS is a commercial RTOS developed by Wind River Systems, Inc. It supports multiple architectures, such as x86, ARM, PowerPC and MIPS, and provides a rich set of features, such as networking, file system, security, graphics and device drivers.
- VXWORKS uses a preemptive priority-based scheduling algorithm, which means that the highest priority task that is ready to run will always preempt the lower priority tasks. The priority of a task can be static or dynamic, depending on the configuration.
- VXWORKS also supports various scheduling policies, such as round-robin, time-slice and deadline-based, which can be applied to tasks with the same priority level. These policies can help to balance the CPU utilization and the fairness among tasks.
- VXWORKS provides mechanisms to deal with priority inversion, which is a situation where a high priority task is blocked by a lower priority task that holds a shared resource. These mechanisms include priority inheritance, priority ceiling and mutexes.

## FREE RTOS

- FREE RTOS is an open source RTOS that is designed to be simple, portable and scalable. It supports many architectures, such as ARM, AVR, PIC and MSP430, and can run on bare metal or with a minimal hardware abstraction layer (HAL).
- FREE RTOS also uses a preemptive priority-based scheduling algorithm, but it has a simpler and smaller kernel than VXWORKS. It only provides the core real-time scheduling features, inter-task communication, and timing and synchronization primitives. Additional features, such as networking, file system and command console, can be added as optional components.
- FREE RTOS allows the user to assign a priority to each task, and the scheduler will always run the highest priority task that is ready. The priority of a task can be changed at run time, but it is not recommended to do so frequently, as it may affect the system performance and determinism.
- FREE RTOS does not support different scheduling policies for tasks with the same priority level, but it does provide a special idle task that will execute only when there are no other tasks able to run. The idle task can be used to perform low priority or background activities, such as power saving or garbage collection.
- FREE RTOS also provides mechanisms to deal with priority inversion, such as priority inheritance and mutexes. However, it does not support priority ceiling, which is a technique to assign the highest priority of all the tasks that may access a shared resource to the resource itself.



# Task Creation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A real-time operating system (RTOS) is a software platform that provides predictable and deterministic behavior for embedded systems that have strict timing and performance requirements .
- An RTOS typically consists of a kernel, which manages the tasks and resources of the system, and optional middleware components, such as file systems, networking stacks, graphics libraries, etc .
- An RTOS can be classified into two types: hard real-time and soft real-time. A hard real-time system guarantees that all deadlines are met, while a soft real-time system allows some deadlines to be missed occasionally.
- VxWorks and FreeRTOS are two popular RTOSs for embedded systems. They have different features, advantages, and disadvantages, which will be discussed in the following sections.

## VxWorks

- VxWorks is a preemptive, deterministic RTOS that prioritizes real-time embedded applications. It has low latency and minimal jitter .
- VxWorks has many security features that address the evolving security threats connected devices face at every stage, from boot-up to operation to data transfer to powered off .
- VxWorks supports a wide range of hardware architectures, such as ARM, Intel, PowerPC, MIPS, etc., and provides a rich set of middleware components, such as POSIX, TCP/IP, USB, Bluetooth, etc .
- VxWorks is based on a modular and scalable architecture that allows developers to choose the components they need and upgrade them as needed. It also supports a modern approach to development, such as C/C++, Java, Python, etc .
- VxWorks is used in many mission-critical embedded systems, such as aerospace, defense, industrial, medical, automotive, etc .
- Some of the advantages of VxWorks are:

  - It has a proven track record of reliability, performance, and security in demanding environments .
  - It offers a comprehensive and integrated development environment, called Wind River Workbench, that simplifies the design, development, debugging, and testing of embedded applications .
  - It supports multicore and heterogeneous systems, as well as virtualization and container technologies, that enable the consolidation of multiple workloads on a single device .
  - It provides a flexible and open platform that can interoperate with other operating systems, such as Linux, Android, Windows, etc .

- Some of the disadvantages of VxWorks are:

  - It is a proprietary and expensive RTOS that requires a license fee and a maintenance fee.
  - It has a steep learning curve and requires specialized skills and knowledge to use effectively.
  - It may not support some of the latest hardware and software technologies, such as IoT, cloud, AI, etc.

## FreeRTOS

- FreeRTOS is a free and open source RTOS that is designed to be simple, small, and portable. It is suitable for microcontrollers and small embedded systems.
- FreeRTOS supports preemptive and cooperative multitasking, as well as inter-task communication and synchronization mechanisms, such as queues, semaphores, mutexes, etc.
- FreeRTOS supports many hardware architectures, such as ARM, AVR, PIC, MSP430, etc., and provides a minimal set of middleware components, such as TCP/IP, USB, FAT, etc.
- FreeRTOS is based on a kernel-only approach that allows developers to customize and extend the functionality of the system as needed. It also supports a variety of development tools, such as GCC, IAR, Keil, etc.
- FreeRTOS is used in many low-cost and low-power embedded systems, such as IoT, consumer electronics, education, hobby, etc.
- Some of the advantages of FreeRTOS are:

  - It is a free and open source RTOS that does not require any license fee or maintenance fee.
  - It is a simple and lightweight RTOS that can run on resource-constrained devices with minimal memory and CPU overhead.
  - It is a portable and flexible RTOS that can be



# Intertask Communication

- Intertask communication is the process of exchanging data or signals between tasks or threads in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources, data or events.
- Intertask communication can also be used to implement task synchronization and mutual exclusion, which are mechanisms to ensure the correct and consistent execution of tasks in a concurrent system.
- Different RTOSs may provide different methods or primitives for intertask communication, such as shared memory, message queues, pipes, semaphores, mutexes, events, signals, etc.
- In this unit, we will focus on two popular RTOSs: VxWorks and FreeRTOS, and compare their intertask communication methods and performance.

## VxWorks Intertask Communication

- VxWorks is a commercial RTOS developed by Wind River Systems, widely used in embedded systems such as aerospace, defense, industrial and automotive applications.
- VxWorks supports several methods for intertask communication , such as:

  - **Shared memory**: A region of memory that can be accessed by multiple tasks. Shared memory is the fastest and simplest way of intertask communication, but it requires explicit synchronization and mutual exclusion mechanisms to avoid data corruption or inconsistency. VxWorks provides semaphores, mutexes and spin locks for this purpose.
  - **Message queues**: A data structure that stores messages in a FIFO (first-in, first-out) order. Message queues allow tasks to send and receive messages of fixed or variable size, with optional priority and timeout parameters. Message queues are thread-safe and can be used for both synchronous and asynchronous communication. VxWorks provides the msgQ API for creating and manipulating message queues.
  - **Pipes**: A special type of message queue that can be accessed by tasks using standard I/O functions, such as read and write. Pipes are useful for transferring streams of data between tasks, such as audio or video data. VxWorks provides the pipeDev API for creating and manipulating pipes.
  - **Events**: A mechanism that allows tasks to signal or wait for the occurrence of one or more events. Events are represented by bits in a 32-bit or 64-bit event flag. Tasks can set, clear, send, receive or test event flags using the eventLib API. Events can be used for both synchronous and asynchronous communication, and can also be triggered by interrupts or timers.
  - **Signals**: A mechanism that allows tasks to send or receive signals, which are predefined integers that represent various types of events or conditions. Signals are similar to events, but they are handled by the task's signal handler function, which can perform actions such as terminating the task, suspending the task, or ignoring the signal. VxWorks provides the sigLib API for creating and manipulating signals.

## FreeRTOS Intertask Communication

- FreeRTOS is a free and open source RTOS developed by Real Time Engineers Ltd, widely used in embedded systems such as microcontrollers, IoT devices, and low-power applications.
- FreeRTOS was designed to have a small ROM footprint and high portability. To this end, all intertask communication mechanisms are built around a single queue primitive , such as:

  - **Queues**: A data structure that stores items in a FIFO order. Queues allow tasks to send and receive items of fixed size, with optional priority and timeout parameters. Queues are thread-safe and can be used for both synchronous and asynchronous communication. FreeRTOS provides the xQueue API for creating and manipulating queues.
  - **Mutexes**: A special type of queue that can be used to implement mutual exclusion between tasks that share a resource. Mutexes are similar to binary semaphores, but they have additional features such as priority inheritance and recursive locking. FreeRTOS provides the xSemaphore API for creating and manipulating mutexes.
  - **Binary semaphores**: A special type of queue that can be used to implement synchronization between tasks or between tasks and interrupts. Binary semaphores have only two states: available or taken. Tasks can take or give binary semaphores using the xSemaphore API. Binary semaphores can also be used as binary flags or signals.
  - **Counting semaphores**: A special type of queue that can be used to implement synchronization between tasks or between tasks and interrupts. Counting semaphores have a positive integer value that represents the number of available resources or events. Tasks can take or give counting semaphores using the xSemaphore API. Counting semaphores can also be used as



# Pipes for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two processes in a unidirectional or bidirectional way.
- Pipes are often implemented as circular buffers or queues that can store a fixed amount of data in memory.
- Pipes can be used to implement producer-consumer patterns, where one process writes data to the pipe and another process reads data from the pipe.
- Pipes can also be used to implement filters, where one process reads data from a pipe, performs some transformation on it, and writes the result to another pipe.
- Pipes can be either named or unnamed. Named pipes have a unique identifier that can be used by any process to access the pipe. Unnamed pipes are created by a parent process and inherited by its child processes.
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available or no space to write.
- Pipes can have different modes of operation, such as byte-stream mode, message mode, or record mode. Byte-stream mode treats the data as a continuous stream of bytes, while message mode and record mode preserve the boundaries of the data units written to the pipe.

## Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that is widely used in embedded systems and critical infrastructure sectors.
- VxWorks supports pipes as a form of IPC, along with other mechanisms such as message queues, semaphores, shared memory, and sockets.
- VxWorks pipes are implemented as message queues with a fixed message size of one byte. This means that pipes in VxWorks can only operate in byte-stream mode.
- VxWorks pipes can be created by using the pipeDevCreate() function, which takes the name of the pipe, the maximum number of bytes that can be stored in the pipe, and the options for the pipe as arguments.
- VxWorks pipes can be accessed by using the open(), close(), read(), and write() functions, which are similar to the standard POSIX functions for file operations.
- VxWorks pipes can be configured to be blocking or non-blocking by using the O_NONBLOCK option in the open() function. By default, pipes are blocking in VxWorks.
- VxWorks pipes can also be configured to be bidirectional by using the O_RDWR option in the open() function. By default, pipes are unidirectional in VxWorks.
- VxWorks pipes can be deleted by using the pipeDevDelete() function, which takes the name of the pipe and a boolean flag to indicate whether to force the deletion or not as arguments.

## Pipes in FreeRTOS

- FreeRTOS is another RTOS that is widely used in embedded systems and IoT devices.
- FreeRTOS does not support pipes as a native form of IPC, but it provides a similar mechanism called stream buffers.
- Stream buffers are circular buffers that can store a variable amount of data in memory. They can be used to implement pipes, UARTs, TCP/IP stacks, and other communication protocols.
- Stream buffers can be created by using the xStreamBufferCreate() function, which takes the size of the buffer and the trigger level as arguments. The trigger level is the minimum amount of data that must be in the buffer before a task that is blocked on the buffer is unblocked.
- Stream buffers can be accessed by using the xStreamBufferSend() and xStreamBufferReceive() functions, which take the handle of the buffer, a pointer to the data, the size of the data, and a timeout value as arguments.
- Stream buffers can be configured to be blocking or non-blocking by using the portMAX_DELAY or 0 as the timeout value in the xStreamBufferSend() and xStreamBufferReceive() functions. By default, stream buffers are blocking in FreeRTOS.
- Stream buffers can also be configured to operate in byte-stream mode or message mode by using the xStreamBufferCreateStatic() or xStreamBufferCreateStaticMessage() functions, respectively. In message mode, the stream buffer preserves the boundaries of the data units written to the buffer.
- Stream buffers can be deleted by using the vStreamBufferDelete() function, which takes the handle of the buffer as an argument.



# Semaphore for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have two states: available or unavailable. A thread or process can acquire a semaphore if it is available, and release it when it is done with the shared resource.
- A semaphore can be binary or counting. A binary semaphore can only have two values: 0 or 1. A counting semaphore can have any non-negative value, and it represents the number of available resources.
- In FreeRTOS, semaphores are built on queues. A queue is a data structure that stores items in a first-in, first-out (FIFO) order. A queue can be used to pass messages or data between tasks, or to synchronize tasks.
- A semaphore is implemented as a queue with a length of one. The queue item is either empty or full, corresponding to the semaphore state. A task can acquire a semaphore by receiving an item from the queue, and release a semaphore by sending an item to the queue.
- FreeRTOS provides several API functions to create and manipulate semaphores. Some of the most common ones are:

  - `xSemaphoreCreateBinary()` creates a binary semaphore and returns a handle to it.
  - `xSemaphoreTake()` tries to acquire a semaphore by receiving an item from the queue. It can block the calling task until the semaphore is available or a timeout expires.
  - `xSemaphoreGive()` releases a semaphore by sending an item to the queue. It can unblock a task that is waiting for the semaphore.
  - `xSemaphoreGiveFromISR()` is a special version of `xSemaphoreGive()` that can be called from an interrupt service routine (ISR). It can also trigger a context switch if a higher priority task is unblocked by the semaphore.

- A mutex is a special type of binary semaphore that can be used to implement mutual exclusion. Mutual exclusion means that only one task can access a shared resource at a time, and other tasks have to wait until the resource is released.
- A mutex has two additional features compared to a binary semaphore:

  - A mutex has a priority inheritance mechanism that can prevent priority inversion. Priority inversion occurs when a higher priority task is blocked by a lower priority task that holds a mutex. The priority inheritance mechanism temporarily boosts the priority of the lower priority task to match the highest priority task that is waiting for the mutex.
  - A mutex can be recursive, meaning that the same task can acquire the same mutex multiple times without blocking itself. The task has to release the mutex the same number of times it acquired it before the mutex is available to other tasks.

- FreeRTOS provides several API functions to create and manipulate mutexes. Some of the most common ones are:

  - `xSemaphoreCreateMutex()` creates a mutex and returns a handle to it.
  - `xSemaphoreCreateRecursiveMutex()` creates a recursive mutex and returns a handle to it.
  - `xSemaphoreTakeRecursive()` tries to acquire a recursive mutex by receiving an item from the queue. It can block the calling task until the mutex is available or a timeout expires.
  - `xSemaphoreGiveRecursive()` releases a recursive mutex by sending an item to the queue. It can unblock a task that is waiting for the mutex.

- In VXWorks, semaphores are also used to synchronize and protect access to shared resources. VXWorks provides several types of semaphores, such as binary, counting, mutual exclusion, and reader-writer semaphores.
- VXWorks also provides several API functions to create and manipulate semaphores. Some of the most common ones are:

  - `semBCreate()` creates a binary semaphore and returns an ID to it.
  - `semCCreate()` creates a counting semaphore and returns an ID to it.
  - `semMCreate()` creates a mutual exclusion semaphore and returns an ID to it.
  - `semTake()` tries to acquire a semaphore by decrementing its value. It can block the calling task until the semaphore is positive or a timeout expires.
  - `semGive()` releases a semaphore by incrementing its value. It can unblock a task that



# Message Queue for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A message queue is a data structure that stores messages between tasks or interrupts in a real-time operating system (RTOS).
- A message queue can be used to send data, signals, events, or commands from one task or interrupt to another, or to multiple recipients.
- A message queue can also be used to synchronize tasks or interrupts by blocking them until a message is available or a timeout occurs.
- A message queue has a fixed size and capacity, and can store messages of a fixed or variable length.
- A message queue can be created, deleted, sent to, received from, or peeked at using the RTOS API functions.
- A message queue can be accessed by tasks or interrupts with different priorities, and the RTOS scheduler can use the queue state to determine which task or interrupt to run next.
- A message queue can be configured to use different queueing policies, such as FIFO (first in, first out), LIFO (last in, first out), or priority-based.
- A message queue can be configured to use different notification mechanisms, such as callbacks, signals, semaphores, or events, to inform the sender or receiver of the queue status.

## VXWORKS Message Queue

- VXWORKS is a commercial RTOS that supports message queues as one of its intertask communication mechanisms.
- VXWORKS message queues are created using the msgQCreate function, which takes the following parameters:
  - maxMsgs: the maximum number of messages that can be stored in the queue
  - maxMsgLength: the maximum length of each message in bytes
  - options: a bitmask of options that control the queue behavior, such as queueing policy, notification mechanism, and message length mode
- VXWORKS message queues are deleted using the msgQDelete function, which takes the queue ID as a parameter and frees the memory allocated for the queue.
- VXWORKS message queues are sent to using the msgQSend function, which takes the following parameters:
  - msgQId: the queue ID returned by msgQCreate
  - buffer: a pointer to the message data to be sent
  - nBytes: the length of the message data in bytes
  - timeout: the maximum time to wait for the queue to have enough space, in ticks
  - priority: the priority of the message, used for priority-based queueing
- VXWORKS message queues are received from using the msgQReceive function, which takes the following parameters:
  - msgQId: the queue ID returned by msgQCreate
  - buffer: a pointer to the buffer where the message data will be copied
  - maxNBytes: the maximum length of the buffer in bytes
  - timeout: the maximum time to wait for the queue to have a message, in ticks
- VXWORKS message queues can be peeked at using the msgQNumMsgs function, which takes the queue ID as a parameter and returns the number of messages currently in the queue.
- VXWORKS message queues can be configured to use different notification mechanisms, such as callbacks, signals, semaphores, or events, to inform the sender or receiver of the queue status. For example, the MSG_Q_EVENT_SEND and MSG_Q_EVENT_RECEIVE options can be used to enable event-based notification, and the msgQEvRegister and msgQEvUnregister functions can be used to register and unregister event handlers for the queue.

## FREE RTOS Message Queue

- FREE RTOS is an open source RTOS that supports message queues as one of its intertask communication mechanisms.
- FREE RTOS message queues are created using the xQueueCreate function, which takes the following parameters:
  - uxQueueLength: the maximum number of messages that can be stored in the queue
  - uxItemSize: the size of each message in bytes
- FREE RTOS message queues are deleted using the vQueueDelete function, which takes the queue handle as a parameter and frees the memory allocated for the queue.
- FREE RTOS message queues are sent to using the xQueueSend or xQueueSendFromISR functions, which take the following parameters:
  - xQueue: the queue handle returned by xQueueCreate
  - pvItemToQueue: a pointer to the message data to be sent
  - xTicksToWait: the maximum time to wait for the queue to have enough space, in ticks
- FREE RTOS message queues are received from using the xQueue



# Signals for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Signals are a form of inter-process communication (IPC) that allow a process to send a notification to another process or to itself.
- Signals can be used to indicate events such as termination, segmentation fault, alarm, user input, etc.
- Signals can also be used to implement software interrupts, timers, and asynchronous I/O.
- Signals are not supported by FreeRTOS, but are supported by VxWorks.

## Signals in VxWorks

- VxWorks provides a signal API that is similar to the POSIX standard, but with some differences and limitations.
- VxWorks signals are associated with tasks, not processes. A task can send a signal to another task or to itself using the `kill()` function.
- VxWorks signals are delivered to tasks asynchronously, meaning that the signal handler is executed as soon as possible after the signal is sent, regardless of the current state of the task.
- VxWorks signals are not queued, meaning that only one instance of each signal can be pending for a task at any time. If a signal is sent to a task that already has that signal pending, the new signal is ignored.
- VxWorks signals have predefined numbers and names, such as `SIGINT`, `SIGSEGV`, `SIGALRM`, etc. The signal numbers range from 1 to 31, and the signal names are defined in the header file `signal.h`.
- VxWorks signals can be blocked, ignored, or handled by a task. A task can block or unblock signals using the `sigprocmask()` function, which manipulates the signal mask of the task. A task can ignore a signal by setting its handler to `SIG_IGN`, or handle a signal by setting its handler to a user-defined function using the `sigaction()` function.
- VxWorks signals can be used to implement software interrupts, timers, and asynchronous I/O. For example, a task can use the `sigqueue()` function to send a signal with a value to another task, which can then use the `sigwaitinfo()` function to receive the signal and the value. A task can also use the `timer_create()` and `timer_settime()` functions to create and start a timer that sends a signal to the task when it expires. A task can also use the `aio_read()` and `aio_write()` functions to perform asynchronous I/O operations that send a signal to the task when they are completed.

## Signals in FreeRTOS

- FreeRTOS does not support signals, but provides other mechanisms for inter-task communication and synchronization, such as queues, semaphores, mutexes, event groups, etc.
- FreeRTOS also provides software timers, which are similar to VxWorks timers, but do not use signals. A software timer is a special type of task that executes a callback function when it expires. A software timer can be created and started using the `xTimerCreate()` and `xTimerStart()` functions, respectively.
- FreeRTOS also provides interrupt service routines (ISRs), which are similar to VxWorks signal handlers, but are executed in response to hardware interrupts, not software signals. An ISR is a special type of function that is registered to handle a specific interrupt vector using the `vPortSetInterruptHandler()` function. An ISR can communicate with tasks using the `xQueueSendFromISR()` and `xSemaphoreGiveFromISR()` functions, which are designed to be safe to use from an ISR context.



# Sockets for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A socket is an endpoint of communication between two processes or devices over a network.
- Sockets can be used to send and receive data using different protocols, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that ensures data delivery and error recovery. UDP is an unreliable, connectionless protocol that does not guarantee data delivery or error recovery, but is faster and more efficient for some applications.
- Sockets can also be used to send and receive broadcast and multicast communications, which are both a form of one-to-many communications.
- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that support socket programming.
- VXWORKS is a proprietary, UNIX-like RTOS that is widely used in safety-critical and high-performance applications, such as aerospace, defense, industrial, and automotive systems.
- FREE RTOS is an open source, scalable, and thread-safe RTOS that is designed for small embedded systems with limited resources, such as microcontrollers.
- Both VXWORKS and FREE RTOS provide a familiar and standards-based Berkeley sockets interface, which is a set of functions and data structures for creating and manipulating sockets  .
- The Berkeley sockets interface includes functions such as socket(), bind(), listen(), accept(), connect(), send(), recv(), sendto(), recvfrom(), close(), etc.
- The socket() function is used to create a socket and returns a socket descriptor, which is an integer that identifies the socket. The socket descriptor can then be used to perform other socket operations.
- The bind() function is used to associate a socket with a local address and port number. This is necessary for receiving data from other sockets.
- The listen() and accept() functions are used to create a server socket that can accept incoming connections from client sockets. The listen() function specifies the maximum number of pending connections that can be queued for the server socket. The accept() function blocks until a connection request arrives, and then returns a new socket descriptor for the connection.
- The connect() function is used to create a client socket that can connect to a server socket. The connect() function specifies the remote address and port number of the server socket.
- The send() and recv() functions are used to send and receive data over a TCP connection. The send() function returns the number of bytes sent, and the recv() function returns the number of bytes received. The send() and recv() functions can block until the data is sent or received, or they can be used in a non-blocking mode with the select() function, which monitors multiple sockets for activity.
- The sendto() and recvfrom() functions are used to send and receive data over a UDP connection. The sendto() function specifies the remote address and port number of the destination socket, and the recvfrom() function returns the remote address and port number of the source socket. The sendto() and recvfrom() functions can also be used for broadcast and multicast communications.
- The close() function is used to close a socket and release its resources. The close() function should be called when the socket is no longer needed.



# Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and notify the CPU that it should take some action.
- Interrupts can be triggered by hardware devices, such as timers, sensors, keyboards, or network interfaces, or by software exceptions, such as division by zero, illegal instruction, or memory access violation.
- Interrupts are handled by interrupt service routines (ISRs), which are special functions that run in response to interrupts and perform the necessary actions to service the interrupt source and resume the normal execution of the system.
- Interrupts are essential for real-time embedded systems, as they allow the system to respond quickly and deterministically to external stimuli and internal events.
- Interrupts can also be used to implement multitasking, by switching the context of the CPU from one task to another at regular intervals or when a task is blocked or preempted by a higher priority task.
- Interrupts can also be used to synchronize tasks with external events, such as sensor readings, user inputs, or network packets.
- Interrupts can also be used to implement inter-task communication, by sending signals or messages to other tasks or by setting flags or semaphores that can be checked by other tasks.

## Interrupts in VXWORKS

- VXWORKS is a preemptive, deterministic RTOS that prioritizes real-time embedded applications.
- VXWORKS has low latency and minimal jitter, which means that it can handle interrupts with high frequency and accuracy.
- VXWORKS has many security features that address the evolving security threats connected devices face at every stage, from boot-up to operation to data transfer to powered off.
- VXWORKS supports various types of interrupts, such as hardware interrupts, software interrupts, and exception interrupts.
- Hardware interrupts are generated by external devices, such as timers, sensors, or network interfaces, and are handled by the hardware interrupt controller (HIC) of the CPU.
- Software interrupts are generated by software instructions, such as system calls, and are handled by the software interrupt controller (SIC) of the CPU.
- Exception interrupts are generated by software errors, such as division by zero, illegal instruction, or memory access violation, and are handled by the exception handler of the CPU.
- VXWORKS provides a set of APIs to register, enable, disable, and acknowledge interrupts, as well as to configure the interrupt priority, vector, and mode.
- VXWORKS also provides a set of APIs to create and manage interrupt tasks, which are special tasks that run in the context of an interrupt and can perform more complex operations than ISRs, such as calling system services, accessing shared resources, or communicating with other tasks.
- VXWORKS also provides a set of APIs to create and manage interrupt objects, which are data structures that store information about interrupts, such as the interrupt source, the ISR, the interrupt task, and the interrupt level.

## Interrupts in FREE RTOS

- FREE RTOS is an open-source, portable, scalable, and configurable RTOS that supports various architectures and platforms.
- FREE RTOS offers various methods to handle interrupts that differ in both latency and the consumption of resources.
- These methods include, Standard ISR processing, Application Controlled Deferred Interrupt Handling, and Centralised Deferred Interrupt Handling.
- Standard ISR processing is the simplest and fastest method, where the ISR runs directly in response to the interrupt and performs the necessary actions to service the interrupt source and resume the normal execution of the system.
- Application Controlled Deferred Interrupt Handling is a method where the ISR runs in response to the interrupt, but instead of performing the necessary actions, it defers them to a task that runs at a lower priority level and can access system services and shared resources.
- Centralised Deferred Interrupt Handling is a method where the ISR runs in response to the interrupt, but instead of performing the necessary actions, it sends them to a queue that is serviced by a single task that runs at a lower priority level and can access system services and shared resources.
- FREE RTOS provides a set of macros to configure and install the RTOS tick interrupt, which is a periodic interrupt that is used to implement multitasking and time-related services.
- FREE RTOS also provides a set of macros to enable and disable interrupts, as well as to raise the interrupt priority level of the CPU to prevent lower priority interrupts from preempting the execution of critical sections of code.
- FREE RTOS also provides a set of macros to create and manage



# I/O Systems for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- I/O systems are the mechanisms that provide uniform access to devices, software stacks, file systems, and other resources in embedded systems and real-time operating systems (RTOS).
- I/O systems can be classified into two types: synchronous and asynchronous.
  - Synchronous I/O systems block the calling thread until the I/O operation is completed, which may cause delays and jitter in real-time applications.
  - Asynchronous I/O systems allow the calling thread to continue execution while the I/O operation is performed in the background, which may improve responsiveness and performance in real-time applications.
- VXWORKS and FREE RTOS are two popular RTOS for embedded systems and real-time applications.
  - VXWORKS is a proprietary RTOS that provides high performance, reliability, safety, and security for the most critical infrastructure's embedded computing systems. It supports C++17, Boost, Rust, Python, pandas, and more, as well as an edge-optimized, OCI-compliant container engine. It has a preemptive, deterministic scheduler that prioritizes real-time tasks and has low latency and minimal jitter.
  - FREE RTOS is an open source RTOS that can be thought of as a thread library rather than an operating system, although command line interface and POSIX-like input/output (I/O) abstraction are available. It implements multiple threads by having the host program call a thread tick method at regular short intervals. It has a cooperative, priority-based scheduler that allows tasks to yield the processor voluntarily or when blocked on an I/O operation.
- Some of the differences between VXWORKS and FREE RTOS in terms of I/O systems are:
  - VXWORKS provides a unified I/O system that supports block, character, network, and memory-mapped devices, as well as pipes, sockets, and message queues. It also provides a virtual file system (VFS) layer that allows applications to access different file systems transparently.
  - FREE RTOS provides a minimal I/O system that supports only character devices, such as serial ports, LCDs, and keyboards. It also provides a simple file system (FFS) layer that supports only FAT file systems.
  - VXWORKS supports asynchronous I/O operations through the asynchronous I/O (AIO) library, which allows applications to submit multiple I/O requests and receive completion notifications through signals, callbacks, or message queues.
  - FREE RTOS does not support asynchronous I/O operations natively, but it can be implemented using tasks, queues, semaphores, and timers.
  - VXWORKS supports advanced I/O features, such as memory mapping, direct I/O, scatter/gather I/O, zero-copy I/O, and DMA I/O.
  - FREE RTOS does not support advanced I/O features natively, but some of them can be implemented using third-party libraries or hardware-specific drivers.



# General Architecture for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that are used for embedded systems and real-time applications.
- An RTOS is an operating system that provides predictable and deterministic performance for time-sensitive tasks, such as controlling sensors, actuators, or communication devices.
- An RTOS typically consists of a kernel, which manages the core functions of the system, such as task scheduling, interrupt handling, memory management, and inter-task communication.
- An RTOS may also provide additional services, such as file systems, network protocols, device drivers, or graphical user interfaces, depending on the requirements and capabilities of the target platform.
- An RTOS differs from a general purpose operating system (GPOS) in several aspects, such as:
  - An RTOS has a smaller footprint and lower overhead than a GPOS, as it is optimized for specific hardware and application domains.
  - An RTOS supports preemptive multitasking, which means that a higher priority task can interrupt a lower priority task at any time, ensuring timely response to critical events.
  - An RTOS provides mechanisms to avoid or resolve priority inversion, which is a situation where a low priority task blocks a high priority task from executing, due to shared resources or dependencies.
  - An RTOS may use fixed or dynamic priority scheduling algorithms, depending on the nature and complexity of the tasks. Fixed priority scheduling assigns a static priority to each task, while dynamic priority scheduling adjusts the priority of tasks based on their deadlines, execution history, or other factors.
  - An RTOS may support hard or soft real-time constraints, depending on the level of guarantee and tolerance for missing deadlines. Hard real-time constraints require that a task must finish before its deadline, otherwise the system may fail or cause damage. Soft real-time constraints allow some degree of flexibility or slack for missing deadlines, as long as the overall performance or quality of service is acceptable.

- VXWORKS and FREE RTOS have different architectures and features, as summarized below:

  - VXWORKS is a proprietary RTOS developed by Wind River Systems, which is widely used in aerospace, defense, industrial, and automotive applications. VXWORKS has a monolithic kernel architecture, which means that all the kernel components and services are integrated into a single executable image that runs in the privileged mode of the processor. VXWORKS supports user-space and kernel-space concepts, which means that applications can run in a separate address space and mode from the kernel, providing protection and isolation. VXWORKS supports hard and soft real-time constraints, and uses a fixed priority preemptive scheduling algorithm with priority inheritance to avoid priority inversion. VXWORKS also provides a rich set of features and services, such as POSIX compatibility, memory protection, file systems, network protocols, device drivers, graphical user interfaces, security, and multicore support.
  - FREE RTOS is an open source RTOS developed by Richard Barry, which is widely used in academic, hobbyist, and commercial applications. FREE RTOS has a microkernel architecture, which means that the kernel consists of a minimal set of components and services that run in the privileged mode of the processor, while the rest of the features and services are implemented as libraries or modules that run in the user mode. FREE RTOS does not support user-space and kernel-space concepts, which means that applications run in the same address space and mode as the kernel, without protection or isolation. FREE RTOS supports soft real-time constraints, and uses a fixed priority preemptive scheduling algorithm with priority inheritance to avoid priority inversion. FREE RTOS also provides a basic set of features and services, such as task management, inter-task communication, timers, memory management, and hooks. FREE RTOS can be extended with additional features and services, such as file systems, network protocols, device drivers, or graphical user interfaces, by using third-party libraries or modules.



# Device Driver Studies for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A device driver is a software component that allows an operating system to communicate with a hardware device, such as a keyboard, mouse, printer, disk, network card, etc.
- A device driver typically implements a standard interface, such as POSIX, that defines the functions and data structures for accessing the device.
- A device driver may also provide additional features, such as power management, error handling, configuration, etc.
- A device driver may be classified into two types: character drivers and block drivers.
  - A character driver transfers data to and from a device one byte at a time, such as a serial port or a keyboard.
  - A block driver transfers data to and from a device in fixed-size blocks, such as a disk or a flash memory.
- A device driver may be implemented in different ways, depending on the operating system and the hardware architecture.
  - A device driver may be part of the kernel, running in privileged mode and having direct access to the hardware registers and memory.
  - A device driver may be a loadable module, dynamically loaded and unloaded by the kernel as needed, and communicating with the hardware through a well-defined interface.
  - A device driver may be a user-level program, running in user mode and communicating with the hardware through a system call or a device file.

- VXWORKS is a real-time operating system (RTOS) for embedded systems, developed by Wind River Systems.
- VXWORKS provides features such as multitasking, inter-task communication, memory management, interrupt handling, device drivers, file system, network stack, etc.
- VXWORKS supports various hardware platforms, such as x86, ARM, PowerPC, MIPS, etc.
- VXWORKS is a deterministic, priority-based preemptive RTOS with low latency and minimal jitter  .
- VXWORKS is built on an upgradable, future-proof architecture to help you rapidly respond to changing market requirements and technology advancements .
- VXWORKS supports various device driver models, such as VxBus, WDB, PCI, USB, etc.
  - VxBus is a device driver framework that provides a uniform interface for device discovery, configuration, and access.
  - WDB is a device driver framework that supports debugging and downloading of applications and drivers over a network or a serial port.
  - PCI is a device driver framework that supports the Peripheral Component Interconnect (PCI) bus standard for connecting devices to the system.
  - USB is a device driver framework that supports the Universal Serial Bus (USB) standard for connecting devices to the system.

- FREE RTOS is a market-leading real-time operating system (RTOS) for microcontrollers and small microprocessors, developed by Real Time Engineers Ltd.
- FREE RTOS provides features such as multitasking, inter-task communication, memory management, interrupt handling, device drivers, file system, network stack, etc.
- FREE RTOS supports various hardware platforms, such as ARM, AVR, PIC, MSP430, etc.
- FREE RTOS is a cooperative RTOS with optional preemption, meaning that tasks can voluntarily yield the processor or be preempted by higher priority tasks.
- FREE RTOS is an open source project, licensed under the MIT license, that allows users to modify and distribute the source code.
- FREE RTOS supports various device driver models, such as IO abstraction, peripheral control, peripheral libraries, etc.
  - IO abstraction is a device driver model that provides a generic interface for accessing different types of devices, such as UART, SPI, I2C, etc.
  - Peripheral control is a device driver model that provides direct access to the hardware registers and memory of the device.
  - Peripheral libraries are device driver libraries that provide specific functions and data structures for accessing the device.



# Driver Module Explanation for the Notes of the Unit 4 - VXWORKS / FREE RTOS in the Subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A driver module is a software component that interacts with a specific hardware device or peripheral, such as a keyboard, mouse, printer, network card, etc.
- A driver module provides a uniform interface to the device, hiding the details of its implementation and operation from the application layer.
- A driver module typically consists of two parts: a device driver and a device controller.
- A device driver is the part of the driver module that communicates with the operating system kernel, such as VxWorks or FreeRTOS, and handles requests from user applications to access the device.
- A device controller is the part of the driver module that communicates with the hardware device directly, using low-level protocols and commands, and performs the actual data transfer or control operations.
- A driver module may also include a device library, which is a set of functions or APIs that provide higher-level abstractions and functionalities for the device, such as graphics, audio, networking, etc.
- A driver module may be implemented as a static or dynamic component, depending on the design and requirements of the system.
- A static driver module is linked with the operating system kernel or the application at compile time, and is loaded into memory when the system boots up.
- A dynamic driver module is loaded into memory at run time, either on demand or by explicit request, and can be unloaded when not needed.
- A dynamic driver module offers more flexibility and modularity, but also requires more memory and processing resources than a static driver module.
- VxWorks and FreeRTOS are two examples of real-time operating systems (RTOS) that support driver modules for various devices and platforms.
- VxWorks is a preemptive, deterministic RTOS that prioritizes real-time embedded applications. It has low latency and minimal jitter. VxWorks has many security features that address the evolving security threats connected devices face at every stage, from boot-up to operation to data transfer to powered off.
- FreeRTOS is a free, open source RTOS that is designed to be simple, small, and scalable. It supports multiple architectures and platforms, and can be configured to meet different application needs. FreeRTOS also provides extensions and libraries for additional features, such as networking, file system, USB, etc.
- VxWorks and FreeRTOS have different approaches to driver module development and integration.
- VxWorks provides a comprehensive and consistent driver framework that supports various types of devices, such as character, block, network, USB, etc. VxWorks also provides a set of tools and APIs for driver development, testing, debugging, and deployment.
- FreeRTOS does not have a standard driver framework, but rather relies on the device driver libraries provided by the hardware vendors or third-party developers. FreeRTOS also provides a POSIX-like interface, called FreeRTOS Plus IO, that allows applications to access devices using open(), read(), write(), ioctl(), etc.
- VxWorks and FreeRTOS are compatible with each other, and there are tools and methods to port applications and driver modules from one RTOS to another. For example, MapuSoft's OS Changer VxWorks Porting Kit can automatically migrate and re-use VxWorks applications and driver modules to FreeRTOS, with minimal code changes.



# Implementation of Device Driver for a Peripheral

- A device driver is a software application that allows a hardware device (such as a printer or a keyboard) to interact with the operating system (such as Windows or Linux) of a computer system.
- A device driver acts as a translator between the operating system and the peripheral device, and communicates with the device through the computer bus (such as PCI or USB) that connects the device with the computer .
- A device driver consists of a physical structure of modes that represent the peripheral device and its functions. The modes can be classified into three types: character, block, and network.
  - Character mode: The device driver transfers data one character at a time, such as a keyboard or a mouse.
  - Block mode: The device driver transfers data in blocks of fixed size, such as a disk or a CD-ROM.
  - Network mode: The device driver transfers data in packets of variable size, such as a network card or a modem.
- A device driver can be implemented in different ways depending on the operating system and the device type. Some common methods are:
  - Monolithic: The device driver is integrated into the kernel of the operating system and runs in the same address space as the kernel. This method provides high performance and low overhead, but also increases the complexity and risk of kernel errors.
  - Modular: The device driver is compiled as a separate module that can be loaded and unloaded dynamically by the kernel of the operating system. This method provides flexibility and modularity, but also introduces some overhead and dependency issues.
  - User mode: The device driver runs in the user space of the operating system and communicates with the kernel through a system call interface. This method provides security and portability, but also reduces the performance and increases the complexity of the communication.
  - Hybrid: The device driver combines the features of the above methods, such as running some parts in the kernel space and some parts in the user space. This method provides a trade-off between the advantages and disadvantages of the other methods.
- A device driver can be developed using various tools and languages, such as C, C++, Java, Python, or assembly. The steps of developing a device driver are:
  - Identify the device type and the operating system requirements.
  - Choose the appropriate method and tools for implementing the device driver.
  - Write the code for the device driver using the chosen language and tools.
  - Compile and test the device driver using the appropriate tools and methods.
  - Debug and optimize the device driver using the appropriate tools and methods.
  - Install and update the device driver using the appropriate tools and methods.

