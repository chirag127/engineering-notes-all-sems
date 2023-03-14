Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory. OCC assumes that multiple transactions can frequently complete without interfering with each other. While running, transactions use data resources without acquiring locks on those resources. Before committing, each transaction verifies that no other transaction has modified the data it has read. If the check reveals conflicting modifications, the committing transaction rolls back and can be restarted. 

OCC transactions involve these phases: 

- Begin: Record a timestamp marking the transaction's beginning.
- Modify: Read database values, and tentatively write changes.
- Validate: Check whether other transactions have modified data that this transaction has used (read or written). This includes transactions that completed after this transaction's start time, and optionally, transactions that are still active at validation time.
- Commit/Rollback: If there is no conflict, make all changes take effect. If there is a conflict, resolve it, typically by aborting the transaction, although other resolution schemes are possible.

The following diagram illustrates the basic architecture of OCC:

```
+-----------------+     +-----------------+     +-----------------+
| Transaction T1  |     | Transaction T2  |     | Transaction T3  |
+-----------------+     +-----------------+     +-----------------+
| Begin           |     | Begin           |     | Begin           |
|                 |     |                 |     |                 |
| Modify          |     | Modify          |     | Modify          |
|                 |     |                 |     |                 |
| Validate        |     | Validate        |     | Validate        |
|                 |     |                 |     |                 |
| Commit/Rollback |     | Commit/Rollback |     | Commit/Rollback |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+---------------------------------------------------------------+
| Database                                                      |
|                                                               |
| +-----------------+ +-----------------+ +-----------------+   |
| | Data item X     | | Data item Y     | | Data item Z     |   |
| +-----------------+ +-----------------+ +-----------------+   |
| | Value: 10       | | Value: 20       | | Value: 30       |   |
| | Timestamp: 100  | | Timestamp: 200  | | Timestamp: 300  |   |
| +-----------------+ +-----------------+ +-----------------+   |
|                                                               |
+---------------------------------------------------------------+
```

: Optimistic concurrency control - Wikipedia
: Database transactions and optimistic concurrency control in Azure Cosmos DB | Microsoft Learn