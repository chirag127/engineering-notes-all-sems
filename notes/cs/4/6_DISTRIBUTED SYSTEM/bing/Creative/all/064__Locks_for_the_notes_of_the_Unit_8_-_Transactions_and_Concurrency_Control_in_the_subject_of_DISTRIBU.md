### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of same task twice and also maintain data integrity.
- Locks are generally used to monitor and control access to shared resources by multiple threads at the same time. They basically protect data integrity and atomicity in concurrent applications.
- Locks can be classified into two types based on the concurrency control policy: optimistic and pessimistic.
  - Optimistic locks assume that conflicts are rare and allow concurrent access to the resource without blocking. They use a version field on the database record to check if the data has been modified by another process before updating it. If the version is different, the update fails and the process has to retry.
  - Pessimistic locks assume that conflicts are frequent and block access to the resource before operating on it. They use an external system that holds the lock for the process until it releases it. They prevent concurrent updates but also introduce latency and potential deadlocks.
- Locks can also be classified into two types based on the security of lock resources: distributed systems based on asynchronous replication and distributed systems based on consensus.
  - Distributed systems based on asynchronous replication, such as MySQL, Tair, and Redis, use a single instance or a master-slave cluster to provide locks. They have low latency and high availability, but they may lose data consistency in case of network partitions or node failures.
  - Distributed systems based on consensus, such as ZooKeeper, etcd, and Consul, use a quorum of nodes to provide locks. They have strong consistency and fault tolerance, but they have higher latency and lower availability than asynchronous replication systems.
- A common algorithm to implement distributed locks with Redis is called Redlock. It involves the following steps:
  - The process tries to acquire the lock on N Redis nodes, using the same key and a random value. It sets a time to live (TTL) on the key to avoid holding the lock forever.
  - The process checks how many nodes granted the lock. If the majority of the nodes (N/2 + 1) did, the process considers the lock acquired.
  - The process performs the intended operation on the resource, making sure it does not exceed the lock TTL.
  - The process releases the lock on all the nodes, using the random value to avoid deleting a lock created by another process.
  - The process uses a fencing token, which is a monotonically increasing number, to ensure that only the current lock holder can release the lock. The token is passed to the lock manager when acquiring and releasing the lock.
- A mnemonic to remember the steps of Redlock is: **A**cquire, **C**heck, **O**perate, **R**elease, **F**ence. The acronym is **ACORF**.