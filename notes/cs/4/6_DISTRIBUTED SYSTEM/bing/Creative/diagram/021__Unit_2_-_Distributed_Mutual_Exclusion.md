## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a problem of ensuring that only one process in a distributed system can access a shared resource or data at a time. It is different from mutual exclusion in a single computer system, where shared variables or semaphores can be used to control the access. In a distributed system, message passing is the only way to implement distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based approach: A unique token is shared among all the processes. A process can enter its critical section only if it has the token. The token is passed from one process to another according to some algorithm. This approach ensures mutual exclusion because the token is unique. An example of this approach is the Suzuki-Kasami's broadcast algorithm.
- Non-token-based approach: A process communicates with other processes to determine which process can enter the critical section next. This requires exchange of two or more rounds of messages among processes. This approach does not rely on a single token, but it may incur more communication overhead. An example of this approach is the Ricart-Agrawala's algorithm.
- Quorum-based approach: A process requests permission from a subset of processes (called a quorum) to enter the critical section. If the majority of the quorum grants permission, the process can enter the critical section. This approach reduces the number of messages needed, but it may introduce conflicts among quorums. An example of this approach is the Maekawa's algorithm.

The following diagram illustrates the basic architecture of a distributed system with four processes (P1, P2, P3, P4) and a shared resource (R). The arrows represent the message passing among processes.

```
    +----+      +----+
    | P1 |      | P2 |
    +----+      +----+
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
+-----+-----+-----+-----+
|     |     |     |     |
| P3  |  R  | P4  | P1  |
|     |     |     |     |
+-----+-----+-----+-----+
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
    +----+      +----+
    | P4 |      | P3 |
    +----+      +----+
```