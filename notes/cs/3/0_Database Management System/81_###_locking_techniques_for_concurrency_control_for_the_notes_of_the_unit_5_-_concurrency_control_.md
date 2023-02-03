### Locking Techniques for Concurrency Control for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

Locking techniques are used in database management systems to control concurrent access to data and ensure the consistency and integrity of data in a database. Locking is a mechanism that is used to prevent concurrent transactions from accessing the same data at the same time, and it is an important aspect of concurrency control.

There are several types of locking techniques that are used in database management systems, including:

1. Exclusive Locking: Exclusive locks are used to prevent other transactions from accessing the data that is being modified by a transaction. Exclusive locks are used to ensure that a transaction has exclusive access to the data that it is modifying.

2. Shared Locking: Shared locks are used to allow multiple transactions to access the same data simultaneously, but to prevent them from modifying the data. Shared locks are used to ensure that multiple transactions can read the same data at the same time, but that only one transaction can modify the data at a time.

3. Optimistic Locking: Optimistic locking is a concurrency control technique that is used to ensure that multiple transactions can access the same data simultaneously, but that only one transaction can modify the data at a time. Optimistic locking is based on the assumption that conflicts between transactions are rare, and that the majority of transactions will complete without any conflicts.

In this unit, you will learn about locking techniques for concurrency control in database management systems, including the various types of locks and their usage, and the benefits and drawbacks of each type of lock. You will also learn about the mechanisms used to implement locking, including lock tables and lock managers. This will provide a foundation for understanding the principles and practices of concurrency control, and for exploring the various concepts and techniques used in database management systems.
