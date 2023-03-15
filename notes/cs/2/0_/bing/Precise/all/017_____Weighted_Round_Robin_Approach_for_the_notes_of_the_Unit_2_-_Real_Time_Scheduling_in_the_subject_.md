### Weighted Round Robin Approach

Weighted Round Robin (WRR) is a scheduling algorithm used in real-time systems. It is an extension of the Round Robin algorithm, where each task is assigned a weight, representing the relative importance of the task. The scheduler allocates CPU time to each task based on its weight, with higher-weighted tasks receiving more CPU time than lower-weighted tasks.

The steps involved in the WRR algorithm are as follows:

1. The scheduler maintains a list of all tasks, sorted in descending order of their weights.
2. The scheduler selects the first task in the list and allocates it a time slice equal to its weight.
3. The task is then moved to the end of the list, and the next task is selected.
4. This process is repeated until all tasks have been allocated a time slice.
5. The scheduler then starts again from the beginning of the list.

The WRR algorithm ensures that higher-weighted tasks are given priority over lower-weighted tasks, while still ensuring that all tasks receive some CPU time. This makes it a suitable algorithm for real-time systems, where tasks may have different levels of importance and urgency.