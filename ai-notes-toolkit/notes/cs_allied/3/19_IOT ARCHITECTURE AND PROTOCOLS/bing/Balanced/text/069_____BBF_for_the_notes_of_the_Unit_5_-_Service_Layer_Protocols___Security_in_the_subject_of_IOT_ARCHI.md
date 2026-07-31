### BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

- Service layer protocols are the protocols that enable the communication and interaction among applications and services running on different IoT devices and on cloud/edge infrastructures.
- Security of service layer protocols is crucial for ensuring the confidentiality, integrity, availability, and privacy of the data and services in IoT.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. It supports confirmable and non-confirmable messages, as well as multicast and observe options. It also provides security features such as encryption, authentication, and authorization using Datagram Transport Layer Security (DTLS).
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that uses a broker to facilitate the communication between publishers and subscribers. It is designed for low-bandwidth, high-latency, and unreliable networks. It offers three levels of quality of service (QoS): at most once, at least once, and exactly once. It also supports Transport Layer Security (TLS) for secure communication.
  - Advanced Message Queuing Protocol (AMQP): An open standard protocol that provides reliable and interoperable messaging between applications and services. It uses a broker to route messages based on exchanges, queues, and bindings. It supports different message delivery modes, such as persistent, transient, and mandatory. It also supports TLS and SASL for security.
- Some of the security challenges and solutions for service layer protocols in IoT are:
  - Data privacy: The protection of sensitive and personal data from unauthorized access and disclosure. Some of the solutions include data encryption, anonymization, pseudonymization, and access control mechanisms .
  - Authentication: The verification of the identity of the communicating parties. Some of the solutions include certificates, passwords, tokens, biometrics, and challenge-response schemes .
  - Authorization: The granting of permissions and privileges to the authenticated parties. Some of the solutions include role-based access control, attribute-based access control, and policy-based access control .
  - Trust management: The establishment and maintenance of trust relationships among the communicating parties. Some of the solutions include reputation systems, trust models, and trust negotiation protocols .
- BBF (Broadband Forum) is an industry organization that develops standards and best practices for broadband networks and services. One of its projects is the User Services Platform (USP), which is a protocol for managing and controlling IoT devices and services. USP is based on the CPE WAN Management Protocol (CWMP), which is commonly known as TR-069.
- USP provides the following features and benefits for IoT service layer protocols and security:
  - Simple migration from CWMP through the use of the same data model and data modeling tools.
  - Support for multiple transport protocols, such as HTTP, WebSocket, CoAP, and MQTT.
  - Support for secure communication using TLS and DTLS, as well as authentication and authorization using certificates and tokens.
  - Support for device grouping, device discovery, device configuration, device monitoring, device control, and device firmware upgrade.
  - Support for event-driven and scheduled communication, as well as push and pull modes.