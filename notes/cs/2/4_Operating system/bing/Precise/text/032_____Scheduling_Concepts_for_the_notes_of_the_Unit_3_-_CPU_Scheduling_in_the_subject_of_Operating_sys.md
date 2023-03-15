### Scheduling Concepts

1. **CPU Scheduling:** CPU scheduling is the process of selecting a process from the ready queue and allocating the CPU to it. The goal of CPU scheduling is to maximize CPU utilization and throughput while minimizing response time and waiting time.

2. **Preemptive and Non-Preemptive Scheduling:** In preemptive scheduling, the CPU can be taken away from a process before it completes its CPU burst. In non-preemptive scheduling, the CPU is allocated to a process until it completes its CPU burst or voluntarily releases the CPU.

3. **Scheduling Criteria:** There are several criteria to consider when evaluating a CPU scheduling algorithm, including CPU utilization, throughput, turnaround time, waiting time, and response time.

4. **Scheduling Algorithms:** There are several scheduling algorithms, including First-Come, First-Served (FCFS), Shortest Job First (SJF), Priority Scheduling, Round Robin (RR), and Multilevel Queue Scheduling.

5. **Context Switch:** A context switch is the process of saving the state of the currently running process and restoring the state of the next process to run. Context switches are necessary when switching between processes, but they incur overhead and can affect system performance.

6. **Dispatcher:** The dispatcher is the module that gives control of the CPU to the process selected by the short-term scheduler. The dispatcher performs the context switch, switching the CPU to the selected process's context.

7. **Process State:** A process can be in one of several states, including new, ready, running, waiting, and terminated. The state of a process changes as it is created, selected for execution, waits for resources, and completes execution.

8. **Process Control Block (PCB):** The PCB is a data structure that contains information about a process, including its state, program counter, CPU registers, and memory management information. The PCB is used by the operating system to manage the process and perform context switches.

9. **Thread Scheduling:** Threads are lightweight processes that share the same address space and resources. Thread scheduling is the process of selecting a thread from the ready queue and allocating the CPU to it. Thread scheduling can be performed at the user level or the kernel level.

10. **Multiprocessor Scheduling:** Multiprocessor scheduling is the process of scheduling processes and threads on a system with multiple CPUs. Multiprocessor scheduling can be performed using a centralized approach, where a single queue is used for all CPUs, or a decentralized approach, where each CPU has its own queue.