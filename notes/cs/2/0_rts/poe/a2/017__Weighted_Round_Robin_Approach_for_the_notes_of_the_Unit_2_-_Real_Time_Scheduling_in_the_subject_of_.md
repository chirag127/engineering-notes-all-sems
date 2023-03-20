 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Weighted Round Robin Approach

- Weighted Round Robin is an extended version of simple Round Robin scheduling.
- In Weighted Round Robin, each task is assigned a weight based on its priority.
- Higher priority tasks are given higher weights.
- The scheduler serves the tasks in a Round Robin manner but for a time slice proportional to the weight of the task.
- For example, if task T1 has weight 2 and task T2 has weight 1 then T1 gets twice the time slice as T2 in one round of service.
- This approach ensures that higher priority tasks get more CPU time and hence meet their deadlines.
- However, it does not guarantee a deadline for the lower priority tasks. Their execution depends on the availability of CPU time left after serving the higher priority tasks.
- Weighted Round Robin is easy to implement but may cause starvation for lower priority tasks. It provides a trade-off between throughput and delay.

The above points cover the key aspects of the Weighted Round Robin approach for Real Time Scheduling. Let me know if you would like me to elaborate on any of the points or add/modify any points.