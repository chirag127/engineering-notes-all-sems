### Scheduling Concepts

CPU scheduling is a process which allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU. The aim of CPU scheduling is to make the system efficient, fast and fair.

1. **Dispatcher**: The dispatcher is the module that gives control of the CPU to the process selected by the short-term scheduler. This function involves the following:
    - Switching context
    - Switching to user mode
    - Jumping to the proper location in the user program to restart that program
2. **Scheduling Criteria**: Different CPU scheduling algorithms have different properties, and the choice of a particular algorithm may favor one class of processes over another. In choosing which algorithm to use in a given situation, we must consider the properties of the various algorithms. Many criteria have been suggested for comparing CPU scheduling algorithms. Which characteristics are used for comparison can make a substantial difference in which algorithm is judged to be best. The criteria include the following:
    - CPU utilization
    - Throughput
    - Turnaround time
    - Waiting time
    - Response time
3. **Scheduling Algorithms**: A variety of CPU scheduling algorithms are used by systems. These algorithms are either preemptive or non-preemptive. Preemptive scheduling is based on priority where a scheduler may preempt a low priority running process anytime when a high priority process enters into a ready queue. Non-preemptive scheduling is based on the concept that once the CPU has been allocated to a process, the process keeps the CPU until it releases the CPU either by terminating or by switching to the waiting state.
    - First-Come, First-Served (FCFS) Scheduling
    - Shortest-Job-First (SJF) Scheduling
    - Priority Scheduling
    - Round Robin (RR) Scheduling
    - Multilevel Queue Scheduling
    - Multilevel Feedback Queue Scheduling
4. **Multiple-Processor Scheduling**: CPU scheduling more complex when multiple CPUs are available. The issue is how to assign processes to processors. There are two approaches to this issue: asymmetric multiprocessing and symmetric multiprocessing (SMP). In asymmetric multiprocessing, the master processor schedules and allocates work to slave processors. In SMP, each processor is self-scheduling, all processes in common ready queue, or each has its own private queue of ready processes.
5. **Real-Time Scheduling**: The scheduling algorithm must support a real-time operating system. A real-time operating system is a multitasking operating system that aims at executing real-time applications. Real-time systems are used when there are rigid time requirements on the operation of a processor or the flow of data, and thus are often used as control devices in dedicated applications. Real-time systems can be either hard or soft real-time.