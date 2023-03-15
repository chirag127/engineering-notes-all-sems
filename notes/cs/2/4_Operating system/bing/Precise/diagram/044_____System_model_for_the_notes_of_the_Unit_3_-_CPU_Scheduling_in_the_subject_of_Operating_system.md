### System Model

A system model is a representation of the system that is used to study and understand its behavior. In the context of CPU scheduling, the system model is used to represent the behavior of the CPU and the processes that are being executed.

The system model for CPU scheduling typically includes the following components:

1. **CPU:** The central processing unit is responsible for executing instructions of the processes.
2. **Process:** A process is a program in execution. It consists of the program code, data, and the current state of the program.
3. **Ready Queue:** The ready queue is a list of processes that are ready to be executed by the CPU. These processes have been loaded into memory and are waiting for the CPU to become available.
4. **Scheduler:** The scheduler is responsible for selecting the next process to be executed by the CPU. It uses a scheduling algorithm to determine which process should be selected from the ready queue.
5. **Dispatcher:** The dispatcher is responsible for switching the CPU from one process to another. It saves the state of the current process and loads the state of the next process to be executed.

These components interact with each other to manage the execution of processes on the CPU. The scheduler selects the next process to be executed, the dispatcher switches the CPU to the selected process, and the CPU executes the instructions of the process. When the process completes or is interrupted, the CPU becomes available and the scheduler selects the next process to be executed.