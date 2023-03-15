### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- SBPCP has the following rules:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered to the highest priority ceiling of the remaining locked resources.
  - A task can preempt another task only if its current priority is higher than the current ceiling of the system.
- SBPCP has the following advantages:
  - It prevents priority inversion and deadlock.
  - It allows tasks to share a run-time stack, which reduces memory requirements and stack overflow risks.
  - It reduces the number of preemptions and context switches compared to OCPP, as tasks can lock multiple resources without being preempted by higher priority tasks that do not need those resources.
  - It has a bounded blocking time for each task, which is equal to the worst-case execution time of the critical sections of the lower priority tasks that may lock any resource needed by the task.
- SBPCP has the following disadvantages:
  - It requires a priori knowledge of the resource usage patterns of the tasks, which may not be available or may change at run-time.
  - It may cause unnecessary blocking of higher priority tasks that do not need the locked resources, as the current ceiling of the system may be higher than the priority of the task that locks the resource.
  - It may cause priority inversion when tasks have different periods or deadlines, as a lower priority task may lock a resource for a longer time than a higher priority task that needs the same resource.