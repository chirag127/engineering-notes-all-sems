 Here is the content in markdown format without any emojis or external links:

### Multiple Granularity for the notes of the Unit 5 - Concurrency Control Techniques in the subject of Database Management System

1. Locking at coarse-grained level: It is used by locking the entire database or a large portion of the database. Coarse-grained locking provides less concurrency but has low overhead.
2. Locking at fine-grained level: It is used by locking a single data item or a small number of data items. Fine-grained locking provides higher concurrency but has higher overhead.
3. Multi-granularity: It uses the benefits of both coarse-grained and fine-grained locking by using a mix of coarse-grained and fine-grained locking. Coarse-grained locking is used when the expected contention is low and fine-grained locking is used when the expected contention is high. This provides high concurrency with reduced overheads.
4. Time stamp ordering: The transaction that starts later is aborted if it requests access to data that has already been accessed by an earlier transaction. The overhead of maintaining time stamps for each data item is high.
5. Optimistic concurrency control: The transactions execute without acquiring any locks initially. Before committing the transaction, the system verifies that no other transaction has modified the data being accessed. If so, the transaction is aborted and re-executed. This provides high concurrency but may result in excessive aborts and re-executions.

The content is written in a formal tone as a study material and in points as instructed. Please let me know if you would like me to modify or add anything.