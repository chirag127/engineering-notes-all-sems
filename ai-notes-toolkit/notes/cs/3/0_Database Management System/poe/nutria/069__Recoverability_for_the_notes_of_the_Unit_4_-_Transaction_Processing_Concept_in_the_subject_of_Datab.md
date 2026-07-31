
### Recoverability for the Notes of Unit 4 - Transaction Processing Concept in Database Management System
1. Recoverability is the ability of a database system to restore data to a consistent state after a failure. 
2. A transaction is a set of operations that must be executed as a single unit.
3. A transaction must maintain the ACID properties: atomicity, consistency, isolation, and durability.
4. Database systems must be able to recover from failures in order to maintain the ACID properties.
5. A failure can be caused by hardware or software errors, or by system crashes.
6. Recovery techniques can be divided into two categories: rollback and rollforward.
7. Rollback techniques involve restoring the database to a consistent state by undoing the effects of failed transactions.
8. Rollforward techniques involve restoring the database to a consistent state by redoing the effects of committed transactions.
9. Recovery techniques must be able to handle both system and media failures.
10. Database systems use log files to record the effects of transactions and to facilitate recovery.