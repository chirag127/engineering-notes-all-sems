### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Voting protocols are used to achieve consensus on transactions and network decisions in distributed systems by tallying the number of votes cast by nodes.
- Voting protocols are also used to enforce mutual exclusion in distributed systems by assigning a number of votes to each node and allowing only the group with a majority of votes to perform a restricted operation.
- Voting protocols can be classified into two types: static and dynamic.
  - Static voting protocols assign a fixed number of votes to each node and do not change them during the system operation. Static voting protocols are simple and efficient, but they may suffer from low availability and fault tolerance if some nodes or links fail.
  - Dynamic voting protocols allow nodes to change their vote values upon node or link failure, in an attempt to make the system more resilient. Dynamic voting protocols are more complex and costly, but they can improve the availability and fault tolerance of the system by reassigning votes to the surviving nodes.
- Voting protocols require a quorum, which is a subset of nodes that must agree on a decision for it to be valid. A quorum can be defined as a simple majority, a weighted majority, or a custom function of the vote values and the node states.
- Voting protocols can be implemented using different techniques, such as:
  - Group-based voting, which arranges nodes in small intersecting groups, such that a node, in absence of failures, needs to communicate only with members of its group to collect the quorum.
  - Leader-based voting, which elects a leader node that collects the votes from other nodes and decides the outcome of the transaction or the network decision.
  - Hash-based voting, which uses a hash function to map each transaction or network decision to a subset of nodes that are responsible for voting on it.
- Voting protocols have advantages and disadvantages, such as:
  - Advantages: Voting protocols are Byzantine fault tolerant, meaning they can tolerate malicious or faulty nodes that may lie or behave arbitrarily. Voting protocols are also democratic, meaning they give equal or proportional power to each node according to its vote value.
  - Disadvantages: Voting protocols are slow and inefficient, meaning they require a lot of communication and computation overhead to reach consensus. Voting protocols are also unfair, meaning they do not guarantee the chronological order of the transactions or the network decisions, and they may be influenced by external factors such as bribes or threats.
- Voting protocols are used in various applications, such as:
  - Distributed databases, which use voting protocols to ensure the atomicity and consistency of transactions that span multiple sites.
  - Distributed ledgers, which use voting protocols to achieve consensus on the state and the history of the ledger among the nodes.
  - Distributed systems, which use voting protocols to coordinate the actions and the configurations of the nodes.

: https://hedera.com/learning/consensus-algorithms/what-are-voting-based-consensus-algorithms
: https://www.cs.princeton.edu/research/techreps/TR-037-86
: https://itqaguru.com/what-is-voting-protocol-in-distributed-system/
: https://en.wikipedia.org/wiki/Quorum_%28distributed_computing%29