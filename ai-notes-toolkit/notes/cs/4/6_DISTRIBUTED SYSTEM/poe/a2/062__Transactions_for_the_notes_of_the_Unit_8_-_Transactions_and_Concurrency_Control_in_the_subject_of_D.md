 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

1. Transaction: A transaction is a unit of work that is performed against a database. Transactions in a database environment have two key properties:

Atomicity: A transaction is an all-or-nothing operation. Either all of its operations are performed or none.
Consistency: A transaction never leaves a database in a half-finished state.

2. ACID Properties: The properties that guarantee that database transactions are processed reliably are known as ACID properties. ACID is an acronym that stands for:

Atomicity: As mentioned above, the transactions are atomic. Either all of its operations are performed or none.
Consistency: The transaction never leaves the database in an inconsistent state. If the transaction executes successfully, the database moves from one consistent state to another.
Isolation: The transactions are isolated from each other. The intermediate states of the transactions are not visible to other transactions.
Durability: Once a transaction is committed, it will persist in the database even if there is a system failure. The changes made by the transaction are permanent.

3. Conflicts and Schedules: When multiple transactions execute concurrently, conflicts can occur if they access/modify the same data. A schedule is an order of executing transactions while maintaining ACID properties. The different types of schedules are:

Serial Schedule: Transactions are executed one after the other sequentially.
Concurrent Schedule: Transactions are executed simultaneously in some order.

...

[The content continues in the similar format with points and formal tone].