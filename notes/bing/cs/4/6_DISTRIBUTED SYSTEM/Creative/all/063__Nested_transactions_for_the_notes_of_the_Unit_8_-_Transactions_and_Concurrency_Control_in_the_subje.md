### Nested transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A nested transaction is a transaction that consists of sub-transactions, each of which may have its own begin and end points.
- A nested transaction that accesses objects handled by different servers is referred to as a distributed nested transaction.
- Nested transactions allow for more concurrency and flexibility in distributed systems, as they can be committed or aborted independently of their parent transactions.
- Nested transactions can be classified into two types: **flat** and **hierarchical** .
  - A flat nested transaction has a single top-level transaction that can open sub-transactions at the same level, which run concurrently and independently .
  - A hierarchical nested transaction has a tree structure, where the top-level transaction can open sub-transactions at lower levels, which inherit some properties from their parent transactions .
- Nested transactions have different commit protocols depending on their type and level  .
  - A flat nested transaction can use the **two-phase commit protocol (2PC)**, which involves a coordinator and a set of participants that vote on whether to commit or abort the transaction.
  - A hierarchical nested transaction can use the **nested two-phase commit protocol (N2PC)**, which extends the 2PC protocol to handle multilevel transactions .
  - A hierarchical nested transaction can also use the **sagas protocol**, which allows partial commits and compensating actions for sub-transactions that cannot be committed .
- Nested transactions have some advantages and disadvantages in distributed systems  .
  - Advantages:
    - They increase the concurrency and parallelism of transactions, as sub-transactions can run independently and overlap with each other  .
    - They improve the fault tolerance and recovery of transactions, as sub-transactions can be committed or aborted separately, and compensating actions can be taken for failed sub-transactions  .
    - They support modularity and reusability of transactions, as sub-transactions can be defined as modules that can be invoked by different parent transactions  .
  - Disadvantages:
    - They increase the complexity and overhead of transaction management, as sub-transactions need to coordinate with their parent transactions and other sub-transactions, and different commit protocols need to be implemented  .
    - They may violate the serializability and consistency of transactions, as sub-transactions may conflict with each other or with other transactions, and partial commits may leave the system in an inconsistent state  .
    - They may reduce the performance and scalability of transactions, as sub-transactions may incur more communication and synchronization costs, and more resources may be locked by sub-transactions  .

- An example of a nested transaction in a distributed system is a travel booking transaction, which consists of sub-transactions for booking a flight, a hotel, and a car rental .
  - The travel booking transaction can be a flat nested transaction, where the sub-transactions run concurrently and independently, and use the 2PC protocol to commit or abort .
  - The travel booking transaction can also be a hierarchical nested transaction, where the sub-transactions run in a tree structure, and use the N2PC or sagas protocol to commit or abort .
  - A possible tree structure for the travel booking transaction is shown below:

```
    Travel booking transaction
    /          |            \
Flight booking  Hotel booking  Car rental booking
  /    \          /    \          /    \
Seat   Meal    Room   Service   Model   Insurance
```

- A possible mnemonic to remember the types of nested transactions is **F**lat **H**ierarchical **N**ested **T**ransactions (FHNT).
- A possible learning trick to understand the commit protocols for nested transactions is to use the analogy of a wedding ceremony, where the