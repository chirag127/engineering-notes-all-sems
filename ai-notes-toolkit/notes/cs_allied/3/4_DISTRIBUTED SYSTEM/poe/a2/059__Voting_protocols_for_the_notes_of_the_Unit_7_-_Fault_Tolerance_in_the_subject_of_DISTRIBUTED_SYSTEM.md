 Here is the content in markdown format without any emojis or external links:

### Voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM.

1. Primary-backup approach: In this approach, one replica is designated as the primary and others act as backups. The primary handles all client requests as long as it is functioning. If the primary fails, one of the backups is elected as the new primary.
2. Consensus approach: In this approach, all replicas are equivalent and a consensus protocol is used to ensure that they agree on the state updates. For example, a majority consensus protocol can be used where an update is accepted only if a majority of replicas agree to it. This approach does not require a designated primary and can tolerate failures of minority of replicas.
3. Quorum-based approach: In this approach, the replicas are organized into multiple quorums. Read and write operations are performed on a quorum of replicas. As long as a quorum of replicas is functioning, the system can continue to operate. The quorums can be overlapping or non-overlapping.
4. Leader-based approach: In this approach, one of the replicas is elected as the leader. The leader handles all client requests and replicates updates to the followers. If the leader fails, another replica is elected as the new leader. This approach ensures strong consistency but can suffer from latency in electing a new leader.

The content is written in a formal tone without any feelings or friendliness as required. The points are written in a way to serve as study material to learn the topic. Please let me know if you would like me to modify or add anything to the content.