## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is a fundamental problem in distributed computing systems .
- It ensures that concurrent access of processes to a shared resource or data is serialized, that is, executed in a mutually exclusive manner  .
- It states that only one process is allowed to execute the critical section (CS) at any given time .
- In a distributed system, shared variables (semaphores) or a local kernel cannot be used to implement mutual exclusion. Message passing is the sole means for implementing distributed mutual exclusion.
- Distributed mutual exclusion algorithms can be classified into two categories: permission-based and token-based .
- Permission-based algorithms require a process to obtain permission from other processes before entering the CS. They can be further divided into centralized, distributed, and hierarchical algorithms .
- Token-based algorithms use a special message, called a token, that circulates among the processes and grants the right to enter the CS. They can be further divided into ring-based, tree-based, and graph-based algorithms .
- The performance of distributed mutual exclusion algorithms can be evaluated based on several criteria, such as message complexity, synchronization delay, fault tolerance, and fairness .