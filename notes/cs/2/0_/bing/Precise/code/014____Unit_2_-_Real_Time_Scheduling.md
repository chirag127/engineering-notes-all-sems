## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning system resources to tasks in a timely and predictable manner. This is important in real-time systems, where tasks have strict timing constraints and must be completed within a certain time frame.

There are several types of real-time scheduling algorithms, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a static priority scheduling algorithm where tasks are assigned priorities based on their periods. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their deadlines. The earlier the deadline, the higher the priority.

3. **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity, the higher the priority.

Real-time scheduling algorithms must ensure that all tasks meet their deadlines while also maximizing system utilization. This can be a challenging problem, and there are many factors to consider when choosing a real-time scheduling algorithm for a particular system.