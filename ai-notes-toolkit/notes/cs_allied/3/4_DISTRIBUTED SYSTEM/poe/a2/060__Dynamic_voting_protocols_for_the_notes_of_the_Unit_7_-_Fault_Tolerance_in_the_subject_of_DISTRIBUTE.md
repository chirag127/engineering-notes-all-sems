 Here is the content in markdown format without any emojis or external links:

### Dynamic voting protocols

- Replication is used to achieve fault tolerance in distributed systems. Multiple replicas of the same data are maintained at different nodes.
- In case of a failure, one of the replicas can be used. However, this leads to the challenge of maintaining consistency between the replicas.
- Voting protocols are used to resolve conflicts between the replicas in a consistent manner. They work by selecting a winner among the values proposed by different replicas.
- Static voting: A fixed majority quorum is decided in advance. As long as a majority of the replicas are correct, the correct value will win. However, if the quorum is not met due to failures, the system becomes unavailable.
- Dynamic voting: The quorum is dynamically reconfigured based on failures. The system can continue to function as long as there are enough correct replicas, even if a majority is lost. The challenge is to ensure that the reconfigured quorum always contains a majority of correct replicas.
- Examples of dynamic voting protocols:
-- Adjusted winner: The replica with the highest version number wins. In case of a tie, previous winner is chosen.
-- Hierarchical quorum consensus: A hierarchy of quorums is maintained. If a lower-level quorum is lost, higher-level quorum is used.
-- Partitionable quorum systems: The system is split into partitions containing a majority of replicas. As long as one partition survives, the system continues to function.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.