 Here is the content in Markdown format without any emojis or external links:

### Atomic Commit in Distributed Database system

1. Atomic Commit: It ensures that all distributed transactions are committed successfully or none of them is committed in case of any failure. This property is called Atomicity.
2. Two Phase Commit (2PC): It is a protocol to ensure Atomic Commit and consists of two phases:
- Phase 1: In this phase, the coordinator (one of the servers) asks all participants (other servers) to prepare to commit the transaction. Each participant will indicate to the coordinator if it is ready to commit by voting either 'commit' or 'abort'.
- Phase 2: In this phase, the coordinator makes a final decision based on the votes of Phase 1. It will either commit the transaction by informing all participants or abort the transaction by informing all to roll back.
3. Problem with 2PC: Although 2PC ensures atomic commit, it suffers from certain problems like:
- Blocking: The coordinator may have to wait for participants to respond before moving to the next phase, leading to blocking.
- Single point of failure: Failure of the coordinator results in the protocol halting and transactions remaining in limbo.
4. Three Phase Commit (3PC): 3PC is an extension to 2PC to overcome the problem of single point of failure. It has an extra phase where the coordinator informs all participants about its state. After this, any one of them can take the role of the coordinator and complete the protocol in case the original coordinator fails.

The content is written in a formal tone with points and without any emojis or external links as instructed. Let me know if you would like me to modify or add any other points to the content.