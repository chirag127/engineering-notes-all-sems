### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks in the system  .
- Voting protocols are based on the idea of collecting votes from a majority or a quorum of nodes, and choosing the value that has the most votes as the consensus value .
- Voting protocols can be classified into two categories: exact voting and inexact voting  .
  - Exact voting requires that all nodes vote for the same value, and that the value is correct and consistent with the system state. Exact voting is typically used for atomic commit or distributed transactions, where the nodes need to agree on whether to commit or abort a transaction  .
  - Inexact voting allows for some nodes to vote for different values, and that the value may not be correct or consistent with the system state. Inexact voting is typically used for fault detection or fault masking, where the nodes need to agree on a value that can tolerate some errors or discrepancies  .
- Voting protocols can also be classified into two types: majority voting and weighted voting .
  - Majority voting assumes that all nodes have equal weight or reputation, and that the consensus value is the one that has more than half of the votes. Majority voting is simple and robust, but it requires a large number of nodes and a high degree of connectivity to achieve consensus .
  - Weighted voting assigns different weights or reputations to different nodes, and that the consensus value is the one that has the highest sum of weights. Weighted voting is more flexible and efficient, but it requires a fair and secure way of assigning and updating the weights of the nodes .
- Voting protocols face several challenges and trade-offs in distributed systems, such as  :
  - Fault tolerance: the ability to cope with node failures, network partitions, message losses, or message delays, and still reach consensus.
  - Security: the ability to resist malicious attacks, such as node impersonation, vote tampering, vote suppression, or vote fabrication, and still reach consensus.
  - Performance: the ability to reach consensus quickly, with low communication and computation overhead, and low latency and bandwidth consumption.
  - Scalability: the ability to reach consensus among a large number of nodes, with high diversity and dynamism, and low coordination and synchronization costs.
  - Fairness: the ability to ensure that all nodes have equal or proportional chances of influencing the consensus value, and that no node is unfairly favored or discriminated.