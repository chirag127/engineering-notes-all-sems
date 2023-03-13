Avoidance is a strategy for handling deadlocks in distributed systems that tries to ensure that the system is always in a safe state, meaning that there is a possible sequence of resource allocation and release that leads to the completion of all processes. Avoidance requires that the system has some knowledge of the current and future resource requests and releases of each process, and that it denies or delays any request that could lead to an unsafe state.

One of the methods for deadlock avoidance in distributed systems is the **banker's algorithm**, which is based on the analogy of a bank that grants loans to customers and checks their credit before doing so. The banker's algorithm works as follows:

- Each process must declare the maximum number of instances of each resource type that it may need.
- The system keeps track of the total number of instances of each resource type, the number of instances allocated to each process, and the number of instances available.
- When a process requests some instances of a resource type, the system checks if granting the request will leave the system in a safe state. If yes, the request is granted; if no, the request is postponed until a later time.
- When a process releases some instances of a resource type, the system updates the number of instances available and checks if any of the postponed requests can now be granted.

The following diagram illustrates the basic architecture of a distributed system that uses the banker's algorithm for deadlock avoidance:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Process P1     |      |  Process P2     |      |  Process Pn     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Resource R1    |      |  Resource R2    |      |  Resource Rm    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Banker         |      |  Banker         |      |  Banker         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              v
+-----------------+
|                 |
|  Coordinator    |
|                 |
+-----------------+
```

In this diagram, each process Pi communicates with the resources Rj that it needs, and also with the corresponding bankers Bj that manage the allocation of those resources. The bankers Bj communicate with each other and with a coordinator C that decides whether to grant or deny the requests based on the global state of the system. The coordinator C maintains the information about the total, allocated, and available instances of each resource type, as well as the maximum needs of each process. The coordinator C uses the banker's algorithm to check the safety of the system and to avoid deadlocks.