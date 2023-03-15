 Here is the content written in markdown format for the topic ## Unit 9 - Distributed Transactions:

## Unit 9 - Distributed Transactions

Distributed transactions involve multiple databases or servers and ensure that all parts of a transaction are completed successfully or none at all (atomicity). Some key points about distributed transactions:

- They maintain ACID properties (atomicity, consistency, isolation, durability) across multiple databases or servers.
- They require coordination between multiple data sources to commit or roll back transactions. This coordination is often handled through a two-phase commit protocol.
- They are more complex to implement than local transactions and can impact performance due to the additional coordination required.
- They are commonly used in enterprise applications that access multiple data sources.

Two-phase commit protocol:

1. Prepare phase: The transaction coordinator asks all data sources to prepare to commit the transaction. Each data source ensures it can commit the transaction and responds with a "ready to commit" message.
2. Commit phase: If all data sources respond that they are ready to commit, the coordinator sends a commit message to all data sources. The transaction is committed in all data sources. Otherwise, if any data source cannot prepare to commit, a rollback message is sent to all data sources to roll back the transaction.

Advantages: Maintain ACID properties across multiple data sources.
Disadvantages: Additional overhead can impact performance. More complex to implement.

Examples: Transferring money across multiple bank accounts (databases). Order processing that updates inventory databases.

[Include additional details, diagrams, codes, etc. here if helpful for learning the topic.]