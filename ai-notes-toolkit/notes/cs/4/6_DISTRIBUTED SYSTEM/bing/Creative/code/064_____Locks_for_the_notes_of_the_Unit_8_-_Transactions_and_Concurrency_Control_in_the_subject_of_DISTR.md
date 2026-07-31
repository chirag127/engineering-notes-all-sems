# Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A lock is a mechanism that allows only one of the innumerable nodes or processes to access and modify a resource or data that is being shared commonly to prevent execution of the same task twice and also maintain data integrity.
- In distributed systems, locks are used to coordinate access to a shared resource among multiple nodes or processes that may be geographically dispersed or communicate asynchronously.
- Locks can be classified into different types based on the security of lock resources, the granularity of lock resources, the duration of lock holding, and the lock acquisition protocol.
- Some of the common types of locks are:
  - Exclusive locks and shared locks: Exclusive locks allow only one node or process to access and modify a resource, while shared locks allow multiple nodes or processes to access but not modify a resource.
  - Read locks and write locks: Read locks are shared locks that allow reading a resource, while write locks are exclusive locks that allow writing a resource.
  - Binary locks and counting locks: Binary locks have only two states: locked or unlocked, while counting locks have a counter that indicates how many nodes or processes are holding the lock.
  - Pessimistic locks and optimistic locks: Pessimistic locks are acquired before accessing a resource and released after finishing the access, while optimistic locks are acquired after accessing a resource and checked for validity before committing the access.
  - Centralized locks and distributed locks: Centralized locks are managed by a single node or process that acts as a lock manager, while distributed locks are managed by multiple nodes or processes that communicate with each other using a consensus protocol.
- Locks can also be implemented using different techniques, such as:
  - Database locks: Database locks are locks that are provided by a database system to ensure the consistency and isolation of transactions. Database locks can be row-level, table-level, or database-level.
  - Redis locks: Redis locks are locks that are implemented using Redis, a key-value store that supports atomic operations and expiration. Redis locks can be implemented using the SETNX and EXPIRE commands, or using the Redlock algorithm.
  - ZooKeeper locks: ZooKeeper locks are locks that are implemented using ZooKeeper, a distributed coordination service that provides a hierarchical namespace and ephemeral nodes. ZooKeeper locks can be implemented using the sequential ephemeral nodes and the leader election pattern.