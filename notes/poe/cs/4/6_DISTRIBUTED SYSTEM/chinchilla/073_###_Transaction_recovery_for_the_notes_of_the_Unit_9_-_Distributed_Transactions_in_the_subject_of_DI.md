### Transaction Recovery for the Notes of the Unit 9 - Distributed Transactions in the Subject of Distributed System

In a distributed system, transactions may involve multiple nodes, and they may fail due to various reasons, such as network failures, node crashes, or power outages. To ensure data consistency, the system must be able to recover transactions that have been partially completed before a failure occurs. Transaction recovery is the process of restoring a transaction to its pre-failure state and completing it or rolling it back. In this section, we will discuss different techniques for transaction recovery in distributed systems.

#### Two-Phase Commit (2PC)

Two-phase commit is a widely used protocol for transaction recovery in distributed systems. In this protocol, a coordinator node is responsible for coordinating the transaction among the participating nodes. The protocol has two phases:

1. Prepare Phase: The coordinator sends a prepare message to all participating nodes, asking them if they are ready to commit the transaction. If a node is ready, it replies with a yes message. If a node is not ready or encounters an error, it replies with a no message.

2. Commit Phase: If all participating nodes reply with a yes message, the coordinator sends a commit message to all nodes, asking them to commit the transaction. If any node encounters an error during the commit phase, it sends an abort message to the coordinator, indicating that the transaction should be rolled back.

#### Three-Phase Commit (3PC)

Three-phase commit is an extension of the two-phase commit protocol that adds an extra phase to handle the case where the coordinator fails during the prepare phase. The protocol has three phases:

1. CanCommit Phase: The coordinator sends a canCommit message to all participating nodes, asking them if they are ready to commit the transaction. If a node is ready, it replies with a yes message. If a node is not ready or encounters an error, it replies with a no message.

2. PreCommit Phase: If all participating nodes reply with a yes message, the coordinator sends a preCommit message to all nodes, asking them to prepare to commit the transaction. If any node encounters an error during the preCommit phase, it sends an abort message to the coordinator, indicating that the transaction should be rolled back.

3. Commit Phase: If all participating nodes reply with a prepared message, the coordinator sends a commit message to all nodes, asking them to commit the transaction. If any node encounters an error during the commit phase, it sends an abort message to the coordinator, indicating that the transaction should be rolled back.

#### Write-Ahead Logging (WAL)

Write-ahead logging is a technique for recovering transactions that have been partially completed before a failure occurs. In this technique, all modifications to the database are first written to a log file before they are applied to the database. If a failure occurs, the system uses the log file to recover the database to its pre-failure state. The advantage of this technique is that it does not require coordination among multiple nodes, making it suitable for systems with a large number of nodes.

#### Checkpointing

Checkpointing is a technique for reducing the time required to recover from a failure. In this technique, the system periodically saves a checkpoint of the database to disk. If a failure occurs, the system can recover the database to the last checkpoint and then apply the log file to restore the database to its pre-failure state. The advantage of this technique is that it reduces the amount of data that needs to be processed during the recovery process, making it faster.

#### Mnemonics and Learning Tricks

- Remember the two phases of the two-phase commit protocol as "prepare" and "commit".
- Remember the three phases of the three-phase commit protocol as "can commit", "pre-commit", and "commit".
- Use a visual aid, such as a flowchart or diagram, to help you understand the different phases of the protocols.
- Practice recovering transactions using different techniques on a sample database to reinforce your understanding.