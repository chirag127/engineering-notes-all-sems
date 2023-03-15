### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The scheduler allocates CPU time to each task based on its weight.

Here are the key points to note about the Weighted Round Robin approach:

1. In WRR, tasks with higher weights are given more CPU time compared to tasks with lower weights.
2. The scheduler assigns time slices to each task in proportion to their weights.
3. The time slice for each task is calculated by dividing the weight of the task by the sum of the weights of all tasks.
4. Tasks with the same weight are scheduled in a round-robin fashion.
5. WRR is a fair scheduling algorithm, as it ensures that tasks with higher weights are given more CPU time, while tasks with lower weights are not starved of CPU time.
6. WRR is suitable for real-time systems where tasks have different priorities and importance.
