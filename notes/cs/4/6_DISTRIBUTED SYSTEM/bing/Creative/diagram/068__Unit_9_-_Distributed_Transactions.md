## Unit 9 - Distributed Transactions

A distributed transaction is a database transaction that involves two or more network hosts, usually providing transactional resources such as databases, message queues, or file systems. A distributed transaction is coordinated by a transaction manager, which is responsible for creating and managing a global transaction that encompasses all the operations against the transactional resources. A distributed transaction can be committed only if all the participants agree to commit, otherwise it is rolled back to ensure data consistency.

The following diagram illustrates the basic architecture of a distributed transaction using the two-phase commit protocol, which is a common method for achieving atomicity and durability across multiple hosts.

```
+-----------------+     +-----------------+     +-----------------+
| Transaction     |     | Transaction     |     | Transaction     |
| Manager         |     | Resource        |     | Resource        |
|                 |     | Manager 1       |     | Manager 2       |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     | +-------------+ |     | +-------------+ |
|                 |     | | Database 1  | |     | | Database 2  | |
|                 |     | +-------------+ |     | +-------------+ |
+-----------------+     +-----------------+     +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |<----------------------|---------------------->|
       |   Prepare request     |   Prepare request     |
       |                       |                       |
       |                       |                       |
       |---------------------->|---------------------->|
       |   Prepare response    |   Prepare response    |
       |                       |                       |
       |                       |                       |
       |<----------------------|---------------------->|
       |   Commit request      |   Commit request      |
       |                       |                       |
       |                       |                       |
       |---------------------->|---------------------->|
       |   Commit response     |   Commit response     |
       |                       |                       |
       |                       |                       |
```

The diagram shows the following steps:

1. The transaction manager initiates a distributed transaction that involves two transactional resources: database 1 and database 2, which are managed by their respective transaction resource managers.
2. The transaction manager sends a prepare request to both transaction resource managers, asking them to prepare their local transactions for commit.
3. The transaction resource managers execute their local transactions and lock the data that is affected by the transactions. They send a prepare response to the transaction manager, indicating whether they are ready to commit or not.
4. The transaction manager collects the prepare responses from both transaction resource managers. If both responses are positive, the transaction manager decides to commit the global transaction. If either response is negative, the transaction manager decides to abort the global transaction.
5. The transaction manager sends a commit request to both transaction resource managers, asking them to commit or abort their local transactions according to the global decision.
6. The transaction resource managers commit or abort their local transactions and release the locks on the data. They send a commit response to the transaction manager, indicating whether they have completed the commit or abort operation.
7. The transaction manager collects the commit responses from both transaction resource managers and completes the distributed transaction.