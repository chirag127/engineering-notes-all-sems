### Common Approaches to Real Time Scheduling

Real-time scheduling is a critical aspect of real-time systems. It involves making critical decisions in a timely manner to ensure that tasks are executed within their deadlines. There are several approaches to real-time scheduling, and they are as follows:

1. **Priority-Based Scheduling:** This approach is based on assigning priorities to tasks based on their criticality. The scheduler assigns a higher priority to more critical tasks and ensures that they are executed first. Priority-based scheduling is simple and effective, but it may not be suitable for systems with a large number of tasks.

2. **Earliest Deadline First (EDF) Scheduling:** This approach is based on the deadline of the task. The scheduler assigns the highest priority to the task with the earliest deadline. This approach ensures that tasks with shorter deadlines are executed first, which helps in meeting the deadlines of all the tasks.

3. **Rate Monotonic Scheduling (RMS):** This approach is based on the periodicity of the tasks. The scheduler assigns priorities to tasks based on their periods. Tasks with shorter periods are assigned higher priorities. This approach ensures that tasks with shorter periods are executed more frequently, which helps in meeting their deadlines.

4. **Deadline Monotonic Scheduling (DMS):** This approach is similar to RMS, but it assigns priorities based on the task's deadline instead of its period. Tasks with shorter deadlines are assigned higher priorities. This approach ensures that tasks with shorter deadlines are executed first, which helps in meeting their deadlines.

5. **Dynamic Scheduling:** This approach is based on the current system state. The scheduler evaluates the current state of the system and decides which task to execute next. This approach is more complex than the other approaches, but it can handle systems with a large number of tasks and changing priorities.

These are the common approaches to real-time scheduling. The choice of approach depends on the system's requirements and constraints, such as the number of tasks, their criticality, and their deadlines. Understanding these approaches is essential for designing efficient real-time systems.