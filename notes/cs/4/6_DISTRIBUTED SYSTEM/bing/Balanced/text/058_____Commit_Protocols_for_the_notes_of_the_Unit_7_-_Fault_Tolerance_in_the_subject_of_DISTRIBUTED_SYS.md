### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are algorithms that ensure the atomicity of distributed transactions, i.e., all the sites involved in a transaction either commit or abort it unanimously, even in the presence of failures  .
- Commit protocols are necessary to maintain the consistency and reliability of distributed systems, as they prevent partial execution or data loss due to network or site failures  .
- There are different types of commit protocols, such as one-phase commit (1PC), two-phase commit (2PC), and three-phase commit (3PC), each with its own advantages and disadvantages    .
- One-phase commit (1PC) is the simplest commit protocol, where a coordinator sends a commit or abort message to all the participating sites, and they execute the transaction accordingly .
  - The advantage of 1PC is that it is fast and simple, as it requires only one round of communication .
  - The disadvantage of 1PC is that it is not fault-tolerant, as a single failure of the coordinator or a site can cause inconsistency or data loss .
- Two-phase commit (2PC) is the most widely used commit protocol, where a coordinator initiates a voting phase and a decision phase to reach a consensus among the participating sites    .
  - In the voting phase, the coordinator sends a prepare message to all the sites, and they reply with a yes or no vote, indicating whether they are ready to commit or abort the transaction    .
  - In the decision phase, the coordinator collects the votes and decides to commit or abort the transaction based on the majority. It then sends a commit or abort message to all the sites, and they execute the transaction accordingly    .
  - The advantage of 2PC is that it is fault-tolerant, as it ensures that all the sites agree on the same outcome, and it uses a log to recover from failures    .
  - The disadvantage of 2PC is that it is blocking, as a failure of the coordinator or a site can cause the other sites to wait indefinitely for a decision    .
- Three-phase commit (3PC) is an extension of 2PC, where a coordinator adds a pre-commit phase between the voting phase and the decision phase to avoid blocking .
  - In the pre-commit phase, the coordinator sends a pre-commit message to all the sites that voted yes in the voting phase, and they reply with an acknowledgment, indicating that they are ready to commit the transaction .
  - In the decision phase, the coordinator sends a commit or abort message to all the sites, and they execute the transaction accordingly .
  - The advantage of 3PC is that it is non-blocking, as it allows the sites to decide on their own in case of a coordinator failure, based on a timeout mechanism .
  - The disadvantage of 3PC is that it is more complex and costly, as it requires an extra round of communication and more log entries .