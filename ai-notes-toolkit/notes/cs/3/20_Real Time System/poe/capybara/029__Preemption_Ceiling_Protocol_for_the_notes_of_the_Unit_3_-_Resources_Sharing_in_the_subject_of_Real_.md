### Preemption Ceiling Protocol

The Preemption Ceiling Protocol is a popular and effective technique for preventing priority inversion in real-time systems. It is a resource-sharing protocol that ensures that a high-priority task is not blocked by a lower-priority task that is holding a resource that the high-priority task needs.

Here are some important points to understand about the Preemption Ceiling Protocol:

- The Preemption Ceiling Protocol is based on the concept of a "ceiling priority" for each resource. The ceiling priority is the highest priority of any task that could potentially use the resource. The ceiling priority is determined at the time the resource is created.
- When a task requests a resource, its priority is temporarily raised to the ceiling priority of the resource. This ensures that no lower-priority task can block the requesting task while it is holding the resource.
- If a task attempts to acquire a resource that is already held by a lower-priority task, it will be blocked until the lower-priority task releases the resource.
- The Preemption Ceiling Protocol is simple to implement and is effective at preventing priority inversion. However, it may result in priority inheritance, where a low-priority task inherits the priority of a high-priority task that is blocked waiting for a resource.

In summary, the Preemption Ceiling Protocol is a resource-sharing protocol that prevents priority inversion by temporarily raising the priority of a task to the ceiling priority of a resource it needs. It is a simple and effective technique for real-time systems, but it may result in priority inheritance.