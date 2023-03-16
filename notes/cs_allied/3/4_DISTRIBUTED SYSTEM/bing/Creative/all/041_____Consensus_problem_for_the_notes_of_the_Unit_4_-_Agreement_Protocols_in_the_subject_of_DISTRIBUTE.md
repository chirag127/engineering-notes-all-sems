# Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common types of failures that can affect consensus are:
  - Crash failures: A process stops executing and does not resume.
  - Byzantine failures: A process behaves arbitrarily, deviating from the protocol.
  - Network failures: Messages are lost, delayed, duplicated, or reordered.
- Some of the common consensus algorithms are:
  - Two-phase commit: A coordinator process initiates a transaction and asks other processes to vote on whether to commit or abort.
  - Three-phase commit: An extension of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of algorithms that use a quorum of processes to propose and accept values.
  - Raft: A simplified version of Paxos that uses a leader election and a replicated log to achieve consensus.
  - Byzantine fault tolerance: A class of algorithms that can tolerate arbitrary failures of up to a third of the processes.