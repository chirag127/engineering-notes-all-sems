### Resource Vs Communication Deadlocks

- A deadlock is a condition where a process cannot proceed because it needs to obtain a resource held by another process, and it itself is holding a resource that the other process needs.
- There are two types of deadlocks in distributed systems: resource deadlocks and communication deadlocks.
- Resource deadlocks occur when processes access resources, such as data objects in database systems and buffers in store and forward communication networks. A process acquires a resource before accessing it and releasing it after using it. A resource deadlock happens when a process is waiting for a resource that is held by another process, and vice versa.
- Communication deadlocks occur when processes exchange messages, such as in message passing systems and distributed algorithms. A process sends a message to another process and waits for a reply before continuing. A communication deadlock happens when a process is waiting for a message that is never sent by another process, and vice versa.
- The main difference between resource deadlocks and communication deadlocks is that resource deadlocks involve contention for resources, while communication deadlocks involve loss or corruption of messages.
- Another difference is that resource deadlocks can be detected by analyzing the resource allocation graph, while communication deadlocks can be detected by analyzing the wait-for graph.
- A resource allocation graph is a directed graph where the nodes represent processes and resources, and the edges represent requests and assignments of resources. A cycle in the graph indicates a resource deadlock.
- A wait-for graph is a directed graph where the nodes represent processes, and the edges represent waiting for messages. A cycle in the graph indicates a communication deadlock.
- An example of a resource allocation graph and a wait-for graph is shown below:

```markdown
Resource allocation graph:

P1 -> R1 -> P2 -> R2 -> P1

Wait-for graph:

P1 -> P2 -> P3 -> P1
```

- In the resource allocation graph, P1 and P2 are deadlocked because they are holding R1 and R2 respectively, and requesting R2 and R1 respectively.
- In the wait-for graph, P1, P2, and P3 are deadlocked because they are waiting for messages from each other.