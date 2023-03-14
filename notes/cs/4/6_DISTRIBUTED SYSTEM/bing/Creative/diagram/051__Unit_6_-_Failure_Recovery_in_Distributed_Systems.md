## Unit 6 - Failure Recovery in Distributed Systems

The following diagram illustrates the basic architecture of a distributed system with four nodes (A, B, C, and D) and the possible failure scenarios and recovery mechanisms.

```
+-----+     +-----+     +-----+     +-----+
|     |     |     |     |     |     |     |
|  A  |-----|  B  |-----|  C  |-----|  D  |
|     |     |     |     |     |     |     |
+-----+     +-----+     +-----+     +-----+
```

- Node failure: A node may crash or become unreachable due to network partition or power outage. For example, if node B crashes, the system may lose some data or functionality that is hosted by node B. To recover from node failure, the system may use techniques such as checkpointing, replication, or logging to restore the state of the failed node or migrate it to another node. For example, if node B has a backup copy of its state on node C, then node C can take over the role of node B until node B recovers or is replaced.

- Link failure: A link may fail or become congested due to network problems or malicious attacks. For example, if the link between node B and node C fails, the system may lose some communication or coordination between these two nodes. To recover from link failure, the system may use techniques such as retransmission, routing, or timeout to resend or reroute the messages or detect the failure and take appropriate actions. For example, if node B and node C use a reliable IPC protocol, they can retransmit the messages or use an alternative link until the original link is restored.

- Process failure: A process may fail or behave incorrectly due to software bugs, hardware faults, or human errors. For example, if a process on node A fails, the system may lose some computation or service that is provided by that process. To recover from process failure, the system may use techniques such as exception handling, rollback, or restart to handle the errors, undo the effects, or restart the process. For example, if a process on node A uses a try-catch-finally block, it can catch the exceptions and execute the finally block to release the resources or notify other processes.