# Multi-version Schemes for Concurrency Control

- Multi-version concurrency control (MVCC) is a technique that allows concurrent access to the database without locking the data.
- MVCC creates multiple versions of each data item and assigns them timestamps to indicate their validity periods.
- MVCC ensures that each transaction reads the most recent committed version of the data that is consistent with its snapshot.
- MVCC avoids the problems of locking-based concurrency control, such as deadlocks, starvation, and blocking.
- MVCC improves the performance and scalability of database applications in a multiuser environment.

## How MVCC Works

- While different database systems may implement MVCC in their own ways, the general idea is as follows:
  - Every database record has a version number that is incremented whenever the record is updated.
  - Concurrent reads happen against the record with the highest version number that is lower than or equal to the transaction's snapshot.
  - Write operations operate on a copy of the record, not the record itself.
  - Users continue to read the older version while the copy is updated.
  - After the write operation is successful, the version number is incremented and the copy becomes the new version.
  - Subsequent concurrent reads use the updated version.
  - Old versions of the records are eventually garbage collected when they are no longer needed.

## Example of MVCC

- Suppose we have a table called `products` with the following schema and data:

| id | name | price | version |
| -- | ---- | ----- | ------- |
| 1  | A    | 10    | 1       |
| 2  | B    | 20    | 1       |
| 3  | C    | 30    | 1       |

- Now suppose we have two transactions, T1 and T2, that execute concurrently as follows:

| T1                          | T2                          |
| --------------------------- | --------------------------- |
| begin                       | begin                       |
| read products where id = 1  | read products where id = 2  |
| update products set price = 15 where id = 1 | update products set price = 25 where id = 2 |
| commit                      | commit                      |

- With MVCC, the transactions will execute without any conflict or locking as follows:
  - T1 and T2 start with their own snapshots of the database, which are the same as the initial state of the table.
  - T1 reads the product with id = 1, which has version 1 and price 10.
  - T2 reads the product with id = 2, which has version 1 and price 20.
  - T1 updates the product with id = 1 by creating a copy of the record with version 2 and price 15.
  - T2 updates the product with id = 2 by creating a copy of the record with version 2 and price 25.
  - T1 commits and the copy of the product with id = 1 becomes the new version.
  - T2 commits and the copy of the product with id = 2 becomes the new version.
  - The final state of the table is as follows:

| id | name | price | version |
| -- | ---- | ----- | ------- |
| 1  | A    | 15    | 2       |
| 2  | B    | 25    | 2       |
| 3  | C    | 30    | 1       |

- Note that T1 and T2 did not interfere with each other, as they read and wrote different versions of the data.
- Note also that the old versions of the products with id = 1 and 2 are still present in the database, but they are marked as invalid and will be deleted later.