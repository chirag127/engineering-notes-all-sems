### Validation Based Protocol

- Validation Based Protocol is a type of concurrency control technique that works on the validation rules and time-stamps .
- It is also known as Optimistic Concurrency Control Technique because it assumes that very less interference occurs, therefore, there is no need for checking while the transaction is executing .
- The protocol consists of three phases for managing concurrent transactions: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data values from the database but the write operation or updates are only applied to the local data copies, not the actual database.
- In the validation phase, the transaction is checked for serializability using some validation rules and time-stamps. If the transaction passes the validation, it can proceed to the write phase. Otherwise, it is aborted and restarted  .
- In the write phase, the transaction writes the updated local data copies to the database. No other transaction can access the database during this phase  .
- The validation based protocol avoids locking and deadlock problems, but it may incur high overhead due to validation and restarting of aborted transactions   .
- The validation based protocol is suitable for applications where the probability of conflicts is low and the cost of validation is less than the cost of locking   .