### Weighted Round Robin Approach for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System
Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems to allocate CPU time to multiple tasks based on their priority and weight. In WRR, each task is assigned a weight, which reflects its relative importance. The scheduler allocates time to each task in a round-robin fashion, but with a twist: the amount of time each task receives is proportional to its weight. 

For example, if task A has a weight of 2 and task B has a weight of 4, task B will receive twice as much CPU time as task A in each round. This approach helps ensure that important tasks receive a larger share of the CPU, while still allowing lower priority tasks to run. 

WRR is particularly useful in real-time systems where tasks have varying levels of importance, and where some tasks may have deadlines that must be met. By assigning weights to tasks, the scheduler can make sure that the most important tasks receive the necessary resources to meet their deadlines. 

Overall, the WRR approach is a flexible and effective way to allocate CPU time in real-time systems, and is widely used in a variety of applications, including embedded systems, network routers, and multimedia systems.
