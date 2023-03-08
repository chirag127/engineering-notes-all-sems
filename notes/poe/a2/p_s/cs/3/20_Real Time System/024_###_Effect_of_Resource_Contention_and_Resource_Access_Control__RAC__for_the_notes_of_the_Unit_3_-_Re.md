 Here is the content in markdown format for the given topic:

### Effect of Resource Contention and Resource Access Control (RAC)

1. Resource contention refers to the competition between two or more tasks for a shared resource. When multiple tasks access a shared resource at the same time, it can lead to:
- Delay in task execution due to waiting for the resource to become available.
- Priority inversion where a higher priority task has to wait for a lower priority task to release the shared resource.
- Deadlock where two or more tasks keep waiting for each other to release the resources, resulting in both getting blocked permanently.

2. Resource Access Control (RAC) mechanisms are used to arbitrate the access to shared resources and avoid the negative effects of resource contention. Some common RAC mechanisms are:
- Priority based - Higher priority tasks get the resource first. Can lead to starvation of lower priority tasks.
- Round-robin - Each task gets the resource in a cyclic manner for a fixed time slot. Ensures every task gets the resource but can lead to latency.
- Mutual exclusion using semaphores - Only one task can access the resource at a time. Complex to implement but avoids contention issues.
- Readers-writer locks - Allows multiple readers to access simultaneously but only one exclusive writer at a time. Useful for shared data resources.

[Diagrams and examples can be added here to explain the concepts]

The choice of a suitable RAC mechanism depends on the type of shared resource and requirements of the real-time system. Proper implementation of RAC is critical to ensuring predictable and timely execution of tasks in a real-time system.