# Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A **transaction** is a logical unit of work that accesses and possibly modifies the data in a database.
- A **distributed transaction** is a transaction that involves multiple sites or nodes in a distributed system, such as a network of databases or servers.
- A **transaction recovery** is the process of restoring the database to a consistent state after a transaction failure, such as a system crash, a network partition, or a user abort.
- Transaction recovery is essential for ensuring the **ACID** properties of transactions, which are:
  - **Atomicity**: A transaction either commits (completes) or aborts (undoes) as a whole.
  - **Consistency**: A transaction preserves the integrity constraints of the database.
  - **Isolation**: A transaction does not interfere with other concurrent transactions.
  - **Durability**: The effects of a committed transaction are permanent and survive failures.
- Transaction recovery in distributed systems is more challenging than in centralized systems, because of the following issues:
  - **Partial failures**: Some sites or nodes may fail while others continue to operate, making it difficult to coordinate the outcome of a distributed transaction.
  - **Network failures**: The communication links between sites or nodes may fail, causing network partitions or message losses, which may prevent the exchange of information or acknowledgments among the participants of a distributed transaction.
  - **Concurrency control**: The concurrent execution of distributed transactions may cause conflicts or deadlocks, which may require aborting or restarting some transactions.
  - **Heterogeneity**: The sites or nodes involved in a distributed transaction may have different hardware, software, or data models, which may require data conversion or protocol adaptation.

- To address these challenges, transaction recovery in distributed systems typically relies on the following techniques:
  - **Logging**: Each site or node maintains a log of the operations performed by the transactions, as well as the commit or abort decisions. The log is used to undo or redo the effects of transactions in case of failures.
  - **Two-phase commit (2PC)**: A distributed transaction is coordinated by a designated site or node, called the **coordinator**, which communicates with the other sites or nodes, called the **participants**. The coordinator initiates the commit protocol, which consists of two phases:
    - **Prepare phase**: The coordinator asks each participant to prepare to commit, i.e., to flush its log to stable storage and vote either yes or no. A participant votes yes if it can commit, and no if it cannot or has aborted. The coordinator collects the votes from all participants.
    - **Commit phase**: The coordinator decides to commit the transaction if all participants voted yes, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
  - **Three-phase commit (3PC)**: A variation of 2PC that adds a third phase, called the **pre-commit phase**, to avoid blocking in case of network failures. The pre-commit phase is between the prepare and commit phases, and involves the following steps:
    - **Pre-commit phase**: The coordinator decides to pre-commit the transaction if all participants voted yes, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
    - **Commit phase**: The coordinator decides to commit the transaction if it has received the acknowledgments from all participants, and to abort otherwise. The coordinator sends the decision to all participants, and waits for their acknowledgments. The participants execute the decision and send the acknowledgments to the coordinator.
  - **Shadow versions**: An alternative to logging that avoids the need to undo or redo the effects of transactions. A shadow version is a copy of the data item that is modified by a transaction, which is stored in a separate location from the original data item. The original data item is not overwritten until the transaction commits, and the shadow version is discarded. If the transaction aborts, the original data item is unchanged, and the shadow version is discarded.