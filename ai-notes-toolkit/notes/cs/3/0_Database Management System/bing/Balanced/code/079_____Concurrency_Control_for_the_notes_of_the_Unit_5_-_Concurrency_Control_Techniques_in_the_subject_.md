Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of concurrency control for the notes of the unit 5 - concurrency control techniques in the subject of database management system.

### Concurrency Control

- Concurrency control is the process of managing simultaneous operations on a database without compromising its integrity or consistency.
- Concurrency control is necessary to ensure that concurrent transactions do not interfere with each other and violate the ACID properties of the database.
- ACID stands for atomicity, consistency, isolation, and durability. These are the desirable characteristics of a database transaction.
- Atomicity means that a transaction is either executed completely or not at all. Consistency means that a transaction preserves the integrity constraints of the database. Isolation means that a transaction is executed as if it were the only one in the system. Durability means that the effects of a committed transaction are permanent and survive any system failures.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by a transaction. Locking can be done at different levels of granularity, such as record, page, file, or table. Locking can also be done in different modes, such as shared, exclusive, or update. Locking protocols ensure that the locking is done in a consistent and deadlock-free manner.
- Optimistic concurrency control techniques allow conflicts to occur but detect and resolve them before committing the transactions. Optimistic techniques do not use locking, but instead use timestamps or validation rules to determine the order and validity of the transactions. Optimistic techniques are suitable for applications where conflicts are rare and locking is expensive or impractical.