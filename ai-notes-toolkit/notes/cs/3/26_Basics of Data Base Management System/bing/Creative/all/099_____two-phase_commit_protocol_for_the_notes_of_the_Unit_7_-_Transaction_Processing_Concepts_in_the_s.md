# Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol involves two phases:

- **Phase 1: Prepare phase**. In this phase, the coordinator (the process that initiates the transaction) sends a prepare message to all the participants (the processes that execute the transaction) and waits for their replies. Each participant executes the transaction up to the point where it is ready to commit, writes a prepare record to its log, and sends a prepared message to the coordinator. If any participant encounters an error or decides to abort, it sends an abort message to the coordinator and undoes the transaction.
- **Phase 2: Commit phase**. In this phase, the coordinator decides the outcome of the transaction based on the replies from the participants. If all the participants replied with prepared messages, the coordinator commits the transaction and sends a commit message to all the participants. If any participant replied with an abort message, the coordinator aborts the transaction and sends an abort message to all the participants. Each participant then follows the coordinator's decision and either commits or aborts the transaction, and writes a commit or abort record to its log.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.

The two-phase commit protocol is used for distributed transaction management in databases, computer networking, and transaction processing systems . It ensures the ACID (atomicity, consistency, isolation, and durability) properties of transactions in a distributed system.