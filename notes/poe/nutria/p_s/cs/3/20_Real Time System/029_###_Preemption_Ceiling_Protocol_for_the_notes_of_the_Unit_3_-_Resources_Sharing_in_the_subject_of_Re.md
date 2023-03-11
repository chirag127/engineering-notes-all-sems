
### Preemption Ceiling Protocol

The Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems. This protocol is used to ensure that tasks with higher priority are allocated resources before tasks with lower priority. In order to achieve this, the protocol uses a preemption ceiling that defines the maximum priority that a task can obtain.

#### Advantages

- Prevents low-priority tasks from monopolizing resources.
- Allows high-priority tasks to be allocated resources more quickly.
- Ensures fairness in resource allocation.

#### Disadvantages

- If a high-priority task is assigned a preemption ceiling that is too low, it may not be able to obtain the resources it needs in a timely manner.
- If the preemption ceiling is set too high, low-priority tasks may not be able to obtain the resources they need.

#### Applications

The Preemption Ceiling Protocol is commonly used in embedded systems, such as those used in automotive and aerospace applications. It is also used in operating systems, where it is used to ensure that critical tasks are allocated resources before non-critical tasks.

#### Examples

In a real-time system, a high-priority task may be assigned a preemption ceiling of 4. This means that this task will be allocated resources before any task with a priority of 5 or higher. Similarly, a low-priority task may be assigned a preemption ceiling of 9, meaning that it will be allocated resources after any task with a priority of 8 or lower.