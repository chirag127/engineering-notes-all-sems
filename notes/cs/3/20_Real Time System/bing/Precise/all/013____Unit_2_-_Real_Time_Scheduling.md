## Unit 2 - Real Time Scheduling

Real-time scheduling is the process of assigning tasks to resources in a way that ensures that all tasks meet their timing constraints. This is important in real-time systems, where tasks have deadlines that must be met in order for the system to function correctly.

There are several types of real-time scheduling algorithms, including:

1. **Rate Monotonic Scheduling (RMS)**: This is a static priority scheduling algorithm where tasks are assigned priorities based on their periods. The shorter the period, the higher the priority.

2. **Earliest Deadline First (EDF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their deadlines. The earlier the deadline, the higher the priority.

3. **Least Laxity First (LLF)**: This is a dynamic priority scheduling algorithm where tasks are assigned priorities based on their laxity. The laxity of a task is the amount of time remaining until its deadline minus its remaining execution time. The smaller the laxity, the higher the priority.

Real-time scheduling algorithms can be classified as either **hard real-time** or **soft real-time**. Hard real-time scheduling algorithms guarantee that all tasks will meet their deadlines, while soft real-time scheduling algorithms do not provide such guarantees but instead aim to minimize the number of missed deadlines.

Real-time scheduling is a complex and challenging problem, and there is ongoing research in this area to develop new algorithms and techniques to improve the performance of real-time systems.