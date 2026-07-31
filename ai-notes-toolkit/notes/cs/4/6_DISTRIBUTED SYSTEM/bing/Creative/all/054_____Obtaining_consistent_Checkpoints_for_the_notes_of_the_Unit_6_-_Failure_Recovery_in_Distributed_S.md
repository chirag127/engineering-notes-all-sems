# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- Failure recovery can be achieved by using checkpoints, which are snapshots of the system state at certain points in time.
- Checkpoints can be used to roll back the system to a previous state in case of a failure, and to resume the execution from that point.
- Checkpoints can be classified into two types: local and global.
  - Local checkpoints are taken by individual processes independently, without any coordination with other processes.
  - Global checkpoints are taken by all processes in the system in a coordinated manner, such that they form a consistent global state.
- A global state is consistent if it does not contain any orphan messages, which are messages that are sent by a process before taking a checkpoint, but are received by another process after taking a checkpoint.
- A global state is also consistent if it does not contain any lost messages, which are messages that are sent by a process after taking a checkpoint, but are lost due to a failure before reaching the destination.
- To obtain consistent global checkpoints, the system can use different algorithms, such as the following :
  - Synchronous checkpointing: All processes take checkpoints simultaneously, after exchanging messages to synchronize their clocks.
  - Asynchronous checkpointing: Each process takes checkpoints independently, without any synchronization with other processes.
  - Coordinated checkpointing: Each process takes checkpoints in a coordinated manner, after receiving a checkpoint request message from a coordinator process.
  - Communication-induced checkpointing: Each process takes checkpoints based on the messages it receives from other processes, using a dependency tracking mechanism.
- The advantages and disadvantages of these algorithms depend on various factors, such as the frequency of checkpoints, the overhead of communication, the storage space required, the number of processes involved, the failure rate, and the recovery time .
- The choice of the checkpointing algorithm should be based on the trade-off between these factors, and the specific requirements and characteristics of the distributed system .