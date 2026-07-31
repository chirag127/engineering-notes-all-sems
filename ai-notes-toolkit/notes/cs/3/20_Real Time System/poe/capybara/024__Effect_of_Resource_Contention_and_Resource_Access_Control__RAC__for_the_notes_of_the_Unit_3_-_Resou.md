### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System.

Resource contention and Resource Access Control (RAC) are significant issues in real-time systems that require shared resources. Resource contention arises when multiple tasks compete for the same resource. In such a scenario, it is crucial to manage the resources and avoid conflicts that may arise due to the contention. Resource Access Control (RAC) is a mechanism used to manage resource contention.

Some of the effects of resource contention and resource access control (RAC) in real-time systems are:

- **Performance degradation**: Resource contention can lead to performance degradation, where the system becomes slow and unresponsive due to the delay in accessing resources. This can result in missed deadlines and system failure.

- **Priority inversion**: Priority inversion occurs when a low-priority task holds a resource that a high-priority task requires. As a result, the high-priority task is delayed, and the system's overall performance is impacted.

- **Deadlock**: A deadlock occurs when two or more tasks are waiting for resources held by each other. This creates a situation where neither task can proceed, leading to a system failure.

- **Starvation**: Starvation is a situation where a task is unable to access a resource due to resource contention. This can result in the task being delayed indefinitely, leading to system failure.

To avoid these effects, resource access control mechanisms such as priority inheritance protocol, priority ceiling protocol, and stack resource policy can be implemented. These mechanisms ensure that tasks access resources in a controlled manner, avoiding conflicts due to resource contention.

In conclusion, resource contention and resource access control are significant issues in real-time systems that require shared resources. The effects of resource contention can be severe, leading to performance degradation, priority inversion, deadlock, and starvation. Resource access control mechanisms can be implemented to avoid these effects and ensure that tasks access resources in a controlled manner.