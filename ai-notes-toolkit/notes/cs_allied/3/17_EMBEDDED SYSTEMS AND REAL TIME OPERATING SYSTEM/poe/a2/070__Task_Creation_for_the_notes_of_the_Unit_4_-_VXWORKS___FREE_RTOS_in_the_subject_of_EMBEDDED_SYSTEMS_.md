 Here is the content in markdown format without any emojis or external links:

### Task Creation for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Task is the basic unit of execution in RTOS. It is like a process which is being executed.
- Each task has its own stack, priority, and state.
- Tasks are created using task create system call. This system call takes following arguments:
-- Task entry point: It is the address of the task function. When the task is scheduled to run, task function is executed.
-- Task priority: It defines the importance of the task. Higher priority task gets preference over lower priority task.
-- Task stack size: It defines the size of stack required by the task. The task stack holds the local variables and partial results.
-- Task name: It is the name given to the task. It is used for debugging and tracking the task.
- Tasks can be in ready, running, waiting, timeout or suspended state.
- Context switching happens when a task changes its state from running to waiting or ready. The context of the running task is stored and the context of the new task to run is loaded. This is efficiently done by RTOS.
- Various task synchronization mechanisms like semaphores, mutexes, message passing, etc. are provided by the RTOS to coordinate between tasks.

The content is written in formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.