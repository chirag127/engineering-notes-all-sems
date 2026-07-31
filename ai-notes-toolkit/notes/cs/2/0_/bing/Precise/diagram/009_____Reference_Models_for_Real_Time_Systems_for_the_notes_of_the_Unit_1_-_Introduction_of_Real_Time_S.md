### Reference Models for Real Time Systems

Real-time systems are computer systems that monitor, respond to, or control an external environment. This environment is connected to the computer system through sensors, actuators, and other input-output interfaces. The system must provide a response within a specified time, otherwise, the system's performance will degrade or fail.

Here are some reference models for real-time systems:

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-driven algorithm for scheduling periodic tasks in a real-time system. The tasks are assigned priorities based on their periods, with the shortest period task having the highest priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm for real-time systems. The tasks are assigned priorities based on their deadlines, with the earliest deadline task having the highest priority.

3. **Least Laxity First (LLF)**: This is another dynamic priority scheduling algorithm for real-time systems. The tasks are assigned priorities based on their laxity, which is the difference between the task's deadline and its remaining computation time. The task with the least laxity has the highest priority.

4. **Sporadic Server**: This is a scheduling algorithm for handling aperiodic tasks in a real-time system. The sporadic server reserves a portion of the processor's capacity for handling aperiodic tasks, and schedules them using the EDF or LLF algorithm.

These are some of the reference models used in real-time systems. They provide a framework for designing and analyzing real-time systems to ensure that they meet their timing constraints.