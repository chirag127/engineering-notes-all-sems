# Concurrency Control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.

## Concurrency Control in Real-Time Database

A real-time database is a database that supports applications that have timing constraints on their data and transactions. For example, a real-time database may be used for air traffic control, industrial automation, or online gaming. A real-time database must provide timely and consistent data access to meet the deadlines and quality of service requirements of the real-time applications.

Concurrency control in real-time database is about ensuring non-interference among transactions by restricting concurrent transactions to be serializable. A concurrent execution of a set of transactions is said to be serializable if and only if the database operations carried out by them is equivalent to some serial execution of these transactions.

However, serializability alone is not sufficient for real-time database, as it does not consider the timing constraints of the transactions. A real-time database must also ensure that transactions meet their deadlines, which may be hard or soft. A hard deadline is a deadline that must be met by the transaction, otherwise the system may fail or cause serious consequences. A soft deadline is a deadline that can be missed by the transaction, but the system performance or quality may degrade.

Therefore, concurrency control in real-time database must balance between data consistency and timing constraints, and adapt to the changes in the operating environment and the workload. Some of the challenges and issues in concurrency control in real-time database are:

- How to assign priorities to transactions based on their deadlines, importance, and resource requirements?
- How to resolve conflicts among transactions that access the same data items in read or write mode?
- How to handle transactions that miss their deadlines or abort due to concurrency control or other reasons?
- How to cope with data freshness and temporal consistency, which means that the data accessed by the transactions should reflect the current state of the real world?
- How to deal with distributed and decomposable transactions that span across multiple nodes or subtransactions ?

## Concurrency Control Protocols for Real-Time Database

There are various concurrency control protocols that have been proposed for real-time database, which can be classified into two main categories: lock-based protocols and timestamp-based protocols.

### Lock-Based Protocols

Lock-based protocols use locks to control the access to data items by transactions. A lock is a mechanism that grants exclusive or shared access to a data item to a transaction. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. A lock can be either exclusive or shared. An exclusive lock allows only one transaction to access the data item in write mode, while a shared lock allows multiple transactions to access the data item in read mode. A conflict occurs when two transactions try to acquire incompatible locks on the same data item, such as an exclusive lock and a shared lock, or two exclusive locks. A conflict resolution policy is used to decide which transaction should get the lock and which transaction should wait or abort.

Some of the lock-based protocols for real-time database are:

- Two-Phase Locking (2PL): This is a basic lock-based protocol that requires a transaction to acquire all the locks it needs before releasing any lock. This ensures serializability, but may cause deadlock, which is a situation where two or more transactions are waiting for each other to release locks. Deadlock can be prevented or detected and resolved by using timeouts, deadlock prevention algorithms, or deadlock detection algorithms.
- Priority Ceiling Protocol (PCP): This is a lock-based protocol that assigns a priority ceiling to each data item, which is the highest priority of any transaction that may lock the data item. A transaction can lock a data item only if its priority is higher than the priority ceiling of all the data items currently locked by other transactions. This prevents deadlock and ensures that higher priority transactions are not blocked by lower priority transactions. However, it may cause priority inversion, which is a situation where a higher priority transaction is blocked by a lower priority transaction that holds a lock on a data item needed by the higher priority transaction.
- Wait-Free Priority Ceiling Protocol (WFPCP): This is a lock-based protocol that extends PCP by allowing a transaction to abort and restart another transaction that holds a lock on a data item needed by the former transaction, if the latter transaction has a lower priority and a later deadline than the former transaction. This avoids priority inversion and ensures that transactions meet their