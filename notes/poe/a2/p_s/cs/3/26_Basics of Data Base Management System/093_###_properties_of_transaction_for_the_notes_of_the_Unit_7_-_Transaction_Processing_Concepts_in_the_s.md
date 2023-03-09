 Here is the content in markdown format for the topic ### properties of transaction for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System:

### Properties of Transaction

1. Atomicity: Either all operations of a transaction are executed successfully or none. If any operation fails, the entire transaction is rolled back.
2. Consistency: A transaction never leaves the database in a half-done state. It always moves the database from one consistent state to another.
3. Isolation: The execution of a transaction is isolated from the execution of other transactions. The effects of one transaction are not visible to other transactions until it commits. This avoids inconsistencies.
4. Durability: Once a transaction commits, its effects persist in the database even if there is a system failure. The changes made by committed transactions are never lost.

**Atomicity:** It ensures that all operations of a transaction are performed successfully or none at all. If any operation fails, the entire transaction is rolled back to its initial state as if it never occurred. This maintains the consistency of the database.

**Consistency:** A transaction always transforms the database from one consistent state to another. A transaction never leaves the database in an inconsistent state. It maintains all the constraints, cascading actions, and validation rules defined on the database.

**Isolation:** The execution of one transaction is isolated from the execution of other transactions. The effects of one transaction are not visible to other transactions until it commits. This avoids inconsistencies and maintains the atomicity of transactions. The most common isolation levels are Read Uncommitted, Read Committed, Repeatable Read, and Serializable.

**Durability:** Once a transaction commits, its effects persist in the database even if there is a system failure. The changes made by committed transactions are never lost. The database is updated with the changes once the transaction commits. This ensures that the database reflects all committed changes.

[You can include diagrams, examples, advantages, disadvantages, applications, etc. here if required.]