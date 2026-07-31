 Here are the points on Advantage and disadvantage of RTOS for the notes of the Unit 2 - OPEN SOURCE RTOS:

### Advantages:

1. Provides multitasking environment: RTOS provides multitasking environment which allows multiple tasks to run concurrently. This enables efficient utilization of CPU.
2. Scheduling: RTOS provides Scheduling mechanism to schedule multiple tasks. Scheduling can be preemptive or non-preemptive. This ensures all tasks get CPU time.
3. Fast response: RTOS provides fast response as it is designed for real time systems. The tasks are scheduled strictly based on their priorities to meet deadlines.
4. Low latency: RTOS aims to provide low latency. The time taken between receiving an event and starting the execution of the corresponding task is very less. This is important for real time systems.
5. Memory management: RTOS provides memory management to dynamically allocate memory to tasks. It provides mechanisms to avoid memory fragmentation and unused memory wastage.

### Disadvantages:

1. Complex: RTOS is complex software which increases the size of the code and complexity of the system. This may affect the performance of the system.
2. Preemption overhead: In case of preemptive scheduling, the overhead of task preemption reduces the CPU utilization. This scheduling overhead has to be minimized.
3. Priority Inversion: Priority Inversion is a problem in which a high priority task is blocked by a low priority task leading to deadlock. This has to be avoided using priority inheritance protocol.
4. Resource sharing: Proper mechanisms have to be implemented to share resources between multiple tasks. This requires the use of resources locking and synchronization techniques.
5. Cost: The commercial RTOS may increase the cost of the product as licensing fees have to be paid. However, there are many open source RTOS available with minimal or no cost.