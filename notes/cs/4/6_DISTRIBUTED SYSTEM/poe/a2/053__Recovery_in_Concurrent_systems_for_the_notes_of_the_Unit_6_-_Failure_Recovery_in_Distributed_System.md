 Here is the formal content in Markdown format without any emojis or external links on the topic "Recovery in Concurrent systems" for the notes of Unit 6 - Failure Recovery in Distributed Systems:

### Recovery in Concurrent systems

1. Recovery in distributed systems is challenging due to concurrent processes and lack of global state.
2. Log-based recovery: Maintain logs of all operations. On failure, redo all operations from logs to recover. However, determining correct order of operations from logs can be difficult in concurrent systems.
3. Checkpointing: Take periodic snapshots/checkpoints of system state. On failure, recover from latest checkpoint. However, determining consistent global checkpoint is challenging.
4. Combination of logging and checkpointing: Use checkpointing for performance, and logging to recover from failures between checkpoints.
5. Replication: Maintain multiple replicas of data/services. On failure, switch to healthy replica. However, consistency must be ensured between replicas.
6. Stronger semantics: Use stronger consistency models (linearizability, serializability, etc.) to simplify recovery. However, this impacts performance.

The material is written in a formal tone with points in a Markdown format as requested. Please let me know if you would like me to modify or expand the content in any way.