### Avoidance and detection for the notes of the Unit 3 - CPU Scheduling in the subject of Operating system

- Avoidance and detection are two strategies to deal with the problem of deadlock in operating systems.
- Deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Avoidance is a proactive approach that prevents deadlock from occurring by ensuring that the system is always in a safe state.
- A safe state is one where there is at least one sequence of resource allocation that does not lead to deadlock.
- To use avoidance, the operating system needs to know in advance the maximum number of resources that each process may request and the current allocation of resources to each process.
- The operating system can then use an algorithm, such as the Banker's algorithm, to determine whether granting a resource request will keep the system in a safe state or not.
- If the request will lead to an unsafe state, the operating system can deny or postpone the request until a safe state is restored.
- Detection is a reactive approach that allows deadlock to occur but then detects and resolves it.
- To use detection, the operating system needs to maintain information about the current allocation of resources to each process and the waiting requests of each process.
- The operating system can then use an algorithm, such as the wait-for graph or the matrix algorithm, to check whether there is a cycle of processes waiting for each other's resources.
- If a cycle is found, the operating system can apply a recovery method, such as aborting or preempting some processes, to break the cycle and free the resources.
- Detection and recovery may involve more overhead and complexity than avoidance, but they are more flexible and adaptable to dynamic and unpredictable resource requests.
- The choice of strategy depends on the specific requirements and characteristics of the system, such as the number and type of resources, the frequency and duration of requests, and the performance and reliability goals.