# Multi-version Schemes for Concurrency Control

- Multi-version concurrency control (MVCC) is a technique that allows concurrent access to the database without locking the data.
- MVCC creates multiple versions of each data item and assigns them version numbers.
- Each transaction reads the most recent version of the data item that is compatible with its timestamp.
- Each transaction writes a new version of the data item with an incremented version number.
- MVCC avoids conflicts between read and write operations, as well as between write and write operations.
- MVCC improves the performance and scalability of database applications in a multi-user environment.

## Example of MVCC

- Suppose there are two transactions, T1 and T2, that operate on a data item X.
- Initially, X has a value of 10 and a version number of 1.
- T1 starts at time 1 and reads X. It gets the value 10 and the version number 1.
- T2 starts at time 2 and writes X. It creates a new version of X with a value of 20 and a version number of 2.
- T1 continues and writes X. It creates another new version of X with a value of 30 and a version number of 3.
- T2 reads X. It gets the value 20 and the version number 2, which is the most recent version compatible with its timestamp.
- T1 commits at time 3 and T2 commits at time 4.
- The final state of X is 30 with a version number of 3. The older versions of X are either deleted or archived.