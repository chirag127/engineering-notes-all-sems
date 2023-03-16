# Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

## Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering and synchronization of events  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure on a remote machine as if it were local  .
  - Publish-subscribe: a pattern of communication where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message passing interface (MPI): a standard for parallel programming that supports point-to-point and collective communication among processes  .

## Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant mechanisms and protocols to ensure the reliability and availability of the system  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously  .

## Security Models
- Security models define the goals and threats of a distributed system in terms of confidentiality, integrity and availability  .
- They help us design cryptographic techniques and protocols to protect the system from unauthorized access and manipulation  .
- Some examples of security models are:
  - Symmetric-key cryptography: a method of encryption and decryption that uses the same secret key for both parties  .
  - Public-key cryptography: a method of encryption and decryption that uses a pair of keys: a public key that can be shared and a private key that is kept secret  .
  - Digital signature: a technique that allows a sender to prove the authenticity and integrity of a message using a private key  .
  - Authentication: a process that verifies the identity of a user or a process  .