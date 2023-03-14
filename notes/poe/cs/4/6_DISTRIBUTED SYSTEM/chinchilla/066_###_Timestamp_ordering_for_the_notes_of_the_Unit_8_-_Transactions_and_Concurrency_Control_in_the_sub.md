### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Timestamp ordering is a concurrency control technique used in distributed systems to ensure serializability of transactions. It assigns a unique timestamp to each transaction at the time of its submission and ensures that transactions are executed in timestamp order.

Here are the key points to understand about timestamp ordering:

- Each transaction is assigned a unique timestamp at the time of its submission. The timestamp can be a logical or physical timestamp, depending on the system's implementation.
- Transactions are executed in timestamp order. A transaction with a smaller timestamp is executed before a transaction with a larger timestamp.
- If two transactions have the same timestamp, tie-breaking rules are used to determine the order of execution.
- If a transaction is found to violate serializability, it is rolled back and resubmitted with a new timestamp.
- Timestamp ordering is an optimistic concurrency control technique, meaning that it assumes that transactions will not conflict with each other. If conflicts do occur, the system will roll back transactions and retry them in a different order.
- Timestamp ordering is efficient and scalable, as it does not require locking or blocking of transactions.

Here are some mnemonics and learning tricks that can help you remember the key points of timestamp ordering:

- "Timestamps never lie." This phrase reminds us that timestamps are always unique and accurate, and that they are used to determine the order of transaction execution.
- "Smaller is better." This phrase reminds us that transactions with smaller timestamps are executed first, while transactions with larger timestamps are executed later.
- "Tie goes to the runner." This phrase reminds us that if two transactions have the same timestamp, tie-breaking rules are used to determine the order of execution.

Overall, timestamp ordering is a powerful technique for ensuring serializability of transactions in distributed systems. By assigning unique timestamps to transactions and ensuring that they are executed in timestamp order, timestamp ordering can help to prevent conflicts and ensure that transactions are executed efficiently and scalably.