# Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for commit protocols is to maintain the atomicity of distributed transactions .
- A distributed transaction is a transaction that involves multiple database sites that may be geographically dispersed.
- A commit protocol is a set of rules that ensures that either all the changes made by a distributed transaction are committed at all the sites, or none of them are.
- Atomic commitment issue is of prime importance in the distributed system and the issue becomes more necessary to deal with if some of the sites participating in the execution of the transaction commitment fail .
- There are two main types of commit protocols: blocking and non-blocking .
- Blocking protocols are those that may block the progress of the transaction if a site fails during the commit process .
- Non-blocking protocols are those that do not block the progress of the transaction even if a site fails during the commit process .
- The most common blocking protocol is the two-phase commit protocol (2PC), which consists of two phases: a prepare phase and a commit phase.
- The most common non-blocking protocol is the three-phase commit protocol (3PC), which consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
- There are also other variations and optimizations of commit protocols, such as the failure-aware atomic commit protocol (FLAC), which aims to reduce the latency and abort rate of distributed transactions.
- There are also different ways to integrate commit protocols with other aspects of distributed database systems, such as concurrency control, replication, and recovery.