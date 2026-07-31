# BBF for the notes of the Unit 5 - Service Layer Protocols & Security in the subject of IOT ARCHITECTURE AND PROTOCOLS

## Service Layer Protocols
- Service layer protocols are the protocols that enable the communication and interaction among applications and services running on different IoT devices and on cloud/edge infrastructures.
- Service layer protocols are typically based on the application layer of the TCP/IP model, but they may also operate on other layers, such as the transport or the network layer.
- Some of the common service layer protocols in IoT are:
  - Constrained Application Protocol (CoAP): A lightweight protocol that is HTTP-friendly and uses two basic message types: request and response. It supports confirmable and non-confirmable messages, as well as multicast and observe options. It is designed for constrained devices and networks, and uses UDP as the transport protocol.
  - Message Queuing Telemetry Transport (MQTT): A publish-subscribe protocol that allows devices to publish messages to a broker, which then delivers them to the subscribers. It is suitable for low-power and low-bandwidth devices, and uses TCP as the transport protocol. It supports three levels of quality of service (QoS): at most once, at least once, and exactly once.
  - Advanced Message Queuing Protocol (AMQP): A binary protocol that supports both publish-subscribe and point-to-point communication models. It is designed for high-performance and reliable messaging, and uses TCP as the transport protocol. It supports transactions, acknowledgments, and security features.
  - HyperText Transfer Protocol (HTTP): A widely used protocol that supports request-response and RESTful communication models. It is based on the client-server architecture, and uses TCP as the transport protocol. It supports various methods, such as GET, POST, PUT, and DELETE, and various formats, such as XML, JSON, and HTML.
  - Extensible Messaging and Presence Protocol (XMPP): A protocol that supports instant messaging and presence information. It is based on the XML format, and uses TCP as the transport protocol. It supports various features, such as authentication, encryption, federation, and extensions.

## Security in IoT
- Security in IoT is the protection of the confidentiality, integrity, and availability of the data and devices involved in the IoT system.
- Security in IoT is challenging due to the heterogeneity, scalability, and resource constraints of the IoT devices and networks, as well as the complexity and diversity of the IoT applications and services.
- Security in IoT can be addressed at different layers of the IoT architecture, such as the device layer, the network layer, the service layer, and the application layer.
- Some of the security threats and attacks that can affect the IoT system are:
  - Eavesdropping: The interception and analysis of the data transmitted over the network by an unauthorized party.
  - Replay: The retransmission of a previously captured message by an attacker to impersonate a legitimate sender or receiver.
  - Modification: The alteration of the data or the message header by an attacker to change the content or the destination of the message.
  - Spoofing: The creation and transmission of a fake message by an attacker to impersonate a legitimate sender or receiver.
  - Denial-of-service (DoS): The prevention of the normal functioning of the network or the device by an attacker by flooding them with malicious traffic or requests.
  - Distributed denial-of-service (DDoS): The prevention of the normal functioning of the network or the device by an attacker by coordinating multiple compromised devices to flood them with malicious traffic or requests.
  - Malware: The malicious software that can infect the device or the network and perform harmful actions, such as stealing data, deleting files, or executing commands.
  - Man-in-the-middle (MITM): The interception and modification of the data transmitted between two parties by an attacker who positions himself in the middle of the communication channel.
  - Sybil: The creation and use of multiple fake identities by an attacker to disrupt the network or the service, such as by spreading false information, voting multiple times, or colluding with other attackers.
  - Wormhole: The creation and use of a tunnel between two distant points in the network by an attacker to relay the messages and create a false sense of proximity, such as by attracting traffic, disrupting routing, or launching other attacks.
- Some of the security solutions and mechanisms that can be applied to the IoT system are:
  - Encryption: The transformation of the data into an unreadable form by using a