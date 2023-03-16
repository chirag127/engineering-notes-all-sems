### Transactions with replicated data

- Transactions are a sequence of operations that are executed atomically, consistently, isolatedly, and durably (ACID properties) on a database system.
- Replication is a technique to distribute data from a source server to other servers while keeping the data updated and synced with the source.
- Transactions with replicated data are transactions that involve data items that are stored on multiple servers and need to be coordinated to ensure consistency and correctness.
- Transactions with replicated data can improve availability, performance, and fault-tolerance of distributed systems, but also introduce challenges such as concurrency control, recovery, and commit protocols.
- Some of the issues and solutions for transactions with replicated data are:

  - Concurrency control: how to ensure serializability and isolation of transactions that access replicated data items on different servers?
    - One solution is to use a primary copy approach, where one server is designated as the primary server for each data item and is responsible for locking and validating transactions that access that item.
    - Another solution is to use a majority consensus approach, where each server maintains a version number for each data item and transactions need to obtain a majority of votes from the servers to commit.
  - Recovery: how to ensure durability and atomicity of transactions that update replicated data items on different servers?
    - One solution is to use a two-phase commit protocol, where a coordinator server initiates the commit process and collects the votes from the participating servers, and then sends a final decision (commit or abort) to all the servers.
    - Another solution is to use a three-phase commit protocol, where a coordinator server adds a pre-commit phase before the final decision to avoid blocking in case of failures.
  - Commit protocols: how to ensure consistency and correctness of transactions that span across multiple servers or databases?
    - One solution is to use a distributed transaction manager, which coordinates the commit process among the servers or databases using a two-phase commit protocol or a variant of it.
    - Another solution is to use an elastic database transaction, which is a feature of Azure SQL Database that allows transactions to span across multiple databases in the same region using a two-phase commit protocol.