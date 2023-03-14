### Recovery in Concurrent systems for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

In distributed systems, concurrent execution of processes is common, which can lead to failures. Therefore, recovery mechanisms are necessary to ensure the system's availability and reliability. Recovery in concurrent systems is an essential aspect of distributed systems that involves restoring the system to a consistent state after a failure.

Here are some important points to keep in mind while studying the recovery in concurrent systems in the context of distributed systems:

1. Failure types: There are two types of failures in distributed systems: transient and permanent. Transient failures are temporary and can be recovered by retrying the operation, whereas permanent failures are permanent and require a recovery mechanism.

2. Recovery techniques: There are two main recovery techniques used in concurrent systems: checkpointing and message logging. Checkpointing involves taking a snapshot of the system's state at a particular point in time and saving it to secondary storage. If a failure occurs, the system can be restored to the last consistent checkpoint. Message logging involves recording all the messages exchanged between processes in a log file. If a failure occurs, the system can replay the log file to restore the system's state.

3. Recovery time: The recovery time in concurrent systems depends on the amount of data that needs to be recovered and the recovery technique used. Checkpointing is faster than message logging, but it requires more storage space.

4. Consistency: The recovery mechanism should ensure that the system is restored to a consistent state. In other words, the system should not be left in an inconsistent state after a failure.

5. Rollback recovery: Rollback recovery is a recovery mechanism that involves rolling back the system to a previous consistent state and replaying the operations from that point onward. This mechanism is used when the system cannot be restored to the last consistent checkpoint.

6. Forward recovery: Forward recovery is a recovery mechanism that involves continuing the operation from the point of failure without rolling back the system. This mechanism is used when rolling back is not feasible or when the system cannot tolerate the downtime required for rollback recovery.

Mnemonics and learning tricks can be helpful in remembering the different recovery techniques and their advantages and disadvantages. For example, the acronym "CASH" can be used to remember the advantages of checkpointing: Consistency, Availability, Space-efficiency, and High-speed recovery. Similarly, the acronym "LOG" can be used to remember the advantages of message logging: Low space requirement, Ordering of events, and Guaranteed recovery.

In conclusion, recovery in concurrent systems is an important aspect of distributed systems that ensures the system's availability and reliability. Understanding the different recovery techniques and their advantages and disadvantages is crucial for designing and implementing robust distributed systems.