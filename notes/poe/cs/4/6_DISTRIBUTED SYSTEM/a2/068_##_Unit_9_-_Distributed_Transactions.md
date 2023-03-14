 Here is the content in markdown format for the topic ## Unit 9 - Distributed Transactions:

## Unit 9 - Distributed Transactions

- Distributed transactions involve multiple databases or systems and atomicity, consistency, isolation, and durability (ACID) properties must be maintained across all systems.
- A distributed transaction manager handles coordination between the resource managers (databases). It uses a two-phase commit protocol to ensure all-or-nothing execution.
- In phase 1 (prepare), the transaction manager asks all resource managers to prepare to commit the transaction. If all agree, it proceeds to phase 2. If any cannot prepare, the transaction is aborted.
- In phase 2 (commit), the transaction manager orders all resource managers to commit the transaction. If any fail, the transaction manager aborts the transaction at all others.
- Challenges include network failures, resource manager failures, and lack of atomic commit capabilities in some systems. Compensating transactions may be needed to undo partial executions.
- Examples of distributed transactions include transfers across multiple accounts, inventory updates across warehouses, and assembly of components from various manufacturing plants.

**Mnemonics**:

- ACID needs to be maintained across all systems in a distributed transaction.
- Two-phase commit uses prepare and commit phases to ensure all-or-nothing execution.
- Challenges include failures and lack of full transactional capabilities.
- Examples involve updates across multiple resources.

**Advantages**: Data integrity is upheld; related updates succeed or fail together.
**Disadvantages**: Complexity; performance impacts.

[Detailed diagrams and examples can be added here if required to enhance the learning and understanding]