### Process States

Processes are the fundamental building blocks of an Operating System. A process is an instance of a program in execution. A process goes through several phases in its lifetime. These phases are known as process states. In this section, we will discuss the various process states that a process goes through during its lifetime.

#### New State
When a process is first created, it enters the New state. In this state, the process is not yet ready for execution. It is in the queue of processes waiting for the necessary resources to be allocated to it.

#### Ready State
When the necessary resources are allocated to a process, it enters the Ready state. In this state, the process is waiting for the CPU to be assigned to it for execution. The process is in the queue of processes that are ready to be executed.

#### Running State
When the CPU is assigned to a process, it enters the Running state. In this state, the process is being executed by the CPU.

#### Blocked State
When a process is waiting for a resource to become available, it enters the Blocked state. In this state, the process cannot proceed without the resource it is waiting for. The process is in the queue of processes waiting for the resource to become available.

#### Terminated State
When a process completes its execution, it enters the Terminated state. In this state, the process has finished its execution, and its resources are released.

These are the five process states that a process goes through during its lifetime. The transition from one state to another is governed by the CPU scheduling algorithm in the Operating System. Understanding these process states is essential for effective CPU scheduling and resource management in an Operating System.