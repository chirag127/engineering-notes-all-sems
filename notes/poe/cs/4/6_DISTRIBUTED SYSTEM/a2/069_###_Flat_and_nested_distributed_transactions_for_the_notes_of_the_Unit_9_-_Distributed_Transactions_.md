 Here is the content in markdown format:

### Flat and nested distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

Flat distributed transactions:
- involve two or more servers.
- either all transactions commit or all abort.
- transactions are isolated from each other.

Nested distributed transactions:
- form a tree structure with the root transaction at the top.
- if the root transaction commits, then all nested transactions must commit.
- if the root transaction aborts, then all nested transactions are aborted.
- allow partial outcomes and increased concurrency.

**Mnemonics:**
 Flat = all or none
 Nested = tree structure

**Advantages of flat distributed transactions:**
- Atomicity is ensured. Either all transactions complete successfully or none do.
- Isolation between transactions is maintained.

**Disadvantages of flat distributed transactions:**
- Reduced concurrency. Nested transactions allow increased concurrency.

**Advantages of nested distributed transactions:**
- Increased concurrency is possible as partial outcomes are allowed.

**Disadvantages of nested distributed transactions:**
- Atomicity may be violated if some nested transactions commit but the root transaction aborts.
- Isolation between nested transactions is lost.

*Applications:* Distributed databases, workflow systems.

Detailed diagrams and examples can be included if required. The content can be expanded with more points and details as needed.