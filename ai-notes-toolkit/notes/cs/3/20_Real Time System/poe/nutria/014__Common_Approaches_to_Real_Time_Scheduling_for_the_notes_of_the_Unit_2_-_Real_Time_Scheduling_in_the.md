
### Common Approaches to Real Time Scheduling 

1. Rate Monotonic Scheduling (RMS): This approach assigns the highest priority to the task with the shortest period, and assigns lower priorities to longer-period tasks. It is the simplest and most widely used scheduling algorithm for real-time systems.

2. Earliest Deadline First (EDF): This approach assigns the highest priority to the task with the earliest deadline, and assigns lower priorities to tasks with later deadlines. It is more suitable for systems with dynamic task sets, since it can handle deadline changes more efficiently than RMS.

3. Least Laxity First (LLF): This approach assigns the highest priority to the task with the least amount of time remaining before its deadline, and assigns lower priorities to tasks with more time remaining. It is useful in situations where the deadlines may be missed due to high processor utilization.

4. Priority Inheritance Protocol (PIP): This approach allows a lower-priority task to temporarily inherit the priority of a higher-priority task that is accessing a shared resource. This allows the lower-priority task to complete its work in a timely manner.