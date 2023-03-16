# Real Time Operating Systems

## Introduction

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints  .
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS is designed for critical systems and for devices like microcontrollers that are timing-specific.
- An RTOS has two key features: predictability and determinism. Predictability means that repeated tasks are performed within a tight time boundary, while determinism means that the system responds to events in a fixed and known amount of time.
- An RTOS can be classified into two types: hard real-time and soft real-time  . A hard real-time system must meet all the deadlines, otherwise the system may fail or cause severe consequences. A soft real-time system can tolerate some missed deadlines, but the quality of service may degrade  .

## Real Time Kernel Basics

- A real-time kernel is the core component of an RTOS that provides the basic services for managing tasks, interrupts, timers, and synchronization  .
- A real-time kernel can be implemented as a library, a module, or a separate layer in the system architecture  .
- A real-time kernel supports the following features  :
  - Real-time multithreading: The ability to create and execute multiple tasks (or threads) that run concurrently and independently on the same processor or on different processors in a multiprocessor system  .
  - Inter-thread communication and synchronization: The ability to exchange data and signals between tasks, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, event flags, and pipes  .
  - Memory management: The ability to allocate and deallocate memory for tasks and data structures, and to protect the memory regions from unauthorized access or corruption  .
  - Interrupt handling: The ability to respond to external or internal events that require immediate attention, such as hardware devices, timers, or software exceptions  .
  - Timer services: The ability to measure and control the time and frequency of tasks and events, and to generate periodic or one-shot signals or callbacks  .
  - Debugging and profiling: The ability to monitor and analyze the behavior and performance of the system, and to identify and correct errors or bottlenecks  .

## Examples of Real Time Operating Systems

- Some examples of RTOSs are  :
  - Azure RTOS ThreadX: This advanced RTOS is designed specifically for deeply embedded applications. It supports multicore and symmetric multiprocessing (SMP) architectures, and provides a rich set of services, such as TCP/IP stack, USB host/device stack, file system, GUI, and IoT protocols.
  - FreeRTOS: This open source RTOS is widely used for microcontrollers and small embedded systems. It supports various architectures, such as ARM, AVR, PIC, and x86, and provides a minimal but sufficient set of services, such as task management, queues, semaphores, timers, and event groups.
  - VxWorks: This commercial RTOS is widely used for mission-critical and safety-critical applications, such as aerospace, defense, industrial, and automotive. It supports various architectures, such as x86, ARM, PowerPC, and MIPS, and provides a comprehensive set of services, such as networking, security, graphics, file system, and POSIX compatibility.
  - Windows CE: This RTOS is a subset of the Windows operating system that is designed for embedded devices, such as smartphones, tablets, and handheld computers. It supports various architectures, such as x86, ARM, MIPS, and SH, and provides a familiar Windows-based user interface