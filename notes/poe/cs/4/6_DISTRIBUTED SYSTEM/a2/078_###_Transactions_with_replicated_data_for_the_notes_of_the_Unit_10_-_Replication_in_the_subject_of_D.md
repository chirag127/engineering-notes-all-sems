 Here is the content in markdown format for the topic ### Transactions with replicated data for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM:

## Transactions with replicated data

- When data is replicated across multiple sites, transactions that access and update the data must be handled carefully to maintain consistency.
- Two common approaches for handling transactions with replicated data are:
    - Primary-backup approach: One replica (the primary) handles all updates. Updates are then propagated to backups. This avoids complex concurrency control but has a single point of failure.
    - Multiple primary approach: Each replica can accept updates. This increases availability but requires mechanisms to resolve conflicts between concurrent updates.
- Conflicts can be resolved in a few ways:
    - Last update wins: The update that is propagated last overwrites any previous updates. This can lead to lost updates.
    - First update wins: The first update to arrive at a replica is the one that is preserved. This can also lead to lost updates.
    - Manual resolution: The conflicting updates are detected and a resolver (either human or automated) determines how to merge them. This maintains consistency but may be impractical for large systems or high volumes of updates.
    - Custom merge functions: Application-specific logic is used to merge the conflicting updates in a way that maintains integrity. This is the most flexible but also the most complex approach.

- Some key things to keep in mind with replicated data and transactions:
    - Updates must be propagated reliably to all replicas.
    - The order of updates can affect consistency and must be handled carefully.
    - Concurrent transactions must be isolated to avoid conflicts.
    - A consistent state must be maintained even in the face of failures, network issues, and other disruptions.

- In summary, managing transactions with replicated data introduces complexities due to maintaining consistency and concurrency control across multiple replicas. The chosen approach depends on availability and consistency needs as well as practical capabilities.