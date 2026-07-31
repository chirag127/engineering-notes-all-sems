# Unit 4 - Transaction Processing Concept

- A transaction is a logical unit of work that accesses and possibly modifies data in a database or a system.
- A transaction processing system (TPS) is a system that supports the execution of transactions in a reliable, efficient and secure manner.
- A transaction has four main properties, known as ACID:
  - Atomicity: A transaction is either completed in its entirety or not at all. If any part of the transaction fails, the entire transaction is aborted and the system is restored to its previous state.
  - Consistency: A transaction preserves the integrity and validity of the data in the system. It ensures that the system moves from one consistent state to another consistent state, without violating any rules or constraints.
  - Isolation: A transaction is executed independently of other transactions. It does not interfere with or see the effects of other concurrent transactions. Each transaction appears as if it is the only one running in the system.
  - Durability: A transaction, once committed, is permanent and cannot be undone. The effects of a committed transaction are preserved even in the event of system failures or power outages.
- A transaction can have one of the following outcomes:
  - Commit: The transaction successfully completes all its operations and makes its changes permanent in the system.
  - Abort: The transaction fails to complete all its operations and discards any changes it has made in the system.
  - Partial commit: The transaction completes some of its operations but not all. This is an undesirable outcome that violates the atomicity property and can lead to data inconsistency or corruption.
- A transaction can be classified into one of the following types:
  - Interactive transaction: A transaction that is initiated and controlled by a human user, such as withdrawing money from an ATM or booking a flight ticket online.
  - Batch transaction: A transaction that is executed as a group of transactions, without user intervention, such as payroll processing or billing.
  - Distributed transaction: A transaction that involves multiple systems or databases, such as transferring money between different banks or updating inventory across different warehouses.
  - Real-time transaction: A transaction that has strict time constraints and requires immediate response, such as stock trading or online gaming.