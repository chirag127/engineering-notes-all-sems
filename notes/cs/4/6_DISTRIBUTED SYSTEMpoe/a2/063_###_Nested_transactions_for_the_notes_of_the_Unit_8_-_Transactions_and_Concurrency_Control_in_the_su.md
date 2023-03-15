 Here is the content in markdown format:

### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Nested transactions are transactions that are nested within other transactions. The commit or abort of an outer transaction determines the commitment of its inner nested transactions.

Advantages:
- Allows hierarchical decomposition of complex transactions into simpler ones. This increases modularity.
- Allows conditional commit of inner transactions based on the outcome of outer transactions.

Disadvantages:
- Makes error recovery complex due to nesting. If an outer transaction aborts, its effects on inner transactions must be undone.
- Reduces concurrency as inner transactions cannot commit until the outer transaction commits. This delays transaction completion.

Examples:
- Transaction to book a conference room and reserve required equipment (outer) with nested transactions to reserve each piece of equipment (inner). The outer transaction commits only if all equipment reservations succeed.
- Transaction to create a new course (outer) with nested transactions to add each lecture (inner). The outer transaction commits only if all lectures are added successfully.

To remember:
- Think of nested transactions as a hierarchy of transactions.
- The fate of inner nested transactions depends on the outer transaction.
- Error recovery and concurrency are challenges with nested transactions due to nesting.

Mnemonics:
Nested transactions - in a hierarchy
Outer transaction leads - inner transactions follow