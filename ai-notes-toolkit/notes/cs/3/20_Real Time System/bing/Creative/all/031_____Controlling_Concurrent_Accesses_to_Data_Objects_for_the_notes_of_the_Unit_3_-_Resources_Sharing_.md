# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timeliness.
- Concurrency control algorithms for real time systems can be classified into two categories: locking-based and optimistic.
- Locking-based algorithms use locks to grant exclusive access to data objects to one job at a time. They can be further divided into static and dynamic locking algorithms.
- Static locking algorithms assign locks to data objects before the execution of jobs, based on their priority or deadline. Examples of static locking algorithms are priority ceiling protocol (PCP) and immediate ceiling protocol (ICP).
- Dynamic locking algorithms assign locks to data objects during the execution of jobs, based on their requests or conflicts. Examples of dynamic locking algorithms are wait-free protocol (WFP) and wound-wait protocol (WWP).
- Optimistic algorithms allow concurrent accesses to data objects without locks, but detect and resolve conflicts after the accesses. They can be further divided into validation-based and compensation-based algorithms.
- Validation-based algorithms check the validity of the accessed data objects at the end of the jobs, and abort and restart the jobs if they are invalid. Examples of validation-based algorithms are optimistic concurrency control (OCC) and timestamp ordering (TO).
- Compensation-based algorithms compensate for the effects of the accessed data objects at the end of the jobs, and update the data objects accordingly. Examples of compensation-based algorithms are compensation-based concurrency control (CCC) and compensation-based timestamp ordering (CTO).
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the data consistency requirements, the timing constraints, the workload, and the operating environment.