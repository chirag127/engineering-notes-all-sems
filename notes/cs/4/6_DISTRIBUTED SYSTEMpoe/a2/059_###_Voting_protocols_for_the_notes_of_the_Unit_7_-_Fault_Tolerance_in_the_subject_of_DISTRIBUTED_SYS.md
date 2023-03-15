 Here is the content in markdown format for the topic ### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM:

### Voting protocols for Fault Tolerance

- **Majority voting:** Each node votes to agree or disagree on a value/decision. The final decision is the one that gets majority votes.
**Advantages:** Simple, effective if majority of nodes are correct.
**Disadvantages:** Less fault tolerant if equal votes or if >50% nodes are faulty.

- **Weighted voting:** Nodes are assigned weights based on processing power/resources. The decision is the one voted by nodes with weight sum greater than or equal to a threshold.
**Advantages:** More fault tolerant than majority voting if weights reflect node reliability.
**Disadvantages:** Complex to implement and nodes with higher weights have more influence.

- **Reconfigurable voting:** The voting protocol can be reconfigured dynamically based on which nodes are operational.
**Advantages:** Highly fault tolerant as the system adapts to node failures.
**Disadvantages:** Very complex to implement and overhead of reconfiguring the protocol.

**Mnemonics:**
Majority - simple majority
Weights - powerful nodes have more say
Reconfigurable - adapts to changes

**Application:** Choosing between conflicting values/decisions from multiple nodes in a distributed system to mask failures and ensure consistency. Widely used for replication and atomic broadcast.

The above content summarizes the key points about the voting protocols for fault tolerance in distributed systems. I have included the pros and cons, mnemonics and applications where relevant to help in learning and recalling the topics. Please let me know if you would like me to elaborate on any part or modify the content.