
### Detection & Resolution for the Notes of the Unit 3 - Distributed Deadlock Detection in the Subject of DISTRIBUTED SYSTEM

1. Detection: 
    - Distributed deadlock detection is the process of detecting deadlocks in a distributed system. 
    - In distributed systems, deadlocks can arise due to the lack of coordination between multiple processes or nodes. 
    - To detect deadlocks, each node in the system needs to maintain information about the resources held by all other nodes. 
    - This information can be gathered from periodic messages sent between the nodes. 
    - Once the information is gathered, a deadlock can be detected by checking for a cycle in the resource graph. 
    - If a cycle is found, then a deadlock has occurred.

2. Resolution: 
    - Once a deadlock is detected, it must be resolved in order to restore the system to a working state. 
    - The most common way to resolve a deadlock is to preempt one of the processes involved in the deadlock. 
    - This process is known as the victim process and it is terminated, allowing the other processes to continue. 
    - Another way to resolve a deadlock is to rollback some of the transactions involved in the deadlock. 
    - This requires the system to be able to undo some of the changes that were made by the transactions. 
    - Finally, deadlocks can also be resolved by changing the order in which resources are requested. 
    - This requires careful design of the algorithms used by the processes in the system.