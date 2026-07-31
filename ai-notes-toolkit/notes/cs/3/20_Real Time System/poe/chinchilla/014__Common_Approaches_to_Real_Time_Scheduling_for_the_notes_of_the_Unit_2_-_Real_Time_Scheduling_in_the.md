### Common Approaches to Real Time Scheduling

Real-time scheduling is a crucial aspect of real-time systems that ensures timely execution of tasks. There are various approaches to real-time scheduling, and some of the common ones are:

1. **Rate Monotonic Scheduling (RMS)**: RMS is a widely used scheduling algorithm in real-time systems. It assigns priorities to tasks based on their period, where the task with the shortest period gets the highest priority. This approach is efficient but assumes that all tasks have the same deadline.

2. **Earliest Deadline First (EDF)**: EDF is a dynamic scheduling algorithm that assigns priorities to tasks based on their absolute deadline. The task with the earliest deadline gets the highest priority. This approach is flexible and can handle tasks with varying deadlines.

3. **Deadline Monotonic Scheduling (DMS)**: DMS is similar to RMS, but instead of using task periods, it assigns priorities based on the task's deadline. Tasks with shorter deadlines get higher priorities. This approach is efficient and can handle tasks with varying deadlines.

4. **Fixed Priority Scheduling (FPS)**: FPS assigns fixed priorities to tasks. This approach is simple and efficient but may not be suitable for handling tasks with varying deadlines.

5. **Dynamic Priority Scheduling (DPS)**: DPS is a dynamic scheduling algorithm that adjusts task priorities based on their execution time and remaining deadlines. This approach is flexible and can handle tasks with varying deadlines.

6. **Least Laxity First (LLF)**: LLF is a dynamic scheduling algorithm that assigns priorities based on the task's laxity, which is the difference between the deadline and the remaining execution time. The task with the smallest laxity gets the highest priority. This approach is efficient and can handle tasks with varying deadlines.

In conclusion, real-time scheduling is a critical aspect of real-time systems, and there are various approaches to scheduling tasks. The choice of scheduling algorithm depends on the system requirements, task characteristics, and performance goals.