
## Unit 8 - Transactions and Concurrency Control

* Transactions are a sequence of operations that are executed as a single unit, meaning that either all of the operations are executed or none of them are.
* Concurrency control ensures that multiple transactions are executed in a manner that preserves the consistency of the database.
* In order to ensure that concurrency control is maintained, there are several techniques that can be used, such as locking, timestamp ordering, and optimistic concurrency control.
* Locking is a technique that is used to ensure that only one transaction can access a particular resource at a given time.
* Timestamp ordering is a technique that is used to ensure that transactions are executed in the order in which they are received.
* Optimistic concurrency control is a technique that is used to ensure that transactions are executed in the order in which they are received, but also allows transactions to execute concurrently if they do not conflict with each other.
* Mnemonic: CCLT - Concurrency Control with Locking and Timestamping
* Mnemonic: OCC - Optimistic Concurrency Control