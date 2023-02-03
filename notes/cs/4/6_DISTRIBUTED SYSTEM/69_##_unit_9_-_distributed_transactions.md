## Unit 9 - Distributed Transactions
Distributed transactions refer to a series of database transactions that occur across multiple systems. They ensure that all transactions are committed or rolled back as a single unit of work. This helps to maintain data consistency and integrity across multiple systems. Key components of distributed transactions include: 

1. Transaction Manager: Coordinates the execution of transactions across multiple systems. 

2. Resource Manager: Manages access to shared resources, such as databases or message queues. 

3. Two-Phase Commit Protocol: Ensures that all participants in a transaction agree on the outcome of the transaction. 

4. XA Standard: Defines a common interface for transaction managers and resource managers to communicate with each other. 

Distributed transactions are typically used in situations where multiple systems need to access shared resources and coordinate their actions. For example, a bank might use distributed transactions to ensure that a customer's account balance is updated correctly across multiple systems, such as a database and a message queue.
