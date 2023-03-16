## Unit 6 - Failure Recovery in Distributed Systems

- Failure recovery is the process of restoring the correct state and functionality of a distributed system after a failure occurs.
- A failure is an event that causes a deviation from the expected behavior of a system or a component.
- Failures can be classified into different types, such as:
  - Crash failure: A component stops functioning and does not resume.
  - Omission failure: A component fails to send or receive a message.
  - Timing failure: A component violates the timing constraints of the system.
  - Response failure: A component produces an incorrect output or performs an incorrect action.
  - Byzantine failure: A component behaves arbitrarily and maliciously, possibly colluding with other faulty components.
- Failure recovery can be achieved by different techniques, such as:
  - Checkpointing: A component periodically saves its state to a stable storage, which can be used to restore the state in case of a failure.
  - Logging: A component records its actions and messages to a stable storage, which can be used to replay the actions and messages in case of a failure.
  - Replication: A component is replicated by one or more backup components, which can take over the role of the primary component in case of a failure.
  - Voting: A component receives multiple results from different sources and chooses the correct one based on a majority or a consensus rule.
  - Rollback-recovery: A component reverts its state to a previous consistent state after a failure, and resumes the computation from that point.
  - Forward-recovery: A component detects and corrects the errors in its state after a failure, and continues the computation from the current point.