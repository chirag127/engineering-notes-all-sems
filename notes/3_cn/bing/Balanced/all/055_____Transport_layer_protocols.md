### Transport layer protocols

- Transport layer protocols are responsible for providing end-to-end communication between applications on different hosts in a network.
- Transport layer protocols can offer various services such as reliability, flow control, congestion control, multiplexing, error detection, and security.
- The two most common transport layer protocols are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP).

#### TCP

- TCP is a connection-oriented protocol that establishes a logical connection between the sender and the receiver before exchanging data.
- TCP provides reliable data transfer by using sequence numbers, acknowledgments, timers, and retransmission mechanisms to ensure that all data segments are delivered correctly and in order.
- TCP also provides flow control by using a sliding window mechanism to regulate the amount of data that can be sent by the sender at a time, based on the receiver's buffer capacity and network conditions.
- TCP also provides congestion control by using various algorithms to adjust the sender's window size and transmission rate according to the network congestion level, to avoid overwhelming the network and causing packet loss.
- TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate a connection.
- TCP uses port numbers to identify different applications on the same host, and to multiplex and demultiplex data streams.
- TCP is suitable for applications that require reliable and ordered delivery of data, such as web browsing, email, file transfer, and remote login.

#### UDP

- UDP is a connectionless protocol that does not establish a logical connection between the sender and the receiver before exchanging data.
- UDP provides unreliable data transfer by sending data segments without any guarantee of delivery, order, or error detection.
- UDP does not provide any flow control or congestion control mechanisms, and relies on the application layer to handle these issues.
- UDP does not use any handshaking or connection management procedures, and thus has less overhead and latency than TCP.
- UDP also uses port numbers to identify different applications on the same host, and to multiplex and demultiplex data streams.
- UDP is suitable for applications that require fast and real-time delivery of data, such as voice over IP, video streaming, online gaming, and DNS.

#### Comparison of TCP and UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Unreliable |
| Ordering | Ordered | Unordered |
| Error detection | Yes | No |
| Flow control | Yes | No |
| Congestion control | Yes | No |
| Handshaking | Yes | No |
| Overhead | High | Low |
| Latency | High | Low |
| Port numbers | Yes | Yes |
| Applications | Web, email, file transfer, remote login | Voice, video, gaming, DNS |

#### Mnemonics and learning tricks

- To remember the features of TCP and UDP, you can use the following acronyms:

  - TCP: **T**ransport **C**onnection **P**rotocol
  - UDP: **U**nreliable **D**atagram **P**rotocol

- To remember the difference between connection-oriented and connectionless protocols, you can use the following analogy:

  - Connection-oriented protocols are like making a phone call, where you have to dial a number, wait for the other person to answer, and then talk. You also have to say goodbye and hang up when you are done.
  - Connectionless protocols are like sending a postcard, where you just write a message, put a stamp, and drop it in the mailbox. You don't know if the other person will receive it, read it, or reply to it.

- To remember the difference between reliable and unreliable protocols, you can use the following analogy:

  - Reliable protocols are like sending a registered mail, where you get a receipt, a tracking number, and a confirmation of delivery. You can also resend the mail if it gets lost or damaged.
  - Unreliable protocols are like sending a regular mail, where you don't get any receipt, tracking number, or confirmation of delivery. You also don't know if the mail gets lost, damaged, or delivered out of order.