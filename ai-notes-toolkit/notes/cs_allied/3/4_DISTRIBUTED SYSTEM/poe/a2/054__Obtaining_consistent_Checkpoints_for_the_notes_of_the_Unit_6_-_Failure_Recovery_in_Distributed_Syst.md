 Here is the content in markdown format without any emojis or external links:

### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Checkpointing is a mechanism to record the state of a distributed system at certain points in time. This allows the system to roll back to a previous correct state in case of failures.
2. The challenge in distributed systems is to obtain consistent global checkpoints, i.e., checkpoints that reflect a correct global state of the system.
3. Two main approaches to obtain consistent checkpoints in distributed systems:

- Coordinated checkpointing: Process checkpoints are coordinated by a central coordinator. Processes are forced to checkpoint in a certain order to maintain consistency.
- Uncoordinated checkpointing: Processes independently decide when to checkpoint based on their own progress. Causality tracking is used to determine consistent global checkpoints in retrospect.

4. Comparison:

- Coordinated checkpointing typically yields lower overhead but suffers from coordinator bottlenecks.
- Uncoordinated checkpointing has lower coordination overhead but may waste work if inconsistent checkpoints are selected.

5. Other approaches like communication-induced checkpointing have been proposed to balance the trade-offs. The optimal approach depends on the particular system and workload.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.