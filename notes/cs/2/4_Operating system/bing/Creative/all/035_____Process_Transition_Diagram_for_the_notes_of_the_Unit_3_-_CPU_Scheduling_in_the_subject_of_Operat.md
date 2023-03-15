# Process Transition Diagram for CPU Scheduling

- A process transition diagram is a graphical representation of the possible states of a process and the transitions between them in an operating system.
- A process state is a condition or mode that a process can be in, such as ready, running, waiting, or terminated.
- A process can change its state due to various events, such as CPU allocation, I/O completion, timer expiration, or termination.
- A process transition diagram helps to understand the behavior and life cycle of a process, as well as the scheduling policies and algorithms that manage the process execution.
- A typical process transition diagram for CPU scheduling is shown below :

![Process Transition Diagram](https://docs.oracle.com/cd/E19683-01/816-5042/psched-16/psched-16-img001.gif)

- The diagram consists of five states and six transitions:
  - **New**: The process is being created and has not yet been admitted to the ready queue.
  - **Ready**: The process is waiting in the ready queue for CPU allocation.
  - **Running**: The process is executing on a CPU.
  - **Waiting**: The process is blocked on some I/O event or resource request.
  - **Terminated**: The process has completed its execution and is being removed from the system.
  - **Admit**: The transition from new to ready state, when the process is admitted to the ready queue by the long-term scheduler.
  - **Dispatch**: The transition from ready to running state, when the process is selected by the short-term scheduler and assigned to a CPU.
  - **Timeout**: The transition from running to ready state, when the process is preempted by the CPU scheduler due to a timer interrupt or a higher priority process.
  - **Event wait**: The transition from running to waiting state, when the process voluntarily relinquishes the CPU due to an I/O request or a resource wait.
  - **Event occurs**: The transition from waiting to ready state, when the process is unblocked by the completion of the I/O event or the availability of the resource.
  - **Exit**: The transition from running to terminated state, when the process finishes its execution and releases all its resources.

- The process transition diagram can also include other states and transitions, depending on the specific features and policies of the operating system, such as suspended, zombie, fork, exec, signal, etc  .