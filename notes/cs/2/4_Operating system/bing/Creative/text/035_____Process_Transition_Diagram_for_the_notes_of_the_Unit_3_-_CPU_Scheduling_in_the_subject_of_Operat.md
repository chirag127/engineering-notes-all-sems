### Process Transition Diagram for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- A process transition diagram is a graphical representation of the possible states of a process and the transitions between them .
- A process state is a condition or a mode that a process can be in during its execution.
- The basic process states are:
  - **New**: The process is being created .
  - **Ready**: The process is waiting to be assigned to a CPU  .
  - **Running**: The process is executing on a CPU  .
  - **Waiting**: The process is waiting for some event to occur, such as an I/O completion or a signal  .
  - **Terminated**: The process has finished its execution .
- The process transition diagram shows how a process can move from one state to another, depending on the actions of the CPU scheduler, the process itself, and the external events .
- The CPU scheduler is the component of the operating system that decides which process should run on the CPU at any given time  .
- The CPU scheduler uses different algorithms and policies to select the next process to run, such as first-come first-served, shortest job first, priority-based, round-robin, etc  .
- The CPU scheduler maintains different queues for different process states, such as the ready queue, the waiting queue, the device queue, etc  .
- The CPU scheduler can also be classified into different types, such as long-term, medium-term, and short-term schedulers, depending on the frequency and scope of their decisions .
- The process transition diagram can be used to illustrate the behavior and performance of different CPU scheduling algorithms and policies .
- The process transition diagram can also be used to show the impact of context switching, which is the process of saving and restoring the state of a process when it is switched from running to ready or waiting, or vice versa  .
- The process transition diagram can be drawn as follows:

![Process Transition Diagram](https://docs.oracle.com/cd/E19683-01/816-5042/psched-16/figures/psched-2.gif)

: https://www.tutorialspoint.com/what-is-process-scheduling
: https://docs.oracle.com/cd/E19683-01/816-5042/psched-16/index.html
: https://www.guru99.com/process-scheduling.html
: https://www.geeksforgeeks.org/cpu-scheduling-gq/
: https://www.geeksforgeeks.org/process-table-and-process-control-block-pcb/
: https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/techpaper/vmware-vsphere-cpu-sched-performance-white-paper.pdf