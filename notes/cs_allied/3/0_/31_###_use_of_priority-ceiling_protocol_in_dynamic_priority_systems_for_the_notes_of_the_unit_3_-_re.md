### Use of Priority-Ceiling Protocol in Dynamic Priority Systems for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

The Priority-Ceiling Protocol is a resource allocation protocol used in real-time systems to ensure that resources are shared fairly among tasks with different priority levels.

1. Definition: The Priority-Ceiling Protocol is a resource allocation protocol used in real-time systems to ensure that resources are shared fairly among tasks with different priority levels. The protocol assigns a priority ceiling to each resource, which determines the highest priority task that can access the resource.

2. Dynamic Priority Systems: Dynamic priority systems are real-time systems where the priority of tasks can change dynamically. The Priority-Ceiling Protocol is used in dynamic priority systems to ensure that changes in task priority do not result in resource allocation problems.

3. Priority Ceiling: The priority ceiling is the highest priority level that can be assigned to a task when it is accessing a particular resource. The priority ceiling is determined by the priority of the highest-priority task that is currently accessing the resource.

4. Resource Allocation: The Priority-Ceiling Protocol ensures that resources are allocated fairly among tasks with different priority levels by assigning a priority ceiling to each resource. When a task requests access to a resource, its priority is temporarily raised to the priority ceiling of the resource, ensuring that no lower-priority task can access the resource while the higher-priority task is using it.

5. Advantages: The Priority-Ceiling Protocol has several advantages, including its ability to ensure that resources are shared fairly among tasks with different priority levels, its ability to prevent priority inversion, and its ability to ensure that changes in task priority do not result in resource allocation problems.

6. Limitations: Despite its advantages, the Priority-Ceiling Protocol also has several limitations, including its complexity, its potential to cause resource starvation, and its potential to result in priority inversion if not implemented correctly.

In conclusion, The Priority-Ceiling Protocol is a resource allocation protocol used in real-time systems to ensure that resources are shared fairly among tasks with different priority levels. The protocol is used in dynamic priority systems to ensure that changes in task priority do not result in resource allocation problems. The priority ceiling is the highest priority level that can be assigned to a task when it is accessing a particular resource, and the protocol ensures that resources are allocated fairly by temporarily raising the priority of a task to the priority ceiling of the resource it is accessing. The Priority-Ceiling Protocol has several advantages, including its ability to ensure fair resource allocation, but also has several limitations, including its complexity and potential to cause resource starvation.
