### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us to understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a function or procedure on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Peer-to-peer: a model where each node can act as both a client and a server, and communicate directly with other nodes  .

#### Failure Models
- Failure models specify the types of faults that can occur in a distributed system, and how they affect the processes and communication channels  .
- They help us to design fault-tolerant and reliable distributed systems that can cope with failures and recover from them  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously, sending incorrect or conflicting messages  .

#### Security Models
- Security models describe the threats and attacks that can compromise the confidentiality, integrity and availability of a distributed system, and the mechanisms to prevent or mitigate them  .
- They help us to design secure and trustworthy distributed systems that can protect the data and resources from unauthorized access and manipulation  .
- Some examples of security models are:
  - Cryptography: the use of mathematical techniques to encrypt and decrypt data, and to verify the identity and authenticity of the sender and receiver  .
  - Authentication: the process of verifying the identity of a user or a process before granting access to the system  .
  - Authorization: the process of determining the permissions and privileges of a user or a process to access or modify the data and resources of the system  .
  - Intrusion detection: the process of monitoring and analyzing the activities and events in the system to detect and respond to malicious or anomalous behavior  .