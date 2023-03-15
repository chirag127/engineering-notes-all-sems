### Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases .

The main objectives of concurrency control are:

- To ensure the **isolation** of transactions, that is, to prevent interference or conflicts between concurrent transactions.
- To resolve **read-write** and **write-write** conflicts, that is, to handle situations where one transaction reads or writes data that is concurrently modified by another transaction.
- To preserve **database consistency**, that is, to ensure that the database state remains valid after the execution of concurrent transactions.

The main challenges of concurrency control are:

- To achieve **high performance** and **scalability**, that is, to allow a large number of transactions to execute concurrently without degrading the system throughput or response time.
- To handle **failures** and **recovery**, that is, to ensure that the database state is restored to a consistent state after a system crash or a transaction abort.
- To support **distributed** and **replicated** databases, that is, to coordinate transactions that span multiple nodes or copies of the database.

The main techniques of concurrency control are:

- **Lock-based protocols**, that is, to use locks or flags to control the access to data items by transactions. Locks can be shared or exclusive, and can be granted or released at different levels of granularity (such as records, pages, tables, etc.).
- **Timestamp-based protocols**, that is, to use timestamps or logical clocks to order the transactions and determine their precedence. Timestamps can be assigned either at the beginning or at the end of a transaction, and can be used to detect and resolve conflicts.
- **Validation-based protocols**, that is, to use a validation or certification phase to check the compatibility of transactions before committing them. Validation can be done either centrally or distributedly, and can be based on serializability or snapshot isolation criteria.
- **Multiversion protocols**, that is, to use multiple versions of data items to allow concurrent reads and writes without conflicts. Multiversion protocols can be based on timestamps, locks, or validation, and can provide different levels of consistency guarantees (such as snapshot isolation, repeatable read, etc.).
- **Optimistic protocols**, that is, to assume that conflicts are rare and allow transactions to execute without any concurrency control, and then check and resolve conflicts at commit time. Optimistic protocols can be based on validation, multiversion, or hybrid techniques.