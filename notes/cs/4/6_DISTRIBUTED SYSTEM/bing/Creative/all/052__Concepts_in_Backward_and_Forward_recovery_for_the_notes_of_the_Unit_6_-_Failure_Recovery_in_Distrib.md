### Concepts in Backward and Forward recovery for the notes of the Unit 6 - Failure Recovery in Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Backward recovery and forward recovery are two techniques for restoring a distributed system to a consistent state after a failure.
- Backward recovery involves moving the system from its current erroneous state to a previously correct state by using checkpoints .
- Checkpoints are snapshots of the system state that are periodically saved to stable storage .
- A checkpoint is consistent if it does not contain any partial effects of a transaction. For example, if a process P has recorded the receipt of a message in a checkpoint, then there should also be a process Q that has recorded the sending of that message in its checkpoint.
- Backward recovery requires the system to roll back to the most recent consistent checkpoint and undo the effects of any incomplete transactions .
- Backward recovery does not depend on the nature of the faults, but it may incur a high overhead of checkpointing and rollback .
- Forward recovery involves moving the system from its current erroneous state to a new correct state by correcting the errors and continuing the execution.
- Forward recovery requires the system to anticipate and detect the possible errors and have a mechanism to correct them.
- Forward recovery does not need to save checkpoints, but it may not be able to handle all types of errors .
- A mnemonic to remember the difference between backward and forward recovery is: **backward** goes **back** to a previous state, **forward** goes **forward** to a new state.
- An example of backward recovery is the undo operation in a text editor, which restores the previous state of the document.
- An example of forward recovery is the error correction code in a communication system, which detects and corrects the errors in the transmitted data.