# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use at the time.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock.
  - It reduces the blocking time of high-priority tasks by allowing them to preempt lower-priority tasks that are using resources.
  - It simplifies the analysis of the worst-case response time of tasks by bounding the blocking time to the maximum execution time of any lower-priority task that can lock a resource.
  - It reduces the memory requirement by allowing tasks to share a common stack.