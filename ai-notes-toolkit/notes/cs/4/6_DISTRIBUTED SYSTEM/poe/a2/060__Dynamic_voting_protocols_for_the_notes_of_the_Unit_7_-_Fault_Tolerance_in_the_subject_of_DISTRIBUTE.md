 Here is the content in Markdown format without emojis and external links:

### Dynamic voting protocols

- Fault tolerance is achieved in distributed systems using replication and consensus protocols.
- Consensus protocols help replicas agree on a value even with failures and network delays.
- Two phase commit is a blocking consensus protocol which waits for all replicas to commit. This can lead to scalability issues.
- Non-blocking consensus protocols like Paxos allow replicas to commit independently and achieve higher throughput.
- Paxos has a Leader election phase to elect a proposer and then a Convention phase where proposals are accepted by a majority of replicas.
- Viewstamped replication is an optimization of Paxos which decouples leader election from the convention phase leading to better performance.
- Practical Byzantine fault tolerance (PBFT) is another non-blocking consensus protocol that can tolerate Byzantine faults with malicious replicas. It uses three phase commit - Pre-prepare, Prepare, Commit.
- These dynamic voting protocols allow the replicas to change leaders and adapt to changes, network delays and failures to achieve fault tolerance and consistency in a scalable manner.

The content summarizes some key points about dynamic voting protocols for fault tolerance in distributed systems. It covers concepts like two phase commit, Paxos, viewstamped replication and PBFT in a formal tone with points and without emojis or external links as desired. Please let me know if you would like me to modify or expand the answer.