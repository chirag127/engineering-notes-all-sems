 Here is the content in markdown format without any emojis or external links, in a formal tone with points:

### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Checkpointing is a technique to record the state of a distributed system at a particular instant of time. This recorded state can be used to resume execution in case of a failure.
2. Consistent global checkpoints are required to ensure that the resumed execution is logically correct. A consistent global checkpoint is a set of local checkpoints, one at each process, such that no messages are in transit between the processes.
3. Two basic methods to obtain consistent global checkpoints are:

(a) Coordinated checkpointing: Processes are synchronized to take local checkpoints simultaneously. This avoids the problem of messages in transit but the synchronization overhead can affect performance.
(b) Communication-induced checkpointing: Each process takes local checkpoints independently after processing messages from all neighbours. The resulting global checkpoint may be inconsistent. Subsequently, a recovery line algorithm is used to determine a consistent global checkpoint. The advantage is that checkpointing can be done asynchronously without synchronization.

4. The recovery line algorithm works as follows:
(a) Take an initial global checkpoint G
(b) Each process maintains a list of messages received after G
(c) When a process takes a new local checkpoint, it sends a message to all neighbours with the message numbers of messages received after the current checkpoint
(d) When a process receives messages from all neighbours, the smallest message number across all messages is the recovery line. Local checkpoints prior to the recovery line form a consistent global checkpoint.

5. The key advantage of asynchronous checkpointing is reduced performance overhead due to lack of synchronization. However, determining a consistent global checkpoint may take more time and the resulting checkpoint may be stale. The trade-off depends on system characteristics and requirements.