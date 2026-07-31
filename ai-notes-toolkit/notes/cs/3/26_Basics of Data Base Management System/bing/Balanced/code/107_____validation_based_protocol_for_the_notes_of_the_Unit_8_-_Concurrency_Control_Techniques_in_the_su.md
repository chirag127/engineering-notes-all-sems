### Validation Based Protocol in DBMS

- Validation based protocol is a type of concurrency control technique that works on the assumption that very few transactions interfere with each other, and therefore there is no need to check for conflicts while the transaction is executing  .
- It is also called optimistic concurrency control technique because it optimistically allows transactions to execute without locking any data items, and only validates them at the end to ensure serializability  .
- The protocol consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items it reads  .
- In the validation phase, the transaction checks whether it can commit without violating serializability. It does so by comparing its timestamps with those of other transactions that have already committed or are in the validation phase. The validation rules are as follows  :
  - If the transaction Ti reads a data item X that was written by another transaction Tj, then Ti must start after Tj commits. This ensures that Ti does not read a dirty value of X.
  - If the transaction Ti writes a data item X that was read by another transaction Tj, then Ti must start before Tj starts. This ensures that Ti does not overwrite a value of X that Tj has already read.
  - If the transaction Ti writes a data item X that was written by another transaction Tj, then Ti must start after Tj commits. This ensures that Ti does not cause a lost update of X.
- If the transaction passes the validation phase, it moves to the write phase, where it writes the updated data items from its local buffer to the database. It also commits and releases any resources it holds  .
- If the transaction fails the validation phase, it aborts and restarts from the beginning  .
- The advantages of validation based protocol are that it avoids locking and deadlock, and it allows more concurrency and parallelism among transactions  .
- The disadvantages of validation based protocol are that it may cause more aborts and restarts, and it requires more memory and processing power to store and validate timestamps  .