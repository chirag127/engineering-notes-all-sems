### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a transaction failure.
- Transaction failure can occur due to various reasons, such as system failure, hardware failure, network error, invalid or incorrect data, application problems, etc.
- Transaction recovery is one of the most challenging tasks in distributed databases, as it is very difficult to identify and correct the source of the problem in a large communication network.
- Transaction recovery requires a distributed commit protocol, which is a mechanism to ensure that all the nodes involved in a transaction agree on the final outcome (commit or abort) of the transaction.
- One of the most popular distributed commit protocols is the Two-Phase Commit Protocol (2PC), which uses two types of nodes: the coordinator and the subordinates.
- The coordinator is the node that initiates the transaction and communicates with the subordinates, which are the nodes that execute the transaction operations on their local data.
- The 2PC protocol consists of two phases: the prepare phase and the decision phase.
  - In the prepare phase, the coordinator sends a PREPARE message to all the subordinates, asking them to vote on whether they are ready to commit or not.
  - In the decision phase, the coordinator collects the votes from the subordinates and decides whether to commit or abort the transaction based on the majority rule.
  - If all the subordinates vote YES, the coordinator sends a COMMIT message to all the subordinates, instructing them to commit their local changes and release the locks.
  - If any subordinate votes NO, or if the coordinator does not receive a vote from any subordinate within a timeout period, the coordinator sends an ABORT message to all the subordinates, instructing them to roll back their local changes and release the locks.
- The 2PC protocol ensures atomicity and durability of distributed transactions, but it has some drawbacks, such as:
  - It is a blocking protocol, which means that if the coordinator or any subordinate fails during the protocol execution, the other nodes have to wait indefinitely until the failed node recovers.
  - It is a costly protocol, which requires a lot of messages and disk accesses to complete the transaction.
  - It is a rigid protocol, which does not allow any flexibility or optimization in the transaction execution.
- There are some variations of the 2PC protocol, such as:
  - Centralized 2PC, which limits the communication to the coordinator and does not allow any communication between the subordinates.
  - Linear 2PC, which organizes the subordinates in a linear chain and passes the messages along the chain, reducing the number of messages but increasing the latency.
  - Distributed 2PC, which allows the subordinates to communicate with each other and elect a new coordinator in case of a failure, increasing the fault tolerance but also the complexity.
- There are also some alternative distributed commit protocols, such as:
  - Three-Phase Commit Protocol (3PC), which adds a pre-commit phase between the prepare and the decision phases, reducing the blocking problem but increasing the message overhead.
  - Paxos Commit Protocol, which uses a consensus algorithm to reach an agreement among the nodes, tolerating the failure of any number of nodes but requiring a lot of rounds of communication.
  - Sagas, which decompose a long-running transaction into a sequence of compensatable subtransactions, avoiding locking and blocking but requiring additional logic to handle failures and rollbacks.

: https://www.geeksforgeeks.org/transaction-recovery-in-distributed-system/
: https://developers.redhat.com/articles/2021/09/21/distributed-transaction-patterns-microservices-compared