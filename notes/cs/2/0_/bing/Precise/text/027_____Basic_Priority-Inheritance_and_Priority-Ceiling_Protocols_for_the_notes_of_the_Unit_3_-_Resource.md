### Basic Priority-Inheritance and Priority-Ceiling Protocols

Priority-Inheritance and Priority-Ceiling Protocols are used in real-time systems to manage resource sharing and prevent priority inversion. Here are some key points to remember:

1. **Priority Inversion** occurs when a low-priority task holds a resource that a high-priority task needs, causing the high-priority task to be blocked and the low-priority task to continue executing.
2. **Priority-Inheritance Protocol (PIP)** is a solution to priority inversion where the low-priority task inherits the priority of the highest-priority task that is blocked by it. This allows the low-priority task to complete and release the resource, unblocking the high-priority task.
3. **Priority-Ceiling Protocol (PCP)** is another solution to priority inversion where each resource is assigned a priority ceiling, which is the highest priority of any task that may access the resource. A task can only access a resource if its priority is higher than the current priority ceiling of the resource.
4. **Basic Priority Ceiling Protocol (BPCP)** is a variant of PCP where the priority ceiling of a resource is the highest priority of any task that may access the resource, regardless of whether the task is currently blocked or not.
5. Both PIP and PCP can prevent priority inversion, but PCP has the added benefit of preventing deadlock and reducing blocking time.

These are some basic concepts of Priority-Inheritance and Priority-Ceiling Protocols for resource sharing in real-time systems. It is important to understand these concepts for the Unit 3 - Resources Sharing in the subject of Real Time System.