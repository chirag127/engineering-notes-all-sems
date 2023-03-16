### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Agreement protocols are a class of algorithms that allow a set of distributed processes to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the correctness and consistency of distributed systems, especially in the context of fault tolerance, replication, distributed transactions, distributed consensus, and distributed commit.
- Agreement protocols can be classified into different types based on the following criteria:
  - The type of failures that the protocol can tolerate, such as crash failures, omission failures, timing failures, or Byzantine failures.
  - The type of communication model that the protocol assumes, such as synchronous, asynchronous, or partially synchronous.
  - The type of agreement that the protocol guarantees, such as uniform agreement, non-uniform agreement, or interactive consistency.
  - The type of value that the protocol agrees on, such as binary, multivalued, or vector.
- Some of the most well-known agreement protocols are:
  - Paxos, which is a family of protocols that achieve consensus in a network of unreliable processes.
  - Raft, which is a protocol that simplifies the design and implementation of Paxos by dividing the consensus problem into three subproblems: leader election, log replication, and safety.
  - Two-phase commit (2PC), which is a protocol that allows a coordinator to atomically commit or abort a distributed transaction involving multiple participants.
  - Three-phase commit (3PC), which is a protocol that improves the availability of 2PC by introducing a third phase to avoid blocking in case of failures.
  - Byzantine agreement (BA), which is a protocol that allows a set of processes to agree on a value even if some of them are faulty or malicious.
  - Byzantine fault tolerance (BFT), which is a general technique that enables a system to tolerate Byzantine failures by using replication, cryptography, and voting.