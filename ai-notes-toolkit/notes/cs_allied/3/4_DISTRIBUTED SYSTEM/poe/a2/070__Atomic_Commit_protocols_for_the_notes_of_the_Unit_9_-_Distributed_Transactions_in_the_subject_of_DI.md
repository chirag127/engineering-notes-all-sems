 Here is the formal content in Markdown format without any emojis or external links on the topic "Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM":

### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

1. Atomic Commit Protocol: It is a protocol which ensures that all the distributed transactions are committed successfully or aborted successfully but not left in an intermediate state. It provides atomicity to the distributed transactions.
2. Two Phase Commit (2PC) protocol: It is the most popular atomic commitment protocol which uses two phases to commit a distributed transaction:
- Phase 1: In the prepare phase, the coordinator asks all the participating sites whether they are ready to commit the transaction. If all the sites vote to commit, the transaction enters phase 2. If any site votes to abort, the transaction is aborted.
- Phase 2: In the commit phase, the coordinator informs all the sites to commit the transaction. If all the acknowledgments are received, the transaction is committed. If any site fails to acknowledge, the transaction is aborted.
3. Three Phase Commit (3PC) protocol: It is an extension of 2PC protocol. It adds an extra phase to handle the site or coordinator failures. The three phases are:
- Phase 1: Same as the prepare phase of 2PC
- Phase 2: The coordinator commits the transaction and informs all the sites. The sites acknowledge the commit request but do not actually commit.
- Phase 3: The coordinator informs all the sites to really commit. If all the acknowledgments are received, the transaction is committed. If any site fails to acknowledge, the transaction is aborted.

The content summarizes the key points around Atomic Commit protocols with relevant examples. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.