# System Model for CPU Scheduling

- CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU.
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling is the foundation or starting concept of multi-programmed operating systems (OSs). By toggling the CPU with different processes, the operating system can make the computer and its processing power more productive.
- A system model for CPU scheduling consists of the following components:
  - CPU: The central processing unit that executes the instructions of the processes.
  - Ready Queue: A list of processes that are ready to execute on the CPU. The processes are stored in the order of their arrival or priority.
  - Dispatcher: A module that gives control of the CPU to the process selected by the CPU scheduler.
  - CPU Scheduler: A module that selects one of the processes from the ready queue to run on the CPU, based on a certain algorithm or policy.
- The system model for CPU scheduling can be represented by the following diagram:

```
+--------+     +------------+     +--------+
|        |     |            |     |        |
|  CPU   |<--->| Dispatcher |<--->|  CPU   |
|        |     |            |     |        |
+--------+     +------------+     +--------+
                         ^
                         |
                         |
                         v
                   +------------+
                   |            |
                   | CPU        |
                   | Scheduler  |
                   |            |
                   +------------+
                         ^
                         |
                         |
                         v
                   +------------+
                   |            |
                   | Ready      |
                   | Queue      |
                   |            |
                   +------------+
```
- The CPU scheduler can use different algorithms or policies to select the next process to run on the CPU, such as:
  - First Come First Serve (FCFS): The process that arrives first in the ready queue is selected to run on the CPU.
  - Shortest Job First (SJF): The process that has the shortest estimated burst time (the time required to complete its execution) is selected to run on the CPU.
  - Longest Job First (LJF): The process that has the longest estimated burst time is selected to run on the CPU.
  - Priority Scheduling: The process that has the highest priority (a predefined value assigned to each process) is selected to run on the CPU.
  - Round Robin (RR): The processes are selected to run on the CPU in a circular order, with each process getting a fixed amount of time (called quantum) to use the CPU.
- The CPU scheduler can be classified into three types, based on the frequency of their execution:
  - Long-term scheduler: It decides which processes to admit into the system for execution. It controls the degree of multiprogramming (the number of processes in memory). It runs infrequently and may be invoked once every few minutes or hours.
  - Medium-term scheduler: It decides which processes to swap out of the main memory to the secondary storage (such as disk) to create space for new processes. It controls the size of the working set (the set of pages that a process is currently using). It runs more frequently than the long-term scheduler and may be invoked once every few seconds or minutes.
  - Short-term scheduler: It decides which process to run on the CPU next. It controls the CPU utilization and response time of the processes. It runs very frequently and may be invoked once every few milliseconds.