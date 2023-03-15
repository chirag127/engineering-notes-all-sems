### Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol involves two phases:

- **Phase 1: Prepare phase**. The coordinator (Ci) of the transaction (T) sends a Prepare T message to all the sites where T executed, and places a log record <Prepare T> on its site. Each site that receives the message decides whether to commit or abort T locally, and sends its vote to the coordinator. If the site votes to commit, it also writes a log record <Ready T> and waits for the coordinator's decision. If the site votes to abort, it writes a log record <Abort T> and undoes the changes of T.

- **Phase 2: Commit phase**. The coordinator collects the votes from all the sites. If all the sites voted to commit, the coordinator decides to commit T globally, and writes a log record <Commit T> on its site. It then sends a Commit T message to all the sites that voted to commit. Each site that receives the message writes a log record <Commit T> and makes the changes of T permanent. If any site voted to abort, or the coordinator did not receive a vote from some site, the coordinator decides to abort T globally, and writes a log record <Abort T> on its site. It then sends an Abort T message to all the sites that voted to commit. Each site that receives the message writes a log record <Abort T> and undoes the changes of T.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.