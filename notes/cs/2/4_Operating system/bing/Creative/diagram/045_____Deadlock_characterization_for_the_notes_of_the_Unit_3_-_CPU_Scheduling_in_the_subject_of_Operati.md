### Deadlock Characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock occurs if the four Coffman conditions hold true. They are given as follows:
  - **Mutual exclusion**: Each resource is either allocated to one process or available.
  - **No preemption**: A resource can be released only voluntarily by the process holding it.
  - **Hold and wait**: A process holding at least one resource is waiting to acquire additional resources held by other processes.
  - **Circular wait**: There exists a set of waiting processes such that each process is waiting for a resource that is held by another process in the set.
- These conditions are not mutually exclusive. They are necessary but not sufficient for a deadlock to occur.
- A deadlock can be described using a directed graph called a **resource-allocation graph**. This graph consists of a set of vertices and a set of edges. The vertices can be divided into two types: **processes** and **resources**. The edges can be divided into two types: **request** and **assignment**.
  - A request edge P → R indicates that process P has requested resource R and is waiting for it.
  - An assignment edge R → P indicates that resource R has been allocated to process P.
  - A cycle in the graph implies the possibility of a deadlock. A cycle is necessary but not sufficient for a deadlock to occur.
- A deadlock can be prevented by ensuring that at least one of the Coffman conditions does not hold. This can be done by using various techniques such as resource ordering, resource preallocation, resource revocation, etc.
- A deadlock can be avoided by ensuring that the system will always remain in a safe state. A safe state is one where there exists a safe sequence of processes that can finish without causing a deadlock. A safe state can be determined by using various algorithms such as Banker's algorithm, Resource-allocation graph algorithm, etc.
- A deadlock can be detected by periodically checking for cycles in the resource-allocation graph or by using a matrix representation of the allocation and request of resources. If a deadlock is detected, the system can recover by using various methods such as process termination, resource preemption, rollback, etc.