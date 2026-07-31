## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state or value.
- Consensus is essential for distributed systems that need to coordinate their actions and ensure consistency and reliability.
- Consensus can be achieved by various algorithms or protocols, such as Paxos, Raft, Byzantine Fault Tolerance, Proof of Work, Proof of Stake, etc.
- Consensus algorithms or protocols have different properties and trade-offs, such as fault tolerance, availability, latency, scalability, security, etc.
- Consensus algorithms or protocols can be classified into two categories: leader-based and leaderless.
  - Leader-based consensus algorithms or protocols elect a leader or a set of leaders to propose and commit values, and the other participants follow the leader(s).
  - Leaderless consensus algorithms or protocols allow any participant to propose and commit values, and the participants reach agreement through some form of voting or validation.
- Consensus algorithms or protocols can also be classified into two categories: deterministic and probabilistic.
  - Deterministic consensus algorithms or protocols guarantee that the participants will eventually agree on the same value with certainty, as long as some assumptions are met, such as a majority of honest participants, bounded network delays, etc.
  - Probabilistic consensus algorithms or protocols guarantee that the participants will agree on the same value with high probability, but not with certainty, as there may be some scenarios where the participants diverge or disagree, such as network partitions, malicious attacks, etc.