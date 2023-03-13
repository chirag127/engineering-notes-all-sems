## Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are software programs that can move from one host to another in a network, carrying their code, data, and state with them.
- Mobile agents can be used for various applications, such as information retrieval, network management, e-commerce, distributed computing, and mobile computing.
- Mobile agents computing has several advantages, such as:
  - Reducing network traffic by moving computation closer to data sources.
  - Adapting to dynamic network conditions and user preferences.
  - Enhancing scalability and fault tolerance by exploiting parallelism and redundancy.
  - Supporting disconnected operation by allowing agents to resume execution after reconnection.
- Mobile agents computing also faces several challenges, such as:
  - Security: protecting agents from malicious hosts and hosts from malicious agents.
  - Fault tolerance: ensuring reliable execution of agents in the presence of failures.
  - Transaction processing: ensuring atomicity, consistency, isolation, and durability of agents that access shared data in a database.

### Mobile agents security

- Security is a major concern for mobile agents, as they are exposed to various threats and attacks in the network.
- Mobile agents security can be classified into three categories:
  - Security between agents: preventing unauthorized communication, impersonation, eavesdropping, tampering, and replaying of messages between agents.
  - Security between hosts: preventing unauthorized access, modification, deletion, and denial of service of hosts by agents or other hosts.
  - Security between agents and hosts: preventing unauthorized inspection, modification, deletion, and copying of agents by hosts or other agents.
- Some of the security measures to protect mobile agents are:
  - Authentication: verifying the identity and integrity of agents and hosts using cryptographic techniques, such as digital signatures, certificates, and public-key encryption.
  - Encryption: protecting the confidentiality and integrity of agents and messages using cryptographic techniques, such as symmetric-key encryption, public-key encryption, and hash functions.
  - Obfuscation: hiding the code and data of agents from unauthorized inspection using techniques, such as encryption, compression, and transformation.
  - Watermarking: embedding a unique identifier or a secret message into the code or data of agents using techniques, such as steganography, cryptography, and error-correcting codes.
  - Replication: creating multiple copies of agents and distributing them across different hosts to increase availability and fault tolerance.
  - Recovery: restoring the state and data of agents after a failure or an attack using techniques, such as checkpoints, logging, and backups.

### Mobile agents fault tolerance

- Fault tolerance is the ability of a system to continue functioning correctly in the presence of failures.
- Mobile agents fault tolerance can be achieved by using various techniques, such as:
  - Checkpointing: saving the state and data of agents at certain points during their execution, so that they can resume from the last checkpoint in case of a failure.
  - Logging: recording the actions and events of agents during their execution, so that they can be replayed or undone in case of a failure.
  - Replication: creating multiple copies of agents and distributing them across different hosts to increase availability and fault tolerance.
  - Migration: moving agents from one host to another to avoid or recover from failures, or to improve performance or load balancing.
  - Rejuvenation: restarting or refreshing agents periodically to prevent or recover from failures caused by aging or accumulation of errors.
  - Exception handling: detecting and handling errors and exceptions that occur during the execution of agents, such as communication failures, host failures, agent failures, or malicious attacks.

### Transaction processing in mobile computing

- Transaction processing is the execution of a sequence of operations that access or modify shared data in a database, such as booking tickets, flight reservation, banking, or e-payment.
- Transaction processing in mobile computing is challenging, as mobile devices and networks are prone to disconnections, low bandwidth, high latency, and limited resources.
- Transaction processing in mobile computing can be supported by using various techniques, such as:
  - Disconnected operation: allowing mobile devices to execute transactions locally without a network connection, and synchronizing them with the database when the connection is available.
  - Semantic properties: using the meaning and context of transactions to determine their validity and consistency, and resolving conflicts or inconsistencies that may arise due to disconnections or concurrency.
  - Open-nesting: structuring transactions into a hierarchy of subtransactions that can interleave and commit independently, and using compensation or reporting mechanisms to ensure global consistency.
  - Optimistic concurrency control: allowing transactions to execute and commit without locking or blocking, and detecting and