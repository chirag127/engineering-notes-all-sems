### Two-Phase Commit Protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. It is a specialized type of consensus protocol.

The protocol achieves its goal even in many cases of temporary system failure (involving either process, network node, communication, etc. failures), and is thus widely used. However, it is not resilient to all possible failure configurations, and in rare cases, user (e.g., a system's administrator) intervention is needed to remedy an outcome.

The protocol uses a coordinator process to manage all the other processes (called cohorts) that participate in the transaction. The protocol assumes that there is stable storage at each node with a write-ahead log, that no node crashes forever, that the data in the write-ahead log is never lost or corrupted in a crash, and that any two nodes can communicate with each other.

The protocol is initiated by the coordinator after the last step of the transaction has been reached. The coordinator sends a message to all cohorts asking whether they are prepared to commit the transaction, and waits for a reply from all cohorts.

1. **Phase 1 (Voting phase)**: The coordinator sends a query to commit message to all cohorts and waits until it has received a reply from all cohorts.
    - If all cohorts reply with a "Yes" message, the coordinator will proceed to the second phase of the protocol.
    - If any cohort replies with a "No" message, or if the coordinator does not receive a reply from a cohort within a certain time frame, the coordinator will abort the transaction.

2. **Phase 2 (Commit phase)**: The coordinator sends a commit or abort message to all cohorts, depending on the result of the first phase.
    - If the coordinator decided to commit the transaction, it sends a commit message to all cohorts. Each cohort will then commit the transaction and release all the locks and resources held during the transaction.
    - If the coordinator decided to abort the transaction, it sends an abort message to all cohorts. Each cohort will then abort the transaction and release all the locks and resources held during the transaction.

The two-phase commit protocol is a simple and effective way to ensure the atomicity of distributed transactions. However, it has some limitations, such as the single point of failure of the coordinator and the blocking nature of the protocol, which can lead to reduced performance in some cases. There are other protocols, such as the three-phase commit protocol, that address some of these limitations.