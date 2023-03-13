A checkpoint is a point in time when the state of a distributed system is consistent and all transactions are committed. Obtaining consistent checkpoints is a technique for failure recovery in distributed systems, which allows the system to restore to a previous consistent state after a failure. A consistent checkpoint is a set of local checkpoints, one for each process, such that no process has a local checkpoint that reflects the effects of a message that was sent after the checkpoint but not received before the checkpoint by the destination process.

The following diagram illustrates the basic architecture of a distributed system with three processes (P1, P2, P3) and a coordinator (C) that performs consistent checkpointing using a coordinated algorithm. The algorithm works as follows:

- The coordinator initiates the checkpointing by sending a checkpoint request message to all processes.
- Each process, upon receiving the checkpoint request message, records its local state and sends an acknowledgement message to the coordinator.
- The coordinator waits until it receives an acknowledgement message from all processes, and then records its own state as the global checkpoint.
- The coordinator also maintains a log of all the messages that are sent and received during the checkpointing, which can be used for recovery.

The diagram shows an example of a consistent checkpoint that is taken at time t3, after P1 has sent a message m1 to P2, and P2 has sent a message m2 to P3. The checkpoint reflects the state of the system before m1 and m2 are delivered, and thus is consistent.

```
+----+     +----+     +----+     +----+
| P1 |     | P2 |     | P3 |     | C  |
+----+     +----+     +----+     +----+
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |
  |          |          |          |<-----------------+
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |<---------+          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  +----------+          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          +----------+          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          +----------+                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  +----------+----------+          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  +----------+----------+----------+                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  +----------+----------+----------+                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  +----------+----------+----------+                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |                  |
  |          |          |          |