### Prevention for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

Preemption is a technique used in CPU scheduling to temporarily interrupt a process that is currently executing on the CPU and to allocate the CPU to another process. Preemption allows the scheduler to dynamically adjust the allocation of the CPU to processes, and to ensure that processes are executed fairly and efficiently.

There are several factors that can cause preemption in CPU scheduling, including:

1. Time slicing: The scheduler allocates a fixed time quantum to each process, and when the time quantum expires, the process is preempted and the CPU is allocated to the next process in the ready queue.

2. Interrupts: An interrupt can cause the CPU to be temporarily allocated to another process, such as an I/O operation or a timer interrupt.

3. Higher-priority processes: A higher-priority process can cause a lower-priority process to be preempted, allowing the higher-priority process to execute on the CPU.

Preemption has several advantages, including improved system responsiveness, improved fairness, and improved utilization of the CPU. However, preemption also has several disadvantages, including increased overhead and increased complexity in the scheduler.

In this unit, we will study the concept of preemption in CPU scheduling, and examine the factors that cause preemption. We will also study the advantages and disadvantages of preemption, and the trade-offs involved in using preemption in CPU scheduling. This will provide a foundation for understanding the design and implementation of CPU scheduling algorithms, and for exploring the various approaches to improving the performance of CPU scheduling algorithms.
