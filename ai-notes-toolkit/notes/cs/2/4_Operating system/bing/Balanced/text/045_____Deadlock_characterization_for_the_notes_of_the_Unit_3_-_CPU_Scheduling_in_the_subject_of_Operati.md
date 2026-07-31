### Deadlock characterization

- A deadlock is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- A deadlock can be characterized by four necessary conditions:
  - Mutual exclusion: At least one resource must be held in a non-sharable mode, that is, only one process can use the resource at a time.
  - Hold and wait: A process must be holding at least one resource and waiting to acquire additional resources that are currently being held by other processes.
  - No preemption: A resource can be released only voluntarily by the process holding it, after the process has completed its task.
  - Circular wait: A set of processes must exist such that each process is waiting for a resource that is held by another process in the set, which in turn is waiting for another resource, and so on, forming a circular chain.
- These conditions are necessary but not sufficient for a deadlock to occur, that is, if a system does not satisfy any one of these conditions, then a deadlock cannot occur. However, satisfying these conditions does not guarantee that a deadlock will occur, as it depends on the order and timing of requests and releases of resources.