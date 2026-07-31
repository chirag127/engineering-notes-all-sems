### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources without causing priority inversion or deadlock .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at that time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
- The advantages of SBPCP are :
  - It prevents priority inversion by ensuring that a higher priority task can always preempt a lower priority task that is holding a resource.
  - It prevents deadlock by ensuring that a task can lock a resource only if it does not cause a circular wait among the tasks.
  - It reduces blocking time by allowing a task to lock multiple resources without being blocked by lower priority tasks.
  - It simplifies stack management by allowing tasks to share a common stack space without interference.