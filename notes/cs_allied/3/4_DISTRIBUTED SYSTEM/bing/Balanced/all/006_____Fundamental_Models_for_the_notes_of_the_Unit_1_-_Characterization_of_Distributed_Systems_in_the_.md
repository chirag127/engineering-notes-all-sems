# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not.
  - Remote procedure call (RPC) vs. message passing: whether the communication is based on invoking a procedure on a remote machine or sending a message to a destination.
  - Publish/subscribe vs. point-to-point: whether the communication is based on broadcasting messages to multiple subscribers or sending messages to a specific receiver.
  - Client/server vs. peer-to-peer: whether the communication is based on a centralized server that provides services to clients or a decentralized network of peers that cooperate with each other.

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant mechanisms and protocols to ensure the reliability and availability of the system.
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume .
  - Omission failure: a process fails to send or receive a message .
  - Timing failure: a process fails to meet a timing constraint .
  - Byzantine failure: a process behaves arbitrarily and may send incorrect or malicious messages .

## Security Models
- Security models define the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system and the countermeasures that can be applied to prevent or mitigate them .
- They help us design secure mechanisms and protocols to ensure the authenticity, authorization and accountability of the system.
- Some examples of security models are:
  - Cryptographic models: based on mathematical techniques to encrypt and decrypt data, generate keys and signatures, and verify identities.
  - Access control models: based on policies and rules to grant or deny access to resources, such as discretionary, mandatory and role-based access control.
  - Trust models: based on assumptions and evidence to establish the trustworthiness of entities, such as certificates, reputation and trust networks.