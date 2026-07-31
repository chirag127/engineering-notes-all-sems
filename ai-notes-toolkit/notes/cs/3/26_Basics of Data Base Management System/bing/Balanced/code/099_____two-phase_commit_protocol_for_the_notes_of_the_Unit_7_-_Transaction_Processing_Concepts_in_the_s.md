### Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol consists of two phases:

- **Phase 1: Prepare phase**. The coordinator (Ci) of the transaction (T) sends a Prepare T message to all the sites where T executed and waits for their replies. Each site that receives the message writes a <Prepare T> record on its log and forces it to disk. Then, it replies with either Yes or No, depending on whether it is ready to commit or not. If the site replies Yes, it locks all the data items updated by T and waits for the final decision from the coordinator. If the site replies No, it aborts T and releases all the locks.

- **Phase 2: Commit/Abort phase**. The coordinator collects the replies from all the sites and decides the outcome of the transaction. If all the sites replied Yes, the coordinator decides to commit T and writes a <Commit T> record on its log. Then, it sends a Commit T message to all the sites. If any site replied No, the coordinator decides to abort T and writes an <Abort T> record on its log. Then, it sends an Abort T message to all the sites. Each site that receives the message executes the decision and writes a <Commit T> or <Abort T> record on its log. Then, it sends an Acknowledgment message to the coordinator and releases all the locks.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.

: https://www.educative.io/answers/what-is-the-two-phase-commit-protocol
: https://en.wikipedia.org/wiki/Two-phase_commit_protocol
: https://courses.cs.vt.edu/~cs5204/fall00/distributedDBMS/duckett/tpcp.html
: https://www.geeksforgeeks.org/two-phase-commit-protocol-distributed-transaction-management/