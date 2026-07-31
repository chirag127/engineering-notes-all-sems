 Here is the content in markdown format without any emojis or external links as per your instructions:

## Unit 8 - Concurrency Control Techniques

1. Locks
- Prevent multiple transactions from accessing the same data item simultaneously
- Can be exclusive locks (only one transaction can lock the data item) or shared locks (multiple transactions can lock the data item for reads, but only one transaction can lock for writes)
- Deadlock can occur if two transactions lock resources in different orders

2. Timestamp ordering
- Each transaction is assigned a timestamp when it starts
- Transactions are executed in timestamp order to ensure serializability
- May require waiting for older transactions to commit, which can reduce concurrency

3. Serializability graph testing
- Build a directed graph of transactions where an edge from T1 to T2 exists if T1 must precede T2 to maintain serializability
- If the graph has a cycle, then the transactions are not serializable and must be rolled back and re-run in a different schedule
- Not commonly used in practice due to the overhead of graph maintenance

4. Multi-version concurrency control (MVCC)
- Each transaction reads from its own snapshot of the database, allowing for high concurrency
- When a transaction commits, its changes are written to the database and made visible to subsequent transactions
- Relies on maintaining multiple versions of data and uses timestamps to determine the correct version to read
- Popular approach used in many databases to maximize concurrency

The content is written in a formal tone with points and without any emojis or external links as per your instructions. Please let me know if you would like me to modify or expand the answer.