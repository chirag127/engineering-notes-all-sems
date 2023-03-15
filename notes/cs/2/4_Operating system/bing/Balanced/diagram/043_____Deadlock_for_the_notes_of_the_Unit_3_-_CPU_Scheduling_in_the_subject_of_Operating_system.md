### Deadlock

- A deadlock is a situation in which a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.
- Deadlocks are a common problem in multiprocessing systems, parallel computing, and distributed systems, because in these contexts systems often use software or hardware locks to arbitrate shared resources and implement process synchronization.
- A deadlock can occur if the following four conditions hold simultaneously:
  - **Mutual exclusion**: At least one resource must be held in a non-sharable mode, that is, only one process can use the resource at a time.
  - **Hold and wait**: A process must be holding at least one resource and waiting for one or more additional resources that are currently being held by other processes.
  - **No preemption**: A resource can be released only voluntarily by the process holding it, after the process has completed its task.
  - **Circular wait**: A set of processes must exist such that each process is waiting for a resource that is held by another process in the set, which in turn is waiting for another resource, and so on, forming a circular chain.
- Deadlocks can be prevented by ensuring that at least one of the four conditions does not hold. Some of the methods for deadlock prevention are  :
  - **Resource allocation graph**: A directed graph that depicts the allocation of resources to processes. A deadlock exists if and only if the graph contains a cycle.
  - **Resource ordering**: A global ordering of all resource types is defined, and each process requests resources in an increasing order of enumeration.
  - **Maximal parallelism**: A process requests all the resources it needs at once, and does not start execution until it acquires all of them.
  - **Wait-die and wound-wait schemes**: A process that requests a resource held by another process is either allowed to wait or aborted, based on the relative ages of the processes.
  - **Banker's algorithm**: A resource allocation and deadlock avoidance algorithm that tests for safety by simulating the allocation of resources to processes and checking if the system can reach a safe state.