# Serializability of Schedules

Serializability is a concept in transaction processing that refers to the ability to execute multiple transactions concurrently while maintaining the consistency of the database. In other words, the result of executing multiple transactions concurrently should be the same as if they were executed one after the other in some order.

There are two types of serializability: conflict serializability and view serializability.

1. **Conflict Serializability**: A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations are said to be conflicting if they belong to different transactions, operate on the same data item, and at least one of them is a write operation.

2. **View Serializability**: A schedule is view serializable if it is view equivalent to a serial schedule. Two schedules are said to be view equivalent if the following conditions hold:
    - The same set of transactions participate in both schedules.
    - For any data item, the transaction that performs the first read in both schedules is the same.
    - For any data item, the transaction that performs the last write in both schedules is the same.
    - For any data item, the set of transactions that read the value written by a transaction is the same in both schedules.

Serializability is an important concept in transaction processing as it ensures the consistency of the database while allowing for concurrent execution of transactions. It is achieved through the use of concurrency control mechanisms such as locking and timestamping.