### Recovery with Concurrent Transactions

Concurrency control is an important aspect of database management systems that allows multiple transactions to access the same data simultaneously without causing any conflicts. However, sometimes transactions can fail due to various reasons such as system crashes, power outages, or software errors. In such cases, recovery mechanisms are used to restore the database to a consistent state. Recovery with concurrent transactions is an approach that enables transactions to continue executing even during the recovery process. In this section, we will discuss the various techniques used for recovery with concurrent transactions.

#### Shadow Paging

Shadow paging is a recovery technique that uses a shadow or temporary copy of the database to perform recovery operations. In this technique, a shadow page table is maintained that keeps track of the changes made by each transaction. When a transaction executes, it updates the shadow page table instead of the actual page table. Once the transaction is committed, the changes are propagated to the actual page table. If a transaction fails, the shadow page table can be used to roll back the changes made by the transaction. This technique is simple and efficient, but requires a lot of disk space to store the shadow copy of the database.

#### Deferred Update

Deferred update is another recovery technique that postpones the updates made by a transaction until the transaction is committed. In this technique, a log file is maintained that records all the changes made by each transaction. When a transaction executes, it only updates the log file and not the actual database. Once the transaction is committed, the changes are propagated to the actual database. If a transaction fails, the changes made by the transaction are simply discarded. This technique is efficient and requires less disk space than shadow paging, but it can cause data inconsistencies if transactions are not properly ordered.

#### Immediate Update

Immediate update is a recovery technique that updates the actual database as soon as a transaction makes a change. In this technique, a log file is maintained that records all the changes made by each transaction. When a transaction executes, it updates the actual database and the log file simultaneously. Once the transaction is committed, the log file is discarded. If a transaction fails, the log file can be used to roll back the changes made by the transaction. This technique is efficient and requires less disk space than shadow paging, but it can cause data inconsistencies if transactions are not properly ordered.

Recovery with concurrent transactions is a complex topic, but it is essential for ensuring the reliability and consistency of database systems. By using the techniques discussed in this section, it is possible to recover from transaction failures while still allowing multiple transactions to access the database concurrently.