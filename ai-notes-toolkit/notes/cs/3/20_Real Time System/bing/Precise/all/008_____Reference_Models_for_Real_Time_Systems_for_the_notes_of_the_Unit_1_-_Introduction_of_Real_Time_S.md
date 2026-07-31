# Reference Models for Real Time Systems

Real-time systems are computer systems that must meet strict timing constraints to function correctly. These systems are used in a variety of applications, including control systems, multimedia systems, and financial systems. To ensure that real-time systems meet their timing constraints, several reference models have been developed. These models provide a framework for designing, analyzing, and implementing real-time systems.

Some of the most commonly used reference models for real-time systems include:

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their periods, with shorter periods receiving higher priorities.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm for periodic and aperiodic tasks. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines receiving higher priorities.

3. **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm for periodic and aperiodic tasks. In this model, tasks are assigned priorities based on their laxity, which is the difference between their deadlines and their remaining computation time.

4. **Sporadic Server**: This model is used to schedule aperiodic tasks in a system with periodic tasks. In this model, a server task is created to handle the execution of aperiodic tasks. The server is assigned a budget and a period, and it can execute aperiodic tasks as long as it has budget remaining.

These are just a few of the reference models used in real-time systems. Each model has its strengths and weaknesses, and the choice of model depends on the specific requirements of the system being designed.