### Atomic Commit in Distributed Database system for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

Atomic Commit is a distributed database system protocol that ensures that every transaction is either fully committed or fully aborted. It is used to maintain the consistency and integrity of data in a distributed system. The protocol ensures that all nodes participating in a transaction either commit or abort the transaction atomically, i.e., all nodes must agree on the outcome of the transaction.

#### How does Atomic Commit work?

Atomic Commit protocol involves the following steps:

1. The coordinator node initiates the transaction and sends a request to all participant nodes to perform the operation.

2. Each participant node executes the operation and sends back an acknowledgment to the coordinator.

3. The coordinator collects all acknowledgments from the participant nodes and decides whether to commit or abort the transaction.

4. If all nodes have acknowledged that the operation was successful, the coordinator sends a commit message to all nodes. Otherwise, it sends an abort message to all nodes.

5. Each participant node takes the appropriate action based on the message received from the coordinator. If the message is a commit message, the node makes the changes to the database permanent. Otherwise, it rolls back the changes made during the transaction.

#### Advantages of Atomic Commit

- Ensures that transactions are executed consistently across all nodes in the system.
- Maintains data integrity by ensuring that transactions are either fully committed or fully aborted.
- Reduces the possibility of data inconsistencies that may occur in a distributed system.

#### Disadvantages of Atomic Commit

- Increased communication overhead due to the need for the coordinator to communicate with all participant nodes.
- Increased latency due to the time it takes to collect acknowledgments from all participant nodes.

#### Example

Consider a scenario where a customer wants to transfer money from one account to another in a distributed system with two nodes. The Atomic Commit protocol would work as follows:

1. The customer initiates the transaction by sending a request to Node A.

2. Node A sends a request to Node B to update the balance of the receiving account.

3. Node B sends an acknowledgment to Node A.

4. Node A collects all acknowledgments and decides whether to commit or abort the transaction.

5. If all nodes have acknowledged that the operation was successful, Node A sends a commit message to Node B. Otherwise, it sends an abort message to Node B.

6. Node B takes the appropriate action based on the message received from Node A. If the message is a commit message, it makes the changes to the database permanent. Otherwise, it rolls back the changes made during the transaction.

#### Applications

Atomic Commit protocol is widely used in distributed database systems, where data consistency and integrity are crucial. It is used in applications such as online banking, e-commerce, and data processing systems.

#### Conclusion

The Atomic Commit protocol is an essential part of distributed systems that helps ensure data consistency and integrity. It provides a mechanism for maintaining the consistency of data across all nodes in a distributed system, thereby reducing the possibility of data inconsistencies.