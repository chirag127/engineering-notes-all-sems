## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failures can be classified into three types: crash failures, omission failures, and Byzantine failures.
- Crash failures occur when a process stops executing and does not resume. Omission failures occur when a process fails to send or receive a message. Byzantine failures occur when a process behaves arbitrarily or maliciously, such as sending incorrect or conflicting messages.
- Failure recovery techniques can be divided into two categories: backward recovery and forward recovery.
- Backward recovery involves undoing the effects of a failure and restoring the system to a previous consistent state. This can be achieved by using checkpoints, logging, and rollback protocols.
- Forward recovery involves correcting the effects of a failure and continuing the execution from the current state. This can be achieved by using redundancy, replication, and fault tolerance protocols.
- Checkpoints are snapshots of the system state that are periodically saved on stable storage. They can be used to restart the execution from a consistent point after a failure.
- Logging is the process of recording the events and actions that occur in the system. Logs can be used to replay or undo the events and actions after a failure.
- Rollback protocols are algorithms that coordinate the processes to restore a consistent state after a failure. They can be based on synchronous or asynchronous communication, and on pessimistic or optimistic assumptions.
- Redundancy is the provision of extra resources or components that can take over the functionality of a failed component. Redundancy can be static or dynamic, and can be applied at different levels of granularity.
- Replication is the creation and maintenance of multiple copies of the same data or service. Replication can improve availability, performance, and fault tolerance of the system.
- Fault tolerance protocols are algorithms that enable the system to tolerate a certain number of failures and continue to provide correct service. They can be based on consensus, voting, or quorum techniques.