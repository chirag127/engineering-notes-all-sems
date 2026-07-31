 Here are the notes for the topic **OS tasks for the notes of the Unit 3 - REAL TIME KERNEL BASICS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM**:

### Task Management
- Tasks are the basic units of execution in a real-time operating system.
- Tasks are independent programs with their own stack and context.
- The operating system manages the tasks using scheduling. The scheduler determines which task gets the CPU based on priority and other factors.
- There are two broad types of task management:
	- Cooperating tasks: Tasks must explicitly yield the CPU. The scheduler only gets involved if a task does not yield.
	- Preemptive tasks: The scheduler can force a running task to relinquish the CPU. This allows for more timely scheduling of high priority tasks. Most real-time systems use preemptive scheduling.

### Scheduling
- Scheduling is the process of determining which task gets to use the CPU.
- Schedulers can be highly complex, taking many factors into account including task priority, task dependencies, CPU utilization, I/O events, etc.
- Common scheduling algorithms include:
	- Rate Monotonic Scheduling: Static priority based on task period
	- Earliest Deadline First: Dynamic priority based on closest deadline
	- Round Robin: Equal time slices for each task
- Scheduling latency refers to any delay in the scheduler switching from one task to the next. Minimizing scheduling latency is important for real-time systems to meet deadlines.

### Inter-task Communication
- Tasks often need to communicate or synchronize with each other.
- Common inter-task communication mechanisms include:
	- Shared memory: Fast but requires locking/mutual exclusion to avoid issues
	- Message passing: Avoid locking issues but can add extra latency
	- Semaphores: Allow controlled access to shared resources
	- Events: Used to signal state changes to waiting tasks