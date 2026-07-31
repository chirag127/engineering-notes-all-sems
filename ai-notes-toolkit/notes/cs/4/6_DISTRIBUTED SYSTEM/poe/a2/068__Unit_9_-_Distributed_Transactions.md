 Here is the content in markdown format with formal tone and without external links or emojis:

## Unit 9 - Distributed Transactions

1. Distributed transactions involve multiple parties and resources. They must satisfy ACID properties:
 - Atomicity: Either all steps succeed or all fail
 - Consistency: Data is consistent across resources
 - Isolation: Transactions are isolated from each other
 - Durability: Changes persist even after failures
2. Two-phase commit protocol coordinates commits across multiple resources:
 - Phase 1: Participants prepare to commit
 - Phase 2: Coordinator commits if all participants prepared to commit
 - If any participant aborts in Phase 1, the coordinator aborts all participants
3. Challenges with distributed transactions:
 - Latency in communication can lead to temporary inconsistency
 - Partial failures can lead to transaction abortion even if some parties succeed
 - Complexity of coordination across multiple resources and parties
4. Alternative approaches with eventual consistency relax ACID rules:
 - Replicated data with asynchronous propagation of updates
 - Compensating transactions to undo effects of failed transactions
 - Limited scope of transactions to reduce coordination needs

Does this meet your requirements? Let me know if you would like me to modify or expand the content in any way.