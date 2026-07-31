### Distributed Database

A distributed database is a collection of multiple interconnected databases, which are spread physically across various locations that communicate via a computer network. 

#### Transaction Processing Concept

- A distributed transaction includes one or more statements that, individually or as a group, update data on two or more distinct nodes of a distributed database.
- All databases in a collection are linked by a network and communicate with each other.
- Distributed databases incorporate transaction processing, which is a program including a collection of one or more database operations.
- A distributed transaction is a set of operations that we want to perform on our data, but it is committed to more than one piece of hardware.
- A distributed transaction is a database transaction in which two or more network hosts are involved.
- Usually, hosts provide transactional resources, while the transaction manager is responsible for creating and managing a global transaction that encompasses all operations against such resources.
- In a distributed database environment, the database must coordinate the committing or rolling back of the changes in a distributed transaction as a self-contained unit.
- A transaction becomes in-doubt if the two-phase commit mechanism fails.