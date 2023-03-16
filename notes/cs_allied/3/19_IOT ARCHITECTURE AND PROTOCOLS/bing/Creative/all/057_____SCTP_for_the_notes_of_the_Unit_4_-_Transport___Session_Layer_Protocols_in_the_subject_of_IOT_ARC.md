# SCTP

SCTP stands for **Stream Control Transmission Protocol**. It is a **transport layer** protocol in the Internet protocol suite that provides reliable and in-sequence data transmission over a connectionless packet network such as IP .

Some of the features and characteristics of SCTP are:

- It supports **multiple streams** of data within a single connection, which allows different types of data to be sent simultaneously without blocking or interleaving .
- It uses **chunks** to encapsulate messages and control information, each with a chunk header that identifies the type, length, and flags of the chunk. A chunk can be either a **data chunk** that contains user data, or a **control chunk** that contains protocol commands or responses.
- It can **fragment** a large message into multiple data chunks, or **bundle** multiple chunks into a single SCTP packet, depending on the network conditions and the maximum transmission unit (MTU) of the underlying network .
- It provides **reliable** data transmission, which means that it ensures that all data chunks are acknowledged by the receiver, and retransmitted if lost or corrupted .
- It provides **ordered** and **unordered** delivery modes, which means that the sender can specify whether the data chunks should be delivered to the receiver in the same order as they were sent, or in any order as long as they belong to the same stream .
- It supports **multihoming**, which means that each endpoint of a connection can have multiple IP addresses, and the protocol can switch between them in case of network failure or congestion .
- It supports **congestion control** and **flow control**, which means that it adjusts the transmission rate and window size according to the network conditions and the receiver's buffer capacity .
- It supports **graceful shutdown**, which means that it allows the endpoints to close the connection in an orderly manner, by exchanging termination chunks and releasing the resources .
- It supports **partial reliability**, which means that it allows the sender to specify a lifetime for each data chunk, and discard the chunk if it is not delivered within the specified time .
- It supports **authentication**, which means that it allows the endpoints to exchange a shared secret key and use it to verify the integrity and origin of the chunks .

SCTP was originally designed to transport **Public Switched Telephone Network (PSTN) signaling messages** over IP networks, but it is capable of broader applications, such as web browsing, streaming media, file transfer, and voice over IP (VoIP)  .