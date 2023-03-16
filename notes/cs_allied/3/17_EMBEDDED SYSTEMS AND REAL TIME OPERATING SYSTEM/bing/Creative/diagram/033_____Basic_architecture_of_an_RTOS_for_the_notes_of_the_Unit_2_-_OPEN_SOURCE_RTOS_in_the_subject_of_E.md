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

![RTOS Architecture](https://www.engineersgarage.com/wp-content/uploads/2011/11/RTOS-Architecture.jpg)

: https://www.engineersgarage.com/rtos-real-time-operating-system/
: https://www.windriver.com/solutions/learning/rtos
: https://microcontrollerslab.com/rtos-real-time-operating-system/