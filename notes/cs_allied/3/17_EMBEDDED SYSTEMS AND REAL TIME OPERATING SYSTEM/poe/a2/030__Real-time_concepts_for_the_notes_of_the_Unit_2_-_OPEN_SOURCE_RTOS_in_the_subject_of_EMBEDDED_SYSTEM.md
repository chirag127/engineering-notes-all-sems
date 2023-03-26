 Here is the formal content in Markdown format without any emojis or external links:

### Real-time concepts for the notes of the Unit 2 - OPEN SOURCE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

1. Hard Real-Time System: A hard real-time system is a system where missing a deadline results in a catastrophic failure. Missing a deadline is unacceptable. Example: Flight control system, industrial control systems.

2. Soft Real-Time System: A soft real-time system is a system where missing a deadline results in degradation of service. Missing deadlines occasionally is acceptable but not desirable. Example: Video streaming, voice calling.

3. Real-Time Operating System (RTOS): An RTOS is an OS designed for real-time applications. It provides mechanisms to meet deadlines and time constraints. Some features of an RTOS are:

- Preemptive and priority based scheduling
- Fast context switching
- Low interrupt latency
- Memory protection
- Deterministic behavior

4. Preemptive vs Non-Preemptive Scheduling: In preemptive scheduling, a higher priority task can preempt (interrupt) a lower priority running task. In non-preemptive scheduling, once a task starts executing, it runs to completion unless it blocks itself. Preemptive scheduling is more suitable for hard real-time systems.

5. Scheduling Algorithms: Some common real-time scheduling algorithms are:

- Rate Monotonic Scheduling (RMS): Higher priority to tasks with shorter periods (deadlines)
- Deadline Monotonic Scheduling (DMS): Higher priority to tasks with shorter deadlines
- Earliest Deadline First (EDF): The task with the earliest deadline is scheduled first
- Least Laxity First: Task with least laxity (deadline - execution time - current time) is scheduled first