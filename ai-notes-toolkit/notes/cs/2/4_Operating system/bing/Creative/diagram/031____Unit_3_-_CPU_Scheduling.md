## Unit 3 - CPU Scheduling

- CPU scheduling is the process of deciding which process will own the CPU for execution while another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU .
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- CPU scheduling can be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling is when the CPU can be taken away from a running process by the scheduler before the process completes its execution .
  - Non-preemptive scheduling is when the CPU cannot be taken away from a running process until the process voluntarily releases the CPU or terminates .
- CPU scheduling algorithms are the methods of choosing which process will get the CPU next based on some criteria .
- Some of the common CPU scheduling algorithms are:
  - First Come First Serve (FCFS): This algorithm selects the process that arrives first in the ready queue and allocates the CPU to it until it finishes or blocks .
  - Shortest Job First (SJF): This algorithm selects the process that has the shortest estimated CPU burst time and allocates the CPU to it until it finishes or blocks .
  - Priority Scheduling: This algorithm selects the process that has the highest priority and allocates the CPU to it until it finishes or blocks .
  - Round Robin (RR): This algorithm allocates the CPU to each process in the ready queue for a fixed time quantum and then moves it to the end of the queue if it does not finish or block within the quantum .
  - Multilevel Queue Scheduling: This algorithm partitions the ready queue into several subqueues, each with its own scheduling algorithm, and selects a process from the subqueue with the highest priority .
  - Multilevel Feedback Queue Scheduling: This algorithm is similar to multilevel queue scheduling, but allows processes to move between subqueues based on their behavior and characteristics .
- CPU scheduling can be configured for better performance in Windows 11/10 by adjusting the processor scheduling option in the system properties.
  - The processor scheduling option allows the user to choose whether to optimize the system for programs or for background services.
  - Programs option gives more CPU time to the foreground applications, while background services option gives more CPU time to the background processes.
  - The default option is programs, which is suitable for most users.