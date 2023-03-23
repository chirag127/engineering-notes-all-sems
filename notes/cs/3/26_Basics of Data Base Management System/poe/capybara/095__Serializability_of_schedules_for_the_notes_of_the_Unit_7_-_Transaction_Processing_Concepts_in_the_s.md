### Serializability of schedules for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

In the world of databases, transactions are a crucial concept, and they are used to ensure the consistency and reliability of the data. In this context, a schedule is a sequence of actions that are performed by transactions, and it is essential to ensure that schedules are serializable. In this section, we will explore what serializability is and how it can be achieved.

#### What is serializability?

Serializability is a property of schedules that ensures that the outcome of executing a set of transactions is equivalent to the outcome of executing the same transactions in some serial order. In other words, a serializable schedule is one that produces the same result as some serial order of executing transactions.

#### Achieving serializability

There are two ways to achieve serializability: conflict serializability and view serializability.

##### Conflict serializability

Conflict serializability is achieved by ensuring that transactions do not conflict with each other. A conflict between two transactions arises when they access the same data item, and at least one of them modifies that item. To ensure conflict serializability, we can use a technique called locking.

Locking involves acquiring a lock on a data item before accessing it. If a transaction attempts to access a data item that is already locked by another transaction, it must wait until the lock is released. By using locking, we can ensure that transactions do not conflict with each other and that schedules are serializable.

##### View serializability

View serializability is achieved by ensuring that transactions do not violate the consistency constraints of the database. These constraints are defined by the database schema and the integrity constraints. To ensure view serializability, we can use a technique called validation.

Validation involves checking whether a schedule preserves the consistency constraints of the database. If a schedule violates these constraints, it is considered to be non-serializable. By using validation, we can ensure that schedules are serializable and that the consistency of the data is maintained.

#### Conclusion

In conclusion, serializability is a crucial property of schedules in databases, and it ensures that the outcome of executing a set of transactions is equivalent to the outcome of executing the same transactions in some serial order. Conflict serializability and view serializability are two techniques that can be used to achieve serializability, and they involve locking and validation, respectively. By ensuring that schedules are serializable, we can ensure the consistency and reliability of the data in the database.