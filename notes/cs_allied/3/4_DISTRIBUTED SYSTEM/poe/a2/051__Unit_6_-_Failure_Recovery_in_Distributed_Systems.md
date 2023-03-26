 Here is the content in markdown format without any external links or emojis:

## Unit 6 - Failure Recovery in Distributed Systems

1. Failure Detection - Failure detection refers to the techniques and mechanisms used by distributed systems to detect the occurrence of faults or failures. This is a crucial task as the system must be aware of any failures or faults before it can proceed with failure recovery. Some common failure detection techniques are:
- Heartbeat Monitoring - Nodes periodically send heartbeat messages to inform other nodes about their health. Failure is detected if heartbeat messages are not received within a specified time interval.
- Timeout-based Detection - Expectations of response/arrival of messages or signals within a certain time period. Failure is detected if timeout expires without the expected response.
- Byzantine Fault Detection - More complex technique to detect arbitrary or malicious failures in presence of adversarial nodes.

2. Failure Recovery - The goal of failure recovery is to perform necessary actions to maintain system availability and consistency in the event of node failures. Common approaches include:
- Redundancy - Presence of backup components or replicas of resources to take over in event of failure.
- Checkpointing - Periodically saving state of a system so that it can roll back to a previous correct state in case of failure.
- Replication - Maintaining multiple copies of resources/data and using consensus to keep them consistent. Upon failure, remaining replicas can continue providing service.
- Rollback Recovery - Rolling back a system to a previously recorded correct state and re-executing operations.

3. consensus - Consensus is a crucial aspect of failure recovery to maintain consistency between system replicas/components. Consensus allows the system to agree on a certain state being reflected across all nodes. Popular consensus protocols include Paxos, Raft, and ZAB.

The content is written in a formal tone with points and without any external links or emojis as instructed. Please let me know if you would like me to modify or expand the content in any way.