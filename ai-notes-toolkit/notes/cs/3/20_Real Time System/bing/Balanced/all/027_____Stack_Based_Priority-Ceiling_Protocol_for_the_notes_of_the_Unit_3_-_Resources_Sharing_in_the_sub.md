# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its current priority is higher than the current ceiling of the system.
- The advantages of SBPCP are :
  - It prevents priority inversion, deadlock, and chain blocking.
  - It has a bounded blocking time for each task, which is equal to the worst-case execution time of the critical sections of the lower priority tasks that share the same resources.
  - It reduces the number of context switches and stack operations compared to OCPP, since a task does not need to switch to a new stack when it locks a resource.
  - It allows tasks to share a run-time stack, which reduces the memory requirement and simplifies the stack management.