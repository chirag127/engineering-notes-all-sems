### Task States for the Notes of the Unit 3 - Real Time Kernel Basics in the Subject of Embedded Systems and Real Time Operating System

- A task is a basic unit of execution in a real time operating system (RTOS). A task can be a process, a thread, or a coroutine, depending on the implementation of the RTOS.
- A task state is the condition of a task at a given point of time. It indicates whether the task is running, ready, waiting, suspended, or terminated.
- A real time kernel is the core component of an RTOS that manages the tasks and their states, as well as the resources and the interrupts of the system.
- A real time kernel typically supports the following task states:

  - **Running**: The task is currently executing on the processor. Only one task can be in this state at a time, unless the system supports multicore or multiprocessor architectures.
  - **Ready**: The task is eligible to run, but it is not currently running. It is placed in a ready queue, which is a data structure that stores the tasks according to their priorities. The scheduler of the kernel selects the highest priority task from the ready queue to run next.
  - **Waiting**: The task is blocked by an event or a resource that is not available. It is placed in a waiting queue, which is a data structure that stores the tasks according to the event or the resource they are waiting for. The kernel moves the task to the ready queue when the event occurs or the resource becomes available.
  - **Suspended**: The task is temporarily stopped by an external command or a self-request. It is removed from the ready or the waiting queue, and it does not consume any processor time. The kernel resumes the task when the command or the request is reversed.
  - **Terminated**: The task has completed its execution or has been aborted by an error or an exception. It is removed from the system and its resources are freed.

- The task state diagram shows the possible transitions between the task states and the events or the actions that trigger them.

![Task State Diagram](https://i.imgur.com/6k1Y6Xy.png)

- The task state diagram is based on the following assumptions:

  - The system has a single processor and a preemptive scheduler, which means that a higher priority task can interrupt a lower priority task at any time.
  - The system supports dynamic task creation and deletion, which means that new tasks can be created or existing tasks can be deleted at run time.
  - The system supports task suspension and resumption, which means that tasks can be stopped and restarted by external commands or self-requests.
  - The system supports task synchronization and communication, which means that tasks can wait for or signal events, and share or exchange data with other tasks.