### Interactive Consistency Problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Interactive consistency is the problem in which n distinct nodes, each having its own private value, where up to t may be Byzantine, run an algorithm that allows all non-faulty nodes to infer the values of each other node  .
- Byzantine nodes are nodes that can behave arbitrarily, such as sending incorrect or conflicting messages, or remaining silent.
- The goal of interactive consistency is to reach agreement in a distributed system in the presence of faults.
- Interactive consistency is also known as Byzantine Generals Problem, which is a metaphor for a situation where a group of generals must coordinate an attack or retreat, but some of them may be traitors who try to sabotage the plan.
- Interactive consistency is a fundamental problem in computer science, as it is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service, such as distributed databases, fault-tolerant systems, blockchain, and voting systems .
- Interactive consistency is a hard problem to solve, as it requires a high degree of synchronization and communication among the nodes, and it has some impossibility results that limit the feasibility and efficiency of the algorithms  .
- Some of the impossibility results are:
  - There is no deterministic algorithm that can solve interactive consistency in an asynchronous system with one or more Byzantine nodes.
  - There is no deterministic algorithm that can solve interactive consistency in a synchronous system with more than n/3 Byzantine nodes.
  - There is no randomized algorithm that can solve interactive consistency in a synchronous system with more than n/2 Byzantine nodes.
- Some of the algorithms that can solve interactive consistency in different settings are:
  - The Oral Messages Algorithm, which can solve interactive consistency in a synchronous system with up to n/3 Byzantine nodes, using O(n^2) messages and O(n) rounds.
  - The Signed Messages Algorithm, which can solve interactive consistency in a synchronous system with up to n/2 Byzantine nodes, using O(n^2) messages and O(n) rounds, but requiring digital signatures.
  - The Randomized Consensus Algorithm, which can solve interactive consistency in a synchronous system with up to n/2 Byzantine nodes, using O(n^2) messages and O(n) rounds, but requiring random bits and having a probability of failure that decreases exponentially with the number of rounds.
  - The Broadcast Algorithm, which can solve interactive consistency in a mostly-asynchronous system with up to n/3 Byzantine nodes, using O(n^2) messages and O(1) rounds, but requiring a single synchronization barrier .
- Interactive consistency is an important and challenging problem in distributed systems, and it has many applications and variations that require different assumptions and solutions.