### Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queue Telemetry Transport): A lightweight, publish-subscribe protocol that is designed for constrained devices and low-bandwidth networks. It is widely used for IoT applications that require real-time data delivery, low power consumption, and high reliability  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is optimized for constrained devices and networks. It is based on the RESTful architecture and uses UDP as the transport layer protocol. It supports features such as multicast, caching, and asynchronous communication  .
  - AMQP (Advanced Message Queuing Protocol): An open standard protocol that provides reliable and secure messaging between applications and devices. It is based on the broker model and uses TCP as the transport layer protocol. It supports features such as message routing, queuing, delivery confirmation, and transactions  .
  - XMPP (Extensible Messaging and Presence Protocol): An open standard protocol that enables instant messaging and presence information exchange between applications and devices. It is based on the client-server model and uses XML as the data format. It supports features such as authentication, encryption, federation, and extensions  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the same network.
  - Synchronization: It allows the communication to resume from the point of interruption in case of a failure or disconnection.