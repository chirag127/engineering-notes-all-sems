### TCP

TCP, or Transmission Control Protocol, is a transport layer protocol used to establish and maintain a reliable connection between two devices on a network. TCP provides a reliable, ordered, and error-checked delivery of data between applications running on hosts.

Here are some important points to remember about TCP:

- TCP is connection-oriented, meaning that it establishes a connection between two devices before data transmission begins.
- TCP uses a three-way handshake to establish a connection between devices. During the handshake, the devices exchange SYN and ACK packets to synchronize the sequence numbers used to identify each packet in the transmission.
- TCP uses a sliding window protocol to ensure reliable delivery of data. The sender sends a packet and waits for an acknowledgement from the receiver before sending the next packet. The receiver acknowledges receipt of each packet, and if a packet is lost, the sender will retransmit it until it is acknowledged.
- TCP provides flow control by using a mechanism called congestion control. If the network becomes congested, TCP will slow down the rate at which it sends packets to avoid overwhelming the network.
- TCP provides reliable delivery of data by using sequence numbers to identify each packet in the transmission. If a packet is lost or damaged in transit, the receiver will request that the sender retransmit it.
- TCP is used by many applications, including web browsers, email clients, and file transfer protocols.

In summary, TCP is an important transport layer protocol that provides reliable, ordered, and error-checked delivery of data between applications running on hosts. Its connection-oriented nature, sliding window protocol, congestion control, and reliable delivery mechanisms make it an essential protocol for many applications on the Internet.