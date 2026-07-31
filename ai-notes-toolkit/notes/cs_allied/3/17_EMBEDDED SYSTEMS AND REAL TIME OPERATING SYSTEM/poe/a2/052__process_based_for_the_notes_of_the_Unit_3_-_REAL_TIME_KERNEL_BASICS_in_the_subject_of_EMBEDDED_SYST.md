 Here are the notes in markdown format without any emojis or external links:

### Process based notes for Unit 3 - REAL TIME KERNEL BASICS

1. Process: A program in execution is called a process. It includes the program code and its current activity. A process needs certain resources to accomplish its task, such as CPU time, memory, files, and I/O devices.

2. Process State: A process transitions between different states in its lifetime. The major states are:

- New: The process is being created.
- Ready: The process is ready to execute.
- Running: The process is executing on the CPU.
- Waiting: The process is waiting for an event to occur or a resource to become available.
- Terminated: The process has completed its task and is terminated.

3. Context Switch: When a running process is interrupted by a higher priority process or due to resource unavailability, the kernel performs a context switch. The context of the running process is saved and the context of another ready process is loaded to resume its execution. This happens very frequently in real-time systems to meet deadlines. Frequent context switches lead to performance degradation due to the overhead involved.

4. Dispatch Latency: The time taken by the kernel to stop one process and start another process is called dispatch latency. Minimizing dispatch latency is critical in real-time systems to achieve deterministic behavior and meet deadlines. This can be done by optimizing context switch code and using techniques like priority inheritance.

5. Scheduling: The kernel allots CPU time to processes. Scheduling is critical in real-time systems to ensure that all timing constraints are met. The major types of real-time scheduling algorithms are:

- Rate Monotonic (RM) Scheduling: Assigns priorities based on task periods. Shorter the period, higher the priority.
- Earliest Deadline First (EDF) Scheduling: Assigns priorities based on closest deadline. Process with closest deadline has highest priority.
- Feasible Condition: A necessary and sufficient condition for a set of real-time tasks to meet all their deadlines under EDF scheduling.