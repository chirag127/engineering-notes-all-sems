### Validation Based Protocol

- Validation Based Protocol is a concurrency control technique that works on the assumption that interference among transactions is rare and can be detected during validation  .
- It is also called Optimistic Concurrency Control Technique because it does not use locking or timestamping to prevent conflicts, but rather checks for them at the end of the transaction  .
- Validation Based Protocol consists of three phases for each transaction: read phase, validation phase, and write phase   .
- In the read phase, the transaction reads data from the database and makes local copies for updates, but does not write anything to the database   .
- In the validation phase, the transaction checks whether it has any conflicts with other transactions that have already committed or are in the validation phase   .
- A conflict occurs when two transactions access the same data item and at least one of them updates it   .
- The validation phase uses some rules or criteria to decide whether a transaction can commit or has to abort   .
- Some common validation rules are based on timestamps, such as start time, end time, or validation time of each transaction   .
- In the write phase, if the transaction passes the validation, it writes its updates to the database, otherwise it aborts and restarts   .
- Validation Based Protocol has the advantage of avoiding locking overhead and deadlock, but it may incur more aborts and restarts due to conflicts   .