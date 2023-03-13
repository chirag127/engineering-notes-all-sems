## Unit 2 - Consensus

Consensus is the process of reaching agreement among a group of participants on a shared state or a decision. Consensus is essential for distributed systems, where multiple nodes need to coordinate their actions and maintain consistency.

Some of the topics covered in this unit are:

- **The consensus problem**: The formal definition and the challenges of solving it in asynchronous and partially synchronous systems. The impossibility results of FLP and CAP theorem, and the trade-offs between consistency, availability, and partition tolerance.
- **Consensus algorithms**: The basic principles and properties of some well-known consensus algorithms, such as Paxos, Raft, and Byzantine Fault Tolerance (BFT). The differences and similarities between them, and their advantages and disadvantages in different scenarios.
- **Consensus applications**: The practical use cases and examples of consensus algorithms in various domains, such as distributed databases, blockchain, and cloud computing. The challenges and opportunities of applying consensus algorithms in real-world systems.

Some of the mnemonics and learning tricks for this unit are:

- **FLP**: Fischer, Lynch, and Paterson are the authors of the FLP impossibility result, which states that no deterministic consensus algorithm can guarantee termination in an asynchronous system with one faulty process. A mnemonic to remember this is: **F**aulty **L**eaders **P**revent consensus.
- **CAP**: Brewer's CAP theorem states that in a distributed system, it is impossible to achieve both consistency and availability in the presence of network partitions. A mnemonic to remember this is: **C**hoose **A**vailability or **P**artition tolerance.
- **Paxos**: Paxos is a family of consensus algorithms that use a leader-based approach and a two-phase commit protocol to reach agreement. A mnemonic to remember the basic steps of Paxos is: **P**ropose, **A**ccept, **X**ecute, **O**rder, **S**ync.
- **Raft**: Raft is a consensus algorithm that simplifies Paxos by using a stronger leader and a more intuitive state machine. A mnemonic to remember the basic steps of Raft is: **R**eplicate, **A**ppend, **F**ollow, **T**erm.
- **BFT**: Byzantine Fault Tolerance is a class of consensus algorithms that can tolerate arbitrary faults, including malicious behavior, among a subset of participants. A mnemonic to remember the basic idea of BFT is: **B**elieve, **F**ilter, **T**rust.