# Task States for the Notes of the Unit 3 - Real Time Kernel Basics

- A task is a basic unit of execution in a real time operating system (RTOS).
- A task can have different states depending on its current status and priority.
- The fundamental task states are:
  - **Current**: The task that is currently running on the processor. Only one task can be in this state at any time.
  - **Ready**: The task that is ready to run but is waiting for the processor to be available. A task can become ready when it is created, resumed, or unblocked by an event. A ready task can preempt a lower priority current task if the RTOS supports preemption.
  - **Suspended**: The task that is temporarily stopped from running and is not eligible for scheduling. A task can become suspended when it is explicitly paused by the application or the RTOS. A suspended task can be resumed by the application or the RTOS.
  - **Blocked**: The task that is waiting for an event to occur, such as a timer, a semaphore, a message, or an interrupt. A task can become blocked when it explicitly requests an event or a resource that is not available. A blocked task can be unblocked by the occurrence of the event or the availability of the resource.
- Some RTOS may have additional task states, such as :
  - **Zombie**: The task that has terminated its execution but has not been deleted by the RTOS. A zombie task can be deleted by the RTOS or the application.
  - **Interruptible**: The task that is running in kernel space and can be interrupted by a higher priority task or an interrupt. An interruptible task can resume its execution after the interruption is handled.
  - **Uninterruptible**: The task that is running in kernel space and cannot be interrupted by any other task or interrupt. An uninterruptible task can only be preempted by a non-maskable interrupt (NMI) or a system reset. An uninterruptible task should finish its execution as soon as possible to avoid blocking the system.
- The task state can be represented by a state diagram, such as the following:

![Task State Diagram](https://www.freertos.org/TaskStates.png)

- The task state can be changed by the RTOS scheduler, which is responsible for selecting the next task to run based on the task priority, the task state, and the system events.
- The task state can also be changed by the task itself, which can perform various operations, such as:
  - **Create**: The task can create a new task with a specified priority and parameters. The new task can be in ready or suspended state depending on the RTOS configuration.
  - **Delete**: The task can delete itself or another task. The deleted task can be in zombie state until it is removed by the RTOS.
  - **Suspend**: The task can suspend itself or another task. The suspended task can be resumed by the task or the RTOS.
  - **Resume**: The task can resume a suspended task. The resumed task can be in ready or blocked state depending on the RTOS configuration and the events.
  - **Yield**: The task can voluntarily relinquish the processor to allow another ready task to run. The yielded task can be in ready state until it is scheduled again by the RTOS.
  - **Delay**: The task can delay its execution for a specified amount of time. The delayed task can be in blocked state until the time expires or it is unblocked by the RTOS or an event.
  - **Wait**: The task can wait for an event or a resource to occur or become available. The waiting task can be in blocked state until the event or the resource is available or it is unblocked by the RTOS or another event.
  - **Signal**: The task can signal an event or a resource to another task or the RTOS. The signaling task can be in current or ready state depending on the RTOS configuration and the events. The signaled task can be in ready or blocked state depending on the RTOS configuration and the events.