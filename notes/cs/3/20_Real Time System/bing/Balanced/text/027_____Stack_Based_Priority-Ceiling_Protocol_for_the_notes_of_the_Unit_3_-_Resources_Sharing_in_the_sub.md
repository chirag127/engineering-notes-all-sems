### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources without causing priority inversion or deadlock .
- In SBPCP, each resource is assigned a priority ceiling, which is equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at that time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its priority is higher than the current ceiling of the system.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock by ensuring that a task holding a resource cannot be blocked by a lower priority task.
  - It reduces the blocking time of a task by allowing it to lock multiple resources without being preempted by intermediate priority tasks.
  - It simplifies the analysis of the worst-case response time of a task by bounding the blocking time by the maximum priority ceiling of all the resources that the task may lock.
  - It allows tasks to share a run-time stack by allocating a stack segment to each resource and switching the stack pointer when a task locks or unlocks a resource. This reduces the memory requirement and the overhead of stack management.