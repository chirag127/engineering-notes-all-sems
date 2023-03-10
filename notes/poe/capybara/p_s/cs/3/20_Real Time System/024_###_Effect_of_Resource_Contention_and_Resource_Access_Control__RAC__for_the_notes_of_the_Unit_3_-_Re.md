### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

Resource sharing is an important aspect of real-time systems. Multiple tasks or processes running on a system often need to access the same resources simultaneously. This can lead to resource contention, which can negatively impact the performance and predictability of the system.

Resource contention can occur in various forms, such as:

- Memory contention: When multiple tasks compete for the same physical memory space.
- CPU contention: When multiple tasks compete for CPU cycles.
- I/O contention: When multiple tasks compete for access to I/O devices.

Resource Access Control (RAC) is a mechanism that helps mitigate the effects of resource contention in real-time systems. It ensures that tasks are granted access to resources in a controlled and predictable manner.

The effects of resource contention and RAC on real-time systems can be summarized as follows:

#### Effects of Resource Contention

- Reduced system performance: When multiple tasks compete for resources, the system may slow down or become less responsive.
- Unpredictable system behavior: Resource contention can lead to unpredictable task execution times, making it difficult to guarantee timing constraints.
- Deadlock and livelock: In extreme cases, resource contention can lead to deadlock or livelock, where tasks wait indefinitely for resources to become available.

#### Effects of Resource Access Control (RAC)

- Improved system performance: By controlling access to shared resources, RAC can improve the overall performance of the system.
- Predictable system behavior: RAC ensures that tasks are granted access to resources in a predictable manner, making it easier to guarantee timing constraints.
- Reduced risk of deadlock and livelock: By preventing tasks from accessing resources that are already in use, RAC can reduce the risk of deadlock and livelock.

Some common RAC techniques used in real-time systems include:

- Priority-based access control: Resources are allocated to tasks based on their priority levels. Tasks with higher priority levels are given access to resources before lower priority tasks.
- Time-based access control: Resources are allocated to tasks based on their temporal requirements. Tasks with more urgent deadlines are given access to resources before less urgent tasks.
- Token-based access control: A token is passed among tasks to grant access to a shared resource. Only the task holding the token can access the resource.

In conclusion, resource contention can have a negative impact on the performance and predictability of real-time systems. However, by using Resource Access Control (RAC) techniques, we can mitigate the effects of resource contention and improve the overall performance and predictability of the system.