# TCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

- TCP stands for Transmission Control Protocol and it is a transport layer or routing protocol.
- TCP is used to provide reliable, ordered, and error-free data delivery between applications over the Internet .
- TCP works with the Internet Protocol (IP), which is a network layer or adaption layer protocol that handles the routing and addressing of packets.
- TCP has the following features and functions   :
  - TCP guarantees the ordered data delivery by acknowledgment function. It uses sequence numbers and acknowledgments to ensure that all packets are received and in the correct order.
  - TCP retransmits lost packets. It uses timers and retransmission mechanisms to detect and recover from packet loss.
  - TCP helps to control traffic on the Internet. It uses congestion control and flow control algorithms to adjust the sending rate and window size according to the network conditions and the receiver's capacity.
  - TCP supports error control and checksums. It uses a checksum field in the TCP header to detect and discard corrupted packets.
  - TCP supports connection management and state transitions. It uses a three-way handshake to establish and terminate a connection between two endpoints. It also uses flags and state variables to indicate the status of the connection and the direction of data transfer.
  - TCP supports multiplexing and demultiplexing. It uses port numbers to identify different applications or processes on the same host and to deliver packets to the appropriate destination.
- TCP is best suited whenever a program wants to send a lot of data because TCP does fragmentation of data and sends it in the form of small packets.
- TCP is widely used in the Internet of Things (IoT) scenarios where reliability, security, and interoperability are important, such as smart grid, industrial IoT, smart home, and smart city .
- TCP faces some challenges and limitations in the IoT environments, such as constrained-node networks (CNNs), which are characterized by low-power, low-memory, and low-bandwidth devices and links .
- TCP can be optimized and adapted for the IoT scenarios by using lightweight TCP implementations, selective use of optional TCP features, and tuning of TCP parameters and algorithms .