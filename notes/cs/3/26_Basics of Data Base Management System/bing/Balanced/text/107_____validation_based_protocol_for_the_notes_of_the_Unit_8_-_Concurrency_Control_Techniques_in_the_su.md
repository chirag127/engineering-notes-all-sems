### Validation Based Protocol in DBMS

- Validation Based Protocol is a concurrency control technique that works on the assumption that very few transactions interfere with each other, and therefore there is no need for checking while the transaction is executing  .
- It is also called Optimistic Concurrency Control Technique because it optimistically allows transactions to execute without any locking or checking, and only validates them at the end  .
- Validation Based Protocol divides the execution of a transaction into three phases: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It does not write anything to the database in this phase  .
- In the validation phase, the transaction checks whether it can commit without violating the serializability of the schedule. It uses timestamps to determine the order of transactions and compares them with the read and write sets of other transactions  .
- In the write phase, if the transaction passes the validation, it writes the updated data items from the local buffer to the database. Otherwise, it aborts and restarts  .
- Validation Based Protocol ensures serializability and avoids deadlock, but it may cause more aborts and restarts than locking protocols. It also requires more storage space for maintaining the read and write sets of transactions   .