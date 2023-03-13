### Atomic Commit in Distributed Database System

- An atomic commit protocol (ACP) is a distributed algorithm used to ensure the atomicity property of transactions in distributed database systems  .
- Atomicity means that either all the operations of a transaction are executed successfully, or none of them are executed at all.
- Atomicity is one of the ACID properties of transactions, along with consistency, isolation, and durability.
- Atomic commit protocols are needed to coordinate the commit or abort decisions of multiple sites that participate in a distributed transaction  .
- Atomic commit protocols must deal with the possibility of site failures, network failures, or communication delays that may affect the outcome of a distributed transaction  .
- Atomic commit protocols can be classified into two main categories: blocking and non-blocking .
- Blocking protocols are those that require some sites to wait for the recovery of other sites before making a final decision .
- Non-blocking protocols are those that allow some sites to proceed with their decision without waiting for the recovery of other sites .
- Blocking protocols are simpler and more efficient than non-blocking protocols in normal situations, but they may cause long delays or deadlocks in case of failures .
- Non-blocking protocols are more resilient and fault-tolerant than blocking protocols, but they may incur more overhead and complexity in normal situations .
- Some examples of blocking protocols are the two-phase commit protocol (2PC) and the three-phase commit protocol (3PC).
- Some examples of non-blocking protocols are the presumed abort protocol (PA), the presumed commit protocol (PC), and the failure-aware atomic commit protocol (FLAC)  .
- The choice of an atomic commit protocol depends on the trade-off between performance, availability, and reliability of the distributed database system  .