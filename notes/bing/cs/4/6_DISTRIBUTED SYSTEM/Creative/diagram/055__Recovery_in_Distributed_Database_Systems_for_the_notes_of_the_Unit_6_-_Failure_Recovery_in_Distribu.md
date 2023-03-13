Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure. A failure can be a soft failure, which affects only the main memory and causes inconsistency of the database, or a hard failure, which affects the disk storage and causes loss of data. Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site, and transactions can span multiple sites.

One of the common techniques for recovery in distributed database systems is the two-phase commit protocol, which ensures the atomicity of distributed transactions. The two-phase commit protocol involves a coordinator site and one or more participant sites. The coordinator site initiates the commit process by sending a prepare message to all the participant sites. Each participant site replies with a yes or no vote, depending on whether it is ready to commit or not. If the coordinator site receives a yes vote from all the participant sites, it sends a commit message to all of them. Otherwise, it sends an abort message to all of them. Each participant site then follows the coordinator's decision and either commits or aborts the transaction.

The following diagram illustrates the basic architecture of a two-phase commit protocol:

```
+----------------+             +----------------+
| Coordinator    |             | Participant    |
| Site           |             | Site           |
+----------------+             +----------------+
|                |             |                |
|                | prepare     |                |
|                |------------>|                |
|                |             |                |
|                |             |                |
|                |             | yes/no         |
|                |             |<---------------|
|                |             |                |
|                |             |                |
|                | commit/abort|                |
|                |------------>|                |
|                |             |                |
|                |             |                |
|                |             | ack            |
|                |             |<---------------|
|                |             |                |
+----------------+             +----------------+
```

The two-phase commit protocol has some drawbacks, such as blocking, which occurs when the coordinator site fails and the participant sites have to wait for its recovery to complete the transaction. To overcome this problem, some variants of the two-phase commit protocol have been proposed, such as the three-phase commit protocol, which adds a pre-commit phase to reduce the blocking time, and the non-blocking commit protocol, which uses backup coordinators to avoid blocking.