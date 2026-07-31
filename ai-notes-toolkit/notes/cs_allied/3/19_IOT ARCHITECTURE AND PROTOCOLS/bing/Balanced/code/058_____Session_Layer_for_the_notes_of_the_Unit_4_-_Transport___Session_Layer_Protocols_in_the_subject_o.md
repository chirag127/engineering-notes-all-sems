### Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for the actual transmission of data in the IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queuing Telemetry Transport): A lightweight publish-subscribe protocol that works on top of TCP/IP and supports QoS levels, authentication, and encryption  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that is designed for constrained devices and networks. It uses UDP as the transport layer and supports RESTful architecture, caching, and multicast  .
  - AMQP (Advanced Message Queuing Protocol): An open standard protocol that provides reliable and secure messaging between applications or organizations. It uses TCP as the transport layer and supports message orientation, queuing, routing, and security  .
  - XMPP (Extensible Messaging and Presence Protocol): An XML-based protocol that enables real-time communication and collaboration between devices and applications. It uses TCP or HTTP as the transport layer and supports presence, chat, group chat, and file transfer  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the network.
  - Synchronization: It allows the addition of checkpoints into a data stream so that the data can be re-synchronized in case of failure or interruption.