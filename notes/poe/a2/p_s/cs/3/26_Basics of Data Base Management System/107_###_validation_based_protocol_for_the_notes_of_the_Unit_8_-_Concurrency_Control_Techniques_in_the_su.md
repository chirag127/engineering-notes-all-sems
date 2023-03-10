 Here is the content in markdown format for the given topic:

### Validation Based Protocol

This is a concurrency control protocol which ensures serializability of transactions using the technique of validation of read/write operations of transactions. The steps involved are:

1. When a transaction T1 wants to read an item x, it sends a validation request to the concurrency controller.
2. The concurrency controller checks if any other transaction T2 has updated x after T1 read x but before T2 committed. If no, then T1's read operation is allowed. Otherwise, T1's read operation is delayed until T2 either commits or aborts.
3. When a transaction T3 wants to update an item y, it sends a validation request to the concurrency controller.
4. The concurrency controller checks if any other transaction T4 has read y after T3 updated y but before T4 committed. If no, then T3's update operation is allowed. Otherwise, T3's update operation is delayed until T4 either commits or aborts.
5. Once a transaction completes its execution, it sends a commit request to the concurrency controller. The concurrency controller then checks for any validation or invalidation requests pending for the transaction. If none, the transaction is committed. Otherwise, the transaction is delayed until the pending requests are serviced.

Advantages:
- It ensures serializability and avoids cascading aborts.
- It is non-blocking as transactions are delayed only when validation/invalidation is required.

Disadvantages:
- The concurrency controller can become a bottleneck due to large number of validation requests.
- The protocol can lead to deadlocks due to circular waits.