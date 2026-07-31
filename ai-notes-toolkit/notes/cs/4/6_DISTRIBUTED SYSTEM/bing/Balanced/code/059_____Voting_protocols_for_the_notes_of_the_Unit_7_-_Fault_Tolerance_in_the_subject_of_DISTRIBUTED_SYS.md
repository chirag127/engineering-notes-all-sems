# Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are a type of consensus protocols that allow a set of distributed nodes to agree on a common value or decision.
- Voting protocols are useful for achieving fault tolerance in distributed systems, as they can tolerate the failure or malicious behavior of some nodes, as long as a majority of nodes are correct and reachable.
- Voting protocols can be classified into two categories: exact voting and inexact voting.
  - Exact voting requires that all nodes agree on the same value or decision, and that the value or decision is correct according to some predefined criterion. Examples of exact voting are the two-phase commit protocol and the Paxos algorithm.
  - Inexact voting allows some degree of disagreement or error among the nodes, as long as the value or decision is acceptable according to some predefined criterion. Examples of inexact voting are the weighted voting protocol and the Byzantine agreement protocol.
- Voting protocols can also be classified into two categories based on the security properties they provide: secure voting and non-secure voting.
  - Secure voting ensures that the value or decision agreed by the nodes is not influenced by malicious nodes or external attackers, and that the voting process is confidential and verifiable. Examples of secure voting are the secret sharing scheme and the digital signature scheme.
  - Non-secure voting does not provide any security guarantees, and relies on the assumption that the nodes are honest and the network is reliable. Examples of non-secure voting are the majority voting protocol and the plurality voting protocol.
- Voting protocols can be evaluated based on several criteria, such as fairness, efficiency, scalability, robustness, and simplicity.
  - Fairness measures how equally the nodes are treated in the voting process, and how their preferences or weights are reflected in the value or decision. Fairness can be formalized using concepts such as anonymity, neutrality, monotonicity, and proportionality.
  - Efficiency measures how fast and how cheap the voting process is, in terms of communication, computation, and storage costs. Efficiency can be formalized using concepts such as latency, throughput, bandwidth, and complexity.
  - Scalability measures how well the voting protocol can handle a large number of nodes or a dynamic network topology. Scalability can be formalized using concepts such as fault tolerance, adaptability, and self-organization.
  - Robustness measures how resilient the voting protocol is to failures or attacks, and how it can recover from them. Robustness can be formalized using concepts such as reliability, availability, consistency, and security.
  - Simplicity measures how easy the voting protocol is to understand, implement, and verify. Simplicity can be formalized using concepts such as elegance, clarity, and correctness.