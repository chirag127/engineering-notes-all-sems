 Here is the formal content in Markdown format without any emojis or external links:

## Unit 4 - Agreement Protocols

1. Consensus Protocols - Protocols that are used to achieve consensus between nodes in a distributed network. Some examples are:
- Proof of Work - Nodes prove that they have solved a complex computational problem to achieve consensus. Used in Bitcoin.
- Proof of Stake - Nodes prove that they have stake (own coins) in the system to achieve consensus. The node with the most stake is chosen to validate transactions.
- Practical Byzantine Fault Tolerance - A protocol that tolerates Byzantine faults and reaches consensus without proofs.Used in systems like Hyperledger.

2. Atomic Commit Protocols - Protocols that are used to ensure that a set of transactions either all commit or all abort. This ensures data consistency in distributed databases. Some examples are:
- Two-phase commit - A classic protocol that consists of voting and commit phases to ensure atomicity.
- Three-phase commit - An extension of two-phase commit that adds a pre-commit phase to reduce blocking.
- Commitment ordering-based protocols - Protocols that order transactions based on precedence to determine commit order and ensure atomicity.

3. Concurrent Protocols - Protocols that are designed to handle concurrent executions and conflicts in a distributed system. Some examples are:
- Timestamp ordering - Transactions are ordered based on timestamps to handle conflicts.
- Multi-version concurrency control - Existing data versions are used until transactions commit to handle conflicts.
- Optimistic concurrency control - Transactions proceed without locking and conflicts are resolved at commit time.

Does this look okay? Let me know if you would like me to modify or add any other content.