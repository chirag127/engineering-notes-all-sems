### SCTP

- SCTP stands for **Stream Control Transmission Protocol**.
- It is a **transport layer** protocol in the Internet protocol suite.
- It is a **connection-oriented** protocol that supports **multiple streams** of data between two endpoints.
- It ensures **reliable** and **in-sequence** data transmission, so that data units arrive completely and in the right order to the application or user.
- It can **fragment** a message into multiple data chunks, but each data chunk contains data from only one user message.
- It **bundles** the chunks into SCTP packets, each identified by a chunk header.
- It is designed to transport **PSTN** (Public Switched Telephone Network) signaling messages over IP networks, but is capable of broader applications.
- It provides features such as **multihoming**, **congestion control**, **flow control**, **error detection**, **security** and **graceful shutdown**.