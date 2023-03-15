### Deadlock Characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock can be characterized by four necessary conditions:
  - **Mutual exclusion**: Each resource is either allocated to one process or available.
  - **Hold and wait**: A process holding at least one resource is waiting to acquire additional resources held by other processes.
  - **No preemption**: A resource can be released only voluntarily by the process holding it, after that process has completed its task.
  - **Circular wait**: There exists a set of waiting processes {P0, P1, ..., Pn} such that P0 is waiting for a resource that is held by P1, P1 is waiting for a resource that is held by P2, ..., Pn is waiting for a resource that is held by P0.
- These four conditions are necessary and sufficient for a deadlock to occur. If one of them is not satisfied, then a deadlock cannot occur.