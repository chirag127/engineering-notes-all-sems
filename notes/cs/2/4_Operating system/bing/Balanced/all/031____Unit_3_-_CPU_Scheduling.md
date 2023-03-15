# Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling is done by the CPU scheduler, which is a part of the operating system kernel.
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
  - In preemptive scheduling, the CPU can be taken away from a running process by the scheduler if a higher priority process arrives or a certain time quantum expires .
  - In non-preemptive scheduling, the CPU cannot be taken away from a running process until it completes or voluntarily relinquishes the CPU .
- CPU scheduling algorithms are the methods used by the CPU scheduler to select a process from the ready queue and allocate the CPU to it .
- Some of the common CPU scheduling algorithms are :
  - First Come First Serve (FCFS): The process that arrives first in the ready queue is selected for execution .
  - Shortest Job First (SJF): The process that has the shortest burst time (the time required to complete its execution) is selected for execution .
  - Priority Scheduling: The process that has the highest priority is selected for execution .
  - Round Robin (RR): The processes are executed in a circular order, each for a fixed time slice called quantum .
  - Multilevel Queue (MLQ): The processes are divided into different queues based on their characteristics, and each queue has its own scheduling algorithm .
  - Multilevel Feedback Queue (MLFQ): The processes are divided into different queues based on their characteristics, and each queue has its own scheduling algorithm, but the processes can move between the queues based on their behavior .
- CPU scheduling algorithms can be evaluated based on different criteria, such as CPU utilization, throughput, turnaround time, waiting time, response time, and fairness .
- CPU scheduling algorithms can be implemented using different data structures, such as arrays, linked lists, queues, heaps, and trees .
- CPU scheduling can be influenced by other factors, such as process synchronization, memory management, I/O management, and multiprocessor systems .