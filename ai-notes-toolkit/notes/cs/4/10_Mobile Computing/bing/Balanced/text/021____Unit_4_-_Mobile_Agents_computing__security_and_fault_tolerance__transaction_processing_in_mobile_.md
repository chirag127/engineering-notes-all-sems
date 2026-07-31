## Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are software entities that can autonomously migrate from one host to another in a network, carrying their code and state with them.
- Mobile agents can be used for various applications, such as distributed information retrieval, electronic commerce, network management, and load balancing.
- Mobile agents face several challenges, such as security, fault tolerance, and transaction processing, which need to be addressed for their successful deployment.

### Security
- Security is a major concern for mobile agents, as they may encounter malicious hosts or other agents that can tamper with their code, data, or execution.
- Some of the security threats for mobile agents are:
  - Code tampering: modifying the agent's code to alter its functionality or behavior.
  - Data tampering: modifying the agent's data to corrupt its state or results.
  - Eavesdropping: intercepting the agent's communication or accessing its private data.
  - Repudiation: denying the agent's actions or transactions.
  - Masquerading: impersonating the agent or its owner.
  - Denial of service: preventing the agent from completing its task or returning to its owner.
- Some of the security techniques for mobile agents are:
  - Encryption: encrypting the agent's code, data, or communication to prevent unauthorized access or modification.
  - Authentication: verifying the identity and integrity of the agent or its owner using digital signatures, certificates, or passwords.
  - Authorization: granting or denying access rights to the agent or its resources based on predefined policies or rules.
  - Auditing: logging the agent's actions or transactions for accountability or verification purposes.
  - Sandbox: isolating the agent's execution environment from the host system to limit its access or impact.
  - Obfuscation: hiding or obscuring the agent's code or data to make it difficult to analyze or modify.

### Fault tolerance
- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures or errors.
- In mobile agent computing, any component of the network - node, link, or agent - may fail at any time, thus preventing the agent from continuing its execution or returning its results.
- Some of the fault tolerance techniques for mobile agents are:
  - Replication: creating multiple copies of the agent and executing them on different hosts to increase the probability of success or reduce the response time.
  - Checkpointing: saving the agent's state periodically or at strategic points to enable its recovery or restart in case of failure.
  - Recovery: restoring the agent's state from a checkpoint or a replica and resuming its execution from the point of failure.
  - Migration: moving the agent from a faulty or overloaded host to another host to avoid or escape from failure.
  - Rejuvenation: refreshing or renewing the agent's code or data to prevent or correct errors or degradation.

### Transaction processing
- Transaction processing is the execution of a series of operations that form a logical unit of work, such as a database query, a payment, or a reservation.
- Transactions have four properties: atomicity, consistency, isolation, and durability (ACID), which ensure the correctness and reliability of the operations and their results.
- In mobile agent computing, transaction processing is challenging, as the agent may visit multiple hosts, interact with multiple resources, and encounter failures or concurrency issues during its execution.
- Some of the transaction processing techniques for mobile agents are:
  - Two-phase commit: coordinating the commitment or abort of a transaction among multiple participants using a prepare and a commit phase.
  - Nested transactions: structuring a transaction as a hierarchy of subtransactions, each with its own ACID properties, to allow partial commitment or abort.
  - Sagas: decomposing a transaction into a sequence of compensatable actions, each with a corresponding undo action, to allow partial rollback or recovery.
  - Optimistic concurrency control: allowing concurrent execution of transactions without locking, and detecting and resolving conflicts at commit time.
  - Mobile transaction models: defining the semantics and protocols for mobile transactions, such as atomic, consistent, isolated, and mobile (ACIM), or atomic, consistent, isolated, and resilient (ACIR).