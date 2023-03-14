 Here is the content in markdown format:

### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Nested transactions are transactions that are nested within other transactions. The commit or rollback of a nested transaction is dependent on the outer transaction within which it is nested.

**Points to note:**

- The nested transaction (inner transaction) can commit only if the outer transaction commits. If the outer transaction aborts, then all its nested transactions must also abort.
- The failure of a nested transaction does not affect the status of its outer transaction. The outer transaction can still commit successfully.
- Data updates performed by a nested transaction are only visible to other transactions after its outer transaction commits.

**Mnemonics:**

Outer transaction is the *boss* of nested transaction

**Advantages:**

- Allows modular decomposition of transactions. Smaller parts (nested transactions) can be managed independently.
- Increase concurrency as nested transactions can commit without waiting for outer transaction.

**Disadvantages:**

- Makes error handling and recovery complex due to interdependencies between nested and outer transactions.
- Reduces concurrency if a transaction is waiting for its nested transaction to commit/abort.

**Applications:**

- Used in hierarchical databases to maintain referential integrity.
- Used in workflow systems to model the various steps/stages. The commit/rollback of a stage (nested transaction) depends on the overall workflow (outer transaction).

**Diagrams:**

[A diagram showing nested transactions with commit/abort dependencies]

[Detailed codes/examples if any]