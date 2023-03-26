 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Recovery in Concurrent systems

- Recovery techniques can be broadly classified into 2 types:
** passive recovery: Where spare processes take over the work of failed processes. No state transfer is required. Suitable for stateless tasks.
** active recovery: Failed process is restarted and its state is reconstructed from checkpoints or backups. Suitable for stateful tasks.
- Passive recovery is simpler but may lead to reduced throughput. Active recovery is more complex but can provide better performance.
- The system should be able to mask failures from the user. This is called fault tolerance. The time period between failure and completion of recovery should be minimized. This is called fault resilience.
- The system state can be maintained at either the process level or the system level:
** Process-level: Each process maintains its own state. Failure leads to loss of state of the failed process.
** System-level: The system maintains a global state. Failure leads to recovery of the system state. Can be complex to implement.
- To enable recovery, the system state is periodically saved in stable storage as checkpoints. On failure, the system is rolled back to the latest checkpoint and re-executed. This may lead to loss of work since last checkpoint.
- The frequency of checkpointing is a trade-off between the amount of work lost and the overhead of checkpointing. Checkpointing leads to a performance penalty and should be done judiciously.
- Log records can be maintained to rollback to any specific point in between checkpoints. This reduces the amount of lost work but increases the logging and recovery overhead.
- The system can be made fault tolerant by replication or redundancy. The state of the system is maintained in multiple replicas. On failure of one replica, others can continue service. However, this leads to higher resource requirements and complexity.
- The concurrency control techniques and recovery techniques should be integrated for correct operation in case of failures. The state reconstruction should be done in a manner consistent with concurrency control.