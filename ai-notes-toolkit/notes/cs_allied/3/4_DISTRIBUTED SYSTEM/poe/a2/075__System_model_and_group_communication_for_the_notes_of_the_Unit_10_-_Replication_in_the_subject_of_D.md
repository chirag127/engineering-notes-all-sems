 Here is the formal content in Markdown format without any emojis or external links:

### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

1. System Model: A distributed system consists of multiple autonomous computers that communicate and coordinate their actions only by passing messages.

2. Group Communication: Group communication is a key building block for implementing distributed systems. It provides a communication abstraction that allows a set of processes to deliver messages reliably.

3. Atomicity: All processes in a group must commit to a transaction or none do. If any process fails, the transaction aborts and has no effect.

4. Consistency: All processes in a group must see transactions in the same order. The order can be defined by a consistency condition such as last-writer-wins or first-writer-wins.

5. Isolation: Transactions performed in a group must be isolated from one another. No transaction can interfere with another transaction until the other is committed.

6. Durability: Once a transaction is committed, it will persist even in the face of failures. The state changes made by a committed transaction must be installed on stable storage.

This formal content covers the key points on System Model, Group Communication and its properties (Atomicity, Consistency, Isolation, Durability) for replication in Distributed Systems. The points are written concisely in a bulleted list format without any informal language or external links to serve as formal study notes.