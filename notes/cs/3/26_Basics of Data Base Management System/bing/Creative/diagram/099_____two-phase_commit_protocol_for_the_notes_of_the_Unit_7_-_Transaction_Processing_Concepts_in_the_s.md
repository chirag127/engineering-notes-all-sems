### Two-phase commit protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort (roll back) the transaction. It ensures that either all the changes are committed or none of them are, even in the case of site failures and message losses.

The protocol involves two phases:

- **Phase 1: Prepare phase**. The coordinator (Ci) of the transaction (T) sends a Prepare T message to all the sites where T executed. Each site responds with either a Yes vote, indicating that it is ready to commit T, or a No vote, indicating that it cannot commit T. The coordinator records the votes in a log and decides the outcome of the transaction based on the majority of votes.

- **Phase 2: Commit phase**. The coordinator sends the outcome of the transaction to all the sites that voted Yes in the prepare phase. If the outcome is commit, then each site commits T and sends an acknowledgement to the coordinator. If the outcome is abort, then each site aborts T and sends an acknowledgement to the coordinator. The coordinator waits for all the acknowledgements before ending the protocol.

The two-phase commit protocol is a blocking protocol; the failure of a single node blocks progress until the node recovers. Moreover, if the coordinator fails, then the database is left in an inconsistent state and only recovers once the coordinator recovers. This leads to another drawback as the protocol’s latency depends on the slowest node.

The following diagram illustrates the two-phase commit protocol:

```
    Coordinator (Ci)              Site 1 (S1)              Site 2 (S2)              Site 3 (S3)
    ---------------              ---------              ---------              ---------
    | Prepare T | ------------> | Prepare T |          | Prepare T |          | Prepare T |
    |           | <------------ | Yes       |          | Yes       |          | No        |
    | Commit T  | ------------> | Commit T  |          | Commit T  |          |           |
    |           | <------------ | Ack       |          | Ack       |          |           |
    | End       |                                                       
```