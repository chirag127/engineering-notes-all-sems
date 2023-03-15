### Process States

In the subject of Operating System, Unit 3 - CPU Scheduling, one of the important topics is Process States. Here are some key points to remember:

1. A process is a program in execution. It is an active entity that requires resources such as CPU time, memory, and input/output devices to complete its task.

2. A process can be in one of several states during its lifetime. These states include new, ready, running, waiting, and terminated.

3. The **new** state represents a process that has just been created but has not yet been admitted to the ready queue.

4. The **ready** state represents a process that is waiting to be assigned to a processor. Processes in the ready state are placed in the ready queue.

5. The **running** state represents a process that is currently being executed by a processor.

6. The **waiting** state represents a process that is waiting for an event to occur, such as the completion of an I/O operation.

7. The **terminated** state represents a process that has completed its execution and is no longer active.

8. The state of a process can change as it moves through the system. The operating system is responsible for managing these state transitions.

9. A process control block (PCB) is used to store information about the current state of a process, including its program counter, register values, and memory allocation.

10. The scheduler is responsible for selecting processes from the ready queue and assigning them to the processor for execution.
