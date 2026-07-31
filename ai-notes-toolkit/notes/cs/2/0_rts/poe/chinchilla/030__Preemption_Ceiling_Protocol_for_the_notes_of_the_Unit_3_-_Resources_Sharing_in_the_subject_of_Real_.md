### Preemption Ceiling Protocol

The Preemption Ceiling Protocol is a resource sharing protocol used in real-time systems to ensure mutual exclusion and avoid priority inversion. It is designed to guarantee that a high-priority task will not be preempted by a lower-priority task while it is accessing a shared resource.

The protocol works by associating each shared resource with a preemption ceiling value, which is the maximum priority of any task that can potentially access the resource. This preemption ceiling value is computed by analyzing the critical sections of the code that access the shared resource.

The following are the key features of the Preemption Ceiling Protocol:

1. Priority Inheritance: When a higher-priority task is blocked waiting for a shared resource held by a lower-priority task, the lower-priority task inherits the priority of the higher-priority task until it releases the shared resource.

2. Priority Ceiling: If a higher-priority task needs to access a shared resource that is already held by a lower-priority task, it can preempt the lower-priority task only if its priority is higher than the preemption ceiling value of the shared resource.

3. Deadlock Avoidance: The protocol ensures that deadlock does not occur by guaranteeing that a task cannot block a higher-priority task by holding a shared resource.

4. Overhead: The protocol requires additional overhead for maintaining the preemption ceiling values and the priority inheritance mechanism.

5. Implementation: The protocol can be implemented in software or hardware, and it requires support from the operating system or the real-time kernel.

In summary, the Preemption Ceiling Protocol is a resource sharing protocol that provides mutual exclusion, priority inversion avoidance, priority inheritance, and deadlock avoidance in real-time systems. It is a widely used protocol in real-time systems to ensure that high-priority tasks are not blocked by lower-priority tasks accessing shared resources.