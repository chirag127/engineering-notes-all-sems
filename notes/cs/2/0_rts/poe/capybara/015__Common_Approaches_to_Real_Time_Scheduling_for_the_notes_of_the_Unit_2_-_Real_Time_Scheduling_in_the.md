### Common Approaches to Real Time Scheduling

Real-time scheduling is a critical aspect of real-time systems. It aims at allocating system resources to different tasks, ensuring that these tasks meet their deadlines. Here are some of the common approaches to real-time scheduling:

1. **Rate Monotonic Scheduling (RMS)**: This scheduling algorithm assigns priority to tasks based on their periods. The shorter the period, the higher the priority. It assumes that tasks are independent and have the same worst-case execution time (WCET). RMS is simple to implement, but it may not be optimal in all situations.

2. **Earliest Deadline First (EDF)**: EDF assigns priority to tasks based on their deadlines. The task with the closest deadline is given the highest priority. It is a dynamic scheduling algorithm and adapts well to changes in the system. EDF is optimal, but it requires more computational resources.

3. **Deadline Monotonic Scheduling (DMS)**: DMS assigns priority to tasks based on their deadlines. The shorter the deadline, the higher the priority. It is similar to RMS, but it is more optimal. DMS is not as simple to implement as RMS but requires less computational resources than EDF.

4. **Fixed Priority Scheduling (FPS)**: FPS assigns a static priority to tasks based on their criticality. The highest priority task is executed first. It is widely used in practice due to its simplicity and predictability. However, it may not be optimal in all situations.

5. **Priority Inheritance (PI)**: PI is a technique used to prevent priority inversion. It assigns the highest priority of the blocked task to the task that holds the resource. It guarantees that the highest priority task will always have access to the required resources.

In conclusion, selecting the right scheduling algorithm depends on the system requirements and the task characteristics. Each algorithm has its advantages and disadvantages, and a careful analysis is required to select the most appropriate one.