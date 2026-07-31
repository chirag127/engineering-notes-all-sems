 Here is the content in markdown format without any emojis or external links:

### Flat and nested distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

1. Flat transactions: Transactions that involve only a single site or single node in a distributed system. They follow ACID properties within a single node.

2. Nested transactions: When a transaction at one site spawns one or more subtransactions that are sent to other sites. The toplevel transaction is committed only if all subtransactions commit. Managing the commit of subtransactions is complex.

3. Distributed transactions: Transactions that access data on two or more networked nodes. They must maintain ACID properties across the entire distributed system.

4. Commit protocols: Mechanisms to coordinate commit decisions for distributed transactions. They ensure consistency across distributed nodes.

- Two phase commit: A popular protocol with two phases - (1) Commit request phase: Coordinator asks participants to prepare to commit. (2) Commit phase: Coordinator commits if all participants are ready, else rolls back.

- Three phase commit: Adds an abort phase to handle failures. More robust but has higher overhead.

The content aims to write the study notes in a formal tone with points in a markdown format without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content.