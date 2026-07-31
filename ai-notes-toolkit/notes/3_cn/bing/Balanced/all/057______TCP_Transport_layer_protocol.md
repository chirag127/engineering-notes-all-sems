#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol. It is one of the core protocols of the Internet Protocol Suite, which provides reliable, ordered, and error-checked delivery of data between applications running on hosts connected by a network.
- TCP operates at the transport layer, which is the fourth layer of the OSI model. The transport layer is responsible for providing end-to-end communication services for applications, such as multiplexing, segmentation, flow control, congestion control, and error detection and correction.
- TCP uses a connection-oriented approach, which means that before any data can be exchanged, a TCP connection must be established between the sender and the receiver. A TCP connection is identified by a four-tuple: source IP address, source port number, destination IP address, and destination port number. A port number is a 16-bit number that identifies a specific process or application running on a host.
- TCP uses a three-way handshake to establish a connection. The three steps are:

  - The sender sends a SYN (synchronize) segment to the receiver, which contains the sender's initial sequence number and other parameters, such as window size and maximum segment size.
  - The receiver replies with a SYN-ACK (synchronize-acknowledge) segment, which contains the receiver's initial sequence number and an acknowledgment of the sender's sequence number, as well as other parameters.
  - The sender responds with an ACK (acknowledge) segment, which acknowledges the receiver's sequence number and completes the connection establishment.

- TCP uses a sliding window mechanism to control the flow of data and to ensure reliable delivery. A sliding window is a variable-sized buffer that indicates how much data can be sent or received at any given time. The sender maintains a send window, which indicates how much data it can send before receiving an acknowledgment from the receiver. The receiver maintains a receive window, which indicates how much data it can receive before sending an acknowledgment to the sender. The size of the window can vary depending on the network conditions and the availability of buffer space at both ends.
- TCP uses sequence numbers and acknowledgments to keep track of the data segments that are sent and received. A sequence number is a 32-bit number that identifies the position of a byte in the data stream. An acknowledgment is a 32-bit number that indicates the next expected sequence number from the sender. TCP uses cumulative acknowledgments, which means that an acknowledgment of a sequence number implies that all the previous segments have been received correctly.
- TCP uses a checksum to detect errors in the data segments. A checksum is a 16-bit value that is computed by adding up all the 16-bit words in the segment, including the header and the payload, and taking the one's complement of the result. The checksum is stored in the header of the segment and is verified by the receiver. If the checksum does not match, the segment is discarded and an acknowledgment is not sent.
- TCP uses timers and retransmission to handle lost or corrupted segments. A timer is a value that indicates how long the sender should wait for an acknowledgment before retransmitting a segment. A retransmission is the process of sending a segment again after a timeout or a duplicate acknowledgment. TCP uses various algorithms to adjust the timer and the retransmission strategy, such as exponential backoff, fast retransmit, and fast recovery.
- TCP uses congestion control to avoid overloading the network with too much data. Congestion control is the process of adjusting the sending rate of the sender based on the feedback from the network. TCP uses various algorithms to implement congestion control, such as slow start, congestion avoidance, and congestion recovery. These algorithms use parameters such as congestion window, threshold, and duplicate acknowledgments to determine the optimal sending rate.
- TCP uses flags to indicate the state of the connection and to signal the termination of the connection. A flag is a 1-bit value that is set or cleared in the header of the segment. TCP uses six flags: SYN, ACK, FIN, RST, PSH, and URG. The meanings of these flags are:

  - SYN: used to initiate a connection
  - ACK: used to acknowledge a segment
  - FIN: used to indicate the end of data transmission
  - RST: used to reset a connection
  - PSH: used to indicate that the data should be pushed to the application immediately
  - URG: used to indicate that the data contains urgent information

- TCP uses a four-way handshake to terminate a connection. The four steps are:

  - The sender sends a FIN segment to the receiver, which indicates that it has no more data to send.
  - The receiver replies with an ACK segment, which acknowledges the sender's FIN segment.
  - The receiver sends a FIN segment to the sender