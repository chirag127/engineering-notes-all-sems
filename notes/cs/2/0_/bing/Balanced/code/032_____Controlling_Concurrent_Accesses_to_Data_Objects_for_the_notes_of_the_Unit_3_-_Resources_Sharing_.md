### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in inconsistent or incorrect data values.
- To ensure data consistency and correctness, concurrent accesses to data objects must be controlled by some synchronization mechanisms.
- The synchronization mechanisms must also consider the timing constraints of the jobs, as blocking or delaying a job may cause it to miss its deadline.
- There are different types of synchronization mechanisms for controlling concurrent accesses to data objects, such as:
  - Lock-based protocols: A job must acquire a lock on a data object before accessing it, and release the lock after finishing the access. The lock can be exclusive (for write access) or shared (for read access). There are different lock-based protocols that vary in how they handle lock conflicts, such as priority inheritance, priority ceiling, and convex ceiling protocols.
  - Timestamp-based protocols: A job is assigned a timestamp when it is released, and the timestamp determines the order of access to data objects. A job can access a data object only if its timestamp is smaller than the timestamp of the last writer of the data object. There are different timestamp-based protocols that vary in how they handle timestamp conflicts, such as wait-die, wound-wait, and optimistic protocols.
  - Validation-based protocols: A job can access data objects without any synchronization, but it must validate its read set and write set before committing the changes. The validation ensures that the data values are consistent and no conflicts have occurred. There are different validation-based protocols that vary in how they perform the validation, such as two-phase locking, two-phase commit, and multiversion protocols.
- The choice of synchronization mechanism depends on the characteristics of the real time system, such as the number and type of data objects, the frequency and duration of accesses, the priority and deadline of jobs, and the performance and overhead requirements.
- The synchronization mechanism should aim to achieve the following objectives:
  - Data consistency: The data values should reflect the correct and logical state of the system, and no data corruption or inconsistency should occur due to concurrent accesses.
  - Timing correctness: The jobs should meet their deadlines, and no unnecessary blocking or aborting should occur due to synchronization.
  - Concurrency: The jobs should be able to access data objects concurrently as much as possible, and no unnecessary serialization or waiting should occur due to synchronization.
  - Adaptability: The synchronization mechanism should be able to adapt to changes in the system state, such as workload, resource availability, and failure conditions.
  - Efficiency: The synchronization mechanism should have low overhead in terms of time, space, and communication, and should not degrade the system performance or throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real-Time Database Systems
: Controlling Concurrent Access to Data Objects - Bench Partner
: Concurrency Control in Real-Time Database Systems