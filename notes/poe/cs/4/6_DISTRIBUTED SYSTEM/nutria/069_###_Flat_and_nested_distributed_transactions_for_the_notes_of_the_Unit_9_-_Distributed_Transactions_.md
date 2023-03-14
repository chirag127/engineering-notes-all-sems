

### Flat and Nested Distributed Transactions for the Notes of the Unit 9 - Distributed Transactions in the Subject of DISTRIBUTED SYSTEM

* A distributed transaction is a transaction that involves multiple databases, which are located on different computers. 
* In a flat distributed transaction, all the databases involved in the transaction are updated in a single atomic unit. 
* A nested distributed transaction is a distributed transaction in which one or more databases are updated in separate atomic units. 
* Flat distributed transactions are simpler and more efficient than nested distributed transactions, as they require fewer resources and less coordination between databases.
* However, nested distributed transactions are more powerful and flexible, as they allow for more complex transactions and can handle more complicated scenarios.
* In order to ensure data consistency across multiple databases, distributed transactions must be properly coordinated. This is done using a two-phase commit protocol, which ensures that all databases involved in the transaction are updated in a consistent manner.
* Common use cases for distributed transactions include banking applications, online shopping, and airline reservations, among others. 
* Advantages of distributed transactions include increased data consistency, improved scalability, and better performance.
* Disadvantages of distributed transactions include increased complexity, increased overhead, and the possibility of data loss in case of failure. 
* In order to ensure data consistency and integrity, distributed transactions must be properly managed and monitored. 
* A good mnemonic for remembering the concept of distributed transactions is "2PC": two-phase commit.