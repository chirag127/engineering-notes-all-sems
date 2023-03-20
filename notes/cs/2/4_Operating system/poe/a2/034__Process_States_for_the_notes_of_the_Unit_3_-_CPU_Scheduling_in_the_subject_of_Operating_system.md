 Here is the content in markdown format without any emojis or external links and in formal tone:

### Process States for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

1. New: The process is being created.
2. Ready: The process is ready to execute but waiting for CPU.
3. Running: Instructions of the process are being executed by the CPU.
4. Waiting: The process is waiting for some event to occur or for some resource. eg. I/O completion, keyboard input etc.
5. Terminated: The process has finished its task and terminated.

The process transits between the states as per the events and scheduler actions. The ready queue and waiting queue hold the processes in ready and waiting states respectively. The scheduler selects a process from the ready queue and allocates the CPU to it. The process then goes to the running state. Once the time quantum assigned to the process expires or it enters into a wait state, the scheduler preempts the CPU and selects another process.

The notes cover the key process states and transitions for understanding CPU scheduling in Operating Systems. The concepts are explained in points with formal tone and without any emoji or external links as per the given guidelines.