 Here is the content in markdown format with formal tone and without emojis or external links:

## Unit 6 - Failure Recovery in Distributed Systems

1. Failure Models
- Crash failures: Nodes fail by crashing. They cease to respond to other nodes.
- Byzantine failures: Nodes may exhibit arbitrary behavior. They may send arbitrary messages to other nodes, deviate from prescribed protocols, etc. These are the most difficult to deal with.

2. Replication
- Replication is a key technique for failure recovery. The system maintains multiple replicas of data/services so that in the event of failures, others can take over.
- Strong consistency: All replicas must agree on updates (sequentially update replicas).
- Eventual consistency: Replicas may differ temporarily, but will eventually converge to the same value.

3. Leader election
- In replicated systems, a leader is often designated to coordinate actions or provide a single system view.
- The leader election problem is to select a process from a group of processes on different processors to act as the leader.
- The leader election algorithm must be robust to changes in system membership (nodes joining/leaving) and failures.

[Further points on consensus, distributed transactions, etc.]

The content is written in a formal manner with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer in any way.