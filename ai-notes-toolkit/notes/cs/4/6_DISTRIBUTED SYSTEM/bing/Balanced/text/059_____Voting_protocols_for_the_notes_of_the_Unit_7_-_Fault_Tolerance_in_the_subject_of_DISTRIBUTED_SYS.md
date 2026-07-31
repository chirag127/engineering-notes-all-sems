### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed file systems, or blockchain networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires all nodes to agree on the same value or decision, and is typically implemented using two-phase commit or three-phase commit protocols.
  - Inexact voting allows some nodes to have different values or decisions, as long as a majority or a weighted majority of nodes agree on the same value or decision. Inexact voting is more flexible and resilient to faults or attacks, but may incur more communication overhead or inconsistency.
- Voting protocols can also be distinguished by their fairness properties, which measure how well they balance the interests or preferences of different nodes or groups of nodes.
  - Fairness can be defined in terms of Pareto optimality, envy-freeness, or proportional representation, among other criteria.
  - Fairness is important for ensuring the legitimacy and stability of the consensus outcome, especially in heterogeneous or adversarial networks, where different nodes may have different levels of reputation or weight.
  - Fairness can be achieved by using appropriate voting rules, such as plurality, Borda, or Condorcet, or by using cryptographic techniques, such as secret sharing, zero-knowledge proofs, or homomorphic encryption.