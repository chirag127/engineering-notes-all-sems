### Deadlock Characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock occurs if the four Coffman conditions hold true . They are given as follows:
  - **Mutual exclusion**: Each resource is either allocated to one process or available.
  - **No preemption**: A resource can be released only voluntarily by the process holding it.
  - **Hold and wait**: A process holding at least one resource is waiting to acquire additional resources held by other processes.
  - **Circular wait**: There exists a set of waiting processes such that each process is waiting for a resource that is held by another process in the set.
- These conditions are not mutually exclusive. They are necessary but not sufficient for a deadlock to occur.
- In a deadlock, processes never finish executing, and system resources are tied up, preventing other jobs from starting.
- Deadlocks can be classified into two types: **resource deadlocks** and **communication deadlocks**.
  - Resource deadlocks occur when processes compete for scarce resources, such as CPU, memory, disk, printer, etc.
  - Communication deadlocks occur when processes wait for messages from other processes that may never arrive, such as in a distributed system or a network.