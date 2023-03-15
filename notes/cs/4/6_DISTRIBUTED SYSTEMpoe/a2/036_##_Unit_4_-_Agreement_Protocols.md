 Here is the content in markdown format for Unit 4 - Agreement Protocols:

## Unit 4 - Agreement Protocols

Agreement protocols are used to achieve consensus in a distributed system. The nodes in the system need to agree upon something, such as:

- Election of a leader
- Ordering of events
- Committing transactions
- Membership changes

Some key agreement protocols are:

1. Raft consensus algorithm:
   - Leader election: Candidates request votes, candidate with majority wins
   - Log replication: Leader replicates log entries to followers, entries committed once majority has them
   - Leader changes: If leader is unresponsive, followers start new election

Advantages:
- Understandable and verifiable
- High availability - cluster can continue operating as long as a majority survives

Disadvantages:
- Slows down with larger clusters due to replication overhead

Mnemonic: "Raft drops logs for committed consistency"

2. Paxos algorithm:
   - Proposers propose values, acceptors determine if proposal has quorum to be accepted
   - Chosen proposal is the highest proposal number that has been accepted by a quorum of acceptors
   - Additional "learners" can detect chosen proposal and apply value

Advantages:
- Can be adapted for different use cases (multi-Paxos)
- Decentralized, no single point of failure

Disadvantages:
- Complex to understand and implement
- Inefficient with multiple proposers simultaneously proposing

Application: Used in distributed databases for replication and consistency

[Additional details, diagrams, examples, etc. can be added here]