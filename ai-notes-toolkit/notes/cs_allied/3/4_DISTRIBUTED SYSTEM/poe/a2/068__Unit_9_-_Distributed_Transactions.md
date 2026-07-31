 Here is the content in formal tone without emojis or external links, written in markdown format with points inside the given header:

## Unit 9 - Distributed Transactions

1. A distributed transaction is a transaction that updates data on two or more networked computers.
2. Atomicity: Either all operations of a distributed transaction are completed successfully or none are, even in the face of system failures.
3. Consistency: The transaction moves data from one valid state to another. The state after the transaction must adhere to all defined rules, constraints, cascades, and triggers.
4. Isolation: Intermediate states of the transaction are not visible to other transactions.
5. Durability: The results of a committed transaction persist even in the face of system failures.
6. Challenges in distributed transactions:

- Network failures: The network could fail at any time, jeopardizing the atomicity of the transaction.
- Temporary failures: A server could fail temporarily, and the transaction manager must ensure the transaction is either fully completed or rolled back once the server is operational again.
- Permanent failures: If a server fails permanently, the portion of the transaction executing on that server must be rolled back.
- Long duration transactions: The longer a transaction runs, the higher the chances of a failure occurring.

7. Solutions to distributed transaction challenges:

- Two phase commit (2PC): A standardized protocol for committing all the individual transactions of a distributed transaction.
- Three phase commit (3PC): An extension of 2PC that provides better performance for distributed transactions that take a long time.
- Commitment ordering: Transactions are committed in a specific order to avoid deadlocks and ensure consistency.
- Compensation-based transactions: Alternative approach where committed transactions that cannot be rolled back are compensated by new transactions.