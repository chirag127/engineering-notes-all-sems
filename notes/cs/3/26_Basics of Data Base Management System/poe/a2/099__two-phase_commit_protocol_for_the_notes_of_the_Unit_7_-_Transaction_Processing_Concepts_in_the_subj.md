 Here is the content in Markdown format without emojis or external links and in a formal tone:

### Two-Phase Commit Protocol

1. Transaction manager proposes commit to all resource managers. Each resource manager votes either commit or abort based on whether it can commit the transaction or not.
2. If all resource managers vote commit, then the transaction manager issues a commit decision and the transaction commits successfully.
3. If any one resource manager votes abort, then the transaction manager issues an abort decision and the transaction is aborted. All the updates by the transaction are rolled back to the original state.
4. The two phases are -

1. Voting phase - Each resource manager votes either commit or abort.
2. Decision phase - Based on the votes, the transaction manager makes the final decision to either commit or abort the transaction.

The two-phase commit protocol ensures that all the resource managers commit or abort the transaction in an atomic manner, maintaining the ACID properties of the transaction. It handles the situation where different resource managers have different opinions regarding the outcome of the transaction.

The key advantages of the two-phase commit protocol are:

1. Atomicity - Either all resource managers commit or all abort, thereby preserving atomicity.
2. Consistency - The database is always in a consistent state as the transaction follows the ACID properties.
3. Durability - Once a transaction is committed, it is guaranteed to persist even in the event of a system failure.

The two-phase commit protocol ensures data integrity by maintaining database consistency even in a distributed database system with multiple resource managers.