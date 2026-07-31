# Session Layer for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- The session layer is the fifth layer of the OSI model that manages the connection between two endpoints of a network by controlling data between sender and receiver  .
- The session layer protocols are responsible for actual transmission of data in IoT ecosystem. That’s why these session layer protocols are called as IoT Messaging Protocols or sometimes referred as IoT Data Protocols .
- The session layer protocols review standards and protocols for message passing. Different standardization organizations introduce the IoT session layer protocols. There are different types of session layer protocol available with different functionality and range.
- Some of the common session layer protocols in IoT are:
  - MQTT (Message Queue Telemetry Transport): A lightweight publish-subscribe protocol that works on TCP/IP and supports QoS levels  .
  - CoAP (Constrained Application Protocol): A web transfer protocol that works on UDP and supports RESTful web services  .
  - AMQP (Advanced Message Queuing Protocol): A binary protocol that works on TCP/IP and supports reliable and secure message delivery  .
  - XMPP (Extensible Messaging and Presence Protocol): An XML-based protocol that works on TCP/IP and supports instant messaging and presence information  .
- The session layer also provides some functions such as:
  - Dialog control: It allows systems to communicate in either half-duplex mode or full-duplex mode.
  - Token management: It prevents two users to simultaneously access or transmit data over the network.
  - Synchronization: It allows the addition of checkpoints into a data stream so that the data can be re-synchronized in case of failure or loss.