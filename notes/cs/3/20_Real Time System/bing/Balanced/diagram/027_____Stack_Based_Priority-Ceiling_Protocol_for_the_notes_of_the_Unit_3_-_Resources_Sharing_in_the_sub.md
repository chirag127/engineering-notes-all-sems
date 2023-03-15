### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock by ensuring that a task can lock a resource only if it can preempt all the tasks that may need that resource in the future.
  - It reduces the blocking time of tasks by allowing a task to lock multiple resources without being blocked by lower priority tasks that have locked some of the resources.
  - It simplifies the stack management by allowing tasks to share a common stack, which reduces the memory requirement and the context switch overhead.
- The disadvantages of SBPCP are :
  - It may cause unnecessary priority boosting of tasks that do not need to access the resources that have high priority ceilings.
  - It may increase the response time of lower priority tasks that are not involved in resource sharing by delaying their execution due to the priority boosting of higher priority tasks.
  - It requires the knowledge of the resource usage patterns and the priority assignments of all the tasks in the system, which may not be available or may change dynamically.