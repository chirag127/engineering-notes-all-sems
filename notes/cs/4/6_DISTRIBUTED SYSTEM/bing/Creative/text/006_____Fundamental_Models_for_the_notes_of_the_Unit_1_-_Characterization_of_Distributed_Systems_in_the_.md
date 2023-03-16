### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering, consistency and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Message passing interface (MPI): a standard for parallel programming that supports point-to-point and collective communication among processes  .
  - Publish/subscribe: a pattern of communication where publishers send messages to a broker or a topic, and subscribers receive messages that match their interests  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us to design fault-tolerant and resilient distributed systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models describe the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and the countermeasures that can be applied to prevent or mitigate them  .
- They include aspects such as authentication, authorization, encryption, digital signatures, firewalls and intrusion detection  .
- Some examples of security models are:
  - Kerberos: a protocol for authenticating users and services in a distributed system using tickets and keys  .
  - Public key infrastructure (PKI): a system for managing public keys and certificates for encryption and digital signatures  .
  - Secure sockets layer (SSL) / transport layer security (TLS): a protocol for securing the communication between a client and a server using encryption and certificates  .
  - Blockchain: a distributed ledger that records transactions in a secure and verifiable way using cryptography and consensus  .