### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol.
- It is designed to solve issues present in UDP and TCP, particularly for **real-time and multimedia** (streaming) traffic.
- It implements reliable **connection setup**, **teardown**, **Explicit Congestion Notification (ECN)**, **congestion control**, and **feature negotiation**.
- It divides into a base protocol (RFC 4340) and pluggable **congestion control modules** called CCIDs.
- It allows applications to access congestion control mechanisms without implementing them at the application layer.
- It supports both **unidirectional** and **bidirectional** data transfer.
- It uses a **packet header** that contains a **sequence number**, a **type**, an **acknowledgement number**, and a **checksum**.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It supports **feature negotiation** to allow endpoints to agree on optional protocol extensions.
- It supports **half-close** and **reset** operations to terminate a connection or a direction of data transfer.
- It supports **server listening**, **active open**, and **passive open** modes to initiate a connection.
- It supports **keepalive** and **ping** mechanisms to maintain a connection or test its liveness.
- It supports **change** and **confirm** options to modify the connection parameters during data transfer.
- It supports **different CCIDs** for different types of traffic, such as TCP-like, TCP-friendly, or multimedia.

: https://en.wikipedia.org/wiki/Datagram_Congestion_Control_Protocol
: https://www.kernel.org/doc/html/latest/networking/dccp.html
: https://www.geeksforgeeks.org/what-is-dccp-datagram-congestion-control-protocol/