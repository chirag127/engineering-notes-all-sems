 Here is the content in markdown format without any emojis or external links:

### Testing of Serializability for the notes of the Unit 7 - Transaction Processing Concepts

1. Serializability: A schedule is serializable if it is equivalent to some serial schedule. That means, the end result of the schedule should be same as some serial execution of the transactions.
2. Conflicts: Two transactions are said to be in conflict if they access the same data item and at least one of them is a write.
3. Conflict graphs: A conflict graph can be constructed with transactions as nodes and edges as conflicts between transactions. A schedule is serializable if and only if its conflict graph is acyclic.
4. View serializability: A weaker form of serializability which ignores the timing of write operations and considers two writes to be in conflict only if they are to the same data item. A schedule is view serializable if its view conflict graph is acyclic. View serializability can lead to anomalies.
5. Recoverability: A schedule has the recoverability property if the end state it produces can also be reached by some serial schedule. Recoverability avoids the problems of view serializability by not ignoring the timing of writes.
6. Cascading rollbacks: If a transaction T1 reads an uncommitted data item written by another transaction T2, and if T2 aborts later, then T1 also has to abort. This may lead to a chain of rollbacks or cascading rollbacks. Strict two phase locking avoids cascading rollbacks.

The content is written in points and in a formal tone with markdown formatting and without any emojis or external links as per the instructions. Please let me know if you would like me to modify or expand the content in any way.