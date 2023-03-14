### Flat and nested distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A distributed transaction is a transaction that accesses objects managed by multiple servers .
- A distributed transaction must maintain the ACID properties of a transaction, especially atomicity, which means that either all of the servers commit the transaction or all of them abort the transaction .
- A distributed transaction can be structured in two different ways: flat or nested .
- A flat transaction has a single initiating point (Begin) and a single end point (Commit or Abort) .
- A flat transaction is usually simple and short, and it performs operations on objects in a sequential order .
- A flat transaction can use the two-phase commit protocol to coordinate the commit or abort decision among the servers.
- A nested transaction is a transaction that contains subtransactions, which can be either distributed or local .
- A nested transaction has a hierarchical structure, where the root transaction is the parent of all subtransactions, and each subtransaction can have its own subtransactions .
- A nested transaction can have partial commits, where some subtransactions can commit independently of the others, as long as they do not violate the consistency of the data .
- A nested transaction can use the nested two-phase commit protocol or the multilevel commit protocol to coordinate the commit or abort decision among the servers.

Mnemonics and learning tricks:

- To remember the difference between flat and nested transactions, think of a flat transaction as a straight line and a nested transaction as a tree.
- To remember the two-phase commit protocol, think of the two phases as "prepare" and "commit/abort", where the coordinator asks the servers to prepare for the decision, and then tells them to commit or abort based on the majority vote.
- To remember the nested two-phase commit protocol, think of the two phases as "prepare" and "commit/abort", where the coordinator asks the subtransactions to prepare for the decision, and then tells them to commit or abort based on the parent transaction's decision.
- To remember the multilevel commit protocol, think of the levels as the levels of the nested transaction hierarchy, where each level has its own coordinator and its own two-phase commit protocol.