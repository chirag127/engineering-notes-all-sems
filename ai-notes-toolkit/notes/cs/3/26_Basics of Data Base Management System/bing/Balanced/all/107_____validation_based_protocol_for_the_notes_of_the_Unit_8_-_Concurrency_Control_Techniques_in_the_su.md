# Validation Based Protocol in DBMS

- Validation Based Protocol is a concurrency control technique that works on the assumption that interference among transactions is rare and can be detected during validation  .
- It is also called Optimistic Concurrency Control Technique because it does not check for conflicts while the transaction is executing, but only at the end before committing  .
- The protocol consists of three phases for each transaction: read phase, validation phase, and write phase  .
- In the read phase, the transaction reads the data items from the database and stores them in a local buffer. It also records the timestamps of the data items it reads  .
- In the validation phase, the transaction checks whether it can commit without violating the serializability order. It compares its timestamps with those of other transactions that have committed or are in the validation phase  .
- If the transaction passes the validation test, it proceeds to the write phase, where it writes the updated data items from its buffer to the database and commits  .
- If the transaction fails the validation test, it aborts and restarts  .
- The validation test can be based on different criteria, such as start time, end time, or commit time of the transactions  .
- The advantages of validation based protocol are that it avoids locking and deadlock, it allows more concurrency, and it reduces the number of rollbacks  .
- The disadvantages of validation based protocol are that it requires more memory and processing power, it may delay the commit of some transactions, and it may not be suitable for applications that have high interference  .