 Here is the content in markdown format for the topic -

### Locking Techniques for Concurrency Control

Locking is a synchronization technique used to prevent incompatible concurrent access to shared data. The main types of locks are:

- Shared (read) lock: Used for read-only access to a data item. Multiple transactions can hold a shared lock on the same item simultaneously.
- Exclusive (write) lock: Used for read-write access to a data item. Only one transaction can hold an exclusive lock on a data item at a time.

#### Two-phase locking

1. **Growing phase**: Transactions can acquire locks.
2. **Shrinking phase**: Transactions can release locks.

Constraints:

- Locks can only be acquired in the growing phase, not released.
- A transaction must hold all its locks until it completes.

This ensures serializability and avoids deadlocks.

#### Deadlocks

- Occur when two or more transactions are waiting for locks held by each other.
- Can be detected and resolved by:
    - Timeout: Abort one of the deadlocked transactions.
    - Resource ordering: Impose a total ordering on all resources and require that transactions lock resources in this order.

Advantages: Prevents lost updates and ensures consistency.
Disadvantages: Reduces concurrency as only one transaction can access data at a time.

[Diagrams and examples can be added here to help understand the concepts better.]

Applications: Widely used in database systems to provide concurrency control.