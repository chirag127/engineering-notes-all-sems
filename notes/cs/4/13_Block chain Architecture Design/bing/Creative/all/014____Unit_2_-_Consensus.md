## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state or value.
- Consensus is essential for distributed systems that need to coordinate their actions and maintain consistency across multiple replicas or nodes.
- Consensus can be achieved by various algorithms or protocols, such as Paxos, Raft, Byzantine Fault Tolerance, Proof of Work, Proof of Stake, etc.
- Consensus algorithms or protocols have different properties and trade-offs, such as fault tolerance, availability, latency, throughput, scalability, security, etc.
- Consensus algorithms or protocols can be classified into two categories: leader-based and leaderless.
  - Leader-based consensus algorithms or protocols elect a leader node that proposes and commits values on behalf of the group. Examples are Paxos and Raft.
  - Leaderless consensus algorithms or protocols allow any node to propose and commit values without relying on a leader. Examples are Byzantine Fault Tolerance and Proof of Work.
- Consensus algorithms or protocols can also be classified into two categories: deterministic and probabilistic.
  - Deterministic consensus algorithms or protocols guarantee that the group will eventually agree on a single value with certainty. Examples are Paxos, Raft, and Byzantine Fault Tolerance.
  - Probabilistic consensus algorithms or protocols guarantee that the group will agree on a single value with high probability, but not with certainty. Examples are Proof of Work and Proof of Stake.