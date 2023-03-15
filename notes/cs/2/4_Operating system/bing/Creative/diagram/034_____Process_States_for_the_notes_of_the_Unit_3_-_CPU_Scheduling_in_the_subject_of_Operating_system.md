Hello, I am Sydney, your AI assistant. I can help you with your topic of process states in operating system. Here is a summary of the topic in markdown format:

### Process States
- A process is a program in execution that has its own process control block (PCB) and requires resources like CPU, memory, disk, and I/O .
- A process can be in one of the following states at any instant of time   :
  - New: The process is being created but not yet loaded into the main memory. It is the program that is present in the secondary memory that will be picked up by the OS to create the process.
  - Ready: The process is loaded into the main memory and is waiting for the CPU to be allocated. It is placed in the ready queue and competes with other processes for the CPU time  .
  - Running: The process is selected for execution and is running on one of the CPUs or cores of the system. There can be at most one running process per CPU or core. A process can run in either user mode or kernel mode. In user mode, the process executes its own instructions and has limited access to system resources. In kernel mode, the process executes the OS instructions and has full access to system resources.
  - Waiting: The process is waiting for some event to occur, such as an I/O completion, a signal, a timer, or a resource availability. It is placed in the waiting queue and cannot use the CPU until the event occurs  .
  - Terminated: The process has completed its execution and is removed from the system. It releases all the resources it has acquired and returns the exit status to the OS  .
- A process can change its state due to various events or actions, such as:
  - Admission: The OS creates a new process and moves it from the new state to the ready state .
  - Dispatch: The OS selects a process from the ready queue and moves it from the ready state to the running state  .
  - Interrupt: The OS suspends the execution of a running process due to an external event, such as a hardware interrupt, a system call, or a preemption, and moves it from the running state to the ready state  .
  - I/O or event wait: The running process requests an I/O operation or waits for an event to occur, and moves from the running state to the waiting state  .
  - I/O or event completion: The event that the waiting process is waiting for occurs, and the OS moves it from the waiting state to the ready state  .
  - Exit: The running process finishes its execution and moves from the running state to the terminated state  .
- A process state diagram is a graphical representation of the possible states of a process and the transitions between them. An example of a process state diagram is shown below:

![Process state diagram](https://www.guru99.com/images/1/020221_0726_ProcessMana1.png)

: Process Management in OS: PCB in Operating System - Guru99
: States of a Process in Operating Systems - GeeksforGeeks
: What are the process states in Windows and Linux? - tutorialspoint.com
: Process state - Wikipedia
: OS Process States - javatpoint