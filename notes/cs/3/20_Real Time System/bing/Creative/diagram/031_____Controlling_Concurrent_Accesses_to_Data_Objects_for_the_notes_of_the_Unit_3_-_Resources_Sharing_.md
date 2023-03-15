### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- Data objects have consistency requirements that must be maintained by the concurrency control mechanism.
- Concurrency control is the process of coordinating the concurrent accesses to data objects to ensure data consistency and meet timing constraints.
- Concurrency control can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking data objects before accessing them.
  - Optimistic concurrency control allows conflicts to occur and resolves them by aborting or restarting transactions after accessing data objects.
- Some of the common concurrency control algorithms for real time systems are:
  - Priority inheritance protocol (PIP): A job that is blocked by a lower priority job inherits the priority of the blocked job until it releases the data object.
  - Priority ceiling protocol (PCP): A job can lock a data object only if its priority is higher than the priority ceiling of the data object, which is the highest priority of any job that can access the data object.
  - Convex ceiling protocol (CCP): A job can lock a data object only if its priority is higher than the convex ceiling of the data object, which is the maximum of the priority ceiling of the data object and the current priority of any job that has locked the data object.
  - Earliest deadline first with conflict resolution (EDF-CR): A job can lock a data object only if it has the earliest deadline among all the jobs that can access the data object. If a conflict occurs, the job with the earliest deadline is allowed to proceed and the others are aborted or restarted.
  - Wait-free synchronization (WFS): A job can access a data object without waiting for other jobs by using a versioning scheme. Each data object has multiple versions and each job can read or write a version that is consistent with its timing constraints.
  - Timestamp ordering (TO): A job can access a data object only if its timestamp is smaller than the timestamp of any other job that can access the data object. If a conflict occurs, the job with the smaller timestamp is allowed to proceed and the others are aborted or restarted.