### Deadlock

- A deadlock is a situation in which one or more processes are unable to proceed because they are waiting for some resources that are held by other waiting processes .
- Deadlocks can occur in operating systems that allow multiple processes to share resources such as CPU, memory, disk, printer, etc .
- Deadlocks can cause performance degradation, system failure, or user frustration.
- To prevent or avoid deadlocks, the operating system must ensure that at least one of the four necessary conditions for deadlock does not hold:
  - Mutual exclusion: A resource can be assigned to only one process at a time.
  - Hold and wait: A process holding some resources can request additional resources and wait for them.
  - No preemption: A resource cannot be forcibly taken away from a process that is holding it.
  - Circular wait: A set of processes are waiting for resources in a circular chain, such that each process is holding a resource that the next process in the chain needs.
- The operating system can use different strategies to deal with deadlocks, such as:
  - Deadlock prevention: Ensure that at least one of the four necessary conditions does not hold by imposing some constraints on how processes can request and release resources.
  - Deadlock avoidance: Allow the four necessary conditions to hold but dynamically check whether a resource allocation will lead to a deadlock using some algorithms such as Banker's algorithm or resource allocation graph.
  - Deadlock detection and recovery: Allow deadlocks to occur but periodically detect them using some algorithms such as wait-for graph or matrix and then recover from them by terminating or rolling back some processes or preempting some resources.
  - Deadlock ignorance: Do not attempt to prevent, avoid, detect, or recover from deadlocks and assume that they will never occur or are rare enough to be ignored. This is the approach used by most modern operating systems such as Windows and Linux.