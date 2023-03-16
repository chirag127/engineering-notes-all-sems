### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It is designed to transport **Public Switched Telephone Network (PSTN)** signaling messages over IP networks, but is capable of broader applications.
- It places messages and control information into separate **chunks**, each identified by a chunk header.
- The protocol can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- SCTP **bundles** the chunks into SCTP packets.
- SCTP provides the following features:
  - Acknowledgement and retransmission of lost data
  - Detection and correction of data corruption
  - Flow control and congestion control
  - Ordered and unordered delivery of data
  - Support for multihoming and network address translation
  - Protection against flooding and masquerade attacks
  - Graceful shutdown of connections
  - Path MTU discovery
  - Optional authentication of chunks