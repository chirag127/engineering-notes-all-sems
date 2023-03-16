## Unit 2 - Distributed Mutual Exclusion

- Distributed mutual exclusion is the problem of ensuring that at most one process in a distributed system can access a shared resource at a time.
- Distributed mutual exclusion algorithms can be classified into two categories: permission-based and token-based.
- Permission-based algorithms require a process to obtain permission from other processes before entering the critical section. Examples of permission-based algorithms are Ricart-Agrawala algorithm, Lamport's algorithm, and Maekawa's algorithm.
- Token-based algorithms use a special message, called a token, that grants the right to enter the critical section. A process can enter the critical section only if it has the token. Examples of token-based algorithms are Suzuki-Kasami algorithm, Raymond's algorithm, and Singhal's algorithm.
- The performance of distributed mutual exclusion algorithms can be measured by the following metrics: message complexity, synchronization delay, and fairness.
- Message complexity is the number of messages exchanged per critical section access.
- Synchronization delay is the time elapsed between a process requesting the critical section and entering it.
- Fairness is the degree to which the algorithm ensures that every process gets a fair chance to enter the critical section.