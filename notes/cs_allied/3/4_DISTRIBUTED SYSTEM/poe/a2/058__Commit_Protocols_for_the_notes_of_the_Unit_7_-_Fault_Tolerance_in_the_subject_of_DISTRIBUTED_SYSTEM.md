 Here is the content in markdown format without any emojis or external links and in formal tone:

### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

1. Two-phase commit protocol:
- Coordinator node is responsible for commit decision.
- In the first phase, coordinator asks all participants to prepare to commit. On preparing, participants record the transaction in their local logs but do not commit.
- In the second phase, if all participants respond with prepared status, coordinator asks all to commit. If any participant fails in the first phase, coordinator asks all to rollback the transaction.
- The protocol ensures atomicity i.e. either all participants commit or rollback the transaction. However, it reduces performance due to two rounds of messages.

2. Three-phase commit protocol:
- Also has a coordinator node.
- In the first phase, coordinator asks all participants to prepare to commit.
- In the second phase, participants vote either to commit or abort.
- In the third phase, coordinator decides on the final outcome based on votes:
-- If all votes are to commit, it asks participants to commit.
-- If any vote is to abort, it asks participants to rollback.
- The three phases ensure that the coordinator takes the decision only after collecting the votes to improve performance. However, it requires more messages than two-phase commit leading to more overhead.

3. Commit protocols for distributed databases:
- Variations of two-phase and three-phase commit protocols are used for commit coordination in distributed databases.
- These protocols are optimized for database transactions with features like batching of commit requests, piggybacking,etc. to improve performance.
- Examples are protocols used in databases like Oracle RAC, MySQL Cluster,etc.

The content summarizes three main commit protocols for distributed systems and databases. Please let me know if you would like me to elaborate on any part of the content.