Recovery in distributed database systems is the process of restoring the consistency and durability of transactions that span multiple sites in the event of failures. Failures can be classified into soft failures, such as power outages or network partitions, and hard failures, such as disk crashes or site failures. Different recovery techniques are used to handle different types of failures, such as undo/redo logging, checkpointing, and distributed commit protocols.

The following diagram illustrates the basic architecture of a distributed database system with recovery components:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Site 1          |    | Site 2          |    | Site 3          |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Transaction | |    | | Transaction | |    | | Transaction | |
| | Manager     | |    | | Manager     | |    | | Manager     | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       |         |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Recovery    | |    | | Recovery    | |    | | Recovery    | |
| | Manager     | |    | | Manager     | |    | | Manager     | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       |         |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Data        | |    | | Data        | |    | | Data        | |
| | Manager     | |    | | Manager     | |    | | Manager     | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       |         |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Data        | |    | | Data        | |    | | Data        | |
| | Dictionary  | |    | | Dictionary  | |    | | Dictionary  | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       |         |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Log         | |    | | Log         | |    | | Log         | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       |         |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Database    | |    | | Database    | |    | | Database    | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
        |                     |                     |
        |                     |                     |
        +---------------------+---------------------+
                          |
                          |
                    +-------------+
                    | Network     |
                    +-------------+
```

Each site has a transaction manager, a recovery manager, a data manager, a data dictionary, a log, and a database. The transaction manager is responsible for coordinating the execution of distributed transactions across multiple sites. The recovery manager is responsible for maintaining the log and restoring the database to a consistent state after a failure. The data manager is responsible for accessing and updating the database. The data dictionary is responsible for storing the metadata and schema information of the database. The log is responsible for recording the changes made by transactions and the actions of the recovery manager. The database is responsible for storing the actual data.

The network is responsible for connecting the sites and enabling communication among them. The network may fail or become partitioned, which affects the availability and consistency of the database. The recovery manager must handle such network failures and ensure that the distributed transactions are either committed or aborted atomically.