# Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- Four requirements must be met for a deadlock to occur:
  - Mutual exclusion: each resource can be assigned to only one process at a time.
  - Hold and wait: a process holding a resource can request additional resources without releasing the ones it already holds.
  - No preemption: a resource can be released only by the process that holds it, voluntarily or after completing its task.
  - Circular wait: there exists a circular chain of processes, each of which is waiting for a resource held by the next process in the chain.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing its execution.
- The main difference between resource deadlocks and communication deadlocks is that in resource deadlocks, the resources are passive entities that do not initiate any action, whereas in communication deadlocks, the resources are active entities that can send and receive messages.
- Another difference is that in resource deadlocks, the processes are aware of the resources they need and request them explicitly, whereas in communication deadlocks, the processes are unaware of the messages they need and wait for them implicitly.
- A third difference is that in resource deadlocks, the processes can release the resources they hold at any time, whereas in communication deadlocks, the processes cannot release the messages they hold until they receive a reply.
- A fourth difference is that in resource deadlocks, the processes can detect the deadlock by examining the resource allocation graph, whereas in communication deadlocks, the processes cannot detect the deadlock by examining the message passing graph.
- A fifth difference is that in resource deadlocks, the deadlock can be resolved by aborting one or more processes or preempting one or more resources, whereas in communication deadlocks, the deadlock can be resolved by sending dummy messages or breaking the circular wait.