### Transaction Management for the Notes of the Unit 1 - Introduction in the Subject of Basics of Data Base Management System

- A **transaction** is a logical unit of work that accesses and possibly modifies the data in a database.
- A transaction is a **program unit** whose execution may or may not change the contents of a database.
- A transaction generally represents any **change** in a database, such as inserting, updating, or deleting data.
- Transactions in a database environment have two main purposes:
  - To provide reliable units of work that allow correct recovery from failures and keep a database consistent even in cases of system failure.
  - To provide isolation between programs accessing a database concurrently. If this isolation is not provided, the program's outcomes are possibly erroneous.
- A transaction has a **life cycle** that consists of four possible states: active, partially committed, committed, and aborted.
  - **Active state** - this is the state in which the transaction is executing and performing database operations.
  - **Partially committed state** - this is the state in which the transaction has executed its final statement, but the changes have not been made permanent in the database.
  - **Committed state** - this is the state in which the transaction has completed successfully and the changes have been made permanent in the database.
  - **Aborted state** - this is the state in which the transaction has failed and the changes have been rolled back from the database.
- A transaction must satisfy four **properties**, known as **ACID** properties, to ensure the consistency and reliability of the database.
  - **Atomicity** - this property ensures that either all the operations of a transaction are executed or none of them are. A transaction is treated as a single unit of work and cannot be divided into smaller parts.
  - **Consistency** - this property ensures that a transaction transforms the database from one consistent state to another consistent state. A transaction must follow the integrity constraints and rules of the database.
  - **Isolation** - this property ensures that a transaction is executed independently of other transactions. A transaction should not interfere with or be affected by the concurrent execution of other transactions.
  - **Durability** - this property ensures that the changes made by a committed transaction are permanent and persist even in the event of system failures. A transaction should not lose its effects due to power outages, crashes, or errors.
- A transaction is recorded in a **transaction log** that keeps track of all the modifications made by each transaction. The transaction log is a critical component of the database that allows correct recovery from failures and ensures data integrity.