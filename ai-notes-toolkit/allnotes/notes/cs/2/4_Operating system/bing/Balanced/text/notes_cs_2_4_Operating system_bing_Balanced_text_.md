

## Unit 1 - Introduction : Operating system and functions

- An operating system (OS) is a program that manages a computer's resources, especially the allocation of those resources among other programs.
- An operating system performs basic functions such as booting, memory management, process management, resource management, security, control over system performance, job accounting, error detection, and coordination between other software and users  .
- An operating system also provides an interface for users and applications to interact with the hardware and other software of the computer.
- Examples of operating systems include Windows, Linux, MacOS, Android, iOS, etc. Each operating system has different features, advantages, and disadvantages.



### Classification of Operating Systems

Operating systems are software programs that manage the hardware and software resources of a computer and provide services to the users and applications. Operating systems can be classified based on different criteria, such as:

- Processing method: how the operating system handles multiple tasks or programs at the same time.
- User interface: how the operating system interacts with the users and displays information.
- Number of users: how many users can use the operating system simultaneously or share its resources.
- Number of processors: how many processors or cores the operating system can utilize or control.
- Purpose: what kind of devices or applications the operating system is designed for.

Some of the common types of operating systems based on these criteria are:

- Batch operating system: a type of operating system that processes a set of similar tasks or jobs in a batch, without user interaction. The jobs are submitted to the system and executed one after another, usually in a sequential order. Batch operating systems are mainly used for large-scale data processing or scientific computing.
- Multiprogramming operating system: a type of operating system that allows multiple programs or processes to run concurrently on a single processor, by switching between them in a fixed or variable time interval. The operating system allocates memory and other resources to each process and manages their execution. Multiprogramming operating systems are used to improve the CPU utilization and throughput of the system.
- Multitasking operating system: a type of operating system that allows multiple tasks or programs to run simultaneously on a single or multiple processors, by dividing the CPU time into small slices and assigning them to different tasks. The operating system also manages the priority and synchronization of the tasks. Multitasking operating systems are used to provide a responsive and interactive user experience and support multiple applications.
- Multiprocessing operating system: a type of operating system that can run on a system with more than one processor or core, and can distribute the workload among them. The operating system coordinates the communication and synchronization between the processors and ensures the consistency and integrity of the data. Multiprocessing operating systems are used to increase the performance and reliability of the system.
- Real-time operating system: a type of operating system that can respond to events or requests within a specified time limit, without any delay or interruption. The operating system prioritizes the tasks based on their urgency and deadlines, and guarantees their completion. Real-time operating systems are used for time-critical or safety-critical applications, such as embedded systems, industrial control, robotics, or multimedia.
- Distributed operating system: a type of operating system that can run on a network of computers or devices, and can coordinate and share their resources and services. The operating system provides a transparent and consistent view of the system to the users and applications, and handles the communication, synchronization, and fault tolerance among the nodes. Distributed operating systems are used for scalable and distributed computing, such as cloud computing, grid computing, or peer-to-peer computing.
- Network operating system: a type of operating system that runs on a server and provides the capability to manage data, users, groups, security, applications, and other network resources. The operating system allows the clients to access the server and its services over the network, and supports various network protocols and standards. Network operating systems are used for network administration and management, such as file sharing, email, web hosting, or database management.
- Mobile operating system: a type of operating system that runs on a mobile device, such as a smartphone, tablet, or wearable device. The operating system provides a user-friendly and touch-based interface, and supports various features and functions, such as wireless communication, multimedia, sensors, GPS, camera, or app store. Mobile operating systems are used for personal and professional use, such as communication, entertainment, education, or productivity.



### Batch for the notes of the Unit 1 - Introduction : Operating system and functions in the subject of Operating system

- An operating system (OS) is a software program that manages the hardware and software resources of a computer.
- The OS performs basic tasks, such as controlling and allocating memory, prioritizing the processing of instructions, controlling input and output devices, facilitating network communication, and managing files.
- The OS also provides a user interface, such as a graphical user interface (GUI), that allows users to interact with the computer and its applications.
- The OS can be classified into different types, such as single-user, multi-user, multitasking, multiprocessing, distributed, real-time, embedded, and mobile.
- Some examples of popular operating systems are Windows, Linux, macOS, Android, iOS, and UNIX.
- The main functions of an OS are:
  - Process management: The OS creates and terminates processes, assigns them to processors, and schedules their execution according to various algorithms.
  - Memory management: The OS allocates and deallocates memory to processes, and implements techniques such as paging and segmentation to optimize the use of physical and virtual memory.
  - Device management: The OS controls the communication and data transfer between the CPU and the input/output devices, such as keyboards, mice, printers, scanners, monitors, disks, etc.
  - File management: The OS organizes the data on the storage devices into files and directories, and provides operations such as creating, deleting, renaming, copying, moving, and searching files.
  - Security and protection: The OS protects the system and the data from unauthorized access, malicious attacks, and accidental errors, by implementing mechanisms such as authentication, encryption, access control, backup, and recovery.
  - Networking and communication: The OS enables the communication and data exchange between different computers and devices over a network, by implementing protocols such as TCP/IP, HTTP, FTP, SMTP, etc.
  - User interface: The OS provides a user-friendly and intuitive interface that allows the user to interact with the system and the applications, by using graphical elements such as windows, icons, menus, buttons, etc.



### Interactive Notes for Unit 1 - Introduction: Operating System and Functions

- An operating system (OS) is a software program that manages the hardware and software resources of a computer.
- The OS performs basic tasks, such as controlling and allocating memory, prioritizing the processing of instructions, controlling input and output devices, facilitating network communication, and managing files.
- The OS also provides a user interface, such as a graphical user interface (GUI), that allows users to interact with the computer and its applications.
- The OS can be classified into different types based on various criteria, such as the number of users, the number of tasks, the type of hardware, the type of interface, the degree of control, and the purpose of use.
- Some common types of OS are:
  - Single-user OS: Only one user can use the computer at a time, such as MS-DOS and Windows 95.
  - Multi-user OS: Multiple users can use the computer simultaneously, such as UNIX and Linux.
  - Single-tasking OS: Only one task can be performed at a time, such as Palm OS and iOS.
  - Multi-tasking OS: Multiple tasks can be performed concurrently, such as Windows 10 and Android.
  - Real-time OS: The OS responds to events or inputs within a fixed time, such as QNX and VxWorks.
  - Batch OS: The OS processes a batch of similar tasks without user intervention, such as IBM OS/360 and MS-DOS.
  - Distributed OS: The OS manages a network of computers that work together, such as Amoeba and Plan 9.
  - Embedded OS: The OS is embedded in a device or system, such as Arduino and Raspberry Pi.
- The OS has several functions that can be grouped into four categories:
  - Process management: The OS creates, schedules, and terminates processes, and manages inter-process communication and synchronization.
  - Memory management: The OS allocates and deallocates memory to processes, and implements paging and swapping techniques to optimize memory usage.
  - Device management: The OS controls and coordinates the access of processes to various input and output devices, such as keyboards, mice, monitors, printers, disks, etc.
  - File management: The OS organizes and maintains files and directories on different storage devices, and provides file access and protection mechanisms.



### Time sharing operating system

- A time sharing operating system is a type of operating system that allows multiple users to share the same computer simultaneously by dividing the CPU time among the users' programs .
- A time sharing operating system uses the concept of multiprogramming, which means that multiple programs can be loaded into the main memory and executed concurrently by switching the CPU among them.
- A time sharing operating system also provides the feature of interactive computing, which means that the users can interact with their programs while they are running and provide inputs or outputs.
- A time sharing operating system aims to minimize the response time for each user and maximize the CPU utilization.
- A time sharing operating system requires the following components:
  - A scheduler, which decides which program gets the CPU next based on some criteria such as priority, fairness, or round-robin.
  - A dispatcher, which switches the CPU from one program to another by saving and restoring the context of each program.
  - A memory manager, which allocates and deallocates the main memory space for each program and handles the virtual memory and paging mechanisms.
  - A file system, which manages the storage and retrieval of files and directories on the secondary storage devices.
  - A device manager, which controls the access and operation of the input/output devices such as keyboard, mouse, printer, etc.
  - A user interface, which provides the means for the users to communicate with the operating system and their programs, such as command-line, graphical, or web-based interfaces.
- Some examples of time sharing operating systems are UNIX, Linux, Windows, and MacOS.



### Real Time System for the notes of the Unit 1 - Introduction : Operating system and functions in the subject of Operating system

- A real time system is a system that must process data and events within a specific time limit, otherwise it may cause failure or loss .
- A real time operating system (RTOS) is an operating system that supports the development and execution of real time applications    .
- An RTOS has two key features: predictability and determinism.
  - Predictability means that the system can guarantee that a task will be completed within a certain time bound.
  - Determinism means that the system can guarantee that a task will always produce the same output for the same input.
- An RTOS is different from a general-purpose operating system (GPOS), such as Windows or Linux, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities .
  - A GPOS is designed to optimize the average performance and throughput of the system, not the worst-case response time.
  - A GPOS may have unpredictable delays or interruptions due to factors such as paging, swapping, caching, or preemption.
- An RTOS is also different from a bare-metal system, which is a system that runs without an operating system and directly interacts with the hardware.
  - A bare-metal system may have low overhead and high performance, but it lacks the features and services of an operating system, such as memory management, file system, network stack, or device drivers.
  - A bare-metal system may also have difficulty in supporting complex or concurrent applications, or porting to different hardware platforms.
- An RTOS provides the following functions and services to support real time applications    :
  - Real time multithreading, which allows the creation and execution of multiple tasks that can run concurrently and independently.
  - Inter-thread communication and synchronization, which allows the exchange of data and signals between tasks, and the coordination of their execution order and timing.
  - Memory management, which allocates and deallocates memory for tasks and data, and ensures that memory is used efficiently and safely.
  - Input/output management, which handles the interaction with external devices, such as sensors, actuators, or displays, and provides device drivers and protocols.
  - Interrupt handling, which responds to external or internal events that require immediate attention, and invokes the appropriate tasks or handlers.
  - Timer and clock services, which provide accurate and reliable measurement and control of time, and support periodic or one-shot tasks.
  - Power management, which optimizes the energy consumption and battery life of the system, and supports low-power modes or wake-up events.
  - Debugging and testing tools, which help the developers to find and fix errors, and to verify the correctness and performance of the system.
- An RTOS can be classified into three types based on the strictness of the time constraints:
  - Hard real time operating system, which guarantees that critical tasks will be completed within a specified time bound, otherwise it may cause catastrophic consequences.
  - Soft real time operating system, which provides some relaxation in the time limit, and allows some tasks to miss their deadlines occasionally without causing serious damage.
  - Firm real time operating system, which requires that tasks meet their deadlines, but does not care about the quality of the output if they miss their deadlines.
- An RTOS can be used for various applications that require real time performance, such as    :
  - Embedded systems, such as automotive, aerospace, industrial, medical, or consumer electronics    .
  - Robotics, such as autonomous vehicles, drones, or humanoid robots    .
  - Multimedia, such as audio, video, or gaming   [^4



### Multiprocessor Systems

- A multiprocessor system is a computer system that has two or more central processing units (CPUs) that work in parallel to perform the required operations .
- The main objective of using a multiprocessor system is to increase the execution speed of the system and to handle larger amounts of information .
- The multiple CPUs in a multiprocessor system are connected with physical memory, computer buses, clocks, and peripheral devices. These systems are referred to as tightly coupled systems .
- There are two main types of multiprocessor systems: asymmetric multiprocessing system and symmetric multiprocessing system .
  - In an asymmetric multiprocessing system, one processor behaves as a master and the other processors behave as slaves. The master processor assigns tasks to the slave processors and coordinates the overall system. The slave processors execute the tasks assigned by the master processor and communicate with it .
  - In a symmetric multiprocessing system, all processors are equal and share the same operating system, memory, and peripherals. Each processor can perform any task and can communicate with any other processor. The operating system is responsible for scheduling and load balancing among the processors .
- The advantages of multiprocessor systems are:
  - They can increase the system performance and throughput by exploiting parallelism and concurrency .
  - They can improve the system reliability and fault tolerance by providing redundancy and backup .
  - They can reduce the system cost and power consumption by using smaller and cheaper processors instead of a single large and expensive processor .
- The challenges of multiprocessor systems are:
  - They require more complex hardware and software design and coordination .
  - They may face scalability and synchronization issues as the number of processors increases .
  - They may suffer from memory contention and communication overhead among the processors .



### Multiuser Systems

- A multiuser system is an operating system that allows multiple users to access the same computer system and its resources simultaneously or consecutively .
- A multiuser system can be classified into three types based on how the users share the CPU time and memory space:
  - Distributed system: A system where multiple computers are connected by a network and each computer runs its own operating system and applications. The users can communicate and share data and resources across the network. Examples of distributed systems are the internet, cloud computing, and peer-to-peer networks.
  - Time-sliced system: A system where a single CPU is shared among multiple users by switching between them in a fixed time interval. The users are unaware of the switching and feel as if they have the CPU to themselves. The switching is done by the operating system using a scheduling algorithm. Examples of time-sliced systems are UNIX, Linux, and Windows.
  - Multiprocessor system: A system where multiple CPUs are installed in a single computer system and share the same memory and peripherals. The operating system can assign different tasks to different CPUs and achieve parallel processing. Examples of multiprocessor systems are supercomputers, servers, and some personal computers.
- The advantages of a multiuser system are:
  - Increased efficiency: The system can utilize the CPU and memory resources more effectively by serving multiple users at the same time.
  - Increased reliability: The system can handle failures and errors more gracefully by isolating the affected users and processes and continuing the operation for the rest of the users and processes.
  - Increased security: The system can protect the data and resources of each user from unauthorized access and modification by enforcing access control policies and authentication mechanisms.
  - Increased scalability: The system can accommodate more users and processes by adding more hardware and software components as needed.
- The disadvantages of a multiuser system are:
  - Increased complexity: The system requires more sophisticated design and implementation to manage the concurrency, synchronization, and communication among multiple users and processes.
  - Increased overhead: The system consumes more CPU time and memory space for the operating system functions and services, such as scheduling, memory management, and interprocess communication.
  - Increased risk: The system is more vulnerable to attacks and breaches by malicious users and programs, as well as to performance degradation and resource contention by excessive or improper usage.



### Multiprocess Systems

- A multiprocess system is a computer system that has more than one processor or CPU that can work in parallel to execute multiple tasks .
- The main objective of a multiprocess system is to increase the computing power and the execution speed of the system .
- A multiprocess system can be classified into two types: symmetric multiprocessing (SMP) and asymmetric multiprocessing (AMP) .
- In SMP, all the processors are identical and have equal access to the shared resources, such as memory, buses, clocks, and peripheral devices . The operating system can assign any task to any processor without any preference .
- In AMP, the processors are different and have different roles and access to the shared resources . The operating system can assign specific tasks to specific processors according to their capabilities .
- Some examples of multiprocess systems are IBM System/370, Intel Pentium, Sun SPARC, and Cray supercomputers .
- Some advantages of multiprocess systems are :
  - They can improve the performance and reliability of the system by distributing the workload among the processors.
  - They can enhance the scalability and flexibility of the system by adding or removing processors as needed.
  - They can support parallel processing and concurrency, which can improve the efficiency and responsiveness of the system.
- Some disadvantages of multiprocess systems are :
  - They require more complex hardware and software design and coordination to ensure the synchronization and communication among the processors and the shared resources.
  - They may incur more overhead and contention due to the increased number of processors and the shared resources.
  - They may face challenges in load balancing and fault tolerance, which can affect the performance and reliability of the system.



### Multithreaded Systems

- A multithreaded system is a system that allows multiple threads of execution to run concurrently on a single processor or a multi-core processor, supported by the operating system.
- A thread is a path of execution within a process. A process can have multiple threads that share the same memory and resources.
- Multithreading enables a program or an operating system to handle multiple user requests or tasks at the same time without requiring multiple copies of the program or the system.
- Multithreading has several advantages, such as:
  - Improved responsiveness: A program can continue to run even if some of its threads are blocked or performing a lengthy operation.
  - Resource sharing: Threads can share the same data and resources of the process that created them, which reduces the overhead of creating and managing multiple processes.
  - Higher throughput: A processor can utilize its idle time by switching between multiple threads, which increases the overall performance and efficiency of the system.
  - Scalability: A multithreaded system can take advantage of multiple processors or cores by distributing the workload among them, which improves the speed and concurrency of the system.
- Multithreading also has some challenges, such as:
  - Synchronization: Threads need to coordinate their access to shared data and resources to avoid inconsistency and deadlock.
  - Testing and debugging: Multithreaded programs are more complex and prone to errors than single-threaded programs, and they require more tools and techniques to test and debug.
  - Overhead: Creating and managing multiple threads involves some overhead in terms of memory, CPU time, and context switching.
- Multithreading can be implemented at different levels, such as:
  - User-level: The threads are created and managed by the user program, and the operating system is unaware of them. This gives the user more control and flexibility, but it also requires more effort and responsibility.
  - Kernel-level: The threads are created and managed by the operating system, and the user program interacts with them through system calls. This gives the operating system more control and efficiency, but it also involves more overhead and dependency.
  - Hybrid-level: The threads are created and managed by both the user program and the operating system, and they communicate with each other through a middleware layer. This combines the benefits and drawbacks of both user-level and kernel-level multithreading.



### Operating System Structure

An operating system is a program that manages a computer's resources, especially the allocation of those resources among other programs. For efficient performance and implementation, an operating system should be partitioned into separate subsystems, each with carefully defined tasks, inputs, outputs, and performance characteristics. These subsystems can then be arranged in various architectural configurations, depending on the design goals and constraints of the operating system.

Some of the common structures of operating systems are:

- **Simple structure**: Such operating systems do not have well defined structure and are small, simple and limited systems. They run as a single program in the kernel mode, with all the functions intermingled. An example of this structure is MS-DOS.
- **Monolithic structure**: In this structure, the operating system is divided into a number of modules or layers, each with a specific function. The modules can communicate with each other through well-defined interfaces. However, all the modules run in the same address space, which makes the system vulnerable to errors and difficult to debug. An example of this structure is UNIX.
- **Layered structure**: In this structure, the operating system is organized as a hierarchy of layers, each built on top of the lower ones. The lowest layer interacts with the hardware, while the highest layer provides the user interface. Each layer provides a set of services to the higher layers, and uses the services of the lower layers. This structure simplifies the design and implementation of the operating system, but may introduce some overhead and inefficiency. An example of this structure is THE operating system.
- **Microkernel structure**: In this structure, the operating system is divided into two parts: a small core or microkernel that runs in the kernel mode, and a number of servers that run in the user mode. The microkernel provides the basic services, such as interprocess communication, memory management, and process management. The servers provide the higher-level services, such as file system, device drivers, and network protocols. This structure enhances the modularity, reliability, and portability of the operating system, but may increase the system call overhead and complexity. An example of this structure is Mach operating system.
- **Modular structure**: In this structure, the operating system is composed of a number of modules or components, each with a specific function. The modules can be dynamically loaded and unloaded, and can communicate with each other through message passing or shared memory. This structure allows the operating system to be flexible, extensible, and adaptable to different hardware and software environments. An example of this structure is Windows NT operating system.



### Layered structure for the notes of the Unit 1 - Introduction : Operating system and functions in the subject of Operating system

- An operating system (OS) is a software that manages the hardware and software resources of a computer system and provides common services for the execution of various application programs.
- An OS can be viewed as a layered structure, where each layer provides a set of functions and services to the higher-level layers and uses the functions and services of the lower-level layers.
- The layered structure of an OS can be classified into four main categories: user interface, system services, system calls, and hardware abstraction layer.

#### User interface
- The user interface is the layer that interacts with the users and allows them to access the OS functions and services.
- The user interface can be graphical (GUI) or command-line (CLI) based, depending on the preference and needs of the users.
- The user interface provides features such as windows, menus, icons, buttons, keyboards, mice, touchscreens, etc. for GUI, and commands, arguments, options, prompts, etc. for CLI.
- The user interface also handles the input and output devices, such as monitors, printers, scanners, speakers, etc.

#### System services
- The system services are the layer that provides the core functionality of the OS, such as process management, memory management, file system management, device management, security, networking, etc.
- The system services are responsible for creating, scheduling, terminating, and synchronizing processes, allocating and deallocating memory, organizing and accessing files and directories, controlling and communicating with devices, enforcing access control and authentication, enabling data transmission and reception, etc.
- The system services are implemented as a set of system programs or daemons that run in the background and perform various tasks.

#### System calls
- The system calls are the layer that provides the interface between the system services and the application programs.
- The system calls are the requests made by the application programs to the OS to use the system services and resources.
- The system calls are usually implemented as a library of functions that are invoked by the application programs using a specific syntax and semantics.
- The system calls can be classified into five main categories: process control, file manipulation, device manipulation, information maintenance, and communication.

#### Hardware abstraction layer
- The hardware abstraction layer (HAL) is the layer that provides the interface between the system calls and the hardware devices.
- The HAL is responsible for hiding the details and differences of the hardware devices from the higher-level layers and presenting a uniform and consistent view of the hardware to the OS.
- The HAL also handles the device drivers, which are the software components that communicate with the hardware devices and translate the system calls into device-specific commands.
- The HAL enables the OS to support a variety of hardware devices and platforms without modifying the higher-level layers.



### System Components for the notes of the Unit 1 - Introduction : Operating system and functions

- A system component is a process, program, utility, or another part of a computer's operating system that helps to manage different areas of the computer.
- An operating system is a large and complex system that can only be created by partitioning into small pieces.
- The main components of an operating system are  :
  - Process Management: A process is a program in execution. A process can be suspended temporarily and the execution can be resumed later. Process management involves creating and deleting processes, scheduling CPU time, managing memory, and synchronizing processes.
  - File Management: A file is a collection of related information which is defined by its creator. Files are used for long-term storage and for both input and output. File management involves creating and deleting files, organizing files in directories, controlling access to files, and managing disk space .
  - Network Management: A network is a collection of computers and devices that are connected by communication channels. Network management involves establishing and maintaining network connections, transmitting and receiving data, and providing network security.
  - Main Memory Management: Main memory is the primary storage area of the computer. It is volatile and fast. Main memory management involves allocating and deallocating memory space to processes, managing virtual memory, and ensuring memory protection .
  - Secondary Storage Management: Secondary storage is the non-volatile storage area of the computer. It is slower and cheaper than main memory. Secondary storage management involves managing disk drives, disk partitions, disk formatting, and disk caching .
  - I/O Device Management: I/O devices are the peripherals that allow the computer to interact with the external world. They include keyboards, mice, monitors, printers, scanners, etc. I/O device management involves controlling the operation of I/O devices, buffering and caching I/O data, and handling I/O errors .
  - Security Management: Security management involves protecting the computer system and its resources from unauthorized access, malicious attacks, and accidental damage. It includes implementing authentication, encryption, firewall, antivirus, and backup mechanisms.
  - Command Interpreter System: A command interpreter system is a program that allows the user to interact with the operating system. It can be a graphical user interface (GUI) or a command-line interface (CLI). It accepts commands from the user and executes them by invoking the appropriate system components .



### Operating System Services

An operating system is a software program that controls and manages the hardware and other software on a computer. It provides an environment for the execution of programs and the interaction of users with the computer system. An operating system also offers various services to both the users and the programs. Some of the common operating system services are:

- **User Interface:** This service allows the user to communicate with the computer system through a graphical or textual interface. The user interface can be a command-line interface (CLI), a graphical user interface (GUI), or a touch-based interface. The user interface enables the user to enter commands, select options, view output, and perform other tasks.
- **Program Execution:** This service allows the computer system to load and run programs in the memory. The operating system is responsible for creating, scheduling, and terminating processes, as well as managing their resources and states. The operating system also handles the communication and synchronization between processes.
- **File System Manipulation:** This service allows the user and the programs to create, delete, modify, and access files and directories on the storage devices. The operating system manages the file system structure, the file attributes, the file permissions, and the file allocation. The operating system also provides file system security and backup mechanisms.
- **Input/Output Operations:** This service allows the user and the programs to interact with the input and output devices, such as the keyboard, mouse, monitor, printer, scanner, etc. The operating system abstracts the details of the device drivers and provides a uniform interface for the device access. The operating system also performs buffering, caching, and spooling of the input and output data.
- **Communication:** This service allows the user and the programs to exchange information between different processes, either on the same computer system or on different computer systems connected by a network. The operating system provides various methods of communication, such as message passing, shared memory, pipes, sockets, etc. The operating system also implements the protocols and standards for the network communication.
- **Resource Allocation:** This service allows the operating system to allocate the available resources, such as the CPU, memory, disk space, etc., to the processes according to their needs and priorities. The operating system uses various algorithms and policies to achieve efficient and fair resource allocation. The operating system also performs resource accounting and auditing.
- **Error Detection:** This service allows the operating system to detect and handle the errors that may occur in the hardware or the software components of the computer system. The operating system can use various techniques, such as exception handling, interrupt handling, debugging, logging, etc., to deal with the errors. The operating system also provides error recovery and prevention mechanisms.
- **Accounting:** This service allows the operating system to keep track of the usage and performance of the computer system and its resources. The operating system can collect and record various statistics, such as the CPU time, memory usage, disk space, network traffic, etc., for each process and user. The operating system can also use this information for billing, auditing, and optimization purposes.



### Reentrant Kernels

- A reentrant kernel is a kernel that allows multiple processes (or their corresponding kernel threads) to execute kernel code simultaneously .
- A reentrant kernel enables a process to give up the CPU while in kernel mode, without blocking other processes from entering kernel mode .
- A reentrant kernel is useful for handling IO wait, where a process needs to wait for a device to complete an operation before resuming execution.
- A reentrant kernel requires that the kernel code is written in a way that avoids data corruption or inconsistency when multiple processes access the same data structures.
- A reentrant kernel can improve the performance and responsiveness of the system, especially on multiprocessor systems where multiple CPUs can run kernel code concurrently .



### Monolithic and Microkernel Systems

- A **monolithic kernel** is an operating system architecture where the entire operating system is working in **kernel space**.
- A **microkernel** is a kernel type that provides mechanisms such as low-level address space management, thread management and interprocess communication to implement an operating system.
- The main difference between microkernel and monolithic kernel is that the microkernel-based systems have OS services and kernel in **separate address spaces** while the monolithic kernel-based systems have OS services and kernel in the **same address space** .
- Some advantages of monolithic kernel are:
  - It provides CPU scheduling, memory management, file management, and other operating system functions through **system calls**.
  - It is **easy to design and implement**.
  - It has **high performance** as there is no overhead of switching between user mode and kernel mode.
- Some disadvantages of monolithic kernel are:
  - It is **difficult to maintain and debug** as any change in one module requires recompilation of the entire kernel.
  - It is **less secure and reliable** as any error in one module can crash the entire system.
  - It is **less flexible and portable** as it is tightly coupled with the hardware and platform.
- Some advantages of microkernel are:
  - It is **easy to maintain and debug** as each module can be modified or replaced independently.
  - It is **more secure and reliable** as any error in one module does not affect the other modules.
  - It is **more flexible and portable** as it can run on different hardware and platforms.
- Some disadvantages of microkernel are:
  - It provides fewer operating system functions than monolithic kernel.
  - It is **complex to design** as it requires careful communication and synchronization among modules.
  - It has **low performance** as there is more overhead of switching between user mode and kernel mode and passing messages among modules.



## Unit 2 - Concurrent Processes

- A concurrent process is a process that can execute simultaneously with other processes on the same or different systems.
- Concurrent processes can communicate and synchronize with each other using various methods, such as shared memory, message passing, semaphores, monitors, etc.
- Concurrent processes can be classified into two types: independent and cooperating.
  - Independent processes do not affect or be affected by the execution of other processes.
  - Cooperating processes can share data or resources with other processes or influence their behavior.
- Concurrent processes can be implemented using threads, which are lightweight processes that share the same address space and resources of a parent process.
- Concurrent processes can also be implemented using distributed systems, which are collections of independent computers that communicate over a network and appear as a single system to the user.
- Concurrent processes can improve the performance, reliability, and scalability of a system, but also introduce challenges such as deadlock, starvation, race conditions, etc.



### Process Concept

- A process is a program in execution which then forms the basis of all computation.
- A process is more than the program code as it includes the program counter, process stack, registers, program code etc.
- A process is defined as an entity which represents the basic unit of work to be implemented in the system.
- A process can be in one of the following states: new, ready, running, waiting, terminated.
- A process control block (PCB) is a data structure that contains the information about a process, such as its identifier, state, priority, program counter, memory allocation, etc.
- The operating system keeps its processes separate and allocates the resources they need, so that they are less likely to interfere with each other and cause system failures.
- The operating system may also provide mechanisms for inter-process communication to enable processes to interact in safe and predictable ways.
- The operating system involves in different CPU processing activities, such as process creation, process scheduling, process synchronization, process termination, etc.
- The operating system manages the processes by using various algorithms and data structures, such as queues, stacks, trees, etc.
- The operating system is a program that manages a computer’s resources, especially the allocation of those resources among other programs.



### Principle of Concurrency for the notes of the Unit 2 - Concurrent Processes in the subject of Operating System

- Concurrency in Operating System refers to the execution of several programs at the same time   .
- It takes place in OS when multiple processes or threads are executing in parallel   .
- It is the execution of processes to provide an impression of a synchronous computation.
- Concurrency can be achieved by using current technology such as multi-core processors and parallel processing, which allow multiple instructions to be executed simultaneously.
- Concurrency has some advantages and challenges in operating system design.
  - Advantages of concurrency:
    - It can improve the performance and efficiency of the system by utilizing the CPU and other resources effectively  .
    - It can enhance the responsiveness and interactivity of the system by allowing processes to run in the background while the user interacts with the foreground processes  .
    - It can support the modularity and structure of the system by allowing processes to be divided into smaller and independent units that can communicate with each other  .
  - Challenges of concurrency:
    - It can introduce complexity and difficulty in the system design and implementation, as the processes need to be coordinated and synchronized to avoid conflicts and errors  .
    - It can increase the overhead and cost of the system, as the processes need to share the limited resources and exchange the messages among them  .
    - It can cause unpredictability and non-determinism in the system behavior, as the processes may interfere with each other and produce different outcomes depending on the order and timing of their execution  .
- Principles of concurrency are the guidelines and rules that help to manage the concurrency in the operating system.
  - Some of the principles of concurrency are:
    - Mutual exclusion: It ensures that only one process can access a critical section or a shared resource at a time, and prevents the interference and inconsistency among the processes.
    - Deadlock: It is a situation where a set of processes are waiting for each other to release the resources that they hold, and none of them can proceed.
    - Starvation: It is a situation where a process is indefinitely delayed or denied from accessing a resource or a service that it needs.
    - Livelock: It is a situation where a set of processes are constantly changing their states in response to each other, but none of them can make any progress.
    - Synchronization: It is a mechanism that coordinates the execution and communication of the processes, and ensures the order and consistency of the system state.
    - Cooperation: It is a mechanism that allows the processes to share the information and resources, and achieve a common goal.



### Producer / Consumer Problem

- Producer / Consumer problem is a classical synchronization problem in the operating system   .
- It involves two types of processes: producers and consumers, that share a common buffer (or queue) of fixed size   .
- Producers produce data items and put them in the buffer, while consumers consume data items and remove them from the buffer   .
- The problem is to ensure that producers and consumers can access the buffer without causing data inconsistency or deadlock   .
- Some of the challenges in solving this problem are   :
  - The buffer has a limited capacity, so producers cannot put data items when the buffer is full, and consumers cannot remove data items when the buffer is empty   .
  - The buffer is a shared resource, so producers and consumers must synchronize their access to avoid race conditions   .
  - The producers and consumers may have different rates of production and consumption, so they must coordinate their activities to avoid starvation   .
- Some of the possible solutions for this problem are   :
  - Using semaphores to control the access to the buffer and the availability of data items and empty slots  .
  - Using monitors to encapsulate the buffer and the synchronization logic in a single abstract data type  .
  - Using message passing to communicate between producers and consumers without using a shared buffer  .
  - Using channels to connect producers and consumers with a queue that can buffer data items.



### Mutual Exclusion

- Mutual exclusion is a property of concurrency control, which is instituted for the purpose of preventing race conditions.
- Race conditions occur when two or more processes or threads access a shared resource concurrently, and the outcome depends on the order or timing of their execution.
- A shared resource can be a variable, a file, a device, or any other object that can be accessed by multiple processes or threads.
- Mutual exclusion ensures that only one process or thread can enter a critical section at a time, where a critical section is a piece of code that accesses a shared resource.
- Mutual exclusion can be implemented by using various techniques, such as locks, semaphores, monitors, or message passing.
- Mutual exclusion is required to ensure the correctness and consistency of the data and operations on the shared resource, and to avoid deadlock, starvation, or livelock .
- Mutual exclusion has some challenges, such as how to ensure fairness, how to avoid busy waiting, how to handle nested critical sections, and how to deal with failures or exceptions.



### Critical Section Problem

- The critical section problem is one of the classic problems in Operating Systems that arises when multiple processes or threads need to access shared resources simultaneously.
- The shared resources may be any resource in a computer like a memory location, data structure, CPU or any IO device.
- The critical section is the part of a program that tries to access the shared resources. The critical section cannot be executed by more than one process at the same time; operating system faces the difficulties in allowing and disallowing the processes to enter the critical section.
- The problem of synchronization occurs when the processes try to access the shared resources without any proper coordination or mutual exclusion. This may lead to data inconsistency, race condition, deadlock or starvation.
- The solution to the critical section problem is to ensure that only one process can enter the critical section at a time and the other processes have to wait until the critical section is free. This can be achieved by using various synchronization techniques such as locks, semaphores, monitors, etc.
- The solution to the critical section problem must satisfy the following requirements:
  - Mutual Exclusion: Only one process can enter the critical section at a time.
  - Progress: A process that is not in the critical section should not prevent other processes from entering the critical section.
  - Bounded Waiting: A process that is waiting to enter the critical section should get a chance to do so within a finite amount of time.
  - Fairness: The processes should be granted access to the critical section in a fair manner, without any bias or preference.



### Dekker's solution

- Dekker's solution is the first known correct solution to the mutual exclusion problem in concurrent programming .
- The mutual exclusion problem is the problem of ensuring that at most one process can enter a critical section (a section of code that accesses a shared resource) at a time .
- Dekker's solution allows two processes to share a single-use resource without conflict, using only shared memory for communication .
- Dekker's solution avoids the strict alternation of a naive turn-taking algorithm, and was one of the first mutual exclusion algorithms to be invented .
- Dekker's solution works as follows :
  - Each process has a boolean flag that indicates its intention to enter the critical section.
  - Each process also has a turn variable that indicates whose turn it is to enter the critical section.
  - Initially, both flags are false and the turn is arbitrary.
  - When a process wants to enter the critical section, it sets its flag to true and checks the other process's flag.
  - If the other process's flag is false, it means that the other process is not interested in the critical section, so the current process can enter it.
  - If the other process's flag is true, it means that the other process is also interested in the critical section, so the current process has to check the turn variable.
  - If the turn variable is equal to the current process's id, it means that the current process has priority to enter the critical section, so it can enter it.
  - If the turn variable is not equal to the current process's id, it means that the other process has priority to enter the critical section, so the current process has to wait until the turn variable changes or the other process's flag becomes false.
  - After exiting the critical section, the current process sets its flag to false and gives the turn to the other process.
- Dekker's solution guarantees mutual exclusion, progress, and bounded waiting .
  - Mutual exclusion: Only one process can enter the critical section at a time, because the flag and turn variables prevent both processes from entering it simultaneously.
  - Progress: If both processes want to enter the critical section, the turn variable decides which one can enter it first, and the other one has to wait until the turn variable changes or the flag variable becomes false. This ensures that no process is starved or blocked indefinitely.
  - Bounded waiting: There is a bound on the number of times that a process can be bypassed by another process before it can enter the critical section, because the turn variable alternates between the two processes after each exit from the critical section. This ensures that no process has to wait too long to enter the critical section.



### Peterson's solution for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Peterson's solution is a classic solution to the critical section problem, which ensures that no two processes change or modify a resource's value simultaneously .
- The critical section problem arises when multiple processes need to access a shared resource, such as a file, a printer, or a variable, and they may interfere with each other's operations.
- The solution requires two processes to cooperate by using two variables: a boolean array `flag` and an integer `turn`.
- The `flag` array indicates whether a process is ready to enter the critical section. The `turn` variable indicates whose turn it is to enter the critical section.
- The algorithm works as follows   :
  - Before entering the critical section, process `i` sets `flag[i]` to `true` and `turn` to the other process's number `j`.
  - Then, it checks if `flag[j]` is `true` and `turn` is `j`. If both conditions are true, it means that the other process is also ready and has priority, so process `i` waits until either `flag[j]` becomes `false` or `turn` becomes `i`.
  - After exiting the critical section, process `i` sets `flag[i]` to `false` to indicate that it is done with the resource.
- The algorithm satisfies the three requirements of mutual exclusion, progress, and bounded waiting   :
  - Mutual exclusion: Only one process can enter the critical section at a time, because the other process will be waiting in the while loop until the first process sets its `flag` to `false` or gives up its `turn`.
  - Progress: If both processes are ready to enter the critical section, the one whose `turn` it is will enter first. The other process will not block the first process from entering or exiting the critical section.
  - Bounded waiting: There is a bound on the number of times that a process can be bypassed by another process. The bound is one, because after a process gives up its `turn`, it will not give it up again until it enters and exits the critical section.
- The algorithm can be implemented in any programming language, and it can be used to solve other problems like the producer-consumer problem and reader-writer problem.
- The algorithm is limited to two processes and requires busy waiting, which wastes CPU cycles   .



### Semaphores for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- A semaphore is a variable or abstract data type used to control access to a common resource by multiple threads and avoid critical section problems in a concurrent system such as a multitasking operating system.
- A semaphore has two fields: a non-negative integer value S.V and a set of processes in a queue S.L.
- A semaphore can be initialized to any non-negative value, depending on the number of resources available.
- A semaphore supports two atomic operations: wait and signal, also known as P and V.
- The wait operation decrements the value of the semaphore if it is positive, or blocks the calling process until the value becomes positive and then decrements it.
- The signal operation increments the value of the semaphore and wakes up one of the blocked processes, if any, in the queue.
- There are two main types of semaphores: counting semaphores and binary semaphores.
- A counting semaphore can have any non-negative value and is used to represent the number of available resources or the number of empty slots in a buffer.
- A binary semaphore can have only two values: 0 or 1, and is used to implement mutual exclusion or locks.
- A binary semaphore is also called a mutex (short for mutual exclusion) semaphore.
- Semaphores have some advantages and disadvantages:
  - Advantages:
    - Semaphores allow only one process into the critical section and follow the mutual exclusion principle.
    - Semaphores are easy to implement and can be used for various synchronization problems.
    - Semaphores can be used to synchronize processes that do not share a common address space or memory.
  - Disadvantages:
    - Semaphores may cause busy waiting, which wastes CPU time and resources.
    - Semaphores may cause deadlock, starvation, or priority inversion, if not used carefully or correctly.
    - Semaphores are low-level primitives and require programmers to handle the details of synchronization logic.



### Test and Set Operation

- Test and set is a hardware instruction that is used to implement mutual exclusion in concurrent processes.
- Test and set operates on a shared variable, usually called a lock, that can have two values: 0 (unlocked) or 1 (locked).
- Test and set returns the old value of the lock and sets it to 1 atomically, meaning that no other process can access the lock until the current process releases it.
- A process can use test and set to acquire the lock by repeatedly calling it until it returns 0, indicating that the lock was previously unlocked and now it is locked by the caller.
- A process can use test and set to release the lock by simply setting it to 0, allowing other processes to acquire it.
- Test and set is a simple and effective way to achieve mutual exclusion, but it has some drawbacks, such as busy waiting, starvation, and priority inversion.



### Classical Problems in Concurrency

- Concurrency is the execution of multiple instruction sequences at the same time.
- It occurs in an operating system when multiple process threads are executing concurrently.
- These threads can interact with each other via shared memory or message passing.
- Concurrency results in resource sharing, which causes issues like deadlocks and resource scarcity.
- A problem in concurrent computing is where a process is continuously denied the resources it needs to complete its work.
- It could be caused by errors in scheduling or mutual exclusion algorithm, but resource leaks may also cause it.
- Sharing of global resources safely is difficult.
- If two processes both make use of a global variable and both make changes to the variables value, then the order in which various changes take place are executed is critical.
- Optimal allocation of resources is also a challenge in concurrency.
- There are some classical problems in concurrency that illustrate the challenges and solutions of concurrent programming.
- These problems are:
  - The producer/consumer problem: This problem is generalized in terms of the Producer-Consumer problem, where a finite buffer pool is used to exchange messages between producer and consumer processes.
  - The dining-philosophers problem: This problem is a model of concurrent processes that compete for a limited number of resources.
  - The readers and writers problem: This problem is a model of concurrent access to a shared data structure.
  - The sleeping barber problem: This problem is a model of a system that provides service to customers who arrive randomly.
- These problems can be solved using various synchronization mechanisms, such as semaphores, locks, monitors, etc.



### Dining Philosopher Problem

- The dining philosopher problem is a classic problem of synchronization in computer science, which illustrates the possibility of deadlocks and starvation in concurrent programs that access multiple shared resources .
- The problem was originally formulated by Edsger Dijkstra in 1965 as a student exam exercise, presented in terms of computers competing for access to tape drive peripherals.
- The problem can be described as follows: There are five philosophers sitting around a circular table, each with a plate of noodles in front of them. There are also five chopsticks on the table, one between each pair of adjacent philosophers    .
- The philosophers alternate between thinking and eating. To eat, a philosopher needs to pick up both chopsticks on his left and right. However, only one philosopher can hold a chopstick at a time. Therefore, a philosopher cannot eat if either of his neighbors is already eating    .
- The problem is to design a protocol that allows the philosophers to eat and think without causing any deadlock or starvation. A deadlock occurs when all philosophers are holding one chopstick and waiting for the other, thus no one can eat. A starvation occurs when a philosopher is unable to eat for an indefinite period of time, even though there is food available    .
- There are different ways of solving the problem, such as using semaphores, monitors, locks, or message passing. Some solutions may impose additional constraints, such as limiting the number of philosophers who can eat at the same time, or assigning priorities or ordering to the chopsticks    .
- The problem is a useful model for studying various synchronization issues and techniques in concurrent systems, such as deadlock detection and prevention, resource allocation, fairness, and deadlock freedom .



### Sleeping Barber Problem

- The sleeping barber problem is a classic inter-process communication and synchronization problem that illustrates the complexities that arise when there are multiple operating system processes .
- The problem is based on a hypothetical barber shop with one barber, one barber chair, and n chairs for waiting customers .
- The barber can either be sleeping or cutting hair. The customers can either be waiting or getting a haircut.
- The problem is to synchronize the barber and the customers using semaphores or other synchronization primitives, so that the following conditions are met  :
  - If there are no customers, the barber goes to sleep.
  - If a customer arrives when the barber is sleeping, the customer wakes up the barber and sits in the barber chair.
  - If a customer arrives when the barber is cutting hair, the customer either sits on one of the waiting chairs or leaves the shop if all chairs are occupied.
  - The barber must finish cutting hair before serving another customer.
  - The customer must leave the shop after getting a haircut.
- The sleeping barber problem can be generalized to have multiple barbers, multiple barber chairs, and a waiting room with a fixed number of chairs .
- The sleeping barber problem can be used to model various scenarios where a server process provides a service to multiple client processes in a concurrent and orderly manner .



### Inter Process Communication models and Schemes

Inter process communication (IPC) is a mechanism that allows processes to communicate with each other and synchronize their actions without sharing the same address space. IPC is useful for developing concurrent and distributed systems, where processes need to exchange data or coordinate their activities. There are different models and schemes of IPC, depending on the operating system and the application requirements. Some of the common models and schemes are:

- **Shared memory model**: In this model, processes access a common region of memory that is allocated by the operating system or by one of the processes. The processes can read and write data to the shared memory, and use synchronization primitives such as semaphores or locks to ensure consistency and avoid race conditions. Shared memory is fast and efficient, but it requires careful management of the memory space and the access rights. Shared memory is supported by POSIX systems and Windows operating systems .

- **Message passing model**: In this model, processes send and receive messages to each other through the operating system or a communication library. The messages can be fixed-size or variable-size, and can be exchanged synchronously or asynchronously. Message passing provides a higher level of abstraction and portability than shared memory, but it may incur more overhead and latency. Message passing is supported by most operating systems and distributed systems .

- **Buffering**: Buffering is a technique that is used in message passing systems to store the messages temporarily in a queue or a buffer. Buffering can be done by the sender, the receiver, or both, and it can be blocking or non-blocking. Buffering can improve the performance and reliability of message passing, but it also introduces complexity and memory consumption. Buffering can be implemented using pipes, sockets, or message queues .

- **Pipes**: Pipes are a form of buffering that allow one process to write data to another process in a sequential manner. Pipes can be named or unnamed, and can be unidirectional or bidirectional. Pipes are useful for implementing filters and pipelines, where the output of one process is the input of another process. Pipes are supported by most operating systems, such as UNIX, Linux, and Windows .

- **Sockets**: Sockets are a form of buffering that allow processes to communicate over a network using the TCP/IP protocol. Sockets can be stream-oriented or datagram-oriented, and can be connection-oriented or connectionless. Sockets are useful for implementing client-server and peer-to-peer applications, where the processes can be located on different machines. Sockets are supported by most operating systems and network libraries, such as Berkeley sockets and Winsock .

- **Semaphores**: Semaphores are a form of synchronization that allow processes to control access to shared resources, such as shared memory or files. Semaphores are integer variables that can be incremented or decremented atomically by the processes, and can be used to implement mutual exclusion or conditional synchronization. Semaphores can be binary or counting, and can be local or global. Semaphores are supported by most operating systems and concurrency libraries, such as POSIX and Java .



### Process generation for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system

- Process generation is the process of creating a new process in an operating system by allocating memory, assigning a process identifier, and initializing the process control block.
- A process is a basic unit of work that executes a program or a part of a program in the system.
- A process can create one or more child processes using system calls such as fork() or exec() in UNIX/Linux systems.
- A process can also terminate itself or another process using system calls such as exit() or kill() in UNIX/Linux systems.
- A process can communicate with other processes using inter-process communication methods such as pipes, message queues, shared memory, semaphores, etc.
- A process can also synchronize with other processes using mutual exclusion, critical sections, locks, monitors, etc.
- A process can be in one of the following states: new, ready, running, waiting, or terminated.
- A process can change its state due to events such as CPU scheduling, I/O completion, interrupts, signals, etc.
- A process can be classified into two types: independent and cooperative.
- An independent process does not affect or get affected by other processes in the system.
- A cooperative process can affect or get affected by other processes in the system, and may share data or resources with them.
- A process can also be classified into two types: foreground and background.
- A foreground process interacts with the user through a terminal or a graphical user interface.
- A background process does not interact with the user and runs in the background, such as a daemon or a service.



## Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
  - In preemptive scheduling, the CPU can be taken away from a running process by the scheduler if a higher priority process arrives or a time quantum expires .
  - In non-preemptive scheduling, the CPU cannot be taken away from a running process until it completes or requests for I/O or terminates .
- Some of the common CPU scheduling algorithms are :
  - First Come First Serve (FCFS): The process that arrives first in the ready queue is selected for execution. It is simple, but may cause long waiting time and low CPU utilization .
  - Shortest Job First (SJF): The process that has the shortest burst time (estimated execution time) in the ready queue is selected for execution. It minimizes the average waiting time, but may cause starvation for longer processes .
  - Priority Scheduling: The process that has the highest priority in the ready queue is selected for execution. It can be preemptive or non-preemptive. It may cause starvation for lower priority processes .
  - Round Robin (RR): The processes in the ready queue are executed in a circular order, with each process getting a fixed time slice (quantum) of CPU. It is fair and responsive, but may cause high context switching overhead and low CPU utilization .
  - Multilevel Queue (MLQ): The processes are divided into different queues based on their characteristics, such as foreground/background, system/user, CPU-bound/I/O-bound, etc. Each queue has its own scheduling algorithm and priority. It allows better process management, but may cause starvation for lower priority queues .
  - Multilevel Feedback Queue (MLFQ): The processes are divided into different queues based on their characteristics, but they can move between the queues based on their behavior, such as CPU usage, waiting time, etc. It allows better process adaptation, but may cause complexity and overhead .



### Scheduling Concepts

- Scheduling is the process of selecting a process from a ready queue and allotting CPU to this process for execution.
- Scheduling aims to maximize the CPU utilization and minimize the waiting time, response time, and turnaround time of the processes.
- Scheduling is carried out by a part of the operating system called the scheduler.
- There are different types of schedulers, such as long-term, short-term, and medium-term schedulers, that perform different functions.
- Long-term scheduler decides which processes to admit into the system and controls the degree of multiprogramming.
- Short-term scheduler decides which process to run next and performs context switching.
- Medium-term scheduler decides which processes to swap out or swap in from the main memory and controls the degree of swapping.
- There are different types of scheduling algorithms, such as first come first serve, shortest job first, priority, round robin, and multilevel queue, that use different criteria to select the next process.
- Scheduling algorithms can be classified into two categories: preemptive and non-preemptive.
- Preemptive algorithms can interrupt the execution of a process and switch to another process, while non-preemptive algorithms can only switch to another process after the current process finishes or blocks.
- Scheduling algorithms can be evaluated based on various parameters, such as throughput, CPU utilization, turnaround time, waiting time, response time, and fairness.
- Scheduling algorithms can be designed for different types of systems, such as batch, interactive, and real-time systems, that have different requirements and constraints.



### Performance Criteria for CPU Scheduling

- CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it for execution.
- CPU scheduling aims to maximize the utilization of the CPU and the throughput of the system, while minimizing the turnaround time, waiting time, and response time of the processes.
- The performance criteria for CPU scheduling are as follows  :

  - **CPU utilization**: The percentage of time the CPU is busy executing processes. The higher the CPU utilization, the better the performance of the system. CPU utilization can range from 0% to 100%, but in a real system, it varies from 40% to 90% depending on the load on the system.
  - **Throughput**: The number of processes that complete their execution per unit of time. The higher the throughput, the more work is done by the system. Throughput can vary depending on the length and type of the processes.
  - **Turnaround time**: The amount of time it takes for a process to finish its execution, from the time it is submitted to the system until the time it is terminated. The turnaround time includes the waiting time, the CPU time, and the I/O time of the process. The lower the turnaround time, the faster the process is completed.
  - **Waiting time**: The amount of time a process spends in the ready queue, waiting for its turn to use the CPU. The waiting time does not include the I/O time or the CPU time of the process. The lower the waiting time, the less the process is delayed.
  - **Response time**: The amount of time it takes for a process to start its execution, from the time it is submitted to the system until the time it gets the first response from the CPU. The response time is important for interactive processes that require immediate feedback from the system. The lower the response time, the more responsive the system is.

- Different CPU scheduling algorithms may have different performance criteria, depending on the objectives and requirements of the system. For example, a real-time system may prioritize the response time and the deadline of the processes, while a batch system may prioritize the throughput and the CPU utilization of the system.



### Process States

- A process is a program in execution that requires resources such as CPU, memory, disk, and I/O devices.
- A process state is a condition of the process at a specific instant of time.
- Every process is represented in the operating system by a process control block (PCB), which contains information such as process ID, priority, CPU registers, memory pointers, etc.
- A process can be in one of the following states:

  - **New**: The process is being created but not yet loaded into the main memory. It is the program that is present in the secondary memory that will be picked up by the OS to create the process .
  - **Ready**: The process is loaded into the main memory and is waiting for the CPU to be allocated. It is placed in the ready queue, which is a data structure that holds all the ready processes .
  - **Running**: The process is chosen for execution and is running on one of the CPUs or cores of the system. There can be at most one running process per CPU or core. A process can run in either user mode or kernel mode, depending on the type of instructions it is executing .
  - **Waiting**: The process is waiting for some event to occur, such as an I/O operation, a signal, or a resource availability. It is placed in the waiting queue, which is a data structure that holds all the waiting processes .
  - **Terminated**: The process has completed its execution and is removed from the system. The OS releases the resources allocated to the process and updates the PCB .

- A process can change its state due to various events, such as CPU scheduling, I/O interrupts, signals, system calls, etc. The following diagram shows the possible state transitions of a process :

Process State Diagram

- Different operating systems may have different names or additional states for the processes, such as suspended, zombie, or blocked. However, the basic states and transitions are similar in most operating systems.



### Process Transition Diagram for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU.
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- A process is an instance of a program in execution. A process can have one of the following states :
  - **New**: The process is being created.
  - **Ready**: The process is waiting to be assigned to a CPU.
  - **Running**: The process is executing on a CPU.
  - **Waiting**: The process is waiting for some event to occur, such as an I/O completion.
  - **Terminated**: The process has finished execution.
- A process state transition diagram shows how a process changes states in response to certain events . The following diagram is an example of a process state transition diagram:

Process state transition diagram

- The arrows show how the process changes states. A process is running if the process is assigned to a CPU. A process can be preempted by the CPU scheduler if another process has higher priority or if the current process has used up its allocated time slice. A process can be blocked by the operating system if it requests an I/O operation or a resource that is not available. A process can be unblocked by the operating system if the event or resource it was waiting for becomes available. A process can be terminated by the operating system if it completes its execution or if it encounters an error.
- The process state transition diagram is useful for understanding the behavior and performance of the CPU scheduler, which is responsible for selecting the next process to run on the CPU.
- The process state transition diagram is also related to the process control block (PCB), which is a data structure that contains information about a process, such as its state, priority, CPU registers, memory allocation, I/O status, etc. The PCB is updated by the operating system whenever a process changes state. The PCB is also used by the CPU scheduler to select the next process to run on the CPU.
- The process state transition diagram can vary depending on the type of CPU scheduling algorithm used by the operating system, such as first-come first-served (FCFS), shortest job first (SJF), priority, round robin, etc. Different CPU scheduling algorithms have different criteria and objectives for selecting the next process to run on the CPU, such as minimizing waiting time, maximizing CPU utilization, ensuring fairness, etc. The process state transition diagram can help to analyze and compare the advantages and disadvantages of different CPU scheduling algorithms.



### Schedulers for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- Schedulers are operating system modules that select the next jobs to be admitted into the system and the next process to run on the CPU.
- Schedulers are required to maintain the multi-tasking capabilities of a computer and to keep its performance at the highest level by scheduling the process according to their preferences and need.
- There are three types of schedulers in operating system:
  - Long-term scheduler: Also known as an admission scheduler or high-level scheduler, it decides which jobs or programs are admitted to the system for processing. It controls the degree of multiprogramming, i.e., the number of processes in memory. It runs infrequently and may involve I/O or memory allocation.
  - Mid-term scheduler: Also known as a medium-term scheduler, it decides which processes are swapped out of memory to the disk and which are swapped in from the disk to the memory. It is used to improve the process mix and memory utilization. It runs less frequently than the short-term scheduler and may involve I/O or memory allocation.
  - Short-term scheduler: Also known as a CPU scheduler or low-level scheduler, it decides which process runs on the CPU at a certain point in time. It runs frequently and may involve context switching. It can be either preemptive or cooperative, depending on whether it can pause a running process or not.
- The process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process on the basis of a particular strategy.
- The process scheduling can be done using various algorithms, such as first-come first-served (FCFS), shortest job first (SJF), priority, round robin, multilevel queue, multilevel feedback queue, etc.
- The process scheduling algorithms are evaluated based on various criteria, such as CPU utilization, throughput, turnaround time, waiting time, response time, etc.



### Process Control Block (PCB)

- A process control block (PCB) is a data structure used by computer operating systems to store all the information about a process.
- A PCB is also known as a process descriptor or a task control block (TCB) .
- A PCB is created by the operating system when a process is initialized or installed .
- A PCB gives identity to each process so that the operating system can easily distinguish between processes.
- A PCB stores the register content or the execution context of the processor when the process is blocked from running.
- A PCB enables the operating system to restore a process's execution context when the process returns to the running state.
- A PCB typically contains the following components  :
  - Process ID: A unique identifier for the process.
  - Process state: The current status of the process, such as ready, running, waiting, etc.
  - Program counter: The address of the next instruction to be executed by the process.
  - CPU registers: The values of the general-purpose registers, stack pointer, etc.
  - CPU scheduling information: The priority, burst time, queue number, etc. of the process for scheduling purposes.
  - Memory management information: The base and limit registers, page tables, segment tables, etc. of the process for memory allocation and protection.
  - Accounting information: The CPU time, system time, IO time, etc. of the process for performance monitoring and billing.
  - IO status information: The list of IO devices, files, sockets, etc. allocated to the process for input and output operations.
- A PCB is usually stored in a process table, which is an array of PCBs indexed by the process ID.
- A PCB is updated by the operating system whenever there is a change in the process state or the execution context.
- A PCB is deleted by the operating system when the process terminates or exits.



### Process address space

- Process address space is the set of logical addresses that a process references in its code .
- Logical addresses are generated by the CPU during the execution of a process and are translated into physical addresses by the memory management unit (MMU)  .
- The process address space consists of different segments, such as code segment, data segment, stack segment, and heap segment   .
- Code segment contains the executable instructions of the process   .
- Data segment contains the global and static variables of the process   .
- Stack segment contains the local variables and function parameters of the process   .
- Heap segment contains the dynamically allocated memory of the process   .
- The size and layout of the process address space may vary depending on the operating system, the hardware architecture, and the memory management scheme     .
- For example, when 32-bit addressing is in use, addresses can range from 0 to 0x7fffffff; that is, 2^31 possible numbers, for a total theoretical size of 2 gigabytes  .
- However, the actual size of the process address space may be limited by the available physical memory, the virtual memory, and the system reserved space   .
- The operating system is responsible for managing the process address space and ensuring that each process has a separate and protected address space    .
- The operating system also provides mechanisms for sharing memory between processes, such as memory mapping, shared libraries, and interprocess communication    .



### Process identification information

- Process identification information is a part of the process control block (PCB), which is a data structure used by the operating system to store all the information about a process.
- Process identification information includes a unique number called the process identifier (PID), which is assigned by the operating system to each process when it is created .
- The PID is used by the operating system to identify and manage the process, such as allocating resources, scheduling, terminating, etc .
- The PID is also used by other processes or programs to communicate with the process, such as sending signals, debugging, etc .
- The PID is usually an integer that ranges from 0 to a maximum value depending on the operating system. For example, in Linux, the PID can be up to 32768, while in Windows, it can be up to 65535.
- The PID is not a permanent identifier, as it can be reused by the operating system after the process terminates. Therefore, the PID only identifies a process during its lifetime .
- The PID is usually stored in a process table, which is a data structure that contains an entry for each active process in the system. The process table is maintained by the operating system and can be accessed by system calls or commands.



### Threads and their management

- A thread is a single sequence stream within a process. It is a lightweight process that the operating system can schedule and run concurrently with other threads.
- Threads share the same data and code as the process that created them, so they have low operational cost and fast communication.
- Threads can be used to improve the performance, responsiveness and parallelism of a program or an operating system.
- There are two major types of threads in operating systems: user threads and kernel threads .
  - User threads are created and managed by user-level libraries, such as POSIX threads (pthreads) or Java threads. They are not visible to the kernel and do not require system calls to switch between them. They have more flexibility and portability, but less efficiency and support from the kernel .
  - Kernel threads are created and managed by the kernel, such as Windows threads or Linux threads. They are visible to the kernel and require system calls to switch between them. They have less flexibility and portability, but more efficiency and support from the kernel .
- There are different ways of mapping user threads to kernel threads, such as one-to-one, many-to-one, many-to-many or hybrid.
  - One-to-one mapping means each user thread is mapped to a kernel thread. This allows concurrency and parallelism, but also increases the overhead and the number of kernel threads.
  - Many-to-one mapping means many user threads are mapped to a single kernel thread. This reduces the overhead and the number of kernel threads, but also limits the concurrency and parallelism. If one user thread blocks, the whole process blocks.
  - Many-to-many mapping means many user threads are mapped to many kernel threads. This allows concurrency and parallelism, and also balances the overhead and the number of kernel threads. The kernel can assign user threads to available kernel threads dynamically.
  - Hybrid mapping means many user threads are mapped to many kernel threads, but also allows multiple user threads to be mapped to a single kernel thread. This combines the advantages of many-to-one and many-to-many mappings, and also allows user-level thread management.
- Threads can be in different states, such as new, ready, running, waiting, terminated or suspended .
  - New state means the thread is created but not yet ready to run.
  - Ready state means the thread is ready to run and waiting for the CPU to be assigned.
  - Running state means the thread is running on the CPU.
  - Waiting state means the thread is waiting for some event or resource to resume running.
  - Terminated state means the thread has completed its execution and is no longer active.
  - Suspended state means the thread is temporarily stopped by the user or the system and can be resumed later.
- Threads can be managed by the operating system using various techniques, such as thread scheduling, thread synchronization, thread communication and thread termination .
  - Thread scheduling is the process of selecting a thread from the ready queue and assigning it to the CPU. The operating system can use different scheduling algorithms, such as round-robin, priority-based, shortest job first, etc .
  - Thread synchronization is the process of coordinating the execution of multiple threads that share data or resources. The operating system can use different synchronization mechanisms, such as locks, semaphores, monitors, condition variables, etc .
  - Thread communication is the process of exchanging data or messages between threads. The operating system can use different communication methods, such as shared memory, message passing, signals, pipes, sockets, etc .
  - Thread termination is the process of ending the execution of a thread and releasing its resources. The operating system can use different termination methods, such as explicit termination, implicit termination, cancellation, etc .



### Scheduling Algorithms

Scheduling algorithms are the algorithms that determine how the CPU allocates its time to the processes that are ready to execute. Scheduling algorithms can be classified into two types: preemptive and non-preemptive.

- Preemptive scheduling algorithms allow the CPU to interrupt the execution of a process and switch to another process, based on some criteria. This can improve the responsiveness and fairness of the system, but also introduce overhead and complexity.
- Non-preemptive scheduling algorithms do not interrupt the execution of a process until it completes or requests an I/O operation. This can reduce the overhead and complexity of the system, but also cause starvation and poor utilization of the CPU.

Some of the common scheduling algorithms are:

- First-Come, First-Served (FCFS) Scheduling: This is the simplest scheduling algorithm that assigns the CPU to the process that arrives first in the ready queue. This algorithm is non-preemptive and easy to implement, but it can cause long waiting times and low CPU utilization.
- Shortest-Job-Next (SJN) Scheduling: This is a non-preemptive scheduling algorithm that assigns the CPU to the process that has the shortest estimated burst time (the time required to complete the process). This algorithm can minimize the average waiting time and turnaround time, but it requires the knowledge of the burst time of each process, which is not always possible or accurate.
- Priority Scheduling: This is a scheduling algorithm that assigns the CPU to the process that has the highest priority. The priority can be static (assigned by the system or the user) or dynamic (based on some factors such as age, I/O requirements, etc.). This algorithm can be preemptive or non-preemptive, depending on whether the CPU can be taken away from a lower-priority process by a higher-priority process. This algorithm can improve the importance and urgency of the processes, but it can also cause starvation and indefinite blocking of the lower-priority processes.
- Shortest Remaining Time (SRT) Scheduling: This is a preemptive version of the SJN scheduling algorithm that assigns the CPU to the process that has the shortest remaining burst time (the time required to complete the process after subtracting the time already executed). This algorithm can minimize the average waiting time and turnaround time, but it also requires the knowledge of the burst time of each process, which is not always possible or accurate. It also introduces more context switches and overhead than the SJN algorithm.
- Round Robin (RR) Scheduling: This is a preemptive scheduling algorithm that assigns the CPU to the processes in the ready queue in a circular order, for a fixed time quantum (or slice). If a process does not finish within the time quantum, it is preempted and moved to the end of the queue. This algorithm is fair and simple to implement, but it can cause high context switches and overhead, and it depends on the choice of the time quantum.
- Multiple-Level Queues Scheduling: This is a scheduling algorithm that divides the processes into different categories or classes, based on some criteria such as memory size, CPU usage, I/O requirements, etc. Each class has its own queue and its own scheduling algorithm. The CPU is assigned to the processes from the different queues according to some predefined rules. This algorithm can improve the performance and flexibility of the system, but it also requires more data structures and complexity.



### Multiprocessor Scheduling

- Multiprocessor scheduling is the process of allocating CPU resources to multiple processes or threads that run on multiple processors or cores in a system.
- Multiprocessor scheduling aims to achieve high performance, load balancing, fairness, and responsiveness for the system and the processes.
- Multiprocessor scheduling is more complex than single processor scheduling because of the following challenges:
  - Interprocessor communication and synchronization: Processes or threads that run on different processors may need to communicate or synchronize with each other, which may incur overhead and delay.
  - Processor affinity: Processes or threads may have a preference or affinity for a certain processor or core, based on the locality of data or code. Moving a process or thread from one processor to another may cause cache misses and performance degradation.
  - Load balancing: The workload of the system may vary over time and across processors. A good multiprocessor scheduler should distribute the load evenly among the processors to avoid idle or overloaded processors.
  - Scalability: The multiprocessor scheduler should be able to handle a large number of processors and processes or threads without compromising efficiency or fairness.

- There are two main approaches to multiprocessor scheduling in the operating system: symmetric multiprocessing and asymmetric multiprocessing.
  - Symmetric multiprocessing (SMP): In SMP, each processor is self-scheduling and has equal access to the system resources. All processes or threads may be in a common ready queue, or each processor may have its own private queue. The advantages of SMP are simplicity, flexibility, and scalability. The disadvantages are contention, overhead, and lack of processor affinity.
  - Asymmetric multiprocessing (AMP): In AMP, one processor is designated as the master processor and is responsible for scheduling the other processors, which are called slave processors. The master processor may have its own workload or may be dedicated to scheduling. The advantages of AMP are reduced contention, improved processor affinity, and better control. The disadvantages are complexity, bottleneck, and lack of scalability.

- There are several different algorithms and techniques that have been studied and implemented for multiprocessor scheduling, such as:
  - Gang scheduling: Gang scheduling is a technique that schedules a group of related processes or threads (called a gang) to run simultaneously on a set of processors. The idea is to preserve the communication and synchronization patterns of the gang and to reduce the context switching overhead. Gang scheduling requires global coordination and synchronization among the processors.
  - Processor sharing: Processor sharing is a technique that allows multiple processes or threads to share a processor by dividing its time into small slices. The idea is to provide fairness and responsiveness for the processes or threads and to utilize the processor efficiently. Processor sharing requires local scheduling and preemption on each processor.
  - Work stealing: Work stealing is a technique that allows a processor to steal a process or thread from another processor's queue when it becomes idle. The idea is to balance the load among the processors and to exploit the processor affinity of the processes or threads. Work stealing requires local scheduling and communication among the processors.



### Deadlock

- A deadlock is a situation in which one or more processes are unable to proceed because they are waiting for some resources that are held by other waiting processes .
- Deadlocks can occur in operating systems that allow multiple processes to share resources such as CPU, memory, disk, printer, etc .
- Deadlocks can cause performance degradation, system failure, or user frustration.
- To prevent or avoid deadlocks, the operating system must ensure that at least one of the four necessary conditions for deadlock does not hold:
  - Mutual exclusion: A resource can be assigned to only one process at a time.
  - Hold and wait: A process holding some resources can request additional resources and wait for them.
  - No preemption: A resource cannot be forcibly taken away from a process that is holding it.
  - Circular wait: A set of processes are waiting for resources in a circular chain, such that each process is holding a resource that the next process in the chain needs.
- The operating system can use different strategies to deal with deadlocks, such as:
  - Deadlock prevention: Ensure that at least one of the four necessary conditions does not hold by imposing some constraints on how processes can request and release resources.
  - Deadlock avoidance: Allow the four necessary conditions to hold but dynamically check whether a resource allocation will lead to a deadlock using some algorithms such as Banker's algorithm or resource allocation graph.
  - Deadlock detection and recovery: Allow deadlocks to occur but periodically detect them using some algorithms such as wait-for graph or matrix and then recover from them by terminating or rolling back some processes or preempting some resources.
  - Deadlock ignorance: Do not attempt to prevent, avoid, detect, or recover from deadlocks and assume that they will never occur or are rare enough to be ignored. This is the approach used by most modern operating systems such as Windows and Linux.



### System model for CPU scheduling

- CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it for execution .
- CPU scheduling aims to maximize the utilization of the CPU, the throughput of the system, and the fairness among the processes .
- CPU scheduling can be classified into two types: preemptive and non-preemptive.
  - Preemptive scheduling allows the CPU to be taken away from a running process when a higher priority process arrives or a time quantum expires.
  - Non-preemptive scheduling does not interrupt a running process until it finishes or requests I/O.
- CPU scheduling can also be classified into four levels: long-term, medium-term, short-term, and dispatcher.
  - Long-term scheduling decides which processes are admitted to the system for execution.
  - Medium-term scheduling decides which processes are swapped in or out of the main memory.
  - Short-term scheduling decides which process is selected from the ready queue for the CPU.
  - Dispatcher is the module that switches the context from the current process to the next process.
- CPU scheduling can be performed on different types of resources, such as single processor, multiple processors, or multiple cores .
  - Single processor scheduling assigns one process to the CPU at a time.
  - Multiple processor scheduling assigns processes to more than one CPU simultaneously.
  - Multiple core scheduling assigns processes to different cores within a single CPU.



### Deadlock characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock can be characterized by four necessary conditions:
  - Mutual exclusion: At least one resource must be held in a non-sharable mode, that is, only one process can use the resource at a time.
  - Hold and wait: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.
  - No preemption: A resource can be released only voluntarily by the process holding it, after the process has completed its task.
  - Circular wait: A set of processes must exist such that each process is waiting for a resource that is held by another process in the set, which in turn is waiting for another resource, and so on, forming a circular chain.
- These conditions are necessary but not sufficient for a deadlock to occur, that is, if a system does not satisfy any one of these conditions, then a deadlock cannot occur. However, satisfying these conditions does not guarantee that a deadlock will occur, as it depends on the order and timing of requests and releases of resources.



### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is the process of deciding which process will own the CPU to use while another process is suspended.
- CPU scheduling algorithms are the methods of choosing the next process to run on the CPU based on some criteria, such as priority, burst time, arrival time, etc.
- CPU scheduling algorithms can be classified into two modes: pre-emptive and non-pre-emptive.
  - Pre-emptive scheduling allows the CPU to switch from one process to another before the current process finishes its execution.
  - Non-pre-emptive scheduling does not allow the CPU to switch from one process to another until the current process finishes its execution.
- CPU scheduling algorithms can face some challenges, such as starvation, aging, and deadlock  .
  - Starvation is a phenomenon in which a low-priority process can wait indefinitely for the CPU because of a steady stream of higher-priority processes .
  - Aging is a technique to prevent starvation by gradually increasing the priority of a waiting process over time .
  - Deadlock is a situation in which a set of processes are blocked because each process is holding a resource and waiting for another resource held by another process.
- CPU scheduling algorithms can prevent these challenges by following some principles, such as:
  - Eliminating mutual exclusion, which means allowing multiple processes to share the same resource at the same time.
  - Eliminating hold and wait, which means requiring a process to request all the resources it needs at once and releasing them when done.
  - Eliminating circular wait, which means imposing a total order on the resources and requiring a process to request them in that order.
  - Eliminating no preemption, which means allowing the system to take away a resource from a process if another process needs it more urgently.



### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- Avoidance and detection are two strategies to deal with the problem of deadlock in operating systems.
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Avoidance is a proactive approach that prevents deadlock from occurring by ensuring that the system is always in a safe state.
- Detection is a reactive approach that detects deadlock after it has occurred and then takes some action to recover from it.
- Some of the points to remember about avoidance and detection are:

  - Avoidance requires prior knowledge of the maximum resource requirements of each process, whereas detection does not.
  - Avoidance uses the concept of a safe state, which is a state where there is at least one sequence of resource allocation that does not lead to deadlock. Detection uses the concept of a wait-for graph, which is a graph that shows the dependencies among the processes and the resources they are holding or requesting.
  - Avoidance uses algorithms such as the banker's algorithm, which simulates the allocation and request of resources and checks if the system remains in a safe state. Detection uses algorithms such as the resource allocation graph algorithm, which checks for cycles in the wait-for graph and identifies the processes involved in the deadlock.
  - Avoidance may incur more overhead and reduce system utilization, as it may deny some requests that are actually safe. Detection may incur more delay and waste of resources, as it may allow some requests that are actually unsafe.
  - Avoidance is more suitable for systems where the resource requirements are known in advance and the number of processes and resources is fixed. Detection is more suitable for systems where the resource requirements are dynamic and unpredictable and the number of processes and resources is variable.



### Recovery from deadlock

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- If a system does not use a deadlock prevention or avoidance technique, there is a possibility that a deadlock will occur.
- In order to recover from a deadlock, the operating system must detect and resolve it using some methods.
- There are two main approaches for deadlock recovery: process termination and resource preemption.

#### Process termination

- To eliminate the deadlock, we can simply kill one or more processes involved in the deadlock.
- For this, we use two methods:

  - Abort all the deadlocked processes: This method will certainly break the deadlock, but at a great expense. The processes may have done some useful work before entering the deadlock, and aborting them will lose that work. Also, this method may not be feasible if the processes are critical or interactive.
  - Abort one process at a time until the deadlock cycle is eliminated: This method is more selective and tries to minimize the cost of aborting processes. However, it requires some criteria to choose which process to abort, such as the priority, the amount of resources and time consumed, the number of resources the process needs to finish, etc. Also, this method may not work if a deadlock occurs again after aborting a process.

#### Resource preemption

- To eliminate the deadlock, we can preempt some resources from the processes involved in the deadlock and allocate them to other processes.
- For this, we use three methods:

  - Preempt resources and rollback: This method takes away some resources from a process and restarts it from some previous checkpoint. The process may lose some work, but not as much as aborting it. However, this method requires the system to have a mechanism for checkpointing and rollback, and it may cause starvation if the same process is always preempted.
  - Preempt resources and restart: This method takes away some resources from a process and restarts it from the beginning. The process will lose all its work, but it may be simpler than rollback. However, this method may also cause starvation if the same process is always preempted.
  - Preempt resources and wait: This method takes away some resources from a process and puts it in a waiting state until it can regain its resources. The process will not lose any work, but it may increase the waiting time and the system overhead. Also, this method may not work if a deadlock occurs again after preempting a resource.



## Unit 4 - Memory Management

- Memory management is the process of allocating and deallocating memory to programs and processes in a computer system.
- Memory management can be divided into two levels: hardware level and software level.
- Hardware level memory management involves the physical organization and operation of the memory hardware, such as registers, cache, main memory, and secondary memory.
- Software level memory management involves the logical organization and manipulation of the memory space, such as address translation, memory allocation, memory protection, memory sharing, and memory mapping.
- Memory management can also be classified into two schemes: static memory management and dynamic memory management.
- Static memory management is the allocation of memory at compile time or load time, and the memory remains fixed throughout the program execution. Static memory management is simple and fast, but it can waste memory and limit the flexibility of the program.
- Dynamic memory management is the allocation of memory at run time, and the memory can be changed during the program execution. Dynamic memory management is more complex and slower, but it can save memory and allow the program to adapt to different situations.
- Memory management can also be categorized into two techniques: contiguous memory allocation and non-contiguous memory allocation.
- Contiguous memory allocation is the allocation of memory in a single continuous block of memory. Contiguous memory allocation is easy to implement and efficient, but it can cause external fragmentation and relocation problems.
- Non-contiguous memory allocation is the allocation of memory in multiple non-continuous blocks of memory. Non-contiguous memory allocation is harder to implement and less efficient, but it can avoid external fragmentation and relocation problems.
- Memory management can also be implemented using different methods, such as paging, segmentation, virtual memory, and memory mapping. Each method has its own advantages and disadvantages, and they can be combined to achieve better performance and functionality.



### Basic Bare Machine

- A basic bare machine is a computer that executes instructions directly on the hardware without any operating system or intermediary software .
- A basic bare machine can be used to run programs that have low-level access to the hardware and have time-critical latency requirements, such as embedded systems and firmware.
- A basic bare machine does not provide any services or abstractions to the programs, such as memory management, process management, file system, device drivers, etc. The programs have to manage these aspects by themselves.
- A basic bare machine can be considered as a precursor to modern operating systems, which evolved through various stages to provide more functionality and convenience to the users and applications.
- A basic bare machine can be programmed using assembly language or low-level languages that can generate machine code, such as C or C++.
- A basic bare machine can be booted by using a bootloader, which is a small program that loads the main program from a storage device into the memory and transfers the control to it.



### Resident monitor

- A resident monitor is a type of system software program that was used in many early computers from the 1950s to 1970s  .
- It can be considered a precursor to the operating system  .
- The name is derived from a program which is always present in the computer's memory, thus being "resident"  .
- The resident monitor's main functions were to quickly load the next task to be executed in a batch environment, to control the instructions and perform all necessary functions, and to sequence and schedule the jobs and load them into the main memory according to their order.
- The resident monitor was usually stored in a read-only memory (ROM) or a read-write memory (RWM) that was protected from user programs .
- The resident monitor was also responsible for handling interrupts, errors, and input/output operations .
- The resident monitor was often supplemented by a transient monitor, which was a program that was loaded into the memory along with the user program and provided additional services or functions .



### Multiprogramming with fixed partitions

- Multiprogramming is a technique that allows multiple processes to execute simultaneously in the main memory .
- Fixed partitions are non-overlapping regions of the main memory that have a fixed size and location .
- The number of fixed partitions is determined at system startup and does not change during execution.
- Each partition can hold one process at a time, and the process must fit entirely within the partition .
- The advantages of multiprogramming with fixed partitions are:
  - It is simple and easy to implement .
  - It avoids external fragmentation, as there are no gaps between partitions .
- The disadvantages of multiprogramming with fixed partitions are:
  - It suffers from internal fragmentation, as the unused space within a partition is wasted .
  - It may not utilize the memory efficiently, as some partitions may be too large or too small for some processes .
  - It limits the degree of multiprogramming, as the number of partitions is fixed and may not match the number of ready processes .
  - It requires the processes to be relocatable or position-independent, as they may be loaded into different partitions at different times .



### Multiprogramming with variable partitions

- Multiprogramming with variable partitions is a contiguous memory management technique in which the main memory is not divided into fixed-sized partitions, but rather into variable-sized chunks of free memory that can fit the processes according to their size and memory requirements  .
- The advantages of this technique are:
  - It eliminates internal fragmentation, as the processes are allocated exactly the amount of memory they need .
  - It improves the degree of multiprogramming, as more processes can be loaded into the main memory at the same time .
- The disadvantages of this technique are:
  - It causes external fragmentation, as the free memory space becomes scattered and non-contiguous over time, making it difficult to find a large enough chunk of memory for a new process .
  - It requires dynamic memory allocation and deallocation, which adds overhead and complexity to the memory management system .
- To overcome the problem of external fragmentation, some techniques are used, such as:
  - Compaction, which involves moving the processes in memory to make the free space contiguous . This technique is costly and time-consuming, as it requires shifting the processes and updating their addresses .
  - Memory allocation algorithms, which try to optimize the placement of processes in memory and reduce the amount of wasted space . Some examples of these algorithms are:
    - First fit, which allocates the first chunk of free memory that is large enough for the process . This technique is fast and simple, but it tends to leave large holes at the beginning of the memory .
    - Best fit, which allocates the smallest chunk of free memory that is large enough for the process . This technique tries to minimize the external fragmentation, but it is slow and complex, as it requires searching the entire memory for the best fit .
    - Worst fit, which allocates the largest chunk of free memory that is available . This technique tries to create large holes for future processes, but it may increase the external fragmentation, as it leaves small holes that are unusable .
    - Next fit, which allocates the next chunk of free memory that is large enough for the process, starting from the last allocated chunk . This technique is similar to first fit, but it avoids scanning the memory from the beginning every time .
- Multiprogramming with variable partitions is also known as multiprogramming with dynamic partitions or multiprogramming with variable tasks (MVT) . It is contrasted with multiprogramming with fixed partitions or multiprogramming with fixed tasks (MFT), which divides the main memory into fixed-sized partitions that may not match the size of the processes, causing internal fragmentation .



### Protection schemes for the notes of the Unit 4 - Memory Management in the subject of Operating system

- Memory protection is an important concept in operating system that prevents a process from accessing unallocated memory or memory that belongs to another process or the kernel .
- Memory protection is required to protect the operating system from user processes and to ensure the correct functioning of the programs.
- Memory protection can be implemented by using hardware or software mechanisms, or a combination of both.
- Some of the common protection schemes are:

  - **Base and limit registers**: These are special registers that store the base address and the size of the memory allocated to a process. The CPU checks every memory reference against these registers and generates an exception if the reference is invalid .
  - **Paging**: This is a technique that divides the physical memory into fixed-size blocks called pages and the logical memory into blocks of the same size called page frames. A page table maps the page frames to the pages and stores the protection bits for each page. The CPU uses the page table to translate the logical address to the physical address and to check the protection bits.
  - **Segmentation**: This is a technique that divides the logical memory into variable-size blocks called segments. Each segment has a base address, a limit, and a set of protection bits. A segment table maps the segments to the physical memory and stores the segment information. The CPU uses the segment table to translate the logical address to the physical address and to check the protection bits.
  - **Virtual memory**: This is a technique that allows the execution of processes that are not completely in the physical memory. The operating system uses a combination of paging and segmentation to manage the virtual memory. The operating system also uses a page replacement algorithm to swap the pages between the physical memory and the secondary storage.

- Some operating systems that implement memory protection include: Unix-like systems, Plan9 and Inferno, OS/2, RISC OS, Microsoft Windows, etc.



### Paging

Paging is a memory management scheme that allows the operating system to store and retrieve data from secondary storage for use in main memory. In this scheme, the operating system retrieves data from secondary storage in same-size blocks called pages .

Some of the main points about paging are:

- Paging eliminates the need for contiguous allocation of physical memory, which reduces external fragmentation and simplifies memory allocation.
- Paging allows the physical address space of a process to be non-contiguous, which enables faster and more efficient swapping of processes.
- Paging also allows the logical address space of a process to be larger than the physical address space, which enables virtual memory and memory protection.
- Paging requires a data structure called a page table to map the logical addresses to the physical addresses. The page table is stored in main memory and accessed by the CPU during address translation .
- Paging involves an additional bit called the valid/invalid bit, which indicates whether a page is present in main memory or not. If a page is not present, a page fault occurs and the operating system has to bring the page from secondary storage .
- Paging may introduce internal fragmentation, as the last page of a process may not be completely filled. The size of a page is usually a power of two, ranging from 512 bytes to 16 megabytes .
- Paging may also increase the overhead of address translation, as the CPU has to access the page table for every memory reference. This can be reduced by using a cache called a translation look-aside buffer (TLB) that stores the most frequently used page table entries .
- Paging can be combined with other memory management schemes, such as segmentation, to provide more flexibility and functionality .



### Segmentation

- Segmentation is an operating system memory management technique of division of a computer's primary memory into segments or sections.
- Segments are logical units of memory that correspond to the user's view of the program, such as code, data, stack, etc.
- Segments can be of variable size and can grow or shrink dynamically.
- Segments are identified by a segment number and an offset within the segment.
- Segments are mapped to physical memory by a segment table, which contains the base address and the limit of each segment.
- Segmentation provides the following advantages :
  - It allows the user to access memory in a logical way, rather than a physical way.
  - It supports the protection and sharing of memory among processes, by assigning different access rights to different segments.
  - It reduces the external fragmentation and compaction problems of paging, by allowing noncontiguous allocation of memory.
  - It provides a higher degree of flexibility and modularity than paging, by allowing processes to have multiple segments of different sizes and types.
- Segmentation also has some disadvantages :
  - It introduces the problem of internal fragmentation, as segments may not fully utilize the allocated memory blocks.
  - It requires more complex hardware and software to implement and manage the segment table and the segment mapping.
  - It may cause more overhead and latency in memory access, as the segment number and the offset need to be translated to a physical address.



### Paged segmentation

- Paged segmentation is a memory management technique that combines the advantages of paging and segmentation.
- In paged segmentation, the logical address space of a process is divided into variable-sized segments, and each segment is further divided into fixed-sized pages .
- The segment table contains the base address and the size of each segment, and the page table contains the frame number and the offset of each page within a segment.
- The physical address is computed by using the segment number, the page number, and the offset from the logical address.
- Paged segmentation allows for a flexible and efficient allocation of memory, where each segment can have a different size and meaning, and each page can have a different protection and sharing attributes .
- Paged segmentation reduces the external fragmentation caused by segmentation, and the internal fragmentation caused by paging.
- Paged segmentation also reduces the size of the segment table, by dividing it into pages and storing it in the main memory.
- Paged segmentation is used in some operating systems, such as Multics and Intel 80386.



### Virtual memory concepts

- Virtual memory is a method that computers use to manage storage space to keep systems running quickly and efficiently.
- Virtual memory uses both hardware and software to enable a computer to compensate for physical memory shortages, temporarily transferring data from random access memory (RAM) to disk storage.
- Virtual memory makes application programming easier by hiding fragmentation of physical memory, by delegating to the kernel the burden of managing the memory hierarchy, and by obviating the need to relocate program code or data.
- Virtual memory is implemented using a technique called paging, which divides the logical address space of a process into fixed-size units called pages, and the physical memory into units called frames.
- The operating system maintains a data structure called a page table for each process, which maps the logical addresses of the pages to the physical addresses of the frames where they are stored.
- When a process accesses a page that is not in the physical memory, a page fault occurs, and the operating system has to bring the page from the disk to the memory, replacing an existing page if necessary.
- The operating system uses various algorithms to decide which page to replace, such as least recently used (LRU), first in first out (FIFO), or optimal.
- The performance of virtual memory depends on the page size, the page fault rate, and the page replacement policy.
- Virtual memory allows multiple processes to share the same physical memory, increasing the degree of multiprogramming and the utilization of the CPU.
- Virtual memory also provides memory protection and isolation, preventing one process from accessing or modifying the memory of another process.



### Demand paging

- Demand paging is a method of virtual memory management that allows a process to execute without loading all of its pages into physical memory.
- Demand paging works by loading pages from the secondary storage (such as a hard disk) into the main memory only when they are needed or demanded by the CPU.
- Demand paging reduces the amount of physical memory required by a process and allows more processes to run concurrently.
- Demand paging also reduces the I/O overhead and the startup time of a process, as only the necessary pages are loaded initially.
- Demand paging involves the following components and steps:
  - A page table that maps the logical address space of a process to the physical address space of the main memory.
  - A valid-invalid bit for each entry in the page table that indicates whether the corresponding page is in the main memory or not.
  - A page fault handler that is invoked by the operating system when a page fault occurs, i.e., when the CPU tries to access a page that is not in the main memory.
  - A free-frame list that keeps track of the available frames in the main memory.
  - A page replacement algorithm that decides which page to evict from the main memory when there is no free frame available.
  - A fetch policy that determines when a page should be brought into the main memory, either before or after a page fault occurs.
  - A placement policy that determines where a page should be placed in the main memory, either in a fixed or a variable location.
  - A cleaning policy that determines when a modified page should be written back to the secondary storage, either immediately or later.



### Performance of demand paging

- Demand paging is a memory management technique that allows the operating system to load pages of a process into the main memory only when they are needed, rather than loading the entire process at once  .
- Demand paging can improve the performance of the system by reducing the number of disk I/O operations, increasing the degree of multiprogramming, and allowing the use of virtual memory .
- However, demand paging also introduces the possibility of page faults, which occur when a requested page is not present in the main memory and has to be brought from the disk .
- Page faults can significantly increase the effective access time of memory, which is the average time required to access a word in memory .
- The effective access time can be calculated as follows :

  - Let *p* be the probability of a page fault (0 ≤ *p* ≤ 1).
  - Let *ma* be the memory access time, which is the time to access a word in memory without any page fault.
  - Let *pf* be the page fault service time, which is the time to handle a page fault and bring the page from the disk to the memory.
  - Then, the effective access time is:

    - effective access time = (1 - *p*) x *ma* + *p* x *pf*

- The performance of demand paging depends on various factors, such as :

  - The page size: The larger the page size, the less the number of page tables required, which can result in faster memory access times. However, larger page sizes also increase the internal fragmentation and the disk transfer time.
  - The page replacement algorithm: The page replacement algorithm determines which page to evict from the memory when a page fault occurs. The algorithm should minimize the number of page faults and the overhead of maintaining the page tables.
  - The degree of locality: The degree of locality refers to how frequently a process accesses the same set of pages. The higher the degree of locality, the lower the probability of page faults.



### Page replacement algorithms

- Page replacement algorithms are techniques used by an operating system to manage the memory allocation and deallocation of the physical memory (RAM) of a computer.
- Page replacement algorithms determine how the victim page (the page to be replaced) is selected when a page fault occurs. The aim is to minimize the page fault rate.
- A page fault happens when a running program accesses a memory page that is mapped into the virtual address space but not loaded in physical memory.
- Some common page replacement algorithms are:
  - First In First Out (FIFO): This is the simplest algorithm. In this algorithm, the operating system maintains a queue of all the pages in memory. The oldest page is selected as the victim page and replaced by the new page.
  - Optimal Page replacement: This is the best algorithm as this algorithm replaces the page that will not be used for the longest duration of time in the future. However, this algorithm is not feasible in practice as it requires the knowledge of the future page references.
  - Least Recently Used (LRU): This algorithm replaces the page that has not been used for the longest period of time. This algorithm approximates the optimal page replacement by using the past page references as an indicator of the future ones.
  - Least Frequently Used (LFU): This algorithm replaces the page that has the lowest frequency of use. This algorithm assumes that the page with the least frequency of use is likely to be used less in the future.
  - Clock: This algorithm uses a circular list of pages with a pointer that moves through the list. Each page has a use bit that is set when the page is accessed. When a page fault occurs, the pointer scans the list and replaces the first page with the use bit cleared. If all the pages have the use bit set, the pointer clears the use bit of each page and repeats the scan.



### Thrashing

- Thrashing is a phenomenon that occurs when a computer's virtual memory resources are overused, leading to a constant state of paging and page faults, inhibiting most application-level processing.
- Thrashing happens when the operating system tries to increase the degree of multiprogramming by loading more processes into the main memory, but the available frames are not enough to support the pages in active use by the processes.
- Thrashing results in severe performance problems in the operating system, such as low CPU utilization, high disk I/O, and long response time.
- Thrashing can be detected by monitoring the page fault rate and the CPU utilization. If the page fault rate is high and the CPU utilization is low, it indicates that the system is thrashing.
- Thrashing can be handled by using various techniques, such as:
  - Working set model: This model keeps track of the pages that a process has referenced in a fixed period of time, called the working set window. The working set of a process is the minimum number of pages that it needs to execute without causing too many page faults. The operating system allocates frames to each process according to its working set size, and swaps out the processes whose working sets are not in memory.
  - Page fault frequency scheme: This scheme controls the number of frames allocated to each process by using a lower bound and an upper bound on the acceptable page fault rate. If the page fault rate of a process is too low, it means that the process has more frames than it needs, and some frames can be taken away. If the page fault rate of a process is too high, it means that the process does not have enough frames, and more frames should be allocated. The operating system adjusts the frame allocation of each process dynamically based on its page fault rate.
  - Global and local replacement policies: These policies determine which frames to replace when a page fault occurs. A global replacement policy allows a process to select a replacement frame from the set of all frames, even if it belongs to another process. A local replacement policy restricts a process to select a replacement frame from its own set of allocated frames. A global replacement policy can help reduce thrashing by taking frames from processes that have a low page fault rate, while a local replacement policy can prevent thrashing by ensuring that each process has a minimum number of frames.



### Cache memory organization

- Cache memory is a type of memory that is used to increase the speed of data access.
- Cache memory holds frequently requested data and instructions that are copied from the main memory.
- Cache memory is an extension of the main memory and acts as a buffer between the CPU and the main memory.
- Cache memory is organized into a hierarchy of levels, such as L1, L2, and L3, where L1 is the fastest and smallest, and L3 is the slowest and largest.
- Cache memory organization is about mapping data in the main memory to a location in the cache memory.
- There are different methods of cache mapping, such as direct mapping, associative mapping, and set-associative mapping.
- Direct mapping assigns each block of main memory to a specific line in the cache.
- Associative mapping allows any block of main memory to be stored in any line of the cache.
- Set-associative mapping divides the cache into sets of lines, and each set can store any block of main memory.
- Cache memory organization affects the performance, cost, and complexity of the cache system.



### Locality of reference for the notes of the Unit 4 - Memory Management in the subject of Operating system

- Locality of reference is the tendency of a computer program to access the same set of memory locations for a particular time period .
- Locality of reference is based on the observation that programs usually exhibit two types of locality: temporal and spatial  .
- Temporal locality means that a memory location that is accessed once is likely to be accessed again soon. For example, a loop variable or a frequently used function.
- Spatial locality means that a memory location that is accessed once is likely to have its nearby locations accessed soon. For example, an array or a sequential code.
- Locality of reference is important for memory management because it can improve the performance and efficiency of the system by reducing the number of page faults and cache misses .
- Page faults occur when a program tries to access a page that is not present in the main memory. Cache misses occur when a program tries to access a data that is not present in the cache memory.
- To exploit the locality of reference, the system can use various techniques such as caching, paging, prefetching, and buffering to keep the frequently and recently accessed data in the faster and smaller memory levels .
- Caching is the process of storing a copy of a data in a cache memory, which is faster and closer to the processor than the main memory. The cache memory can store the most frequently or recently accessed data, and check if the requested data is already in the cache before accessing the main memory.
- Paging is the process of dividing the main memory and the virtual memory into fixed-size units called pages. The pages that are currently needed by the program are loaded into the main memory, and the pages that are not needed are swapped out to the virtual memory. The system maintains a page table that maps the logical addresses to the physical addresses of the pages.
- Prefetching is the process of fetching the data that is likely to be accessed soon from the main memory or the virtual memory to the cache memory or the main memory in advance. Prefetching can reduce the latency and the number of page faults and cache misses by anticipating the future data requests.
- Buffering is the process of temporarily storing the data in a buffer, which is a memory area that can hold multiple data items. Buffering can improve the performance and efficiency of the system by reducing the number of memory accesses and allowing the data to be processed in batches.



## Unit 5 - I/O Management and Disk Scheduling

- I/O management is the process of controlling the input and output devices of a computer system, such as disks, keyboards, printers, terminals, etc.
- I/O management involves the following tasks:
  - Providing a uniform interface for different types of devices
  - Allocating and deallocating devices to processes
  - Buffering and caching data to improve performance
  - Handling errors and exceptions
  - Implementing security and protection mechanisms
- Disk scheduling is a specific aspect of I/O management that deals with the order in which disk requests are serviced by the disk controller.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller. Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - The access time of a disk request depends on the seek time, rotational latency, and transfer time. Seek time is the time required to move the disk head to the desired track. Rotational latency is the time required to wait for the desired sector to rotate under the disk head. Transfer time is the time required to read or write the data from or to the disk. Seek time and rotational latency are the major components of the access time and vary depending on the location of the data on the disk.
  - The objective of disk scheduling is to minimize the total access time and maximize the disk throughput (the amount of data transferred per unit time).
- Disk scheduling algorithms are the methods used to decide the order of servicing the disk requests in the waiting queue. Some common disk scheduling algorithms are:
  - First Come First Served (FCFS): The disk requests are serviced in the order they arrive in the queue. This algorithm is simple and fair, but does not take into account the location of the data on the disk and may result in long seek times and low disk throughput.
  - Shortest Seek Time First (SSTF): The disk request with the shortest seek time from the current head position is serviced next. This algorithm reduces the seek time and improves the disk throughput, but may cause starvation for some requests that are far away from the current head position.
  - SCAN: The disk head moves in one direction and services all the requests in that direction until it reaches the end of the disk. Then it reverses the direction and repeats the process. This algorithm is also known as the elevator algorithm, as it resembles the movement of an elevator in a building. This algorithm avoids starvation and provides a more uniform service than SSTF, but may cause long waiting times for requests at the ends of the disk.
  - C-SCAN: The disk head moves in one direction and services all the requests in that direction until it reaches the end of the disk. Then it jumps to the other end of the disk and repeats the process. This algorithm is a circular version of SCAN, and provides a more even distribution of service than SCAN, but may cause longer average waiting times than SCAN.
  - LOOK and C-LOOK: These algorithms are similar to SCAN and C-SCAN, except that they do not go to the end of the disk, but only to the last request in that direction. This reduces the unnecessary movement of the disk head and improves the performance of SCAN and C-SCAN.



### I/O devices

- I/O devices are the hardware components that allow the operating system to interact with the external world, such as users, networks, and storage devices.
- Some common I/O devices are mouse, keyboard, touchpad, USB devices, bit-mapped screen, LED, on/off switch, network connections, audio I/O, printers, etc. 
- I/O devices can be classified into two categories: block devices and character devices.
  - Block devices are devices that transfer data in fixed-size blocks, such as disk drives, CD-ROMs, and flash drives. Block devices support random access to any block of data.
  - Character devices are devices that transfer data one character at a time, such as keyboards, mice, and serial ports. Character devices do not support random access to data.
- I/O devices are managed by the operating system using three components: I/O hardware, device drivers, and I/O subsystems.
  - I/O hardware is the set of specialized hardware devices that help the operating system access the I/O devices. These devices are located inside the motherboard and connected to the processor using a bus.
  - Device drivers are the software modules that communicate with the I/O hardware and control the specific functions of each I/O device. Device drivers are usually written by the device manufacturers and loaded by the operating system at boot time or on demand.
  - I/O subsystems are the software components that provide a uniform interface for the device drivers and the rest of the operating system. I/O subsystems handle tasks such as buffering, caching, spooling, scheduling, and error handling. 
- I/O scheduling is the process of deciding which I/O request to serve next from a queue of pending requests. I/O scheduling is used to improve the performance and efficiency of the I/O system by reducing the waiting time, increasing the throughput, and balancing the load among the I/O devices.



# I/O Subsystems for Operating System

- I/O subsystems are the components of the operating system that manage the input and output devices, such as keyboards, mice, disks, printers, scanners, etc.
- I/O subsystems provide an efficient and secure way of communication between the central system and the outside environment.
- I/O subsystems consist of the following layers of software:

  - **Device drivers**: These are software modules that can be plugged into an OS to handle a particular device. They are responsible for controlling the device, translating the logical requests from the higher layers into device-specific commands, and handling errors and interrupts.
  - **Interrupt handlers**: These are routines that are executed when a device signals an interrupt to the processor. They are responsible for saving the state of the current process, acknowledging the interrupt, and transferring the control to the device driver.
  - **Device-independent I/O software**: This is the layer that provides common services and functions for all types of devices, such as buffering, caching, spooling, device allocation, device naming, etc. It also provides a uniform interface for the user-space I/O software to access the devices.
  - **User-space I/O software**: This is the layer that provides user-level libraries and applications for performing I/O operations, such as file systems, network protocols, graphical user interfaces, etc. It also provides system calls for the user programs to request I/O services from the kernel.
  - **Kernel I/O subsystem**: This is the layer that coordinates the I/O activities of the other layers, such as scheduling, dispatching, synchronization, error handling, security, etc. It also interacts with the memory management and process management subsystems of the OS.



### I/O Buffering

- I/O buffering is a technique used by the operating system to improve the efficiency and performance of input/output operations.
- I/O buffering involves using a temporary memory area, called a buffer, to store data that is transferred between a user process and an I/O device.
- I/O buffering can reduce the number of disk accesses, avoid unnecessary data copying, and allow concurrent execution of user processes and I/O operations.
- There are different types of I/O buffering techniques, such as single buffering, double buffering, and circular buffering.

#### Single Buffering

- Single buffering is the simplest form of I/O buffering, where the operating system assigns a single buffer in the system portion of main memory to each I/O operation.
- In single buffering, the user process issues an I/O request and waits for the completion of the operation. The operating system copies the data from the device to the buffer, or from the buffer to the device, depending on the direction of the transfer.
- Single buffering has the advantage of simplicity and low memory overhead, but it has the disadvantage of low throughput and high latency, as the user process and the I/O device cannot work in parallel.

#### Double Buffering

- Double buffering is an improvement over single buffering, where the operating system assigns two buffers in the system portion of main memory to each I/O operation.
- In double buffering, the user process issues an I/O request and continues to execute until it needs the data. The operating system copies the data from the device to one buffer, while the user process accesses the data from the other buffer, or vice versa.
- Double buffering has the advantage of higher throughput and lower latency, as the user process and the I/O device can work in parallel, but it has the disadvantage of higher memory overhead and complexity.

#### Circular Buffering

- Circular buffering is a further improvement over double buffering, where the operating system assigns a fixed number of buffers, arranged in a circular fashion, to each I/O operation.
- In circular buffering, the user process issues an I/O request and continues to execute until it needs the data. The operating system copies the data from the device to the next available buffer in the circular queue, while the user process accesses the data from the oldest buffer in the queue, or vice versa.
- Circular buffering has the advantage of optimal throughput and latency, as the user process and the I/O device can work in parallel without waiting for each other, but it has the disadvantage of higher memory overhead and complexity.



### Disk Storage and Disk Scheduling

- Disk storage is a type of secondary storage that uses magnetic or optical disks to store data permanently or semi-permanently.
- Disk storage devices include hard disk drives (HDDs), floppy disk drives (FDDs), optical disk drives (ODDs), solid state drives (SSDs), etc.
- Disk storage devices have two main characteristics: capacity and performance.
- Capacity is the amount of data that can be stored on a disk, measured in bytes or multiples of bytes (KB, MB, GB, TB, etc.).
- Performance is the speed at which data can be read from or written to a disk, measured in terms of transfer rate, access time, latency, and throughput.
- Transfer rate is the rate at which data can be transferred between the disk and the main memory, measured in bits per second (bps) or multiples of bps (Kbps, Mbps, Gbps, etc.).
- Access time is the time required to locate and retrieve a block of data from the disk, measured in milliseconds (ms) or microseconds (µs).
- Access time consists of two components: seek time and rotational latency.
- Seek time is the time required to move the read/write head to the desired track on the disk, measured in ms or µs.
- Rotational latency is the time required to rotate the disk until the desired sector is under the read/write head, measured in ms or µs.
- Throughput is the amount of data that can be transferred in a given time interval, measured in bytes per second (Bps) or multiples of Bps (KBps, MBps, GBps, etc.).
- Throughput depends on the transfer rate, the access time, and the size of the data blocks.
- Disk scheduling is a technique used by the operating system to schedule multiple requests for accessing the disk.
- Disk scheduling is also known as I/O scheduling or disk request scheduling.
- Disk scheduling is important because:
  - Multiple I/O requests may arrive by different processes and only one I/O request can be served at a time by the disk controller.
  - Thus other I/O requests need to wait in the waiting queue and need to be scheduled.
  - Disk scheduling aims to reduce the total seek time, which is the sum of the seek times for all the I/O requests in the queue.
  - Reducing the total seek time can improve the disk performance and the system performance.
- Disk scheduling algorithms are the algorithms used for disk scheduling.
- The purpose of disk scheduling algorithms is to reduce the total seek time by selecting an optimal order of servicing the I/O requests in the queue.
- Some of the common disk scheduling algorithms are:
  - First In First Out (FIFO) or First Come First Served (FCFS): This algorithm services the I/O requests in the order of their arrival in the queue. It is simple and fair, but it does not minimize the total seek time.
  - Shortest Seek Time First (SSTF): This algorithm services the I/O request that is closest to the current position of the read/write head. It minimizes the average seek time, but it may cause starvation for some requests that are far away from the head.
  - SCAN or Elevator: This algorithm services the I/O requests in one direction until it reaches the end of the disk, then it reverses the direction and services the requests in the other direction. It avoids starvation and provides a more uniform service time, but it may cause a long waiting time for some requests at the ends of the disk.
  - C-SCAN or Circular SCAN: This algorithm is similar to SCAN, but instead of reversing the direction at the ends of the disk, it jumps to the other end and continues in the same direction. It provides a more fair service time for the requests at the ends of the disk, but it may cause a longer average seek time than SCAN.
  - LOOK and C-LOOK: These algorithms are variations of SCAN and C-SCAN, but they do not go to the ends of the disk, instead they change the direction or jump to the other end when there are no more requests in the current direction. They reduce the unnecessary head movements and improve the performance of SCAN and C-SCAN.



### RAID

- RAID stands for **Redundant Arrays of Independent Disks** , a technique that uses multiple disks to improve performance, reliability, or both  .
- RAID arrays appear to the operating system as a single logical drive  .
- RAID employs the techniques of **disk mirroring** or **disk striping** .
  - Disk mirroring copies identical data onto more than one drive, providing data redundancy and fault tolerance .
  - Disk striping distributes data across multiple drives, allowing parallel I/O operations and improving performance.
- RAID can be implemented by **hardware** or **software** .
  - Hardware RAID uses a dedicated controller device to manage the disks and perform RAID functions .
  - Software RAID uses the host's CPU and operating system to manage the disks and perform RAID functions .
- There are different types or levels of RAID, each with different advantages and disadvantages .
  - RAID 0: Striping without redundancy. It offers the highest performance but no fault tolerance .
  - RAID 1: Mirroring without striping. It offers the highest reliability but lower performance and storage efficiency .
  - RAID 5: Striping with parity. It offers a balance of performance and reliability, but requires more computation and disk space .
  - RAID 10: A combination of RAID 1 and RAID 0. It offers high performance and reliability, but requires more disks and has lower storage efficiency .
  - Other RAID levels include RAID 2, RAID 3, RAID 4, RAID 6, and RAID 50.



### File System

- A file system is a method and data structure that the operating system uses to control how data is stored and retrieved on a storage device.
- A file system is responsible for organizing files and directories, and keeping track of which areas of the media belong to which file and which are not being used.
- A file system also provides an interface for users and applications to access and manipulate files and directories.
- A file system can be classified into two types: disk-based and network-based.
  - Disk-based file systems are installed on local storage devices, such as hard disks, flash drives, CDs, etc. Examples of disk-based file systems are FAT, NTFS, ext, etc .
  - Network-based file systems are accessed over a network, such as the Internet, LAN, etc. Examples of network-based file systems are NFS, CIFS, WebDAV, etc.
- A file system installed on an operating system consists of three layers: physical, virtual, and logical.
  - Physical file system: This layer deals with the low-level details of how data is stored on the physical media, such as sectors, blocks, clusters, etc.
  - Virtual file system: This layer provides a common interface for different types of file systems to interact with the operating system kernel, such as system calls, file descriptors, etc.
  - Logical file system: This layer implements the high-level features of a file system, such as file and directory structures, metadata, permissions, etc.



### File concept

- A file is a collection of related information that is recorded on secondary storage such as magnetic disks, magnetic tapes and optical disks.
- A file has a certain defined structure according to its type.
- A file is organized into logical units called records. A record is a collection of related fields. A field is a basic element of data.
- A file has a name that uniquely identifies it within a specific directory of the file system.
- A file has certain attributes that describe its properties and state. Some common file attributes are:
  - Name: the symbolic file name
  - Identifier: the unique tag that identifies the file within the file system
  - Type: the format or structure of the file
  - Location: the physical or logical address of the file
  - Size: the current size of the file in bytes, blocks or records
  - Protection: the access rights or permissions of the file
  - Time, date and user identification: the data for creation, last modification and last access of the file
- A file can be accessed in different modes, such as read, write, execute, append, update, delete, etc.
- A file can be shared among different users and processes, subject to the protection and access rights.
- A file can be manipulated by various operations, such as create, open, close, read, write, seek, delete, truncate, rename, copy, move, etc.



### File organization and access mechanism

- File organization is the way of arranging the files on a storage device, such as a disk or a tape. It affects the performance, reliability, and security of the file system. 
- File access mechanism is the way of accessing the data or information stored in the files by the operating system or the applications. It affects the efficiency, convenience, and flexibility of the file system. 
- There are different types of file organization and access mechanism, depending on the nature and purpose of the files. Some common types are:

  - Sequential organization and access: The file is stored and accessed in a sequential order, one record after the other. This is suitable for files that are processed in a batch mode, such as backup files or log files. The advantage of this method is its simplicity and low cost. The disadvantage is that it does not support random access or direct access to any record.   

  - Direct organization and access: The file is divided into fixed-length blocks, and each block has a unique address or block number. The file can be accessed randomly or directly by specifying the block number. This is suitable for files that are processed interactively, such as database files or index files. The advantage of this method is its fast and flexible access. The disadvantage is that it requires more space and complexity to manage the blocks and their addresses.    

  - Indexed sequential organization and access: The file is stored and accessed sequentially, but it also has an index that contains the key and the address of each record. The file can be accessed sequentially or directly by using the index. This is suitable for files that are processed both in a batch mode and an interactive mode, such as payroll files or student records. The advantage of this method is that it combines the benefits of sequential and direct access. The disadvantage is that it requires more space and time to maintain the index and the sequential order.



### File directories for the notes of the Unit 5 - I/O Management and Disk Scheduling in the subject of Operating system

- A file directory is a data structure that stores information about the files in a file system.
- A file directory can have different levels of hierarchy, such as a single-level directory, a two-level directory, a tree-structured directory, or an acyclic-graph directory.
- A file directory can have different types of entries, such as file names, file attributes, file locations, file permissions, or file links.
- A file directory can support different operations, such as creating, deleting, renaming, searching, or listing files.
- A file directory can have different access methods, such as sequential, direct, indexed, or hashed.
- A file directory can have different allocation methods, such as contiguous, linked, indexed, or combined.
- A file directory can have different protection mechanisms, such as passwords, access control lists, or encryption.
- A file directory can have different performance issues, such as disk space utilization, disk access time, or disk reliability.

- I/O management is the process of coordinating and controlling the input and output devices of a computer system.
- I/O management can have different components, such as I/O devices, I/O controllers, I/O ports, I/O buffers, I/O drivers, or I/O schedulers.
- I/O management can have different goals, such as efficiency, fairness, throughput, response time, or quality of service.
- I/O management can have different techniques, such as polling, interrupt-driven, direct memory access, or I/O channels.
- I/O management can have different strategies, such as blocking, non-blocking, synchronous, asynchronous, or buffered I/O.
- I/O management can have different challenges, such as device diversity, device contention, device failure, or device security.

- Disk scheduling is the process of deciding the order of servicing the disk requests in the disk queue.
- Disk scheduling can have different objectives, such as minimizing the seek time, minimizing the rotational latency, maximizing the disk bandwidth, or balancing the disk load.
- Disk scheduling can have different algorithms, such as first-come first-served, shortest seek time first, scan, circular scan, look, circular look, or elevator.
- Disk scheduling can have different factors, such as disk geometry, disk head movement, disk request arrival pattern, disk request service time, or disk request priority.
- Disk scheduling can have different performance metrics, such as average seek time, average rotational latency, average transfer time, average response time, or average waiting time.



# I/O Management and Disk Scheduling

## I/O Management
- I/O management is the process of coordinating and controlling the communication between the CPU and the external devices, such as disks, terminals, printers, etc.
- I/O devices vary in their characteristics, such as data transfer rate, access method, capacity, etc. Therefore, different I/O devices may require different I/O techniques and strategies.
- I/O management involves several components, such as:
  - I/O hardware: the physical devices and controllers that perform I/O operations.
  - I/O software: the software layers that provide interfaces and services for I/O operations, such as device drivers, interrupt handlers, device-independent I/O, user-level I/O, etc.
  - I/O performance: the metrics and methods to measure and improve the efficiency and effectiveness of I/O operations.

## Disk Scheduling
- Disk scheduling is the process of deciding the order and timing of I/O requests to a disk drive, in order to optimize the disk performance and reduce the disk access time.
- Disk scheduling is necessary because disk access time consists of two components: seek time and rotational latency. Seek time is the time required to move the disk head to the desired track, and rotational latency is the time required to wait for the desired sector to rotate under the disk head. Both seek time and rotational latency depend on the physical location of the data on the disk, and can be minimized by choosing an appropriate order of I/O requests.
- Disk scheduling algorithms are the methods to determine the order of I/O requests to a disk drive, based on different criteria and objectives, such as:
  - FCFS (First Come First Served): the simplest algorithm that processes the I/O requests in the order they arrive, without any reordering or optimization.
  - SSTF (Shortest Seek Time First): the algorithm that processes the I/O request that requires the shortest seek time from the current position of the disk head, thus minimizing the total seek time.
  - SCAN (Elevator): the algorithm that processes the I/O requests in one direction until there are no more requests in that direction, then reverses the direction and repeats the process, thus avoiding the starvation of requests at the ends of the disk.
  - C-SCAN (Circular SCAN): the algorithm that processes the I/O requests in one direction until there are no more requests in that direction, then jumps to the other end of the disk and repeats the process, thus providing a more uniform service time for all requests.
  - LOOK and C-LOOK: the variants of SCAN and C-SCAN that only change the direction or jump to the other end of the disk when there are requests in that direction, thus avoiding unnecessary movements of the disk head.



### File system implementation issues

- A file system is a method an operating system uses to store, organize, and manage files and directories on a storage device.
- File system implementation involves numerous on-disk and in-memory configurations and structures that differ based on the operating system and the file system.
- Some of the common issues and challenges in file system implementation are:

  - **Disk space management**: How to allocate and deallocate disk blocks efficiently and avoid fragmentation .
  - **File naming**: How to map logical file names to physical disk locations and support different naming conventions .
  - **Directory structure**: How to organize files in a hierarchical or flat structure and support different operations such as creation, deletion, renaming, listing, etc .
  - **File protection**: How to enforce access control policies and permissions for different users and groups .
  - **Reliability and consistency**: How to ensure the integrity and availability of file system data in the presence of failures, crashes, or concurrent access .
  - **Performance**: How to optimize the file system performance by using caching, buffering, prefetching, or other techniques .

- Some of the common data structures and algorithms used for file system implementation are:

  - **File allocation table (FAT)**: A table that stores the mapping between logical file blocks and physical disk blocks. It can be implemented as a linked list, a bitmap, or an index .
  - **Inode**: A data structure that stores the metadata of a file, such as its size, type, permissions, timestamps, and pointers to its data blocks .
  - **Directory entry**: A data structure that stores the name and inode number of a file or a subdirectory in a directory .
  - **Superblock**: A data structure that stores the information about the file system, such as its size, type, free space, and root directory .
  - **Disk scheduling**: An algorithm that determines the order of servicing disk requests to minimize the seek time and rotational latency .

- Some of the common file systems used in different operating systems are:

  - **NTFS**: A file system used by Windows that supports journaling, compression, encryption, and large file sizes.
  - **ext4**: A file system used by Linux that supports journaling, extents, delayed allocation, and large file sizes.
  - **HFS+**: A file system used by macOS that supports journaling, compression, encryption, and large file sizes.
  - **FAT32**: A file system used by older versions of Windows and other operating systems that supports compatibility, portability, and simplicity.



### File system protection and security

- File system protection and security are the mechanisms that ensure the integrity, confidentiality, and availability of files and directories on a computer system.
- File system protection involves controlling the access of users and programs to the files and directories, preventing unauthorized or malicious modifications, deletions, or copies of the data.
- File system security involves protecting the files and directories from external threats, such as viruses, worms, trojan horses, or hackers, that may compromise the system or the data.
- Some of the common techniques for file system protection and security are:

  - **Access control lists (ACLs)**: These are lists that specify the users and the types of access (read, write, execute, etc.) they have for each file or directory. The operating system checks the ACLs before granting or denying access to the files or directories. For example, Windows File Protection (WFP) uses ACLs to prevent programs from replacing critical system files .
  - **Encryption**: This is the process of transforming the data into an unreadable form using a secret key, so that only authorized parties can decrypt and access the data. Encryption can be applied to individual files, directories, or entire disks. For example, BitLocker is a feature in Windows that encrypts the entire disk to protect the data from theft or loss.
  - **Authentication**: This is the process of verifying the identity of a user or a program before granting access to the files or directories. Authentication can be based on passwords, biometrics, tokens, certificates, or other methods. For example, Windows Hello is a feature in Windows that allows users to sign in using their face, fingerprint, or PIN.
  - **Auditing**: This is the process of recording and monitoring the activities of users and programs on the files and directories, such as who accessed, modified, deleted, or copied the data, when, and from where. Auditing can help detect and prevent unauthorized or malicious actions, and provide evidence for investigations or accountability. For example, Windows Event Viewer is a tool that displays the audit logs of the system and the applications.

