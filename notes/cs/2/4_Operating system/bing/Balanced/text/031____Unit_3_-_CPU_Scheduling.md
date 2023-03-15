## Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
  - In preemptive scheduling, the CPU can be taken away from a running process by the scheduler if a higher priority process arrives or a time quantum expires .
  - In non-preemptive scheduling, the CPU cannot be taken away from a running process until it completes or requests for I/O or terminates .
- Some of the common CPU scheduling algorithms are :
  - First Come First Serve (FCFS): The process that arrives first in the ready queue is selected for execution. It is simple, but may cause long waiting time and low CPU utilization .
  - Shortest Job First (SJF): The process that has the shortest burst time (estimated execution time) in the ready queue is selected for execution. It minimizes the average waiting time, but may cause starvation for longer processes .
  - Priority Scheduling: The process that has the highest priority in the ready queue is selected for execution. It can be preemptive or non-preemptive. It may cause starvation for lower priority processes .
  - Round Robin (RR): The processes in the ready queue are executed in a circular order, with each process getting a fixed time slice (quantum) of CPU. It is fair and responsive, but may cause high context switching overhead and low CPU utilization .
  - Multilevel Queue (MLQ): The processes are divided into different queues based on their characteristics, such as foreground/background, system/user, CPU-bound/I/O-bound, etc. Each queue has its own scheduling algorithm and priority. It allows better process management, but may cause starvation for lower priority queues .
  - Multilevel Feedback Queue (MLFQ): The processes are divided into different queues based on their characteristics, but they can move between the queues based on their behavior, such as CPU usage, waiting time, etc. It allows better process adaptation, but may cause complexity and overhead .