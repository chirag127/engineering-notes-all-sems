## Unit 5 - Concurrency Control Techniques

Concurrency control is a critical aspect of database management, as it involves managing multiple users accessing and modifying data in a shared database simultaneously. In this unit, we will explore various concurrency control techniques used in relational databases.

### Lock-based Concurrency Control

Lock-based concurrency control is the most widely used technique for managing concurrent access to a shared database. It involves acquiring a lock on a resource before accessing it and releasing it once the operation is complete. There are two types of locks:

- Shared Lock: allows multiple users to read the resource but not modify it.
- Exclusive Lock: allows only one user to modify the resource while preventing others from accessing it.

Lock-based concurrency control provides strong consistency and ensures that concurrent transactions do not interfere with each other. However, it can lead to a high degree of contention and may result in deadlocks.

### Timestamp-based Concurrency Control

Timestamp-based concurrency control uses timestamps to determine the order of transactions and ensure that transactions do not interfere with each other. Each transaction is assigned a unique timestamp, and the database maintains a global clock that is incremented after each transaction. When a transaction tries to access a resource, its timestamp is compared with the timestamp of the last transaction that accessed the resource. If the transaction's timestamp is older, it is rolled back. Otherwise, it can proceed.

Timestamp-based concurrency control is more efficient than lock-based concurrency control and can handle a higher degree of concurrency. However, it requires a lot of overhead to maintain timestamps and may result in cascading rollbacks.

### Multi-version Concurrency Control

Multi-version concurrency control (MVCC) is a technique that allows multiple versions of a resource to coexist in the database. Each transaction gets a snapshot of the database, which includes all versions of the resources that exist at the time of the snapshot. When a transaction modifies a resource, a new version is created, and the old version remains intact for other transactions to access.

MVCC allows for a high degree of concurrency and reduces contention. However, it requires a lot of overhead to manage multiple versions of resources and may result in increased storage requirements.

### Optimistic Concurrency Control

Optimistic concurrency control (OCC) assumes that conflicts between transactions are rare and allows transactions to proceed without acquiring locks. When a transaction tries to commit, the database checks whether the transaction has modified any resources that have been modified by other transactions since the transaction's snapshot was taken. If there are no conflicts, the transaction is committed. Otherwise, it is rolled back.

OCC provides high concurrency and reduces overhead, but it can result in a high rate of rollbacks and may not be suitable for applications with high contention.

### Conclusion

Concurrency control is a vital aspect of database management and involves managing concurrent access to a shared database. Lock-based concurrency control, timestamp-based concurrency control, multi-version concurrency control, and optimistic concurrency control are some of the techniques used to ensure data consistency and prevent conflicts between transactions. Each technique has its advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.