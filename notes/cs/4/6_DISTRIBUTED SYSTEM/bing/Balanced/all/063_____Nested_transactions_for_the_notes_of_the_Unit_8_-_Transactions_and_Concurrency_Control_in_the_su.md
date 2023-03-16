# Nested Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- A transaction is a unit of work that performs some operations on data and either commits or aborts as a whole.
- A nested transaction is a transaction that is composed of subtransactions, each of which may have its own commit or abort point.
- A nested transaction can be used to improve the performance, reliability, and modularity of distributed systems.
- A nested transaction can be classified into two types: closed nested transactions and open nested transactions.
- A closed nested transaction is a transaction that can only commit or abort as a whole, and its subtransactions are not visible to other transactions until the parent transaction commits.
- A closed nested transaction preserves the ACID properties of a flat transaction, but it may incur more overhead and locking than a flat transaction.
- A closed nested transaction can be implemented using a two-phase commit protocol, where the parent transaction coordinates the commit or abort of its subtransactions.
- A closed nested transaction can be represented by a tree structure, where the root node is the parent transaction and the leaf nodes are the subtransactions.
- A closed nested transaction can be serialized by using a serialization graph, where the nodes are the transactions and the edges are the conflicts between them.
- A conflict between two transactions occurs when they access the same data item and at least one of them writes to it.
- A serialization graph for nested transactions is acyclic if and only if the transactions are conflict-serializable, meaning that they can be executed in some order that is equivalent to a serial execution.
- A serialization graph for nested transactions can be tested by using a depth-first search algorithm, where the transactions are visited in a preorder traversal of the tree structure.
- An example of a closed nested transaction is shown below:

![Closed nested transaction](https://i.imgur.com/0y0fJZS.png)

- An open nested transaction is a transaction that allows some of its subtransactions to commit or abort independently, and their effects are visible to other transactions before the parent transaction commits.
- An open nested transaction relaxes the ACID properties of a flat transaction, but it may improve the concurrency, availability, and scalability of distributed systems.
- An open nested transaction can be implemented using a compensation-based protocol, where the parent transaction records the compensating actions for each subtransaction that commits.
- A compensating action is an action that reverses the effect of a committed subtransaction in case the parent transaction aborts.
- A compensating action must be idempotent, meaning that it can be executed multiple times without changing the outcome.
- A compensating action must be commutative, meaning that it can be executed in any order with other compensating actions without changing the outcome.
- A compensating action must be consistent, meaning that it preserves the integrity constraints of the data.
- An open nested transaction can be represented by a directed acyclic graph, where the nodes are the transactions and the edges are the dependencies between them.
- A dependency between two transactions occurs when one transaction reads or writes a data item that is written by another transaction.
- An open nested transaction can be serialized by using a topological sorting algorithm, where the transactions are ordered according to their dependencies.
- An example of an open nested transaction is shown below:

![Open nested transaction](https://i.imgur.com/0y0fJZS.png)