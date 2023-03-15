### Recoverability for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- Recoverability is an important concept in transaction processing in a database management system.
- It refers to the ability of a system to recover from failures and ensure that the database remains in a consistent state.
- To ensure recoverability, the system must keep track of all changes made to the database during a transaction.
- This is typically done using a log, which records all changes made to the database.
- In the event of a failure, the system can use the log to undo any changes made during the transaction and restore the database to its previous state.
- There are several techniques used to ensure recoverability, including write-ahead logging and shadow paging.
- Write-ahead logging ensures that changes are written to the log before they are applied to the database.
- Shadow paging, on the other hand, involves creating a copy of the database and making changes to the copy rather than the original.
- In the event of a failure, the system can simply switch to the copy to ensure that the database remains consistent.
- It is important to note that recoverability is not the same as durability, which refers to the ability of the system to ensure that committed transactions are permanent and survive any subsequent failures.