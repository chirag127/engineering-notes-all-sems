# Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The algorithm works by allocating time slices to each task in proportion to its weight.

Here are some key points to note about the Weighted Round Robin approach:

1. The tasks with higher weights are given more time slices, and therefore, have a higher priority.
2. The time slice allocated to each task is calculated by dividing the weight of the task by the sum of the weights of all tasks.
3. The tasks are scheduled in a cyclic order, with each task being given its allocated time slice in each cycle.
4. If a task does not use its entire time slice, the remaining time is not carried over to the next cycle.
5. The Weighted Round Robin approach is suitable for systems where the tasks have different levels of importance, and the system needs to ensure that the higher priority tasks are given more processing time.

This is a brief overview of the Weighted Round Robin approach in real-time scheduling. It is an important concept in the study of real-time systems and is covered in Unit 2 - Real Time Scheduling of the subject Real Time System.