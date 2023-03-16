### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events, and consistency and replication of data  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC) vs. message passing: whether the communication is based on invoking a procedure on a remote machine or sending a message to a destination  .
  - Client-server vs. peer-to-peer: whether the communication is based on a centralized or decentralized architecture  .
  - Publish-subscribe vs. message queue: whether the communication is based on a topic or a queue  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they can be detected and handled  .
- They include aspects such as availability, reliability, fault tolerance and recovery  .
- Some examples of failure models are:
  - Crash vs. omission vs. arbitrary failures: whether a process stops working, misses some messages, or behaves unpredictably  .
  - Fail-stop vs. fail-silent vs. fail-noisy: whether a process can notify others of its failure, remains silent, or sends incorrect messages  .
  - Byzantine vs. non-Byzantine failures: whether a process can lie or cheat to other processes or not  .
  - Detection vs. masking vs. tolerance: whether a failure can be detected, hidden, or tolerated by the system  .

#### Security Models
- Security models specify the types of threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and how they can be prevented and mitigated  .
- They include aspects such as authentication, authorization, encryption, digital signatures and firewalls  .
- Some examples of security models are:
  - Symmetric vs. asymmetric cryptography: whether the same or different keys are used for encryption and decryption  .
  - Kerberos vs. public key infrastructure (PKI): whether a trusted third party or a distributed network of certificates is used for authentication  .
  - Denial-of-service (DoS) vs. distributed denial-of-service (DDoS) attacks: whether a single or multiple sources are used to overwhelm a target with requests  .
  - Intrusion detection vs. intrusion prevention systems: whether a system can detect or prevent unauthorized access or malicious activity  .