## Unit 6 - Failure Recovery in Distributed Systems

1. **Introduction:** In distributed systems, failure recovery is the process of restoring the system to a consistent state after a failure has occurred.
2. **Types of Failures:** Failures in distributed systems can be classified into three main categories: crash failures, omission failures, and Byzantine failures.
3. **Crash Failures:** A crash failure occurs when a node in the system stops functioning completely.
4. **Omission Failures:** An omission failure occurs when a node fails to send or receive messages.
5. **Byzantine Failures:** A Byzantine failure occurs when a node behaves arbitrarily, sending incorrect or conflicting information to other nodes.
6. **Failure Recovery Techniques:** There are several techniques for recovering from failures in distributed systems, including checkpointing, logging, and replication.
7. **Checkpointing:** Checkpointing involves periodically saving the state of the system to stable storage, so that the system can be restored to a consistent state in the event of a failure.
8. **Logging:** Logging involves recording all changes to the system in a log, so that the system can be restored to a consistent state by replaying the log in the event of a failure.
9. **Replication:** Replication involves maintaining multiple copies of the system state, so that if one copy fails, another copy can take over.
10. **Conclusion:** Failure recovery is an important aspect of distributed systems, and there are several techniques for recovering from failures, including checkpointing, logging, and replication. These techniques can help to ensure that the system remains consistent and available, even in the face of failures.