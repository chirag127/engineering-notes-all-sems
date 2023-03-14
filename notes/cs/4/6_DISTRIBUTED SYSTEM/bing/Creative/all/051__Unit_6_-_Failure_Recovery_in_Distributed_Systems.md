## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the system to a correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of the system to continue functioning despite failures.
- Failures can be classified into different types, such as crash failures, omission failures, timing failures, response failures, Byzantine failures, etc.
- Different types of failures require different recovery techniques, such as checkpointing, logging, replication, voting, etc.
- Some of the key concepts and techniques for failure recovery in distributed systems are:

  - Stable storage: A storage device that can withstand any failure except major disasters. It can be implemented by using a pair of regular disks that store identical copies of each block. Whenever a block is updated, both disks are updated and verified. If one disk fails or corrupts, the other disk can be used to recover the block.
  - Checkpointing: A technique that periodically saves the state of the system to stable storage. A checkpoint is a consistent global state of the system that can be used to restart the system after a failure. Checkpointing can be coordinated or uncoordinated among the processes in the system.
  - Logging: A technique that records the events and actions of the system to stable storage. A log is a sequence of records that can be used to replay or undo the effects of the events and actions. Logging can be physical or logical, depending on whether the records store the actual data or the operations on the data.
  - Replication: A technique that maintains multiple copies of the same data or service on different nodes in the system. Replication can improve availability, reliability, and performance of the system. Replication can be passive or active, depending on whether the replicas are updated synchronously or asynchronously.
  - Voting: A technique that uses a majority or consensus of the replicas to determine the correct value or decision in the system. Voting can resolve conflicts, detect faults, and ensure consistency among the replicas. Voting can be static or dynamic, depending on whether the number and identity of the voters are fixed or variable.