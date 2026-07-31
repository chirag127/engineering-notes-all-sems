### Time Stamping Protocols for Concurrency Control

- Time stamping protocols are a type of concurrency control methods that do not use locks to ensure serializability of transactions   .
- Time stamping protocols assign a unique timestamp to each transaction when it is created, which represents its logical start time   .
- The timestamp can be either the system time or a logical counter that increments with each transaction .
- The timestamp ordering protocol ensures that any conflicting read and write operations are executed in timestamp order, meaning that older transactions get priority over newer ones   .
- The timestamp ordering protocol can be implemented using two methods: basic timestamp ordering and Thomas' write rule  .
- Basic timestamp ordering checks the timestamp of each transaction against the read timestamp (RTS) and write timestamp (WTS) of the data item it accesses, and rejects the operation if it violates the timestamp order  .
- Thomas' write rule is a variation of basic timestamp ordering that allows some write operations to be ignored instead of rejected, if they do not affect the final outcome of the schedule  .
- The advantages of timestamp ordering protocol are that it avoids deadlock, reduces locking overhead, and preserves causality among transactions  .
- The disadvantages of timestamp ordering protocol are that it may cause more aborts, waste resources, and suffer from the problem of starvation  .
- Time stamping protocols are suitable for applications that have low data contention and high read frequency .