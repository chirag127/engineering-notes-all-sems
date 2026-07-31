### Validation Based Protocol

- Validation based protocol is a type of concurrency control technique that works on the validation rules and time-stamps .
- It is also known as optimistic concurrency control technique because it assumes that very less interference occurs, therefore, there is no need for checking while the transaction is executing .
- The protocol consists of three phases for managing concurrent transactions: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data values from the database but the write operation or updates are only applied to the local data copies, not the actual database.
- In the validation phase, the transaction is checked for serializability using certain validation rules based on the time-stamps of the transactions  .
- In the write phase, the transaction can write the updated values to the database if it passes the validation phase, otherwise it is aborted and restarted  .
- The validation based protocol avoids locking and ensures serializability, but it may cause more aborts and restarts than other concurrency control techniques .
