### Concurrency Control for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

Concurrency control is an important aspect of database management systems that deals with the simultaneous execution of multiple transactions. It is the process of managing access to shared resources to avoid conflicts and ensure consistency in data. In this unit, we will study the various techniques used for concurrency control in database systems.

#### Basic Concepts

Before diving into the techniques, it is essential to understand the following basic concepts:

- Transaction: A transaction is a sequence of operations that are executed as a single unit of work. Transactions ensure that the database remains in a consistent state at all times.

- Schedule: A schedule is a sequence of operations that are performed by various transactions. It determines the order in which transactions execute their operations.

- Serializability: A schedule is serializable if the final result of executing all transactions in the schedule is the same as the result of executing them in some serial order.

#### Concurrency Control Techniques

There are two approaches to concurrency control: pessimistic and optimistic.

##### Pessimistic Concurrency Control

Pessimistic concurrency control assumes that conflicts between transactions are highly probable, and therefore, it locks resources to prevent conflicts. The following techniques are used for pessimistic concurrency control:

- Lock-based Protocols: In this technique, locks are used to prevent multiple transactions from accessing the same resource simultaneously. There are two types of locks: shared and exclusive. Shared locks allow multiple transactions to read the same resource, while exclusive locks allow only one transaction to write to the resource.

- Two-Phase Locking (2PL): 2PL is a lock-based protocol that ensures serializability of transactions. It consists of two phases: the growing phase, where locks are acquired, and the shrinking phase, where locks are released.

- Strict Two-Phase Locking (Strict 2PL): Strict 2PL is an extension of 2PL that ensures that no unlock operation is performed until the transaction commits.

##### Optimistic Concurrency Control

Optimistic concurrency control assumes that conflicts between transactions are rare, and therefore, it allows transactions to proceed without locking resources. The following techniques are used for optimistic concurrency control:

- Timestamp-based Protocols: In this technique, each transaction is assigned a unique timestamp, and the transactions are executed in the order of their timestamps. If a transaction tries to access a resource that has been modified by a transaction with a higher timestamp, it is aborted.

- Validation-based Protocols: In this technique, each transaction is executed without any locks, and the database system validates the final result to ensure that it is serializable. If the result is not serializable, the transaction is aborted.

#### Advantages and Disadvantages

Each concurrency control technique has its advantages and disadvantages. The following are some of the advantages and disadvantages of concurrency control techniques:

##### Advantages

- Pessimistic concurrency control ensures that conflicts between transactions are prevented, and therefore, it provides a high degree of consistency.

- Optimistic concurrency control allows transactions to proceed without locking resources, and therefore, it provides a high degree of concurrency.

##### Disadvantages

- Pessimistic concurrency control can lead to deadlocks, where transactions are waiting for each other to release locks.

- Optimistic concurrency control can lead to transaction aborts, where transactions need to be restarted.

#### Conclusion

Concurrency control is a crucial aspect of database management systems that ensures that transactions are executed in a consistent manner. In this unit, we studied the various techniques used for concurrency control, including lock-based protocols, timestamp-based protocols, and validation-based protocols. Each technique has its advantages and disadvantages, and the choice of technique depends on the specific requirements of the application.