### Process Transition Diagram for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- CPU scheduling is a process that allows one process to use the CPU while the execution of another process is on hold (in waiting state) due to unavailability of any resource like I/O etc, thereby making full use of CPU.
- The aim of CPU scheduling is to make the system efficient, fast, and fair.
- A process is an instance of a program in execution. A process can have one of the following states :
  - **New**: The process is being created.
  - **Ready**: The process is waiting to be assigned to a CPU.
  - **Running**: The process is executing on a CPU.
  - **Waiting**: The process is waiting for some event to occur, such as an I/O completion.
  - **Terminated**: The process has finished execution.
- A process state transition diagram shows how a process changes states in response to certain events . The following diagram is an example of a process state transition diagram:

![Process state transition diagram](https://docs.oracle.com/cd/E19683-01/816-5042/psched-16/figures/psched-2.gif)

- The arrows show how the process changes states. A process is running if the process is assigned to a CPU. A process can be preempted by the CPU scheduler if another process has higher priority or if the current process has used up its allocated time slice. A process can be blocked by the operating system if it requests an I/O operation or a resource that is not available. A process can be unblocked by the operating system if the event or resource it was waiting for becomes available. A process can be terminated by the operating system if it completes its execution or if it encounters an error.
- The process state transition diagram is useful for understanding the behavior and performance of the CPU scheduler, which is responsible for selecting the next process to run on the CPU.
- The process state transition diagram is also related to the process control block (PCB), which is a data structure that contains information about a process, such as its state, priority, CPU registers, memory allocation, I/O status, etc. The PCB is updated by the operating system whenever a process changes state. The PCB is also used by the CPU scheduler to select the next process to run on the CPU.
- The process state transition diagram can vary depending on the type of CPU scheduling algorithm used by the operating system, such as first-come first-served (FCFS), shortest job first (SJF), priority, round robin, etc. Different CPU scheduling algorithms have different criteria and objectives for selecting the next process to run on the CPU, such as minimizing waiting time, maximizing CPU utilization, ensuring fairness, etc. The process state transition diagram can help to analyze and compare the advantages and disadvantages of different CPU scheduling algorithms.