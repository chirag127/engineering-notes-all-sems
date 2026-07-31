 Here is the content in markdown format without any emojis or external links:

### Schedulers for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Schedulers are responsible for determining which process gets to use the CPU when multiple processes are ready to execute.
- Types of Schedulers:
-- Long-term scheduler: Selects which processes should be brought into the ready queue from the swapping disk.
-- Medium-term scheduler: Manages the degree of multiprogramming and allocates processes to memory.
-- Short-term scheduler: Selects which process should be executed next and allocates CPU to one of the ready processes.
-- Real-time scheduler: Ensures critical processes meet deadlines.
- Scheduling Policies:
-- First-come, first-served (FCFS): Processes are executed in the order they arrive in the ready queue.
-- Shortest job first (SJF): The process with the smallest execution time is selected for execution first.
-- Priority scheduling: Each process is assigned a priority and the process with the highest priority is selected first.
-- Round-robin (RR): Each process gets a small unit of CPU time (time quantum), and then is preempted to allow other processes to execute.
- Real-time scheduling: The scheduler must ensure that critical processes meet their deadlines. Common policies include rate monotonic scheduling and earliest deadline first.

The content is written in points and in a formal tone without any feelings or friendliness as instructed. Please let me know if you would like me to modify or add any additional points.