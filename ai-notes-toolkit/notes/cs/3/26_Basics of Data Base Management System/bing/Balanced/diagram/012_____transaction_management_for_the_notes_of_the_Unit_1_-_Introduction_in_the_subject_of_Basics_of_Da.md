### Transaction Management

Transaction management is a logical unit of processing in a DBMS which entails one or more database access operations. It is a transaction is a program unit whose execution may or may not change the contents of a database. Not managing concurrent access may create issues like hardware failure and system crashes.

Some of the topics covered in this unit are:

- Transaction states
- Transaction properties
- Transaction log
- Concurrency control
- Locking mechanisms
- Deadlocks
- Serializability
- Recovery techniques

#### Transaction states

A transaction can be in one of the following states:

- Active state: This is the state in which the transaction is executing and performing database operations.
- Partially committed state: This is the state in which the transaction has completed its execution but the changes are not yet written to the database.
- Committed state: This is the state in which the transaction has completed its execution and the changes are written to the database.
- Failed state: This is the state in which the transaction encounters an error or aborts due to some reason and cannot continue its execution.
- Aborted state: This is the state in which the transaction is rolled back and the database is restored to its previous consistent state.

#### Transaction properties

A transaction must satisfy four properties, known as ACID properties, to ensure the consistency and reliability of the database:

- Atomicity: This property ensures that either all the operations of a transaction are executed or none of them are. A transaction is treated as a single unit of work and cannot be divided into parts.
- Consistency: This property ensures that a transaction transforms the database from one consistent state to another consistent state. A transaction must follow the integrity constraints and rules of the database.
- Isolation: This property ensures that a transaction is executed independently of other transactions and does not interfere with them. A transaction must not see the intermediate results of other transactions.
- Durability: This property ensures that the changes made by a transaction are permanent and persist even in the case of system failures. A transaction must not lose its effects due to power outages, crashes, or errors.

#### Transaction log

A transaction log is a file that records all the transactions and the database modifications made by each transaction. The transaction log is a critical component of the database. If there is a system failure, the transaction log can be used to bring the database back to a consistent state.

The transaction log contains the following information for each transaction:

- The transaction ID
- The start time and end time of the transaction
- The operations performed by the transaction
- The data values before and after the operations
- The commit or abort status of the transaction

#### Concurrency control

Concurrency control is the process of managing the simultaneous execution of multiple transactions in a database. Concurrency control is necessary to ensure the isolation and consistency properties of transactions.

Concurrency control can be achieved by using various techniques, such as:

- Locking mechanisms: These are methods of granting exclusive or shared access to data items or resources to different transactions. Locking mechanisms prevent unauthorized or conflicting updates to the database.
- Timestamp ordering: These are methods of assigning a unique timestamp to each transaction and ordering the transactions based on their timestamps. Timestamp ordering ensures that the transactions are executed in a chronological order and avoid conflicts.
- Validation techniques: These are methods of validating the transactions before committing them to the database. Validation techniques check whether the transactions have violated any consistency or isolation rules and abort them if necessary.
- Multiversion concurrency control: These are methods of maintaining multiple versions of the same data item in the database and allowing transactions to access the appropriate version based on their timestamps. Multiversion concurrency control reduces the need for locking and increases the concurrency level.

#### Locking mechanisms

Locking mechanisms are one of the most common techniques of concurrency control. Locking mechanisms use locks to grant or deny access to data items or resources to different transactions. Locks can be of two types:

- Binary locks: These are locks that have only two states: locked or unlocked. A binary lock can be acquired by only one transaction at a time and prevents any other transaction from accessing the locked data item or resource.
- Shared/exclusive locks: These are locks that have three states: unlocked, shared, or exclusive. A shared lock can be acquired by multiple transactions at the same time and allows read-only access to the locked data item or resource. An exclusive lock can be acquired by only one transaction at a time and allows read-write access to the locked data item or resource.

Locking mechanisms can also be classified