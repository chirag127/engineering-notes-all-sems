### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs or transactions.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause inconsistency or deadlock problems.
- Concurrency control is the technique of managing concurrent accesses to data objects by jobs or transactions, while ensuring data consistency, timing constraints, and system performance.
- Concurrency control can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking data objects before accessing them. Examples of pessimistic concurrency control protocols are priority ceiling protocol, affected set priority ceiling protocol, and convex ceiling protocol.
  - Optimistic concurrency control allows conflicts to occur and resolves them by aborting or restarting transactions. Examples of optimistic concurrency control protocols are wait-free protocol, timestamp ordering protocol, and multiversion protocol.
- Concurrency control protocols should consider the temporal characteristics of data objects, such as deadlines, validity, and freshness, as well as the temporal constraints of jobs or transactions, such as deadlines, priorities, and criticality.