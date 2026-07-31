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