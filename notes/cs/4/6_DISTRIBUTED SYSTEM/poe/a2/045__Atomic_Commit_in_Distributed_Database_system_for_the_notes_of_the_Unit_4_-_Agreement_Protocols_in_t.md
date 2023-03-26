 Here is the content in Markdown format without any emojis or external links:

### Atomic Commit in Distributed Database system

1. Atomic Commit: It refers to executing a distributed transaction either completely or not at all. The transaction must commit on all sites or rollback on all sites.
2. Two-phase commit protocol: It is a basic protocol to achieve atomic commitment of transactions. It consists of two phases:
- Commit-Request phase: The coordinator asks all participants to prepare to commit. If all participants respond positively, the coordinator asks them to commit. Otherwise, it asks them to abort.
- Commit phase: The participants commit the transaction on the coordinator's request.
3. Advantages: Ensures ACID properties. The database remains consistent even after a failure.
4. Limitations: The protocol is blocking. The coordinator has to wait for responses from all participants before moving to the next phase. This can lead to performance bottlenecks. Also, if the coordinator fails after the commit request phase, some participants may commit while others may abort leading to inconsistency.

The points are written in a formal tone without any emojis or external links as per the given instructions. The content is written in Markdown format and adheres to the given topic - Atomic Commit in Distributed Database system for the notes of Unit 4 - Agreement Protocols in DISTRIBUTED SYSTEM. Please let me know if you would like me to modify or expand the content.