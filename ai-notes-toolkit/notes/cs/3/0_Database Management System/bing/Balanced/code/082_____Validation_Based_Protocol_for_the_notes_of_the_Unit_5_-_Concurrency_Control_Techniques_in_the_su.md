### Validation Based Protocol

- Validation based protocol is a type of concurrency control technique that works on the validation rules and time-stamps .
- It is also known as optimistic concurrency control technique because it assumes that very less interference occurs, therefore, there is no need for checking while the transaction is executing .
- The protocol consists of three phases for managing concurrent transactions: read phase, validation phase, and write phase  .
- In the read phase, the transaction can read data values from the database but the write operation or updates are only applied to the local data copies, not the actual database.
- In the validation phase, the transaction is checked for serializability using certain validation rules and time-stamps  .
- In the write phase, if the transaction passes the validation phase, then the updates are applied to the actual database, otherwise the transaction is aborted and restarted  .
