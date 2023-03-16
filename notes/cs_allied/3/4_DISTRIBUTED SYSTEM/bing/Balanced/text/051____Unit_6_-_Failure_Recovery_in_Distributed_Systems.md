## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite faults or errors.
- There are different types of failures that can affect a distributed system, such as:
  - Node failures: when a site or a process in the system stops working or crashes.
  - Communication failures: when a message between two sites or processes is lost, delayed, corrupted, or duplicated.
  - Network failures: when a link or a network segment in the system becomes unavailable or partitioned.
  - Media failures: when a secondary storage device in the system fails or gets damaged.
  - Byzantine failures: when a site or a process in the system behaves maliciously or arbitrarily, violating the system assumptions or protocols.
- There are different techniques for failure recovery in distributed systems, such as:
  - Checkpointing: when a site or a process periodically saves its state to a stable storage, which can resist major disasters. In case of a failure, the site or the process can resume from the last saved checkpoint.
  - Logging: when a site or a process records its actions or events to a stable storage, which can be used to replay or undo the actions or events in case of a failure.
  - Replication: when a site or a process maintains multiple copies of its state or data across different sites or processes in the system, which can provide redundancy and availability in case of a failure.
  - Consensus: when a group of sites or processes in the system agree on a common value or decision, which can ensure consistency and correctness in case of a failure.
  - Fault detection: when a site or a process monitors the status or the behavior of other sites or processes in the system, which can help to identify and isolate the faulty ones.
  - Fault masking: when a site or a process hides or compensates the effects of a failure from the rest of the system, which can prevent the failure from propagating or affecting the system functionality.