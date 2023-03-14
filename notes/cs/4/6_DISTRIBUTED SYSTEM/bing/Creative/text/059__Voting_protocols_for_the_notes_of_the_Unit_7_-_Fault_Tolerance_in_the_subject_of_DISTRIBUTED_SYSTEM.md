### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a technique for achieving consensus among distributed nodes in the presence of faults or attacks.
- Consensus is the agreement on a common value or decision by a majority or a quorum of nodes.
- Voting protocols can be used for various purposes, such as data replication, transaction commit, leader election, etc.
- Voting protocols can be classified into two types: exact and inexact.
  - Exact voting protocols require all nodes to agree on the same value or decision, such as the two-phase commit protocol.
  - Inexact voting protocols allow nodes to agree on an approximate value or decision, such as the weighted voting protocol.
- Voting protocols can also be classified into two types: secure and non-secure.
  - Secure voting protocols ensure that the consensus is not influenced by malicious nodes or external attacks, such as the fair voting protocol.
  - Non-secure voting protocols do not provide any security guarantees and assume that all nodes are honest and reliable, such as the majority voting protocol.
- Voting protocols have several properties and challenges, such as:
  - Fairness: the influence of each node on the consensus is proportional to its weight or reputation.
  - Anonymity: the identity of each node is not revealed during the voting process.
  - Centralization: the degree of dependence on a single node or a subset of nodes for the consensus.
  - Scalability: the ability to handle a large number of nodes and messages in the system.
  - Atomicity: the guarantee that the consensus is either achieved by all nodes or none.
  - Termination: the guarantee that the voting process will eventually end with a consensus or a failure.
  - Validity: the guarantee that the consensus value or decision is valid and consistent with the input of the nodes.