 Here are the notes on Properties of Transaction for the topic Transaction Processing Concepts:

### Properties of Transaction

1. Atomicity: Either all operations of a transaction are performed or none. If one operation fails, the entire transaction is rolled back.
2. Consistency: A transaction must leave the database in a consistent state. It must not violate any database constraints or rules.
3. Isolation: Transactions are isolated from each other. The intermediate state of a transaction is not visible to other transactions. This avoids inconsistent reads.
4. Durability: Once a transaction has been committed, its effects persist even if there is a system failure. The database must keep track of executed transactions to guarantee durability.

A transaction has ACID properties - Atomicity, Consistency, Isolation and Durability that ensure database transactions are processed reliably. Proper implementation of transactions is critical for correct functioning of database systems.

This notes cover the key properties of transactions that are essential concepts to understand transaction processing in database management systems. Let me know if you would like me to elaborate on any of the points or add additional details.