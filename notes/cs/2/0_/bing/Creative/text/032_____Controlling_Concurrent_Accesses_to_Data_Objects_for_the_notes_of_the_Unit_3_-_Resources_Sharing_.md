### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or violation of mutual exclusion.
- To ensure data consistency and mutual exclusion, concurrency control algorithms are needed to regulate the concurrent accesses to data objects.
- Concurrency control algorithms for real time systems should consider both data consistency and timing constraints of the jobs.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent data conflicts by locking the data objects before accessing them. They ensure serializability, but may cause blocking, deadlock, or priority inversion.
  - Optimistic algorithms allow data conflicts to occur, but detect and resolve them before committing the transactions. They avoid blocking, deadlock, and priority inversion, but may cause aborts and restarts.
- Some examples of pessimistic algorithms are:
  - Priority inheritance protocol (PIP): When a high priority job is blocked by a low priority job that holds a lock, the low priority job inherits the priority of the high priority job until it releases the lock.
  - Priority ceiling protocol (PCP): Each data object is assigned a priority ceiling, which is the highest priority of any job that can access it. A job can lock a data object only if its priority is higher than the current priority ceiling of the system, which is the highest priority ceiling of any locked data object.
  - Convex ceiling protocol (CCP): Each data object is assigned a convex ceiling, which is a set of priority levels that can access it. A job can lock a data object only if its priority level belongs to the convex ceiling of the data object and is higher than the current priority ceiling of the system.
- Some examples of optimistic algorithms are:
  - Wait-free algorithm: Each job has a private copy of the data objects it accesses, and updates them locally. At the end of the job, it validates its updates with the global data objects, and commits them if there is no conflict.
  - Timestamp ordering algorithm: Each job is assigned a timestamp based on its deadline or arrival time. A job can access a data object only if its timestamp is smaller than the timestamp of the last update to the data object.
  - Multiversion algorithm: Each data object has multiple versions, each with a timestamp and a validity interval. A job can read the latest version of a data object that is valid for its timestamp. A job can write a new version of a data object only if its timestamp is larger than the timestamp of the last version.