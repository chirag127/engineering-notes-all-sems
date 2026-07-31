### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures  .
- They help us understand the characteristics, challenges and trade-offs of designing and implementing distributed systems.
- There are three main types of fundamental models: interaction models, failure models and security models  .

#### Interaction Models
- Interaction models deal with the issues of how processes communicate and coordinate with each other in a distributed system  .
- They include aspects such as performance, timing, ordering, synchronization and consistency of events and messages  .
- Some examples of interaction models are:
  - Synchronous vs. asynchronous communication: whether the sender and receiver of a message have to wait for each other or not  .
  - Remote procedure call (RPC): a method of invoking a procedure or function on a remote machine as if it were local  .
  - Publish-subscribe: a pattern where publishers send messages to a broker, and subscribers receive messages that match their interests  .
  - Message queue: a data structure that stores messages from senders and delivers them to receivers in a FIFO order  .

#### Failure Models
- Failure models specify the types of faults that can occur in processes and communication channels in a distributed system  .
- They help us design fault-tolerant mechanisms and protocols to cope with failures and ensure reliability and availability  .
- Some examples of failure models are:
  - Crash failure: a process stops executing and does not resume  .
  - Omission failure: a process fails to send or receive a message  .
  - Timing failure: a process does not meet the timing constraints of the system  .
  - Byzantine failure: a process behaves arbitrarily or maliciously  .

#### Security Models
- Security models define the threats and attacks that can compromise the confidentiality, integrity and availability of data and resources in a distributed system  .
- They help us design security mechanisms and protocols to protect the system from unauthorized access and manipulation  .
- Some examples of security models are:
  - Cryptographic model: a model that uses mathematical techniques to encrypt and decrypt data, and to verify the identity and authenticity of the sender and receiver  .
  - Access control model: a model that specifies the permissions and policies that govern who can access what data and resources in the system  .
  - Trust model: a model that evaluates the trustworthiness and reputation of the entities in the system based on their behavior and feedback  .