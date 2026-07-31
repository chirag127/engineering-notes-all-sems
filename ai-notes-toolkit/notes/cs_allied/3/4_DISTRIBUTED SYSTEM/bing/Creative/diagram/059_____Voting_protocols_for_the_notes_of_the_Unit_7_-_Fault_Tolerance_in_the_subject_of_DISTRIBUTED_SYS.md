### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a class of consensus algorithms that allow a set of distributed nodes to agree on a common value or decision in the presence of faults or failures  .
- Voting protocols can be classified into two types: exact voting and inexact voting .
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are majority voting, quorum voting, and Byzantine agreement .
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable or close enough to the correct one. Examples of inexact voting are weighted voting, approximate agreement, and probabilistic consensus .
- Voting protocols can also be distinguished by their fairness properties, which measure how well the protocol respects the preferences or weights of the nodes .
  - A voting protocol is fair if it satisfies the following conditions :
    - Anonymity: The outcome of the protocol does not depend on the identities of the nodes.
    - Neutrality: The outcome of the protocol does not favor any particular value or decision over others.
    - Monotonicity: The outcome of the protocol does not change if a node changes its preference or weight in favor of the current outcome.
    - Pareto efficiency: The outcome of the protocol is not dominated by another possible outcome, i.e., there is no other outcome that is preferred by all nodes or by a subset of nodes with higher total weight.
  - A voting protocol is unfair if it violates any of the above conditions .
- Voting protocols can be implemented using different techniques, such as message passing, shared memory, or blockchain    .
  - Message passing is a technique where nodes communicate by sending and receiving messages over a network. Message passing can be synchronous or asynchronous, reliable or unreliable, authenticated or unauthenticated, depending on the assumptions and requirements of the protocol  .
  - Shared memory is a technique where nodes access a common data structure, such as a register or a queue, that can store and retrieve values or decisions. Shared memory can be atomic or non-atomic, single-writer or multi-writer, depending on the assumptions and requirements of the protocol .
  - Blockchain is a technique where nodes maintain a distributed ledger that records the history of transactions or events, such as votes or proposals. Blockchain can be permissioned or permissionless, public or private, depending on the assumptions and requirements of the protocol .