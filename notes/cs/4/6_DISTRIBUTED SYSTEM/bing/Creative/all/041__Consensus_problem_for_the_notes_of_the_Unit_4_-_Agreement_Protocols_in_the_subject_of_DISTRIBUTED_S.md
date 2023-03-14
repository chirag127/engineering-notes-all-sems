### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for achieving reliability, consistency and fault-tolerance in distributed systems.
- Consensus problem is the problem of getting a set of nodes in a distributed system to agree on something, such as a value, a course of action or a decision.
- Consensus problem is challenging because of the possibility of node failures, network delays, message losses and malicious behaviors.
- Consensus problem can be classified into three types based on the types of faults that the system can tolerate:
  - Consensus without any fault: This is the simplest case where the system is reliable, synchronous and fully connected. The nodes can reach consensus by broadcasting their values and choosing the minimum.
  - Consensus with at most m crash faults: This is the case where the system is reliable, synchronous and fully connected, but some nodes may fail by crashing. The nodes can reach consensus by performing at least m+1 rounds of message exchange, where in each round they broadcast any new value they received in the previous round. After m+1 rounds, every node will have the same set of values and can choose the minimum.
  - Consensus with at most m Byzantine faults: This is the most difficult case where the system is reliable, synchronous and fully connected, but some nodes may fail by behaving arbitrarily or maliciously. The nodes can reach consensus by using a Byzantine agreement protocol, such as the one proposed by Lamport et al. in 1982. The protocol requires 3m+1 nodes and 2m+1 rounds of message exchange, where in each round the nodes send signed messages to each other and use a majority voting scheme to decide on a value.
- Consensus problem has many applications in distributed systems, such as distributed databases, distributed transactions, distributed ledgers, distributed consensus, distributed coordination, distributed replication and distributed voting.
- Consensus problem has some properties that any consensus algorithm must satisfy:
  - Termination: Every non-faulty node must eventually decide on a value.
  - Agreement: Every non-faulty node must agree on the same value.
  - Integrity: If all the non-faulty nodes proposed the same value, then any non-faulty node must decide that value.
- Consensus problem is impossible to solve in an asynchronous system with even one faulty node, as proved by the FLP impossibility result in 1985. Therefore, consensus algorithms usually rely on some form of synchrony or randomness to break the deadlock.
- Consensus problem is usually solved by using consensus protocols, which are algorithms that implement the logic of reaching consensus in a distributed system. Some examples of consensus protocols are two-phase commit, three-phase commit, Paxos, Raft, Zab, Chandra-Toueg, PBFT, Tendermint, PoW, PoS, etc.
- Consensus problem can be solved by using different types of communication models, such as message passing, shared memory, broadcast, multicast, etc.
- Consensus problem can be solved by using different types of failure models, such as crash-stop, crash-recovery, omission, Byzantine, etc.
- Consensus problem can be solved by using different types of trust models, such as authenticated, unauthenticated, partially synchronous, asynchronous, etc.

: https://www.geeksforgeeks.org/consensus-problem-of-distributed-systems/
: https://www.baeldung.com/cs/consensus-algorithms-distributed-systems
: https://www.the-paper-trail.org/post/2008-11-27-consensus-protocols-two-phase-commit/
: https://lamport.azurewebsites.net/pubs/byz.pdf
: https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf