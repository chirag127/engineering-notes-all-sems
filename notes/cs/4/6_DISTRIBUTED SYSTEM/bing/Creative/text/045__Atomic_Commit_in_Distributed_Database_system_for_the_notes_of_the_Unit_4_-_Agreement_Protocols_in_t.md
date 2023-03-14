### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation. If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, where transactions may span multiple sites, atomic commit protocols (ACPs) are used to ensure the atomicity property of transactions, which means that either all the changes of a transaction are committed at all sites, or none of them are .
- ACPs involve a coordinator site and one or more worker sites that participate in a transaction. The coordinator is responsible for collecting the results from the workers and making a final decision to commit or abort the transaction. The workers are aware of the coordinator and communicate their results and follow the coordinator's decision .
- ACPs have two main phases: a prepare phase and a commit phase. In the prepare phase, the coordinator asks the workers to vote on whether they are ready to commit or not. In the commit phase, the coordinator decides based on the votes and informs the workers of the decision .
- ACPs have different variants and optimizations to deal with different scenarios and requirements, such as failures, concurrency, performance, and consistency. Some of the common ACPs are:
  - Two-phase commit (2PC): The basic ACP that uses two phases and ensures atomicity in the presence of failures, but may block if the coordinator fails .
  - Three-phase commit (3PC): An extension of 2PC that uses a third phase to avoid blocking in case of failures, but may incur more overhead and latency .
  - Presumed abort (PA): An optimization of 2PC that reduces the log complexity by assuming that transactions abort by default unless they are explicitly committed .
  - Presumed commit (PC): An optimization of 2PC that reduces the log complexity by assuming that transactions commit by default unless they are explicitly aborted .
  - Non-blocking commit (NBC): A class of ACPs that do not block in case of failures and can make progress with a majority of sites.
  - Nested commit (NC): A class of ACPs that support nested transactions, where a transaction can spawn subtransactions that can be committed independently .