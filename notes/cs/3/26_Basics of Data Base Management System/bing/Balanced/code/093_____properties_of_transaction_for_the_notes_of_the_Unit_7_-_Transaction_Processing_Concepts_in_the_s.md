### Properties of Transaction

A transaction is a logical unit of work that represents a real-world event in a database system. A transaction must satisfy four properties, known as ACID properties, to ensure the consistency and reliability of the database. These properties are:

- **Atomicity**: This property ensures that either all the operations of a transaction are executed successfully, or none of them are executed at all. If a transaction fails at any point, the database is restored to its original state before the transaction started. This property is also called the all-or-nothing property.

- **Consistency**: This property ensures that a transaction transforms the database from one consistent state to another consistent state. A consistent state is one that satisfies all the integrity constraints and business rules of the database. A transaction must not violate any of these rules during its execution.

- **Isolation**: This property ensures that a transaction is executed independently of other concurrent transactions. The intermediate results of a transaction are not visible to other transactions, and the effects of other transactions are not visible to the current transaction. This property is also called the serializability property.

- **Durability**: This property ensures that once a transaction commits, its effects are permanent in the database. The changes made by a transaction are not lost even in the case of system failures, such as power outages, crashes, or restarts. This property is also called the persistence property.