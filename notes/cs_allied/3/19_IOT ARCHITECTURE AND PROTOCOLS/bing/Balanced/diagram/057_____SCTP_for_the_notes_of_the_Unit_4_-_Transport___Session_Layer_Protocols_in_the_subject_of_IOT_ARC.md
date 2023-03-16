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
  - **Multi-homing**: An SCTP endpoint can have more than one IP address, providing network-level fault tolerance.
  - **Multi-streaming**: An SCTP connection can have multiple streams of data, each with its own sequence number and flow control, allowing independent and concurrent delivery of data.
  - **Congestion control**: SCTP uses a modified version of TCP's congestion control algorithm to avoid network congestion and packet loss.
  - **Selective acknowledgment**: SCTP uses a selective acknowledgment mechanism to acknowledge only the received packets, reducing the number of retransmissions.
  - **Path MTU discovery**: SCTP can discover the maximum transmission unit (MTU) of the path between the endpoints, avoiding fragmentation and improving performance.
  - **Heartbeat**: SCTP can send periodic messages to check the availability of the endpoints and the paths, detecting failures and restoring connectivity.
  - **Cookie mechanism**: SCTP uses a cookie mechanism to prevent denial-of-service attacks and to establish connections in a four-way handshake, avoiding the SYN flooding problem of TCP.

: Stream Control Transmission Protocol - Wikipedia
: Stream Control Transmission Protocol (SCTP) - SearchNetworking
: RFC 4960: Stream Control Transmission Protocol - RFC Editor