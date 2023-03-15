# Validation Based Protocol

- Validation Based Protocol is a type of concurrency control technique that works on the validation rules and timestamps .
- It is also called Optimistic Concurrency Control Technique because it assumes that very few conflicts occur among transactions .
- It does not check for conflicts while the transaction is executing, but only at the end of the transaction .
- It divides the transaction into three phases: read phase, validation phase, and write phase  .

## Read Phase
- In the read phase, the transaction can read data values from the database, but it can only write or update the local copies of the data, not the actual database .
- The transaction also records the timestamps of the data items it reads, which are used later for validation .

## Validation Phase
- In the validation phase, the transaction checks whether it has any conflicts with other transactions that have already committed  .
- A conflict occurs when two transactions access the same data item and at least one of them performs a write operation .
- The validation phase uses the timestamps of the transactions and the data items to detect conflicts  .
- There are different validation rules that can be applied, such as basic timestamp ordering, Thomas' write rule, and multiversion timestamp ordering .
- If the transaction passes the validation phase, it can proceed to the write phase. Otherwise, it is aborted and restarted  .

## Write Phase
- In the write phase, the transaction writes or updates the actual database with the local copies of the data .
- The transaction also commits and releases any locks it may have acquired  .
- The write phase is performed only after the validation phase is successful  .

## Advantages and Disadvantages of Validation Based Protocol
- Some advantages of validation based protocol are :
  - It avoids locking overhead and deadlock problems.
  - It allows more concurrency among transactions as they do not block each other during execution.
  - It is suitable for applications where conflicts are rare and transactions are short-lived.
- Some disadvantages of validation based protocol are :
  - It may waste resources and time by executing transactions that may fail the validation phase.
  - It may cause cascading aborts if a transaction that has validated successfully is aborted later due to some reason.
  - It may not be suitable for applications where conflicts are frequent and transactions are long-lived.