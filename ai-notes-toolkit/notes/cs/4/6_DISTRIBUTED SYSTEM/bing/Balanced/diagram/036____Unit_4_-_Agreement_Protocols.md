## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a common decision or consensus in the presence of failures or uncertainties.
- Agreement protocols are useful for solving problems such as leader election, atomic commit, distributed mutual exclusion, and fault tolerance.
- Agreement protocols can be classified into two types: **synchronous** and **asynchronous**.
- Synchronous agreement protocols assume that there are known bounds on the message delays and the process speeds, and use timeouts or clocks to coordinate the actions of the processes.
- Asynchronous agreement protocols do not make any assumptions about the message delays and the process speeds, and rely on message ordering or logical clocks to coordinate the actions of the processes.
- Synchronous agreement protocols can tolerate crash failures, where a process stops executing, and Byzantine failures, where a process behaves arbitrarily or maliciously.
- Asynchronous agreement protocols can only tolerate crash failures, and not Byzantine failures, unless additional assumptions are made, such as the existence of a trusted third party or a majority of correct processes.
- Some examples of synchronous agreement protocols are:
  - **Paxos**, which is a protocol for reaching consensus on a single value among a set of processes, using a leader-based approach and a majority voting scheme.
  - **Raft**, which is a protocol for maintaining a replicated state machine among a set of processes, using a leader-based approach and a log replication scheme.
  - **Two-phase commit (2PC)**, which is a protocol for ensuring atomicity of a distributed transaction among a set of processes, using a coordinator process and a prepare-commit scheme.
- Some examples of asynchronous agreement protocols are:
  - **Chandra-Toueg consensus**, which is a protocol for reaching consensus on a single value among a set of processes, using a failure detector and a round-based scheme.
  - **Viewstamped replication (VSR)**, which is a protocol for maintaining a replicated state machine among a set of processes, using a primary-backup approach and a view change scheme.
  - **Three-phase commit (3PC)**, which is a protocol for ensuring atomicity of a distributed transaction among a set of processes, using a coordinator process and a pre-commit-commit scheme.