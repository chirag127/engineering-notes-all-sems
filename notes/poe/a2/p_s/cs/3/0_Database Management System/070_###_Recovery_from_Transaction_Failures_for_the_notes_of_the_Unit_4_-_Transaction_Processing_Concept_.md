 Here is the content in markdown format for the topic ### Recovery from Transaction Failures for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System:

## Recovery from Transaction Failures

- Transaction failures can occur due to system crashes, errors, etc. The database state must be restored to a consistent state after such failures.
- The following techniques are used for recovery from transaction failures:

1. **Rollback**: If a transaction fails, the database state is rolled back to the state before the start of the transaction. All the updates performed by the transaction are undone. This ensures consistency but the work done by the transaction is lost.
2. **Commitment Control**: The changes made by a transaction are actually committed to the database only after the transaction completes successfully. This avoids inconsistency in case of failures but increases the time required for commitment as the changes have to be buffered temporarily.
3. **Checkpoints**: The state of the database is saved at specific points in time. In case of a failure, the recovery is done starting from the latest checkpoint rather than from the start of the transaction. This reduces the amount of work required for recovery but requires maintaining checkpoints and updating them periodically.
4. **Shadow Paging**: Updates are written to a temporary area (shadow page) and the original page is updated with the committed changes only. In case of a failure, the original pages can be used to roll back the changes. This avoids the overhead of maintaining checkpoints but requires additional storage space.

- The recovery techniques used depend on the specific requirements and overheads acceptable for the database system. A combination of techniques may also be used to get optimal performance and consistency.

[Diagrams and examples can be added here to explain the concepts in a more understandable way.]

[Additional points on applications and pros and cons of the techniques can be included.]