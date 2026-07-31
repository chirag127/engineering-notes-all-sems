### Schedulers for the notes of Unit 3 - CPU Scheduling in the subject of Operating System

In the field of Operating System, scheduling plays a vital role in determining the efficiency of the system. It is the process of selecting the process from the ready queue and allocating the CPU to that process. Scheduling is done by the scheduler, which is responsible for managing the flow of processes in the system. In this unit, we will discuss the different types of schedulers used in Operating Systems.

#### 1. Long-term Scheduler

- Also known as the job scheduler.
- It decides which processes should be brought into the ready queue.
- The main objective of the long-term scheduler is to keep the CPU busy all the time.
- It selects processes from the pool of processes waiting in the secondary storage and loads them into the main memory.
- It is a slow process, as it takes a considerable amount of time to load the process into the main memory.

#### 2. Short-term Scheduler

- Also known as the CPU scheduler.
- It selects the process from the ready queue and allocates the CPU to that process.
- The main objective of the short-term scheduler is to minimize the response time, turnaround time, and waiting time of the processes.
- It is a fast process, as it takes a negligible amount of time to allocate the CPU to the process.

#### 3. Medium-term Scheduler

- It is an optional scheduler that lies between the long-term and short-term schedulers.
- It removes the process from the memory and keeps them in the secondary storage.
- It is used when there is a shortage of memory in the system.
- The main objective of the medium-term scheduler is to reduce the degree of multiprogramming.

#### 4. Priority Scheduler

- It is a scheduling algorithm that assigns a priority to each process in the queue.
- The process with the highest priority is allocated the CPU first.
- Priority can be predefined or dynamic, depending on the system's requirements.
- It is important to keep in mind that a high priority process can cause a low priority process to starve.

#### 5. Round Robin Scheduler

- It is a scheduling algorithm that allocates CPU time to the processes in a cyclic manner.
- Each process is allocated a fixed time slice, known as the time quantum.
- When a process exhausts its time quantum, it is preempted, and the next process in the queue is allocated the CPU.
- It provides a fair share of CPU time to all the processes in the system.

#### 6. Multilevel Queue Scheduler

- It is a scheduling algorithm that divides the ready queue into multiple levels.
- Each level is assigned a different priority based on the type of process it contains.
- Processes with higher priorities are allocated the CPU first.
- It is used in systems where different types of processes require different amounts of CPU time.

In conclusion, scheduling is an important aspect of the Operating System, as it determines the efficiency of the system. The scheduler plays a crucial role in managing the flow of processes in the system. The different types of schedulers discussed in this unit provide various advantages and are used based on the system's requirement.