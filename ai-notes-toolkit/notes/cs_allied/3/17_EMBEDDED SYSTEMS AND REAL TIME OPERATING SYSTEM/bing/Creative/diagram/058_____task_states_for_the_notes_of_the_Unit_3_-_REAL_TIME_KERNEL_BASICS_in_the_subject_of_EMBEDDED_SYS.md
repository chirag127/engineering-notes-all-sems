### Task States

- A task is a unit of execution in a real time operating system (RTOS).
- A task can have different states depending on its status and priority.
- The fundamental task states are:
  - **Current**: The task that is currently running on the processor. Only one task can be in this state at any time.
  - **Ready**: The tasks that are ready to run but are waiting for the processor to be available. They are placed in a run queue according to their priority.
  - **Blocked**: The tasks that are waiting for some event or resource to become available. They are placed in a wait queue according to their priority and timeout value.
  - **Suspended**: The tasks that are temporarily stopped by the user or the system. They are not placed in any queue and cannot be scheduled until they are resumed.
  - **Terminated**: The tasks that have completed their execution or have been killed by the user or the system. They are removed from the system and their resources are freed.
- A task can change its state due to various reasons, such as:
  - **Creation**: A new task is created and placed in the ready state.
  - **Preemption**: A higher priority task becomes ready and preempts the current task, which is moved to the ready state.
  - **Yield**: The current task voluntarily relinquishes the processor and is moved to the ready state.
  - **Delay**: The current task requests a delay and is moved to the blocked state with a timeout value.
  - **Event**: The current task waits for an event (such as a semaphore, a message, or an interrupt) and is moved to the blocked state. A blocked task can be unblocked by the occurrence of the event or by a timeout.
  - **Suspend**: The current task is suspended by the user or the system and is moved to the suspended state.
  - **Resume**: A suspended task is resumed by the user or the system and is moved to the ready state.
  - **Terminate**: The current task finishes its execution or is terminated by the user or the system and is moved to the terminated state.
- A task state diagram shows the possible transitions between the task states and the events that cause them. An example of a task state diagram is shown below:

![Task State Diagram](https://i.imgur.com/9XZfQ2T.png)