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