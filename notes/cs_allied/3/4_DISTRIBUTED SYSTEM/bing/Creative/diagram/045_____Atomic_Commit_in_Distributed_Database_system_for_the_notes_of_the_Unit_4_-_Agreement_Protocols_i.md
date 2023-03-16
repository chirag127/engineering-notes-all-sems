### Atomic Commit in Distributed Database System

- An atomic commit is an operation that applies a set of distinct changes as a single operation.
- If the changes are applied, then the atomic commit is said to have succeeded. If the changes are not applied, then the atomic commit is said to have failed or aborted.
- In distributed database systems, the primary need for atomic commit protocols is to maintain the atomicity of distributed transactions .
- Atomicity is the property that ensures that either all the data changes made by a transaction are committed or none of them are.
- Atomicity is important for ensuring the consistency and reliability of the distributed database system.
- Atomic commit protocols are algorithms that coordinate the commit or abort decisions of multiple sites that participate in a distributed transaction.
- Atomic commit protocols can be classified into two categories: blocking and non-blocking .
- Blocking protocols are those that require some sites to wait for the recovery of other failed sites before making a final decision .
- Non-blocking protocols are those that allow some sites to make a final decision without waiting for the recovery of other failed sites .
- Blocking protocols are simpler and more efficient in normal situations, but they may cause unnecessary delays or deadlocks in case of failures .
- Non-blocking protocols are more complex and less efficient in normal situations, but they can tolerate failures better and avoid delays or deadlocks .
- Some examples of blocking protocols are two-phase commit (2PC), three-phase commit (3PC), and presumed commit (PC) .
- Some examples of non-blocking protocols are presumed abort (PA), presumed nothing (PN), and failure-aware atomic commit (FLAC)  .