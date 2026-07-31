### Timestamp ordering for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Timestamp ordering is a class of concurrency control protocols that use timestamps to determine the serializability order of transactions in a distributed system .
- A timestamp is a monotonically increasing number that is often based on the system clock or a logical clock .
- A transaction is assigned a timestamp when it starts, and this timestamp is used to order the transactions and resolve conflicts .
- There are two types of timestamp ordering protocols: basic timestamp ordering and optimistic timestamp ordering .
- Basic timestamp ordering protocol uses two timestamps for each data item: read timestamp (RTS) and write timestamp (WTS). RTS is the largest timestamp of any transaction that has successfully read the data item. WTS is the largest timestamp of any transaction that has successfully written the data item .
- Basic timestamp ordering protocol enforces two rules: read-write rule and write-write rule. Read-write rule states that a transaction T can read a data item X only if T's timestamp is greater than or equal to X's WTS. Write-write rule states that a transaction T can write a data item X only if T's timestamp is greater than both X's RTS and X's WTS .
- If a transaction T violates either of the rules, it is aborted and restarted with a new timestamp .
- Basic timestamp ordering protocol ensures conflict serializability, but it may cause cascading aborts, where aborting one transaction causes other transactions to abort as well .
- Optimistic timestamp ordering protocol avoids cascading aborts by using three phases for each transaction: read phase, validation phase, and write phase .
- In the read phase, a transaction T reads the data items from the database and stores them in a private workspace. T is not allowed to write any data item to the database in this phase .
- In the validation phase, a transaction T checks whether it can commit without violating serializability. T is assigned a validation timestamp (VTS) when it enters this phase. T compares its VTS with the RTS and WTS of the data items it has read or written. T can commit only if it satisfies the following conditions :
  - For each data item X that T has read, T's VTS must be greater than or equal to X's WTS.
  - For each data item X that T has written, T's VTS must be greater than X's RTS and X's WTS.
- If T fails to satisfy either of the conditions, it is aborted and restarted with a new timestamp .
- In the write phase, a transaction T writes the data items from its private workspace to the database. T is assigned a commit timestamp (CTS) when it enters this phase. T updates the RTS and WTS of the data items it has written with its CTS .
- Optimistic timestamp ordering protocol ensures conflict serializability and avoids cascading aborts, but it may cause more aborts than basic timestamp ordering protocol, especially when the system is highly concurrent .