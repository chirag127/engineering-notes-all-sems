### DCCP

- DCCP stands for **Datagram Congestion Control Protocol**.
- It is a **message-oriented** transport layer protocol.
- It is designed to solve issues present in UDP and TCP, particularly for **real-time and multimedia** (streaming) traffic.
- It implements **reliable connection setup**, **teardown**, **Explicit Congestion Notification (ECN)**, **congestion control**, and **feature negotiation**.
- It divides into a base protocol (RFC 4340) and pluggable congestion control modules called **CCIDs** (Congestion Control IDentifiers).
- It allows applications to access congestion control mechanisms without implementing them at the application layer.
- It supports both **acknowledged** and **unacknowledged** modes of data delivery.
- It uses a **packet header** that contains a **sequence number**, a **type**, a **CCID**, and other optional fields.
- It uses a **three-way handshake** to establish a connection and a **four-way handshake** to close a connection.
- It uses a **feature negotiation mechanism** to allow endpoints to agree on optional protocol parameters.
- It uses a **slow-start** and **congestion avoidance** algorithm to adjust the sending rate according to the network conditions.
- It supports different **congestion control profiles** that can be selected by the application according to its requirements.
- Some examples of CCIDs are:
  - CCID 2: TCP-like congestion control with acknowledgments and retransmissions.
  - CCID 3: TCP-friendly rate control with feedback packets and no retransmissions.
  - CCID 4: TCP-friendly rate control for unidirectional flows.
  - CCID 5: TCP-friendly rate control for bidirectional flows.