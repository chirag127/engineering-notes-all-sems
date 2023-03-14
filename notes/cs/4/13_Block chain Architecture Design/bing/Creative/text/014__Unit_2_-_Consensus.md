## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common decision or action.
- Consensus is important for distributed systems, where multiple nodes need to coordinate their state and behavior in the presence of failures, network delays, and partial information.
- Consensus can be achieved by using algorithms that ensure the following properties:
  - **Termination**: Every correct node eventually decides on a value.
  - **Validity**: The decided value is one of the proposed values by the nodes.
  - **Agreement**: No two correct nodes decide on different values.
- Consensus is impossible to achieve in asynchronous systems, where there is no bound on the message delivery time or the relative speed of nodes, if even one node can fail by crashing. This is known as the **FLP impossibility result**.
- Consensus can be achieved in synchronous systems, where there is a known bound on the message delivery time and the relative speed of nodes, if a majority of nodes are correct. This is known as the **majority quorum** requirement.
- Consensus can also be achieved in partially synchronous systems, where the system behaves asynchronously for some unknown period of time and then becomes synchronous. This is known as the **eventual synchrony** assumption.
- Some examples of consensus algorithms are:
  - **Paxos**: A family of algorithms that use a leader-based approach to propose and accept values among a set of nodes, using majority quorums and multiple rounds of messages.
  - **Raft**: A simplified version of Paxos that uses a leader-based approach to propose and accept values among a set of nodes, using majority quorums and a single round of messages per value.
  - **Zab**: An algorithm that uses a leader-based approach to propose and accept values among a set of nodes, using majority quorums and a single round of messages per value, and also maintains a total order of values across leader changes.
  - **Viewstamped Replication**: An algorithm that uses a leader-based approach to propose and accept values among a set of nodes, using majority quorums and a single round of messages per value, and also maintains a view number that indicates the current leader.
  - **Multi-Paxos**: An optimization of Paxos that uses a single leader to propose and accept multiple values in a single round of messages, using majority quorums and a log of values.
  - **Chandra-Toueg Consensus**: An algorithm that uses a rotating coordinator to propose and accept values among a set of nodes, using majority quorums and multiple rounds of messages, and also handles the case of network partitions and node failures.
  - **Byzantine Fault Tolerant Consensus**: A family of algorithms that can tolerate arbitrary faults, such as malicious behavior or corrupted data, among a set of nodes, using supermajority quorums and multiple rounds of messages. Some examples are PBFT, HotStuff, and Tendermint.