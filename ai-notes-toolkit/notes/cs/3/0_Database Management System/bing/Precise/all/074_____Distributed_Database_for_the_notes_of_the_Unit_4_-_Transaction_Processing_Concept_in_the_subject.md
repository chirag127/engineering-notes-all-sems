# Distributed Database

A distributed database is a collection of databases that are linked by a network and communicate with each other. Distributed databases incorporate transaction processing, which is a program including a collection of one or more database operations.

## Transaction Processing Concept

A distributed transaction includes one or more statements that, individually or as a group, update data on two or more distinct nodes of a distributed database. In a distributed database environment, the database must coordinate the committing or rolling back of the changes in a distributed transaction as a self-contained unit.

### Two-Phase Commit Mechanism

The two-phase commit mechanism is used to coordinate the committing or rolling back of the changes in a distributed transaction.

### In-Doubt Transactions

A transaction becomes in-doubt if the two-phase commit mechanism fails.

## Distributed Transaction Processing: Case Study

A distributed transaction is a set of operations that we want to perform on our data, but it is committed to more than one piece of hardware. So, rather than writing the changes associated with our transaction to the hard drive of a single-instance database, we’re writing those changes to several different database nodes.