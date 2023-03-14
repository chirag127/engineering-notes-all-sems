## Unit 9 - Distributed Transactions

- A distributed transaction is a transaction that involves multiple sites or nodes in a distributed system, such as a network of databases or servers.
- A distributed transaction has the same ACID properties as a local transaction, which are:
  - Atomicity: The transaction is either executed completely or not at all.
  - Consistency: The transaction preserves the consistency of the data, meaning that it does not violate any integrity constraints or business rules.
  - Isolation: The transaction is executed as if it were the only one running in the system, meaning that it does not interfere with or see the effects of other concurrent transactions.
  - Durability: The effects of the transaction are permanent, meaning that they are not lost in case of a system failure or crash.
- A distributed transaction can be classified into two types, depending on how the commit decision is made:
  - Two-phase commit (2PC): The commit decision is made by a coordinator node, which communicates with all the participant nodes involved in the transaction. The coordinator node initiates a prepare phase, where it asks each participant node to vote on whether they are ready to commit or abort the transaction. If all the participant nodes vote to commit, the coordinator node initiates a commit phase, where it instructs each participant node to commit the transaction. If any participant node votes to abort, or if the coordinator node fails to receive a vote from any participant node, the coordinator node initiates an abort phase, where it instructs each participant node to abort the transaction.
  - Three-phase commit (3PC): The commit decision is made by a majority of the participant nodes involved in the transaction, without relying on a single coordinator node. The participant nodes communicate with each other in three phases: a pre-commit phase, where each participant node decides whether to commit or abort the transaction and informs the other participant nodes; a commit phase, where each participant node commits the transaction if it receives a commit message from a majority of the participant nodes, or aborts the transaction otherwise; and an acknowledgement phase, where each participant node acknowledges the commit or abort decision to the other participant nodes.
- A distributed transaction can face various challenges and problems, such as:
  - Network failures: The communication between the nodes involved in the transaction may be disrupted or delayed due to network issues, such as congestion, partitioning, or disconnection.
  - Node failures: The nodes involved in the transaction may crash or become unavailable due to hardware or software issues, such as power outage, disk failure, or bug.
  - Concurrency control: The nodes involved in the transaction may need to coordinate their access to the shared data, such as locking, timestamping, or versioning, to ensure the isolation and consistency of the transaction.
  - Deadlocks: The nodes involved in the transaction may wait for each other to release the locks on the shared data, resulting in a circular dependency that prevents the transaction from progressing.
  - Data replication: The nodes involved in the transaction may have different copies or versions of the shared data, which may need to be synchronized or reconciled to ensure the consistency of the transaction.
  - Security: The nodes involved in the transaction may need to authenticate and authorize each other, as well as encrypt and decrypt the data, to ensure the confidentiality and integrity of the transaction.

- A distributed transaction can have various advantages and disadvantages, such as:
  - Advantages:
    - Scalability: A distributed transaction can handle a large amount of data and requests by distributing the workload among multiple nodes.
    - Availability: A distributed transaction can tolerate node failures by relying on other nodes to continue the transaction.
    - Performance: A distributed transaction can reduce the latency and bandwidth consumption by executing the transaction locally at each node, rather than transferring the data to a central node.
    - Fault tolerance: A distributed transaction can recover from node or network failures by using protocols such as 2PC or 3PC to ensure the atomicity and durability of the transaction.
  - Disadvantages:
    - Complexity: A distributed transaction can introduce more complexity and overhead in the system design and implementation, such as managing the communication, coordination, and synchronization among the nodes.
    - Consistency: A distributed transaction can compromise the consistency of the data, especially in the presence of network or node failures, or data replication, which may result in inconsistent or stale data across the nodes.
    - Isolation: A distributed transaction can compromise the isolation of the transaction, especially in the presence of concurrency control or deadlocks, which may result in interference or conflicts among the transactions.
    - Security: A distributed transaction can compromise the security of the transaction, especially in the presence of malicious or compromised nodes, which may result in data leakage or tampering.

- A distributed transaction can have various applications