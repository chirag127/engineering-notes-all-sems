### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce performance.
- OCC only locks records from the time when the actual update is performed, not when they are fetched from the database for an update.
- OCC works by ensuring that the record being updated or deleted has the same values as it did when the updating or deleting process started.
- OCC can prevent lost updates and deletes by detecting concurrent, conflicting operations and aborting or retrying them.
- OCC is supported on many tables in Microsoft Dataverse, and can be checked by retrieving the table's metadata and looking for the column IsOptimisticConcurrencyEnabled.