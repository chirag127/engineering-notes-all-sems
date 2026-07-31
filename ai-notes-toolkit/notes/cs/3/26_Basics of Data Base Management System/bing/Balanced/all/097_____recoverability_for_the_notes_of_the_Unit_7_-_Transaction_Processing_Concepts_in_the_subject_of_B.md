# Recoverability

Recoverability is the ability of a database system to restore the database to a consistent state after a failure or an abort of a transaction. Recoverability is an important property for ensuring the integrity and consistency of the database.

Some key concepts related to recoverability are:

- **Transaction**: A transaction is a logical unit of work that consists of a sequence of operations on the database. A transaction has the following properties: atomicity, consistency, isolation, and durability (ACID).
- **Commit**: A commit is an operation that marks the successful completion of a transaction and makes its effects permanent in the database.
- **Abort**: An abort is an operation that marks the unsuccessful termination of a transaction and undoes its effects from the database.
- **Schedule**: A schedule is a sequence of operations from a set of transactions that reflects the chronological order of their execution.
- **Serial schedule**: A serial schedule is a schedule in which the operations of each transaction are executed consecutively without any interleaving with other transactions.
- **Concurrent schedule**: A concurrent schedule is a schedule in which the operations of different transactions are interleaved.
- **Conflict**: A conflict is a situation in which two operations from different transactions access the same data item and at least one of them is a write operation.
- **Conflict serializable schedule**: A conflict serializable schedule is a concurrent schedule that is equivalent to some serial schedule, where two schedules are equivalent if they produce the same final state of the database.
- **Recoverable schedule**: A recoverable schedule is a schedule in which, for each pair of transactions T<sub>i</sub> and T<sub>j</sub>, if T<sub>j</sub> reads a data item previously written by T<sub>i</sub>, then the commit operation of T<sub>i</sub> appears before the commit operation of T<sub>j</sub> in the schedule.
- **Cascading abort**: A cascading abort is a situation in which the abort of one transaction causes the abort of other transactions that have read data items written by the aborted transaction.
- **Cascadeless schedule**: A cascadeless schedule is a schedule in which, for each pair of transactions T<sub>i</sub> and T<sub>j</sub>, if T<sub>j</sub> reads a data item previously written by T<sub>i</sub>, then the commit operation of T<sub>i</sub> appears before the read operation of T<sub>j</sub> in the schedule.

Some examples of schedules and their recoverability are:

- Schedule 1: T<sub>1</sub>: R(A), W(A), C; T<sub>2</sub>: R(B), W(B), C
  - This is a serial schedule, and it is recoverable and cascadeless.
- Schedule 2: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(B), W(B), C; T<sub>1</sub>: C
  - This is a concurrent schedule, and it is conflict serializable, recoverable, and cascadeless.
- Schedule 3: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(A), W(A), C; T<sub>1</sub>: C
  - This is a concurrent schedule, and it is conflict serializable and recoverable, but not cascadeless, because T<sub>2</sub> reads A before T<sub>1</sub> commits.
- Schedule 4: T<sub>1</sub>: R(A), W(A); T<sub>2</sub>: R(A), W(A), C; T<sub>1</sub>: A
  - This is a concurrent schedule, and it is not conflict serializable, not recoverable, and not cascadeless, because T<sub>2</sub> commits before T<sub>1</sub>, and T<sub>1</sub> aborts, causing a cascading abort of T<sub>2</sub>.