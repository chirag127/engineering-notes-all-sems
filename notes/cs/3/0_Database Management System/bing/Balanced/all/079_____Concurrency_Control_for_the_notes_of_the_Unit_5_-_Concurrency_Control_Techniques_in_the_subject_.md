# Concurrency Control

Concurrency control is a database management systems (DBMS) concept that is used to address the problems that occur with a multi-user system. Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity of the respective databases .

Concurrency control in DBMS is a procedure of managing simultaneous operations without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database.

The advantages of a concurrent system are:

- Waiting Time: It means if a process is in a ready state but still the process does not get the system to get execute is called waiting time. Concurrency reduces the waiting time of processes.
- CPU Utilization: It means how much CPU is busy in executing processes. Concurrency increases the CPU utilization by allowing multiple processes to use the CPU.
- Throughput: It means how many processes are completed in a unit time. Concurrency increases the throughput by increasing the number of transactions that can be processed in a given time.

The challenges of a concurrent system are:

- Lost Update: It occurs when two transactions that access the same database items have their operations interleaved in a way that makes the value of some database item incorrect.
- Uncommitted Dependency: It occurs when a transaction reads a data item that has been written by another transaction that has not yet committed, and then the second transaction aborts, leaving the first transaction with an incorrect value.
- Inconsistent Analysis: It occurs when a transaction reads several data items and performs some analysis based on their values, but another transaction updates some of these data items in between, making the analysis invalid.
- Deadlock: It occurs when two or more transactions are waiting for each other to release the locks they hold on the data items, resulting in a circular wait.

The methods of concurrency control in DBMS are:

- Lock-Based Protocols: These protocols use locks to prevent multiple transactions from accessing the same data item concurrently. Locks can be shared or exclusive, and can be granted or denied by a lock manager. Lock-based protocols ensure serializability, but may cause deadlocks.
- Timestamp-Based Protocols: These protocols use timestamps to order the transactions and determine their precedence. Each transaction is assigned a unique timestamp when it starts, and each data item has a read timestamp and a write timestamp to record the last transaction that read or wrote it. Timestamp-based protocols ensure serializability and avoid deadlocks, but may cause more aborts.
- Validation-Based Protocols: These protocols use a validation phase to check whether the transactions can be serialized based on their read and write sets. Each transaction is divided into three phases: read phase, validation phase, and write phase. Validation-based protocols ensure serializability and avoid deadlocks, but may cause more delays.