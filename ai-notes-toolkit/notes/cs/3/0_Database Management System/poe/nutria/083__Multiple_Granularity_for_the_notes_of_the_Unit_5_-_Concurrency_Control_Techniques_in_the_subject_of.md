
### Multiple Granularity for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

* Multiple granularity is a concurrency control technique used to ensure that concurrent transactions do not interfere with each other when accessing the database.
* It is based on the idea of locking the smallest possible data element (granule) to ensure that the data is not accessed by two transactions at the same time.
* There are two types of granularity: fine-grained and coarse-grained.
* Fine-grained granularity locks the smallest possible data element, such as a single row in a table, while coarse-grained granularity locks the entire table.
* The choice of granularity depends on the type of transaction and the type of data being accessed.
* Fine-grained granularity is used when the transaction involves small amounts of data, while coarse-grained granularity is used when the transaction involves large amounts of data.
* The advantage of using multiple granularity is that it reduces the amount of time required to lock and unlock data elements.
* The disadvantage of using multiple granularity is that it can lead to deadlocks, where two transactions are waiting for each other to release a lock on a data element.