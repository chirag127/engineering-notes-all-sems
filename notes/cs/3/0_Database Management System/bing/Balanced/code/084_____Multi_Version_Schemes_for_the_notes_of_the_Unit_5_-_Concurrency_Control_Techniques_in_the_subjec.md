### Multi Version Schemes for Concurrency Control

- Multi version schemes are a type of concurrency control method that use multiple versions of data objects to allow concurrent access to the database by different transactions.
- The main idea of multi version schemes is to grant an appropriate version of a data object to each read request, and to create a new version of a data object for each write request.
- Multi version schemes can increase the concurrency and performance of the database system, as they reduce the conflicts and delays between read and write operations.
- Multi version schemes can also improve the isolation and consistency of transactions, as they prevent the phenomenon of dirty reads, non-repeatable reads, and phantom reads.
- There are different types of multi version schemes, such as timestamp-based, validation-based, and snapshot-based. Each type has its own advantages and disadvantages, and requires different mechanisms to manage the versions and their visibility.
- Some examples of database management systems that use multi version schemes are PostgreSQL, Oracle, MySQL, and MongoDB.