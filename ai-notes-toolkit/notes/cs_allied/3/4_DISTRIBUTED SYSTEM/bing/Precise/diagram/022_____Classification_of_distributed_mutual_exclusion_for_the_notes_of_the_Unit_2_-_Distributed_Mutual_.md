### Classification of Distributed Mutual Exclusion

Distributed mutual exclusion is a fundamental problem in distributed systems, where multiple processes need to access shared resources in a mutually exclusive manner. There are several algorithms that have been proposed to solve this problem, and they can be broadly classified into two categories: 

1. **Token-based algorithms**: In this approach, a unique token is circulated among the processes in the system. Only the process that holds the token is allowed to enter the critical section and access the shared resource. Examples of token-based algorithms include the Suzuki-Kasami algorithm and the Raymond's tree-based algorithm.

2. **Permission-based algorithms**: In this approach, a process that wants to enter the critical section must request permission from other processes in the system. The process is allowed to enter the critical section only if it receives permission from all the other processes. Examples of permission-based algorithms include the Ricart-Agrawala algorithm and the Maekawa's algorithm.

These algorithms differ in their performance, message complexity, and fault-tolerance. The choice of algorithm depends on the specific requirements of the distributed system.