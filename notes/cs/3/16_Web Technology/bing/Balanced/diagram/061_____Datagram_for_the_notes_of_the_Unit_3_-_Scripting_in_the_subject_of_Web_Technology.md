Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is some information about datagram for the notes of Unit 3 - Scripting.

### Datagram
- A datagram is a self-contained unit of data that is transmitted over a network.
- A datagram consists of a header and a payload. The header contains information such as the source and destination addresses, the protocol type, and the length of the payload. The payload contains the actual data to be delivered.
- A datagram is also known as a packet or a message in some contexts.
- A datagram is different from a stream, which is a continuous flow of data that is divided into segments by the sender and reassembled by the receiver.
- A datagram is suitable for applications that require low latency, high reliability, and independence from the underlying network. For example, the User Datagram Protocol (UDP) is a datagram-based protocol that is used for real-time communication, such as voice and video streaming.
- A datagram is also suitable for applications that do not require a connection-oriented service, such as the Transmission Control Protocol (TCP). For example, the Internet Control Message Protocol (ICMP) is a datagram-based protocol that is used for error reporting and diagnostic purposes, such as ping and traceroute.
- A datagram is not guaranteed to be delivered, to be delivered in order, or to be delivered only once. Therefore, the application layer may need to implement error detection, error correction, retransmission, sequencing, and duplicate elimination mechanisms if these features are required.
- A datagram may be fragmented, meaning that it is split into smaller pieces by the network layer if it exceeds the maximum transmission unit (MTU) of the network. The fragments are then reassembled by the receiver. The fragmentation and reassembly process may introduce additional overhead and delay.