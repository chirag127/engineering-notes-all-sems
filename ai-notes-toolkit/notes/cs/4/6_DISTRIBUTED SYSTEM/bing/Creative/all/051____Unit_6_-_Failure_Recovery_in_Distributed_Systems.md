## Unit 6 - Failure Recovery in Distributed Systems

- In distributed systems, failures are inevitable and can affect the availability, consistency, and performance of the system.
- Failure recovery is the process of restoring the system to a correct and consistent state after a failure occurs.
- Failure recovery techniques can be classified into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be done by using checkpoints, logging, or rollback.
- Checkpoints are snapshots of the system state taken periodically and stored in stable storage. They can be used to restart the system from a known good state after a failure.
- Logging is the recording of system events and actions in a persistent log. The log can be used to replay or undo the events and actions after a failure.
- Rollback is the process of undoing the effects of a failure by restoring the system state to a previous checkpoint or a consistent point in the log.
- Forward recovery involves masking or tolerating the effects of a failure and continuing the system execution from the current state. This can be done by using redundancy, replication, or fault tolerance.
- Redundancy is the provision of extra resources or components in the system that can take over the functionality of a failed component.
- Replication is the creation and maintenance of multiple copies of the same data or service in the system. Replication can improve availability, consistency, and performance of the system.
- Fault tolerance is the ability of the system to continue functioning correctly in the presence of failures. Fault tolerance can be achieved by using techniques such as consensus, voting, or quorum.