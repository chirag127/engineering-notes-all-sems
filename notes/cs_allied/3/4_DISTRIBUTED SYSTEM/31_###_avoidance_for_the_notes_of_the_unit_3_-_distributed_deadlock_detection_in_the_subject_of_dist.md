### avoidance for the notes of the Unit 3 - Distributed Deadlock Detection in the subject of DISTRIBUTED SYSTEM

Deadlock avoidance is a technique used to prevent deadlocks from occurring in a distributed system. It involves making decisions about resource allocation in advance, based on the current state of the system, to ensure that a deadlock cannot occur.

Deadlock avoidance is achieved by using a resource allocation algorithm that ensures that the necessary conditions for a deadlock to occur are never met. The algorithm takes into account the current state of the system, including the processes and resources, and makes decisions about resource allocation based on this information.

There are two main approaches to deadlock avoidance in a distributed system:

1. Resource ordering: This approach involves defining a global ordering of resources and allocating resources to processes based on this ordering.

2. Banker's algorithm: This approach involves allocating resources to processes based on the maximum number of resources that a process may need in the future.

Deadlock avoidance is an effective way to prevent deadlocks from occurring in a distributed system, but it has some limitations. For example, it may result in lower resource utilization, as resources are reserved in advance even if they are not needed. Additionally, it may be difficult to determine the maximum number of resources that a process may need in the future.

In conclusion, deadlock avoidance is a useful technique for preventing deadlocks in a distributed system, but it is important to consider the trade-offs between the benefits and limitations of this approach when designing and implementing a distributed system.
