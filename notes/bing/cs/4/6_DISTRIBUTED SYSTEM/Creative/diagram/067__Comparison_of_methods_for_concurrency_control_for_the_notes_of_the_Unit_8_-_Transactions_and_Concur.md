The following is a detailed ASCII diagram for comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM.

```
+----------------------+----------------------+----------------------+----------------------+
|                      |                      |                      |                      |
|  Two-phase locking   |  Timestamp ordering  |  Multi-version       |  Validation          |
|                      |                      |  concurrency control |  concurrency control |
+----------------------+----------------------+----------------------+----------------------+
|                      |                      |                      |                      |
|  - Locks are used to |  - Transactions are  |  - Multiple versions |  - Transactions are  |
|    synchronize       |    assigned unique   |    of data items are |    executed without  |
|    access to data    |    timestamps based  |    maintained and    |    any concurrency   |
|    items by          |    on their arrival  |    accessed based on |    control and then  |
|    concurrent        |    time              |    timestamps        |    validated before  |
|    transactions      |                      |                      |    committing        |
|                      |                      |                      |                      |
|  - A transaction     |  - A transaction can |  - A transaction can |  - A transaction can |
|    must acquire a    |    read or write a   |    read the latest   |    read or write any |
|    shared lock (S)   |    data item only if |    committed version |    data item without |
|    before reading    |    its timestamp is  |    of a data item    |    locking or        |
|    and an exclusive  |    greater than the   |    that is not       |    checking          |
|    lock (X) before   |    timestamps of all |    modified by any   |                      |
|    writing           |    transactions that |    concurrent        |                      |
|                      |    have written it   |    transaction with  |                      |
|                      |                      |    a smaller         |                      |
|                      |                      |    timestamp         |                      |
|                      |                      |                      |                      |
|  - A transaction     |  - A transaction can |  - A transaction can |  - A transaction is  |
|    must release all  |    be aborted if it  |    write a new       |    validated by      |
|    its locks after   |    violates the      |    version of a data |    checking if it    |
|    committing or     |    timestamp order   |    item with its own |    conflicts with    |
|    aborting          |                      |    timestamp         |    any committed     |
|                      |                      |                      |    transaction       |
|                      |                      |                      |                      |
|  - A transaction     |  - A transaction can |  - A transaction can |  - A transaction can |
|    can be blocked if |    be delayed if it  |    be aborted if it  |    be aborted if it  |
|    it cannot obtain  |    cannot read or    |    reads an          |    fails the         |
|    a lock due to     |    write a data item |    inconsistent set  |    validation test   |
|    another           |    due to the        |    of versions       |                      |
|    transaction       |    timestamp order   |                      |                      |
|                      |                      |                      |                      |
+----------------------+----------------------+----------------------+----------------------+
```