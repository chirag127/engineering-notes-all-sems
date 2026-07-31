## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring a distributed system to a consistent and correct state after a failure occurs.
- Failure recovery is essential for fault tolerance, which is the ability of a system to continue functioning despite faults or errors.
- There are different types of failures that can affect a distributed system, such as:
  - Node failures: when a site or a process in the system stops working or crashes.
  - Communication failures: when a message or a connection between sites or processes is lost or delayed.
  - Media failures: when a secondary storage device, such as a disk or a tape, fails or gets corrupted.
  - Byzantine failures: when a site or a process behaves maliciously or arbitrarily, sending incorrect or conflicting messages to other sites or processes.
- There are different techniques for failure recovery in distributed systems, such as:
  - Checkpointing: when a site or a process periodically saves its state to a stable storage, which can resist major disasters. In case of a failure, the site or process can resume from the last saved checkpoint.
  - Logging: when a site or a process records its actions and messages to a stable storage, which can be used to replay or undo the actions and messages in case of a failure.
  - Replication: when a site or a process maintains multiple copies of its state or data on different sites or processes, which can be used to replace or update the faulty copy in case of a failure.
  - Voting: when a site or a process consults with other sites or processes to reach a consensus or a majority on the correct state or data, which can be used to detect or correct a failure.
  - Recovery blocks: when a site or a process executes a sequence of alternative modules or actions, each with an acceptance test, until one of them succeeds or passes the test, which can be used to handle a failure.