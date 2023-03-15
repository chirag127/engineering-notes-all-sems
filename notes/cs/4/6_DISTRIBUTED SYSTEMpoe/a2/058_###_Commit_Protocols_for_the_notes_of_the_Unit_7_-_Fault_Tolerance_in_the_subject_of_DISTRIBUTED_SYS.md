 Here is the content in markdown format for the topic ### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM:

### Commit Protocols

Commit protocols are used to achieve consensus in a distributed system and ensure that all replicas have the same data. This is required for fault tolerance. Some of the commit protocols are:

- Two-phase commit:

- Consists of two phases: commit request and commit phase
- In commit request phase, the coordinator ( usually the client) asks all participants (servers) to prepare to commit
- In commit phase, if all participants respond with prepared to commit in phase 1, the coordinator commits the transaction, else it aborts
- Ensures atomicity but reduces performance due to two phases
- Can lead to blocking if any participant fails

- Three-phase commit:

- Adds a pre-commit phase before the two phases of two-phase commit
- The pre-commit phase allows early detection of failure and reduces blocking
- However, it reduces performance further due to an additional phase

**Mnemonics:**

Two-phase like two steps to ensure atomicity

Three-phase for early failure detection and less blocking

**Advantages:**

- Ensure data consistency across replicas
- Atomicity of transactions is guaranteed

**Disadvantages:**

- Reduction in performance due to multiple phases
- Blocking can occur if any participant fails

**Applications:** Database systems, transaction processing systems

The above points can be helpful to learn and remember the key points about commit protocols. The markdown formatting makes the content easy to read. Let me know if you would like me to elaborate on any part of the content.