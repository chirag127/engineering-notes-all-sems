# Reference Models for Real Time Systems

Real-time systems are computer systems that must meet strict timing constraints in order to function correctly. These systems are often used in safety-critical applications, such as air traffic control, medical equipment, and nuclear power plants. To ensure that real-time systems meet their timing constraints, several reference models have been developed. These models provide a framework for designing, analyzing, and implementing real-time systems.

Some of the most commonly used reference models for real-time systems include:

1. **Rate Monotonic Scheduling (RMS)**: This model is based on the principle that tasks with shorter periods should have higher priorities. RMS assigns priorities to tasks based on their periods, with the task with the shortest period receiving the highest priority.

2. **Earliest Deadline First (EDF)**: This model assigns priorities to tasks based on their deadlines. The task with the earliest deadline is given the highest priority.

3. **Least Laxity First (LLF)**: This model assigns priorities to tasks based on their laxity, which is the amount of time remaining until their deadline minus their remaining execution time. The task with the least laxity is given the highest priority.

4. **Fixed Priority Scheduling (FPS)**: This model assigns fixed priorities to tasks, which do not change during the execution of the system. The priorities can be assigned based on various criteria, such as the importance of the task or its period.

These reference models provide a starting point for designing real-time systems. However, it is important to note that each system is unique and may require a customized approach to meet its specific timing constraints.