## Unit 2 - Distributed Mutual Exclusion

Distributed mutual exclusion is a problem in distributed computing systems, where multiple processes need to access a shared resource or data in a mutually exclusive manner, that is, only one process can execute the critical section at any given time. In a distributed system, shared variables or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.

There are three basic approaches for implementing distributed mutual exclusion:

- Token-based algorithms: A special message, called a token, is passed among the processes in a logical ring. Only the process that holds the token can enter the critical section. Examples of token-based algorithms are Suzuki-Kasami's algorithm, Raymond's algorithm, and Maekawa's algorithm.
- Permission-based algorithms: A process that wants to enter the critical section must request permission from a set of processes, called the voting set. The process can enter the critical section only if it receives permission from all the processes in the voting set. Examples of permission-based algorithms are Ricart-Agrawala's algorithm, Lamport's algorithm, and Singhal's algorithm.
- Quorum-based algorithms: A process that wants to enter the critical section must request permission from a subset of processes, called a quorum. The process can enter the critical section only if it receives permission from a majority of the quorum. Examples of quorum-based algorithms are Naimi-Trehel's algorithm, Agrawal-El Abbadi's algorithm, and Thomas's algorithm.

The following diagram illustrates the basic architecture of a distributed mutual exclusion system, where each process has a local state and communicates with other processes through message passing. The diagram also shows an example of a token-based algorithm, where the token is passed in a clockwise direction among the processes.

```
+--------+     +--------+     +--------+
|        |     |        |     |        |
|  P1    |     |  P2    |     |  P3    |
|        |     |        |     |        |
+--------+     +--------+     +--------+
   |  ^           |  ^           |  ^
   |  |           |  |           |  |
   v  |           v  |           v  |
+--------+     +--------+     +--------+
|        |     |        |     |        |
|  P4    |     |  P5    |     |  P6    |
|        |     |        |     |        |
+--------+     +--------+     +--------+

Token: P4 -> P5 -> P6 -> P1 -> P2 -> P3 -> P4 -> ...
```