### DCCP

- DCCP stands for **Datagram Congestion Control Protocol** .
- It is a **message-oriented** transport layer protocol that supports **unreliable** and **congestion-controlled** delivery of datagrams .
- It is suitable for applications that require **low latency**, **high bandwidth**, or **partial reliability**, such as streaming media, online games, or voice over IP .
- It provides the following features :
  - **Reliable connection setup and teardown**: DCCP uses a three-way handshake to establish and close a connection, similar to TCP. It also provides mechanisms for connection migration, reset, and abort.
  - **Explicit Congestion Notification (ECN)**: DCCP supports ECN, which allows routers to mark packets as experiencing congestion, rather than dropping them. This allows the sender to adjust its sending rate accordingly, without waiting for packet loss or timeout.
  - **Congestion control**: DCCP allows the sender and receiver to negotiate the congestion control mechanism to be used for the connection, among a set of predefined options. Some of the available options are TCP-like, TCP-friendly, or TCP-low priority.
  - **Feature negotiation**: DCCP allows the sender and receiver to negotiate various features of the connection, such as checksums, acknowledgments, sequence numbers, or packet types.
- DCCP uses a **32-bit sequence number** to identify each packet, and a **48-bit acknowledgment number** to acknowledge the receipt of packets.
- DCCP has two main packet types: **Data** and **Ack**. Data packets carry application data, while Ack packets carry acknowledgments and feedback information.
- DCCP also has several other packet types, such as **Sync**, **SyncAck**, **CloseReq**, **Close**, **Reset**, and **DataAck**, to support various connection management functions.
- DCCP uses **port numbers** to identify different applications or services on the same host, similar to TCP and UDP.
- DCCP has a **header length** of 16 bytes, plus optional extensions.
- DCCP is defined in **RFC 4340**, a proposed standard, in March 2006. It has several other RFCs that define its congestion control options and features.