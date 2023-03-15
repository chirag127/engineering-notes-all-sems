# Validation Based Protocol

Validation based protocol is a concurrency control technique used in database management systems. It is also known as optimistic concurrency control. This technique is used to ensure the serializability of transactions in a database.

Here are some key points to remember about validation based protocol:

1. In validation based protocol, transactions are allowed to execute concurrently without any locking.
2. Each transaction is validated before it is committed to ensure that it does not conflict with other transactions.
3. If a transaction is found to be in conflict with another transaction, it is rolled back and restarted.
4. Validation based protocol is best suited for environments where conflicts between transactions are rare.
5. This technique can improve the performance of a database system by reducing the overhead of locking.
