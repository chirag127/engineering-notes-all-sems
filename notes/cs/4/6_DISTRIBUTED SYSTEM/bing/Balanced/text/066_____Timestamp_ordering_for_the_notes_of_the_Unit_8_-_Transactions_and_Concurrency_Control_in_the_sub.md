### Timestamp ordering

- Timestamp ordering is a technique for ensuring serializability of transactions in a distributed system.
- A transaction is a sequence of operations that must be executed atomically, i.e., either all or none of them are performed.
- Serializability means that the concurrent execution of transactions produces the same result as some sequential execution of them.
- Timestamp ordering assigns a unique timestamp to each transaction when it starts, and uses these timestamps to order the operations of different transactions.
- A timestamp can be either a logical clock value or a physical clock value, depending on the implementation.
- The basic idea of timestamp ordering is that a transaction can only read or write an object if its timestamp is greater than the timestamp of the last transaction that accessed the object.
- If a transaction tries to access an object with a lower timestamp, it is aborted and restarted with a new timestamp.
- This ensures that the transactions are executed in a consistent order, and that no transaction can overwrite the changes of a later transaction.
- Timestamp ordering can be implemented in a centralized or decentralized manner, depending on the architecture of the distributed system.
- In a centralized system, there is a single timestamp server that assigns timestamps to transactions and maintains the last access timestamps of all objects.
- In a decentralized system, each node has its own local timestamp generator and maintains the last access timestamps of the objects it owns.
- The nodes communicate with each other to synchronize their timestamps and resolve conflicts.