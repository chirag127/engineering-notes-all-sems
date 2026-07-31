## Unit 4 - Agreement Protocols

- Agreement protocols are a class of distributed algorithms that allow a set of processes to reach a consensus on a value or a decision, despite the presence of failures or uncertainties.
- Agreement protocols are useful for solving problems such as leader election, distributed commit, atomic broadcast, and fault tolerance.
- Agreement protocols can be classified into two types: **synchronous** and **asynchronous**.
  - Synchronous protocols assume that there are known bounds on the message delays and the process speeds, and use timeouts or rounds to coordinate the processes.
  - Asynchronous protocols do not make any assumptions about the timing of the system, and rely on message ordering or logical clocks to ensure progress.
- Agreement protocols can also be characterized by the following properties: **validity**, **agreement**, **termination**, and **fault tolerance**.
  - Validity means that the agreed value must be one of the proposed values by the processes.
  - Agreement means that all correct processes must agree on the same value.
  - Termination means that all correct processes must eventually decide on a value.
  - Fault tolerance means that the protocol can tolerate a certain number of faulty processes, such as crashed, Byzantine, or malicious processes.
- Some examples of agreement protocols are:
  - **Paxos**, which is a family of asynchronous protocols that can tolerate up to half of the processes being crashed, and guarantee safety (validity and agreement) under all circumstances, and liveness (termination) under some assumptions.
  - **Raft**, which is a synchronous protocol that can tolerate up to half of the processes being crashed, and guarantee safety and liveness, as well as simplicity and understandability.
  - **Two-phase commit (2PC)**, which is a synchronous protocol that can tolerate up to one process being crashed, and guarantee atomicity and durability of a distributed transaction, but may block if the coordinator fails.
  - **Three-phase commit (3PC)**, which is a synchronous protocol that can tolerate up to one process being crashed, and guarantee atomicity and durability of a distributed transaction, as well as non-blocking, but may violate consistency if there are network partitions.
  - **Practical Byzantine Fault Tolerance (PBFT)**, which is a synchronous protocol that can tolerate up to one-third of the processes being Byzantine, and guarantee safety and liveness, as well as high performance and scalability.