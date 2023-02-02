### Distributed deadlocks for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM
Distributed Deadlocks:
- Occur when multiple transactions executing concurrently in a distributed system are blocked waiting for resources held by other transactions.
- Can arise due to communication delays, process crashes, and other factors.
- Detection and resolution methods: 
  1. Centralized detection: a designated process periodically checks for deadlocks. 
  2. Distributed detection: each process periodically checks for deadlocks and communicates with other processes. 
  3. Prevention: design transactions to avoid conflicting access to resources. 
  4. Recovery: abort one or more transactions to release resources.
