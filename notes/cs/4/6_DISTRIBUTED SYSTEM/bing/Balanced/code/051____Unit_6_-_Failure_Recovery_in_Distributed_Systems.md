## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after one or more components fail.
- Failure recovery is important for ensuring the availability, reliability, and correctness of distributed systems.
- Failure recovery can be classified into two types: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of erroneous or incomplete actions and restoring the system to a previous consistent state.
- Forward recovery involves correcting or compensating for the errors and continuing the execution from the current state.
- Backward recovery can be implemented using techniques such as checkpoints, logging, rollback, and replay.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage.
- Logging is the recording of the actions or events that occur in the system on stable storage.
- Rollback is the process of restoring the system state to a previous checkpoint.
- Replay is the process of re-executing the actions or events that occurred after the checkpoint.
- Forward recovery can be implemented using techniques such as redundancy, replication, voting, and exception handling.
- Redundancy is the provision of extra resources or components that can take over the functionality of the failed ones.
- Replication is the creation of multiple copies of the same data or service that can be accessed by different components.
- Voting is the mechanism of reaching a consensus among the replicas or components on the correct value or action.
- Exception handling is the mechanism of detecting, reporting, and handling the errors or failures that occur in the system.