### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of communication and coordination among processes in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern of communication where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message queue: a data structure that stores messages from senders until they are consumed by receivers  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system and how they affect the processes and communication channels  .
- They help us design fault-tolerant and resilient systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process or a message violates the timing assumptions of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models define the goals and threats of a distributed system in terms of confidentiality, integrity and availability of data and services  .
- They help us design secure and trustworthy systems that can prevent, detect and respond to attacks  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, as well as to authenticate and verify the identity and integrity of the parties involved  .
  - Access control: the mechanism of granting or denying permissions to access data or services based on the identity and role of the requester  .
  - Distributed firewalls: the use of filters and rules to block or allow network traffic based on the source, destination and content of the packets  .