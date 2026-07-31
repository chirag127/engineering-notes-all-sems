
### Transaction Recovery for the Notes of Unit 9 - Distributed Transactions in DISTRIBUTED SYSTEM

1. Transaction recovery is a process of recovering from system failures in distributed systems. 
2. It is the process of restoring the system to a consistent state after a failure. 
3. The goal of transaction recovery is to ensure that transactions that were in progress when a failure occurred are either completed or aborted. 
4. Transaction recovery is a complex process that requires coordination between the various components of the distributed system. 
5. Transaction recovery algorithms must ensure that the system is consistent after a failure, and that no transactions are lost or duplicated. 
6. The most common approach to transaction recovery is the two-phase commit protocol. 
7. In this protocol, a coordinator sends out a request to all participants to prepare for a transaction. 
8. If all participants are ready, the coordinator sends a commit message, and all participants commit the transaction. 
9. If any participant is not ready, the coordinator sends an abort message, and all participants abort the transaction. 
10. Other approaches to transaction recovery include the three-phase commit protocol, the distributed commit protocol, and the atomic broadcast protocol.