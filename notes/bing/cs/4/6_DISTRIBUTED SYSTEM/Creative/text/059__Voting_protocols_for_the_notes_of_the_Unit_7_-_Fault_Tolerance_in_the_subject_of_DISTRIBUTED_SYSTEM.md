### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a technique for achieving consensus among a set of distributed processes or nodes that may be subject to faults or attacks.
- Voting protocols can be used for various purposes, such as data replication, transaction commit, leader election, or distributed agreement.
- Voting protocols typically involve two phases: a voting phase and a decision phase. In the voting phase, each node sends its vote (or preference) to a coordinator or to all other nodes. In the decision phase, the coordinator or the nodes collect the votes and decide on the outcome based on some criteria.
- Voting protocols can be classified into two types: exact voting and inexact voting. Exact voting requires that all nodes agree on the same outcome, while inexact voting allows for some degree of disagreement or uncertainty.
- Exact voting protocols can be further divided into majority voting and unanimous voting. Majority voting requires that more than half of the nodes vote for the same outcome, while unanimous voting requires that all nodes vote for the same outcome.
- Inexact voting protocols can be further divided into weighted voting and probabilistic voting. Weighted voting assigns different weights to the nodes based on their reputation or reliability, and decides on the outcome based on the sum of the weights. Probabilistic voting uses randomization or cryptography to decide on the outcome based on the probability of the votes.
- Voting protocols need to consider both fault-tolerance and security aspects. Fault-tolerance refers to the ability of the protocol to cope with node failures, network partitions, or message losses. Security refers to the ability of the protocol to resist malicious attacks, such as denial-of-service, impersonation, or tampering.
- Some of the challenges and trade-offs in designing voting protocols are:

  - How to ensure fairness and correctness of the voting process and the outcome?
  - How to balance the performance and the overhead of the voting protocol?
  - How to handle dynamic changes in the system, such as node join or leave, or network reconfiguration?
  - How to deal with partial or incomplete information, such as missing or delayed votes, or conflicting votes?