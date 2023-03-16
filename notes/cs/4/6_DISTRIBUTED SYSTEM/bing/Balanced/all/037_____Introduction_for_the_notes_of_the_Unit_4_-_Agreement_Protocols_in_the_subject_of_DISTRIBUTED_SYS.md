# Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or a consistent state, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the reliability, consistency, fault-tolerance, and security of distributed systems.
- Some examples of agreement problems are:
  - Consensus: All processes agree on a single value from a set of proposed values.
  - Atomic commit: All processes agree on whether to commit or abort a distributed transaction.
  - Byzantine agreement: All processes agree on a single value from a set of proposed values, even if some processes are faulty and may behave arbitrarily.
  - Leader election: All processes agree on which process is the leader or coordinator of the system.
  - Mutual exclusion: All processes agree on which process has exclusive access to a shared resource.
- Agreement protocols are challenging to design and implement because of the following issues:
  - Asynchrony: The processes and the communication channels may have unpredictable delays or failures, making it hard to synchronize or order events.
  - Partial failure: Some processes or communication channels may fail while others continue to operate, making it hard to detect or recover from failures.
  - Non-determinism: The processes may have different inputs, states, or behaviors, making it hard to predict or control the outcome of the protocol.
  - Adversarial behavior: Some processes may be malicious or compromised, making it hard to trust or verify the messages they send or receive.