# Two-Phase Commit Protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. It is a specialized type of consensus protocol.

The protocol achieves its goal even in many cases of temporary system failure (involving either process, network node, communication, etc. failures), and is thus widely used. However, it is not resilient to all possible failure configurations, and in rare cases, user (e.g., a system's administrator) intervention is needed to remedy an outcome.

The protocol uses a coordinator process to manage all the other processes (called cohorts) that participate in the transaction. The protocol assumes that there is stable storage at each node with a write-ahead log, that no node crashes forever, that the data in the write-ahead log is never lost or corrupted in a crash, and that any two nodes can communicate with each other.

The protocol has two phases:

1. **Phase 1 (voting phase):** The coordinator sends a query to commit message to all cohorts and waits until it has received a reply from all cohorts.

2. **Phase 2 (commit phase):** Based on the votes, the coordinator decides whether to commit or abort the transaction. If the coordinator decides to commit, it sends a commit message to all the cohorts. If the coordinator decides to abort, it sends an abort message to all the cohorts.

The cohorts then follow the coordinator's decision and either commit or abort the transaction.

The two-phase commit protocol is a blocking protocol. If the coordinator fails permanently, some cohorts will never resolve their transactions: After a cohort has sent an agreement message to the coordinator, it will block until a commit or abort is received. If the coordinator is permanently down, the cohorts will block indefinitely. This is known as the "blocking problem" of the two-phase commit protocol.