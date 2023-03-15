#### TCP Transport layer protocol

TCP is a transport layer protocol that is used on top of IP to ensure reliable transmission of packets. TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets.

TCP is a connection-oriented protocol, which means that it establishes a connection between the sender and the receiver before transmitting data. TCP uses a three-way handshake to establish a connection, as shown in the following diagram:

![TCP three-way handshake](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/TCP_CLOSE.svg/1200px-TCP_CLOSE.svg.png)

The steps of the three-way handshake are:

- The sender sends a SYN (synchronize) segment to the receiver, with a random sequence number x.
- The receiver sends a SYN-ACK (synchronize-acknowledge) segment to the sender, with a random sequence number y and an acknowledgment number x+1.
- The sender sends an ACK (acknowledge) segment to the receiver, with an acknowledgment number y+1.

After the three-way handshake, the connection is established and data can be exchanged. TCP uses sequence numbers and acknowledgment numbers to keep track of the data segments sent and received. TCP also uses a sliding window mechanism to control the flow of data and avoid congestion. TCP can adjust the size of the window based on the network conditions and the feedback from the receiver.

TCP also provides error detection and correction by using checksums and retransmission. TCP calculates a checksum for each segment and includes it in the header. The receiver verifies the checksum and discards any corrupted segment. TCP also uses timers to detect lost segments and retransmits them until they are acknowledged by the receiver.

TCP is a reliable and robust protocol, but it also has some drawbacks, such as:

- TCP is more complex and requires more resources than UDP, another transport layer protocol that is connectionless and unreliable.
- TCP introduces more overhead and latency than UDP, due to the connection establishment, acknowledgment, and retransmission mechanisms.
- TCP is not suitable for real-time applications that require low latency and high throughput, such as voice and video streaming.