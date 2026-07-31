# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, consistency and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Peer-to-peer: a model where each node can act as both a client and a server, and communicate directly with other nodes  .

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system, and how they affect the processes and communication channels  .
- They help us design fault-tolerant and resilient systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failures: when a process stops executing and does not resume  .
  - Omission failures: when a process fails to send or receive a message  .
  - Timing failures: when a process does not meet the timing constraints of the system  .
  - Byzantine failures: when a process behaves arbitrarily or maliciously, and may send incorrect or conflicting messages  .

## Security Models
- Security models define the goals and requirements of protecting a distributed system from unauthorized access, modification or disclosure of information  .
- They include aspects such as confidentiality, integrity, availability, authentication, authorization and non-repudiation  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, and to verify its authenticity and origin  .
  - Kerberos: a protocol that uses tickets and keys to authenticate users and services in a distributed system  .
  - Blockchain: a distributed ledger that uses consensus algorithms and cryptographic hashes to ensure the validity and immutability of transactions  .