## Unit 4 - Transaction Processing Concept

Transaction processing is a type of computer processing that takes place in a system that supports transaction-oriented applications. A transaction is a logical unit of work that must be either completed in its entirety or completely undone. The key properties of a transaction are atomicity, consistency, isolation, and durability (ACID).

1. **Atomicity:** This property ensures that either all the changes made during a transaction are committed to the database or none of them are. If a transaction fails at any point, all changes made during the transaction are rolled back to their previous state.

2. **Consistency:** This property ensures that the database remains in a consistent state before and after the transaction. The transaction must follow all the rules and constraints defined in the database.

3. **Isolation:** This property ensures that each transaction is executed independently of other transactions. The changes made by one transaction are not visible to other transactions until the first transaction is committed.

4. **Durability:** This property ensures that once a transaction is committed, the changes made by the transaction are permanent and will survive any subsequent failures.

Transaction processing systems are designed to handle a large number of transactions efficiently and reliably. They are commonly used in applications such as banking systems, airline reservation systems, and e-commerce systems.