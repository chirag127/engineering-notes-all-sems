

#### Failures in Map Reduce

- **Task Failure**: When a task fails, the master assigns the task to another worker. Task failure occurs when the new worker also fails to complete the task.
- **Job Failure**: Job failure occurs when the master fails to assign the task to a new worker.
- **Data Loss**: Data loss occurs when a task fails and the data associated with the task is not recovered.
- **Network Partition**: Network partition occurs when the network is split into two or more components, which cannot communicate with each other.
- **Deadlock**: Deadlock occurs when two or more tasks are waiting for each other to complete, but none of them can complete.
- **Memory Leak**: Memory leak occurs when a program or process is unable to release memory that it has allocated.
- **Disk Space Exhaustion**: Disk space exhaustion occurs when the disk space allocated to a task is insufficient to complete the task.
- **Data Skew**: Data skew occurs when the input data is not evenly distributed across the nodes.
- **Stragglers**: Stragglers occur when some tasks take significantly longer to complete than others.
- **Speculative Execution**: Speculative execution occurs when the master assigns multiple tasks to the same worker, in order to increase the overall throughput.