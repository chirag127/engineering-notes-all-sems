# BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Service layer protocols are the protocols that enable the communication and interaction among applications and services running on different IoT devices and on cloud/edge infrastructures.
- Security of service layer protocols is crucial for ensuring the confidentiality, integrity, availability, and privacy of the data and services in IoT.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. Messages can be confirmable or non-confirmable. CoAP supports four methods: GET, PUT, POST, and DELETE. CoAP also supports resource discovery, caching, and observation.
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that uses a broker to manage the communication between publishers and subscribers. MQTT is designed for low-bandwidth, high-latency, and unreliable networks. MQTT supports three levels of quality of service: at most once, at least once, and exactly once.
  - Advanced Message Queuing Protocol (AMQP): A peer-to-peer protocol that uses exchanges and queues to route messages between producers and consumers. AMQP is designed for high-performance, reliable, and secure messaging. AMQP supports four types of exchanges: direct, fanout, topic, and headers.
  - HyperText Transfer Protocol (HTTP): A request-response protocol that uses Uniform Resource Identifiers (URIs) to identify resources and methods to manipulate them. HTTP is the most widely used protocol for web applications and services. HTTP supports caching, compression, authentication, and encryption.
- Some of the security challenges and solutions for service layer protocols in IoT are:
  - Data privacy: The protection of sensitive or personal data from unauthorized access or disclosure. Data privacy can be achieved by using encryption, anonymization, pseudonymization, or differential privacy techniques.
  - Authentication: The verification of the identity or credentials of a device, user, or service. Authentication can be achieved by using passwords, tokens, certificates, biometrics, or multi-factor authentication methods.
  - Authorization: The granting or denying of access rights or permissions to a device, user, or service. Authorization can be achieved by using access control lists, roles, policies, or attributes.
  - Trust management: The establishment and maintenance of trust relationships among devices, users, or services. Trust management can be achieved by using reputation, feedback, or blockchain mechanisms.
  - Security attacks: The malicious attempts to compromise the security of service layer protocols or the data and services they carry. Security attacks can be classified into passive or active, internal or external, and physical or logical.
- Some of the security standards and best practices for service layer protocols in IoT are:
  - Transport Layer Security (TLS): A protocol that provides end-to-end encryption, authentication, and integrity for data transmitted over a network. TLS can be used with CoAP, MQTT, AMQP, and HTTP to secure the communication between devices and services.
  - Datagram Transport Layer Security (DTLS): A protocol that provides the same security features as TLS, but for datagram-based protocols such as User Datagram Protocol (UDP). DTLS can be used with CoAP to secure the communication between constrained devices and services.
  - User Services Platform (USP): A protocol that provides a standardized way to manage, monitor, and control IoT devices and services. USP is based on the Broadband Forum (BBF) data model and uses CoAP, MQTT, or WebSocket as the underlying transport protocol. USP supports security features such as mutual authentication, encryption, and authorization.
  - Internet of Things Security Foundation (IoTSF): A non-profit organization that promotes the security of IoT devices and services. IoTSF provides best practice guides, compliance frameworks, certification schemes, and training programs for IoT stakeholders.

: Security of IoT Application Layer Protocols: Challenges and Findings
: Security Protocols for IoT
: BBF – 1 Introduction
: Communication Protocols for IoT > IoT and Security Standards and Best Practices
: Common application layer protocols in IoT explained