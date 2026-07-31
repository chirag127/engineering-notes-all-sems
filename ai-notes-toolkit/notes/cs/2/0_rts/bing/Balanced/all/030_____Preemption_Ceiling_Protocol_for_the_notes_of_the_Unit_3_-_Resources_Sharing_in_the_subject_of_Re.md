# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems to avoid unbounded priority inversion and mutual deadlock.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources that are held by other tasks, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the current ceiling of the system, which is the maximum of the ceilings of all the locked resources.
- A task that locks a resource inherits the ceiling of that resource, and cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that no deadlock can occur.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceilings of the resources at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceilings of the resources at run time, based on the actual priorities of the tasks that request them.
- Dynamic preemption ceiling protocol has lower overhead and better response time than static preemption ceiling protocol, but it requires more storage and complexity.
- Preemption ceiling protocol can be extended to support object-oriented real-time systems, where the shared resources are encapsulated in objects and accessed by methods.
- Dual ceiling protocol is a variant of preemption ceiling protocol that allows a task to invoke a method of an object without locking it, if the method does not modify the object state.
- Dual ceiling protocol assigns two ceilings to each object: a normal ceiling and a preemption ceiling.
- The normal ceiling is the highest priority of any task that can invoke a modifying method of the object, and the preemption ceiling is the highest priority of any task that can invoke a non-modifying method of the object.
- A task can invoke a method of an object only if its priority is higher than the current normal ceiling of the system, and it inherits the normal ceiling or the preemption ceiling of the object, depending on the type of the method.
- Dual ceiling protocol reduces the blocking time and improves the schedulability of object-oriented real-time systems.