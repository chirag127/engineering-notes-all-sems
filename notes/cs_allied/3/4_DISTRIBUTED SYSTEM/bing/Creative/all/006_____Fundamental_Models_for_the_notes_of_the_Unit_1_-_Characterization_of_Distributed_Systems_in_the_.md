# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of distributed systems .
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not.
  - Remote procedure call (RPC): a method of invoking a procedure on a remote machine as if it were local.
  - Publish-subscribe: a pattern of message exchange where publishers send messages to a broker and subscribers receive messages that match their interests.
  - Distributed shared memory (DSM): a model of memory access where processes can read and write to a shared virtual memory space.

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the system's behavior  .
- They include aspects such as fault detection, fault tolerance, fault recovery and fault prevention  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume.
  - Omission failure: a process fails to send or receive a message.
  - Timing failure: a process does not meet a timing constraint.
  - Byzantine failure: a process behaves arbitrarily or maliciously.

## Security Models
- Security models describe the goals and mechanisms of protecting a distributed system from unauthorized or malicious actions  .
- They include aspects such as confidentiality, integrity, availability, authentication, authorization and non-repudiation  .
- Some examples of security models are:
  - Symmetric-key cryptography: a method of encryption and decryption where the same secret key is used by both parties.
  - Public-key cryptography: a method of encryption and decryption where each party has a public key and a private key.
  - Digital signature: a way of verifying the authenticity and integrity of a message using public-key cryptography.
  - Kerberos: a protocol for authenticating users and services in a distributed system using symmetric-key cryptography and a trusted third party.