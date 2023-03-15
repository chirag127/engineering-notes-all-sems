# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- SBPCP has the following rules:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its current priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its current priority is restored to its original priority, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its current priority is higher than the current priority of the other task.
- SBPCP has the following properties:
  - SBPCP prevents deadlock, as a circular wait among tasks is impossible.
  - SBPCP prevents unbounded priority inversion, as a task can be blocked by a lower priority task for at most one critical section.
  - SBPCP is optimal, as it allows any feasible set of tasks to be scheduled without missing any deadlines.
  - SBPCP is stack optimal, as it minimizes the total stack space required by the tasks.