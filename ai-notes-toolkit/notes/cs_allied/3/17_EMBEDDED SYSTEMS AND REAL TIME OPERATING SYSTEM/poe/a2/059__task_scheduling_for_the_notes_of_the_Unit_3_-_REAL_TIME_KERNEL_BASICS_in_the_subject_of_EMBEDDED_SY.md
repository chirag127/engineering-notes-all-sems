 Here is the formal content on the given topic:

### Task Scheduling for the notes of the Unit 3 - REAL TIME KERNEL BASICS

1. Task scheduling: The process of determining which task should be executed at a given time is called task scheduling. The scheduler selects a task from the ready queue and allocates CPU to it.
2. Types of task scheduling:
- Preemptive: The scheduler can preempt a running task and allocate CPU to a higher priority task. Most real-time OS use preemptive scheduling.
- Non-preemptive: Once a task starts executing, it runs to completion without preemption. Non-preemptive scheduling is rarely used in real-time systems.
3. Scheduling algorithms:
- Priority based: Each task is assigned a priority. The scheduler selects the highest priority task from the ready queue.
- Round-robin: Each task gets a small time quantum. After a time quantum expires, the scheduler selects the next task. This approach ensures fairness but can affect deadlines.
- Earliest deadline first: The task with the earliest deadline is selected first. This algorithm optimizes the number of missed deadlines but can lead to starvation of lower priority tasks.
4. Scheduling parameters:
- Period: Time interval between successive releases/arrivals of a task.
- Deadline: Time by which a task must complete its execution. Deadline equals release time plus relative deadline.
- Release time: Time at which a task is released for execution.
- Relative deadline: The maximum time a task can take to complete its execution after release.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or add any other points to the content.