### Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of concurrency control methods that do not use locks to ensure serializability of transactions   .
- Time stamping protocols assign a unique timestamp to each transaction when it is created, which reflects its logical or physical start time   .
- Time stamping protocols use the timestamps to order the transactions and resolve any conflicts that may arise due to concurrent execution   .
- Time stamping protocols ensure that any conflicting read and write operations are executed in timestamp order, which is equivalent to the serial order of the transactions   .
- Time stamping protocols can be classified into two types: optimistic and pessimistic.
  - Optimistic time stamping protocols assume that conflicts are rare and allow transactions to execute without checking for conflicts until they commit.
  - Pessimistic time stamping protocols check for conflicts before every read and write operation and abort or delay transactions that violate the timestamp order.
- Time stamping protocols have some advantages and disadvantages over lock-based protocols :
  - Advantages:
    - Time stamping protocols avoid deadlock, as transactions do not acquire any locks that need to be released later .
    - Time stamping protocols are more efficient in terms of memory and communication overhead, as transactions do not need to store or exchange any lock information .
    - Time stamping protocols are more suitable for distributed and parallel systems, as transactions can be ordered globally and consistently based on their timestamps .
  - Disadvantages:
    - Time stamping protocols may cause more aborts and restarts of transactions, as conflicts are detected only at commit time or during execution .
    - Time stamping protocols may suffer from the problem of starvation, as older transactions may be repeatedly aborted by newer transactions with higher timestamps .
    - Time stamping protocols may not reflect the actual order of events in the real world, as timestamps are assigned based on the system clock or a logical counter, which may not be synchronized or accurate .