## Unit 8 - Concurrency Control Techniques

- Concurrency control techniques are methods to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by the transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and timestamp-based concurrency control.
- Concurrency control techniques can also be classified based on the level of data abstraction they operate on: record-level, page-level, or file-level.
- Record-level concurrency control techniques lock individual records or tuples in the database. They provide the finest granularity of locking and the highest degree of concurrency, but also incur the highest overhead of locking and unlocking operations.
- Page-level concurrency control techniques lock entire pages or blocks of records in the database. They provide a coarser granularity of locking and a lower degree of concurrency, but also reduce the overhead of locking and unlocking operations.
- File-level concurrency control techniques lock entire files or tables in the database. They provide the coarsest granularity of locking and the lowest degree of concurrency, but also eliminate the overhead of locking and unlocking operations.