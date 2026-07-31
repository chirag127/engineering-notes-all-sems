## Unit 7 - Transaction Processing Concepts

1. **Transaction**: A transaction is a logical unit of work that represents real-world events of any business or commercial activity. It is a sequence of operations that are executed as a single unit.

2. **ACID Properties**: A transaction must follow the ACID properties, which stands for Atomicity, Consistency, Isolation, and Durability. These properties ensure the reliability of the transaction processing system.

3. **Atomicity**: Atomicity ensures that either all the operations of a transaction are completed or none of them are. If any operation fails, the entire transaction is rolled back to its initial state.

4. **Consistency**: Consistency ensures that the database remains in a consistent state before and after the transaction. The transaction must follow the integrity constraints defined on the database.

5. **Isolation**: Isolation ensures that the concurrent execution of transactions does not affect their outcome. Each transaction must be executed in isolation from other transactions.

6. **Durability**: Durability ensures that once a transaction is committed, its effects are permanent and can survive any subsequent failures.

7. **Transaction Processing System**: A transaction processing system is a system that is responsible for managing the execution of transactions. It ensures that the ACID properties are followed and the database remains in a consistent state.

8. **Transaction Management**: Transaction management involves the coordination of transactions, ensuring their correct execution, and handling any conflicts that may arise.

9. **Concurrency Control**: Concurrency control is the process of managing the simultaneous execution of transactions in a multi-user environment. It ensures that the transactions are executed in a way that maintains the consistency of the database.

10. **Recovery Management**: Recovery management is the process of restoring the database to a consistent state in the event of a failure. It involves undoing the effects of incomplete transactions and redoing the effects of committed transactions.