The following diagram illustrates the basic architecture of a **two-phase commit protocol (2PC)**, a type of atomic commit protocol for distributed transactions   . The diagram is drawn using ASCII characters.

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|    Coordinator  |        |    Worker 1     |        |    Worker 2     |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |<------------------------|------------------------>|
       |                         |                         |
       |     Prepare Phase       |                         |
       |                         |                         |
       |------------------------>|------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |<------------------------|------------------------>|
       |                         |                         |
       |     Commit Phase        |                         |
       |                         |                         |
       |------------------------>|------------------------>|
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
```

The 2PC protocol consists of two phases: the prepare phase and the commit phase. In the prepare phase, the coordinator sends a prepare message to all the workers involved in the transaction, asking them to vote on whether they are ready to commit or not. The workers execute the transaction locally and lock the resources they need. Then they send back their votes to the coordinator. If all the workers vote yes, the coordinator moves to the commit phase. In the commit phase, the coordinator sends a commit message to all the workers, telling them to commit the transaction and release the locks. The workers acknowledge the commit message and send back an acknowledgement to the coordinator. The coordinator waits for all the acknowledgements and then declares the transaction committed. If any of the workers vote no or fail to respond in the prepare phase, the coordinator aborts the transaction and sends an abort message to all the workers, telling them to roll back the transaction and release the locks. The workers acknowledge the abort message and send back an acknowledgement to the coordinator. The coordinator waits for all the acknowledgements and then declares the transaction aborted. The 2PC protocol ensures that either all the workers commit the transaction or none of them do, thus achieving atomicity. However, the protocol also has some drawbacks, such as blocking, vulnerability to failures, and performance overhead.