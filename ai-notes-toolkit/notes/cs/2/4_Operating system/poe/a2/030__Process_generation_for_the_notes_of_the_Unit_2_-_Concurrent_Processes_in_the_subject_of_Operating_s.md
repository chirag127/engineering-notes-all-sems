 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Process generation for the notes of the Unit 2 - Concurrent Processes in the subject of Operating system.

1. Process creation: A process is created when a program is executed. The operating system loads the program into memory and starts executing it.

2. Process termination: A process terminates when its task is completed or it is aborted by the operating system due to an error condition. The process execution may either complete successfully or terminate with an error. The operating system reclaims all the resources allocated to the terminated process.

3. Process states: A process transitions between the following states:

- New: The process is created but not yet executing.
- Running: Instructions are being executed.
- Waiting: The process is waiting for some event to occur.
- Ready: The process is ready to execute.
- Terminated: The process has finished execution.

4. Context Switch: When a running process switches to the waiting state, the operating system switches the CPU to another ready process. This is called a context switch. The state of the old process is saved in its Process Control Block (PCB) and the state of the new process is loaded from its PCB. This allows the new process to begin or resume execution immediately. Frequent context switches can create overhead and reduce performance.

5. Process Scheduling: The operating system must schedule processes to allocate the limited system resources to processes. The goals of process scheduling are:

- Maximize processor utilization.
- Maximize throughput.
- Maximize response time.
- Avoid starvation.
- Ensure fairness.

Scheduling algorithms include first-come, first-served, shortest job first, priority scheduling, and round-robin. The chosen algorithm depends upon the goals and workload.