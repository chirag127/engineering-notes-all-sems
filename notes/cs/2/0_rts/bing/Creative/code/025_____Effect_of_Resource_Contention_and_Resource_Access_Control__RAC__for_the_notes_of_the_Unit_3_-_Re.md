Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of effect of resource contention and resource access control (RAC) for the notes of the unit 3 - resource sharing in the subject of real time system.

### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock .
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource .
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way .
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed .
- Some examples of RAC protocols are priority inheritance protocol, priority ceiling protocol, stack resource policy, and multiprocessor priority ceiling protocol  .
- These protocols aim to prevent or bound priority inversion, avoid timing anomalies, and prevent deadlock by enforcing certain rules on the priority, order, and duration of resource access  .
- The choice of RAC protocol depends on the characteristics of the system, such as the number of resources, the number of tasks, the number of processors, the type of scheduling algorithm, and the performance requirements  .