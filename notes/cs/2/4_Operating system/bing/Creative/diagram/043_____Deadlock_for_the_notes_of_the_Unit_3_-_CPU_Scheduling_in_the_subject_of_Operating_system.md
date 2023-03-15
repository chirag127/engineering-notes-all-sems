### Deadlock

- A deadlock is a situation in which two or more processes are waiting for each other to release a resource, resulting in both processes ceasing to function .
- A deadlock can occur in a system composed of multiple processes that can access shared resources, such as memory, files, devices, etc.
- A deadlock is said to occur when the following four conditions are met simultaneously:
  - Mutual exclusion: Each resource is either allocated to one process or available.
  - Hold and wait: A process holding at least one resource is waiting for another resource held by some other process.
  - No preemption: A resource cannot be taken away from a process unless the process releases it voluntarily.
  - Circular wait: A set of processes are waiting for each other in a circular chain, such as P1 waits for P2, P2 waits for P3, ..., Pn waits for P1.

- A deadlock can be prevented by ensuring that at least one of the four conditions is not met. For example, by using a resource allocation policy that avoids circular wait, or by allowing preemption of resources.
- A deadlock can be avoided by using a resource allocation algorithm that dynamically checks the possibility of deadlock before granting a request. For example, by using the banker's algorithm or the resource allocation graph algorithm.
- A deadlock can be detected by using a deadlock detection algorithm that periodically checks the system state for the existence of a deadlock. For example, by using the wait-for graph or the matrix algorithm.
- A deadlock can be recovered by using a deadlock recovery algorithm that takes some actions to resolve the deadlock. For example, by aborting one or more processes, or by preempting some resources and rolling back the processes.