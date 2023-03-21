### System model for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

The following points describe the system model for CPU scheduling:

- The system consists of a set of identical, independent processes, each with its own CPU burst time.
- Each process enters the system at a random time and must be scheduled to run on the CPU.
- The CPU executes only one process at a time, and each process is executed in a sequential manner.
- The CPU scheduler selects the next process to run based on a scheduling algorithm.
- The selected process is then dispatched to the CPU for execution.
- The CPU executes the process for a certain amount of time, known as the time quantum, and then interrupts the process to allow other processes to run.
- The interrupted process is then placed back into the ready queue, where it waits for its next turn on the CPU.
- The scheduling algorithm is designed to maximize system performance by minimizing the waiting time and turnaround time of each process.
- The system also includes a set of I/O devices, which are used by processes to perform input and output operations.
- When a process needs to perform an I/O operation, it is blocked and placed into the blocked queue until the operation is complete.
- Once the operation is complete, the process is moved back into the ready queue and waits for its turn on the CPU.
- The system also includes a set of system processes, such as the CPU scheduler, which are responsible for managing the overall system operation.
- The system model assumes that all processes are well-behaved and do not attempt to interfere with other processes or the operating system itself.

Overall, the system model for CPU scheduling provides a framework for understanding how processes are scheduled to run on the CPU and how I/O operations are handled. By understanding this model, we can design better scheduling algorithms that improve system performance and reduce the waiting and turnaround time of each process.