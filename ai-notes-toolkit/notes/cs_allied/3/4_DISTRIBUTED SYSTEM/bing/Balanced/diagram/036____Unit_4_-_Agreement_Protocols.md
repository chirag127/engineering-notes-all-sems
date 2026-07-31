## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus, despite the possibility of failures or malicious behavior.
- Agreement protocols are useful for implementing fault-tolerant services, such as distributed databases, replicated state machines, leader election, atomic broadcast, etc.
- Agreement protocols can be classified into different types, depending on the assumptions and guarantees they provide, such as:
  - Crash fault tolerance: The protocol can tolerate processes that fail by halting (crashing), but not by deviating from the protocol specification (Byzantine).
  - Byzantine fault tolerance: The protocol can tolerate processes that fail by behaving arbitrarily (Byzantine), including sending conflicting or malicious messages to other processes.
  - Synchronous: The protocol assumes that there are known bounds on the message delay and the process speed, and can use timeouts to detect failures.
  - Asynchronous: The protocol does not assume any bounds on the message delay and the process speed, and cannot use timeouts to detect failures.
  - Partially synchronous: The protocol assumes that the system is asynchronous most of the time, but eventually becomes synchronous, and can use adaptive timeouts to detect failures.
  - Deterministic: The protocol guarantees that all correct processes will reach the same decision, regardless of the inputs or the message order.
  - Randomized: The protocol guarantees that all correct processes will reach the same decision with high probability, depending on the inputs and the message order.
- Some examples of agreement protocols are:
  - Paxos: A deterministic, partially synchronous, crash fault tolerant protocol that allows a set of processes to agree on a single value, such as the identity of a leader or the state of a replicated service.
  - Raft: A deterministic, partially synchronous, crash fault tolerant protocol that simplifies the design of Paxos by separating the agreement into two phases: leader election and log replication.
  - Byzantine Generals: A deterministic, synchronous, Byzantine fault tolerant protocol that allows a set of generals (processes) to agree on a common plan of action, such as attacking or retreating, despite the presence of traitors (Byzantine processes).
  - Practical Byzantine Fault Tolerance (PBFT): A deterministic, partially synchronous, Byzantine fault tolerant protocol that extends the Byzantine Generals protocol to handle multiple requests and optimize the message complexity.
  - Bitcoin: A randomized, asynchronous, Byzantine fault tolerant protocol that allows a set of nodes to agree on a distributed ledger of transactions, using a proof-of-work mechanism to prevent double-spending and Sybil attacks.