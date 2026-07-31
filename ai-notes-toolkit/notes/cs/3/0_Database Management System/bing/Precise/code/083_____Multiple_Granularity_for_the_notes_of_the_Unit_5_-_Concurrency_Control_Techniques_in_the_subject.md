### Multiple Granularity

Multiple granularity refers to the ability to lock data at different levels of granularity. In the context of a database management system, this means that locks can be placed on individual data items, sets of data items, or entire tables.

1. **Locking at different levels of granularity:** Locking at different levels of granularity allows for more flexible and efficient concurrency control. For example, if a transaction only needs to access a small subset of data within a table, it can place a lock on just that subset of data, rather than locking the entire table.

2. **Lock compatibility matrix:** A lock compatibility matrix is used to determine whether two transactions can hold locks on the same data item at the same time. The matrix specifies which types of locks are compatible with each other. For example, a shared lock and an exclusive lock are not compatible, meaning that two transactions cannot hold these types of locks on the same data item at the same time.

3. **Lock escalation:** Lock escalation is the process of converting a large number of fine-grained locks into a smaller number of coarse-grained locks. This can help to reduce the overhead associated with managing a large number of locks.

4. **Intention locks:** Intention locks are used to indicate that a transaction intends to acquire a lock on a data item at a lower level of granularity. For example, a transaction may place an intention lock on a table to indicate that it intends to acquire a lock on a specific row within that table.

5. **Multiple granularity locking protocol:** A multiple granularity locking protocol is a set of rules that govern how locks can be acquired and released at different levels of granularity. The protocol ensures that transactions do not interfere with each other and that data consistency is maintained.
