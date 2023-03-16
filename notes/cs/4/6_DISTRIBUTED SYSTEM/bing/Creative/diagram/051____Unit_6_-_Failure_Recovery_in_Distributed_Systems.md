## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and arbitrary failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Arbitrary failures occur when a process behaves in an unpredictable or malicious way.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be done using checkpoints, logging, or rollback-recovery protocols.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state. This can be done using redundancy, replication, or fault-tolerance protocols.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage. They can be used to restart the system from a consistent state after a failure.
- Logging is the technique of recording the events or actions that occur in the system on stable storage. They can be used to replay or undo the events or actions after a failure.
- Rollback-recovery protocols are algorithms that coordinate the processes to roll back to a consistent state after a failure. They can be based on message logging, checkpointing, or both.
- Redundancy is the technique of having multiple copies or versions of the same data or service. They can be used to mask or tolerate failures by switching to an alternative copy or version.
- Replication is the technique of maintaining multiple copies of the same data or service on different processes or nodes. They can be used to improve availability, reliability, and performance of the system.
- Fault-tolerance protocols are algorithms that ensure the system can continue to function correctly despite the presence of failures. They can be based on consensus, voting, or quorum.