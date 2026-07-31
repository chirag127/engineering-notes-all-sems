### Deadlock characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock can be characterized by four necessary conditions:
  - **Mutual exclusion**: Each resource is either allocated to one process or available.
  - **Hold and wait**: A process holding at least one resource is waiting to acquire additional resources held by other processes.
  - **No preemption**: A resource can be released only voluntarily by the process holding it, after that process has completed its task.
  - **Circular wait**: There exists a set of waiting processes such that P0 is waiting for a resource that is held by P1, P1 is waiting for a resource that is held by P2, ..., Pn-1 is waiting for a resource that is held by Pn, and Pn is waiting for a resource that is held by P0.
- A deadlock can be prevented by ensuring that at least one of the four necessary conditions does not hold.
- A deadlock can be avoided by using a resource-allocation algorithm that ensures that the system will always remain in a safe state, where there is a possibility of avoiding deadlock.
- A deadlock can be detected by using an algorithm that examines the current state of the system and checks if there is a cycle in the resource allocation graph.
- A deadlock can be recovered by using one of the following methods:
  - **Process termination**: Aborting one or more processes to break the circular wait.
  - **Resource preemption**: Taking a resource away from a process and giving it to another process, possibly causing the former process to rollback and restart.