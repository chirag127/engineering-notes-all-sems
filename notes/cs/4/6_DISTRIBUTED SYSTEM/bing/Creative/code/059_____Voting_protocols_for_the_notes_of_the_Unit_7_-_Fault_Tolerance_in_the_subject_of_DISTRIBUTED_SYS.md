### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision  .
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are honest and reachable  .
- Voting protocols can be classified into two categories: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria .
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria .
- Voting protocols can also be classified based on the number of rounds or phases they require to reach a consensus .
  - One-phase voting protocols require only one round of communication among the nodes, where each node sends its vote to a coordinator, and the coordinator decides the final value or decision based on the majority of votes .
  - Two-phase voting protocols require two rounds of communication among the nodes, where the first round is similar to one-phase voting, and the second round is used to confirm or abort the decision of the coordinator .
  - Multi-phase voting protocols require more than two rounds of communication among the nodes, where each round is used to exchange information, propose values or decisions, and reach partial agreements .
- Voting protocols can also be classified based on the level of security or fairness they provide .
  - Security refers to the ability of the voting protocol to resist attacks from malicious nodes, such as lying, cheating, or colluding .
  - Fairness refers to the ability of the voting protocol to ensure that every node has an equal chance of influencing the final value or decision, regardless of its reputation or weight .
  - Secure and fair voting protocols are desirable, but they may have trade-offs with other properties, such as efficiency, scalability, or simplicity .