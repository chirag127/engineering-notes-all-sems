### Weighted Round Robin Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

In real-time systems, scheduling plays a critical role in ensuring that tasks are executed on time. One of the most popular scheduling algorithms used in real-time systems is the Weighted Round Robin (WRR) approach. This approach is a variant of the Round Robin scheduling algorithm, but with a weight assigned to each task to prioritize them accordingly.

Here are some key points about the Weighted Round Robin approach:

- WRR is a preemptive scheduling algorithm that assigns a time quantum to each task in a cyclic manner. The task with the highest priority is executed first, and if there are multiple tasks with the same priority, they are executed in a round-robin fashion.

- Each task is assigned a weight, which determines its relative priority compared to other tasks. The higher the weight, the higher the priority of the task.

- The time quantum assigned to each task is proportional to its weight. Thus, tasks with higher weights are given more time to execute, which ensures that they get executed more frequently and with a higher priority.

- One advantage of the WRR approach is that it can handle tasks with different execution times efficiently. Tasks that require more time to execute are assigned a higher weight, which ensures that they get more CPU time and are completed on time.

- Another advantage of the WRR approach is that it can handle both hard and soft real-time tasks. Hard real-time tasks have strict deadlines that must be met, while soft real-time tasks have more flexible deadlines. The WRR approach can prioritize hard real-time tasks over soft real-time tasks by assigning them higher weights.

- The WRR approach can be implemented using a variety of data structures, such as priority queues or circular lists. The choice of data structure depends on the specific requirements of the system.

- One limitation of the WRR approach is that it can lead to task starvation if a task with a lower weight never gets a chance to execute. To avoid this, the WRR approach can be combined with other scheduling algorithms, such as the Earliest Deadline First (EDF) algorithm.

In conclusion, the Weighted Round Robin approach is a popular scheduling algorithm used in real-time systems. It assigns a time quantum to each task based on its weight, which ensures that higher priority tasks are executed more frequently. The WRR approach can handle tasks with different execution times and can prioritize hard real-time tasks over soft real-time tasks. However, it can lead to task starvation, which can be avoided by combining it with other scheduling algorithms.