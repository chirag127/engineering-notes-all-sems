# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Real-time systems are systems that have strict timing constraints and must respond to events within a specified deadline.
- Resource access control is the problem of ensuring that concurrent tasks do not interfere with each other when accessing shared resources, such as memory, devices, or semaphores.
- Interference can cause priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a resource needed by the higher-priority task.
- Priority inversion can lead to missed deadlines, reduced performance, and even deadlock in real-time systems.

## Priority-Inheritance Protocol

- The priority-inheritance protocol (PIP) is a method for eliminating unbounded priority inversion by temporarily raising the priority of a task that holds a resource needed by a higher-priority task.
- The basic idea of PIP is that when a higher-priority task requests a resource that is locked by a lower-priority task, the lower-priority task inherits the priority of the higher-priority task until it releases the resource.
- This way, the lower-priority task can finish its critical section faster and unblock the higher-priority task, reducing the blocking time and avoiding deadlock.
- PIP has the following properties:
  - A task can be blocked by at most one lower-priority task at a time.
  - The blocking time of a task is bounded by the longest critical section of any lower-priority task.
  - A task can inherit multiple priorities if it holds multiple resources that are requested by multiple higher-priority tasks.
  - A task can release its resources in any order, regardless of the order of acquisition.

## Priority-Ceiling Protocol

- The priority-ceiling protocol (PCP) is a method for minimizing the blocking time of a task to at most one critical section of a lower-priority task, and preventing deadlock and unnecessary blocking.
- The basic idea of PCP is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource. A task can only lock a resource if its priority is higher than the priority ceiling of all the resources currently locked by other tasks.
- This way, a task can avoid being blocked by a lower-priority task that does not hold the requested resource, and also avoid creating a circular dependency of resource requests that can cause deadlock.
- PCP has the following properties:
  - A task can be blocked by at most one lower-priority task at a time.
  - The blocking time of a task is bounded by the shortest critical section of any lower-priority task.
  - A task can inherit only one priority, which is the highest priority ceiling of all the resources it holds.
  - A task must release its resources in the reverse order of acquisition.

## Differences between PIP and PCP

- PIP is greedy, while PCP is not. PIP allows a task to lock a resource whenever the resource is free, while PCP may deny a task access to a free resource if its priority is lower than the priority ceiling of another locked resource.
- PCP is more restrictive, but also more predictable than PIP. PCP prevents unnecessary blocking and deadlock, but also imposes a fixed order of resource acquisition and release, while PIP allows more flexibility, but also more uncertainty in resource access control.
- PCP requires a priori knowledge of the resource usage of each task, while PIP does not. PCP needs to assign a priority ceiling to each resource based on the highest priority of any task that can access it, while PIP does not need any information about the resource usage of the tasks.