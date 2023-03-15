### Schedulers for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

Schedulers are responsible for allocating system resources, including the CPU, to processes. There are three types of schedulers in an operating system:

1. **Long-term scheduler**: This scheduler determines which processes are admitted to the ready queue. It controls the degree of multiprogramming, or the number of processes that are in memory at the same time.

2. **Short-term scheduler**: This scheduler selects which process from the ready queue will be executed next by the CPU. It is also known as the CPU scheduler.

3. **Medium-term scheduler**: This scheduler is responsible for temporarily removing processes from main memory and placing them on secondary storage, such as a hard disk, to reduce the degree of multiprogramming. This process is known as swapping.

Schedulers use various algorithms to determine which process should be allocated resources next. Some common scheduling algorithms include First-Come, First-Served (FCFS), Shortest Job First (SJF), and Round Robin (RR). Each algorithm has its own advantages and disadvantages, and the choice of algorithm depends on the specific requirements of the system.