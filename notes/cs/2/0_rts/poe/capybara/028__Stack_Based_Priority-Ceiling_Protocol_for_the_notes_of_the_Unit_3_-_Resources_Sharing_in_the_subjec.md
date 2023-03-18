### Stack Based Priority-Ceiling Protocol

The Stack Based Priority-Ceiling Protocol (PCP) is a resource-sharing protocol used in Real-Time Systems. It is designed to avoid priority inversion by assigning a priority ceiling to each shared resource. Here are some key points to understand this protocol:

- The PCP is a lock-based protocol, which means that it uses locks to protect shared resources from simultaneous access by multiple tasks.
- Each shared resource is associated with a priority ceiling, which is the highest priority of all tasks that may access the resource. This priority ceiling is used to temporarily boost the priority of a task that holds the lock for the resource.
- When a task requests a lock on a shared resource, its priority is raised to the priority ceiling of the resource. This ensures that no higher-priority task can preempt it while it holds the lock.
- If a task attempts to acquire a lock while another task is holding it, the priority of the waiting task is raised to the priority ceiling of the resource. This prevents priority inversion, where a higher-priority task is blocked by a lower-priority task holding a shared resource.
- The PCP is stack-based because it uses a stack to keep track of the priority ceilings of nested locks. When a task acquires a lock, its priority is raised to the priority ceiling of the lock. If the task then acquires another lock for a resource with a higher priority ceiling, its priority is raised again to the new ceiling. The original ceiling is pushed onto the stack, and the current ceiling becomes the new one.
- When a task releases a lock, its priority is lowered to the highest priority ceiling remaining on the stack. If there are no more ceilings on the stack, the priority is lowered to its base priority.

In conclusion, the Stack Based Priority-Ceiling Protocol is an effective way to prevent priority inversion in Real-Time Systems. It assigns priority ceilings to shared resources and uses a stack to keep track of nested locks. By temporarily boosting the priority of a task holding a lock, it ensures that no higher-priority task can preempt it.