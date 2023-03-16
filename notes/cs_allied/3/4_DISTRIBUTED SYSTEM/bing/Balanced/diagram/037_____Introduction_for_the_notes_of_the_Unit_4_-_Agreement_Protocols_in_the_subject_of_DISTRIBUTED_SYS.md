### Introduction

- Agreement protocols are a class of protocols that enable a set of processes to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties in the system.
- Agreement protocols are essential for ensuring the consistency, reliability, and availability of distributed systems, especially in the face of faults, attacks, or network partitions.
- Agreement protocols can be classified into different types, depending on the problem they aim to solve, the assumptions they make about the system model, and the properties they guarantee. Some of the common types of agreement protocols are:
  - **Atomic commit**: A protocol that ensures that a set of processes either all commit to execute a transaction or all abort it, even if some processes or the coordinator fail.
  - **Consensus**: A protocol that ensures that a set of processes agree on a single value, chosen from the set of proposed values, even if some processes fail or behave maliciously.
  - **Byzantine agreement**: A protocol that ensures that a set of processes agree on a single value, chosen from the set of proposed values, even if some processes fail or behave maliciously, and the communication channels are unreliable or compromised.
  - **Leader election**: A protocol that ensures that a set of processes elect a unique leader, who can coordinate the actions of the other processes, even if some processes fail or leave the system.
  - **Group membership**: A protocol that ensures that a set of processes maintain a consistent view of the current members of the system, even if some processes join, leave, or fail.
- Agreement protocols can be implemented using various techniques, such as message passing, shared memory, logical clocks, vector clocks, timestamps, quorums, Paxos, Raft, blockchain, etc.
- Agreement protocols can be evaluated based on various criteria, such as correctness, termination, validity, agreement, fault tolerance, resilience, safety, liveness, complexity, scalability, performance, etc.