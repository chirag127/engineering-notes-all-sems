### Transactions
- A transaction is a logical unit of work that accesses and possibly modifies the data in a distributed system.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the data, such as uniqueness, referential integrity, etc.
- Isolation means that a transaction executes as if it were the only one in the system, without interference from other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted.
- A transaction begins in the active state, where it executes its operations.
- A transaction enters the partially committed state when it issues a commit request, indicating that it has completed its operations successfully.
- A transaction enters the committed state when it receives a confirmation that its commit request has been processed and its effects are durable.
- A transaction enters the failed state when it encounters an error or a failure that prevents it from completing its operations.
- A transaction enters the aborted state when it is rolled back, undoing its effects and releasing any resources it acquired.
- A transaction can only transition from one state to another according to the following state diagram:

![Transaction state diagram](https://i.imgur.com/6Z0c6Zl.png)

- A transaction manager is a component of a distributed system that is responsible for coordinating the execution of transactions across multiple nodes.
- A transaction manager typically performs the following tasks:
  - Assigning unique identifiers to transactions and keeping track of their states.
  - Communicating with other transaction managers to ensure global atomicity and consistency of transactions.
  - Managing the concurrency control and recovery mechanisms for transactions.
  - Handling failures and aborts of transactions and ensuring their durability.