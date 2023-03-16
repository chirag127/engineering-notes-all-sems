## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after one or more components fail.
- Failure recovery is important for ensuring the availability, reliability, and integrity of the distributed system and its data.
- Failure recovery can be classified into two types: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of the failed components and restoring the system to a previous consistent state, such as a checkpoint or a backup.
- Forward recovery involves correcting the errors caused by the failed components and continuing the execution from the current state, such as by using redundancy or replication.
- Backward recovery can be further divided into three techniques: checkpointing, logging, and rollback-recovery.
- Checkpointing is the process of periodically saving the state of the system or its components to a stable storage, such as a disk or a cloud.
- Logging is the process of recording the events or actions that occur in the system or its components to a stable storage, such as a disk or a cloud.
- Rollback-recovery is the process of restoring the system or its components to a previous checkpoint or a consistent log, and replaying the events or actions that occurred after the checkpoint or the log.
- Forward recovery can be further divided into two techniques: redundancy and replication.
- Redundancy is the process of having multiple copies or versions of the system or its components, such as hardware, software, or data, that can perform the same function or provide the same service.
- Replication is the process of maintaining multiple copies or replicas of the system or its data, such as files, databases, or objects, that are synchronized and consistent with each other.
- Redundancy and replication can be used to mask, tolerate, or resolve failures, depending on the level of consistency and availability required by the system or its applications.