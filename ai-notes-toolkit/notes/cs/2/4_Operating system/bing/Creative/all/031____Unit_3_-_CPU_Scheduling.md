# Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling is done by the operating system, which can configure the processor scheduling for better performance.
- CPU scheduling can be classified into two types: preemptive and non-preemptive.
  - In preemptive scheduling, the tasks are mostly assigned with their priorities. The CPU can be taken away from a process if a higher priority process arrives in the ready queue.
  - In non-preemptive scheduling, the CPU has been allocated to a specific process. The process keeps the CPU until it releases the CPU either by terminating or by switching to the waiting state.
- There are different types of CPU scheduling algorithms, such as:
  - First Come First Serve (FCFS): This is the simplest of all operating system scheduling algorithms. The process that requests the CPU first is allocated the CPU first.
  - Shortest Job First (SJF): This is a scheduling process that selects the waiting process with the smallest execution time to execute next.
  - Priority Scheduling: This is a scheduling process that assigns a priority to each process, and the process with the highest priority is executed first.
  - Round Robin (RR): This is a scheduling process that assigns a fixed time slice to each process, called a quantum, and the process that uses up its quantum is preempted and added to the end of the ready queue.
  - Multilevel Queue (MLQ): This is a scheduling process that partitions the ready queue into several separate queues, each with its own scheduling algorithm.
  - Multilevel Feedback Queue (MLFQ): This is a scheduling process that allows a process to move between queues based on its behavior and characteristics.