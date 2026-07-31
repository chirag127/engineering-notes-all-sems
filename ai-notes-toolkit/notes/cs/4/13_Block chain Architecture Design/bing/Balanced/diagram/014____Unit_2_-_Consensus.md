## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state or value.
- Consensus is essential for distributed systems that need to coordinate their actions and maintain consistency across replicas or nodes.
- Consensus can be achieved by various algorithms or protocols, such as Paxos, Raft, Byzantine Fault Tolerance, Proof of Work, Proof of Stake, etc.
- Consensus algorithms or protocols have different properties and trade-offs, such as fault tolerance, availability, latency, scalability, security, etc.
- Consensus algorithms or protocols can be classified into two categories: leader-based and leaderless.
  - Leader-based consensus algorithms or protocols elect a leader or a coordinator among the participants, who is responsible for proposing and committing values. Examples are Paxos and Raft.
  - Leaderless consensus algorithms or protocols do not rely on a leader or a coordinator, but rather allow participants to propose and commit values independently. Examples are Byzantine Fault Tolerance and Proof of Work.
- Consensus algorithms or protocols can also be classified into two categories: deterministic and probabilistic.
  - Deterministic consensus algorithms or protocols guarantee that the participants will eventually agree on the same value with certainty. Examples are Paxos, Raft, and Byzantine Fault Tolerance.
  - Probabilistic consensus algorithms or protocols guarantee that the participants will agree on the same value with high probability, but not with certainty. Examples are Proof of Work and Proof of Stake.