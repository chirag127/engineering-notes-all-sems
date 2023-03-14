An atomic commit protocol is a protocol that guarantees the atomicity property of a transaction in a distributed database system. Atomicity means that either all the changes made by a transaction are committed at all the participating sites, or none of them are. An atomic commit protocol ensures that a transaction has a deterministic final outcome, even in the presence of failures.

There are different types of atomic commit protocols, such as two-phase commit (2PC), three-phase commit (3PC), and non-blocking commit protocols. The basic idea of these protocols is to use a coordinator site that initiates the commit process and collects the votes from the other sites (called workers or participants). The coordinator then decides whether to commit or abort the transaction based on the votes, and informs the workers about the decision.

The following diagram illustrates the basic architecture of a distributed database system with a coordinator and three workers, and the message flow of a 2PC protocol:

```
    +-----------+      +-----------+      +-----------+      +-----------+
    |           |      |           |      |           |      |           |
    | Coordinator|     |  Worker 1 |     |  Worker 2 |     |  Worker 3 |
    |           |      |           |      |           |      |           |
    +-----------+      +-----------+      +-----------+      +-----------+
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |<-----------------|<-----------------|<-----------------|
         |   Prepare to     |   Prepare to     |   Prepare to     |
         |    commit?       |    commit?       |    commit?       |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |----------------->|----------------->|----------------->|
         |   Yes/No         |   Yes/No         |   Yes/No         |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |<-----------------|<-----------------|<-----------------|
         |   Commit/Abort   |   Commit/Abort   |   Commit/Abort   |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         |                  |                  |                  |
         V                  V                  V                  V
```