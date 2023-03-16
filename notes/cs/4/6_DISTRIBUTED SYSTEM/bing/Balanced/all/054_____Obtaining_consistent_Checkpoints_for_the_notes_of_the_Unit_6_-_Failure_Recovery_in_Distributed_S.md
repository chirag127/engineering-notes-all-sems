# Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Failure recovery in distributed systems is the process of restoring the system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite the presence of errors.
- Failure recovery can be achieved by using checkpoints, which are snapshots of the system state at certain points in time.
- Checkpoints can be used to rollback the system to a previous state and resume the execution from there, avoiding the need to restart the system from scratch.
- Checkpoints can be classified into two types: global and local.
  - Global checkpoints capture the state of the entire system, including all the processes and communication channels.
  - Local checkpoints capture the state of a single process or a group of processes.
- Checkpoints can also be classified into two types: synchronous and asynchronous.
  - Synchronous checkpoints require coordination among all the processes to take a consistent snapshot of the system.
  - Asynchronous checkpoints allow each process to take a snapshot independently, without waiting for others.
- Synchronous checkpoints have the advantage of simplicity and consistency, but they incur a high overhead and may cause blocking or deadlock.
- Asynchronous checkpoints have the advantage of efficiency and scalability, but they may result in inconsistent or useless snapshots that cannot be used for recovery.
- To obtain consistent checkpoints in distributed systems, several algorithms and techniques have been proposed, such as :
  - The Chandy-Lamport algorithm, which uses special messages called markers to record the state of the communication channels.
  - The Lai-Yang algorithm, which uses a global clock to synchronize the processes and record the state of the communication channels.
  - The Manetho algorithm, which uses a distributed logging mechanism to record the causal dependencies among the processes.
  - The Zorro algorithm, which uses a zero-cost reactive approach to detect and correct inconsistent checkpoints on the fly.
- The choice of the checkpointing algorithm depends on several factors, such as the system model, the failure model, the communication model, the performance requirements, and the recovery objectives.