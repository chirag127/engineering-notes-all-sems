
### Recovery from Transaction Failures

1. A transaction failure occurs when a transaction is not completed successfully due to a system or user error. 
2. Transaction processing systems must have a way to recover from transaction failures. 
3. There are two ways to recover from transaction failures: 
    1. Rollback: This involves undoing the effects of the transaction by restoring the database to the state it was in before the transaction began. 
    2. Compensation: This involves compensating for the effects of the transaction by taking corrective action to restore the database to a consistent state. 
4. To ensure the database remains in a consistent state, the system must maintain an audit trail of all transactions. 
5. The audit trail is used to identify the transactions that need to be rolled back or compensated. 
6. Once the transactions have been identified, the system must take appropriate action to restore the database to a consistent state. 
7. The recovery process must also ensure that the effects of the transaction are not lost. 
8. The recovery process must also ensure that the database remains in a consistent state after the recovery process is complete.