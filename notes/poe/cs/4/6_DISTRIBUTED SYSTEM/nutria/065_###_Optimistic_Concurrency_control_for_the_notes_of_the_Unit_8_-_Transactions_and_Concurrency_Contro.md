
### Optimistic Concurrency Control for the Notes of the Unit 8 - Transactions and Concurrency Control in the Subject of DISTRIBUTED SYSTEM
Optimistic concurrency control is an approach to managing concurrency control in distributed systems. The primary goal of this approach is to provide a high level of concurrency while still ensuring the correctness of transactions.

**Mnemonic**: OCC (Optimistic Concurrency Control)

Optimistic concurrency control works by allowing multiple transactions to be executed concurrently, but it does so without locking any of the data being accessed by the transactions. Instead, the system checks for conflicts between transactions at the end of each transaction. If any conflicts are detected, the conflicting transactions are rolled back and restarted.

**Advantages**
- High concurrency: Optimistic concurrency control allows for a high level of concurrency, since transactions do not need to wait for locks to be released.
- Low overhead: Since no locks are used, there is no need to maintain a lock table, which reduces the overhead of the system.

**Disadvantages**
- Increased complexity: Since the system must detect conflicts between transactions at the end of each transaction, the system is more complex than systems that use locks.
- Increased latency: The system must wait until the end of each transaction to detect conflicts, which can increase latency.

**Examples**
- Online shopping: Optimistic concurrency control can be used in online shopping systems to ensure that multiple customers can access the same item at the same time, but that only one customer can purchase the item.
- Stock trading: Optimistic concurrency control can be used in stock trading systems to ensure that multiple traders can access the same stock at the same time, but that only one trader can purchase the stock.

**Applications**
- Optimistic concurrency control can be used in any system that requires high concurrency and low overhead, such as online shopping systems, stock trading systems, and distributed databases.