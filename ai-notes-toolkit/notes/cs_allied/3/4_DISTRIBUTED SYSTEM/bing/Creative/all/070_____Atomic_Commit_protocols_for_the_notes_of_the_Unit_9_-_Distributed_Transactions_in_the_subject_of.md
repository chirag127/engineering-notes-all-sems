# Atomic Commit Protocols for Distributed Transactions

- A distributed transaction is a transaction that involves multiple servers or nodes in a distributed system.
- An atomic commit protocol is a protocol that ensures that a distributed transaction is either committed or rolled back in its entirety, even if the system fails or some of the nodes fail or crash.
- Ensuring atomic commit is important for maintaining the consistency and integrity of the data in a distributed system.
- There are different types of atomic commit protocols, such as two-phase commit, three-phase commit, parallel commit, and failure-aware commit.

## Two-phase commit (2PC)

- Two-phase commit is the most widely used atomic commit protocol.
- It involves two phases: a prepare phase and a commit phase.
- In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies with a yes or no vote, depending on whether it is ready to commit or not.
- In the commit phase, the coordinator node collects all the votes and decides whether to commit or abort the transaction based on the majority rule.
- If all the votes are yes, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction.
- If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction.
- Two-phase commit ensures atomicity, but it has some drawbacks, such as blocking, high latency, and vulnerability to failures.

## Three-phase commit (3PC)

- Three-phase commit is an extension of two-phase commit that aims to overcome some of its drawbacks.
- It involves three phases: a prepare phase, a pre-commit phase, and a commit phase.
- In the prepare phase, the coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies with a yes or no vote, depending on whether it is ready to commit or not.
- In the pre-commit phase, the coordinator node collects all the votes and decides whether to commit or abort the transaction based on the majority rule.
- If all the votes are yes, the coordinator node sends a pre-commit message to all the participant nodes, instructing them to prepare to commit the transaction.
- If any of the votes are no, or if the coordinator node does not receive all the votes within a timeout, the coordinator node sends an abort message to all the participant nodes, instructing them to roll back the transaction.
- In the commit phase, the coordinator node sends a commit message to all the participant nodes, instructing them to commit the transaction.
- If the coordinator node does not receive an acknowledgment from all the participant nodes within a timeout, it sends a commit message again until it does.
- Three-phase commit reduces the blocking problem of two-phase commit, but it still has high latency and vulnerability to failures.

## Parallel commit

- Parallel commit is a new atomic commit protocol that aims to reduce the latency of distributed transactions to only a single round-trip of distributed consensus.
- It involves two phases: a staging phase and a commit phase.
- In the staging phase, each participant node writes the transaction data to a staging area, which is a temporary location that is not visible to other transactions.
- Each participant node also generates a unique transaction identifier and sends it to a consensus service, which is a distributed system that provides reliable and consistent agreement among nodes.
- The consensus service assigns a global commit timestamp to each transaction identifier and returns it to the participant node.
- In the commit phase, each participant node checks whether its transaction identifier has a global commit timestamp that is lower than the current timestamp of the system.
- If yes, the participant node commits the transaction by moving the data from the staging area to the final location, which is visible to other transactions.
- If no, the participant node aborts the transaction by discarding the data from the staging area.
- Parallel commit ensures atomicity and reduces latency, but it requires a reliable and consistent consensus service.

## Failure-aware commit (FLAC)

- Failure-aware commit is a practical atomic commit protocol that leverages the failure information of the participant nodes to optimize the commit decision and reduce the latency of distributed transactions.
- It involves two phases: a prepare phase and a commit phase.
- In the prepare phase, a coordinator node sends a prepare message to all the participant nodes, asking them to vote on whether to commit or abort the transaction.
- Each participant node replies