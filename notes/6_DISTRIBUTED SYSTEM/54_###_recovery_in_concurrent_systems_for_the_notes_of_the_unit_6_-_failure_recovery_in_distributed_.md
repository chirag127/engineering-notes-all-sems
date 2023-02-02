### Recovery in Concurrent systems for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM
Recovery in concurrent systems refers to the process of restoring the system to a consistent state after a failure. This is important in distributed systems, where multiple nodes are involved and a failure in one node can affect the entire system.

- Types of failures:
  1. Node failure: when a node crashes or becomes unavailable
  2. Link failure: when a communication link between nodes is lost
  3. Process failure: when a process crashes or terminates abnormally

- Recovery strategies:
  1. Rollback recovery: rolling back the system to a previous state
  2. Checkpoint and restart: saving the state of the system and restarting from that state
  3. Replication: maintaining multiple copies of data to ensure that the system can continue to function even if one node fails

- Failure detection:
  1. Heartbeats: regularly sending messages between nodes to detect failures
  2. Timeouts: detecting failures by checking if a node has not responded within a certain time frame

- Consistency:
  1. Two-phase commit protocol: ensuring that all nodes agree on the outcome of a transaction before committing it
  2. Distributed transactions: coordinating transactions that involve multiple nodes

- Recovery algorithms:
  1. Chandy-Lamport algorithm: a distributed algorithm for detecting and recovering from failures in a distributed system
  2. Byzantine fault tolerance: a technique for tolerating failures in a distributed system, even if some nodes are faulty or malicious.
