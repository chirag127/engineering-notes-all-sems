# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its current priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task releases a resource, its current priority is restored to its original priority, and the current ceiling of the system is lowered accordingly.
- SBPCP prevents priority inversion, deadlock, and chain blocking, and guarantees bounded blocking time for each task .
- SBPCP is suitable for systems that have limited memory and need to share a run-time stack among tasks .