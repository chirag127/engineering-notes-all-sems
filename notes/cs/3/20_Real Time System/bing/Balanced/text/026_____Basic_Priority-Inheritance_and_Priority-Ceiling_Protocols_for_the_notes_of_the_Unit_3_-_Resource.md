### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) is a technique for sharing critical resources among different tasks without the occurrence of unbounded priority inversions.
- Priority inversion is a situation where a low-priority task holds a resource that is needed by a high-priority task, and the low-priority task is preempted by a medium-priority task, thus delaying the high-priority task indefinitely.
- The basic idea of PIP is that when a task blocks one or more higher-priority tasks, it ignores its original priority assignment and executes its critical section at an elevated priority level. After executing its critical section and releasing its locks, the task returns to its original priority level.
- PIP has the following rules:
  - Scheduling Rule: Ready tasks are scheduled on the processor preemptively in a priority-driven manner according to their current priority.
  - Priority Assignment Rule: At its release time, the current priority of every task is equal to its assigned priority. The task remains at this priority except under the condition stated in rule 3.
  - Priority Inheritance Rule: If a task J is blocked on a resource R that is currently locked by a task I, then the current priority of task I is set to the maximum of its current priority and the assigned priority of task J. This rule is applied transitively to handle nested resource requests and multiple inheritance situations.
  - Priority Restoration Rule: When a task releases a resource, its current priority is set to the maximum of its assigned priority and the current priority of all tasks that are blocked on any resource that it still holds.
- Priority-Ceiling Protocol (PCP) is another technique for sharing critical resources among different tasks without the occurrence of unbounded priority inversions.
- PCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling.
- PCP has two variants: Immediate Ceiling Priority Protocol (ICPP) and Original Ceiling Priority Protocol (OCPP).
- In ICPP, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource. A task can lock a resource only if its current priority is higher than the priority ceiling of all resources currently locked by other tasks. When a task locks a resource, its current priority is raised to the priority ceiling of that resource. When a task releases a resource, its current priority is restored to the maximum of its assigned priority and the priority ceiling of all resources that it still holds.
- In OCPP, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task which may lock the resource. A task can lock a resource only if its current priority is higher than the priority ceiling of all resources currently locked by other tasks. When a task locks a resource, its current priority is not changed. When a task releases a resource, its current priority is restored to the maximum of its assigned priority and the priority ceiling of all resources that it still holds.
- The advantages of PCP over PIP are:
  - PCP prevents deadlock by ensuring that a task can lock a resource only if it does not block any higher-priority task.
  - PCP reduces the number of context switches by avoiding unnecessary priority changes.
  - PCP allows the schedulability analysis of tasks to be simpler and more efficient.