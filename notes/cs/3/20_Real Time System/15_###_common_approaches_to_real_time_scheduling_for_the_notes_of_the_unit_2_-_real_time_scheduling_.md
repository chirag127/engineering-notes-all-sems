### Common Approaches to Real Time Scheduling for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

Common approaches to real-time scheduling are methods used to schedule tasks in real-time systems to ensure that they are executed in a timely manner. The following are some of the key concepts related to common approaches to real-time scheduling:

1. Rate Monotonic Scheduling (RMS): RMS is a scheduling algorithm that assigns priorities to tasks based on their periodic release times, and executes tasks with higher priorities before tasks with lower priorities. RMS is a deterministic algorithm and is suitable for real-time systems with periodic tasks.

2. Earliest Deadline First (EDF): EDF is a scheduling algorithm that assigns priorities to tasks based on their deadlines, and executes tasks with earlier deadlines before tasks with later deadlines. EDF is a dynamic algorithm and is suitable for real-time systems with aperiodic tasks.

3. Least Laxity First (LLF): LLF is a scheduling algorithm that assigns priorities to tasks based on their remaining execution time and their deadlines, and executes tasks with lower laxity first. LLF is a dynamic algorithm and is suitable for real-time systems with aperiodic tasks.

4. Priority Inheritance Protocol (PIP): PIP is a protocol used to resolve priority inversion, which is a situation where a lower priority task is holding a resource needed by a higher priority task. PIP temporarily raises the priority of the lower priority task to the priority of the higher priority task, allowing the higher priority task to execute.

5. Priority Ceiling Protocol (PCP): PCP is a protocol used to resolve priority inversion, which is a situation where a lower priority task is holding a resource needed by a higher priority task. PCP assigns a ceiling priority to each resource, and raises the priority of a task to the ceiling priority of the resource it is holding, allowing higher priority tasks to execute.

In this unit, you will learn about common approaches to real-time scheduling, including Rate Monotonic Scheduling (RMS), Earliest Deadline First (EDF), Least Laxity First (LLF), Priority Inheritance Protocol (PIP), and Priority Ceiling Protocol (PCP).

This unit will provide a foundation for understanding the principles and practices of common approaches to real-time scheduling, and for exploring the various concepts and techniques used in the field of real-time systems.
