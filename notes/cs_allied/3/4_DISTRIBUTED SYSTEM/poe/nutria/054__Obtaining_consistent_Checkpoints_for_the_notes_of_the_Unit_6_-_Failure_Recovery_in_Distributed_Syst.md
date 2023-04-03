

### Obtaining consistent Checkpoints for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

1. Checkpointing is a technique used to ensure that the distributed system can recover from failures. 
2. It involves taking a snapshot of the system's state at regular intervals and storing it in a safe location.
3. The checkpointing process should be deterministic, meaning that the same sequence of actions should produce the same results every time.
4. Checkpoints should be taken frequently enough to provide an acceptable level of recovery.
5. When a failure occurs, the system can be restored to the state it was in at the time of the last checkpoint.
6. The system can then be restarted from that point and continue normal operation.
7. Checkpoints should be stored in a secure location, such as a database or a file system, to ensure that they are not lost in the event of a system failure.
8. Checkpoints should also be taken in such a way that the system can be restored to a consistent state, meaning that all transactions that were in progress at the time of the checkpoint are either committed or rolled back.
9. This ensures that the system is in a consistent state when it is restarted.
10. Checkpoints should also be taken in such a way that the system can be restored to the same state it was in when the checkpoint was taken.
11. This ensures that the system is not left in an inconsistent state after a failure.