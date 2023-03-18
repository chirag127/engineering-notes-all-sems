### System Model for the Notes of the Unit 3 - CPU Scheduling in the Subject of Operating System

CPU scheduling is an important concept in the subject of Operating System. It involves the allocation of CPU time to different processes in a system. In order to understand CPU scheduling, it is important to have a clear understanding of the system model. The following points provide a brief overview of the system model for the notes of the Unit 3 - CPU Scheduling:

- **Process**: A process is a program in execution. It consists of a set of instructions, data, and a program counter. A process can be in various states such as running, waiting, or ready.

- **CPU**: The CPU is the central processing unit of a computer. It executes instructions of a process and switches between different processes according to the CPU scheduling algorithm.

- **Scheduler**: The scheduler is responsible for selecting the next process to be executed by the CPU. It uses a scheduling algorithm to determine which process should be given CPU time.

- **Dispatcher**: The dispatcher is responsible for giving control of the CPU to the selected process. It saves the state of the currently running process and loads the state of the selected process.

- **Context Switch**: A context switch is the process of saving the state of the currently running process and restoring the state of the selected process. It involves saving and restoring the values of the program counter, registers, and other CPU state information.

- **Ready Queue**: The ready queue is a queue of processes that are ready to be executed by the CPU. The scheduler selects the next process from the ready queue.

- **Blocking Queue**: The blocking queue is a queue of processes that are waiting for an event such as an I/O operation to complete. Processes in the blocking queue cannot be executed by the CPU until the event they are waiting for has occurred.

- **CPU Burst**: A CPU burst is the amount of time a process spends executing on the CPU before it is interrupted by the scheduler. CPU bursts are typically short and are followed by periods of waiting for I/O operations to complete.

In conclusion, the system model for CPU scheduling involves a set of processes, a CPU, a scheduler, a dispatcher, and various queues. The scheduler selects the next process to be executed by the CPU based on a scheduling algorithm, and the dispatcher gives control of the CPU to the selected process. Understanding the system model is essential for understanding CPU scheduling and its importance in the operating system.