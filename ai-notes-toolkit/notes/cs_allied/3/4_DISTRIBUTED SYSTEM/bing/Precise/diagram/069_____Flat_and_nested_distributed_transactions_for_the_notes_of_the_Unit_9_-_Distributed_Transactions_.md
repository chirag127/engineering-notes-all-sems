### Unit 9 - Distributed Transactions: Flat and Nested Distributed Transactions

#### Flat Distributed Transactions
- A flat distributed transaction is a transaction that involves multiple networked computer systems, where all the systems must agree on the outcome of the transaction.
- The two-phase commit protocol is commonly used to coordinate flat distributed transactions.
- In the first phase, the coordinator sends a prepare message to all participants, asking them to prepare to commit or abort the transaction.
- In the second phase, the coordinator makes a decision to commit or abort the transaction based on the responses from the participants and sends a commit or abort message to all participants.

#### Nested Distributed Transactions
- A nested distributed transaction is a transaction that contains other transactions, called subtransactions, which can be distributed across multiple networked computer systems.
- Nested distributed transactions provide more flexibility than flat distributed transactions, as subtransactions can be committed or aborted independently.
- The coordinator of a nested distributed transaction is responsible for coordinating the commit or abort of the subtransactions.
- The two-phase commit protocol can also be used to coordinate nested distributed transactions, with the coordinator sending prepare and commit or abort messages to the coordinators of the subtransactions.