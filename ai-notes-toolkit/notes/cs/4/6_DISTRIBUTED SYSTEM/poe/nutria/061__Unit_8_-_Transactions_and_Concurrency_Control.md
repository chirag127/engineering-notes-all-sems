
## Unit 8 - Transactions and Concurrency Control

1. Transaction: A transaction is a unit of work that can be performed within a database management system (DBMS) against a database. It is a logical unit of work that includes one or more related data manipulation language (DML) operations.

2. ACID Properties: Transactions must have four properties (atomicity, consistency, isolation, and durability) in order to ensure data integrity and maintain the integrity of the database.

3. Atomicity: Atomicity requires that each transaction is "all or nothing". If one part of the transaction fails, the entire transaction fails and the database state is left unchanged.

4. Consistency: Consistency requires that all data must meet the defined rules of the database. This means that any data written to the database must be valid according to all defined rules, including any constraints, cascades, triggers, and any other rules defined on the database.

5. Isolation: Isolation requires that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially, i.e., one after the other.

6. Durability: Durability requires that once a transaction has been committed, it will remain so, even in the case of a system failure.

7. Concurrency Control: Concurrency control is a technique used to ensure that multiple transactions can execute concurrently without resulting in an inconsistent state in the database. It is used to ensure that data integrity is maintained in a multi-user environment.