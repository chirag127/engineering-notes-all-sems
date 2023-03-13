## Unit 4 - Agreement Protocols

Agreement protocols are used in distributed systems to ensure that a set of processes can reach a common decision or state, even in the presence of failures or communication delays. Agreement protocols are essential for achieving reliability and fault tolerance in distributed systems, such as distributed databases, distributed consensus, leader election, atomic broadcast, etc.

There are different types of agreement protocols, depending on the assumptions and requirements of the system, such as:

- **Consensus**: All processes must agree on a single value proposed by one or more processes.
- **Byzantine agreement**: All processes must agree on a single value proposed by one or more processes, even if some processes are faulty and may behave arbitrarily (Byzantine faults).
- **Atomic commit**: All processes must agree on whether to commit or abort a transaction that involves multiple processes.
- **View-synchronous communication**: All processes must agree on a common view of the system membership and deliver messages in the same order within each view.

The following diagram illustrates the basic architecture of a consensus protocol in a distributed system:

```
+--------+    +--------+    +--------+
|Process |    |Process |    |Process |
|   1    |    |   2    |    |   3    |
+--------+    +--------+    +--------+
    |             |             |
    | propose(v1) | propose(v2) |
    |-------------|-------------|----> Round 1
    |             |             |
    |<------------|-------------|----> Round 2
    |             |             |
    |-------------|------------>|----> Round 3
    |             |             |
    | decide(v)   | decide(v)   |----> Round 4
    |             |             |
    V             V             V
```

In this diagram, there are three processes that participate in the consensus protocol. Each process can propose a value (v1, v2, etc.) and must decide on a single value (v) that is equal to one of the proposed values. The protocol consists of four rounds of message exchange, where each process sends and receives messages from all other processes. The protocol ensures that all processes decide on the same value, even if some messages are lost or delayed. The protocol also ensures that the decided value is one of the proposed values, and that the protocol terminates in a finite number of rounds.