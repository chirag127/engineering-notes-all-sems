 Here is the content in markdown format without any emojis or external links as per your instructions:

### Distributed deadlocks for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed deadlock occurs when two or more transactions hold resources and each is waiting for the other to release resources. This results in both transactions being unable to proceed, leading to a deadlock.
- For example, Transaction 1 locks resource A and waits for resource B. Transaction 2 locks resource B and waits for resource A. This results in a deadlock as both transactions wait forever.
- To handle distributed deadlocks, one of the following techniques can be used:
- Deadlock avoidance: Prevents deadlocks by denying operations that may lead to deadlocks
- Deadlock detection and recovery: Allows deadlocks to occur but detects and recovers from them
- Timeouts: Transactions are aborted if they do not complete within a specified time period
- The deadlock problem is more difficult to solve in distributed systems compared to centralized systems due to the following reasons:
- Lack of global system state: No single entity has complete information about resource allocation across all nodes in the system, which makes it difficult to detect deadlocks.
- Resource allocation cycles: Cyclic resource allocation dependencies can span multiple nodes, which makes them harder to detect.
- The above points are key notes on the topic of distributed deadlocks which occurs in distributed systems handling distributed transactions requiring access to shared resources. The points can be reviewed as study material to learn and understand the concept in detail.