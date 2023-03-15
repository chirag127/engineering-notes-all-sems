## Unit 7 - Transaction Processing Concepts

Transaction processing is a type of computer processing that takes place in the presence of a computer database. It is used to ensure that data is processed in a reliable and consistent manner. The following are some key concepts related to transaction processing:

1. **Atomicity**: This refers to the all-or-nothing nature of transactions. Either all the changes made during a transaction are committed to the database, or none of them are.

2. **Consistency**: This refers to the requirement that the database must remain in a consistent state before and after a transaction. This means that all data integrity constraints must be satisfied.

3. **Isolation**: This refers to the requirement that each transaction must be executed in isolation from other transactions. This means that the changes made by one transaction must not be visible to other transactions until the first transaction is committed.

4. **Durability**: This refers to the requirement that once a transaction is committed, its changes to the database must be permanent. This means that even in the event of a system failure, the changes made by the transaction must be recoverable.

These four properties are often referred to as the ACID properties of transaction processing. They are essential for ensuring the reliability and consistency of data in a database.