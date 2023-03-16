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