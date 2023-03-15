 Here is the content in markdown format for the topic ### Consensus protocols for Permissioned Blockchains for the notes of the Unit 3 - Permissioned Blockchains in the subject of Block chain Architecture Design:

## Consensus protocols for Permissioned Blockchains

Some of the consensus protocols used in Permissioned Blockchains are:

- Practical Byzantine Fault Tolerance (PBFT):
- It is a replication algorithm that works on the state machine approach.
- It can tolerate Byzantine faults with high probability.
- It uses a distributed replicated state machine comprising of multiple nodes.
- It uses a 3-phase commit protocol - Pre-prepare, Prepare, and Commit phase to reach consensus.
- The leader node sends a pre-prepare message with the proposal in the first phase.
- In the second phase, the remaining nodes verify and send a prepare message.
- In the third phase, the commit message is broadcast if a quorum of nodes agreed in the second phase.
- The final committed value is added to the blockchain.
- PBFT has good performance but less scalability.

- Raft:
- It is a consensus algorithm that manages replication of a state machine.
- It elects a leader to whom followers replicate the state machine.
- The leader accepts client requests, replicates the state machine updates to followers.
- If the leader fails, a new leader is elected.
- It uses a replicated log and leader election mechanism to achieve consensus.
- Raft is easier to understand but has limitations in performance and fault tolerance.

- Proof of Authority (PoA):
- It is a reputation-based consensus mechanism.
- Pre-approved validators or authorities verify and add blocks to the blockchain.
- The identities of validators are known and validated using identity verification methods.
- Sybil attacks are prevented as the identities are verified.
- It is more efficient than PoW but gives more power to the validators.
- The consensus depends on the validators, so proper selection and rotation of validators are important.

[Detailed explanations, ascii diagrams, examples, applications, advantages, disadvantages, etc can be added here for the topics if required.]