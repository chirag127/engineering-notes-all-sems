## Unit 3 - CPU Scheduling

CPU scheduling is the process of determining which process in the ready queue is to be allocated the CPU. There are several different CPU scheduling algorithms that can be used to determine the order in which processes are executed. Some of the most common algorithms include:

1. **First-Come, First-Served (FCFS):** This is the simplest scheduling algorithm. Processes are executed in the order in which they arrive in the ready queue.

2. **Shortest Job First (SJF):** This algorithm selects the process with the shortest estimated run time to execute next. This can be either preemptive or non-preemptive.

3. **Priority Scheduling:** In this algorithm, each process is assigned a priority. The process with the highest priority is executed next. This can also be either preemptive or non-preemptive.

4. **Round Robin:** This algorithm assigns a time quantum to each process in the ready queue. The CPU is then allocated to the first process in the queue for that time quantum. If the process does not complete within the time quantum, it is moved to the end of the queue and the next process is allocated the CPU.

5. **Multilevel Queue:** This algorithm partitions the ready queue into several separate queues. Each queue has its own scheduling algorithm. Processes are assigned to a queue based on their characteristics, such as memory requirements or priority.

Each of these algorithms has its own advantages and disadvantages, and the choice of algorithm will depend on the specific requirements of the system. It is important to carefully evaluate the needs of the system and choose the most appropriate algorithm to ensure efficient and effective CPU scheduling.