### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Fundamental models are descriptions of properties that are present in all distributed architectures, such as concurrency, scalability, transparency, and fault tolerance.
- Fundamental models can be classified into three categories: interaction models, failure models, and security models.
- Interaction models deal with the issues of communication and coordination among processes in a distributed system, such as performance, timing, ordering, and consistency of events.
- Failure models specify the types of faults that can occur in processes and communication channels, such as crash, omission, timing, response, and arbitrary faults.
- Security models define the threats and countermeasures for protecting the confidentiality, integrity, and availability of data and resources in a distributed system, such as encryption, authentication, authorization, and auditing.

- Some examples of interaction models are:

  - Message passing: Processes communicate by sending and receiving messages over a network. This model is simple, flexible, and scalable, but it requires explicit synchronization and error handling.
  - Remote procedure call (RPC): Processes invoke procedures or methods on remote machines as if they were local. This model hides the details of message passing and provides a familiar abstraction, but it introduces additional complexity and overhead for marshalling, unmarshalling, and binding.
  - Remote method invocation (RMI): Processes invoke methods on remote objects as if they were local. This model extends the RPC model with object-oriented features, such as inheritance, polymorphism, and garbage collection, but it also inherits the same drawbacks of RPC.
  - Publish-subscribe: Processes publish events to a broker or a topic, and other processes subscribe to receive those events. This model decouples the producers and consumers of events, and supports asynchronous and multicast communication, but it also requires reliable and scalable brokers or topics, and may suffer from information overload or inconsistency.
  - Shared memory: Processes access a common memory space to read and write data. This model provides a convenient and fast way of communication, but it also introduces challenges for maintaining consistency, coherence, and synchronization of the shared data.

- Some examples of failure models are:

  - Crash failure: A process or a channel stops functioning correctly and does not resume. This is the simplest and most common type of failure, and it can be detected by timeouts or heartbeats.
  - Omission failure: A process or a channel fails to send or receive a message. This type of failure can be caused by network congestion, packet loss, or buffer overflow, and it can be detected by acknowledgments or retries.
  - Timing failure: A process or a channel fails to meet the timing constraints of the system. This type of failure can be caused by clock drift, network delay, or resource contention, and it can be detected by timestamps or synchronization protocols.
  - Response failure: A process or a channel sends an incorrect or malformed message. This type of failure can be caused by software bugs, hardware faults, or malicious attacks, and it can be detected by checksums, signatures, or verification protocols.
  - Arbitrary failure: A process or a channel exhibits arbitrary or unpredictable behavior. This is the most general and worst type of failure, and it can be caused by any of the above reasons or by malicious attacks, and it can be detected by redundancy, replication, or consensus protocols.

- Some examples of security models are:

  - Symmetric-key cryptography: Processes use a shared secret key to encrypt and decrypt messages. This model provides fast and secure communication, but it also requires a secure way of distributing and managing the keys, and it does not provide non-repudiation or authentication.
  - Public-key cryptography: Processes use a pair of public and private keys to encrypt and decrypt messages. This model provides secure communication without the need of a shared secret key, and it also provides non-repudiation and authentication, but it also introduces additional complexity and overhead for generating, distributing, and verifying the keys.
  - Digital signature: Processes use their private keys to sign messages, and other processes use their public keys to verify the signatures. This model provides authentication, integrity, and non-repudiation of messages, but it also requires a trusted authority or a certificate to validate the public keys.
  - Access control: Processes use policies and mechanisms to grant or deny access to data and resources. This model provides authorization and confidentiality of data and resources, but it also requires a secure way of identifying and authenticating the users and the processes, and a consistent way of enforcing and updating the policies.