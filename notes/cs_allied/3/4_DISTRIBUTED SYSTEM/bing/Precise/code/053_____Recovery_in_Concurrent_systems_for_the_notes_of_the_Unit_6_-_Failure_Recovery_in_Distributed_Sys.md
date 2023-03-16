### Recovery in Concurrent Systems

Recovery in concurrent systems is an important aspect of failure recovery in distributed systems. Here are some key points to consider:

1. **Concurrency control** is necessary to ensure that multiple processes can access shared data and resources without interfering with each other.

2. **Failure recovery** involves restoring the system to a consistent state after a failure has occurred.

3. **Checkpointing** is a technique used to save the state of the system at regular intervals, so that in the event of a failure, the system can be restored to the most recent checkpoint.

4. **Logging** is another technique used to record changes to the system, so that in the event of a failure, the system can be restored by replaying the log.

5. **Two-phase commit** is a protocol used to ensure that all participants in a distributed transaction agree to commit or abort the transaction.

6. **Distributed commit** is a more general form of two-phase commit, where multiple participants can be involved in the commit process.

7. **Recovery-oriented computing** is an approach to designing systems that focuses on rapid recovery from failures, rather than trying to prevent failures from occurring.

These are some of the key concepts to consider when studying recovery in concurrent systems as part of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM. It is important to understand these concepts in order to effectively design and implement distributed systems that can recover from failures.