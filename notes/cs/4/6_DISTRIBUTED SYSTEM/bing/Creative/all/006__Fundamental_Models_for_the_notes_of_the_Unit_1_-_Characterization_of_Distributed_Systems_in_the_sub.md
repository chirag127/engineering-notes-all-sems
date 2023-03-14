### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Fundamental models are descriptions of properties that are present in all distributed architectures. They help us to understand the basic characteristics and challenges of distributed systems, and to design and evaluate solutions for them. There are four main types of fundamental models:

- Interaction models: These models deal with the issues of communication and coordination between processes in a distributed system, such as performance, timing, ordering, and synchronization of events.
- Failure models: These models specify the types of faults that can occur in processes and communication channels in a distributed system, and how they can be detected and handled.
- Security models: These models describe the threats and attacks that can compromise the confidentiality, integrity, and availability of processes and communication channels in a distributed system, and how they can be prevented and mitigated.
- Consistency models: These models define the degree of agreement or coherence among the data or state of processes in a distributed system, and how they can be maintained and updated.

Some examples of interaction models are:

- Synchronous model: This model assumes that there are known bounds on the time to execute a step, the message transmission delay, and the clock drift rate in a distributed system. This model simplifies the design of distributed algorithms, but it is unrealistic and inefficient in practice, as it requires timeouts and synchronization mechanisms to cope with uncertainty and variability.
- Asynchronous model: This model makes no assumptions about the timing of events or messages in a distributed system. This model is more realistic and flexible, but it also makes the design of distributed algorithms more complex and challenging, as it requires logical ordering and consensus mechanisms to deal with uncertainty and variability.

Some examples of failure models are:

- Omission failures: These are failures where a process or a communication channel fails to perform an expected action, such as sending or receiving a message. For example, a process may crash and stop executing, or a message may be lost or delayed in the network. These failures can be detected by timeouts or acknowledgments, and handled by retries or replication.
- Arbitrary failures: These are failures where a process or a communication channel behaves in an unpredictable or malicious way, such as sending incorrect or inconsistent data, or modifying or dropping messages. For example, a process may be corrupted by a virus or a hacker, or a message may be tampered with or forged by an adversary. These failures are hard to detect and handle, as they require integrity and authentication mechanisms.

Some examples of security models are:

- Threat model: This model identifies the potential adversaries and their capabilities and goals in attacking a distributed system. For example, an adversary may be an external hacker or an internal employee, and they may have access to the network or the machines, and they may want to steal or modify data, or disrupt or deny service.
- Security policy: This model defines the rules and requirements for protecting the distributed system from the threats. For example, a security policy may specify the confidentiality, integrity, and availability levels for the data and the processes, and the authentication, authorization, and encryption methods for the communication channels.
- Security mechanism: This model implements the security policy by providing the tools and techniques for enforcing the security rules and requirements. For example, a security mechanism may use cryptographic algorithms, digital signatures, certificates, firewalls, or intrusion detection systems to secure the distributed system.

Some examples of consistency models are:

- Strong consistency: This model guarantees that all processes in a distributed system see the same data or state at all times, and that any update is immediately visible to all processes. This model is desirable for applications that require high accuracy and reliability, but it is costly and difficult to achieve in practice, as it requires synchronization and replication mechanisms.
- Weak consistency: This model allows some degree of divergence or inconsistency among the data or state of processes in a distributed system, and that any update may take some time to propagate to all processes. This model is acceptable for applications that can tolerate some inaccuracy and unreliability, but it is cheaper and easier to achieve in practice, as it requires less synchronization and replication mechanisms.