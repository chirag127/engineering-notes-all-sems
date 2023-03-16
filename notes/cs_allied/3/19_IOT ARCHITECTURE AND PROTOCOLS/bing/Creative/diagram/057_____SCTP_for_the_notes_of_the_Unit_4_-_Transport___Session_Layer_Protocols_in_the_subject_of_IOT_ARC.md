### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It is designed to transport **Public Switched Telephone Network (PSTN)** signaling messages over IP networks, but is capable of broader applications.
- It places messages and control information into separate **chunks**, each identified by a chunk header.
- The protocol can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- SCTP **bundles** the chunks into SCTP packets.
- SCTP packets have a common header and a variable number of chunks.
- SCTP provides the following features  :
  - **Multi-homing**: Each endpoint can have more than one IP address, providing network-level fault tolerance.
  - **Multi-streaming**: Each connection can have multiple logical streams that deliver data chunks in order within each stream, but not across streams.
  - **Congestion control**: SCTP uses a modified version of TCP's congestion control algorithm to avoid network congestion.
  - **Flow control**: SCTP uses a window-based mechanism to regulate the amount of data in flight.
  - **Error detection**: SCTP uses checksums to detect corrupted packets and discard them.
  - **Error correction**: SCTP uses selective acknowledgments (SACKs) to report the receipt of data and request retransmission of lost data.
  - **Ordered and unordered delivery**: SCTP allows the application to choose whether to receive data in order or not.
  - **Message-oriented**: SCTP preserves the boundaries of each user message and does not merge or split them.
  - **Path MTU discovery**: SCTP can discover the maximum transmission unit (MTU) of the path and adjust the packet size accordingly.
  - **Cookie mechanism**: SCTP uses a four-way handshake with a cookie exchange to establish a connection and prevent denial-of-service attacks.

: Stream Control Transmission Protocol - Wikipedia
: Stream Control Transmission Protocol (SCTP) - SearchNetworking
: RFC 4960: Stream Control Transmission Protocol - RFC Editor