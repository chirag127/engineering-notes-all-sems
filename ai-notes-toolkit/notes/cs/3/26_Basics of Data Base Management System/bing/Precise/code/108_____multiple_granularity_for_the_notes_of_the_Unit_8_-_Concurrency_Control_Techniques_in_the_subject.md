### Multiple Granularity

Multiple granularity refers to the ability to lock data at different levels of granularity. In the context of concurrency control in database management systems, this means that locks can be applied to different levels of the database hierarchy, such as at the database, table, page, or row level.

- **Database-level locking** involves locking the entire database, preventing any other transactions from accessing it. This level of locking is the most restrictive and is typically used for maintenance or backup operations.

- **Table-level locking** involves locking an entire table, preventing any other transactions from accessing it. This level of locking is less restrictive than database-level locking, but still prevents concurrent access to the table.

- **Page-level locking** involves locking a page of data, which is a unit of data storage in a database. This level of locking is less restrictive than table-level locking, as it allows concurrent access to other pages in the table.

- **Row-level locking** involves locking a single row of data, allowing other transactions to access other rows in the table concurrently. This level of locking is the least restrictive and provides the highest level of concurrency.

Multiple granularity locking allows for more flexible and efficient concurrency control, as it allows transactions to lock only the data they need, rather than locking larger portions of the database. However, it also introduces additional complexity in managing locks and ensuring data consistency.