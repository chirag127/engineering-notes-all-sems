### DCCP

- DCCP stands for **Datagram Congestion Control Protocol** .
- It is a **message-oriented** transport layer protocol that provides **bidirectional unicast** connections of **congestion-controlled unreliable datagrams** .
- It is suitable for applications that transfer fairly large amounts of data, but can benefit from control over the tradeoff between **timeliness and reliability**.
- It implements reliable connection setup, teardown, Explicit Congestion Notification (ECN), congestion control, and feature negotiation.
- It supports different **congestion control mechanisms** that can be selected by the application or negotiated during connection establishment .
- It uses a **packet header** that contains a **source port, a destination port, a packet type, a sequence number, an acknowledgment number, and a checksum** .
- It defines several **packet types** for different purposes, such as **Request, Response, Data, Ack, DataAck, CloseReq, Close, Reset, Sync, and SyncAck** .
- It uses a **three-way handshake** to establish a connection, a **four-way handshake** to close a connection, and a **Reset packet** to abort a connection .
- It uses a **feature negotiation mechanism** to allow endpoints to agree on optional protocol parameters, such as **congestion control ID, ECN capability, send and receive window sizes, and acknowledgment frequency** .
- It is designed to be **extensible** and **interoperable** with other transport protocols, such as TCP and UDP .