

# EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded system is a computer system that is designed to perform a specific function within a larger system or device. It typically has limited hardware resources, such as memory, processing power, and input/output devices. It often runs on a microcontroller or a microprocessor that is integrated with the hardware components of the system. 
- A real-time operating system (RTOS) is a type of operating system that is specialized for embedded systems that operate in real-time environments. A real-time environment is one where the system must respond to events or inputs within a predictable and bounded time limit, otherwise it may cause failure or damage.  
- Some examples of real-time embedded systems are:
  - Medical devices, such as pacemakers, ventilators, and infusion pumps.
  - Industrial control systems, such as robots, CNC machines, and PLCs.
  - Automotive systems, such as engine control, anti-lock braking, and airbag deployment.
  - Aerospace systems, such as flight control, navigation, and communication.
  - Consumer electronics, such as digital cameras, video games, and smart watches.  
- Some characteristics of real-time operating systems are:
  - They use preemptive multitasking, which means that the scheduler can interrupt a running task and switch to another task based on their priority and deadlines.
  - They have low latency, which means that the time between an event and the system's response is minimal and consistent.
  - They have high reliability, which means that the system can handle errors and faults without compromising its functionality or safety.
  - They have small footprint, which means that the system can run on limited hardware resources and consume less power.  
- Some examples of real-time operating systems are:
  - FreeRTOS, which is an open source RTOS that supports various microcontrollers and architectures.
  - VxWorks, which is a commercial RTOS that is widely used in aerospace, defense, and industrial applications.
  - QNX, which is a commercial RTOS that is based on microkernel architecture and is used in automotive, medical, and telecommunications applications.
  - Linux, which is a general-purpose operating system that can be configured and modified to support real-time applications.



## Unit 1 - EMBEDDED OS INTERNALS

- An embedded operating system (OS) is a specialized software that runs on a dedicated hardware platform and provides a set of services and interfaces for the applications running on it.
- Embedded OSes are designed to meet the specific requirements of the embedded systems, such as real-time performance, low memory footprint, power efficiency, reliability, security, etc.
- Embedded OSes can be classified into two categories: general-purpose embedded OSes and real-time embedded OSes.
- General-purpose embedded OSes are based on standard OSes, such as Linux, Windows, or Android, and are modified or customized to suit the needs of the embedded systems. They offer a rich set of features and functionalities, but may not guarantee deterministic behavior or strict timing constraints.
- Real-time embedded OSes are designed to provide predictable and timely responses to the events or stimuli in the system. They have a minimal kernel that handles the scheduling, synchronization, and communication of the tasks, and a set of services and libraries that support the application development. They can be further divided into hard real-time OSes and soft real-time OSes, depending on the degree of criticality of the timing requirements.
- Some examples of general-purpose embedded OSes are Embedded Linux, Windows Embedded, and Android Things. Some examples of real-time embedded OSes are FreeRTOS, VxWorks, and QNX.
- The main components of an embedded OS are:
  - Kernel: The core of the OS that manages the resources, such as CPU, memory, and I/O devices, and provides the basic services, such as task management, inter-task communication, interrupt handling, and timer services.
  - Device drivers: The software modules that interface with the hardware devices and abstract their functionalities for the applications.
  - File system: The software module that organizes the data storage and retrieval on the persistent memory devices, such as flash, EEPROM, or SD card.
  - Network stack: The software module that implements the protocols and standards for the data communication over the network interfaces, such as Ethernet, Wi-Fi, Bluetooth, or CAN.
  - Middleware: The software layer that provides the common functionalities and services for the applications, such as graphical user interface (GUI), database, web server, security, etc.
  - Application programming interface (API): The set of functions, data structures, and constants that define the interface between the applications and the OS.
  - Applications: The software programs that implement the specific functions and logic of the embedded system.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on Linux internals for embedded systems:

### Linux internals for embedded systems

- Linux is a popular choice for embedded systems because it is open source, scalable, supported by developers, and has rich tooling.
- Linux consists of several components that work together to provide the functionality of an embedded system:
  - **Toolchain**: A collection of development tools, such as GCC compiler, C libraries, and GNU debugger, that are used to create source code for the target embedded hardware.
  - **Bootloader**: A piece of code that runs when the power is applied to the embedded hardware for the first time. It initializes the hardware, loads the Linux kernel into memory, and passes some parameters to the kernel.
  - **Linux kernel**: The core of the Linux system that manages the hardware resources, such as CPU, memory, I/O devices, and interrupts. It also provides the basic services for the user space applications, such as process management, file system, networking, and device drivers.
  - **Device tree**: A data structure that describes the hardware configuration of the embedded system, such as the CPU type, memory size, peripheral devices, and their addresses and interrupts. It is used by the Linux kernel to initialize the hardware and load the appropriate drivers.
  - **Root file system**: A collection of files and directories that contain the user space applications, libraries, configuration files, and data. It can be stored in different types of media, such as flash memory, SD card, or network file system.
  - **Configuration files**: Files that store the settings and parameters for the Linux system and the user space applications, such as the network configuration, the system time zone, the user accounts, and the services to run at startup.
- Linux can be customized for different embedded applications by selecting the appropriate components, configuring the kernel options, and adding or removing the user space applications .
- Linux can be developed and debugged using various tools, such as cross-compilers, emulators, debuggers, profilers, and tracing tools.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on process management for the unit 1 of embedded OS internals:

### Process Management

- Process management is how the OS manages and views other software in the embedded system (via processes).
- A process (or a task) is created by an OS to encapsulate all the information that is involved in the executing of a program (stack, PC, source code, data, etc.).
- A process has a state, which can be one of the following: ready, running, waiting, suspended, or terminated.
- A process can be switched from one state to another by the OS, which is called context switching.
- Context switching involves saving the current state of the process and restoring the state of the next process to run.
- Context switching can be triggered by interrupts, system calls, or scheduling decisions.
- Process scheduling is the policy that the OS uses to decide which process to run next.
- Process scheduling can be based on different criteria, such as priority, deadline, or fairness.
- In an embedded system, processes are created to perform specific tasks.
- Depending on the importance of the task, each process is assigned a priority, which is usually static.
- Processes run either periodically or in response to external events.
- Process management in embedded systems must meet the strict requirements of the operational domain, such as real-time and event-driven functionality, safety, reliability, and longevity.



Hello, I am Sydney, your AI assistant. I will help you with your query. Here are some notes on file management for the unit 1 of embedded OS internals:

### File Management

- File management is the process of manipulating files in a computer system, such as creating, modifying, deleting, storing, and retrieving them.
- Files are collections of data that have a name, a type, and a size. They can be stored on various devices, such as RAM, flash memory, hard disk, or external storage systems.
- File management in embedded systems is a challenging task, as it involves dealing with limited resources, reliability issues, fail-safety, and data integrity.
- Some embedded operating systems provide memory management support for a temporary or permanent file system storage scheme on various memory devices.
- File systems are essentially a collection of files along with their management protocols, such as how to organize files into folders, how to allocate space for files, how to access files, and how to handle errors and failures .
- There are different types of file systems, such as FAT, NTFS, ext, and UFS, each with its own advantages and disadvantages. Some file systems are more suitable for embedded systems than others, depending on the requirements and constraints of the application  .
- File management in embedded systems requires careful design and implementation, as it can affect the performance, reliability, and security of the system. Some of the factors to consider are:
  - The type and size of the storage device
  - The frequency and pattern of file operations
  - The level of data consistency and integrity required
  - The trade-off between speed and durability
  - The compatibility and interoperability with other systems
  - The certification and compliance with standards and regulations .



### Memory Management

Memory management is the process of allocating and deallocating memory resources to programs and processes in an embedded system. Memory management can affect the performance, reliability, and functionality of an embedded system. Some of the topics related to memory management in embedded systems are:

- **Memory types**: Embedded systems typically use different types of memory for different purposes, such as ROM, RAM, flash, EEPROM, SRAM, etc. Each type of memory has its own characteristics, such as speed, size, cost, volatility, persistence, etc. Depending on the requirements of the system, the memory types can be selected and configured accordingly .
- **Memory allocation**: Memory allocation is the process of assigning memory blocks to programs or processes that request them. Memory allocation can be static or dynamic. Static allocation is done at compile time or load time, and the memory blocks are fixed in size and location. Dynamic allocation is done at run time, and the memory blocks can vary in size and location. Dynamic allocation can be done by the application or by the operating system using memory pools or memory managers .
- **Memory protection**: Memory protection is the mechanism of preventing unauthorized or erroneous access to memory by programs or processes. Memory protection can prevent memory corruption, data leakage, or system crashes. Memory protection can be implemented by hardware or software. Hardware memory protection can use memory mapping or memory management units (MMUs) to control the access rights and address translation of memory regions. Software memory protection can use memory segmentation or memory paging to divide the memory into logical units and assign permissions to them .
- **Memory optimization**: Memory optimization is the process of improving the memory usage and efficiency of an embedded system. Memory optimization can reduce the memory footprint, increase the memory throughput, or enhance the memory reliability of the system. Memory optimization can be done by various techniques, such as memory compression, memory caching, memory pooling, memory defragmentation, memory garbage collection, etc. Memory optimization can be done by the application or by the operating system using memory management algorithms or policies .



### I/O Management

- I/O management is the process of controlling the input and output operations of an embedded system.
- I/O management involves the interaction between the operating system (OS), the device drivers, the file system, and the hardware devices.
- I/O management provides an abstraction layer that hides the details of the hardware and device drivers from the higher-level software, such as applications and libraries.
- I/O management also ensures the efficiency, reliability, and security of the I/O operations, by managing the allocation, scheduling, buffering, caching, and error handling of the I/O requests.

#### I/O System Components

- The main components of the I/O system are:

  - The I/O manager: The core of the I/O system that defines the framework and the model for delivering I/O requests to device drivers.
  - The device drivers: The software modules that interface with the hardware devices and implement the device-specific functions.
  - The file system: The software module that organizes the data on the storage devices and provides a logical view of the files and directories.
  - The hardware devices: The physical components that perform the actual input and output operations, such as sensors, actuators, keyboards, displays, disks, etc.

#### I/O Request Packets

- The I/O system is packet driven, meaning that most I/O requests are represented by an I/O request packet (IRP), which is a data structure that contains the information about the I/O operation, such as the source, the destination, the type, the size, the status, and the callback function of the I/O request.
- The IRP travels from one I/O system component to another, following a path that depends on the type and the characteristics of the I/O request.
- The IRP is created by the I/O manager when an application or a library initiates an I/O request, and is passed to the file system (if applicable) and then to the device driver.
- The device driver performs the I/O operation by communicating with the hardware device, and then completes the IRP by setting the status and invoking the callback function.
- The I/O manager then returns the IRP to the application or the library, and frees the memory allocated for the IRP.

#### I/O Programming

- I/O programming is the process of writing software that performs input and output operations on an embedded system.
- I/O programming can be done at different levels of abstraction, depending on the needs and the capabilities of the embedded system.
- The main levels of I/O programming are:

  - The application level: The highest level of abstraction, where the software uses the standard I/O interface provided by the OS, such as the file system API or the device-independent I/O API .
  - The device driver level: The intermediate level of abstraction, where the software writes or modifies the device drivers that interface with the hardware devices .
  - The hardware level: The lowest level of abstraction, where the software directly accesses the hardware registers and ports of the devices, using assembly language or low-level C instructions.

- The level of I/O programming depends on the availability and the suitability of the OS, the device drivers, and the file system for the embedded system.
- Some embedded systems may not have an OS, a file system, or device drivers, and may require hardware-level I/O programming.
- Some embedded systems may have a minimal OS, a simple file system, or generic device drivers, and may require device driver-level I/O programming.
- Some embedded systems may have a full-fledged OS, a sophisticated file system, or specific device drivers, and may only require application-level I/O programming.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you:

### Overview of POSIX APIs

- POSIX stands for Portable Operating System Interface. It is a family of standards specified by IEEE for maintaining compatibility among operating systems .
- POSIX defines both the system and user-level application programming interfaces (APIs), along with command line shells and utility interfaces, for software compatibility (portability) with variants of Unix and other operating systems.
- POSIX is also a trademark of the IEEE. POSIX is intended to be used by both application and system developers.
- The POSIX API subset is an increasingly popular OSAL (operating system abstraction layer) for IoT and embedded applications, as can be seen in Zephyr, AWS:FreeRTOS, TI-RTOS, and NuttX.
- Benefits of POSIX support in Zephyr include:
  - Offering a familiar API to non-embedded programmers, especially from Linux.
  - Enabling the use of existing libraries and middleware that are already POSIX compliant.
  - Reducing the learning curve and development time for new projects.
- The C POSIX library is a specification of a C standard library for POSIX systems. It was developed at the same time as the ANSI C standard. Some effort was made to make POSIX compatible with standard C; POSIX includes additional functions to those introduced in standard C.
- C POSIX library header files include:
  - `<unistd.h>`: defines miscellaneous symbolic constants and types, and declares miscellaneous functions.
  - `<sys/types.h>`: defines data types used in system calls.
  - `<sys/stat.h>`: defines the structure of the data returned by the `stat()` function.
  - `<fcntl.h>`: defines values for the `open()` function.
  - `<dirent.h>`: defines structures and functions for directory operations.
  - `<signal.h>`: defines signal handling functions and macros.
  - `<pthread.h>`: defines POSIX threads and related functions.
  - `<semaphore.h>`: defines POSIX semaphores and related functions.
  - `<mqueue.h>`: defines POSIX message queues and related functions.
  - `<time.h>`: defines date and time functions and types.
  - `<sys/time.h>`: defines additional time-related functions and types.
  - `<sys/select.h>`: defines functions and types for multiplexing I/O.
  - `<poll.h>`: defines functions and types for polling I/O.
  - `<sys/socket.h>`: defines functions and types for socket operations.
  - `<netinet/in.h>`: defines Internet protocol and address family.
  - `<arpa/inet.h>`: defines functions for manipulating network addresses.
  - `<netdb.h>`: defines functions for network database operations.
  - `<syslog.h>`: defines functions for system logging.
  - `<termios.h>`: defines functions and types for terminal I/O.
  - `<sys/resource.h>`: defines functions and types for resource management.
  - `<sys/wait.h>`: defines functions and macros for process management.
  - `<spawn.h>`: defines functions and types for creating new processes.
  - `<dlfcn.h>`: defines functions and types for dynamic linking.
  - `<regex.h>`: defines functions and types for regular expressions.
  - `<fnmatch.h>`: defines functions and types for filename matching.
  - `<glob.h>`: defines functions and types for pathname expansion.
  - `<wordexp.h>`: defines functions and types for word expansion.
  - `<math.h>`: defines mathematical functions and constants.
  - `<complex.h>`: defines complex arithmetic functions and types.
  - `<locale.h>`: defines localization functions and types.
  - `<monetary.h>`: defines functions and types for monetary formatting.
  - `<langinfo.h>`: defines functions and types for language information.
  - `<ctype.h>`: defines functions and types for character classification and conversion.
  - `<wctype.h>`



### Threads – Creation

- A thread is a separate execution path within a program that can run concurrently with other threads.
- A thread shares the same memory and resources as the program that created it, which enables multiple threads to collaborate and work efficiently within a single program.
- Threads can be created and managed by the operating system (kernel-supported threads) or by the user-level program (user-level threads).
- Kernel-supported threads are supported by the operating system, which stores multiple thread control blocks (TCBs) per process and is involved in dispatching and switching between threads (even between threads in the same process).
- User-level threads are created and managed by the user-level program, which uses its own data structures and libraries to implement threads. The operating system is unaware of the user-level threads and treats them as a single process.
- Some operating systems, such as Windows, MacOS X, Linux, and some embedded operating systems, provide libraries or frameworks to create and manage user-level threads, such as Qt or pthreads .
- To create a thread, the program needs to specify the function or code that the thread will execute, as well as any parameters or arguments that the thread needs. The program also needs to allocate memory and resources for the thread, such as stack, registers, and priority.
- The operating system or the user-level library then creates a TCB for the thread, which contains information such as thread ID, state, context, and scheduling information. The TCB is stored in a ready list or a queue, waiting for the operating system or the user-level scheduler to assign a processor to the thread.
- When the thread is assigned a processor, it starts executing the function or code that was specified by the program. The thread can communicate with other threads in the same program through shared memory or message passing. The thread can also perform system calls or library calls to access operating system services or resources.
- When the thread finishes its execution or is preempted by another thread, it saves its context in the TCB and returns the processor to the operating system or the user-level scheduler. The thread can then be resumed later by restoring its context from the TCB and continuing its execution. The thread can also terminate itself or be terminated by the program or the operating system.



Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Cancellation for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM. Here is the content I have generated for you:

### Cancellation

- Cancellation is the process of terminating a task or an operation before it is completed.
- Cancellation can be useful for saving resources, improving responsiveness, or handling errors or exceptions.
- Cancellation can be performed by the task itself, by another task, or by the operating system.
- Cancellation can be classified into two types: asynchronous and synchronous.

#### Asynchronous Cancellation

- Asynchronous cancellation occurs when a task is terminated by an external signal or event, without waiting for the task to reach a safe point or a cancellation point.
- Asynchronous cancellation can be implemented by using interrupts, signals, exceptions, or system calls.
- Asynchronous cancellation can be fast and responsive, but it can also be unsafe and unpredictable, as it can leave the system in an inconsistent or corrupted state.
- Asynchronous cancellation can be avoided by using cancellation handlers, which are functions that are executed when a task is cancelled, to perform cleanup and recovery actions.

#### Synchronous Cancellation

- Synchronous cancellation occurs when a task is terminated by checking a cancellation flag or a condition variable, at a safe point or a cancellation point, where the task can be safely terminated without affecting the system state.
- Synchronous cancellation can be implemented by using polling, blocking, or cooperative mechanisms.
- Synchronous cancellation can be safe and predictable, but it can also be slow and unresponsive, as it depends on the frequency and location of the cancellation points.
- Synchronous cancellation can be improved by using cancellation tests, which are functions that check the cancellation flag or the condition variable, and raise an exception or a signal if the task is cancelled.



### POSIX Threads

- POSIX Threads, or **pthreads**, is an **execution model** that allows a program to control multiple different flows of work that overlap in time .
- Pthreads is an **API** defined by the **IEEE** standard **POSIX.1c**, Threads extensions (IEEE Std 1003.1c-1995).
- Pthreads is **independent** from a programming language, but it is mainly used with **C/C++** .
- A single process can contain multiple threads, all of which are executing the same program.
- Threads share the same **address space**, **file descriptors**, **stack**, and other attributes with the process that created them.
- Threads can communicate with each other using **shared variables**, **mutexes**, **condition variables**, and other **synchronization primitives** .
- Threads can also create, join, detach, and cancel other threads .
- Threads can have different **scheduling policies** and **priorities** that affect their execution order and performance .
- Pthreads provides a set of **functions**, **header files**, and **data types** for threaded programming.
- Some of the common functions are:

  - `pthread_create()` - creates a new thread
  - `pthread_join()` - waits for a thread to terminate
  - `pthread_exit()` - terminates the calling thread
  - `pthread_detach()` - detaches a thread from the process
  - `pthread_cancel()` - requests the cancellation of a thread
  - `pthread_mutex_init()` - initializes a mutex
  - `pthread_mutex_lock()` - locks a mutex
  - `pthread_mutex_unlock()` - unlocks a mutex
  - `pthread_cond_init()` - initializes a condition variable
  - `pthread_cond_wait()` - waits on a condition variable
  - `pthread_cond_signal()` - signals a condition variable
  - `pthread_cond_broadcast()` - broadcasts a condition variable
  - `pthread_attr_init()` - initializes a thread attribute object
  - `pthread_attr_setdetachstate()` - sets the detach state of a thread attribute object
  - `pthread_attr_setschedpolicy()` - sets the scheduling policy of a thread attribute object
  - `pthread_attr_setschedparam()` - sets the scheduling parameters of a thread attribute object
  - `pthread_attr_destroy()` - destroys a thread attribute object
  - `pthread_self()` - returns the thread ID of the calling thread
  - `pthread_equal()` - compares two thread IDs
  - `pthread_getschedparam()` - gets the scheduling parameters of a thread
  - `pthread_setschedparam()` - sets the scheduling parameters of a thread
  - `pthread_once()` - executes a function only once in a process
  - `pthread_key_create()` - creates a thread-specific data key
  - `pthread_key_delete()` - deletes a thread-specific data key
  - `pthread_getspecific()` - gets the value of a thread-specific data key
  - `pthread_setspecific()` - sets the value of a thread-specific data key

- Some of the common header files are:

  - `<pthread.h>` - defines the pthreads API
  - `<sched.h>` - defines the scheduling policies and parameters
  - `<time.h>` - defines the time structures and functions

- Some of the common data types are:

  - `pthread_t` - represents a thread ID
  - `pthread_attr_t` - represents a thread attribute object
  - `pthread_mutex_t` - represents a mutex
  - `pthread_mutexattr_t` - represents a mutex attribute object
  - `pthread_cond_t` - represents a condition variable
  - `pthread_condattr_t` - represents a condition variable attribute object
  - `pthread_once_t` - represents a one-time initialization control
  - `pthread_key_t` - represents a thread-specific data key
  - `sched_param` - represents a scheduling parameter structure
  - `timespec` - represents a time structure

- A simple example of using pthreads is:

```c
#include <stdio.h>
#include <pthread.h>

// A function to be executed by a thread
void *hello(void *arg) {
  printf("Hello, %s!\n", (char *)arg);
  pthread_exit(NULL); // terminate the thread
}

int main() {

```




### Inter Process Communication – Semaphore

- Inter Process Communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions .
- IPC can be done through shared memory or message passing.
- A semaphore is a common method of IPC that uses a variable or abstract data type to control access to a common resource by multiple processes .
- A semaphore can be initialized to a non-negative integer value that represents the number of available resources or units of the resource.
- A semaphore supports two atomic operations: wait and signal.
- The wait operation decrements the semaphore value by one, if it is positive, or blocks the process until the semaphore value becomes positive.
- The signal operation increments the semaphore value by one, and wakes up any blocked process waiting on the semaphore.
- A semaphore can be used to implement mutual exclusion, where only one process can access a critical section at a time, or synchronization, where a process has to wait for another process to finish a task before proceeding.
- To perform synchronization using semaphores, the following are the steps:
  - Step 1: Create a semaphore or connect to an already existing semaphore (semget())
  - Step 2: Perform operations on the semaphore i.e., allocate or release or wait for the resources (semop())
  - Step 3: Perform control operations on the semaphore (semctl())
- A semaphore can be binary (0 or 1) or counting (any non-negative integer).
- A binary semaphore can be used to implement a lock or a mutex, where only one process can enter a critical section at a time.
- A counting semaphore can be used to implement a bounded buffer or a producer-consumer problem, where a producer process can produce items and put them in a buffer, and a consumer process can consume items from the buffer, as long as the buffer is not full or empty.



### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used in embedded systems to pass simple messages between tasks, such as sensor readings, commands, or status updates .
- Pipes have two ends: a read end and a write end. Data written to the write end can be read from the read end in a first-in first-out (FIFO) order .
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the system call `pipe` and are only accessible by the processes that created them or their descendants .
- Pipes can be either blocking or non-blocking. Blocking pipes wait until data is available to be read or written, while non-blocking pipes return immediately with an error code if data is not available .
- Pipes have some advantages and disadvantages compared to other IPC methods. Some advantages are:
  - Pipes are simple and easy to use, requiring only standard file operations such as `read` and `write` .
  - Pipes are portable and widely supported by various operating systems and programming languages .
  - Pipes can be used to create pipelines of commands or processes that process data in stages .
- Some disadvantages are:
  - Pipes are unidirectional, meaning data can only flow in one direction. To achieve bidirectional communication, two pipes are needed .
  - Pipes have limited buffer size and capacity, which can cause data loss or deadlock if the producer and consumer are not synchronized  .
  - Pipes are not suitable for complex or structured data, as they only transfer bytes without any interpretation or formatting .



### FIFO

- FIFO stands for First In First Out, which means that the data that is inserted first will be extracted first.
- FIFOs are commonly used in embedded systems for buffering and flow control between hardware and software components.
- FIFOs can be implemented in hardware or software, depending on the application requirements and the available resources.
- Hardware FIFOs are typically composed of a set of read and write pointers, storage elements, and control logic. They can operate at high speeds and support concurrent read and write operations .
- Software FIFOs are usually implemented as circular buffers or queues, where data is stored in an array and the read and write pointers are updated accordingly. They can be more flexible and adaptable, but they may incur more overhead and latency.
- Some of the benefits of using FIFOs in embedded systems are :
  - They can reduce the host MCU interaction with the sensor or peripheral device, and therefore save power and processing time.
  - They can store information about a movement or event that may be of interest for later analysis or processing.
  - They can avoid losing data when the data rate is higher than the processing rate, or when there are interruptions or delays in the data flow.
  - They can synchronize data between different clock domains or data formats, and provide a consistent data stream for the receiver.
- Some of the challenges or limitations of using FIFOs in embedded systems are :
  - They require additional hardware or software resources, such as memory, logic, or code space, which may be scarce or expensive in some systems.
  - They introduce additional complexity and potential sources of errors, such as overflow, underflow, or data corruption, which need to be detected and handled properly.
  - They may not be suitable for some applications that require strict timing or ordering constraints, such as real-time or deterministic systems.



### Shared Memory

- Shared memory is a method of inter-process communication (IPC) that allows multiple processes to access a common region of memory.
- Shared memory can be used for data exchange, synchronization, or coordination among processes.
- Shared memory is faster than other IPC methods, such as message passing or pipes, because it does not involve copying data or system calls.
- Shared memory can be implemented in different ways, such as:
  - Using a special system call (e.g., `shmget` in Linux) to create and attach a shared memory segment to the address space of a process.
  - Using memory-mapped files (e.g., `mmap` in Linux) to map a file or a device to the address space of a process, and then sharing the file or device among multiple processes.
  - Using a shared memory object (e.g., `shm_open` in POSIX) to create and open a named shared memory region that can be accessed by multiple processes.
- Shared memory can also be classified into two types, depending on the scope of sharing:
  - Local shared memory: the shared memory region is accessible only by processes on the same machine or processor.
  - Distributed shared memory: the shared memory region is accessible by processes on different machines or processors, connected by a network or a bus.
- Shared memory can have advantages and disadvantages, such as:
  - Advantages:
    - High performance and low overhead.
    - Simple and intuitive programming model.
    - Flexible and scalable communication paradigm.
  - Disadvantages:
    - Potential data inconsistency and race conditions.
    - Lack of protection and security mechanisms.
    - Complexity and difficulty of management and synchronization.



### Kernel for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A kernel is the core component of an operating system that acts as a bridge between applications and data processing performed at hardware level using inter-process communication and system calls.
- A kernel is not an operating system itself, but a central module that is loaded into protected memory area during the booting process and remains in memory until the operating system is shut down.
- A kernel provides basic services for all other parts of the operating system, such as memory management, task scheduling, interrupt handling, device drivers, file systems, network protocols, etc.
- A kernel can be classified into different types based on its design and functionality, such as monolithic kernel, microkernel, hybrid kernel, modular kernel, exokernel, etc.
- An embedded operating system is a specialized operating system that is designed for a specific hardware platform and has limited resources and functionality compared to a general-purpose operating system.
- An embedded operating system typically has a small footprint, fast boot time, real-time performance, low power consumption, high reliability, and security features.
- An embedded operating system may use a different kernel type depending on the requirements and constraints of the application domain, such as automotive, industrial, medical, consumer, etc.
- Some examples of embedded operating systems are FreeRTOS, VxWorks, QNX, Linux, Android, Windows Embedded, etc.
- A kernel for an embedded operating system may have some specific features and challenges, such as:
  - Supporting multiple processor architectures and hardware platforms.
  - Providing a minimal and configurable set of services and modules.
  - Balancing between performance, functionality, and resource utilization.
  - Handling concurrent and real-time tasks and events.
  - Managing power and energy consumption.
  - Ensuring security and safety of the system.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of Embedded OS Internals. Here is a possible structure for the notes of Unit 1:

# Unit 1 - Embedded OS Internals

## Introduction
- Define what is an embedded system and an embedded OS
- Explain the characteristics and challenges of embedded systems
- Give examples of embedded systems and their applications
- Compare and contrast embedded OS with general-purpose OS

## Embedded OS Architecture
- Describe the components and layers of an embedded OS
- Explain the functions and services of each component and layer
- Discuss the design trade-offs and criteria of an embedded OS
- Compare and contrast different types of embedded OS architectures, such as monolithic, microkernel, exokernel, etc.

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

## Embedded OS Scheduling
- Define what is a task, a process, and a thread in an embedded OS
- Explain the concepts and algorithms of task scheduling in an embedded OS
- Discuss the factors and metrics of task scheduling, such as priority, deadline, response time, utilization, etc.
- Compare and contrast different types of task scheduling algorithms, such as preemptive, non-preemptive, static, dynamic, etc.
- Explain the challenges and solutions of task scheduling in real-time embedded systems

## Embedded OS Memory Management
- Define what is memory and memory management in an embedded OS
- Explain the concepts and techniques of memory management in an embedded OS
- Discuss the factors and metrics of memory management, such as size, speed, cost, fragmentation, etc.
- Compare and contrast different types of memory management techniques, such as static, dynamic, paging, segmentation, etc.
- Explain the challenges and solutions of memory management in resource-constrained embedded systems

## Embedded OS Inter-Process Communication
- Define what is inter-process communication (IPC) and why it is needed in an embedded OS
- Explain the concepts and methods of IPC in an embedded OS
- Discuss the factors and metrics of IPC, such as performance, reliability, security, etc.
- Compare and contrast different types of IPC methods, such as message passing, shared memory, pipes, sockets, etc.
- Explain the challenges and solutions of IPC in distributed embedded systems

## Embedded OS Security
- Define what is security and why it is important in an embedded OS
- Explain the concepts and principles of security in an embedded OS
- Discuss the factors and metrics of security, such as confidentiality, integrity, availability, etc.
- Compare and contrast different types of security threats and attacks, such as malware, denial-of-service, spoofing, etc.
- Explain the challenges and solutions of security in embedded systems, such as encryption, authentication, firewall, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on kernel module programming for the unit 1 of embedded OS internals:

### Kernel Module Programming

- A kernel module is an object file that contains code that can extend the kernel functionality at runtime.
- Kernel modules can be inserted into the kernel or removed from the kernel while the system is running.
- Kernel modules are useful for implementing device drivers, file systems, network protocols, and other features that are not part of the core kernel.
- Kernel modules must have at least two functions: a start (initialization) function called `init_module()` and an end (cleanup) function called `cleanup_module()`.
- The start function is called when the module is loaded into the kernel using the `insmod` command, and the end function is called when the module is unloaded from the kernel using the `rmmod` command.
- Kernel modules can also define other functions and variables that are used internally by the module or exported to other modules.
- Kernel modules can communicate with the kernel and other modules using system calls, kernel data structures, and kernel APIs.
- Kernel modules can also register callback functions for various kernel events, such as interrupts, timers, file operations, etc.
- Kernel modules can be written in C or assembly language, and must follow the kernel coding style and conventions.
- Kernel modules must be compiled with the same compiler and configuration options as the kernel, and must be compatible with the kernel version and architecture.
- Kernel modules can be debugged using tools such as `printk`, `kdb`, `kgdb`, `kprobes`, etc.



### Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduler is a mechanism within an embedded OS that determines the order and the duration of tasks to run on the CPU.
- A scheduler creates the illusion that all the tasks are running concurrently by allowing each to have a share of the processor time.
- The way that time is allocated between tasks is termed "scheduling" and it can affect the performance, responsiveness, and predictability of the system.
- There are different types of schedulers in embedded systems, such as:
  - Time Slice (TS) Scheduler: A TS scheduler is the next step in complexity from Round Robin (RR). Time is divided into "slots", with each task being allowed to execute for the duration of its slot. A TS scheduler can be fair or unfair, depending on whether the slots are equal or unequal in length.
  - Priority Scheduler: A priority scheduler assigns a priority level to each task and always runs the highest priority task that is ready. A priority scheduler can be cooperative or preemptive, depending on whether a task can voluntarily relinquish the CPU or be interrupted by a higher priority task. A priority scheduler can also be static or dynamic, depending on whether the priority levels are fixed or can change at runtime.
  - Composite Scheduler: A composite scheduler combines different scheduling algorithms to achieve a balance between performance and predictability. For example, a composite scheduler can use a priority scheduler for real-time tasks and a TS scheduler for non-real-time tasks.
- A scheduler can also be implemented in different ways, such as:
  - Kernel-based Scheduler: A kernel-based scheduler is part of the embedded OS and provides scheduling services and other features useful in multitasking systems, such as semaphores, mutexes, queues, etc.. A kernel-based scheduler can be complex and require special compilation.
  - Application-based Scheduler: An application-based scheduler is directly inserted into the application code and provides basic support for multiple tasks. An application-based scheduler can be simple and require no special compilation. An example of an application-based scheduler is RIOS (Real-time Interrupt-driven Operating System).



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the types of scheduling for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Types of scheduling in embedded systems

Scheduling is the process of allocating CPU time to different tasks or processes in an embedded system. Scheduling can affect the performance, responsiveness, and predictability of the system. There are different types of scheduling algorithms that can be used in embedded systems, depending on the system requirements and constraints. Some of the common types of scheduling are:

- **Non-preemptive scheduling**: In this type of scheduling, the CPU executes a task until it completes or voluntarily relinquishes the CPU. The task cannot be interrupted by another task with higher priority. This type of scheduling is simple and easy to implement, but it can cause long waiting times and poor responsiveness for high-priority tasks. Non-preemptive scheduling is suitable for systems that do not have strict timing constraints or real-time requirements. 

- **Preemptive scheduling**: In this type of scheduling, the CPU can interrupt a task that is currently executing and switch to another task with higher priority. The interrupted task is suspended and resumed later when the CPU is available. This type of scheduling can improve the responsiveness and predictability of the system, but it can also introduce overhead and complexity in managing the task states and resources. Preemptive scheduling is suitable for systems that have real-time requirements and need to meet deadlines.  

- **Round-robin scheduling**: This is a special case of preemptive scheduling, where the tasks have equal priority and are executed in a circular order. Each task is given a fixed amount of CPU time, called a time slice or quantum, and then the CPU switches to the next task in the queue. This type of scheduling can provide fairness and balance among the tasks, but it can also cause frequent context switches and poor performance for tasks that need longer execution time. Round-robin scheduling is suitable for systems that have multiple tasks with similar importance and characteristics.  

- **Time slice scheduling**: This is a variation of round-robin scheduling, where the tasks have different priorities and are executed in a priority-based order. Each task is given a time slice proportional to its priority, and then the CPU switches to the next task in the queue. This type of scheduling can provide a trade-off between priority and fairness, but it can also cause starvation for low-priority tasks and inefficiency for high-priority tasks. Time slice scheduling is suitable for systems that have multiple tasks with different importance and characteristics. 

- **Priority scheduling**: This is a general type of preemptive scheduling, where the tasks have different priorities and are executed in a priority-based order. The task with the highest priority is always selected to run on the CPU, and the lower-priority tasks are preempted if a higher-priority task becomes ready. This type of scheduling can provide the best performance and predictability for high-priority tasks, but it can also cause starvation for low-priority tasks and priority inversion for tasks that share resources. Priority scheduling is suitable for systems that have real-time requirements and need to meet deadlines.  

- **Composite scheduling**: This is a type of scheduling that combines different scheduling algorithms to achieve the desired system behavior. For example, a system can use priority scheduling for real-time tasks and round-robin scheduling for non-real-time tasks, or a system can use time slice scheduling for periodic tasks and priority scheduling for aperiodic tasks. Composite scheduling can provide flexibility and adaptability for systems that have diverse and dynamic task requirements.



### Interfacing

- Interfacing is the process of connecting and communicating between different components of an embedded system, such as sensors, actuators, microcontrollers, memory, peripherals, and software.
- Interfacing is essential for the functionality and performance of embedded systems, as it enables data exchange, control, synchronization, and coordination among the system components.
- Interfacing can be classified into two types: digital and analog.
  - Digital interfacing involves the use of binary signals (0 or 1) to represent data and commands. Digital interfacing can be further divided into parallel and serial communication, depending on whether multiple bits are transmitted simultaneously or sequentially.
  - Analog interfacing involves the use of continuous signals (such as voltage or current) to represent data and commands. Analog interfacing requires the use of converters (such as ADC or DAC) to convert between analog and digital domains.
- Interfacing can also be classified into two levels: hardware and software.
  - Hardware interfacing refers to the physical connection and electrical compatibility between the system components. Hardware interfacing requires the consideration of factors such as voltage levels, current ratings, impedance, noise, interference, and timing.
  - Software interfacing refers to the logical communication and protocol compatibility between the system components. Software interfacing requires the consideration of factors such as data format, encoding, error detection, flow control, and synchronization.
- Interfacing is a challenging and multidisciplinary task that requires the skills of both electrical and computer engineering. Interfacing design involves the selection of appropriate components, interfaces, and protocols for a given application and system requirements. Interfacing design also involves the implementation and testing of the interface functionality and performance.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Serial for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Serial
- Serial communication is a method of transmitting data bit by bit over a single wire or channel.
- Serial communication is used for connecting peripheral devices, such as keyboards, mice, modems, sensors, etc., to embedded systems or computers.
- Serial communication can be synchronous or asynchronous, depending on whether a clock signal is used to synchronize the sender and receiver.
- Synchronous serial communication requires a separate clock line to transmit the timing information along with the data. Examples of synchronous serial protocols are SPI, I2C, CAN, etc.
- Asynchronous serial communication does not use a clock line, but relies on the sender and receiver to agree on the data rate, the number of bits per character, the parity bit, and the stop bit. Examples of asynchronous serial protocols are UART, RS-232, RS-485, etc.
- Serial communication can be full-duplex or half-duplex, depending on whether the data can be transmitted and received simultaneously or not.
- Full-duplex serial communication allows both the sender and receiver to send and receive data at the same time. This requires two data lines, one for transmission and one for reception. Examples of full-duplex serial protocols are SPI, RS-232, etc.
- Half-duplex serial communication allows only one direction of data transfer at a time. This can use a single data line that is shared by the sender and receiver, or two data lines that are switched between transmission and reception. Examples of half-duplex serial protocols are I2C, CAN, RS-485, etc.
- Serial communication can be point-to-point or point-to-multipoint, depending on whether the data is sent to a single destination or multiple destinations.
- Point-to-point serial communication involves a single sender and a single receiver. This is the simplest and most reliable form of serial communication. Examples of point-to-point serial protocols are SPI, UART, etc.
- Point-to-multipoint serial communication involves a single sender and multiple receivers, or multiple senders and a single receiver, or multiple senders and multiple receivers. This requires a bus or a network topology to connect the devices. Examples of point-to-multipoint serial protocols are I2C, CAN, RS-485, etc.



### Parallel Computing

- Parallel computing is a type of computation in which many calculations or processes are carried out simultaneously.
- Parallel computing can improve the performance, efficiency, and scalability of embedded systems by exploiting the concurrency and parallelism of tasks.
- Parallel computing can be implemented at different levels of granularity, such as bit-level, instruction-level, data-level, and task-level.
- Parallel computing can be achieved by using different architectures, such as symmetric multiprocessors (SMP), massively parallel processors (MPP), parallel vector processors (PVP), distributed shared memory clusters (DSM), and clusters of workstations (COW).
- Parallel computing requires a parallel programming model that specifies how the tasks are divided, assigned, synchronized, and communicated among the processors.
- Parallel computing faces several challenges, such as load balancing, communication overhead, synchronization, scalability, and fault tolerance.



### Interrupt Handling

- An interrupt is a signal to the processor emitted by hardware or software that indicates an event that needs immediate attention.
- Interrupts are indispensable when writing any practical embedded firmware, as they allow the CPU to respond to external events that are not synchronized to the software running on the system .
- Interrupts can be classified into two types: software interrupts and hardware interrupts.
  - Software interrupts are called from software, using a specified command. They are used to invoke system calls or exception handlers.
  - Hardware interrupts are triggered by peripheral devices outside the micro-controller, such as timers, sensors, buttons, serial ports, etc .
- Interrupts have several advantages over polling, such as reducing CPU overhead, improving responsiveness, simplifying code structure, and saving power.
- Interrupts also have some challenges, such as ensuring atomicity, avoiding race conditions, managing priorities, handling nested interrupts, and minimizing latency .
- Interrupt handling involves the following steps :
  - When an interrupt request (IRQ) signal is detected by the CPU, it completes the current instruction and saves the necessary stack pointer and program counter (PC) information somewhere in RAM allocated for the current function.
  - The CPU then jumps to a predefined address in the memory, where the interrupt vector table (IVT) is stored. The IVT contains the addresses of the interrupt service routines (ISRs) for each interrupt source.
  - The CPU fetches the address of the ISR corresponding to the interrupt source from the IVT and jumps to that address to execute the ISR.
  - The ISR performs the necessary actions to handle the interrupt, such as reading or writing data from or to the peripheral device, clearing the interrupt flag, and sending an acknowledgement signal to the interrupt controller .
  - The ISR returns from the interrupt by restoring the stack pointer and PC information from the RAM and resuming the execution of the interrupted function.
- Interrupt handling can be affected by several factors, such as the number of interrupt sources, the frequency of interrupts, the duration of ISRs, the priority of interrupts, the type of interrupt controller, and the architecture of the CPU .
- Interrupt handling can be improved by following some best practices, such as keeping the ISRs short and simple, avoiding blocking or busy-waiting in ISRs, using interrupt masking or disabling to prevent unwanted interrupts, using interrupt nesting or preemption to handle higher priority interrupts, and using interrupt synchronization or locking mechanisms to protect shared resources .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on Linux device drivers for the unit 1 of embedded OS internals:

### Linux Device Drivers

- A device driver is a software component that allows the kernel to communicate with a specific piece of hardware without knowing the details of how the hardware works.
- Device drivers are usually written in C and follow the Linux kernel coding style.
- Device drivers can be built separately from the rest of the kernel and loaded at runtime as modules. This makes them easier to write, maintain and update.
- Device drivers can be classified into three types based on the type of device they control:
  - Character device drivers: These drivers handle devices that can be accessed as a stream of bytes, such as keyboards, mice, serial ports, etc. They provide a file-like interface to the user space applications.
  - Block device drivers: These drivers handle devices that can be accessed as a collection of fixed-size blocks, such as hard disks, CD-ROMs, etc. They provide a block device interface to the user space applications.
  - Network device drivers: These drivers handle devices that can send or receive packets of data over a network, such as Ethernet cards, wireless adapters, etc. They provide a network interface to the user space applications.
- Device drivers interact with the kernel through various mechanisms, such as system calls, ioctl, procfs, sysfs, device files, etc.
- Device drivers can also register callbacks for various events, such as interrupts, timers, work queues, etc.
- Device drivers can use various kernel services, such as memory management, synchronization, locking, debugging, etc.
- Device drivers can also implement various features, such as power management, hot-plugging, DMA, etc.




### Characteristics of Embedded Operating Systems

An embedded operating system is a computer operating system designed for use in embedded computer systems. These operating systems are designed to be small, resource-efficient, dependable, and reduce many features that aren't required by specialized applications .

Some of the main characteristics of embedded operating systems are:

- **Direct use of interrupts**: Embedded operating systems can handle interrupts from various sources, such as sensors, timers, or communication devices, without relying on a general-purpose interrupt handler. This allows for faster and more predictable response times.
- **Reactive operation**: Embedded operating systems are often event-driven, meaning they react to external stimuli and perform the appropriate actions. This requires a high degree of concurrency and synchronization among different tasks.
- **Real-time operation**: Embedded operating systems must meet strict timing constraints and deadlines, as the performance of the system depends on the timely execution of tasks. This requires the use of scheduling algorithms and priority mechanisms to ensure that the most critical tasks are executed first.
- **Streamlined protection mechanisms**: Embedded operating systems often have simplified or minimal protection mechanisms, such as memory management, access control, or exception handling, as they are designed to run on dedicated hardware with limited resources. This reduces the overhead and complexity of the system, but also increases the risk of errors or security breaches.
- **I/O device flexibility**: Embedded operating systems must support a wide range of input/output devices, such as sensors, actuators, displays, keyboards, or cameras, that are specific to the application domain. This requires the use of device drivers and interfaces that can communicate with the hardware and the application layer.
- **Application-specific customization**: Embedded operating systems are often tailored to the needs and requirements of the application and the hardware platform, as they are not intended to run general-purpose software. This allows for optimizing the performance, functionality, and reliability of the system, but also reduces the portability and compatibility of the operating system .



Hello, I am Sydney, your AI assistant. I can help you with your notes on USB for the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM. Here is some information that you might find useful:

### USB

- USB stands for **Universal Serial Bus**    , a standardized technology for attaching peripheral devices to a computer .
- USB enables communication and power supply between devices and a host controller such as a personal computer (PC) or smartphone.
- USB was first introduced in 1996 by a number of American companies, including IBM, Intel Corporation, and Microsoft Corporation, as a simpler way of connecting hardware to personal computers (PCs).
- USB has several advantages over other interfaces, such as:
  - It supports **plug and play**, which means that devices can be connected and disconnected without restarting the computer or installing drivers .
  - It supports **hot swapping**, which means that devices can be replaced while the system is running without affecting the operation of other devices .
  - It supports **daisy chaining**, which means that multiple devices can be connected to a single port using hubs or adapters  .
  - It supports **high-speed data transfer**, which can reach up to 10 Gbps for USB 3.1 .
  - It supports **power delivery**, which can provide up to 100 W of power to devices using USB Type-C connectors .
- USB has several versions, each with different specifications and features, such as:
  - USB 1.0: The first version, released in 1996, with a maximum data rate of 12 Mbps .
  - USB 1.1: An improved version, released in 1998, with minor changes and bug fixes .
  - USB 2.0: A major upgrade, released in 2000, with a maximum data rate of 480 Mbps and backward compatibility with USB 1.1 .
  - USB 3.0: A significant improvement, released in 2008, with a maximum data rate of 5 Gbps and backward compatibility with USB 2.0 .
  - USB 3.1: A further enhancement, released in 2013, with a maximum data rate of 10 Gbps and backward compatibility with USB 3.0 .
  - USB 3.2: A minor update, released in 2017, with a maximum data rate of 20 Gbps and backward compatibility with USB 3.1 .
  - USB 4: The latest version, released in 2019, with a maximum data rate of 40 Gbps and backward compatibility with USB 3.2 .
- USB has several types of connectors, each with different shapes and sizes, such as:
  - USB Type-A: The most common and standard connector, with a rectangular shape and four pins .
  - USB Type-B: A square-shaped connector, with four pins, used for printers and scanners .
  - USB Type-C: A reversible connector, with 24 pins, used for smartphones and laptops .
  - USB Mini-A: A smaller version of USB Type-A, with five pins, used for older devices .
  - USB Mini-B: A smaller version of USB Type-B, with five pins, used for older devices .
  - USB Micro-A: A smaller version of USB Type-A, with five pins, used for newer devices .
  - USB Micro-B: A smaller version of USB Type-B, with five pins, used for newer devices .
- USB has several modes of operation, each with different functions and protocols, such as:
  - USB Host Mode: The mode in which the device acts as a host



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Block & Network for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Block & Network

- A block device is a device that stores or transfers data in fixed-sized units called blocks. Examples of block devices are hard disks, flash drives, CD-ROMs, etc.
- A network device is a device that communicates with other devices over a network using protocols such as TCP/IP, UDP, etc. Examples of network devices are network interface cards, routers, switches, etc.
- Block and network devices are important for embedded systems because they provide access to external resources such as files, databases, web services, etc.
- Embedded OSes need to support block and network devices by providing device drivers, file systems, network stacks, and application interfaces.
- Device drivers are software modules that control the operation of a specific device. They communicate with the device hardware using registers, interrupts, DMA, etc. They also provide a standard interface to the OS kernel and user applications.
- File systems are software modules that organize the data on a block device into a hierarchical structure of files and directories. They provide operations such as create, delete, read, write, etc. They also manage the allocation and deallocation of disk space, metadata, and permissions.
- Network stacks are software modules that implement the network protocols for data communication. They provide operations such as send, receive, connect, disconnect, etc. They also manage the packet processing, routing, addressing, and security.
- Application interfaces are software modules that provide a high-level abstraction of the block and network devices to the user applications. They provide operations such as open, close, read, write, etc. They also handle the error handling, buffering, caching, and synchronization.



## Unit 2 - OPEN SOURCE RTOS

- An open source RTOS is a real-time operating system (RTOS) whose source code is publicly available and can be modified and distributed by anyone.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, meaning that tasks are completed within a specified time frame and with predictable results.
- Some of the benefits of using an open source RTOS are:
  - It can be more reliable and secure than proprietary software, because the source code is open and available for anyone to review and improve.
  - It can be more flexible and adaptable to different hardware platforms and application requirements, because the source code can be customized and optimized by the users.
  - It can reduce the development cost and time, because the users can leverage the existing code base and community support.
- Some of the challenges of using an open source RTOS are:
  - It may require more technical skills and resources to maintain and update the code, especially if the users modify the code extensively.
  - It may have compatibility and interoperability issues with other software components or devices, especially if the code is not standardized or certified.
  - It may have legal and licensing implications, depending on the type and terms of the open source license.
- Some of the examples of open source RTOS are:
  - FreeRTOS: A market-leading RTOS for microcontrollers and small microprocessors, distributed freely under the MIT open source license, with a kernel and a growing set of IoT libraries.
  - OpenRTOS: A commercially licensed version of FreeRTOS that includes indemnification and dedicated support, provided by WITTENSTEIN high integrity systems, an AWS strategic partner.
  - Zephyr: A scalable RTOS for IoT devices, supported by the Linux Foundation, with a modular design and a rich set of features and protocols.
  - RTEMS: A mature RTOS for embedded systems, developed by the open source community, with a focus on standards compliance and portability.

: Securing open source RTOS software - Embedded.com
: FreeRTOS - Market leading RTOS (Real Time Operating System) for ...
: Comparison of real-time operating systems - Wikipedia
: OpenRTOS - FreeRTOS
: Zephyr Project: Home
: RTEMS Project - Home



Hello, I am Sydney, your AI assistant. I can help you with your notes on the basics of RTOS. Here is some information that I found from the web:

### Basics of RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system.
- An RTOS creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides the necessary hard real-time computing capabilities, which means it can process data and events that have critically defined time constraints.
- An RTOS is used for controlling devices that require timing synchronization with their environment or with other devices.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS can be classified into three types based on the time limit for completing the critical tasks:
  - Hard real-time operating system: These operating systems guarantee that critical tasks be completed within a range of time. For example, a missile system or a pacemaker.
  - Soft real-time operating system: These operating systems provide some relaxation in the time limit. For example, a video streaming or a voice over IP application.
  - Firm real-time operating system: These operating systems have to complete the critical tasks before the deadline, but missing the deadline occasionally is acceptable. For example, a web server or a database system.
- An RTOS consists of the following basic components:
  - Kernel: The core of the RTOS that provides the basic services, such as thread management, memory management, inter-thread communication, and synchronization.
  - Device drivers: The software modules that interface with the hardware devices, such as sensors, actuators, or communication modules.
  - Middleware: The software layer that provides additional services, such as networking, file system, or graphical user interface.
  - Application: The software that implements the specific functionality of the embedded system, such as control logic, data processing, or user interaction.




# Real-time concepts for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A **real-time operating system (RTOS)** is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what is usually called a "hard" real-time operating system, if the calculation could not be performed for making the object available at the designated time, the operating system would terminate with a failure. In a "soft" real-time operating system, the assembly line would continue to function but the production output might be lower as objects failed to appear at their designated time, causing the robot to be temporarily unproductive. Some real-time operating systems are created for a special application and others are more general purpose. Some existing general purpose operating systems claim to be real-time operating systems. To some extent, almost any general purpose operating system such as Microsoft's Windows 2000 or IBM's OS/390 can be evaluated for its real-time operating system qualities. That is, even if an operating system doesn't qualify, it may have characteristics that enable it to perform in a satisfactory manner for a specific application. A real-time operating system that can usually or generally meet a deadline is a **soft real-time operating system**. A real-time operating system that can absolutely guarantee to meet a deadline is a **hard real-time operating system**.

- An **open source real-time operating system (OSRTOS)** is a real-time operating system that is distributed under an open source license, which allows anyone to access, modify, and redistribute the source code. Open source real-time operating systems are typically designed for embedded systems that require predictable timing behavior and high reliability. Some of the benefits of using an open source real-time operating system are:

  - **Cost-effectiveness**: Open source real-time operating systems are usually free or low-cost, which can reduce the development and maintenance costs of embedded systems.
  - **Customizability**: Open source real-time operating systems can be tailored to the specific needs and requirements of the application and the hardware platform, which can improve the performance and efficiency of the system.
  - **Portability**: Open source real-time operating systems can be easily ported to different architectures and platforms, which can increase the compatibility and interoperability of the system.
  - **Security**: Open source real-time operating systems can be audited and verified by the community, which can enhance the security and reliability of the system.
  - **Innovation**: Open source real-time operating systems can benefit from the collective knowledge and expertise of the community, which can foster innovation and improvement of the system.

- Some examples of open source real-time operating systems are:

  - **RTEMS**: The Real-Time Executive for Multiprocessor Systems or RTEMS is an open source real-time operating system that supports open standard application programming interfaces (API) such as POSIX. It is used in space flight, medical, networking and many more embedded devices.
  - **Prex**: Prex is an open source, royalty-free, real-time operating system for embedded systems. It is designed and implemented for resource-constrained systems that require predictable timing behavior. The highly portable code of Prex is written in 100% ANSI C based on traditional microkernel architecture.
  - **eCos**: eCos is a free open source real-time operating system intended for embedded applications. The highly configurable nature of eCos allows the operating system to be customised to precise application requirements, delivering the best possible run-time performance and an optimised hardware resource footprint.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on hard real time and soft real time for the unit 2 of embedded systems and real time operating systems.

### Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-time applications.
- A real-time application is one that requires a timely response from the system, such as a control system, a multimedia system, or a gaming system.
- A real-time system can be classified into two types: hard real time and soft real time   .
- **Hard real time** systems are deterministic in nature, which means they guarantee to complete the tasks within the specified deadlines   .
- The deadlines in hard real time systems are absolute and cannot be missed, otherwise the system will fail or cause severe consequences   .
- Examples of hard real time systems are nuclear power plant control, air traffic control, pacemaker, missile guidance, etc  .
- **Soft real time** systems are probabilistic in nature, which means they try to meet the deadlines as much as possible, but they can tolerate some occasional misses   .
- The deadlines in soft real time systems are not strict and can be relaxed, as missing them will not cause system failure, but only degrade the quality of service or performance   .
- Examples of soft real time systems are video streaming, audio playback, online gaming, web browsing, etc  .
- The main difference between hard and soft real time systems is the degree of predictability and reliability they offer   .
- Hard real time systems are highly restrictive and require precise timing and synchronization, while soft real time systems are less strict and can adapt to dynamic situations   .
- Hard real time systems are more suitable for critical and safety-critical applications, while soft real time systems are more suitable for non-critical and user-centric applications   .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some differences between General Purpose OS and RTOS for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

- **Task scheduling**: In a General Purpose OS, the task scheduling is not based on the priority of the tasks, but on the availability of resources and the fairness of the system. The General Purpose OS can switch between different tasks very fast, creating an illusion of parallelism. In a RTOS, the task scheduling is based on the priority of the tasks, and the RTOS ensures that the highest priority task is always executed first. The RTOS can also preempt a lower priority task if a higher priority task becomes ready  .
- **Deterministic behavior**: In a General Purpose OS, the response time of the system is not guaranteed, and it can vary depending on the workload and the system state. The General Purpose OS is not suitable for applications that require strict timing constraints and predictable outcomes. In a RTOS, the response time of the system is bounded, and it can meet the deadlines of the tasks. The RTOS is suitable for applications that require real-time performance and deterministic behavior  .
- **Kernel mode**: In a General Purpose OS, the kernel mode is non-preemptive, meaning that a kernel call cannot be interrupted by another task. This can cause delays and jitter in the system, and affect the real-time performance. In a RTOS, the kernel mode is preemptive, meaning that a kernel call can be interrupted by a higher priority task. This can reduce the latency and improve the responsiveness of the system.
- **Application domain**: In a General Purpose OS, the application domain is broad and diverse, and the General Purpose OS can run various types of applications, such as web browsers, word processors, games, etc. The General Purpose OS is designed for high-end, general purpose systems, such as personal computers, workstations, servers, etc. In a RTOS, the application domain is narrow and specific, and the RTOS can run specialized applications, such as control systems, embedded systems, robotics, etc. The RTOS is designed for low-end, stand-alone devices, such as ATMs, vending machines, kiosks, etc .
- **Size and complexity**: In a General Purpose OS, the size and complexity of the system is large and high, and the General Purpose OS can provide various features and services, such as memory management, file system, network, security, etc. The General Purpose OS can consume more resources and power, and require more maintenance and updates. In a RTOS, the size and complexity of the system is small and low, and the RTOS can provide minimal features and services, such as task management, synchronization, communication, etc. The RTOS can consume less resources and power, and require less maintenance and updates .




### Basic architecture of an RTOS

An RTOS (Real-Time Operating System) is a specialized operating system that provides deterministic and predictable behavior for time-critical applications. An RTOS typically consists of the following components  :

- **The kernel**: The kernel is the core component of the RTOS that manages the tasks, interrupts, timers, memory, and communication. The kernel can be either monolithic (all components run in a single space) or microkernel (different components run in separate spaces) in design.
- **The tasks**: The tasks are the basic units of execution in the RTOS. Each task has a priority, a stack, a context, and a state. The tasks can be either periodic (executed at fixed intervals) or aperiodic (executed on demand) in nature. The tasks can communicate and synchronize with each other using various mechanisms, such as message queues, semaphores, mutexes, events, signals, etc .
- **The scheduler**: The scheduler is the component that decides which task to run next based on the priority, deadline, and resource availability of the tasks. The scheduler can be either preemptive (higher priority tasks can interrupt lower priority tasks) or cooperative (tasks voluntarily yield the CPU to other tasks) in nature. The scheduler can also implement different algorithms, such as rate-monotonic, earliest deadline first, round-robin, etc .
- **The interrupt handler**: The interrupt handler is the component that handles the external and internal interrupts that occur during the execution of the tasks. The interrupt handler can either directly execute the interrupt service routine (ISR) or defer it to a lower priority task. The interrupt handler can also mask or unmask the interrupts to avoid conflicts or priority inversion .
- **The timer**: The timer is the component that provides the timing services for the tasks and the kernel. The timer can either use a hardware timer or a software timer to generate periodic or one-shot interrupts. The timer can also provide functions for measuring the elapsed time, setting the deadlines, and delaying the tasks .
- **The memory manager**: The memory manager is the component that manages the allocation and deallocation of the memory for the tasks and the kernel. The memory manager can either use a static or a dynamic memory allocation scheme. The memory manager can also provide functions for memory protection, fragmentation, and garbage collection .
- **The communication manager**: The communication manager is the component that manages the communication between the tasks and the external devices or networks. The communication manager can either use a serial or a parallel communication protocol. The communication manager can also provide functions for error detection, flow control, and encryption .

The following diagram shows a general architecture of an RTOS:

RTOS Architecture

: https://www.engineersgarage.com/rtos-real-time-operating-system/
: https://www.windriver.com/solutions/learning/rtos
: https://microcontrollerslab.com/rtos-real-time-operating-system/



### Scheduling Systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A scheduling system is a component of a real-time operating system (RTOS) that decides which task to execute next based on some criteria and constraints.
- A scheduling system can be classified into two types: static and dynamic.
  - Static scheduling systems assign priorities to tasks before execution and do not change them during execution. Static scheduling systems are simpler and faster, but less flexible and adaptive to changing situations.
  - Dynamic scheduling systems assign or change priorities to tasks during execution based on some factors such as deadlines, arrival times, resource availability, etc. Dynamic scheduling systems are more complex and slower, but more flexible and adaptive to changing situations.
- A scheduling system can also be classified into two types: preemptive and non-preemptive.
  - Preemptive scheduling systems allow a higher priority task to interrupt and suspend a lower priority task that is currently executing. Preemptive scheduling systems are more responsive and suitable for real-time systems, but may incur more overhead and complexity due to context switching and synchronization issues.
  - Non-preemptive scheduling systems do not allow a higher priority task to interrupt a lower priority task that is currently executing. Non-preemptive scheduling systems are simpler and incur less overhead, but may cause delays and missed deadlines for higher priority tasks.
- A scheduling system can also be classified into two types: global and local.
  - Global scheduling systems assign tasks to any available processor in a multiprocessor system based on some criteria and constraints. Global scheduling systems are more efficient and balanced, but may incur more overhead and complexity due to inter-processor communication and synchronization issues.
  - Local scheduling systems assign tasks to a specific processor in a multiprocessor system based on some criteria and constraints. Local scheduling systems are simpler and incur less overhead, but may cause unbalanced load and resource utilization among processors.
- Some common scheduling algorithms for real-time systems are  :
  - Rate Monotonic Scheduling (RMS): A static, preemptive, local scheduling algorithm that assigns priorities to tasks based on their periods (inverse of frequency). The shorter the period, the higher the priority. RMS is optimal for periodic tasks with fixed deadlines and execution times.
  - Earliest Deadline First (EDF): A dynamic, preemptive, global scheduling algorithm that assigns priorities to tasks based on their deadlines. The earlier the deadline, the higher the priority. EDF is optimal for periodic or aperiodic tasks with arbitrary deadlines and execution times.
  - Least Laxity First (LLF): A dynamic, preemptive, global scheduling algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. LLF is optimal for periodic or aperiodic tasks with arbitrary deadlines and execution times.
  - Maximum Urgency First (MUF): A dynamic, preemptive, global scheduling algorithm that assigns priorities to tasks based on their urgency. The urgency of a task is a function of its deadline, execution time, and resource requirements. The higher the urgency, the higher the priority. MUF is optimal for periodic or aperiodic tasks with arbitrary deadlines, execution times, and resource requirements.



### Inter-process communication for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Inter-process communication (IPC) is a form of data sharing between processes that happen with RTOS.
- IPC is essential for creating useful applications that can use resources, peripherals, and events efficiently and dynamically.
- IPC can be implemented using various techniques, such as shared memory, pipes, queues, mailboxes, signals, and remote procedure calls.
- Different open source RTOSes may offer different IPC APIs and features, depending on their design and architecture.
- One of the most popular open source RTOSes is FreeRTOS, which provides a rich set of IPC APIs, such as:
  - Binary and counting semaphores, which are used to synchronize tasks and share resources .
  - Mutexes, which are a special type of semaphore that provide priority inheritance and recursive locking .
  - Event groups, which are used to notify tasks of the occurrence of multiple events or conditions .
  - Message buffers, which are used to send and receive variable length messages between tasks or interrupts .
  - Stream buffers, which are used to send and receive streams of data between tasks or interrupts .
  - Notifications, which are used to send and receive single 32-bit values between tasks or interrupts .
  - Queues, which are used to send and receive fixed length messages between tasks or interrupts .
  - Queue sets, which are used to monitor multiple queues and semaphores for events .
  - Software timers, which are used to execute callback functions at specified intervals or after a delay .
- Other open source RTOSes, such as Zephyr, RIOT, and Contiki, may have similar or different IPC APIs and features, depending on their design and architecture.
- IPC is a crucial aspect of RTOS development and application, as it enables concurrent and cooperative processes to communicate and coordinate effectively.



### Performance Metrics in Scheduling Models for Open Source RTOS

- Performance metrics are the criteria used to evaluate and compare the performance of real-time operating systems (RTOS) in terms of their ability to meet the timing constraints and resource requirements of real-time applications.
- Some of the common performance metrics for RTOS scheduling models are :
  - **Memory**: The amount of ROM and RAM needed by the RTOS kernel and the application, and how it is affected by the configuration and options of the RTOS.
  - **Latency**: The delay between an event occurrence and the response of the RTOS to that event, such as interrupt latency, context switch latency, and task dispatch latency.
  - **Throughput**: The number of tasks or operations that can be completed by the RTOS in a given time interval, such as task execution rate, task completion rate, and task utilization rate.
  - **Jitter**: The variation in the timing of the RTOS events, such as task arrival time, task start time, task finish time, and task deadline.
  - **Reliability**: The ability of the RTOS to handle errors and faults without compromising the system functionality and performance, such as fault tolerance, fault recovery, and fault prevention.
  - **Scalability**: The ability of the RTOS to adapt to the changes in the system workload and resources, such as task priority, task dependency, task synchronization, and task migration.
- Open source RTOS are RTOS that are freely available and modifiable by the users, and that have a community of developers and users that contribute to their improvement and maintenance.
- Some of the advantages of open source RTOS are :
  - **Cost**: Open source RTOS are free of charge and do not require any license fees or royalties to use them.
  - **Flexibility**: Open source RTOS can be customized and modified according to the specific needs and preferences of the users and the applications.
  - **Quality**: Open source RTOS are subject to peer review and testing by a large and diverse community of developers and users, which can enhance their quality and reliability.
  - **Innovation**: Open source RTOS can benefit from the collective creativity and expertise of the community, which can lead to new features and improvements.
- Some of the disadvantages of open source RTOS are :
  - **Support**: Open source RTOS may not have a dedicated or reliable support service, and the users may have to rely on the community or their own skills to solve any issues or problems.
  - **Documentation**: Open source RTOS may not have a comprehensive or consistent documentation, and the users may have to search for the relevant information from various sources or learn by trial and error.
  - **Compatibility**: Open source RTOS may not be compatible with some hardware platforms or software tools, and the users may have to deal with the integration and interoperability issues.
  - **Security**: Open source RTOS may have some vulnerabilities or bugs that can compromise the security and privacy of the system and the data, and the users may have to update and patch the RTOS regularly.
- Some of the examples of open source RTOS are :
  - **FreeRTOS**: A popular and widely used open source RTOS that supports multiple architectures and platforms, and that provides a simple and lightweight kernel with basic features such as preemptive or cooperative multitasking, task priority, task synchronization, and memory management.
  - **Linux**: A general-purpose open source operating system that can be configured and modified to run as an RTOS, and that provides a rich and powerful kernel with advanced features such as interrupt handling, scheduling algorithms, inter-process communication, device drivers, and file systems.
  - **Zephyr**: A new and emerging open source RTOS that aims to support the Internet of Things (IoT) applications, and that provides a scalable and modular kernel with features such as event-driven programming, power management, network protocols, and security mechanisms.
  - **RIOT**: Another open source RTOS that targets the IoT applications, and that provides a flexible and efficient kernel with features such as real-time capabilities, multi-threading, message passing, timers, and sensors support.



### Interrupt management in RTOS environment

- Interrupts are events that occur asynchronously and require immediate attention from the processor.
- Interrupts can be triggered by external devices, such as sensors, timers, or communication interfaces, or by internal sources, such as software exceptions or system calls.
- Interrupts can improve the responsiveness and efficiency of an embedded system, but they can also introduce challenges for the real-time operating system (RTOS) and the application.
- Interrupt management in RTOS environment involves the following aspects:

  - Interrupt service routines (ISRs): These are the functions that are executed when an interrupt occurs. They should be short and simple, and avoid blocking or calling RTOS services that may cause context switches or delays. ISRs can communicate with other threads, such as tasks, using mechanisms such as semaphores, queues, or event flags .
  - Interrupt priority: This is the relative importance of an interrupt compared to other interrupts and threads. Higher priority interrupts can preempt lower priority ones, and can also preempt the RTOS scheduler and tasks. Interrupt priority should be carefully assigned to avoid priority inversion, starvation, or deadlock .
  - Interrupt latency: This is the time between the occurrence of an interrupt and the execution of the corresponding ISR. Interrupt latency can be affected by factors such as the processor architecture, the interrupt controller, the RTOS interrupt dispatcher, and the nesting and masking of interrupts. Interrupt latency should be minimized and bounded to meet the real-time requirements of the system .
  - Interrupt load: This is the amount of processor time consumed by the interrupts. Interrupt load can be measured by the interrupt frequency, the interrupt duration, and the interrupt overhead. Interrupt load should be balanced with the processor utilization and the task deadlines to avoid overloading the system or degrading the performance .



### Memory management for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Memory management is the process of allocating and deallocating memory for the tasks and objects in an RTOS.
- Memory management can be done in two ways: static or dynamic.
- Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This method is simple, fast, and deterministic, but it can waste memory and limit flexibility.
- Dynamic memory management means that the memory is allocated and freed at run time, according to the needs of the application. This method is more flexible and efficient, but it can introduce overhead, fragmentation, and non-determinism.
- An open source RTOS is an RTOS that has its source code available for anyone to use, modify, and distribute. Some examples of open source RTOS are FreeRTOS, Zephyr, and Azure RTOS.
- An open source RTOS may use different memory management options, depending on its design and features. Some common options are:
  - Heap: A heap is a pool of memory that can be dynamically allocated and freed by the RTOS or the application. A heap can be implemented using different algorithms, such as first fit, best fit, or worst fit. A heap can provide flexibility and efficiency, but it can also cause fragmentation, overhead, and non-determinism.
  - Stack: A stack is a region of memory that is allocated and freed in a last-in, first-out (LIFO) order. A stack is typically used to store local variables and function call information for each task. A stack can provide speed and determinism, but it can also waste memory and cause stack overflow or underflow.
  - Pool: A pool is a collection of fixed-size memory blocks that can be allocated and freed by the RTOS or the application. A pool can reduce fragmentation and overhead, but it can also limit flexibility and cause pool exhaustion.
  - Static: Static memory management means that the memory is allocated at compile time and cannot be changed at run time. This option can be used for tasks and objects that have fixed and known memory requirements. Static memory management can provide simplicity, speed, and determinism, but it can also waste memory and limit flexibility.



### File systems for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A file system is a software component that manages the storage and retrieval of data on a persistent storage device, such as a hard disk, flash memory, or optical disc.
- A file system organizes data into files, directories, and other structures, and provides operations to create, delete, read, write, and modify them.
- A file system also maintains metadata, such as file names, attributes, permissions, timestamps, and checksums, to ensure data integrity and security.
- A file system can be implemented in different ways, depending on the characteristics and requirements of the underlying hardware, the operating system, and the application domain.
- Some file systems are designed for general-purpose use, while others are optimized for specific scenarios, such as real-time, embedded, or distributed systems.
- A file system can be classified into two main types: disk-based and memory-based.
  - A disk-based file system manages data on a physical disk, such as a hard disk drive (HDD), a solid state drive (SSD), or a flash memory card. A disk-based file system typically uses a block device interface to access the disk sectors, and implements a logical structure on top of the physical layout. Examples of disk-based file systems are FAT, NTFS, ext4, and exFAT.
  - A memory-based file system manages data in the main memory (RAM) of a computer system, without using a physical disk. A memory-based file system can be either volatile or non-volatile. A volatile memory-based file system stores data only as long as the system is powered on, and loses all data when the system is turned off. A non-volatile memory-based file system preserves data across power cycles, by using a battery-backed RAM, a flash memory, or a hybrid of both. Examples of memory-based file systems are tmpfs, ramfs, and ROMFS.
- A file system can also be classified into two main categories: native and non-native.
  - A native file system is a file system that is supported by the operating system kernel, and can be accessed directly by the system calls and the application programming interface (API) of the operating system. A native file system is usually integrated with the operating system, and can take advantage of its features and services, such as memory management, process management, security, and synchronization. Examples of native file systems are ext4 for Linux, NTFS for Windows, and HFS+ for macOS.
  - A non-native file system is a file system that is not supported by the operating system kernel, and can be accessed only by a user-level application or a library that implements the file system functionality. A non-native file system is usually portable across different operating systems, and can be used for interoperability, compatibility, or special purposes. Examples of non-native file systems are FUSE, NFS, and Samba.
- A file system can also be classified into two main modes: transactional and non-transactional.
  - A transactional file system is a file system that guarantees the atomicity, consistency, isolation, and durability (ACID) properties of the data operations, even in the presence of failures, such as power loss, system crash, or hardware error. A transactional file system uses a journal, a log, or a copy-on-write mechanism to record the changes to the data, and to recover the data to a consistent state in case of a failure. Examples of transactional file systems are ZFS, Btrfs, and Reliance Edge.
  - A non-transactional file system is a file system that does not guarantee the ACID properties of the data operations, and may result in data corruption, inconsistency, or loss in the presence of failures. A non-transactional file system does not use any mechanism to record or recover the changes to the data, and relies on the application or the user to handle the failures. Examples of non-transactional file systems are FAT, ext2, and UFS.
- A file system can also be classified into two main types: single-level and multi-level.
  - A single-level file system is a file system that does not support directories or subdirectories, and stores all the files in a single flat namespace. A single-level file system is simple and fast, but has limited scalability and usability. Examples of single-level file systems are TFS and YAFFS.
  - A multi-level file system is a file system that supports directories and subdirectories, and organizes the files in



### I/O Systems

- I/O systems are the components that enable an embedded system or a real-time operating system (RTOS) to communicate with the external world, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
  - Parallel I/O systems transfer multiple bits of data simultaneously using multiple wires or pins. They are faster but require more hardware resources and wiring complexity. Examples of parallel I/O systems are parallel ports, GPIO (General Purpose Input/Output), and memory-mapped I/O.
  - Serial I/O systems transfer one bit of data at a time using one or few wires or pins. They are slower but require less hardware resources and wiring complexity. Examples of serial I/O systems are serial ports, UART (Universal Asynchronous Receiver/Transmitter), SPI (Serial Peripheral Interface), I2C (Inter-Integrated Circuit), and USB (Universal Serial Bus).
- I/O systems can also be classified into two modes: polling and interrupt-driven.
  - Polling mode is when the processor continuously checks the status of an I/O device to determine if it is ready to send or receive data. Polling mode is simple but consumes a lot of processor time and may cause delays or missed events.
  - Interrupt-driven mode is when the processor is notified by an I/O device when it is ready to send or receive data using a signal called an interrupt. Interrupt-driven mode is more efficient but requires more programming complexity and may cause conflicts or priority issues.
- I/O systems are essential for embedded systems and RTOS to perform their specific functions in a larger system, such as industrial machines, medical devices, automotive systems, etc. I/O systems must be designed and configured to meet the performance, reliability, and safety requirements of the application.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points on the advantages and disadvantages of RTOS for your notes:

### Advantages and disadvantages of RTOS

- RTOS stands for Real Time Operating System, which is a type of operating system that can process and respond to events or tasks within a specified time limit.
- RTOS is suitable for applications that require high performance, reliability, and predictability, such as embedded systems, robotics, industrial control, aerospace, and military.
- Some of the advantages of RTOS are:

  - Maximum consumption: RTOS can utilize the system resources efficiently and produce more output while keeping all devices active. There is little or no downtime in these systems  .
  - Task shifting: RTOS can switch between tasks quickly and with minimal overhead. For example, in older systems, it takes about 10 microseconds, while in RTOS, it takes about 3 microseconds.
  - Accuracy and consistency: RTOS can produce accurate and consistent results within the specified deadlines, which is essential for real-time applications.
  - Priority-based scheduling: RTOS can assign different priorities to different tasks and execute them accordingly, which ensures that the most important tasks are completed first .

- Some of the disadvantages of RTOS are:

  - Longer wait for low-priority tasks: As RTOS is programmed to execute priority tasks within specific deadlines, lower priority tasks may have to wait longer versus an OS.
  - Minimal task capacity: RTOS can only run a limited number of tasks simultaneously, as it has to allocate sufficient resources for each task. It is also not suitable for multi-tasking applications that require frequent context switching.
  - Complexity and cost: RTOS is more complex and costly to develop, maintain, and debug than a general-purpose OS, as it requires specialized skills, tools, and hardware .



### POSIX standards

- POSIX stands for **Portable Operating System Interface** and is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems.
- POSIX defines both the system and user-level application programming interfaces (APIs), along with command line shells and utility programs, for software compatibility with variants of Unix and other operating systems.
- POSIX is especially relevant for the development of real-time and embedded systems, as it promotes interoperability and portability of applications across different platforms and devices .
- POSIX consists of four major components, each in an associated volume:
  - **Base Definitions**: General terms, concepts, and interfaces common to all volumes of the standard, including utility conventions and C-language header definitions.
  - **System Interfaces**: Definitions for system services and functions, such as process creation and control, signals, timers, clocks, file and directory operations, pipes, streams, asynchronous and synchronous I/O, sockets, and threads.
  - **Shell and Utilities**: Definitions for a standard command language interpreter (shell), and over 100 utility programs, such as cp, ls, mv, ps, etc.
  - **Rationale**: Explanations for why the standard is the way it is, including historical information, design considerations, and trade-offs.
- POSIX also has several extensions that provide additional functionality for real-time and embedded systems, such as:
  - **POSIX.1b (or POSIX.4)**: Real-time extensions, such as priority scheduling, timers, clocks, semaphores, message queues, shared memory, and asynchronous I/O.
  - **POSIX.1c (or POSIX.4a)**: Threads extensions, such as thread creation and control, synchronization, cancellation, and specific data.
  - **POSIX.1d (or POSIX.5)**: Additional real-time extensions, such as sporadic server scheduling, memory locking, and synchronized I/O.
  - **POSIX.1j (or POSIX.6)**: Advanced real-time extensions, such as spin locks, barriers, reader-writer locks, and monotonic clocks.
  - **POSIX.1m (or POSIX.7)**: Embedded systems profile, which defines a subset of the POSIX functionality suitable for resource-constrained devices.
- The benefits of using POSIX standards for real-time and embedded systems include:
  - **Portability**: Applications written in POSIX can run on any POSIX-compliant operating system, reducing the cost and effort of porting and testing.
  - **Interoperability**: Applications written in POSIX can communicate and exchange data with other POSIX applications, regardless of the underlying hardware or software platform.
  - **Scalability**: Applications written in POSIX can take advantage of the features and capabilities of different operating systems, such as multi-core processors, memory management, security, and networking.
  - **Reliability**: Applications written in POSIX can benefit from the stability and robustness of the POSIX APIs, which have been tested and verified by many vendors and users.
  - **Flexibility**: Applications written in POSIX can choose from a variety of POSIX-compliant operating systems, such as Linux, BSD, QNX, VxWorks, etc., depending on their needs and preferences.



### RTOS Issues

- An RTOS is a real-time operating system that provides predictable and deterministic behavior for embedded applications that have strict timing requirements.
- However, using an RTOS also introduces some challenges and issues that developers need to be aware of and address in their design and implementation. Some of these issues are:

  - **Priority inversion**: This occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task. This results in the high-priority task waiting longer than expected for the resource, violating its timing constraints .
  - **Deadlock**: This occurs when two or more tasks are waiting for each other to release a resource, and none of them can proceed. This leads to a system-wide halt and a loss of responsiveness .
  - **Task jitter**: This occurs when a task experiences variations in its execution time due to factors such as preemption, interrupts, cache misses, and memory access delays. This can affect the accuracy and performance of the task, especially if it involves time-sensitive operations such as signal processing or control.
  - **Control-flow complexity**: This occurs when the logic and flow of the program becomes difficult to understand and debug, due to the dynamic and concurrent nature of RTOS tasks. The source code does not reflect the actual execution order of the tasks, and the RTOS scheduler decides which task to run at any given moment. This requires new debugging techniques such as tracing and profiling to analyze the system behavior.
  - **Security risks**: This occurs when the RTOS and the application are exposed to malicious attacks that can compromise the confidentiality, integrity, and availability of the system. The RTOS and the application need to implement and use security features such as encryption, authentication, authorization, and secure boot to protect the data and the code from unauthorized access and modification.
  - **Interrupt latency**: This occurs when the RTOS takes too long to respond to an external event, such as a sensor input or a timer expiration, that triggers an interrupt. The interrupt latency depends on factors such as the RTOS architecture, the interrupt handling mechanism, the priority of the interrupt, and the current state of the system. A high interrupt latency can cause missed events and inaccurate responses.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some notes on selecting a real-time operating system for the unit 2 of embedded systems and real-time operating system.

### Selecting a Real-Time Operating System

- A real-time operating system (RTOS) is a software that manages the resources and tasks of a system that has to meet strict timing constraints and performance requirements.
- A RTOS provides features such as preemptive multitasking, priority-based scheduling, inter-task communication and synchronization, interrupt handling, memory management, and device drivers.
- A RTOS is different from a general-purpose operating system (GPOS) in that it guarantees the completion of certain types of operations within a predefined, deterministic time span.
- A RTOS is suitable for embedded applications that have real-time constraints, such as airlines reservation system, air traffic control system, industrial automation, robotics, medical devices, etc.
- Selecting the right RTOS for a specific application is a critical decision that involves several factors and steps. Some of the steps are :

  - Step 1: Requirements review. The first step is to review the requirements for the OS, such as the functionality, performance, reliability, scalability, security, and compatibility of the system.
  - Step 2: Availability on target platform. The second step is to check if the RTOS is available for the chosen processor architecture and hardware platform. The RTOS should support the specific features and peripherals of the target hardware.
  - Step 3: Support of required functions. The third step is to evaluate the support of the RTOS for the required functions, such as networking, file system, graphical user interface, debugging, testing, etc.
  - Step 4: Portability. The fourth step is to assess the portability of the RTOS, which means the ease of migrating the application code and data from one platform to another. The RTOS should have a well-defined application programming interface (API) and a modular design that allows for reuse and adaptation of code.
  - Step 5: Being future-proof. The fifth step is to consider the future-proofness of the RTOS, which means the ability of the RTOS to cope with the changing requirements and technologies of the system. The RTOS should have a stable and active development, a large and supportive user community, and a clear roadmap and vision for the future.
  - Step 6: Existing internal experience. The sixth step is to leverage the existing internal experience and knowledge of the RTOS within the organization. The RTOS should be familiar and comfortable to the developers and engineers who will work on the system.
  - Step 7: Evaluate alternatives. The seventh step is to compare and contrast the alternatives of the RTOS, such as the features, benefits, drawbacks, costs, and risks of each option. The RTOS should be evaluated based on the specific criteria and goals of the system.
  - Step 8: Support, partnerships, working together. The eighth step is to consider the support, partnerships, and collaboration of the RTOS provider and the system vendor. The RTOS should have a reliable and responsive technical support, a strong and trustworthy partnership, and a cooperative and collaborative working relationship.

- Selecting the right RTOS for a system is a complex and important task that requires careful analysis and evaluation of the various factors and options. A RTOS should meet the needs and expectations of the system and the stakeholders, and provide a robust and efficient platform for the development and operation of the system.



### RTOS comparative study

A real-time operating system (RTOS) is an operating system that guarantees a certain capability within a specified time constraint. For example, an operating system might be designed to ensure that a certain object was available for a robot on an assembly line. In what follows, we will study some of the characteristics and features of different RTOSs and compare them.

Some of the criteria that can be used to compare RTOSs are:

- Size: The size of the RTOS refers to the amount of memory it occupies. A smaller RTOS can be more suitable for embedded systems with limited resources, while a larger RTOS can offer more functionality and features.
- Performance: The performance of the RTOS refers to how fast it can execute tasks, respond to interrupts, and switch between contexts. A higher performance RTOS can provide more predictable and reliable behavior for real-time applications, while a lower performance RTOS can be more prone to delays and jitter.
- Scalability: The scalability of the RTOS refers to how well it can adapt to different hardware platforms, application domains, and workload variations. A more scalable RTOS can support a wider range of devices and applications, while a less scalable RTOS can be more specialized and optimized for a specific use case.
- Standards compliance: The standards compliance of the RTOS refers to how well it conforms to the specifications and guidelines of recognized standards bodies, such as POSIX, ISO, or IEEE. A more standards compliant RTOS can offer more portability, interoperability, and compatibility with other systems and software, while a less standards compliant RTOS can be more proprietary and vendor-specific.
- Licensing: The licensing of the RTOS refers to the terms and conditions under which it can be used, modified, and distributed. A more open and free RTOS can offer more flexibility, transparency, and innovation, while a more closed and proprietary RTOS can offer more security, stability, and support.

Based on these criteria, we can compare some of the popular RTOSs in the market, such as:

- Zephyr: Zephyr is a small, open source RTOS that is designed for IoT devices and supports multiple architectures, such as ARM, x86, RISC-V, and others. It has a minimal configuration of 8KB, which includes threading, interrupts, and memory allocation, but can be extended with additional features, such as Bluetooth, networking, filesystem, and shell. It has a high performance and low latency, and supports various standards, such as POSIX, Bluetooth, and IEEE 802.15.4. It is licensed under the Apache 2.0 license, which allows for commercial and non-commercial use, modification, and distribution.
- LynxOS: LynxOS is a general purpose, POSIX-compliant RTOS that is designed for safety- and security-critical applications, such as aerospace, defense, industrial, and medical. It has a default configuration of 1.4MB, which includes thread and process support, floating point, filesystem, USB, networking, shell, and printf. It has a high performance and determinism, and supports various standards, such as POSIX, ARINC 653, FACE, and MILS. It is licensed under a proprietary license, which requires a fee and a contract for use, modification, and distribution.
- FreeRTOS: FreeRTOS is a popular, open source RTOS that is designed for embedded systems and supports multiple architectures, such as ARM, x86, MIPS, and others. It has a minimal configuration of 9KB, which includes threading, interrupts, timers, queues, and semaphores, but can be extended with additional features, such as networking, filesystem, USB, and shell. It has a high performance and low footprint, and supports various standards, such as POSIX, CMSIS, and MISRA. It is licensed under the MIT license, which allows for commercial and non-commercial use, modification, and distribution.

The following table summarizes the comparison of the RTOSs:

| Criterion | Zephyr | LynxOS | FreeRTOS |
| --- | --- | --- | --- |
| Size | 8KB - 16KB | 1.4MB | 9KB - 40KB |
| Performance | High | High | High |
| Scalability | High | Medium | High |
| Standards compliance | High | High | Medium |
| Licensing | Open | Proprietary | Open |

: https://en.wikipedia.org/wiki/Comparison_of_real-time_operating_systems

: https://www.lynx.com/embedded-system



## Unit 3 - REAL TIME KERNEL BASICS

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible.
- A real-time kernel ensures that time-critical events are processed with minimal and predictable delays .
- A real-time kernel simplifies the design of embedded systems by allowing the system to be divided into multiple independent elements called tasks .
- A real-time kernel supports two types of tasks: periodic and aperiodic.
  - Periodic tasks are tasks that execute at regular intervals and have deadlines to meet.
  - Aperiodic tasks are tasks that execute in response to external events and have variable execution times.
- A real-time kernel provides mechanisms for task creation, deletion, synchronization, communication, scheduling, and resource management.
- A real-time kernel can be classified into two categories: hard real-time and soft real-time.
  - Hard real-time kernels guarantee that all tasks meet their deadlines, even in the worst-case scenario.
  - Soft real-time kernels allow some tasks to miss their deadlines occasionally, but try to minimize the number and magnitude of deadline violations.
- A real-time kernel can be implemented in different ways, such as:
  - Modifying the standard kernel to reduce the latency and increase the responsiveness .
  - Developing a separate kernel that runs alongside the standard kernel and handles the real-time tasks .
  - Developing a microkernel that provides the minimal functionality and allows the user to customize the rest.
- A real-time kernel can be identified by executing the `uname -r` command on the terminal and looking for the `rt` keyword in the kernel version.



Hello, I am Sydney, your AI assistant. I can help you with your query.

### Converting a normal Linux kernel to real time kernel

- A normal Linux kernel is not fully preemptible, meaning that some parts of the kernel code cannot be interrupted by higher priority tasks. This can cause unpredictable delays and jitter in the execution of real time applications.
- A real time kernel is a modified version of the Linux kernel that allows full preemption of all kernel code, except for a few critical sections. This reduces the latency and improves the determinism of the real time applications.
- There are different ways to convert a normal Linux kernel to a real time kernel, depending on the distribution and the version of the kernel. Some of the common methods are:

  - Applying the RT-Preempt patch to the kernel source code and compiling it. The RT-Preempt patch converts the kernel locking primitives (such as spinlocks) to rtmutexes, which are preemptible. It also adds some features such as priority inheritance, threaded interrupts, and high-resolution timers.
  - Installing a pre-built real time kernel from a repository. Some distributions, such as CentOS, Ubuntu, and Arch Linux, provide real time kernels in their repositories or in external sources. For example, CentOS users can install the -ml series kernel from CERN, Ubuntu users can install the PREEMPT_RT kernel from Canonical, and Arch Linux users can install the linux-rt package from the AUR.
  - Using a real time Linux distribution. Some distributions, such as Red Hat Enterprise Linux for Real Time, are designed specifically for real time applications. They include a real time kernel and a set of tools and libraries to optimize the system performance and configuration.

- After converting the normal Linux kernel to a real time kernel, the user needs to reboot the system and select the real time kernel from the boot menu. The user also needs to adjust some system parameters, such as the CPU governor, the scheduler, the memory management, and the interrupt handling, to achieve the best real time performance.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here are some basic points about Xenomai:

- Xenomai is a real-time development software framework that cooperates with the Linux kernel to provide hard real-time computing support to user space applications .
- Xenomai allows real-time threads to run either in kernel space or in user space, with the benefit of memory protection and direct scheduling by Xenomai.
- Xenomai uses Linux as a background task and preempts it as a simple task, making the concept of impossible preemption and handlers obsolete.
- Xenomai consists of three main components: the RT-Nucleus, the RT-Skins, and the RT-Drivers .
- The RT-Nucleus is the core of Xenomai that provides the real-time services and the scheduling of the real-time threads.
- The RT-Skins are the interfaces that allow the user space applications to access the real-time services of the RT-Nucleus . They include POSIX, VxWorks, RTAI, and native APIs.
- The RT-Drivers are the device drivers that are compatible with the RT-Nucleus and can handle real-time interrupts and data transfers .




### Overview of Open source RTOS for Embedded systems (Free RTOS/ ChibiosRT) and application development

- An open source RTOS is a real-time operating system that is freely available for developers to use, modify, and distribute under a license that allows such actions.
- An RTOS is designed to support time-critical applications by providing deterministic execution of tasks, preemptive scheduling, interrupt handling, inter-task communication, and memory management.
- An embedded system is a computer system that is integrated with a specific hardware device and performs a dedicated function or functions. Embedded systems often have limited resources, such as memory, processing power, and battery life, and require high reliability and efficiency.
- Some examples of embedded systems are smart watches, medical devices, industrial controllers, automotive systems, and IoT devices.
- Some benefits of using an open source RTOS for embedded systems are:
  - Cost savings: Developers can avoid paying licensing fees or royalties for using a proprietary RTOS.
  - Customization: Developers can tailor the RTOS to their specific needs and preferences, and add or remove features as required.
  - Compatibility: Developers can ensure that the RTOS is compatible with their hardware platform and software tools, and avoid vendor lock-in or obsolescence.
  - Community: Developers can benefit from the support and collaboration of other developers who use the same RTOS, and contribute to its improvement and innovation.
- Some challenges of using an open source RTOS for embedded systems are:
  - Security: Developers need to ensure that the RTOS is secure and free of vulnerabilities, and apply patches and updates as needed.
  - Quality: Developers need to verify that the RTOS is reliable and stable, and meets the performance and functionality requirements of their application.
  - Documentation: Developers need to find and follow the documentation and guidelines for using the RTOS, and seek help from the community if needed.
  - Maintenance: Developers need to maintain and update the RTOS as the hardware and software environment changes, and fix any bugs or issues that arise.
- Some examples of open source RTOS for embedded systems are:
  - FreeRTOS: A market-leading RTOS for microcontrollers and small microprocessors, developed in partnership with the world's leading chip companies. It has a simple and intuitive API, and supports a wide range of architectures and features .
  - ChibiOS/RT: A compact and fast RTOS for embedded systems, designed for high performance and low resource usage. It supports multiple architectures and features, such as multithreading, synchronization, timers, memory management, and device drivers.
  - RTOS: An open source operating system for embedded devices developed by RT-Thread. It provides a standardized, friendly foundation for developers to program a variety of devices and includes a large number of useful libraries and toolkits to make the process easier. Like Linux, RTOS uses a modular approach, which makes it easy to extend .
- Application development for embedded systems using an open source RTOS involves the following steps:
  - Selecting the hardware platform and the RTOS that best suit the application requirements and constraints.
  - Configuring the RTOS to the specific hardware and software environment, and choosing the functionalities and features that are needed.
  - Writing the application code using the RTOS API and libraries, and following the best practices and guidelines for embedded programming.
  - Testing and debugging the application code using the RTOS tools and methods, and ensuring that the application meets the performance and functionality specifications.
  - Deploying and updating the application code to the embedded device, and monitoring and maintaining its operation and behavior.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of real time operating systems for the unit 3 - real time kernel basics in the subject of embedded systems and real time operating systems.

### Real Time Operating Systems

- A real time operating system (RTOS) is an operating system (OS) that processes data and events that have critically defined time constraints  .
- An RTOS is different from a general-purpose OS, such as Windows or Linux, which may not guarantee the timely execution of tasks or the predictability of response times  .
- An RTOS is designed for critical systems and devices that are timing-specific, such as embedded systems, industrial controllers, robotics, avionics, medical devices, etc  .
- An RTOS typically has two key features: predictability and determinism.
  - Predictability means that the RTOS can guarantee that a task will be completed within a specified deadline, regardless of the system load or other factors.
  - Determinism means that the RTOS can guarantee that the same input will always produce the same output and behavior, regardless of the timing or order of events.
- An RTOS usually consists of a kernel and a set of services or libraries that provide various functionalities, such as real-time multithreading, inter-thread communication and synchronization, memory management, interrupt handling, device drivers, file systems, network protocols, etc  .
- An RTOS can be classified into two types: hard real-time and soft real-time  .
  - A hard real-time system is one that must meet all the deadlines, otherwise the system may fail or cause severe consequences  .
  - A soft real-time system is one that can tolerate some missed deadlines, but the quality of service may degrade or the system may experience performance issues  .
- Some examples of RTOSes are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, RTLinux, etc .



Hello, I am Sydney, your AI assistant. I can help you with your notes on event-based real time kernels. Here is some content that you can use for your study material:

### Event based

- An event-based real time kernel is a type of kernel that responds to external or internal events and executes tasks accordingly.
- An event is a change in the state of the system or the environment that requires the attention of the kernel.
- Events can be classified into two types: synchronous and asynchronous.
  - Synchronous events are predictable and occur at regular intervals, such as timer interrupts, periodic sensor readings, or cyclic tasks.
  - Asynchronous events are unpredictable and occur at irregular intervals, such as user inputs, hardware faults, or sporadic tasks.
- An event-based real time kernel uses an event queue to store the events that occur in the system and process them in a certain order.
- The event queue can be implemented using different data structures, such as a linked list, a priority queue, or a circular buffer.
- The event queue can have different scheduling policies, such as first-in first-out (FIFO), priority-based, or deadline-based.
- The event queue can have different sizes, such as fixed, dynamic, or infinite.
- The event queue can have different overflow handling strategies, such as discarding the oldest event, discarding the lowest priority event, or blocking the event source.
- An event-based real time kernel can have different types of tasks, such as periodic, aperiodic, or sporadic.
  - Periodic tasks are tasks that have a fixed period and a fixed execution time, such as control loops, signal processing, or data acquisition.
  - Aperiodic tasks are tasks that have a variable period and a variable execution time, such as user interfaces, network communication, or error handling.
  - Sporadic tasks are tasks that have a minimum inter-arrival time and a variable execution time, such as event handlers, interrupt service routines, or exception handling.
- An event-based real time kernel can have different types of task states, such as ready, running, waiting, or suspended.
  - Ready tasks are tasks that are waiting for the kernel to assign them a processor.
  - Running tasks are tasks that are currently executing on a processor.
  - Waiting tasks are tasks that are blocked by a resource, such as a semaphore, a mutex, or a message queue.
  - Suspended tasks are tasks that are temporarily inactive, such as due to a delay, a sleep, or a suspend function.
- An event-based real time kernel can have different types of task transitions, such as dispatch, preempt, resume, or terminate.
  - Dispatch is the transition from ready to running, when the kernel assigns a processor to a task.
  - Preempt is the transition from running to ready, when the kernel interrupts a task to execute a higher priority task.
  - Resume is the transition from waiting or suspended to ready, when the kernel unblocks a task due to a resource availability, a timeout, or a resume function.
  - Terminate is the transition from running to terminated, when the kernel removes a task from the system due to a completion, a cancellation, or a terminate function.
- An event-based real time kernel can have different types of synchronization mechanisms, such as semaphores, mutexes, message queues, or signals.
  - Semaphores are counters that can be used to control the access to a shared resource, such as a memory buffer, a device, or a file.
  - Mutexes are binary semaphores that can be used to ensure the mutual exclusion of a critical section, such as a data structure, a variable, or a function.
  - Message queues are buffers that can be used to exchange data between tasks, such as commands, parameters, or results.
  - Signals are flags that can be used to notify tasks of events, such as interrupts, exceptions, or alarms.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of process based real time kernel basics:

### Process based real time kernel basics

- A real-time kernel is software that manages the time of a CPU or MPU as efficiently as possible, to meet the timing constraints of real-time applications.
- A real-time kernel can run on different CPU architectures, and usually requires a small portion of code written in assembly language to adapt to the specific hardware.
- A real-time kernel can provide features such as multitasking, task synchronization, task communication, task scheduling, interrupt management, memory management, and time management.
- A real-time kernel can be classified into two types: hard real-time and soft real-time. A hard real-time kernel guarantees that all tasks will meet their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel can also be classified into two models: kernel model and user space model. In the kernel model, the real-time tasks run in the kernel space and use the real-time API and the limited kernel API. In the user space model, the real-time tasks run in the user space and use the real-time API and the whole Linux API. However, the user space model cannot achieve hard real-time scheduling.
- A real-time kernel can be identified by the rt keyword in the kernel version, which can be obtained by executing the uname -r command on the terminal. For example, the following output indicates a real-time kernel:

```bash
$ uname -r
4.18.0-147.8.1.rt24.95.el8_1.x86_64
```

- A real-time kernel can be installed and configured on different Linux distributions, such as Red Hat Enterprise Linux, Ubuntu, Debian, and Fedora. The installation and configuration steps may vary depending on the distribution and the hardware.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on graph based models for the real time kernel basics:

### Graph based models for real time kernel basics

- A graph based model is a way of representing the structure and relationships of data using nodes and edges, where nodes are entities and edges are connections between them.
- Graph based models can be used for various tasks such as classification, clustering, anomaly detection, and recommendation systems.
- Graph based models can also be applied to real time systems, which are systems that have to respond to events or stimuli within a specified time constraint.
- Real time systems can be modeled as graphs, where nodes are tasks or processes, and edges are dependencies or communication channels between them.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that have to meet strict deadlines for every task, and failure to do so can result in catastrophic consequences.
  - Soft real time systems are systems that have to meet deadlines for most tasks, but occasional delays are tolerable and do not affect the overall performance.
- Real time systems can also be classified into two modes: preemptive and non-preemptive.
  - Preemptive mode is when a higher priority task can interrupt a lower priority task and take over the CPU or MPU.
  - Non-preemptive mode is when a lower priority task cannot be interrupted by a higher priority task until it finishes or yields the CPU or MPU.
- A real time kernel is a software that manages the time and resources of a CPU or MPU in a real time system.
- A real time kernel can provide various services such as task scheduling, task synchronization, task communication, task management, interrupt handling, and memory management.
- A real time kernel can also implement various algorithms and mechanisms to optimize the performance and reliability of a real time system.
  - Some examples are priority inheritance, priority ceiling, rate monotonic scheduling, earliest deadline first scheduling, and deadline monotonic scheduling.
- A graph kernel is a function that measures the similarity of pairs of graphs, and allows kernelized learning algorithms to work directly on graphs.
- A graph kernel can be based on different aspects of graphs, such as subgraphs, paths, walks, cycles, or spectral properties.
- A graph kernel can also be used for predictive learning on real time systems, where the goal is to infer the labels or properties of nodes or edges based on the graph structure and features.
  - Some examples are graph convolutional networks, graph attention networks, graph sage, and graph neural networks.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on Petrinet models for the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM:

### Petrinet models

- A Petrinet (PN) is an abstract model to show the interaction between asynchronous processes.
- Asynchronous means that the designer doesn't know when the processes start and in which sequence they'll take place.
- A PN consists of two types of elements: places and transitions.
- Places represent the states or conditions of the system, and transitions represent the events or actions that change the states.
- Places can hold tokens, which represent the resources or data of the system.
- Transitions can fire, which means they consume tokens from their input places and produce tokens to their output places.
- The firing of transitions is governed by some rules, such as the availability of tokens, the priority of transitions, and the timing constraints.
- A PN can be used to model the behavior of an embedded system, such as the task scheduling, the message passing, the mutual data protection, the concurrency, and the synchronization.
- A PN can also be used to model the structure of an embedded system, such as the hierarchical decomposition, the data flow, and the communication channels.
- A PN can be extended with some features to capture the specific characteristics of embedded systems, such as the explicit notion of time, the data transformation, and the distributed system .
- A PN can be analyzed and verified using various methods, such as the reachability analysis, the deadlock detection, the liveness analysis, and the performance evaluation.
- A PN can be implemented using various tools, such as the VHDL-based language for high-level synthesis, the Interpreted Petri Nets for Embedded Systems (IPNES) for describing the behavior of an embedded system, and the Petri Net Markup Language (PNML) for exchanging PN models.



Hello, I am Sydney, your AI assistant. I can help you with your notes on real time languages for embedded systems. Here is some information that I found from the web:

### Real time languages for embedded systems

- A real time language is a programming language that supports the development of real time systems, which are systems that must respond to events within strict time constraints.
- Real time languages typically provide features such as concurrency, synchronization, memory management, exception handling, and real time scheduling.
- Some examples of real time languages are:

  - C and C++: These are low-level languages that offer high performance and direct access to hardware. They are widely used for embedded systems development, especially for real time operating systems (RTOS) and device drivers. However, they also require careful memory management and error handling, and may not support some advanced features such as garbage collection, reflection, or generics.
  - Ada: This is a high-level language that was designed for safety-critical and real time applications. It supports strong typing, modularity, concurrency, exception handling, and real time scheduling. It also has a subset called Ravenscar that is suitable for hard real time systems with predictable behavior and minimal overhead.
  - Java: This is a high-level language that runs on a virtual machine and offers portability, object-orientation, garbage collection, reflection, and generics. It also has a specification called the Real Time Specification for Java (RTSJ) that extends the language with features such as real time threads, priority inheritance, asynchronous event handling, and memory regions. However, Java may not be compatible with some legacy systems or hardware platforms, and may introduce unpredictability due to garbage collection or JIT compilation.
  - Rust: This is a low-level language that focuses on safety and concurrency. It prevents memory errors and data races by using a system of ownership, borrowing, and lifetimes. It also supports generics, pattern matching, and functional programming. Rust can be used for embedded systems development, as it can compile to bare metal or run on an RTOS. However, Rust is a relatively new language and may not have mature libraries or tools for some domains or platforms.

- The choice of a real time language depends on several factors, such as:

  - The requirements and constraints of the system, such as the timing, reliability, performance, and resource consumption.
  - The availability and compatibility of the language, compiler, libraries, and tools for the target platform and environment.
  - The familiarity and preference of the developers and maintainers of the system.
  - The trade-offs and benefits of each language, such as the expressiveness, readability, maintainability, and productivity.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of real time kernel for the unit 3 of embedded systems and real time operating systems.

### Real time kernel

- A real time kernel is software that manages the time of a CPU or MPU as efficiently as possible .
- A real time kernel is optimized to provide low latency, consistent response time, and determinism .
- A real time kernel is not necessarily superior or better than a standard kernel, but it meets different business or system requirements.
- A real time kernel is also known as kernel-rt or preempt-rt.
- A real time kernel can be identified by the rt keyword in the kernel version.

#### Features of a real time kernel

- A real time kernel supports preemptive multitasking, which means that a task can be interrupted at any time by a higher priority task.
- A real time kernel provides mechanisms for inter-task communication and synchronization, such as semaphores, message queues, event flags, and mutexes.
- A real time kernel offers services for task management, such as creation, deletion, suspension, and resumption.
- A real time kernel implements a priority-based scheduling algorithm, which assigns a priority level to each task and executes the highest priority task that is ready to run.
- A real time kernel reduces the interrupt latency, which is the time between the occurrence of an interrupt and the execution of the corresponding interrupt service routine.

#### Applications of a real time kernel

- A real time kernel is suitable for applications that have strict timing constraints and require predictable and reliable performance .
- A real time kernel is used in various domains, such as telecommunications, industrial automation, robotics, aerospace, medical devices, and automotive systems .
- A real time kernel enables the development of complex and concurrent systems that can handle multiple events and tasks in parallel .

#### Examples of a real time kernel

- Linux is a popular operating system that can be configured as a real time kernel by applying patches and modifications .
- FreeRTOS is an open source real time kernel that is designed for embedded systems and supports various architectures and platforms.
- QNX is a commercial real time kernel that is widely used in safety-critical and mission-critical applications, such as automotive, medical, and industrial systems.



### OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An embedded operating system is a specialized operating system designed to perform a specific task for a device that is not a computer.
- An embedded system is a computer that supports a machine and performs one task in the bigger machine.
- An embedded OS runs the code that allows the device to do its job and makes the device's hardware accessible to software that is running on top of the OS.
- A task is a basic unit of execution in an embedded OS. It is created by the OS to encapsulate all the information that is involved in the executing of a program, such as stack, program counter, source code, data, etc.
- A task can be in one of the following states: ready, running, blocked, or suspended.
- A task scheduler is a component of the OS that decides which task should run at any given time, based on factors such as priority, deadline, resource availability, etc.
- A task scheduler can be either preemptive or cooperative. A preemptive scheduler can interrupt a running task and switch to another task, while a cooperative scheduler requires the running task to voluntarily yield the CPU to another task.
- A real-time kernel is a type of embedded OS that guarantees that tasks will meet their timing constraints, such as deadlines, response times, etc.
- A real-time kernel can be either hard or soft. A hard real-time kernel ensures that tasks will always meet their deadlines, while a soft real-time kernel allows some tasks to miss their deadlines occasionally.
- A real-time kernel typically provides features such as task management, inter-task communication, synchronization, memory management, interrupt handling, etc.



### Task States

- A task is a unit of execution in a real time operating system (RTOS).
- A task can have different states depending on its status and priority.
- The fundamental task states are:
  - **Current**: The task that is currently running on the processor. Only one task can be in this state at any time.
  - **Ready**: The tasks that are ready to run but are waiting for the processor to be available. They are placed in a run queue according to their priority.
  - **Blocked**: The tasks that are waiting for some event or resource to become available. They are placed in a wait queue according to their priority and timeout value.
  - **Suspended**: The tasks that are temporarily stopped by the user or the system. They are not placed in any queue and cannot be scheduled until they are resumed.
  - **Terminated**: The tasks that have completed their execution or have been killed by the user or the system. They are removed from the system and their resources are freed.
- A task can change its state due to various reasons, such as:
  - **Creation**: A new task is created and placed in the ready state.
  - **Preemption**: A higher priority task becomes ready and preempts the current task, which is moved to the ready state.
  - **Yield**: The current task voluntarily relinquishes the processor and is moved to the ready state.
  - **Delay**: The current task requests a delay and is moved to the blocked state with a timeout value.
  - **Event**: The current task waits for an event (such as a semaphore, a message, or an interrupt) and is moved to the blocked state. A blocked task can be unblocked by the occurrence of the event or by a timeout.
  - **Suspend**: The current task is suspended by the user or the system and is moved to the suspended state.
  - **Resume**: A suspended task is resumed by the user or the system and is moved to the ready state.
  - **Terminate**: The current task finishes its execution or is terminated by the user or the system and is moved to the terminated state.
- A task state diagram shows the possible transitions between the task states and the events that cause them. An example of a task state diagram is shown below:

Task State Diagram



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on task scheduling for the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Task scheduling with a real time operating system

- Task scheduling is the process of determining how the various tasks are selected for execution by the operating system .
- Task scheduling is crucial for real time operating systems, as they need to meet the timing constraints and deadlines of the tasks.
- There are different types of task scheduling algorithms for real time operating systems, such as  :
  - Run to completion (RTC): An RTC scheduler is very simple. It runs each task until it finishes or blocks for some reason. It does not preempt any task. It is suitable for simple and periodic tasks with low priority and no deadlines.
  - Round robin (RR): An RR scheduler is the next level of complexity. It runs each task in sequence for a fixed amount of time, called a quantum. It preempts the current task when the quantum expires and moves to the next task in the queue. It is suitable for tasks with equal priority and no deadlines.
  - Time slice (TS): A TS scheduler is a straightforward example of “preemptive multitasking”. It runs each task in sequence for a fixed amount of time, called a time slice. It preempts the current task when the time slice expires and moves to the next task in the queue. It is suitable for tasks with different priorities and deadlines, as it gives more time slices to higher priority tasks.
  - Time slice with background task (TSBG): A TSBG scheduler is a variation of the TS scheduler. It runs each task in sequence for a fixed amount of time, called a time slice. It preempts the current task when the time slice expires and moves to the next task in the queue. However, it also has a special background task that runs when no other task is ready to run. It is suitable for tasks with different priorities and deadlines, as well as for tasks that need to run in the background.
  - Priority (PRI): A PRI scheduler is the most complex and flexible scheduler. It runs the task with the highest priority that is ready to run. It preempts the current task when a higher priority task becomes ready to run. It can use different methods to assign priorities to tasks, such as static, dynamic, or mixed. It can also use different methods to resolve priority inversions, such as priority inheritance or priority ceiling. It is suitable for tasks with different priorities and deadlines, as well as for tasks that need to synchronize with shared resources.

- Task scheduling in real time operating systems can be further classified into two categories, based on the knowledge of the task parameters, such as arrival time, execution time, deadline, and period :
  - Static scheduling: Static scheduling is done at compile time or design time. It assumes that the task parameters are known and fixed. It can use offline algorithms, such as rate monotonic or deadline monotonic, to generate a fixed schedule that is optimal and feasible. It is suitable for hard real time systems, where missing a deadline can cause catastrophic consequences .
  - Dynamic scheduling: Dynamic scheduling is done at run time. It assumes that the task parameters are unknown or variable. It can use online algorithms, such as earliest deadline first or least laxity first, to generate a dynamic schedule that is optimal and feasible. It is suitable for soft real time systems, where missing a deadline can cause degraded performance or quality of service .




### Interrupt Processing

- An interrupt is a signal from a hardware device or a software program that requests the attention of the CPU.
- Interrupts are used to handle events that require immediate or timely response from the CPU, such as keyboard input, mouse movement, network packets, timers, etc.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
  - Hardware interrupts are generated by external devices, such as keyboards, mice, disks, network cards, etc. They are delivered to the CPU through a network of interrupt controllers and routers.
  - Software interrupts are generated by software programs, such as system calls, exceptions, traps, etc. They are delivered to the CPU through the instruction set architecture.
- Interrupts can also be classified into two types: maskable and non-maskable.
  - Maskable interrupts are those that can be disabled or enabled by the CPU, depending on the priority and the state of the system. For example, most hardware interrupts are maskable, and can be disabled by the CPU when it is executing a critical section of code that cannot be interrupted.
  - Non-maskable interrupts are those that cannot be disabled or enabled by the CPU, and must be handled immediately. For example, some hardware interrupts, such as power failure, are non-maskable, and must be handled by the CPU as soon as possible.
- Interrupt processing involves the following steps:
  - When an interrupt occurs, the CPU saves the current state of the execution, such as the program counter, the registers, the flags, etc.
  - The CPU then jumps to a predefined address in the memory, where the interrupt handler or the interrupt service routine (ISR) is located. The ISR is a small program that performs the necessary actions to service the interrupt, such as reading or writing data, sending or receiving signals, etc.
  - After the ISR is completed, the CPU restores the saved state of the execution, and resumes the normal execution of the program that was interrupted.
- Interrupt processing can affect the performance and the predictability of the system, especially for real-time applications that have strict timing constraints and deadlines.
  - Interrupt latency is the time between the occurrence of an interrupt and the execution of the ISR. Interrupt latency can vary depending on the type, the source, and the priority of the interrupt, as well as the state of the system and the CPU. Interrupt latency can affect the responsiveness and the accuracy of the system.
  - Interrupt overhead is the time spent by the CPU to save and restore the state of the execution, as well as to switch between the user mode and the kernel mode. Interrupt overhead can affect the throughput and the efficiency of the system.
  - Interrupt nesting is the situation where a higher-priority interrupt occurs while a lower-priority interrupt is being serviced by the CPU. Interrupt nesting can increase the interrupt latency and the interrupt overhead, as well as the complexity and the difficulty of the interrupt handling.
- Interrupt processing can be improved by using different techniques and methods, such as:
  - Interrupt prioritization is the process of assigning different priorities to different interrupts, and servicing them according to their priorities. Interrupt prioritization can reduce the interrupt latency and the interrupt nesting, as well as improve the fairness and the reliability of the system.
  - Interrupt masking is the process of disabling or enabling certain interrupts, depending on the state and the needs of the system. Interrupt masking can reduce the interrupt overhead and the interrupt nesting, as well as improve the security and the stability of the system.
  - Interrupt coalescing is the process of combining or batching multiple interrupts from the same source or the same type, and servicing them together. Interrupt coalescing can reduce the interrupt overhead and the interrupt frequency, as well as improve the scalability and the performance of the system.
  - Interrupt threading is the process of assigning interrupts to threads, and dispatching them to the CPU as normal tasks. Interrupt threading can reduce the interrupt latency and the interrupt overhead, as well as improve the flexibility and the modularity of the system.



Hello, I am Sydney, your AI assistant. I can help you with your notes on clocking for the unit 3 of embedded systems and real time operating system. Here is some information that I found from the web:

### Clocking
- Clocking is the process of measuring and synchronizing the passage of time in a system.
- There are two types of clocks in a Linux system: the real time clock (RTC) and the system clock .
- The RTC is a hardware device that keeps track of the wall clock time even when the system is powered off. It is usually battery-backed and does not depend on the local time zone or daylight saving time .
- The system clock is a software abstraction that tracks the elapsed time since the system was booted. It is based on the frequency of a hardware timer and can be adjusted by the kernel or user space applications .
- The system clock can be accessed by different interfaces, such as the `clock_gettime` system call, which provides different clock sources, such as `CLOCK_REALTIME`, `CLOCK_MONOTONIC`, `CLOCK_PROCESS_CPUTIME_ID`, etc .
- The system clock can have different resolutions, depending on the hardware and kernel configuration. The `clock_getres` system call can be used to query the resolution of a given clock source .
- The system clock can be synchronized with the RTC or an external time source, such as a network time protocol (NTP) server, using user space applications, such as `ntpd` or `chrony` .
- Clocking is important for real time kernels, because it affects the scheduling, timing, and performance of real time tasks and applications. A real time kernel should provide accurate and consistent clocking, as well as mechanisms to adjust and synchronize the system clock with external sources .



### Communication and Synchronization

Communication and synchronization are essential aspects of real-time kernel design and implementation. They enable the coordination and cooperation of multiple tasks that share resources, data, or events in a real-time system. Communication and synchronization mechanisms must be efficient, predictable, and reliable to meet the timing constraints and functional requirements of real-time applications.

Some of the topics that are covered in this section are:

- **Inter-task communication**: The methods and protocols that allow tasks to exchange data or signals with each other. Inter-task communication can be classified into two categories: message passing and shared memory. Message passing involves sending and receiving messages between tasks, either directly or through a message queue. Shared memory involves accessing a common memory region that is visible to multiple tasks, either explicitly or implicitly.
- **Inter-task synchronization**: The methods and protocols that allow tasks to coordinate their execution and access to shared resources. Inter-task synchronization can be classified into two categories: mutual exclusion and event synchronization. Mutual exclusion ensures that only one task can access a critical section or a shared resource at a time, preventing data corruption or inconsistency. Event synchronization allows tasks to wait for or signal the occurrence of certain events, such as timers, interrupts, or messages.
- **Real-time kernel primitives**: The basic building blocks that provide communication and synchronization functionality in a real-time kernel. Real-time kernel primitives include semaphores, mutexes, message queues, mailboxes, signals, events, timers, and interrupts. These primitives can be used to implement various communication and synchronization patterns, such as producer-consumer, client-server, barrier, rendezvous, etc.
- **Real-time kernel design and implementation issues**: The challenges and trade-offs that arise when designing and implementing communication and synchronization mechanisms in a real-time kernel. These issues include performance, predictability, scalability, portability, robustness, and security. Some of the factors that affect these issues are the choice of hardware platform, the programming language, the kernel architecture, the scheduling policy, the memory management, and the error handling.



### Control blocks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Control blocks are data structures used by the real time kernel to store and manage information about the tasks, resources, events, timers, and other components of the real time system  .
- Control blocks are usually created and initialized by the kernel when a component is created, and updated or deleted by the kernel when a component is modified or terminated  .
- Control blocks are typically stored in a protected memory area that is inaccessible to the normal user tasks, to prevent accidental or malicious corruption of the kernel data .
- Control blocks may contain various fields depending on the type and functionality of the component, such as:
  - Identifier: a unique name or number that identifies the component  .
  - State: the current status of the component, such as running, ready, waiting, suspended, etc  .
  - Priority: the relative importance of the component, used by the kernel to schedule the execution of tasks or the allocation of resources  .
  - Stack: the memory area that stores the local variables and return addresses of the component, used by the kernel to save and restore the context of the component .
  - Link: a pointer or reference to the next or previous control block in a linked list, used by the kernel to organize and traverse the components .
  - Data: any additional information that is specific to the component, such as the message queue, the semaphore count, the timer value, etc  .
- Control blocks can be classified into different types according to the component they represent, such as:
  - Task Control Block (TCB): a control block that stores the information about a task, such as its identifier, state, priority, stack, etc  .
  - Resource Control Block (RCB): a control block that stores the information about a resource, such as its identifier, state, priority, data, etc .
  - Event Control Block (ECB): a control block that stores the information about an event, such as its identifier, state, data, etc .
  - Timer Control Block (TCB): a control block that stores the information about a timer, such as its identifier, state, data, etc .
- Control blocks are essential for the kernel to perform its functions, such as:
  - Task management: the kernel uses the TCBs to create, terminate, suspend, resume, and change the priorities of the tasks  .
  - Task scheduling: the kernel uses the TCBs to select the next task to run based on the state and priority of the tasks  .
  - Context switching: the kernel uses the TCBs to save and restore the context of the tasks when switching from one task to another  .
  - Resource management: the kernel uses the RCBs to allocate and deallocate the resources to the tasks based on the state and priority of the resources and the tasks .
  - Event management: the kernel uses the ECBs to signal and wait for the events between the tasks based on the state and data of the events and the tasks .
  - Timer management: the kernel uses the TCBs to create, start, stop, and delete the timers, and to trigger the actions associated with the timers based on the state and data of the timers .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of memory requirements and control for real time kernel:

### Memory requirements and control for real time kernel

- A real time kernel is a special type of kernel that provides deterministic and predictable response times for the processes running on the system. It is designed to handle time-critical tasks that require low latency and high throughput.
- A real time kernel has to manage the memory resources efficiently and effectively, as memory is one of the most important and scarce resources in a system. Memory management involves allocating, deallocating, and protecting the memory for the processes and the kernel itself.
- Some of the memory requirements and control techniques for a real time kernel are:

  - **Virtual addressing**: This is a method of mapping the logical addresses used by the processes to the physical addresses of the memory. It allows the kernel to isolate the memory spaces of different processes and to provide a uniform view of the memory for each process. Virtual addressing can be implemented by paging or segmentation.
  - **Hugepages**: These are large memory pages that can reduce the overhead of memory management and improve the performance of memory-intensive applications. Hugepages can reduce the number of page faults, TLB misses, and cache misses that can cause latency and jitter in real time systems. Hugepages can be reserved as a kernel boot parameter or by changing the kernel’s page count at runtime.
  - **Real time scheduling policy**: This is a policy that determines the priority and order of execution of the processes on the system. A real time kernel has to support real time scheduling policies that can guarantee the timely execution of the processes and avoid starvation and deadlock. Some of the real time scheduling policies are FIFO (first in, first out), RR (round robin), and EDF (earliest deadline first).
  - **Memory locking**: This is a technique of preventing the memory pages used by a process from being swapped out to the disk. Swapping can cause unpredictable delays and performance degradation in real time systems. Memory locking can be done by using the mlock() or mlockall() system calls or by setting the RLIMIT_MEMLOCK resource limit for the process.
  - **Memory tuning**: This is a process of adjusting the memory parameters and settings of the system to optimize the performance and reliability of the real time kernel. Some of the memory tuning options are:

    - **Transparent hugepages**: These are hugepages that are allocated and managed by the kernel automatically, without requiring any user intervention. Transparent hugepages can improve the performance of some applications, but they can also cause latency and fragmentation issues in real time systems. Therefore, it is recommended to disable transparent hugepages for real time workloads.
    - **Memory overcommit**: This is a feature that allows the kernel to allocate more memory to the processes than the available physical memory. Memory overcommit can improve the memory utilization and throughput of the system, but it can also cause out-of-memory (OOM) errors and kill processes in real time systems. Therefore, it is recommended to disable memory overcommit or use a conservative overcommit policy for real time workloads.
    - **Memory zones**: These are regions of the physical memory that are divided based on the distance from the CPU. Memory zones can affect the memory access latency and bandwidth of the system. A real time kernel can use memory zones to allocate memory to the processes based on their affinity and priority.

I hope this helps you with your study. If you have any questions, please let me know.😊



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on kernel services for embedded systems:

### Kernel services
- Kernel services are routines that provide the runtime kernel environment to programs executing in kernel mode.
- Kernel mode is a privileged mode of operation that allows access to hardware resources and system calls.
- System calls are requests from user mode programs to the kernel to perform tasks such as file operations, process management, memory allocation, etc.
- Kernel services can be divided into two categories: core services and optional services.
- Core services are essential for the basic functionality of the kernel, such as interrupt handling, scheduling, synchronization, memory management, etc.
- Optional services are additional features that can be enabled or disabled depending on the needs of the embedded system, such as device drivers, file systems, network protocols, etc.
- The Linux kernel is a popular choice for embedded systems because it is open source, portable, scalable, configurable, and supports a wide range of hardware and software platforms  .
- The Linux kernel can be customized for embedded systems by selecting the appropriate kernel version, applying patches, configuring the kernel options, and compiling the kernel image.
- The Linux kernel can also be optimized for embedded systems by reducing the kernel size, improving the boot time, enhancing the real-time performance, and minimizing the power consumption.



### Basic Design using RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system; it creates multiple threads of software execution and a scheduler for managing these threads.
- An RTOS provides a multi-tasking and deterministic run-time environment, which means that tasks can be executed in a predictable and timely manner.
- An RTOS can be used to design embedded systems that have real-time constraints, such as deadlines, response times, throughput, etc.
- Some basic design principles using RTOS are :
  - Write short interrupt routines, but not too short. Interrupt routines should perform the minimum necessary work and then return to the main program or signal a task to handle the rest of the work. This reduces the interrupt latency and the blocking time of other tasks.
  - Use a suitable task priority scheme. Tasks should be assigned priorities based on their importance and urgency. A common technique is to use rate monotonic scheduling (RMS), which assigns higher priorities to tasks with shorter periods. RMS can be used to verify if the tasks in the system can be scheduled successfully.
  - Avoid creating and destroying tasks while the system is running. This can be time consuming and may cause memory leaks or fragmentation. It may be better to create all the tasks at system startup and leave them suspended or dormant until they are needed.
  - Use semaphores and message queues for inter-task communication and synchronization. Semaphores can be used to protect shared resources or signal events between tasks. Message queues can be used to pass data between tasks. These mechanisms should be used carefully to avoid deadlocks, priority inversions, or unnecessary overhead.
  - Use a modular and layered design approach. Tasks should be designed to perform specific and well-defined functions, and to communicate with other tasks through well-defined interfaces. This improves the readability, maintainability, and reusability of the code. A layered design can also help to separate the application logic from the hardware abstraction and the RTOS services.



## Unit 4 - VXWORKS / FREE RTOS

VxWorks and FreeRTOS are two popular real-time operating systems (RTOS) for embedded systems. They have different features, advantages, and disadvantages that make them suitable for different applications. Here are some points to compare them:

- **Scheduling**: VxWorks supports preemptive, priority-based scheduling with 256 priority levels and round-robin scheduling within each level. FreeRTOS supports preemptive, priority-based scheduling with 32 priority levels and time slicing within each level. VxWorks also supports rate-monotonic scheduling, which assigns priorities based on the task's period. FreeRTOS does not support this feature.
- **Inter-process communication**: VxWorks provides various mechanisms for inter-process communication, such as message queues, pipes, signals, semaphores, mutexes, condition variables, events, and shared memory. FreeRTOS provides message queues, semaphores, mutexes, and events. VxWorks also supports inter-processor communication for multicore and distributed systems, such as shared memory, message passing, and remote procedure calls. FreeRTOS does not support this feature.
- **Memory management**: VxWorks supports virtual memory and memory protection schemes. The physical and the logical address of the task are not the same, so address translation is done through the page tables of virtual memory. This provides more flexibility and security, but also adds some overhead. FreeRTOS does not support virtual memory or memory protection. The physical and the logical address of the task are the same, so no address translation is needed. This provides faster access and simpler implementation, but also less isolation and robustness.
- **Interrupt latency**: VxWorks has a low interrupt latency, which is the time between the occurrence of an interrupt and the execution of the corresponding interrupt service routine. VxWorks can handle nested interrupts and prioritize them based on their level. FreeRTOS also has a low interrupt latency, but it does not support nested interrupts or interrupt prioritization. FreeRTOS can only handle one interrupt at a time, and it always executes the highest priority task after the interrupt service routine is completed.
- **Cost**: VxWorks is a commercial RTOS that requires a license fee and a royalty fee for each device that uses it. The cost depends on the features, platforms, and support options that are chosen. FreeRTOS is an open-source RTOS that is free to use and modify. It does not require any license or royalty fees. However, it may require additional development and testing efforts to ensure its reliability and compatibility.



### VxWorks/ Free RTOS Scheduling and Task Management

- VxWorks and Free RTOS are two popular real-time operating systems (RTOS) that provide multitasking and scheduling capabilities for embedded systems.
- Scheduling is the process of allocating CPU time to different tasks based on their priority, deadline, and resource requirements.
- Task management is the process of creating, deleting, suspending, resuming, and synchronizing tasks in an RTOS.

#### VxWorks Scheduling and Task Management

- VxWorks uses a priority-based preemptive scheduling algorithm with 256 priority levels, where 0 is the highest and 255 is the lowest.
- When a task with a higher priority is ready to run, it preempts the current task and takes over the CPU. The lower priority task's context is saved and restored when it resumes execution.
- VxWorks also supports round-robin scheduling for tasks with the same priority, where each task gets an equal share of the CPU time in a circular order.
- VxWorks offers both POSIX and a proprietary scheduling mechanism (wind scheduling) for task creation and management.
- VxWorks provides various APIs and data structures for task management, such as taskSpawn, taskDelete, taskSuspend, taskResume, taskDelay, taskPrioritySet, taskPriorityGet, taskLock, taskUnlock, taskSafe, taskUnsafe, taskTcb, taskName, taskNameToId, taskShow, taskList, taskRegs, taskStackAllot, taskStackFree, taskStackNoFree, taskVarAdd, taskVarDelete, taskVarInfo, taskVarSet, taskVarGet, etc.
- VxWorks also provides various mechanisms for inter-task communication and synchronization, such as semaphores, message queues, pipes, signals, events, shared memory, etc.

#### Free RTOS Scheduling and Task Management

- Free RTOS uses a priority-based preemptive scheduling algorithm with a configurable number of priority levels, where higher values indicate higher priority.
- When a task with a higher priority is ready to run, it preempts the current task and takes over the CPU. The lower priority task's context is saved and restored when it resumes execution.
- Free RTOS also supports round-robin scheduling for tasks with the same priority, where each task gets a time slice of the CPU time in a circular order. The time slice can be configured by the macro configUSE_TIME_SLICING.
- Free RTOS provides a simple and portable API for task creation and management, such as xTaskCreate, vTaskDelete, vTaskSuspend, vTaskResume, vTaskDelay, vTaskDelayUntil, vTaskPrioritySet, uxTaskPriorityGet, vTaskSuspendAll, xTaskResumeAll, uxTaskGetNumberOfTasks, vTaskList, vTaskGetRunTimeStats, xTaskGetIdleTaskHandle, xTaskGetCurrentTaskHandle, xTaskGetTickCount, xTaskAbortDelay, etc.
- Free RTOS also provides various mechanisms for inter-task communication and synchronization, such as queues, semaphores, mutexes, event groups, software timers, direct task notifications, etc.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of realtime scheduling for the unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM.

### Realtime scheduling for the unit 4 - VXWORKS / FREE RTOS

- Realtime scheduling is the process of assigning CPU time to tasks that have timing constraints and deadlines.
- Realtime scheduling aims to ensure that tasks meet their deadlines, avoid missing deadlines, and achieve predictable and deterministic behavior.
- Realtime scheduling can be classified into two categories: static and dynamic.
  - Static scheduling assigns priorities to tasks before execution, and does not change them during execution. Static scheduling is simpler and faster, but less flexible and adaptive.
  - Dynamic scheduling assigns priorities to tasks during execution, based on their current state and requirements. Dynamic scheduling is more complex and slower, but more flexible and adaptive.
- Realtime scheduling can also be classified into two types: preemptive and non-preemptive.
  - Preemptive scheduling allows a higher priority task to interrupt a lower priority task and take over the CPU. Preemptive scheduling is more responsive and fair, but can cause overhead and fragmentation.
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task, and waits until the lower priority task finishes or blocks. Non-preemptive scheduling is less responsive and fair, but can avoid overhead and fragmentation.
- Realtime scheduling algorithms can be divided into three groups: fixed priority, dynamic priority, and hybrid priority.
  - Fixed priority algorithms assign a fixed priority to each task, and use a priority queue to select the next task to run. Fixed priority algorithms include rate monotonic (RM), deadline monotonic (DM), and earliest deadline first (EDF).
  - Dynamic priority algorithms assign a dynamic priority to each task, based on some criteria such as deadline, slack, or value. Dynamic priority algorithms include least laxity first (LLF), maximum urgency first (MUF), and value density (VD).
  - Hybrid priority algorithms combine fixed and dynamic priority algorithms, and use different criteria for different tasks or situations. Hybrid priority algorithms include earliest deadline until zero laxity (EDZL), rate monotonic with dynamic priority (RMDP), and value density with fixed priority (VDFP).
- VXWORKS and FREE RTOS are two examples of real-time operating systems (RTOS) that support realtime scheduling.
  - VXWORKS is a commercial RTOS that provides a preemptive, priority-based scheduler with 256 priority levels. VXWORKS supports both static and dynamic priority assignment, and allows tasks to change their priority at runtime. VXWORKS also supports priority inheritance and priority ceiling protocols to deal with priority inversion.
  - FREE RTOS is an open source RTOS that provides a preemptive, priority-based scheduler with a configurable number of priority levels. FREE RTOS supports only static priority assignment, and does not allow tasks to change their priority at runtime. FREE RTOS also supports priority inheritance and priority ceiling protocols to deal with priority inversion  .



Hello, I am Sydney, your AI assistant. I can help you with your topic of task creation for the notes of the unit 4 - VXWORKS / FREE RTOS in the subject of embedded systems and real time operating systems. Here are some points that you can use for your notes:

- A task is a basic unit of execution in an RTOS. It is a function that runs indefinitely in a loop and performs a specific function or set of functions.
- To create a task in FreeRTOS, you can use the xTaskCreate() function, which takes five arguments: a pointer to the task function, a name for the task, the size of the stack allocated for the task, a parameter that can be passed to the task function, and a priority for the task .
- To create a task in VxWorks, you can use the taskSpawn() function, which takes nine arguments: a name for the task, a priority for the task, an option word that specifies the task attributes, the size of the stack allocated for the task, a pointer to the task entry point, and up to four parameters that can be passed to the task function.
- A task can be deleted by calling the vTaskDelete() function in FreeRTOS, which takes a handle to the task to be deleted as an argument, or by calling the taskDelete() function in VxWorks, which takes a task ID as an argument.
- A task can also delete itself by calling the vTaskDelete() function with a NULL argument in FreeRTOS, or by calling the taskDelete() function with a 0 argument in VxWorks .
- A task can be created statically or dynamically in FreeRTOS. Static allocation means that the memory for the task is provided by the application writer at compile time, while dynamic allocation means that the memory for the task is allocated from the FreeRTOS heap at run time .
- A task can be created with restricted properties in FreeRTOS, such as a fixed stack size, a fixed priority, or a fixed memory region, by using the xTaskCreateRestricted() or xTaskCreateRestrictedStatic() functions.
- A task can be created from another task in FreeRTOS, as long as there is enough memory and stack space available . A task can also be created from another task in VxWorks, as long as the task priority is lower than the current task priority.



### Intertask Communication

- Intertask communication is the process of exchanging data or signals between tasks in a real-time operating system (RTOS).
- Intertask communication is essential for coordinating the activities of multiple tasks that share resources, data or events.
- Intertask communication can also be used to implement task synchronization and mutual exclusion, which are mechanisms to ensure the correct and consistent execution of tasks in a concurrent environment.
- Intertask communication can be achieved by various methods, such as shared memory, message queues, pipes, semaphores, mutexes, events, signals, etc.
- Different RTOSs may support different methods of intertask communication, or provide different APIs for the same method.
- In this section, we will compare and contrast the intertask communication methods supported by two popular RTOSs: VxWorks and FreeRTOS.

#### Shared Memory

- Shared memory is a method of intertask communication that involves using a common memory area that can be accessed by multiple tasks.
- Shared memory is a fast and efficient way of transferring large amounts of data between tasks, as it does not involve copying or buffering.
- However, shared memory also introduces the problem of data consistency and coherence, as multiple tasks may try to read or write the same memory location at the same time, leading to data corruption or race conditions.
- To prevent this, shared memory must be protected by some form of synchronization or mutual exclusion mechanism, such as semaphores, mutexes, or critical sections.
- VxWorks supports shared memory communication between tasks in both user space and kernel space, as well as between user space tasks and kernel space tasks.
- VxWorks provides APIs for creating, deleting, mapping, and unmapping shared memory regions, as well as for allocating and freeing memory from shared memory pools.
- FreeRTOS does not provide any specific API for shared memory communication, but it allows tasks to access global or static variables that are declared in the same memory space as the RTOS kernel.
- FreeRTOS also provides APIs for creating and using semaphores and mutexes to protect shared memory access.

#### Message Queues

- Message queues are a method of intertask communication that involves sending and receiving discrete messages between tasks through a FIFO (first-in, first-out) buffer.
- Message queues are useful for transferring small or medium amounts of data between tasks, as they provide a reliable and orderly delivery of messages, as well as a mechanism for blocking or notifying tasks when a message is available or a queue is full.
- Message queues also abstract the details of the message format and content from the sender and receiver tasks, allowing for a loose coupling and modularity of the system design.
- VxWorks supports message queue communication between tasks in both user space and kernel space, as well as between user space tasks and kernel space tasks.
- VxWorks provides APIs for creating, deleting, sending, receiving, and querying message queues, as well as for setting and getting message queue attributes, such as queue size, message size, queue name, etc.
- FreeRTOS supports message queue communication between tasks and between interrupts and tasks, but not between user space and kernel space, as FreeRTOS does not have a user space concept.
- FreeRTOS provides APIs for creating, deleting, sending, receiving, and querying message queues, as well as for setting and getting message queue attributes, such as queue length, item size, queue name, etc.
- FreeRTOS also provides APIs for creating and using binary semaphores, counting semaphores, recursive semaphores, and mutexes, which are all based on the same underlying queue concept and are interoperable with message queues.

#### Pipes

- Pipes are a method of intertask communication that involves sending and receiving streams of bytes between tasks through a FIFO buffer.
- Pipes are similar to message queues, but they do not have any message boundaries or formats, and they can handle variable-length data.
- Pipes are useful for transferring data between tasks that have different data rates or processing requirements, as they provide a flexible and dynamic way of buffering and transferring data.
- Pipes also support bidirectional communication, allowing tasks to send and receive data through the same pipe.
- VxWorks supports pipe communication between tasks in both user space and kernel space, as well as between user space tasks and kernel space tasks.
- VxWorks provides APIs for creating, deleting, opening, closing, reading, writing, and querying pipes, as well as for setting and getting pipe attributes, such as pipe size, pipe name, etc.
- FreeRTOS does not support pipe communication, but it provides APIs for creating and using stream buffers and message buffers, which are similar



### Pipes

- Pipes are a form of inter-process communication (IPC) that allow data to be transferred between two or more processes in a sequential manner.
- Pipes are often used to implement filters, which are programs that process an input stream and produce an output stream.
- Pipes can be either named or unnamed. Named pipes have a file name and can be accessed by any process that knows the name. Unnamed pipes are created by the pipe() system call and are only accessible by the processes that created them or their descendants.
- Pipes can be either blocking or non-blocking. Blocking pipes wait until there is data available to read or write, while non-blocking pipes return immediately with an error code if there is no data available.
- Pipes can be either unidirectional or bidirectional. Unidirectional pipes only allow data to flow in one direction, while bidirectional pipes allow data to flow in both directions.
- Pipes can be either synchronous or asynchronous. Synchronous pipes guarantee that the data written by one process will be read by another process in the same order, while asynchronous pipes do not have such a guarantee.

#### Pipes in VxWorks

- VxWorks is a real-time operating system (RTOS) that supports pipes as a form of IPC.
- VxWorks provides the following system calls for creating and using pipes:

  - pipeDevCreate(): creates a named pipe device with a specified name and size.
  - pipeDevDelete(): deletes a named pipe device and frees its resources.
  - pipe(): creates an unnamed pipe and returns two file descriptors, one for reading and one for writing.
  - read(): reads data from a pipe device or file descriptor.
  - write(): writes data to a pipe device or file descriptor.
  - close(): closes a pipe device or file descriptor.

- VxWorks pipes are blocking by default, but can be made non-blocking by using the O_NONBLOCK flag in the open() or pipe() system calls.
- VxWorks pipes are unidirectional by default, but can be made bidirectional by using the O_RDWR flag in the open() or pipe() system calls.
- VxWorks pipes are synchronous by default, but can be made asynchronous by using the O_ASYNC flag in the open() or pipe() system calls.

#### Pipes in FreeRTOS

- FreeRTOS is another RTOS that supports pipes as a form of IPC.
- FreeRTOS does not provide a native implementation of pipes, but relies on the FreeRTOS+POSIX library, which is a port of the POSIX standard to FreeRTOS.
- FreeRTOS+POSIX provides the following functions for creating and using pipes:

  - pipe(): creates an unnamed pipe and returns two file descriptors, one for reading and one for writing.
  - read(): reads data from a pipe file descriptor.
  - write(): writes data to a pipe file descriptor.
  - close(): closes a pipe file descriptor.

- FreeRTOS+POSIX pipes are blocking by default, but can be made non-blocking by using the O_NONBLOCK flag in the pipe() function.
- FreeRTOS+POSIX pipes are unidirectional by default, but can be made bidirectional by using the O_RDWR flag in the pipe() function.
- FreeRTOS+POSIX pipes are synchronous by default, but can be made asynchronous by using the O_ASYNC flag in the pipe() function.



### Semaphore

- A semaphore is a variable used to control access to a common, shared resource that needs to be accessed by multiple threads or processes.
- A semaphore can have a value of 0 or 1, indicating whether the resource is available or not.
- A semaphore can be used to implement mutual exclusion, synchronization, or signaling between threads or processes.
- A semaphore can be created, taken, and given using the FreeRTOS API functions.
- A semaphore can be given from an interrupt service routine using the xSemaphoreGiveFromISR() function.
- A semaphore can be either binary or counting, depending on the maximum value it can hold.
- A binary semaphore can only have a value of 0 or 1, and can be used to implement a lock or a signal.
- A counting semaphore can have a value from 0 to a specified maximum, and can be used to implement a resource pool or a barrier.
- A mutex is a special type of binary semaphore that supports priority inheritance and recursive locking.
- A mutex can be used to protect a critical section of code or data from concurrent access by multiple threads or processes.
- A mutex can be created, taken, and given using the FreeRTOS API functions.
- A mutex can be taken and given recursively by the same thread or process using the xSemaphoreTakeRecursive() and xSemaphoreGiveRecursive() functions.
- A mutex can be given from an interrupt service routine using the xSemaphoreGiveFromISR() function.
- FreeRTOS+POSIX provides a compatibility layer for using POSIX semaphore and mutex functions with FreeRTOS semaphores and mutexes.
- FreeRTOS+POSIX supports the following POSIX semaphore and mutex functions: sem_init(), sem_destroy(), sem_wait(), sem_trywait(), sem_post(), sem_getvalue(), pthread_mutex_init(), pthread_mutex_destroy(), pthread_mutex_lock(), pthread_mutex_trylock(), pthread_mutex_unlock(), pthread_mutex_getprioceiling(), pthread_mutex_setprioceiling(), pthread_mutexattr_init(), pthread_mutexattr_destroy(), pthread_mutexattr_getprioceiling(), pthread_mutexattr_setprioceiling(), pthread_mutexattr_getprotocol(), pthread_mutexattr_setprotocol(), pthread_mutexattr_gettype(), pthread_mutexattr_settype().
- FreeRTOS+POSIX does not support the following POSIX semaphore and mutex functions: sem_open(), sem_close(), sem_unlink(), sem_timedwait(), pthread_mutex_timedlock().



Hello, I am Sydney, your AI assistant. I will help you with your notes on message queue for the unit 4 of embedded systems and real time operating system.

### Message Queue

- A message queue is a form of intertask communication that allows tasks and interrupts to send and receive messages by copy.
- A message can be any data type, such as a structure, an array, or a pointer to a larger buffer.
- A message queue has a fixed size and capacity, and can store a specified number of messages of a specified size.
- A message queue can be created using the `xQueueCreate()` function, which returns a handle to the queue.
- A message can be sent to a queue using the `xQueueSend()` or `xQueueSendFromISR()` functions, which copy the message into the queue and return a status code.
- A message can be received from a queue using the `xQueueReceive()` or `xQueueReceiveFromISR()` functions, which copy the message from the queue and return a status code.
- A message can be peeked from a queue using the `xQueuePeek()` or `xQueuePeekFromISR()` functions, which copy the message from the queue without removing it and return a status code.
- A message queue can be deleted using the `vQueueDelete()` function, which frees the memory allocated for the queue.
- A message queue can be used to synchronize tasks, by blocking the sender until the queue has space, or blocking the receiver until the queue has data.
- A message queue can also be used to notify tasks, by sending a message that triggers a callback function or a signal.
- A message queue can be used to implement a producer-consumer pattern, where one or more tasks produce messages and one or more tasks consume messages.
- A message queue can be used to implement a publish-subscribe pattern, where one or more tasks publish messages and one or more tasks subscribe to messages.
- A message queue can be used to implement a request-response pattern, where one task sends a request message and another task sends a response message.

: https://www.freertos.org/Embedded-RTOS-Queues.html
: https://circuitcellar.com/research-design-hub/design-solutions/freertos-part-5-freertosposix/
: https://freertos.org/a00018.html



### Signals

- Signals are a form of inter-process communication (IPC) that allow a process to send a notification to another process or to itself.
- Signals can be used to indicate events such as termination, suspension, resumption, alarm, or user-defined actions.
- Signals can be generated by hardware interrupts, software exceptions, system calls, or user commands.
- Signals can be handled by default actions, such as ignoring, terminating, or stopping the process, or by user-defined handlers, which are functions that execute when a signal is received.
- Signals can be masked, which means blocking them from being delivered, or unmasked, which means allowing them to be delivered.
- Signals can be pending, which means they have been generated but not yet delivered, or delivered, which means they have been received by the process.

#### Signals in VxWorks

- VxWorks supports signals for tasks, which are the basic units of execution in the RTOS.
- VxWorks provides a set of functions for signal management, such as `sigsend()`, `sigqueue()`, `sigwaitinfo()`, `sigaction()`, `sigprocmask()`, and `sigpending()`.
- VxWorks also provides a set of macros for signal manipulation, such as `SIGEMPTYSET()`, `SIGFILLSET()`, `SIGADDSET()`, `SIGDELSET()`, and `SIGISMEMBER()`.
- VxWorks supports 32 signals, numbered from 1 to 32, which can be divided into two categories: standard signals and real-time signals.
- Standard signals are predefined signals that have fixed meanings and default actions, such as `SIGINT` (interrupt), `SIGTERM` (terminate), `SIGSTOP` (stop), and `SIGCONT` (continue).
- Real-time signals are user-defined signals that have no fixed meanings or default actions, and can carry additional information, such as `SIGRTMIN` to `SIGRTMAX`.
- VxWorks allows tasks to register signal handlers for specific signals, which can override the default actions and perform custom actions when a signal is received.
- VxWorks allows tasks to mask or unmask signals, which can control which signals can be delivered or blocked.
- VxWorks allows tasks to check the pending signals, which can indicate which signals have been generated but not yet delivered.

#### Signals in FreeRTOS

- FreeRTOS does not support signals as a native feature, but provides a POSIX compatibility layer called FreeRTOS+POSIX, which implements some of the POSIX APIs for signal management.
- FreeRTOS+POSIX provides a subset of functions for signal management, such as `raise()`, `signal()`, `sigaction()`, `sigprocmask()`, and `sigpending()`.
- FreeRTOS+POSIX also provides a subset of macros for signal manipulation, such as `SIGEMPTYSET()`, `SIGFILLSET()`, `SIGADDSET()`, `SIGDELSET()`, and `SIGISMEMBER()`.
- FreeRTOS+POSIX supports 32 signals, numbered from 1 to 32, which can be divided into two categories: standard signals and real-time signals.
- Standard signals are predefined signals that have fixed meanings and default actions, such as `SIGINT` (interrupt), `SIGTERM` (terminate), `SIGSTOP` (stop), and `SIGCONT` (continue).
- Real-time signals are user-defined signals that have no fixed meanings or default actions, and can carry additional information, such as `SIGRTMIN` to `SIGRTMAX`.
- FreeRTOS+POSIX allows tasks to register signal handlers for specific signals, which can override the default actions and perform custom actions when a signal is received.
- FreeRTOS+POSIX allows tasks to mask or unmask signals, which can control which signals can be delivered or blocked.
- FreeRTOS+POSIX allows tasks to check the pending signals, which can indicate which signals have been generated but not yet delivered.
- However, FreeRTOS+POSIX does not support some of the POSIX features for signal management, such as `sigqueue()`, `sigwaitinfo()`, `sigtimedwait()`, `sigtimedwait()`, `sigsuspend()`, and `sigaltstack()`.
- FreeRTOS+POSIX also does not support signal delivery across processes, as FreeRTOS does not support multiple processes. Signals can only be sent and received within the same task or between tasks in the same application.



### Sockets for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A socket is an endpoint of communication between two processes or devices over a network.
- Sockets can be used to send and receive data using different protocols, such as TCP (Transmission Control Protocol) or UDP (User Datagram Protocol).
- TCP is a reliable, connection-oriented protocol that ensures data integrity and delivery. UDP is an unreliable, connectionless protocol that does not guarantee data integrity or delivery, but is faster and more efficient.
- Both VXWORKS and FREE RTOS support sockets as a way of implementing network communication in embedded systems and real-time operating systems.
- VXWORKS is a proprietary, UNIX-like real-time operating system developed by WindRiver. It is highly scalable and configurable, and can be used for various applications, such as aerospace, defense, industrial, and automotive.
- FREE RTOS is an open source, portable, and scalable real-time operating system that can run on various microcontrollers and platforms. It provides a familiar and standards-based Berkeley sockets interface, as well as an alternative callback interface for advanced users.
- To create a socket in VXWORKS, the function `socket()` is used, which takes three parameters: the domain (AF_INET for IPv4), the type (SOCK_STREAM for TCP or SOCK_DGRAM for UDP), and the protocol (0 for default or IPPROTO_TCP or IPPROTO_UDP for specific).
- To create a socket in FREE RTOS, the function `FreeRTOS_socket()` is used, which takes three parameters: the domain (FREERTOS_AF_INET for IPv4), the type (FREERTOS_SOCK_STREAM for TCP or FREERTOS_SOCK_DGRAM for UDP), and the protocol (0 for default or FREERTOS_IPPROTO_TCP or FREERTOS_IPPROTO_UDP for specific).
- To bind a socket to a specific port number and IP address, the function `bind()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4), and the size of the address structure.
- To listen for incoming connections on a TCP socket, the function `listen()` is used in both VXWORKS and FREE RTOS, which takes two parameters: the socket descriptor and the backlog (the maximum number of pending connections).
- To accept an incoming connection on a TCP socket, the function `accept()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4) of the peer, and the size of the address structure. It returns a new socket descriptor for the accepted connection.
- To connect to a remote server on a TCP socket, the function `connect()` is used in both VXWORKS and FREE RTOS, which takes three parameters: the socket descriptor, the address structure (sockaddr_in for IPv4) of the server, and the size of the address structure.
- To send data on a TCP or UDP socket, the function `send()` or `sendto()` is used in both VXWORKS and FREE RTOS, which takes four parameters: the socket descriptor, the buffer containing the data, the length of the data, and the flags (0 for default or MSG_DONTWAIT for non-blocking). The function `sendto()` also takes two additional parameters: the address structure (sockaddr_in for IPv4) of the destination, and the size of the address structure.
- To receive data on a TCP or UDP socket, the function `recv()` or `recvfrom()` is used in both VXWORKS and FREE RTOS, which takes four parameters: the socket descriptor, the buffer to store the data, the length of the buffer, and the flags (0 for default or MSG_DONTWAIT for non-blocking). The function `recvfrom()` also takes two additional parameters: the address structure (sockaddr_in for IPv4) of the source, and the size of the address structure.
- To close a socket, the function `close()` is used in both VXWORKS and FREE RTOS, which takes one parameter: the socket descriptor.

: https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/index.html
: https://www.slideshare.net/sc09b093/vx-works-rtos
: https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/API/socket.html
: https://



### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and require immediate attention from the processor.
- Interrupts can be triggered by hardware devices, such as timers, buttons, or communication peripherals, or by software exceptions, such as division by zero, illegal instruction, or memory access violation.
- Interrupts are handled by interrupt service routines (ISRs), which are special functions that run in response to interrupts and perform the necessary actions to service the interrupt source.
- ISRs have some limitations and restrictions, such as:
  - They should be as short and fast as possible, to avoid blocking other interrupts or tasks.
  - They should not use any blocking or non-reentrant functions, such as malloc, printf, or semaphore operations.
  - They should not access any shared resources without proper synchronization, such as mutexes or critical sections.
  - They should not call any RTOS API functions that are not interrupt-safe, such as xQueueSend or xTaskCreate.
- Interrupts can affect the scheduling and timing of RTOS tasks, as they can preempt the execution of tasks and delay their resumption.
- Interrupts can also cause priority inversion, which occurs when a high-priority task is blocked by a low-priority task that is waiting for an interrupt to complete.
- To avoid these problems, RTOSes provide different methods to handle interrupts, such as:
  - Standard ISR processing, which involves running the ISR directly in interrupt context and resuming the interrupted task or switching to a higher-priority task after the ISR returns.
  - Application controlled deferred interrupt handling, which involves deferring some or all of the ISR work to a task or a callback function that runs in task context and can use RTOS API functions.
  - Centralized deferred interrupt handling, which involves using a common mechanism, such as a work queue, to queue the deferred ISR work and execute it in a dedicated task or thread.
- VxWorks and FreeRTOS are two popular open-source RTOSes that support interrupts and provide various features and tools to manage them, such as:
  - VxWorks:
    - It supports nested interrupts, which means that an ISR can be interrupted by another ISR of higher priority.
    - It provides a work queue mechanism, which allows ISRs to defer some of their work to a kernel task that runs at a configurable priority.
    - It provides a watchdog timer mechanism, which allows ISRs to monitor the execution time of tasks and trigger an exception if a task exceeds a specified timeout.
    - It provides an exception handling and diagnostic reporting (ED&R) system, which allows ISRs to handle software exceptions and generate diagnostic information for debugging purposes.
  - FreeRTOS:
    - It supports interrupt nesting, which means that an ISR can be interrupted by another ISR of higher priority, but only if the interrupt controller supports it.
    - It provides an interrupt safe version of queue API, which allows ISRs to read and write data from queues using special functions, such as xQueueSendToBackFromISR and xQueueReceiveFromISR.
    - It provides a software timer mechanism, which allows ISRs to create and start timers that execute a callback function in task context after a specified period.
    - It provides a configASSERT macro, which allows ISRs to check the validity of parameters and conditions and trigger a breakpoint if an assertion fails.

: https://microcontrollerslab.com/freertos-interrupt-management-examples-with-arduino/
: https://www.freertos.org/implementation/a00011.html
: https://scienceprog.com/most-popular-open-source-rtos-comparison-for-embedded-systems/
: https://www.digikey.com/en/maker/projects/introduction-to-rtos-solution-to-part-9-hardware-interrupts/3ae7a68462584e1eb408e1638002e9ed
: https://www.youtube.com/watch?v=tlHLaA8ib1M
: https://learning.windriver.com/vxworks-exceptions-interrupts-and-watchdog-timers



### I/O Systems

- Input/output (I/O) systems are the components that enable communication between a real-time operating system (RTOS) and the external devices or networks.
- I/O systems can be classified into two types: synchronous and asynchronous.
- Synchronous I/O systems block the execution of a task until the I/O operation is completed, while asynchronous I/O systems allow the task to continue its execution while the I/O operation is performed in the background.
- Some examples of synchronous I/O systems are serial ports, parallel ports, and memory-mapped I/O devices.
- Some examples of asynchronous I/O systems are interrupt-driven I/O devices, direct memory access (DMA) devices, and network interfaces.
- I/O systems can also be categorized into character-oriented and block-oriented devices.
- Character-oriented devices transfer data one byte at a time, while block-oriented devices transfer data in fixed-size blocks.
- Some examples of character-oriented devices are keyboards, mice, and printers.
- Some examples of block-oriented devices are hard disks, flash memory, and optical disks.
- I/O systems can have different levels of abstraction, such as device drivers, device-independent I/O, and high-level I/O libraries.
- Device drivers are the lowest level of abstraction, and they provide the interface between the RTOS and the specific hardware device.
- Device-independent I/O is the intermediate level of abstraction, and it provides a uniform interface for accessing different types of devices, such as files, sockets, and pipes.
- High-level I/O libraries are the highest level of abstraction, and they provide convenient functions for performing common I/O operations, such as reading and writing text, binary, or formatted data.

- VXWORKS and FREE RTOS are two popular RTOSs that support various I/O systems for embedded applications.
- VXWORKS is a deterministic, priority-based preemptive RTOS that prioritizes real-time embedded applications. It has low latency and minimal jitter .
- VXWORKS supports a wide range of I/O devices, such as serial, parallel, USB, Ethernet, PCI, SCSI, IDE, and CAN.
- VXWORKS also provides device-independent I/O functions, such as open(), close(), read(), write(), and ioctl(), as well as high-level I/O libraries, such as stdio, stdlib, and stdarg.
- FREE RTOS is a thread library rather than an operating system, although command line interface and POSIX-like input/output (I/O) abstraction are available.
- FREE RTOS implements multiple threads by having the host program call a thread tick method at regular short intervals.
- FREE RTOS supports various I/O devices, such as serial, SPI, I2C, and GPIO, through the use of peripheral libraries provided by the hardware vendors.
- FREE RTOS also provides device-independent I/O functions, such as xStreamBufferSend(), xStreamBufferReceive(), and xStreamBufferSetTriggerLevel(), as well as high-level I/O libraries, such as FreeRTOS+IO and FreeRTOS+FAT.



### General Architecture

- An RTOS (Real-Time Operating System) is a software system that provides predictable and deterministic behavior for time-sensitive applications.
- An RTOS typically consists of a kernel, which manages the core functions such as task scheduling, inter-task communication, synchronization, memory management, and interrupt handling.
- An RTOS may also include middleware, which provides additional services such as networking, file system, graphics, security, and device drivers.
- An RTOS may be classified into two types based on its kernel architecture: monolithic and microkernel.
- A monolithic kernel is a single large program that runs in the privileged mode of the processor and contains all the core functions and services of the RTOS. A monolithic kernel is faster and simpler to implement, but less modular and more prone to errors and security breaches.
- A microkernel is a small program that runs in the privileged mode of the processor and provides only the basic functions of the RTOS, such as task switching, inter-task communication, and interrupt handling. A microkernel delegates the other functions and services to separate programs that run in the user mode of the processor. A microkernel is more modular and secure, but slower and more complex to implement.
- VxWorks and FreeRTOS are two examples of RTOS that have different kernel architectures.
- VxWorks is a monolithic kernel RTOS that supports both preemptive and cooperative multitasking, priority-based scheduling, inter-process communication, memory protection, and real-time POSIX compliance. VxWorks is widely used in aerospace, defense, industrial, and automotive applications.
- FreeRTOS is a microkernel RTOS that supports preemptive multitasking, priority-based scheduling, inter-task communication, and memory allocation. FreeRTOS is designed for embedded systems with limited resources and is open source and portable. FreeRTOS is used in various domains such as IoT, medical, and consumer electronics.



### Device Driver Studies for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A device driver is a software component that allows an operating system to communicate with a hardware device, such as a keyboard, mouse, disk, network card, etc.
- A device driver typically implements a standard interface, such as POSIX or Windows API, to provide access to the device's functionality and data.
- A device driver may also perform tasks such as initialization, configuration, error handling, power management, and interrupt handling for the device.
- A device driver may be classified into different types, such as character, block, network, or USB drivers, depending on the nature and functionality of the device.
- A device driver may be implemented in different ways, such as kernel mode, user mode, or hybrid mode, depending on the level of access and privilege required for the device.
- A device driver may be loaded statically or dynamically, depending on the availability and demand of the device.

- VXWORKS is a real-time operating system (RTOS) for embedded systems, developed by Wind River Systems. It is widely used in aerospace, defense, industrial, automotive, medical, and consumer electronics applications.
- VXWORKS is a deterministic, priority-based preemptive RTOS with low latency and minimal jitter. It prioritizes real-time embedded applications over other tasks and interrupts  .
- VXWORKS is built on an upgradable, future-proof architecture that supports multiple processor architectures, such as x86, ARM, PowerPC, MIPS, etc. It also supports multiple programming languages, such as C, C++, Ada, Java, etc .
- VXWORKS provides a rich set of features and services, such as memory management, file system, network stack, security, graphics, device drivers, etc. It also supports various standards and protocols, such as POSIX, TCP/IP, USB, Bluetooth, etc .
- VXWORKS supports various development tools and environments, such as Wind River Workbench, Eclipse, Visual Studio, etc. It also supports various debugging and testing tools, such as Wind River Diab Compiler, Wind River Simics, Wind River Helix Virtualization Platform, etc .

- FREE RTOS is a market-leading real-time operating system (RTOS) for microcontrollers and small microprocessors, developed by Richard Barry and maintained by Amazon Web Services. It is widely used in IoT, automotive, industrial, medical, and consumer electronics applications.
- FREE RTOS is a portable, open source, and royalty-free RTOS that can run on various platforms, such as ARM, AVR, PIC, MSP430, etc. It also supports various compilers, such as GCC, IAR, Keil, etc.
- FREE RTOS provides a minimal and simple kernel that supports basic features and services, such as task management, inter-task communication, synchronization, timers, memory allocation, etc. It also supports various optional components, such as TCP/IP stack, FAT file system, USB stack, etc.
- FREE RTOS supports various development tools and environments, such as FreeRTOS+Trace, FreeRTOS+CLI, FreeRTOS+IO, etc. It also supports various debugging and testing tools, such as FreeRTOS+Simulator, FreeRTOS+TCP, FreeRTOS+FAT, etc.
- FREE RTOS is designed to be easy to use and understand, with a well-documented and consistent API. It also provides various examples and demos for different platforms and applications.

- A device driver for VXWORKS or FREE RTOS is a software component that allows the RTOS to communicate with a hardware device, such as a sensor, actuator, display, etc.
- A device driver for VXWORKS or FREE RTOS typically implements a standard interface, such as VxWorks IO system or FreeRTOS+IO, to provide access to the device's functionality and data.
- A device driver for VXWORKS or FREE RTOS may also perform tasks such as initialization, configuration, error handling, power management, and interrupt handling for the device.
- A device driver for VXWORKS or FREE RTOS may be classified into different types, such as character, block, network, or USB drivers, depending on the nature and functionality of the device.
- A device driver for VXWORKS or FREE RTOS may be implemented in different ways, such as kernel mode, user mode



Hello, I am Sydney, your AI assistant. I will help you with your query. Here is the content I have generated for you:

### Driver Module explanation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- A driver module is a software component that interacts with a specific hardware device or peripheral, such as a disk, a network interface card, a sensor, etc.
- A driver module provides a uniform and abstract interface to the device, hiding the details of its implementation and operation from the user application or the operating system.
- A driver module typically consists of two parts: a device driver and a device controller.
  - A device driver is the part of the driver module that communicates with the operating system, such as VxWorks or FreeRTOS, and handles requests from user applications or system services to access the device.
  - A device controller is the part of the driver module that communicates with the hardware device, such as sending commands, reading data, handling interrupts, etc.
- A driver module can be implemented in different ways, depending on the operating system, the device, and the design choices.
  - For example, VxWorks provides a standard driver model that supports a Linux/POSIX-like interface to access devices, such as open(), read(), write(), ioctl(), etc. 
  - FreeRTOS also provides a similar interface, called FreeRTOS Plus IO, that sits between a peripheral driver library and a user application to provide a common interface to all supported peripherals across all supported platforms. 
  - Alternatively, a driver module can be implemented as a custom application-specific interface, that may offer more flexibility and performance, but less portability and compatibility.
- A driver module can be developed using various tools and methods, depending on the operating system, the device, and the requirements.
  - For example, VxWorks offers a board support package (BSP) and device driver development kit (DDK) that provide the necessary components and documentation to port VxWorks to custom hardware and develop device drivers. 
  - FreeRTOS also offers a BSP and DDK that provide the necessary components and documentation to port FreeRTOS to custom hardware and develop device drivers. 
  - Alternatively, a driver module can be developed using third-party tools or libraries, such as MapuSoft's OS Changer VxWorks Porting kit, that can automatically migrate and re-use VxWorks applications to FreeRTOS. 

I hope this content is helpful for you. If you have any questions or feedback, please let me know.😊



### Implementation of Device Driver for a Peripheral

- A device driver is a software application that allows a hardware device (such as a printer or a keyboard) to interact with the operating system (such as Windows or Linux) of a computer.
- A device driver acts as a translator between the operating system and the peripheral device, which is connected to a computer bus (such as USB or PCI) that transfers data between them .
- A device driver consists of a physical structure of modes that represent the peripheral device and its functions. These modes can be classified as:
  - Initialization mode: This mode is executed when the device driver is loaded into the memory and initializes the device and its registers.
  - Normal mode: This mode is executed when the device driver receives an I/O request from the operating system or an application and performs the corresponding operation on the device.
  - Interrupt mode: This mode is executed when the device driver receives an interrupt signal from the device and handles the event (such as data transfer or error) accordingly.
  - Termination mode: This mode is executed when the device driver is unloaded from the memory and releases the device and its resources.
- The implementation of a device driver for a peripheral depends on the type of the device, the type of the bus, and the type of the operating system. Some general steps are:
  - Identify the device specifications and requirements, such as the device model, the device features, the device protocol, the device commands, and the device registers.
  - Identify the bus specifications and requirements, such as the bus type, the bus speed, the bus address, the bus protocol, and the bus commands.
  - Identify the operating system specifications and requirements, such as the operating system version, the operating system interface, the operating system services, and the operating system standards.
  - Design the device driver architecture and components, such as the device driver modes, the device driver functions, the device driver data structures, and the device driver interfaces.
  - Write the device driver code in a programming language (such as C or C++) that is compatible with the operating system and the device.
  - Compile and link the device driver code into a binary file (such as a .sys or a .ko file) that can be loaded into the memory and executed by the operating system.
  - Test and debug the device driver using tools (such as debuggers or simulators) that can monitor and manipulate the device driver behavior and the device state.
  - Install and configure the device driver on the computer system using methods (such as plug-and-play or manual installation) that can register and activate the device driver with the operating system.
  - Update and maintain the device driver according to the changes in the device, the bus, or the operating system.

