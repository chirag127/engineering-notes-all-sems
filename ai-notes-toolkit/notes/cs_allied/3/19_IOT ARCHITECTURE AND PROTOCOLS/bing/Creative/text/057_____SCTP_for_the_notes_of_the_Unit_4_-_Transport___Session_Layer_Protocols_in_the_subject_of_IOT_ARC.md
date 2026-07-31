### SCTP

- Stream Control Transmission Protocol (SCTP) is a transport layer protocol that provides reliable and in-sequence data transmission over IP networks  .
- SCTP was originally designed by the IETF for SS7 transport over IP-based networks.
- SCTP is a message-oriented protocol that can fragment a message into multiple data chunks, each identified by a chunk header.
- SCTP can also bundle multiple chunks into one SCTP packet, which contains a common header and a variable number of chunks.
- SCTP uses a 12-byte header that consists of the following fields :
  - Source port: 16 bits, identifies the source port number
  - Destination port: 16 bits, identifies the destination port number
  - Verification tag: 32 bits, used for verification of the sender
  - Checksum: 32 bits, used for error detection
- SCTP uses a 4-way handshake to establish, maintain, and terminate associations between endpoints .
- SCTP supports multiple streams within an association, which allows for parallel and independent delivery of messages .
- SCTP also supports multihoming, which allows for multiple IP addresses to be associated with each endpoint .
- SCTP is suitable for IOT applications that require reliable, ordered, and message-oriented data transfer, such as voice over IP, video conferencing, and signaling .