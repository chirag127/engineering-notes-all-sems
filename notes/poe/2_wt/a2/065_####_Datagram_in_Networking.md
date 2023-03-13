 Here is the content in markdown format on the topic #### Datagram in Networking:

#### Datagram in Networking

A datagram is a basic transfer unit associated with a packet-switched network that includes source and destination address and data. Datagrams are self-contained and independent, with no relationship between packets.

Key points to remember:

- Datagrams are packets of information that contain source and destination addresses along with the actual data being sent.
- Datagrams are transmitted independently and can take different routes to reach the destination. They are reassembled in the correct order at the destination.
- Datagrams include enough information to be routed from source to destination without reliance on earlier exchanges between the two hosts.
- The user data in a datagram is not necessarily related to data in other datagrams.
- In UDP, data is transmitted in datagrams.

Mnemonics:

- Think of Datagram as a self-contained packet - It has its own (source, destination, data) and can travel independently.
- Datagram's relation to UDP - UDP uses datagrams to transmit data.

Examples and applications:

- Email is a typical example of a datagram network. Each email message is a separate datagram that includes destination address information and can take different routes to reach the destination.
- The UDP protocol uses datagrams to deliver data over IP networks without guaranteeing packet ordering, delivery, or duplicate protection.
- DNS queries and responses use UDP datagrams.

Advantages:

- Simplicity of design. Datagrams are easy to implement and the protocols are fairly simple.
- Flexibility. Datagrams can take different paths to the destination and can be easily rerouted in case of congestion or link failure.
- Scalability. The independent and self-contained nature of datagrams makes the design highly scalable.

Disadvantages:

- Packet loss. Since there is no tracking of individual datagrams, packets may be lost or delivered out of order. Higher level protocols are required to handle this.
- Congestion control. The independent nature of datagrams makes it difficult to implement effective congestion control mechanisms.
- Security. The lack of relationships between datagrams makes it difficult to implement strong security mechanisms.

[Detailed diagrams and codes can be included here if required.]