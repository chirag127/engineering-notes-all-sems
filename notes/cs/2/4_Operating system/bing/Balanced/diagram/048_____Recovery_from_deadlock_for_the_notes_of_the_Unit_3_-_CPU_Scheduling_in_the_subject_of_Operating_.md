### Recovery from deadlock

- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- To recover from deadlock, there are two methods: deadlock prevention and deadlock avoidance.
- Deadlock prevention is a technique to ensure that at least one of the four necessary conditions for deadlock does not hold. These conditions are: mutual exclusion, hold and wait, no preemption, and circular wait.
- Deadlock avoidance is a technique to ensure that the system will always remain in a safe state, where there is at least one possible sequence of resource allocation that does not lead to deadlock. This can be done by using a resource-allocation graph or a banker's algorithm.
- If deadlock prevention or avoidance is not used, then deadlock detection and recovery must be employed. This involves periodically checking the system for a cycle of waiting processes, and then taking some actions to break the cycle, such as terminating or preempting some processes, or rolling back their state.