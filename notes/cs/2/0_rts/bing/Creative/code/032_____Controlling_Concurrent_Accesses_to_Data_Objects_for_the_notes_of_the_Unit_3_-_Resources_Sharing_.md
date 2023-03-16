### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause inconsistency and corruption of data.
- To ensure data consistency and avoid data conflicts, concurrency control mechanisms are needed to regulate the concurrent accesses to data objects.
- Concurrency control mechanisms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control mechanisms prevent data conflicts by enforcing mutual exclusion among conflicting accesses to data objects.
  - Optimistic concurrency control mechanisms allow data conflicts to occur, but detect and resolve them before committing the transactions.
- Concurrency control mechanisms for real time systems should also consider the timing constraints of the transactions, and guarantee the completion of critical transactions.
- Some examples of concurrency control mechanisms for real time systems are:
  - Priority inheritance protocol: a pessimistic protocol that allows a lower priority job to inherit the priority of a higher priority job that is blocked by it, and release the inherited priority when the blocking is resolved.
  - Priority ceiling protocol: a pessimistic protocol that assigns a priority ceiling to each data object, and prevents a job from accessing a data object if its priority is lower than the current system ceiling, which is the maximum of the priority ceilings of all the data objects currently accessed.
  - Convex ceiling protocol: a pessimistic protocol that assigns a convex ceiling function to each data object, and prevents a job from accessing a data object if its priority is lower than the value of the convex ceiling function at the current system time.
  - Wait-free protocol: an optimistic protocol that allows a job to access a data object without waiting, but uses a validation function to check if the data object is consistent before committing the transaction.
  - Earliest-deadline-first commit protocol: an optimistic protocol that allows a job to access a data object without waiting, but uses the deadline of the transaction as the commit priority, and aborts the transaction if it conflicts with a higher priority transaction.