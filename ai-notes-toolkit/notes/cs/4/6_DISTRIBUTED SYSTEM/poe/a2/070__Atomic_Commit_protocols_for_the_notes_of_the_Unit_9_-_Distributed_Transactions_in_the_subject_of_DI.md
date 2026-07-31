 Here is the content in Markdown format without any emojis or external links:

### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

1. Atomic Commit Protocol: It is a protocol which ensures that all the distributed transactions are committed successfully or none of them. It guarantees the atomicity of the distributed transactions. The two phase commit protocol is an example of atomic commit protocol.

2. Two Phase Commit Protocol: It is a distributed algorithm which ensures that all the distributed transactions are committed successfully across all the nodes or none of them. It proceeds in two phases:

- Phase 1: In this phase, the coordinator asks all the participants whether they are ready to commit the transaction or not. If all the participants vote to commit, then the coordinator moves to phase 2.
- Phase 2: In this phase, the coordinator asks all the participants to commit the transaction. If all the participants commit successfully, then the coordinator commits the transaction. Otherwise, it aborts the transaction.

The two phase commit protocol ensures the atomicity of the distributed transactions. However, it suffers from some disadvantages like blocking and single point of failure.

3. Three Phase Commit Protocol: It is an extension of two phase commit protocol which eliminates the blocking disadvantage of two phase commit protocol. It proceeds in three phases:

- Phase 1: Same as phase 1 of two phase commit protocol.
- Phase 2: In this phase, the coordinator asks all the ready participants to prepare to commit. The participants either vote commit or abort.
- Phase 3: In this phase, the coordinator either commits the transaction if all the participants voted commit in phase 2 or aborts the transaction if any participant voted abort in phase 2.

The three phase commit protocol is non-blocking but suffers from single point of failure disadvantage.