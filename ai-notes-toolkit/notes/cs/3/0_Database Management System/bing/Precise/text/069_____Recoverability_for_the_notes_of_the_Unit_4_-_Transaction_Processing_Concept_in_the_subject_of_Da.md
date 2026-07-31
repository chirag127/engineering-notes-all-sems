### Recoverability for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- Recoverability is an important concept in transaction processing in database management systems.
- It refers to the ability of a system to recover from failures and ensure that the database remains consistent and correct.
- There are several techniques used to achieve recoverability, including write-ahead logging, checkpoints, and shadow paging.
- Write-ahead logging involves writing changes to a log before they are applied to the database. In the event of a failure, the log can be used to undo or redo changes to the database to ensure consistency.
- Checkpoints involve periodically saving the state of the database to disk. In the event of a failure, the system can be restored to the last checkpoint and changes can be reapplied from the log.
- Shadow paging involves maintaining a copy of the database and making changes to the copy rather than the original. In the event of a failure, the original database can be restored and changes can be reapplied from the log.
- These techniques help ensure that the database remains consistent and correct, even in the event of failures. They are essential for maintaining the integrity of the data in a transaction processing system.