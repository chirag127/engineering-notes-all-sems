### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Both protocols aim to prevent or reduce priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a shared resource.
- Priority inversion can cause deadline misses, reduced throughput, and increased response time for real-time tasks.

#### Priority-Inheritance Protocol

- The basic idea of priority-inheritance protocol is to temporarily raise the priority of a task that holds a resource to the highest priority of any task that is waiting for the same resource.
- This way, the resource-holding task can finish its critical section and release the resource as soon as possible, reducing the blocking time for the higher-priority tasks.
- The priority of the resource-holding task is restored to its original value after releasing the resource.
- The priority-inheritance protocol can be implemented using a priority queue for each resource, where the tasks that request the resource are inserted in the order of their priorities.
- The priority-inheritance protocol guarantees that the blocking time of a task is bounded by the duration of the longest critical section of a lower-priority task that shares a resource with it.
- The priority-inheritance protocol is greedy, meaning that it allows a task to access a resource whenever the resource is free, regardless of the priorities of other tasks that may request the same resource later.

#### Priority-Ceiling Protocol

- The basic idea of priority-ceiling protocol is to assign a priority ceiling to each resource, which is the highest priority of any task that can access the resource.
- A task can access a resource only if its priority is higher than the priority ceilings of all the resources that are currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from being blocked by a lower-priority task that does not hold the requested resource, which is called avoidance blocking.
- The priority-ceiling protocol also prevents deadlock, which is a situation where a set of tasks are waiting for each other's resources in a circular manner.
- The priority-ceiling protocol can be implemented using a global variable that stores the highest priority ceiling of all the resources that are currently held by any task.
- The priority-ceiling protocol guarantees that the blocking time of a task is bounded by the duration of the shortest critical section of a lower-priority task that shares a resource with it.
- The priority-ceiling protocol is not greedy, meaning that it may withhold access to a free resource, causing a task to be blocked by a lower-priority task that may request the same resource later.