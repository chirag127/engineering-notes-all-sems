Recovery in concurrent systems is the process of restoring the system to a consistent state after a failure, while allowing multiple transactions to execute simultaneously. There are different techniques for recovery in concurrent systems, such as checkpointing, transaction rollback, and restart recovery. Here is a possible diagram for recovery in concurrent systems using checkpointing:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Transaction 1  |     |  Transaction 2  |     |  Transaction 3  |
|                 |     |                 |     |                 |
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|     Log File    |     |     Log File    |     |     Log File    |
|                 |     |                 |     |                 |
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
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Checkpoint    |     |   Checkpoint    |     |   Checkpoint    |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Database      |     |   Database      |     |   Database      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The diagram shows how each transaction writes its updates to a log file, and periodically saves its state to a checkpoint. A checkpoint is a point of time at which a record is written onto the database from the buffers. Checkpointing reduces the number of log records that the system must scan when it recovers from a crash. If a failure occurs, the system can restore the database to the last checkpoint, and then redo or undo the transactions that were active at that time. This way, the system can recover from a failure without losing any committed updates or violating any consistency constraints.