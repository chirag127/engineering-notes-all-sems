 Here is the content in markdown format for the given topic:

### Multi-Version Schemes

- Multi-version schemes maintain multiple versions of a data item that is being updated concurrently.
- Each transaction reads a consistent snapshot of the database (an earlier version of the data items it is accessing).
- No locks are required during read operations.
- When a transaction updates a data item, a new version of that item is created.
- The updates by transactions are merged and conflicting versions are resolved during transaction commit.
- This avoids the lost update problem as each transaction is working on its own consistent snapshot.
- Two common multi-version schemes are:
    - Timestamp ordering: Each data item version is marked with a timestamp. Transactions read the latest timestamped version at the time of reading and update creates a new version with a new timestamp.
    - Version vectors: Each transaction maintains a vector that is incremented for each data item updated. Data item versions are marked with transaction IDs and version vectors. Transactions use the version vectors to find a consistent set of versions to work with.

Advantages:
- Eliminates blocking during read operations as no locking is required.
- Throughput can be increased as transactions can execute concurrently without conflicts.
- Lost updates are avoided.

Disadvantages:
- Extra storage space is required to maintain multiple versions.
- Complex concurrency control.
- Transaction rollback and commit becomes expensive due to merging of multiple versions.

Applications:
- Multi-version schemes are suitable for:
-- Databases with high read-write contention.
-- Applications that require high throughput.
-- Databases that cannot tolerate blocking during reads.