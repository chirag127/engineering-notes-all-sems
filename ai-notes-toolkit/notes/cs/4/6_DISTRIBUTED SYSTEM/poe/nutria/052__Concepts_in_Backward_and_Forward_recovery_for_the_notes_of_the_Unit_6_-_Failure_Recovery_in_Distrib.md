
### Concepts in Backward and Forward Recovery for the Notes of Unit 6 - Failure Recovery in Distributed Systems

1. **Backward Recovery**: This process is used to restore a distributed system to its state before the failure occurred. It is also known as ‘rollback’ and is used to restore the system to a consistent state.

2. **Forward Recovery**: This process is used to restore the system to its state after the failure occurred. It is also known as ‘rollforward’ and is used to restore the system to a consistent state.

3. **Checkpointing**: Checkpointing is a process used to create a snapshot of the distributed system at a particular point in time. This snapshot can then be used for backward or forward recovery.

4. **Failure Detection**: This is the process of detecting failures in a distributed system. It is used to identify the source of the failure and to initiate the recovery process.

5. **Recovery Algorithms**: Recovery algorithms are used to recover from failures in a distributed system. These algorithms can be divided into two categories: synchronous and asynchronous. Synchronous algorithms are used to restore the system to its state before the failure while asynchronous algorithms are used to restore the system to its state after the failure.