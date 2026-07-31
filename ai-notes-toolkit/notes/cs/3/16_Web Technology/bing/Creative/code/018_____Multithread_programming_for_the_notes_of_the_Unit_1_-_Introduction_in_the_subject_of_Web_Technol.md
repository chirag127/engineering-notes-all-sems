# Multithread Programming for the Notes of the Unit 1 - Introduction in the Subject of Web Technology

- Multithreading is the ability of a program or an operating system to enable more than one user at a time without requiring multiple copies of the program running on the computer.
- Multithreading can also handle multiple requests from the same user. Each user request for a program or system service is tracked as a thread with a separate identity.
- Multithreading is the phenomenon of executing more than a thread in the system, where the execution of these threads can be of two different types, such as Concurrent and Parallel multithread executions.
- A Thread can be defined as a chunk or unit of a process that can be identified as either a user-level thread or a Kernel-level thread.
- User-level threads are managed by the user program without the involvement of the operating system. Kernel-level threads are managed by the operating system directly.
- Multithreading has several benefits for the operating system and the applications, such as:
  - Responsiveness: A multithreaded program can respond to user input while performing other tasks in the background. For example, a multi threaded web browser allow user interaction in one thread while an video is being loaded in another thread.
  - Resource Sharing: Processes may share resources only through techniques such as Message Passing or Shared Memory. Threads can share resources of the process to which they belong by default.
  - Economy: Creating and switching between threads is faster and cheaper than creating and switching between processes. Threads share the address space and the context of the process, so they do not need to duplicate them.
  - Utilization of Multiprocessor or Multi-core Systems: A single process can use only one processor or core at a time. A multithreaded process can use multiple processors or cores simultaneously, increasing the throughput and performance of the system .
- Multithreading programming allows the creation and management of multiple threads within a single process. A multithreaded application is an application that uses more than two threads for two processor or more.
- Multithreading programming requires the use of synchronization mechanisms to avoid data inconsistency, deadlock, and race conditions among the threads. Some common synchronization mechanisms are mutexes, semaphores, monitors, and locks.
- Multithreading programming can be implemented in different languages and platforms, such as Java, C#, C++, Python, etc. Each language and platform may have its own syntax and library for multithreading programming.