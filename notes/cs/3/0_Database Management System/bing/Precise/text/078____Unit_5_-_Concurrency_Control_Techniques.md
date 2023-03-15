## Unit 5 - Concurrency Control Techniques

Concurrency control is the process of managing simultaneous operations on a database without having them interfere with one another. There are several techniques used to achieve concurrency control, including:

1. **Locking**: This technique involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously. Locks can be shared or exclusive, and can be placed on individual data items or entire tables.

2. **Timestamp ordering**: This technique assigns a unique timestamp to each transaction, and transactions are executed in timestamp order. If a transaction tries to access data that has been modified by a later transaction, it is rolled back and restarted with a new timestamp.

3. **Optimistic concurrency control**: This technique assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Before committing, a transaction checks to see if any conflicts have occurred. If a conflict is detected, the transaction is rolled back and restarted.

4. **Multiversion concurrency control**: This technique maintains multiple versions of data items, allowing transactions to access older versions of data if the current version is locked. This can increase concurrency by allowing transactions to continue executing even if another transaction has locked the data they need.

These are some of the main techniques used to achieve concurrency control in database systems. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the system.