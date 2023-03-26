### Transaction Recovery for the Notes of Unit 9 - Distributed Transactions in the Subject of Distributed System

In a distributed system, transaction recovery is critical to ensure data consistency and reliability. In this section, we will discuss the concept of transaction recovery and its various techniques.

#### What is Transaction Recovery?

Transaction recovery refers to the process of restoring the system to a consistent state after a failure has occurred during the execution of a transaction. It involves undoing the effects of the incomplete or failed transaction and redoing the effects of the successfully completed transaction.

#### Types of Failures

Before discussing the techniques for transaction recovery, it is essential to understand the different types of failures that can occur in a distributed system. The following are the most common types of failures:

1. System Failure: A system failure occurs when a hardware or software component of the system fails, such as a disk crash, power failure, or network failure.

2. Transaction Failure: A transaction failure occurs when a transaction cannot be completed due to some internal or external error, such as a deadlock, timeout, or communication failure.

3. Media Failure: A media failure occurs when data is lost or corrupted due to a physical problem with the storage media, such as a disk head crash or a magnetic field error.

#### Techniques for Transaction Recovery

There are two primary techniques for transaction recovery in a distributed system:

1. Undo-Redo Technique: The undo-redo technique involves undoing the effects of the incomplete or failed transaction and redoing the effects of the successfully completed transaction. This technique is used in most transaction processing systems and is based on the use of transaction logs.

2. Shadow-Paging Technique: The shadow-paging technique involves creating a shadow copy of the database before a transaction starts. The transaction is then executed on the shadow copy, and if it is successful, the changes are committed to the original database. If the transaction fails, the shadow copy is discarded, and the original database remains unchanged.

#### Conclusion

Transaction recovery is a critical aspect of distributed systems that ensures data consistency and reliability. The two primary techniques for transaction recovery are the undo-redo technique and the shadow-paging technique. Understanding these techniques is essential for ensuring the smooth and reliable operation of distributed systems.