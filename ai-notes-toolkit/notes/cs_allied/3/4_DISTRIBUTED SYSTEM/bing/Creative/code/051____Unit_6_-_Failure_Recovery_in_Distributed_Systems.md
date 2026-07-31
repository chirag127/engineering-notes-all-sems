## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and arbitrary failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Arbitrary failures occur when a process behaves in an unpredictable or malicious way.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be achieved by using checkpoints, logging, and rollback.
- Checkpoints are snapshots of the system state taken periodically or on demand. Logging is the recording of events or actions that occur in the system. Rollback is the process of restoring the system state to a checkpoint or a log entry.
- Forward recovery involves correcting the effects of a failure and continuing the system execution from the current state. This can be achieved by using redundancy, replication, and fault tolerance.
- Redundancy is the provision of extra resources or components that can take over the function of a failed one. Replication is the creation of multiple copies of data or processes that can be accessed in case of a failure. Fault tolerance is the ability of the system to continue functioning correctly despite the presence of failures.