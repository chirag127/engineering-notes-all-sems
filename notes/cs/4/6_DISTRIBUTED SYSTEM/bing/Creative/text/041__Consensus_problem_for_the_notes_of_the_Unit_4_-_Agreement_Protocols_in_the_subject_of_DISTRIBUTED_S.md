### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is important for distributed systems, where nodes are distributed across the network and may fail or behave abnormally.
- Consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus algorithms are the protocols that enable the nodes to reach consensus in a distributed system.
- Consensus algorithms have to be fault-tolerant or resilient, meaning they can tolerate some nodes failing or behaving maliciously.
- Consensus algorithms have to exhibit certain properties, such as termination, agreement and integrity.
  - Termination: every non-faulty node must decide on a value.
  - Agreement: every correct node must agree on the same value.
  - Integrity: if all the correct nodes proposed the same value, then any correct node must decide the same value.
- Consensus algorithms can be classified into different categories based on the type of faults they can tolerate, the communication model they use, the performance and security trade-offs they make, and the application domain they target.
- Some examples of consensus algorithms are:
  - Two-phase commit: a simple protocol that uses a coordinator node to propose a value and get votes from the other nodes, and then commits or aborts the value based on the majority of votes.
  - Paxos: a family of protocols that use a leader node to propose a value and get acceptances from the other nodes, and then learn the value from a quorum of nodes.
  - Raft: a protocol that uses a leader node to replicate a log of commands across the other nodes, and then executes the commands in the same order on all nodes.
  - Byzantine fault tolerance: a class of protocols that can tolerate arbitrary faults, including malicious behavior, by using cryptographic techniques and requiring more than two-thirds of the nodes to be honest.
  - Proof-of-work: a protocol that uses a probabilistic mechanism to elect a leader node that proposes a value, and then requires the other nodes to validate the value by solving a hard mathematical puzzle.
  - Proof-of-stake: a protocol that uses a deterministic mechanism to elect a leader node that proposes a value, and then requires the other nodes to validate the value by staking some amount of resources.