## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or communication delays.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- The main challenges of designing agreement protocols are:
  - Dealing with asynchrony: The processes and the network may have arbitrary delays, making it hard to synchronize or order events.
  - Dealing with failures: The processes may crash or behave maliciously (Byzantine failures), making it hard to trust or coordinate with them.
  - Dealing with uncertainty: The processes may have incomplete or inconsistent information, making it hard to agree on a common value or action.
- The main properties of agreement protocols are:
  - Validity: The value decided by the processes must be one of the values proposed by them.
  - Agreement: All correct processes must decide the same value.
  - Termination: All correct processes must eventually decide a value.
- Depending on the type and number of failures, the network model, and the assumptions made, different agreement protocols may have different trade-offs in terms of efficiency, complexity, and feasibility.
- Some examples of agreement protocols are:
  - Paxos: A family of protocols that achieve consensus in a partially synchronous network with crash failures, using a quorum-based approach and a leader-based optimization.
  - Raft: A protocol that achieves consensus in a partially synchronous network with crash failures, using a simpler and more understandable design than Paxos, based on leader election and log replication.
  - Byzantine Generals: A protocol that achieves consensus in a synchronous network with Byzantine failures, using a recursive majority voting scheme and digital signatures.
  - Practical Byzantine Fault Tolerance (PBFT): A protocol that achieves consensus in a partially synchronous network with Byzantine failures, using a view-based approach and a three-phase commit protocol.