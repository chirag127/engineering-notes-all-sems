### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision, despite the presence of faults or attacks.
- Voting protocols are useful for achieving fault tolerance in distributed systems, such as replicated databases, distributed ledgers, or peer-to-peer networks.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criteria. Examples of exact voting protocols are two-phase commit, three-phase commit, and Paxos.
  - Inexact voting allows for some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criteria. Examples of inexact voting protocols are majority voting, weighted voting, and probabilistic voting.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision is not influenced by malicious nodes or external attackers, and that the voting process is confidential and verifiable. Examples of secure voting protocols are Byzantine agreement, threshold cryptography, and zero-knowledge proofs.
  - Non-secure voting does not provide any security guarantees, and assumes that the nodes are honest and the network is reliable. Examples of non-secure voting protocols are simple majority voting, quorum-based voting, and Lamport's algorithm.