 Here is the markdown content for the given topic:

### Process Transition Diagram for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. New: The process is being created.
2. Ready: The process is ready to be executed but waiting for the CPU.
3. Running: The process is being executed by the CPU.
4. Waiting: The process is waiting for some event to occur or resource to become available. e.g. I/O completion, synchronization variable.
5. Terminated: The process has finished execution.

The process transitions between the states as follows:

1. New -> Ready: When the process is created and is ready to execute, it enters the ready state.
2. Ready -> Running: The scheduler selects a process from the ready queue and allocates the CPU to it.
3. Running -> Ready: Due to the interrupts or preemption, the running process goes to ready state.
4. Running -> Waiting: Due to the I/O or synchronization requests, the running process goes to waiting state.
5. Waiting -> Ready: When the event occurs or resource becomes available, the waiting process goes to ready state.
6. Any state -> Terminated: The process completes its execution and is terminated.

The above diagram and transitions together represent the life cycle of a process and behavior of the CPU scheduling algorithm.