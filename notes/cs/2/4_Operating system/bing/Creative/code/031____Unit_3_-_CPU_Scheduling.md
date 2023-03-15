## Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling is the process of temporarily suspending a running process before it completes its CPU burst and allocating the CPU to another process of higher priority .
  - Non-preemptive scheduling is the process of allocating the CPU to a specific process until it finishes its CPU burst or requests for I/O .
- There are different types of CPU scheduling algorithms, each with different criteria and objectives . Some of the common algorithms are:
  - First Come First Serve (FCFS): This is the simplest algorithm that assigns the CPU to the process that arrives first in the ready queue . It is non-preemptive and has a high average waiting time .
  - Shortest Job First (SJF): This is the algorithm that assigns the CPU to the process that has the shortest CPU burst in the ready queue . It can be preemptive or non-preemptive and has a low average waiting time .
  - Priority Scheduling: This is the algorithm that assigns the CPU to the process that has the highest priority in the ready queue . It can be preemptive or non-preemptive and may cause starvation for low priority processes .
  - Round Robin (RR): This is the algorithm that assigns the CPU to the process that is at the front of the ready queue for a fixed time quantum . It is preemptive and has a low response time for interactive processes .
  - Multilevel Queue (MLQ): This is the algorithm that divides the ready queue into several subqueues, each with its own scheduling algorithm . It is suitable for systems with different types of processes, such as system processes, interactive processes, and batch processes .
  - Multilevel Feedback Queue (MLFQ): This is the algorithm that allows a process to move between different subqueues of the ready queue based on its behavior and characteristics . It is adaptive and flexible for various types of processes .
- Processor scheduling is the process of configuring the system to optimize the performance of the CPU for different types of tasks, such as programs or background services. It can be done by adjusting the settings in the System Properties of Windows 11/10.