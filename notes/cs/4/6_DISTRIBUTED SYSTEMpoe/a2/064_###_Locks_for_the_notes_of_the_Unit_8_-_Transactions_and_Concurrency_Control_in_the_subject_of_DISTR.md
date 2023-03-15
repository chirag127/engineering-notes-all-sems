 Here is the content in markdown format:

### Locks for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Locks are mechanisms used to enforce concurrency control in distributed systems and ensure data consistency. Some key points about locks are:

- They allow only one transaction to access a data item at a time. This prevents dirty reads and inconsistent updates.
- Locks can be shared or exclusive:
    - Shared locks: Multiple transactions can read a data item simultaneously but cannot write to it. Used for read-only access.
    - Exclusive locks: Only one transaction can access a data item. Used for write access.
- Locks can be granted immediately or after a delay:
    - Immediate locks: Transaction waits if a lock is not available. can lead to deadlocks.
    - Delayed locks: Transaction waits for a random amount of time if a lock is not available. Reduces deadlocks but can lead to starvation.
- Locks can be released manually by transactions or automatically after a transaction completes. Automatic release avoids manual unlocking errors.
- Deadlocks can occur if two transactions hold locks on data items the other transaction needs and waits indefinitely for the locks. Deadlock detection and resolution techniques are required to handle them.

Some mnemonics for remembering types of locks:

- Exclusive locks: "X" marks the spot! Only one transaction can access.
- Shared locks: Share and share alike! Multiple readers can access.

Advantages of locks:

- Simplicity: Easy to implement.
- Understandability: Concept is straightforward.

Disadvantages of locks:

- Deadlocks: As discussed, deadlocks can occur if not handled.
- Starvation: Delayed lock requests can lead to some transactions not getting CPU cycles.
- Performance: There is overhead in requesting, granting, and releasing locks. The more granular the locks, the higher the overhead.

Locks are a key concurrency control technique with several trade-offs to consider. Proper use cases and deadlock handling mechanisms can make them effective in coordinating distributed transactions.