### DCCP

- DCCP stands for **Datagram Congestion Control Protocol** .
- It is a **message-oriented** transport layer protocol that provides **bidirectional unicast** connections of **congestion-controlled unreliable datagrams** .
- It is suitable for applications that transfer fairly large amounts of data, but can benefit from control over the tradeoff between **timeliness and reliability**.
- It implements reliable connection setup, teardown, Explicit Congestion Notification (ECN), congestion control, and feature negotiation.
- It supports different types of congestion control algorithms, such as TCP-like, TCP-friendly, and TFRC .
- It uses a **packet header** that contains a **source port, destination port, packet type, sequence number, acknowledgment number, and checksum** .
- It uses a **feature negotiation mechanism** that allows the endpoints to agree on the options and parameters to use for the connection .
- It uses a **state machine** that defines the possible states and transitions of a DCCP connection, such as REQUEST, RESPOND, OPEN, CLOSEREQ, CLOSE, and RESET .
- It uses a **handshake procedure** that involves the exchange of REQUEST, RESPOND, and ACK packets to establish a connection .
- It uses a **close procedure** that involves the exchange of CLOSEREQ, CLOSE, and ACK packets to terminate a connection .
- It uses a **reset procedure** that involves the exchange of RESET and ACK packets to abort a connection .
- It uses a **feedback mechanism** that involves the exchange of ACK and DATAACK packets to provide information about the received packets, such as sequence number, acknowledgment number, ECN, and loss event rate .
- It uses a **congestion control mechanism** that involves the use of congestion control identifiers (CCIDs) to specify the algorithm to use for each direction of the connection .
- It uses a **security mechanism** that involves the use of HMACs to protect the integrity of the packets and prevent spoofing attacks .
- It is defined by the IETF in RFC 4340, a proposed standard, in March 2006.